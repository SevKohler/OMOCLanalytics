# T3 Fragmentation — scope

Goal: track structural fragmentation in the openEHR to OMOP mapping, to fill Table 3
(`fragmentation`) in the manuscript.

## Idea

Compare the number of archetype nodes against the field count of the OMOP table the
archetype maps to. Any archetype element beyond the table capacity is lost, it has to
be stored elsewhere.

Example: Problem/Diagnosis has 20 elements, the OMOP table it maps against has 10, so
10 elements are lost.

Per archetype:

- archetype nodes vs OMOP target table field count
- surplus (nodes minus fields) = elements lost = auxiliary records needed

## Step 1 — openEHR side (node count per archetype)

Source: the curated archetype tables under
`resources/preparedArchetypeTables/preparedArchetypes/` (one md per archetype, index in
`00_INDEX.md`). This is the vetted list of all 198 archetypes with their nodes and cluster
slots, built from the mapped archetypes by `extract_leaves.py`.

Counting rule:

- each archetype node (data element) counts as 1
- each cluster slot counts as 1
- node count per archetype = elements + cluster slots = the **Leaves** column in `00_INDEX.md`

So every archetype gets one openEHR-side number, its node count.

Machine layer: `extract_leaves.py` now emits `preparedArchetypes/archetypes.csv` next to
`00_INDEX.md`, from the same parse (one row per archetype: `archetype, category, concept,
elements, slots, leaves`). The md is the human view, the CSV is the joinable data the
fragmentation computation reads. Both come from one input so their numbers cannot drift.

### Open question — slotted clusters

A cluster slot is currently counted as a single node (1) and compared against the table
that way. But a slot can hold a whole cluster with many of its own nodes. Those extra
nodes have no field in the target table, so representing them needs auxiliary records
linked by fact_relationship.

TODO (Severin to decide): whether to keep counting a slotted cluster as 1, or to expand
it into its constituent nodes. For now it stays at 1, flagged as an underestimate for the
archetypes that use clusters.

Note (Severin): this is largely covered because clusters are also counted against their
own type. Each cluster archetype has its own mapping to its own OMOP target table and so
appears as its own row in the analysis. Its internal nodes and their fragmentation are
therefore measured there, not lost. Counting the slot as 1 in the parent is then fine, the
slot marks one linking node back to the parent and the cluster's own content is accounted
for in the cluster's own row.

## Step 2 — OMOP side (content concepts per table)

Source: `resources/preparedOMOPTables/`. Each OMOP CDM table that OMOCL targets is reduced
to the content concepts it can actually hold, counted the same way as an archetype leaf.
Redundant columns are collapsed (a `_concept_id` with its `_source_value` and
`_source_concept_id` is one concept) and reference model attributes, record identifiers,
linkage fields and deprecated columns are dropped. What remains is the fair denominator.

These counts are in `preparedOMOPTables/omoptables.csv` (`table, content_concepts, removed`):

| table | content_concepts |
|---|---|
| Measurement | 4 |
| Observation | 5 |
| DrugExposure | 11 |
| ConditionOccurrence | 6 |
| ProcedureOccurrence | 6 |
| Specimen | 7 |
| DeviceExposure | 7 |
| Visit | 6 |
| Person | 4 |
| Death | 3 |

Note: the measured calculation in Step 3 does not consume these counts, it reads the actual
mappings. `omoptables.csv` is kept as the reference denominator (how much each table could
hold) and as context for the per-field view. It is currently transcribed from the generated
`preparedOMOPTables` README, wiring it to a generator is optional and still pending.

## Step 3 — the calculation (fragmentation.py)

`fragmentation.py` is the single executable calculation. One run reproduces everything:

```
python fragmentation.py
```

It measures fragmentation per leaf, no estimation. For every archetype it reads the prepared
leaves and the OMOCL mapping, and matches each leaf to the mapping by its at-code. Each leaf
ends in one of three states:

- mapped to the primary OMOP table, a direct home (the OMOP field is recorded)
- externalised to another OMOP table, already an auxiliary record in a split mapping
- not mapped, no mapping at all, needs a fact_relationship to be represented

Fragmentation is the leaves not in the primary table (externalised plus not mapped), each of
which needs an auxiliary record linked by fact_relationship.

The primary table is the first `- type:` block in the mapping YAML. A mapping path that dives
into a plugged cluster (`items[openEHR-EHR-CLUSTER.x.v1]/...`) is credited to the parent slot
leaf that accepts that cluster. The cluster's own inner nodes are counted in the cluster's own
row, not here, so nothing is double counted.

Why measured and not the earlier capacity estimate: the estimate (leaves vs table size) only
caps covered at the table capacity, so it claims 6 direct fields for Problem/Diagnosis where
only 4 are actually mapped. The per-leaf measurement is what the mapping really does, it
matches the manuscript's by-hand worked example, and every number is auditable in the
per-archetype files. The estimate was dropped.

Data layer: `preparedArchetypeTables/preparedArchetypes/leaves.csv`, one row per leaf
(`archetype, code, kind, label, value_type, allowed`), emitted by `extract_leaves.py` from the
same parse as the md files.

Outputs:

- `resources/<archetype>.md`, one file per archetype, every leaf mapped or not,
  with the OMOP field it maps to.
- `resources/README.md`, the index of those files.
- `resources/fragmentation.csv`, one row per archetype
  (`archetype, concept, primary_table, leaves, mapped_primary, externalised, not_mapped,
  auxiliary, source`).
- a printed Table 3 summary.

### Result (all 198 archetypes, 2289 leaves)

- mapped to the primary table: 293 (12.8%)
- auxiliary, needs fact_relationship: 1996 (87.2%), of which 85 externalised and 1911 not mapped
- archetypes needing at least one auxiliary record: 187 of 198 (94.4%)

Verified anchor, Problem/Diagnosis: 16 leaves, 4 mapped (name, onset, resolution, status), 12
auxiliary. This matches the manuscript's by-hand analysis exactly.

## Status

Done, end to end, from one script. `fragmentation.py` writes `resources/fragmentation.csv` and
the per-archetype `resources/*.md` files from one shared per-leaf function, and prints the
Table 3 totals. Open items: decide the caveat wording for auxiliary leaves (no OMOP field vs
simply not mapped), optionally wire `omoptables.csv` to a generator, and confirm the
first-type-is-primary rule for the 12 split mappings.

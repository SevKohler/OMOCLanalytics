# OMOCL analytics

Analytics for the paper *Bridging openEHR and OMOP: Expanded Mappings and Systematic
Analysis of Semantic and Structural Limitations in the OMOP CDM*.

This repository holds the prepared data and scripts used to measure the openEHR to OMOP
mapping loss, so the figures in the paper can be reproduced and audited.

## Contents

### Prepared data

- `resources/preparedArchetypeTables/` — the archetype side of the comparison: the leaf
  inventory (data ELEMENTs + CLUSTER slots) extracted from the mapped archetypes, plus the
  scripts that build and verify it (`extract_leaves.py`, `qa_leaves.py`).
- `resources/preparedOMOPTables/` — the OMOP CDM side: the content concepts each OMOP
  table can hold, counted the same way, to give a fair denominator.
- `resources/OMOCL mappings/` — the OMOCL archetype-to-CDM mappings the analysis is based on.

### Analytics

One folder per artefact in the paper. Each script is standalone, reads only the prepared
data above, hardcodes no result, and prints its numbers when run. Each explains its method
in its own docstring; run it and the figure is reproduced.

| Folder | Produces | Script |
|---|---|---|
| `Figure4Domains/` | Figure 4, distribution of mapped archetypes across OMOP CDM domains | `domain_distribution.py` |
| `Table2ConceptIds/` | Table 2, distribution of OMOP concept_id mapping properties, plus the conceptMap zero-coverage answer to the Section 3.3 reviewer point | `concept_id_properties.py`, `conceptmap_zeros.py` |
| `T3Fragementation/` | Table 3, structural fragmentation measured per leaf | `fragmentation.py` |
| `T3Overloading/` | Table 3, semantic field overloading (one OMOP field fed by several distinct archetype nodes) | `overloading.py` |
| `LeafCapacityComparison/` | The size comparison behind the fragmentation result: archetype nodes against the content fields of their target table, and the arithmetic floor this puts under the measured fragmentation | `leaf_capacity_comparison.py` |

Requires Python 3.7+ and PyYAML. `LeafCapacityComparison` reads `T3Fragementation`'s output,
so run `T3Fragementation/fragmentation.py` first; the others are independent of each other.

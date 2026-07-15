# Structural fragmentation of the openEHR to OMOP mapping (Table 3 in the manuscript).
#
# This is the single, executable calculation. Run it and everything is reproduced:
#   python fragmentation.py
#
# The calculation compares TWO sources, kept clearly apart in the code below:
#
#   ARCHETYPE SIDE  what openEHR defines: every leaf of every archetype.
#                   Read from the generated leaves.csv / archetypes.csv.
#   OMOCL SIDE      what actually gets written to OMOP: the OMOCL mapping of each archetype.
#                   Read straight from the mapping YAML files.
#
# Method (measured, per leaf, no estimation):
#   For every archetype we take its leaves (archetype side) and its mapping (OMOCL side) and
#   match each leaf to the mapping by its at-code. Each leaf ends in one of three states:
#       mapped to the primary OMOP record   a direct home (the OMOP field is recorded)
#       externalised to a separate record   another instance of the SAME table, or a different
#                                           table; either way a separate OMOP record, already split off
#       not mapped                          the at-code is nowhere in the mapping, needs fact_rel
#   The primary OMOP record is the first `- type:` block. An archetype often emits several
#   records of the same table (e.g. Obstetric_summary -> 12 Measurement records); a leaf in
#   any record after the first is externalised, because that record still needs its own
#   fact_relationship back to the primary. So "externalised" means "a separate OMOP record",
#   NOT necessarily a different table (only some are).
#   Fragmentation = the leaves not in the primary record (externalised + not mapped), each of
#   which requires an auxiliary record linked by a fact_relationship.
#
#   A mapping path that dives into a plugged cluster (items[openEHR-EHR-CLUSTER.x.v1]/...) is
#   credited to the parent SLOT leaf that accepts that cluster. The cluster's own inner nodes
#   belong to that cluster's own row, so they are not double counted here.
#
# Inputs:
#   ARCHETYPE SIDE  ../resources/preparedArchetypeTables/preparedArchetypes/leaves.csv
#                   ../resources/preparedArchetypeTables/preparedArchetypes/archetypes.csv
#   OMOCL SIDE      ../resources/OMOCL mappings/{medical_data,person_data}/**/*.yml
#
# Outputs (this analysis's own resources/ folder):
#   resources/<archetype>.md      one file per archetype, every leaf mapped or not
#   resources/README.md           index of the per-archetype files
#   resources/fragmentation.csv   one row per archetype with the counts
#   printed summary               the Table 3 totals
import csv
import collections
import glob
import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
RESOURCES = os.path.join(HERE, "..", "resources")

# ARCHETYPE-side inputs (what openEHR defines)
PREPARED = os.path.join(RESOURCES, "preparedArchetypeTables", "preparedArchetypes")
LEAVES_CSV = os.path.join(PREPARED, "leaves.csv")
ARCHETYPES_CSV = os.path.join(PREPARED, "archetypes.csv")
# OMOCL-side input (what gets written to OMOP)
MAPPINGS_DIR = os.path.join(RESOURCES, "OMOCL mappings")
# outputs (this analysis's own resources/ folder)
OUTPUT_DIR = os.path.join(HERE, "resources")
COVERAGE_DIR = OUTPUT_DIR   # coverage files land directly in resources/
FRAGMENTATION_CSV = os.path.join(OUTPUT_DIR, "fragmentation.csv")

DIAGNOSIS = "openEHR-EHR-EVALUATION.problem_diagnosis.v1"   # the worked example / anchor

# OMOCL directives that read like a block (`- type:`) but are not OMOP target tables:
#   Include        plugs another archetype's mapping in at a base_path (the linked cluster
#                  becomes its own OMOP record and owes a fact_relationship back).
#   CustomMapping  a converter (e.g. FactRelationshipCustomConverter), no OMOP fields.
# They carry no `path:` fields, so skipping them changes no leaf count; it only stops a
# delegating archetype (device_summary.v0, laboratory_test_result.v1) from reporting a
# nonsense primary table of "Include". Its leaves stay auxiliary (each needs a fact_rel).
NON_TABLE_TYPES = frozenset({"Include", "CustomMapping"})

# Patterns for reading an OMOCL mapping YAML.
ARCHETYPE_LINE = re.compile(r'archetype:\s*(\S+)')
TYPE_LINE = re.compile(r'^\s*-\s*type:\s*"?([A-Za-z][A-Za-z0-9_]*)')  # start of a block; full table name (no truncation on _ / digits)
FIELD_LINE = re.compile(r'^(?:\s{4}|\t{2})([a-z][a-z0-9_]+):\s*$')   # an OMOP target field name
PATH_LINE = re.compile(r'path:\s*"([^"]*)"')
ITEMS_TOKEN = re.compile(r'items\[([^\]]+)\]')                  # each items[...] token inside a path
BASE_ARCHETYPE_ID = re.compile(r'openEHR-EHR-[A-Z_]+\.[a-z0-9_]+')   # archetype id without version/variant

# An OMOCL mapping parsed into blocks; a block is one OMOP target table with its fields.
Field = collections.namedtuple("Field", "name paths")          # e.g. value -> [path, ...]
Block = collections.namedtuple("Block", "table fields")        # e.g. Measurement -> [Field, ...]
# Where the mapping sends one leaf: an OMOP field on a table, in the primary block or not.
Binding = collections.namedtuple("Binding", "omop_field omop_table is_primary")


# ================================================================================
# ARCHETYPE SIDE  -  the prepared leaves (what openEHR defines)
# ================================================================================

def read_prepared_leaves():
    """archetype id -> ordered list of leaf dicts {code, kind, label, allowed, group, ...}.

    From leaves.csv, the vetted inventory of every archetype's data elements and cluster slots.
    """
    leaves = collections.OrderedDict()
    with open(LEAVES_CSV, encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            leaves.setdefault(row["archetype"], []).append(row)
    return leaves


def read_archetype_concepts():
    """archetype id -> human concept label (used only to make the output readable)."""
    with open(ARCHETYPES_CSV, encoding="utf-8") as handle:
        return {row["archetype"]: row["concept"] for row in csv.DictReader(handle)}


# ================================================================================
# OMOCL SIDE  -  the mappings (what actually gets written to OMOP)
# ================================================================================

def omocl_mapping_files():
    """Every OMOCL mapping YAML (medical_data + person_data, tests excluded)."""
    found = (glob.glob(os.path.join(MAPPINGS_DIR, "medical_data", "**", "*.yml"), recursive=True)
             + glob.glob(os.path.join(MAPPINGS_DIR, "person_data", "**", "*.yml"), recursive=True))
    return sorted(f for f in found if os.sep + "tests" + os.sep not in f)


def read_omocl_mapping(path):
    """Parse one OMOCL mapping YAML in a single pass into (archetype id, [Block, ...]).

    A Block is an OMOP target table (`- type:`) holding its Fields (`value`, `concept_id`, ...),
    each Field holding the archetype paths that fill it. The first Block is the primary table.
    """
    archetype = None
    blocks = []
    field = None
    for line in open(path, encoding="utf-8"):
        if archetype is None:
            found = ARCHETYPE_LINE.search(line)
            if found:
                archetype = found.group(1).strip().strip('"')

        new_block = TYPE_LINE.match(line)
        if new_block:
            field = None
            if new_block.group(1) not in NON_TABLE_TYPES:   # an OMOP table, not an Include/Custom directive
                blocks.append(Block(new_block.group(1), []))
            continue
        if not blocks:
            continue

        new_field = FIELD_LINE.match(line)
        if new_field:
            field = Field(new_field.group(1), [])
            blocks[-1].fields.append(field)
            continue

        path_value = PATH_LINE.search(line)
        if path_value:
            if field is not None:
                field.paths.append(path_value.group(1))
            elif "base_path:" not in line:
                # A real `path:` under a table block but with no active field means FIELD_LINE
                # missed the field name above it (indentation is not 4-space / 2-tab as assumed).
                # Fail loudly: silently dropping it would over-count "not mapped".
                raise ValueError(
                    "%s: a 'path:' has no field above it, so FIELD_LINE missed a field "
                    "(non-standard indentation?): %r" % (os.path.basename(path), line.strip()))
    return archetype, blocks


# ================================================================================
# MATCH  -  archetype leaves against OMOCL mapping paths, by at-code
# ================================================================================

def leaf_touched_by(mapping_path, element_codes, slot_codes, slots):
    """The archetype leaf a single OMOCL path refers to, or None for a context/constant path.

    A direct element or slot at-code matches itself. A path that reaches into a plugged
    cluster (its id appears as an items[...] token) is credited to the slot that accepts it,
    and stops there: at-codes deeper in the path belong to the plugged cluster, not to this
    archetype (they are counted on the cluster's own row), so they must not steal the credit.
    Without this, a cluster-internal items[at0144] that collides with a same-named parent
    at-code would be mis-credited (at-codes are unique only within one archetype).
    """
    touched = None
    for token in ITEMS_TOKEN.findall(mapping_path):
        if "openEHR-EHR-" in token:
            cluster = set(BASE_ARCHETYPE_ID.findall(token))
            for slot_code, accepted_clusters in slots:
                if cluster & accepted_clusters:
                    touched = slot_code
            break   # entered a plugged cluster: everything after belongs to it
        if token in element_codes or token in slot_codes:
            touched = token
    return touched


def searchable_leaf_codes(leaves):
    """The three things we match a mapping path against for one archetype.

    Returns (element_codes, slot_codes, slots):
      element_codes  set of element at-codes
      slot_codes     set of slot at-codes
      slots          [(slot at-code, {cluster ids that slot accepts})], for cluster-dive paths
    """
    element_codes = {leaf["code"] for leaf in leaves if leaf["kind"] == "element"}
    slots = [(leaf["code"], set(BASE_ARCHETYPE_ID.findall(leaf["allowed"] or "")))
             for leaf in leaves if leaf["kind"] == "slot"]
    slot_codes = {code for code, _ in slots}
    return element_codes, slot_codes, slots


def iter_mapping_writes(blocks):
    """Flatten one mapping into every (omop_field, omop_table, is_primary, mapping_path).

    A mapping is a list of OMOP tables (blocks); table 0 is the primary one, later tables are
    auxiliary. Each table fills several OMOP fields, and each field is filled from one or more
    archetype paths. This yields one entry per path so callers do not repeat the triple loop.
    """
    for table_index, block in enumerate(blocks):
        is_primary = table_index == 0
        for field in block.fields:
            for mapping_path in field.paths:
                yield field.name, block.table, is_primary, mapping_path


def bindings_by_leaf(leaves, blocks):
    """For each archetype leaf, list every OMOP field the mapping writes it to.

    Returns {leaf at-code: [Binding, ...]}. A leaf that appears nowhere in the mapping is
    simply absent from the result, which the caller reads as "not mapped".

    leaves = the archetype side (the at-codes we search for).
    blocks = the OMOCL side (the mapping, parsed into OMOP tables -> fields -> paths).
    """
    element_codes, slot_codes, slots = searchable_leaf_codes(leaves)

    bindings = collections.defaultdict(list)   # leaf at-code -> [Binding, ...]
    for omop_field, omop_table, is_primary, mapping_path in iter_mapping_writes(blocks):
        leaf_code = leaf_touched_by(mapping_path, element_codes, slot_codes, slots)
        if leaf_code is None:
            continue   # the path points at context or a constant, not a leaf
        binding = Binding(omop_field, omop_table, is_primary)
        if binding not in bindings[leaf_code]:   # avoid listing the same target twice
            bindings[leaf_code].append(binding)
    return bindings


def classify_leaves(leaves, blocks):
    """Sort the archetype's leaves into the three coverage buckets.

    Returns (mapped_primary, externalised, not_mapped); each is a list of (leaf, [Binding]).
    """
    bindings = bindings_by_leaf(leaves, blocks)
    mapped_primary, externalised, not_mapped = [], [], []
    for leaf in leaves:
        found = bindings.get(leaf["code"], [])
        primary = [binding for binding in found if binding.is_primary]
        if primary:
            mapped_primary.append((leaf, primary))
        elif found:
            externalised.append((leaf, found))
        else:
            not_mapped.append((leaf, []))
    return mapped_primary, externalised, not_mapped


# ================================================================================
# RENDER  -  the per-archetype coverage file
# ================================================================================

def format_bindings(bindings):
    return ", ".join("`%s` @ %s" % (b.omop_field, b.omop_table) for b in bindings)


def leaf_name(leaf):
    """The leaf label, prefixed with its internal cluster so repeated labels stay distinct.

    A leaf inside a grouping cluster (e.g. three "Factor" leaves under Modifying/Precipitating/
    Resolving factor) would otherwise be indistinguishable in the "not mapped" list.
    """
    group = (leaf.get("group") or "").strip()
    return "%s > %s" % (group, leaf["label"]) if group else leaf["label"]


def leaf_rows(bucket, with_field):
    """Markdown table rows for one bucket, or a placeholder when it is empty."""
    if not bucket:
        return ["_None._"]
    if with_field:
        lines = ["| Code | Kind | Leaf | OMOP field |", "|------|------|------|------------|"]
        lines += ["| %s | %s | %s | %s |" % (leaf["code"], leaf["kind"], leaf_name(leaf),
                                             format_bindings(bindings))
                  for leaf, bindings in bucket]
    else:
        lines = ["| Code | Kind | Leaf |", "|------|------|------|"]
        lines += ["| %s | %s | %s |" % (leaf["code"], leaf["kind"], leaf_name(leaf))
                  for leaf, _ in bucket]
    return lines


def render_archetype(archetype, concept, primary_table, buckets):
    mapped_primary, externalised, not_mapped = buckets
    lines = [
        "# %s" % archetype, "",
        "**Concept:** %s" % concept, "",
        "**Primary OMOP table:** %s  |  **Leaves:** %d  |  **Mapped to primary:** %d  "
        "|  **Externalised to a separate record:** %d  |  **Not mapped (auxiliary):** %d"
        % (primary_table, len(mapped_primary) + len(externalised) + len(not_mapped),
           len(mapped_primary), len(externalised), len(not_mapped)),
        "", "## Mapped to the primary record", "",
        *leaf_rows(mapped_primary, with_field=True),
        "", "## Auxiliary — externalised to a separate OMOP record "
        "(another instance of the same table, or a different table; see the OMOP field column)", "",
        *leaf_rows(externalised, with_field=True),
        "", "## Auxiliary — not mapped (needs a fact_relationship)", "",
        *leaf_rows(not_mapped, with_field=False),
        "",
    ]
    return "\n".join(lines)


# ================================================================================
# DRIVE  -  run the calculation and write every output
# ================================================================================

def analyse_all():
    """Match every archetype's leaves against its OMOCL mapping, write the per-archetype files,
    and return one summary row per archetype."""
    os.makedirs(COVERAGE_DIR, exist_ok=True)
    prepared_leaves = read_prepared_leaves()          # archetype side
    concepts = read_archetype_concepts()              # archetype side
    canonical_id = {a.lower(): a for a in prepared_leaves}   # a few mapping ids differ in case

    rows = []
    unmatched = []                                     # mapping files whose archetype is not in leaves.csv
    for mapping_file in omocl_mapping_files():         # OMOCL side, one archetype's mapping
        mapping_archetype_id, blocks = read_omocl_mapping(mapping_file)
        archetype = canonical_id.get((mapping_archetype_id or "").lower())
        if archetype is None:
            unmatched.append((os.path.basename(mapping_file), mapping_archetype_id))
            continue

        leaves = prepared_leaves[archetype]            # archetype side: the leaves to account for
        concept = concepts.get(archetype, "")
        primary_table = blocks[0].table if blocks else "-"
        buckets = classify_leaves(leaves, blocks)      # match archetype leaves vs OMOCL paths
        mapped_primary, externalised, not_mapped = buckets

        markdown = render_archetype(archetype, concept, primary_table, buckets)
        with open(os.path.join(COVERAGE_DIR, archetype + ".md"), "w", encoding="utf-8") as out:
            out.write(markdown)

        rows.append({
            "archetype": archetype, "concept": concept, "primary_table": primary_table,
            "leaves": len(leaves), "mapped_primary": len(mapped_primary),
            "externalised": len(externalised), "not_mapped": len(not_mapped),
            "auxiliary": len(externalised) + len(not_mapped),
            "source": os.path.relpath(mapping_file, MAPPINGS_DIR).replace(os.sep, "/"),
        })
    rows.sort(key=lambda row: row["archetype"])

    # Coverage invariant: every prepared archetype maps exactly once, nothing silently dropped.
    mapped_once = collections.Counter(row["archetype"] for row in rows)
    duplicated = sorted(a for a, n in mapped_once.items() if n > 1)
    missing = sorted(set(prepared_leaves) - set(mapped_once))
    problems = []
    if missing:
        problems.append("%d prepared archetype(s) have no mapping: %s" % (len(missing), missing))
    if duplicated:
        problems.append("%d archetype(s) mapped by more than one file: %s" % (len(duplicated), duplicated))
    if unmatched:
        problems.append("%d mapping file(s) match no prepared archetype: %s" % (len(unmatched), unmatched))
    if problems:
        raise ValueError("fragmentation coverage check failed:\n  " + "\n  ".join(problems))
    return rows


def write_fragmentation_csv(rows):
    columns = ["archetype", "concept", "primary_table", "leaves", "mapped_primary",
               "externalised", "not_mapped", "auxiliary", "source"]
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=columns, lineterminator="\n", extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)
    with open(FRAGMENTATION_CSV, "w", encoding="utf-8") as out:
        out.write(buffer.getvalue())


def write_coverage_index(rows):
    lines = [
        "# Mapping coverage per archetype", "",
        "One file per archetype. Each lists every prepared leaf as mapped to the primary OMOP "
        "record, externalised to a separate OMOP record (another instance of the same table, or a "
        "different table), or not mapped (auxiliary / fact_relationship).",
        "", "| Archetype | Primary table | Leaves | Mapped | Externalised (sep. record) | Not mapped |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append("| [%s](%s.md) | %s | %d | %d | %d | %d |"
                     % (row["archetype"], row["archetype"], row["primary_table"], row["leaves"],
                        row["mapped_primary"], row["externalised"], row["not_mapped"]))
    totals = {key: sum(row[key] for row in rows)
              for key in ("leaves", "mapped_primary", "externalised", "not_mapped")}
    lines.append("| **total (%d)** | | **%d** | **%d** | **%d** | **%d** |"
                 % (len(rows), totals["leaves"], totals["mapped_primary"],
                    totals["externalised"], totals["not_mapped"]))
    lines.append("")
    with open(os.path.join(COVERAGE_DIR, "README.md"), "w", encoding="utf-8") as out:
        out.write("\n".join(lines))


def print_summary(rows):
    archetypes = len(rows)
    leaves = sum(row["leaves"] for row in rows)
    mapped = sum(row["mapped_primary"] for row in rows)
    externalised = sum(row["externalised"] for row in rows)
    not_mapped = sum(row["not_mapped"] for row in rows)
    auxiliary = externalised + not_mapped
    fragmented = sum(1 for row in rows if row["auxiliary"] > 0)

    print("=" * 70)
    print("STRUCTURAL FRAGMENTATION  (Table 3, measured per leaf)")
    print("=" * 70)
    print("archetypes                    : %d" % archetypes)
    print("leaf elements                 : %d" % leaves)
    print("  mapped to primary record    : %d  (%.1f%%)" % (mapped, 100.0 * mapped / leaves))
    print("  auxiliary (needs fact_rel)  : %d  (%.1f%%)" % (auxiliary, 100.0 * auxiliary / leaves))
    print("    externalised (sep. record): %d" % externalised)
    print("    not mapped at all         : %d" % not_mapped)
    print("archetypes needing >=1 aux    : %d of %d  (%.1f%%)"
          % (fragmented, archetypes, 100.0 * fragmented / archetypes))

    diagnosis = next((row for row in rows if row["archetype"] == DIAGNOSIS), None)
    if diagnosis:
        print("anchor  Problem/Diagnosis      : leaves=%d mapped=%d auxiliary=%d  "
              "(hand analysis: 4 direct, 12 aux)"
              % (diagnosis["leaves"], diagnosis["mapped_primary"], diagnosis["auxiliary"]))
    print("\nwrote resources/fragmentation.csv + resources/*.md (%d files)" % archetypes)


def main():
    rows = analyse_all()
    write_fragmentation_csv(rows)
    write_coverage_index(rows)
    print_summary(rows)


if __name__ == "__main__":
    main()

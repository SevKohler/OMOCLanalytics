# Semantic field overloading of the openEHR to OMOP mapping (Table 3 in the manuscript).
#
# Run it and the count is reproduced:
#   python overloading.py
#
# WHAT IS MEASURED
# ----------------
# Field overloading = one OMOP field carrying several distinct clinical qualifiers.
# Measurement rule: count the OMOP fields that are fed by two or more DISTINCT
# archetype source paths, i.e. two genuinely different archetype nodes routed into
# the same OMOP column. Fallback values are NOT distinct sources and are excluded:
#     - code:  ...            a constant OMOP concept fallback (a coding, not a path)
#     - reference-model paths ".", "..", "../context", "../../", ...  (RM context/self,
#                             not an archetype data node)
# A field whose alternatives are one real path plus a code, or one real path plus an
# RM-context fallback, is therefore NOT overloaded. Only >=2 different archetype
# paths count, exactly the case the manuscript means by "several source elements
# other than fallback values".
#
# The OMOCL `alternatives:` list is an ordered fallback chain, so >=2 archetype paths
# means the one OMOP column must accept content from two different clinical elements.
#
# Reads the mappings with a real YAML parser so that YAML anchors (&x / *x, one path
# block reused across several fields) are expanded correctly.
#
# Inputs:
#   ../resources/OMOCL mappings/{medical_data,person_data}/**/*.yml
# Outputs (this analysis's own resources/ folder):
#   resources/overloading.csv   one row per overloaded (field, mapping)
#   resources/README.md         human-readable listing, grouped by archetype
#   printed summary             the Table 3 overloading count
import csv
import collections
import glob
import io
import os
import re

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
# Input: the shared mapping library at the repository root.
MAPPINGS_DIR = os.path.join(HERE, "..", "resources", "OMOCL mappings")
# Output: this analysis's own resources/ folder.
OUTPUT_DIR = os.path.join(HERE, "resources")
OVERLOAD_CSV = os.path.join(OUTPUT_DIR, "overloading.csv")
COVERAGE_DIR = OUTPUT_DIR   # coverage files land directly in resources/

# A distinct clinical source is a path that TERMINATES in a data-element node, i.e. its
# last segment is items[...] (or the single "itmes[...]" typo in the library). A path that
# ends in a structural container instead, events[...] (the event node = reference-model
# event time), data[...] or activities[...], or a pure reference-model path (".", "..",
# "../context", "../../"), is a fallback/context source, not a distinct data element, and
# is excluded, matching the rule "several source elements other than fallback values".
DATA_LEAF_PATH = re.compile(r'(?:items|itmes)\[[^\]]*\]\s*$')

# `- type:` blocks that are OMOCL directives, not OMOP target tables (same exclusion as
# fragmentation.py): Include plugs in another archetype's mapping, CustomMapping is a
# converter. Neither is an OMOP field owner, so they cannot be overloaded.
NON_TABLE_TYPES = frozenset({"Include", "CustomMapping"})

Overload = collections.namedtuple("Overload", "archetype table field paths")


def mapping_files():
    """Every OMOCL mapping YAML (medical_data + person_data, tests excluded)."""
    found = (glob.glob(os.path.join(MAPPINGS_DIR, "medical_data", "**", "*.yml"), recursive=True)
             + glob.glob(os.path.join(MAPPINGS_DIR, "person_data", "**", "*.yml"), recursive=True))
    return sorted(f for f in found if os.sep + "tests" + os.sep not in f)


def is_archetype_path(value):
    """True if a path terminates in a data-element node, not RM context / a structural node."""
    return isinstance(value, str) and bool(DATA_LEAF_PATH.search(value))


def alternative_paths(alternatives):
    """The distinct archetype paths listed as alternatives for one OMOP field.

    `alternatives` is the YAML list under a field. Each entry is a dict; we keep only
    the `path` entries that name an archetype node and drop `code` fallbacks and any
    reference-model context path. Order is preserved, duplicates removed.
    """
    distinct = []
    if not isinstance(alternatives, list):
        return distinct
    for entry in alternatives:
        if not isinstance(entry, dict):
            continue
        path = entry.get("path")
        if is_archetype_path(path) and path not in distinct:
            distinct.append(path)
    return distinct


def archetype_id(doc):
    spec = (doc or {}).get("spec", {}) or {}
    cfg = spec.get("openEhrConfig", {}) or {}
    return cfg.get("archetype", "")


def overloaded_fields(doc):
    """Every (table, field, paths) in one mapping where a field is fed by >=2 archetype paths."""
    hits = []
    for block in (doc or {}).get("mappings", []) or []:
        if not isinstance(block, dict):
            continue
        table = block.get("type", "?")
        if table in NON_TABLE_TYPES:
            continue
        for field_name, spec in block.items():
            if field_name == "type" or not isinstance(spec, dict):
                continue
            paths = alternative_paths(spec.get("alternatives"))
            if len(paths) >= 2:
                hits.append((table, field_name, paths))
    return hits


def analyse():
    rows = []
    for path in mapping_files():
        with open(path, encoding="utf-8") as handle:
            try:
                doc = yaml.safe_load(handle)
            except yaml.YAMLError as error:
                print("  skipped (YAML error): %s  (%s)" % (os.path.basename(path), error))
                continue
        arch = archetype_id(doc)
        for table, field, paths in overloaded_fields(doc):
            rows.append(Overload(arch, table, field, paths))
    # One OMOP field counts once even if it recurs identically across mapping blocks.
    seen, unique = set(), []
    for r in rows:
        key = (r.archetype, r.table, r.field, tuple(r.paths))
        if key not in seen:
            seen.add(key)
            unique.append(r)
    unique.sort(key=lambda r: (r.archetype, r.table, r.field))
    return unique


def write_csv(rows):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(["archetype", "omop_table", "omop_field", "n_paths", "paths"])
    for r in rows:
        writer.writerow([r.archetype, r.table, r.field, len(r.paths), " | ".join(r.paths)])
    with open(OVERLOAD_CSV, "w", encoding="utf-8") as out:
        out.write(buffer.getvalue())


def write_coverage(rows):
    os.makedirs(COVERAGE_DIR, exist_ok=True)
    by_arch = collections.OrderedDict()
    for r in rows:
        by_arch.setdefault(r.archetype, []).append(r)
    lines = [
        "# Field overloading per archetype", "",
        "Every OMOP field fed by two or more DISTINCT archetype source paths "
        "(constant `code` fallbacks and reference-model context paths excluded).",
        "", "Overloaded fields: **%d** across **%d** archetype mappings."
        % (len(rows), len(by_arch)), "",
    ]
    for arch, items in by_arch.items():
        lines.append("## %s" % arch)
        lines.append("")
        lines.append("| OMOP table | OMOP field | # paths | Archetype paths |")
        lines.append("|---|---|---|---|")
        for r in items:
            lines.append("| %s | %s | %d | %s |"
                         % (r.table, r.field, len(r.paths),
                            "<br>".join("`%s`" % p for p in r.paths)))
        lines.append("")
    with open(os.path.join(COVERAGE_DIR, "README.md"), "w", encoding="utf-8") as out:
        out.write("\n".join(lines))


def print_summary(rows):
    mappings = len({r.archetype for r in rows})
    tables = collections.Counter(r.table for r in rows)
    print("=" * 70)
    print("FIELD OVERLOADING  (Table 3, measured per OMOP field)")
    print("=" * 70)
    print("overloaded OMOP fields (>=2 distinct archetype paths) : %d" % len(rows))
    print("archetype mappings that contain at least one          : %d" % mappings)
    print("\nby OMOP target table:")
    for table, count in tables.most_common():
        print("  %-22s : %d" % (table, count))
    print("\nwrote resources/overloading.csv + resources/README.md")


def main():
    rows = analyse()
    write_csv(rows)
    write_coverage(rows)
    print_summary(rows)


if __name__ == "__main__":
    main()

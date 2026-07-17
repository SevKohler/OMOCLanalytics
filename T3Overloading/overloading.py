# Semantic field overloading of the openEHR to OMOP mapping (Table 3 in the manuscript).
#
# Run it and the numbers are reproduced:
#   python overloading.py
#
# WHAT IS MEASURED
# ----------------
# An OMOP field is OVERLOADED when, in at least one archetype mapping, it is fed by two or
# more DISTINCT source paths. Source paths are the `path:` alternatives OMOCL lists for the
# field. Two kinds of alternative are not source paths and are excluded:
#     - a constant `code:` value  (a fixed OMOP concept, not data drawn from the archetype)
#     - a conceptMap's path, which is nested inside the conceptMap object where this parser
#       cannot read it (a KNOWN BLIND SPOT, reported below, can only lower the count)
# Reference-model paths (".", "..", "../context", "events[...]") ARE counted. openEHR gives
# no single canonical event time, so an OMOP date fed by the event time and by the record
# context time genuinely holds different things in different records: that is overloading.
#
# THE HEADLINE IS A FIELD-LEVEL RATE
# ----------------------------------
# We report distinct OMOP fields: N of M fields the library maps into are overloaded in at
# least one mapping. Overloading is a structural property of the OMOP schema, so the unit is
# the field, counted once, independent of how often the library happens to write it.
#
# The per-write frequency (how many individual field-writes are overloaded) is printed as a
# SECONDARY figure and is deliberately NOT the headline: it is dominated by a few very
# high-frequency date fields, so it reflects this library's archetype mix more than the CDM.
#
# Inputs:
#   ../resources/OMOCL mappings/{medical_data,person_data}/**/*.yml
# Outputs (this analysis's own resources/ folder):
#   resources/overloading.csv   one row per overloaded (archetype, field, paths)
#   resources/README.md         human-readable listing, grouped by archetype
#   printed summary             the Table 3 overloading numbers
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

# `- type:` blocks that are OMOCL directives, not OMOP target tables: Include plugs in another
# archetype's mapping, CustomMapping is a converter. Neither owns an OMOP field.
NON_TABLE_TYPES = frozenset({"Include", "CustomMapping"})

# A path ending in items[...] terminates in a real data element (the "itmes" typo occurs once
# in the library). Used only to describe WHAT an overloaded field's sources are, never to
# decide whether it is overloaded.
DATA_ELEMENT_PATH = re.compile(r'(?:items|itmes)\[[^\]]*\]\s*$')

# One overloaded field, as one archetype maps it: the archetype, the OMOP table and field, and
# the distinct source paths competing for that single field.
Overload = collections.namedtuple("Overload", "archetype table field paths")


def mapping_files():
    """Every OMOCL mapping YAML (medical_data + person_data, tests excluded)."""
    found = (glob.glob(os.path.join(MAPPINGS_DIR, "medical_data", "**", "*.yml"), recursive=True)
             + glob.glob(os.path.join(MAPPINGS_DIR, "person_data", "**", "*.yml"), recursive=True))
    return sorted(f for f in found if os.sep + "tests" + os.sep not in f)


def archetype_id(doc):
    spec = (doc or {}).get("spec", {}) or {}
    cfg = spec.get("openEhrConfig", {}) or {}
    return cfg.get("archetype", "")


def source_paths(alternatives):
    """The distinct source paths OMOCL lists for one OMOP field.

    A source path is a top-level `path:` alternative. A `code:` alternative is a constant
    concept, not a source path. A conceptMap alternative carries its path nested inside itself
    and is skipped here (see the blind-spot note at the top of the file). Reference-model
    paths are kept. Order preserved, duplicates removed.
    """
    if not isinstance(alternatives, list):
        return []
    paths = []
    for entry in alternatives:
        if not isinstance(entry, dict) or "conceptMap" in entry:
            continue
        path = entry.get("path")
        if isinstance(path, str) and path not in paths:
            paths.append(path)
    return paths


def has_concept_map(alternatives):
    """True if any alternative is a conceptMap (the blind spot we exclude and report)."""
    return isinstance(alternatives, list) and any(
        isinstance(entry, dict) and "conceptMap" in entry for entry in alternatives)


def is_temporal(field_name):
    """A date/time OMOP field. Its overloading is milder: the column stays a date, only the
    clinical event it refers to is lost. Contrasted with cross-semantic fields (concept_id,
    value, qualifier) where the column carries categorically different notions."""
    return "date" in field_name or field_name == "year_of_birth"


def analyse():
    """Walk every mapping once and collect what the report needs.

    Returns:
      written        set of every distinct (table, field) the library maps into
      overloads      deduplicated Overloads (a field fed by >=2 source paths in some mapping)
      field_writes   how many field-writes carry >=1 source path        (frequency denominator)
      overloaded_writes  how many of those carry >=2                     (frequency numerator)
      concept_map_writes how many field-writes are conceptMap            (the blind spot)
    """
    written = set()
    seen_overload = set()
    overloads = []
    field_writes = 0
    overloaded_writes = 0
    concept_map_writes = 0

    for path in mapping_files():
        with open(path, encoding="utf-8") as handle:
            try:
                doc = yaml.safe_load(handle)
            except yaml.YAMLError as error:
                print("  skipped (YAML error): %s  (%s)" % (os.path.basename(path), error))
                continue
        arch = archetype_id(doc)
        for block in (doc or {}).get("mappings", []) or []:
            if not isinstance(block, dict):
                continue
            table = block.get("type", "?")
            if table in NON_TABLE_TYPES:
                continue
            for field_name, spec in block.items():
                if field_name == "type" or not isinstance(spec, dict):
                    continue
                alternatives = spec.get("alternatives")
                if not isinstance(alternatives, list):
                    continue
                written.add((table, field_name))

                if has_concept_map(alternatives):
                    concept_map_writes += 1
                    continue
                paths = source_paths(alternatives)
                if not paths:
                    continue
                field_writes += 1
                if len(paths) >= 2:
                    overloaded_writes += 1
                    key = (arch, table, field_name, tuple(paths))
                    if key not in seen_overload:
                        seen_overload.add(key)
                        overloads.append(Overload(arch, table, field_name, paths))

    overloads.sort(key=lambda o: (o.archetype, o.table, o.field))
    return written, overloads, field_writes, overloaded_writes, concept_map_writes


def write_csv(overloads):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(["archetype", "omop_table", "omop_field", "n_paths", "paths"])
    for o in overloads:
        writer.writerow([o.archetype, o.table, o.field, len(o.paths), " | ".join(o.paths)])
    with open(OVERLOAD_CSV, "w", encoding="utf-8") as out:
        out.write(buffer.getvalue())


def write_coverage(overloads, overloaded_fields):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    by_arch = collections.OrderedDict()
    for o in overloads:
        by_arch.setdefault(o.archetype, []).append(o)
    lines = [
        "# Field overloading per archetype", "",
        "Every OMOP field fed by two or more distinct source paths (constant `code` values "
        "and conceptMap lookups excluded; reference-model paths kept).", "",
        "Overloaded OMOP fields: **%d** distinct, seen across **%d** archetype mappings."
        % (len(overloaded_fields), len(by_arch)), "",
    ]
    for arch, items in by_arch.items():
        lines.append("## %s" % arch)
        lines.append("")
        lines.append("| OMOP table | OMOP field | # paths | Source paths |")
        lines.append("|---|---|---|---|")
        for o in items:
            lines.append("| %s | %s | %d | %s |"
                         % (o.table, o.field, len(o.paths),
                            "<br>".join("`%s`" % p for p in o.paths)))
        lines.append("")
    with open(os.path.join(OUTPUT_DIR, "README.md"), "w", encoding="utf-8") as out:
        out.write("\n".join(lines))


def print_summary(written, overloads, field_writes, overloaded_writes, concept_map_writes):
    overloaded_fields = {(o.table, o.field) for o in overloads}
    archetypes = {o.archetype for o in overloads}
    temporal = {c for c in overloaded_fields if is_temporal(c[1])}
    cross_semantic = overloaded_fields - temporal

    print("=" * 72)
    print("FIELD OVERLOADING  (Table 3)")
    print("=" * 72)
    print("An OMOP field is overloaded when some mapping feeds it >=2 distinct source paths.")
    print()
    print("HEADLINE (structural, per distinct OMOP field):")
    print("  OMOP fields the library maps into        : %d" % len(written))
    print("  overloaded in at least one mapping        : %d" % len(overloaded_fields))
    print("  = %d of %d fields overloaded              : %.1f%%"
          % (len(overloaded_fields), len(written),
             100.0 * len(overloaded_fields) / len(written)))
    print()
    print("  of those %d overloaded fields:" % len(overloaded_fields))
    print("    temporal (a date fed by >1 timestamp)   : %d   milder: column stays a date,"
          % len(temporal))
    print("                                                    the clinical event is lost")
    print("    cross-semantic (concept_id/value/etc.)  : %d   severe: the column means"
          % len(cross_semantic))
    print("                                                    different things per record")
    print()
    print("  seen across %d archetype mappings; the same field is overloaded by different"
          % len(archetypes))
    print("  archetypes, so a field-mapping list (below) has more rows than distinct fields.")
    print()
    print("SECONDARY (frequency, per field-write -- NOT the headline):")
    print("  field-writes carrying a source path       : %d" % field_writes)
    print("  of those, overloaded                      : %d  (%.1f%%)"
          % (overloaded_writes, 100.0 * overloaded_writes / field_writes))
    print("  Dominated by a few high-frequency date fields, so this tracks the archetype mix")
    print("  more than the CDM. Use the headline for a claim about OMOP.")
    print()
    print("LOWER BOUND. Two reasons the true overloading is higher:")
    print("  1. Only fields the mapping actually feeds >=2 sources are counted. A field")
    print("     overloaded by design but mapped from the single source considered correct,")
    print("     because OMOP offers no alternative, looks clean here.")
    print("  2. %d field-writes use a conceptMap, whose source path is nested inside the"
          % concept_map_writes)
    print("     conceptMap object where this parser cannot read it, so they are not assessed.")

    # The CSV lists overloaded field-mappings; every distinct field in it must be in `written`,
    # or the two passes have diverged and neither number is safe to publish.
    if not overloaded_fields.issubset(written):
        raise ValueError(
            "overloaded fields not found among the fields the library writes: %s"
            % sorted(overloaded_fields - written))

    print("\nby OMOP target table (overloaded field-mappings):")
    for table, count in collections.Counter(o.table for o in overloads).most_common():
        print("  %-22s : %d" % (table, count))
    print("\nwrote resources/overloading.csv + resources/README.md")


def main():
    written, overloads, field_writes, overloaded_writes, concept_map_writes = analyse()
    overloaded_fields = {(o.table, o.field) for o in overloads}
    write_csv(overloads)
    write_coverage(overloads, overloaded_fields)
    print_summary(written, overloads, field_writes, overloaded_writes, concept_map_writes)


if __name__ == "__main__":
    main()

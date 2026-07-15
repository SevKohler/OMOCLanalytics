# conceptMap coverage: how many conceptMap entries resolve to no OMOP concept (concept 0).
#
# Answers a reviewer point on Section 3.3. The 8.59% vocabulary-gap figure counts only the
# primary concept_id fields and explicitly excludes zero entries inside conceptMaps. A
# conceptMap translates an archetype's internal openEHR codes (at-codes) to OMOP concepts,
# so a value of 0 means that internal code has no OMOP concept. That is a property of the
# mapping model, independent of how often each code appears in real data, so it can be
# reported. This script measures it directly from the mappings.
#
# A conceptMap block looks like:
#     - conceptMap:
#         path: "..."
#         mapping:
#           at0065: 4176265   # has an OMOP concept
#           at0172: 0         # no OMOP concept
#
# We count the entries inside each `mapping:` block and how many are 0.
#
# Input:  ../resources/OMOCL mappings/{medical_data,person_data}/**/*.yml  (tests excluded)
# Output: printed summary + conceptmap_zeros.csv (one row per file with a conceptMap)
# Run from this Table2ConceptIds/ folder:  python conceptmap_zeros.py
import csv
import glob
import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
MAPPINGS_DIR = os.path.join(HERE, "..", "resources", "OMOCL mappings")
OUT_CSV = os.path.join(HERE, "conceptmap_zeros.csv")

CONCEPTMAP_START = re.compile(r'^\s*-?\s*conceptMap:')          # start of a conceptMap block
MAPPING_START = re.compile(r'^\s*mapping:\s*$')                 # its inner `mapping:` block
ENTRY = re.compile(r'^\s+((?:at|id)\w[\w.]*)\s*:\s*(-?\d+)\s*(?:#.*)?$')   # at-code -> OMOP concept id


def mapping_files():
    found = (glob.glob(os.path.join(MAPPINGS_DIR, "medical_data", "**", "*.yml"), recursive=True)
             + glob.glob(os.path.join(MAPPINGS_DIR, "person_data", "**", "*.yml"), recursive=True))
    return sorted(f for f in found if os.sep + "tests" + os.sep not in f)


def count_conceptmap_zeros(path):
    """(conceptMap blocks, entries, zero entries) in one mapping file."""
    blocks = entries = zeros = 0
    inside_mapping = False
    mapping_indent = None
    for line in open(path, encoding="utf-8"):
        if CONCEPTMAP_START.match(line):
            blocks += 1
            inside_mapping = False
            continue
        if blocks and MAPPING_START.match(line):
            inside_mapping = True
            mapping_indent = len(line) - len(line.lstrip())
            continue
        if inside_mapping:
            indent = len(line) - len(line.lstrip())
            if line.strip() and indent <= mapping_indent:   # dedent, the mapping block ended
                inside_mapping = False
            else:
                entry = ENTRY.match(line)
                if entry:
                    entries += 1
                    if int(entry.group(2)) == 0:
                        zeros += 1
    return blocks, entries, zeros


def main():
    files = mapping_files()
    rows = []
    for path in files:
        blocks, entries, zeros = count_conceptmap_zeros(path)
        if blocks:
            rows.append({"file": os.path.relpath(path, MAPPINGS_DIR).replace(os.sep, "/"),
                         "conceptmaps": blocks, "entries": entries, "zeros": zeros})

    total_files = len(files)
    cm_files = len(rows)
    total_cm = sum(r["conceptmaps"] for r in rows)
    total_entries = sum(r["entries"] for r in rows)
    total_zeros = sum(r["zeros"] for r in rows)
    files_with_zero = sum(1 for r in rows if r["zeros"] > 0)

    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=["file", "conceptmaps", "entries", "zeros"],
                            lineterminator="\n")
    writer.writeheader()
    writer.writerows(sorted(rows, key=lambda r: (-r["zeros"], r["file"])))
    with open(OUT_CSV, "w", encoding="utf-8") as out:
        out.write(buffer.getvalue())

    print("=" * 64)
    print("conceptMap coverage (concept 0 = no OMOP concept)")
    print("=" * 64)
    print("non-test mapping files            : %d" % total_files)
    print("files containing a conceptMap     : %d" % cm_files)
    print("conceptMap blocks                 : %d" % total_cm)
    print("conceptMap entries                : %d" % total_entries)
    print("entries mapping to 0              : %d" % total_zeros)
    print("proportion of entries = 0         : %.1f%%" % (100.0 * total_zeros / total_entries))
    print("files with at least one zero      : %d" % files_with_zero)
    print("\nwrote %s" % os.path.relpath(OUT_CSV, HERE))


if __name__ == "__main__":
    main()

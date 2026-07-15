"""
Reproduces Table 2 of the manuscript, "Distribution of OMOP concept_id mapping properties".

Recomputes, directly from the OMOCL mapping YAML files, how the main OMOP concept_id is
determined for every mapping block, so reviewers can rerun it and check the numbers.

Data: ../resources/OMOCL mappings  (medical_data/** and person_data/**, test fixtures excluded)

Every mapping block with a main `concept_id.alternatives` list is classified by those
alternatives. The categories are not mutually exclusive, so each is counted at most once per
block:
    code == 0   -> zero        (no applicable OMOP concept)
    code != 0   -> fixed       (a constant OMOP concept id)
    path        -> paths       (concept id read from the archetype data node)
    conceptMap  -> conceptMap  (openEHR at-codes translated to OMOP concepts)
A `path:` nested inside a conceptMap belongs to that conceptMap, not to "paths".

Requires: Python 3, PyYAML.   Run: python "concept_id_properties.py"
"""
import os
import glob
import collections
import yaml

MAPPINGS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "..", "resources", "OMOCL mappings")

CATEGORIES = [
    ("zero",       "Mappings to zero (no applicable concept)"),
    ("fixed",      "Mappings using a fixed concept"),
    ("paths",      "Mappings with paths"),
    ("conceptMap", "Mappings with conceptMap"),
]


def mapping_files():
    """All mapping YAMLs under medical_data/ and person_data/, excluding test fixtures."""
    found = []
    for root in ("medical_data", "person_data"):
        found += glob.glob(os.path.join(MAPPINGS_DIR, root, "**", "*.yml"), recursive=True)
    return sorted(path for path in found if os.sep + "tests" + os.sep not in path)


def concept_categories(concept_id):
    """The distinct property categories a single concept_id block exhibits."""
    categories = set()
    for alternative in (concept_id.get("alternatives") or []):
        if not isinstance(alternative, dict):
            continue
        if "conceptMap" in alternative:
            categories.add("conceptMap")
        elif "path" in alternative:
            categories.add("paths")
        elif "code" in alternative:
            categories.add("zero" if str(alternative["code"]).strip() == "0" else "fixed")
    return categories


def main():
    files = mapping_files()
    counts = collections.Counter()
    concept_id_blocks = 0
    for path in files:
        document = yaml.safe_load(open(path, encoding="utf-8")) or {}
        for block in (document.get("mappings") or []):
            concept_id = block.get("concept_id") if isinstance(block, dict) else None
            if not (isinstance(concept_id, dict) and "alternatives" in concept_id):
                continue
            concept_id_blocks += 1
            counts.update(concept_categories(concept_id))

    print("Archetype mapping files (tests excluded): %d" % len(files))
    print("Main concept_id blocks (denominator)    : %d" % concept_id_blocks)
    print("\n%-42s %6s %11s" % ("Property / Concept ID Type", "Count", "Percentage"))
    print("-" * 61)
    for key, label in CATEGORIES:
        count = counts[key]
        print("%-42s %6d %10.2f%%" % (label, count, 100.0 * count / concept_id_blocks))
    print("\nCategories are not mutually exclusive, so a block may count in several rows.")


if __name__ == "__main__":
    main()

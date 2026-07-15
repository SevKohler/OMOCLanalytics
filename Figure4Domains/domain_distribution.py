"""
Reproduces Figure 4 of the manuscript,
"Distribution of mapped archetypes across OMOP CDM domains".

What it does, in plain terms:
  Every OMOCL mapping file contains a `mappings:` list. Each entry in that list is
  one "mapping block", and it names the OMOP table it targets in a `type:` field:

      mappings:
        - type: "Measurement"      <- this block maps into the Measurement table
          concept_id: ...
        - type: "Observation"      <- a second block, into the Observation table
          concept_id: ...

  Figure 4 just counts how many blocks point at each OMOP table. This script does
  exactly that, so a reviewer can rerun it and compare the counts with the figure.

Data: ../resources/OMOCL mappings   (medical_data/** and person_data/**, tests excluded)
Requires: Python 3 and PyYAML.      Run:  python "domain_distribution.py"
"""
import os
import glob
import yaml

# The mapping files live one folder up, under resources/.
MAPPINGS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "..", "resources", "OMOCL mappings")

# Each mapping block's raw `type:` value, and the label Figure 4 prints for it.
# ("CustomMapping" is how a fact_relationship row is built, so it shows as Fact_relationship.)
FIGURE_LABEL = {
    "Measurement":         "Measurement",
    "Observation":         "Observation",
    "DrugExposure":        "Drug_exposure",
    "ConditionOccurrence": "Condition_occurrence",
    "ProcedureOccurrence": "Procedure_occurrence",
    "Specimen":            "Specimen",
    "CustomMapping":       "Fact_relationship",
    "DeviceExposure":      "Device_exposure",
    "Visit":               "Visit_occurrence",
    "Death":               "Death",
    "Person":              "Person",
}

# "Include" is an OMOCL directive, not a real OMOP table, so Figure 4 leaves it out.
NOT_A_TABLE = "Include"


def find_mapping_files():
    """Collect the paths of all mapping files, skipping the test fixtures."""
    paths = []
    for subfolder in ("medical_data", "person_data"):
        paths += glob.glob(os.path.join(MAPPINGS_DIR, subfolder, "**", "*.yml"), recursive=True)
    return sorted(p for p in paths if (os.sep + "tests" + os.sep) not in p)


def main():
    files = find_mapping_files()

    # Step 1: read every file and tally how many blocks use each raw `type`.
    blocks_per_type = {}                       # e.g. {"Measurement": 147, "Include": 4, ...}
    for path in files:
        content = yaml.safe_load(open(path, encoding="utf-8")) or {}
        for block in content.get("mappings", []) or []:
            if isinstance(block, dict) and "type" in block:
                omop_type = block["type"]
                blocks_per_type[omop_type] = blocks_per_type.get(omop_type, 0) + 1

    # Step 2: rename the raw types to the figure's labels and drop the "Include" directive.
    blocks_per_domain = {}                     # e.g. {"Measurement": 147, "Fact_relationship": 1, ...}
    for omop_type, count in blocks_per_type.items():
        if omop_type == NOT_A_TABLE:
            continue
        domain = FIGURE_LABEL.get(omop_type, omop_type)
        blocks_per_domain[domain] = blocks_per_domain.get(domain, 0) + count

    total = sum(blocks_per_domain.values())    # the figure total (295)

    # Step 3: print the table, biggest domain first.
    print("Mapping files read (tests excluded): %d" % len(files))
    print("Mapping blocks on OMOP tables (total): %d" % total)
    if NOT_A_TABLE in blocks_per_type:
        print("Excluded '%s' directive blocks: %d" % (NOT_A_TABLE, blocks_per_type[NOT_A_TABLE]))
    print()
    print("%-24s %6s %11s" % ("Domain", "Count", "Percentage"))
    print("-" * 43)
    for domain, count in sorted(blocks_per_domain.items(), key=lambda pair: pair[1], reverse=True):
        percentage = 100.0 * count / total
        print("%-24s %6d %10.2f%%" % (domain, count, percentage))


if __name__ == "__main__":
    main()

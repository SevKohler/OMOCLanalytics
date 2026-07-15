# openEHR-EHR-CLUSTER.genomic_deletion_insertion_variant.v1

**Concept:** Genomic deletion-insertion variant

**Category:** cluster

**Element leaves:** 4  |  **Cluster slot leaves:** 1  |  **Total leaves:** 5


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0001 | Start position | DV_COUNT |
| at0003 | End position | DV_COUNT |
| at0005 | Deleted sequence | DV_TEXT |
| at0007 | Inserted sequence | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0008 | Reference sequence | openEHR-EHR-CLUSTER.reference_sequence(-[a-zA-Z0-9_]+)*.v1 |

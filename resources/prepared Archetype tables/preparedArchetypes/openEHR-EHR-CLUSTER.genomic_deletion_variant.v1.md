# openEHR-EHR-CLUSTER.genomic_deletion_variant.v1

**Concept:** Genomic deletion variant

**Category:** cluster

**Element leaves:** 3  |  **Cluster slot leaves:** 1  |  **Total leaves:** 4


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0001 | Start position | DV_COUNT |
| at0005 | End position | DV_COUNT |
| at0008 | Deleted sequence | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0009 | Reference sequence | openEHR-EHR-CLUSTER.reference_sequence(-[a-zA-Z0-9_]+)*.v1 |

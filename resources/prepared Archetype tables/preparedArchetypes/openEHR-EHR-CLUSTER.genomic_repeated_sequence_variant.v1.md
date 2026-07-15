# openEHR-EHR-CLUSTER.genomic_repeated_sequence_variant.v1

**Concept:** Genomic repeated sequence variant

**Category:** cluster

**Element leaves:** 5  |  **Cluster slot leaves:** 1  |  **Total leaves:** 6


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0001 | Start position | DV_COUNT |
| at0003 | End position | DV_COUNT |
| at0010 | Repeat order | DV_COUNT |
| at0005 | Repeated sequence | DV_TEXT |
| at0007 | Copy number | DV_COUNT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0008 | Reference sequence | openEHR-EHR-CLUSTER.reference_sequence(-[a-zA-Z0-9_]+)*.v1 |

# openEHR-EHR-CLUSTER.genomic_inversion_variant.v1

**Concept:** Genomic inversion variant

**Category:** cluster

**Element leaves:** 3  |  **Cluster slot leaves:** 1  |  **Total leaves:** 4


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0001 | Start position | DV_COUNT |
| at0004 | End position | DV_COUNT |
| at0006 | Inverted sequence | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0007 | Reference sequence | openEHR-EHR-CLUSTER.reference_sequence(-[a-zA-Z0-9_]+)*.v1 |

# openEHR-EHR-CLUSTER.genomic_copy_number_variant.v1

**Concept:** Genomic copy number variant

**Category:** cluster

**Element leaves:** 4  |  **Cluster slot leaves:** 1  |  **Total leaves:** 5


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0001 | Start | DV_COUNT / DV_INTERVAL |
| at0002 | End | DV_COUNT / DV_INTERVAL |
| at0003 | Total copy number | DV_COUNT / DV_QUANTITY |
| at0005 | Copy number change type | DV_CODED_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0004 | Reference sequence | openEHR-EHR-CLUSTER.reference_sequence(-[a-zA-Z0-9_]+)*.v1 |

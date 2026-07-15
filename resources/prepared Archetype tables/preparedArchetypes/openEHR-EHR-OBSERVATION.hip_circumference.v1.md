# openEHR-EHR-OBSERVATION.hip_circumference.v1

**Concept:** Hip circumference

**Category:** entry/observation

**Element leaves:** 3  |  **Cluster slot leaves:** 1  |  **Total leaves:** 4


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0004 | Hip circumference | DV_QUANTITY |
| at0007 | Comment | DV_TEXT |
| at0009 | Confounding factors | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0006 | Device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |

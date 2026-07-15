# openEHR-EHR-OBSERVATION.waist_circumference.v1

**Concept:** Waist circumference

**Category:** entry/observation

**Element leaves:** 4  |  **Cluster slot leaves:** 1  |  **Total leaves:** 5


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0004 | Waist circumference | DV_QUANTITY |
| at0007 | Comment | DV_TEXT |
| at0009 | Confounding factors | DV_TEXT |
| at0013 | Method | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0006 | Device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |

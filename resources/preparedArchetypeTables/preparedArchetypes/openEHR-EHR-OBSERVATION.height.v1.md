# openEHR-EHR-OBSERVATION.height.v1

**Concept:** Height/Length

**Category:** entry/observation

**Element leaves:** 4  |  **Cluster slot leaves:** 1  |  **Total leaves:** 5


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0004 | Height/Length | DV_QUANTITY |
| at0018 | Comment | DV_TEXT |
| at0014 | Position | DV_CODED_TEXT |
| at0019 | Confounding factors | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0011 | Device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |

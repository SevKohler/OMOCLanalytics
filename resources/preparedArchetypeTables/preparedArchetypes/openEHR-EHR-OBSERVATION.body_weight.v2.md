# openEHR-EHR-OBSERVATION.body_weight.v2

**Concept:** Body weight

**Category:** entry/observation

**Element leaves:** 4  |  **Cluster slot leaves:** 1  |  **Total leaves:** 5


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0004 | Weight | DV_QUANTITY |
| at0024 | Comment | DV_TEXT |
| at0009 | State of dress | DV_CODED_TEXT |
| at0025 | Confounding factors | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0020 | Device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |

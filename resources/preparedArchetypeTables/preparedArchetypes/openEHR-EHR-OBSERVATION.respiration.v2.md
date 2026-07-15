# openEHR-EHR-OBSERVATION.respiration.v2

**Concept:** Respiration

**Category:** entry/observation

**Element leaves:** 9  |  **Cluster slot leaves:** 2  |  **Total leaves:** 11


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0062 | Presence | DV_CODED_TEXT |
| at0004 | Rate | DV_QUANTITY |
| at0005 | Regularity | DV_CODED_TEXT |
| at0016 | Depth | DV_CODED_TEXT |
| at0024 | Clinical description | DV_TEXT |
| at0009 | Clinical interpretation | DV_TEXT |
| at0070 | Comment | DV_TEXT |
| at0065 | Body position | DV_CODED_TEXT |
| at0056 | Confounding factors | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0055 | Inspired oxygen | openEHR-EHR-CLUSTER.inspired_oxygen(-[a-zA-Z0-9_]+)*.v1 |
| at0037 | Exertion | openEHR-EHR-CLUSTER.level_of_exertion(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.level_of_exertion(-[a-zA-Z0-9_]+)*.v1 |

# openEHR-EHR-OBSERVATION.body_surface_area.v1

**Concept:** Body surface area

**Category:** entry/observation

**Element leaves:** 5  |  **Cluster slot leaves:** 1  |  **Total leaves:** 6


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0004 | Body Surface Area | DV_QUANTITY |
| at0019 | Comment | DV_TEXT |
| at0021 | Confounding factors | DV_TEXT |
| at0009 | Method | DV_CODED_TEXT |
| at0006 | Formula | DV_CODED_TEXT / DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0008 | Device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |

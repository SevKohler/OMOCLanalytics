# openEHR-EHR-OBSERVATION.testicular_volume.v1

**Concept:** Testicular volume

**Category:** entry/observation

**Element leaves:** 6  |  **Cluster slot leaves:** 1  |  **Total leaves:** 7


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0020 | Testicle examined | DV_TEXT / DV_CODED_TEXT |
| at0010 | Testicular volume | DV_QUANTITY |
| at0005 | Comment | DV_TEXT |
| at0012 | Confounding factors | DV_TEXT |
| at0013 | Method | DV_TEXT |
| at0008 | Formula | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0007 | Device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |

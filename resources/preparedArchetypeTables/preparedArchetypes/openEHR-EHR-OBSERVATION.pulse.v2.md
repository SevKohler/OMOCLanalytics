# openEHR-EHR-OBSERVATION.pulse.v2

**Concept:** Pulse/Heart beat

**Category:** entry/observation

**Element leaves:** 12  |  **Cluster slot leaves:** 2  |  **Total leaves:** 14


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at1005 | Presence | DV_CODED_TEXT |
| at0004 | Rate | DV_QUANTITY |
| at0005 | Regularity | DV_CODED_TEXT |
| at1055 | Irregular type | DV_CODED_TEXT |
| at1030 | Character | DV_TEXT |
| at1022 | Clinical description | DV_TEXT |
| at1023 | Clinical interpretation | DV_TEXT |
| at1059 | Comment | DV_TEXT |
| at0013 | Position | DV_CODED_TEXT |
| at1018 | Confounding factors | DV_TEXT |
| at1019 | Method | DV_CODED_TEXT |
| at1037 | Body site | DV_CODED_TEXT / DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at1017 | Exertion | openEHR-EHR-CLUSTER.level_of_exertion(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.level_of_exertion(-[a-zA-Z0-9_]+)*.v0 |
| at1013 | Device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |

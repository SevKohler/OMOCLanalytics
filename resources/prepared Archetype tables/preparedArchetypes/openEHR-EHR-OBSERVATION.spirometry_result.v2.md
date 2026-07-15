# openEHR-EHR-OBSERVATION.spirometry_result.v2

**Concept:** Spirometry result

**Category:** entry/observation

**Element leaves:** 19  |  **Cluster slot leaves:** 5  |  **Total leaves:** 24


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0053 | Result | DV_QUANTITY |
| at0054 | Predicted result | DV_QUANTITY |
| at0044 | Measured/predicted ratio | DV_PROPORTION |
| at0058 | Result | DV_QUANTITY |
| at0008 | Predicted result | DV_QUANTITY |
| at0122 | Measured/predicted ratio | DV_PROPORTION |
| at0165 | Result | DV_QUANTITY |
| at0166 | Predicted result | DV_QUANTITY |
| at0167 | Measured/predicted ratio | DV_PROPORTION |
| at0056 | Result | DV_PROPORTION |
| at0018 | Predicted result | DV_PROPORTION |
| at0013 | Forced expiratory time (FET) | DV_DURATION |
| at0130 | Clinical interpretation | DV_TEXT |
| at0101 | Comment | DV_TEXT |
| at0115 | Position | DV_CODED_TEXT |
| at0098 | Confounding factors | DV_TEXT |
| at0196 | Type of measurement | DV_CODED_TEXT |
| at0199 | Method | DV_TEXT |
| at0192 | Challenge/reversibility | DV_CODED_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0131 | Multimedia representation | openEHR-EHR-CLUSTER.media_file(-[a-zA-Z0-9_]+)*.v1 |
| at0191 | Level of exertion | openEHR-EHR-CLUSTER.level_of_exertion(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.level_of_exertion(-[a-zA-Z0-9_]+)*.v1 |
| at0209 | Environmental conditions | openEHR-EHR-CLUSTER.environmental_conditions(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.environmental_conditions(-[a-zA-Z0-9_]+)*.v1 |
| at0030 | Device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0185 | Predicted results source | openEHR-EHR-CLUSTER.knowledge_base_reference(-[a-zA-Z0-9_]+)*.v1 |

# openEHR-EHR-OBSERVATION.body_temperature.v2

**Concept:** Body temperature

**Category:** entry/observation

**Element leaves:** 7  |  **Cluster slot leaves:** 4  |  **Total leaves:** 11


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0004 | Temperature | DV_QUANTITY |
| at0063 | Comment | DV_TEXT |
| at0030 | Body exposure | DV_CODED_TEXT / DV_TEXT |
| at0041 | Description of thermal stress | DV_TEXT |
| at0065 | Day of menstrual cycle | DV_COUNT |
| at0066 | Confounding factors | DV_TEXT |
| at0021 | Location of measurement | DV_CODED_TEXT / DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0056 | Environmental conditions | openEHR-EHR-CLUSTER.environmental_conditions.v1 / openEHR-EHR-CLUSTER.environmental_conditions.v0 |
| at0057 | Exertion | openEHR-EHR-CLUSTER.level_of_exertion.v1 / openEHR-EHR-CLUSTER.level_of_exertion.v0 |
| at0064 | Structured measurement location | openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_relative.v1 |
| at0059 | Device | openEHR-EHR-CLUSTER.device.v1 |

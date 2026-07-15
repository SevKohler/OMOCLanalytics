# openEHR-EHR-OBSERVATION.exposure_screening.v1

**Concept:** Exposure screening questionnaire

**Category:** entry/observation

**Element leaves:** 8  |  **Cluster slot leaves:** 2  |  **Total leaves:** 10


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0004 | Screening purpose | DV_TEXT |
| at0020 | Agent name | DV_TEXT |
| at0005 | Any exposure? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0022 | Description | DV_TEXT |
| at0010 | Situation | DV_TEXT |
| at0011 | Presence? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0015 | Timing | DV_DATE_TIME / DV_INTERVAL / DV_DURATION / DV_TEXT |
| at0017 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0016 | Additional details | openEHR-EHR-CLUSTER.person(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.address(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_circle(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_relative.v2 |
| at0023 | Additional details | any archetype |

# openEHR-EHR-OBSERVATION.travel_screening.v1

**Concept:** Travel screening questionnaire

**Category:** entry/observation

**Element leaves:** 7  |  **Cluster slot leaves:** 2  |  **Total leaves:** 9


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0027 |  | Any travel? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0040 |  | Screening purpose | DV_TEXT |
| at0043 |  | Description | DV_TEXT |
| at0021 | Specific travel | Travel activity | DV_TEXT / DV_CODED_TEXT |
| at0024 | Specific travel | Occurred? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0003 | Specific travel | Timing | DV_DATE_TIME / DV_TEXT / DV_INTERVAL / DV_DURATION |
| at0025 | Specific travel | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0041 | Specific travel | Additional details | any archetype |
| at0044 |  | Additional details | any archetype |

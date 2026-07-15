# openEHR-EHR-OBSERVATION.substance_use_screening.v1

**Concept:** Substance use screening questionnaire

**Category:** entry/observation

**Element leaves:** 9  |  **Cluster slot leaves:** 2  |  **Total leaves:** 11


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0040 | Screening purpose | DV_TEXT |
| at0052 | Any substance use? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0042 | Description | DV_TEXT |
| at0021 | Substance name | DV_TEXT |
| at0024 | Used? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0003 | Last used | DV_DATE_TIME / DV_TEXT |
| at0002 | Timing | DV_DATE_TIME / DV_DURATION / DV_INTERVAL / DV_TEXT |
| at0025 | Comment | DV_TEXT |
| at0056 | Overall comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0041 | Additional details | any archetype |
| at0043 | Additional details | any archetype |

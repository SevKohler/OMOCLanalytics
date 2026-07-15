# openEHR-EHR-OBSERVATION.substance_use_screening.v1

**Concept:** Substance use screening questionnaire

**Category:** entry/observation

**Element leaves:** 9  |  **Cluster slot leaves:** 2  |  **Total leaves:** 11


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0040 |  | Screening purpose | DV_TEXT |
| at0052 |  | Any substance use? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0042 |  | Description | DV_TEXT |
| at0021 | Specific substance | Substance name | DV_TEXT |
| at0024 | Specific substance | Used? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0003 | Specific substance | Last used | DV_DATE_TIME / DV_TEXT |
| at0002 | Specific substance | Timing | DV_DATE_TIME / DV_DURATION / DV_INTERVAL / DV_TEXT |
| at0025 | Specific substance | Comment | DV_TEXT |
| at0056 |  | Overall comment | DV_TEXT |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0041 | Specific substance | Additional details | any archetype |
| at0043 |  | Additional details | any archetype |

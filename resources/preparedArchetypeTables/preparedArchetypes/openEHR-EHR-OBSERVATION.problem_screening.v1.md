# openEHR-EHR-OBSERVATION.problem_screening.v1

**Concept:** Problem/Diagnosis screening questionnaire

**Category:** entry/observation

**Element leaves:** 7  |  **Cluster slot leaves:** 2  |  **Total leaves:** 9


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0034 |  | Screening purpose | DV_TEXT |
| at0028 |  | Any problems or diagnoses? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0043 |  | Description | DV_TEXT |
| at0004 | Specific problem or diagnosis | Problem/diagnosis name | DV_TEXT |
| at0005 | Specific problem or diagnosis | Presence? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0040 | Specific problem or diagnosis | Timing | DV_TEXT / DV_INTERVAL / DV_DURATION / DV_DATE_TIME |
| at0025 | Specific problem or diagnosis | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0039 | Specific problem or diagnosis | Additional details | openEHR-EHR-CLUSTER.organisation.v1 |
| at0042 |  | Additional details | any archetype |

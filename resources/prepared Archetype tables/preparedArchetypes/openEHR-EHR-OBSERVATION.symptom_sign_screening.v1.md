# openEHR-EHR-OBSERVATION.symptom_sign_screening.v1

**Concept:** Symptom/sign screening questionnaire

**Category:** entry/observation

**Element leaves:** 8  |  **Cluster slot leaves:** 2  |  **Total leaves:** 10


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0034 | Screening purpose | DV_TEXT |
| at0028 | Any symptoms or signs? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0029 | Onset | DV_DATE_TIME / DV_INTERVAL / DV_TEXT / DV_DURATION |
| at0036 | Description | DV_TEXT |
| at0004 | Symptom/sign name | DV_TEXT |
| at0005 | Presence? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0037 | Timing | DV_DURATION / DV_INTERVAL / DV_DATE_TIME / DV_TEXT |
| at0035 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0026 | Additional details | openEHR-EHR-CLUSTER.exclusion_symptom_sign.v0 / openEHR-EHR-CLUSTER.symptom_sign.v2 |
| at0039 | Additional details | any archetype |

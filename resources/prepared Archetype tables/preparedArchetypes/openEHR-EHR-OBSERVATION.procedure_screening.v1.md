# openEHR-EHR-OBSERVATION.procedure_screening.v1

**Concept:** Procedure screening questionnaire

**Category:** entry/observation

**Element leaves:** 7  |  **Cluster slot leaves:** 2  |  **Total leaves:** 9


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0034 | Screening purpose | DV_TEXT |
| at0028 | Any previous procedures? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0041 | Description | DV_TEXT |
| at0004 | Procedure name | DV_TEXT |
| at0005 | Carried out? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0037 | Timing | DV_DATE_TIME / DV_TEXT / DV_DURATION / DV_INTERVAL |
| at0025 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0036 | Additional details | openEHR-EHR-CLUSTER.organisation.v1 |
| at0040 | Additional details | any archetype |

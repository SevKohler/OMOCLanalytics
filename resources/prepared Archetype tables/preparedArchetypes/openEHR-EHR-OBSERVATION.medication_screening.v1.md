# openEHR-EHR-OBSERVATION.medication_screening.v1

**Concept:** Medication screening questionnaire

**Category:** entry/observation

**Element leaves:** 8  |  **Cluster slot leaves:** 2  |  **Total leaves:** 10


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0040 | Screening purpose | DV_TEXT |
| at0027 | Any medications used? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0043 | Description | DV_TEXT |
| at0021 | Medication name | DV_TEXT |
| at0024 | Used | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0003 | Latest dose | DV_DATE_TIME / DV_TEXT |
| at0002 | Timing | DV_DURATION / DV_INTERVAL / DV_TEXT / DV_DATE_TIME |
| at0025 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0041 | Additional details | openEHR-EHR-CLUSTER.dosage(-[a-zA-Z0-9_]+)*.v2 |
| at0042 | Additional details | any archetype |

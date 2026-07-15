# openEHR-EHR-OBSERVATION.management_screening.v1

**Concept:** Management screening questionnaire

**Category:** entry/observation

**Element leaves:** 8  |  **Cluster slot leaves:** 2  |  **Total leaves:** 10


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0034 | Screening purpose | DV_TEXT |
| at0039 | Any management? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0044 | Description | DV_TEXT |
| at0004 | Management name | DV_TEXT |
| at0005 | Specific management? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0037 | Start | DV_DATE_TIME / DV_INTERVAL / DV_TEXT / DV_DURATION |
| at0038 | Stopped | DV_DATE_TIME / DV_INTERVAL / DV_TEXT / DV_DURATION |
| at0035 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0036 | Additional details | openEHR-EHR-CLUSTER.organisation.v1 |
| at0043 | Additional details | any archetype |

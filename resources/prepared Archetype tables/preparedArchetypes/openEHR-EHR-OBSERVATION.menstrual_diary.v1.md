# openEHR-EHR-OBSERVATION.menstrual_diary.v1

**Concept:** Menstrual diary

**Category:** entry/observation

**Element leaves:** 6  |  **Cluster slot leaves:** 1  |  **Total leaves:** 7


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0004 | Flow | DV_CODED_TEXT / DV_TEXT |
| at0010 | Volume | DV_QUANTITY |
| at0014 | Blood clots | DV_CODED_TEXT |
| at0017 | Color | DV_TEXT |
| at0018 | Description | DV_TEXT |
| at0021 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0020 | Additional details | openEHR-EHR-CLUSTER.symptom_sign(-[a-zA-Z0-9_]+)*.v1 |

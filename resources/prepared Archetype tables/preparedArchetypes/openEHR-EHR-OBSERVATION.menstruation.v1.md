# openEHR-EHR-OBSERVATION.menstruation.v1

**Concept:** Menstrual cycle

**Category:** entry/observation

**Element leaves:** 7  |  **Cluster slot leaves:** 1  |  **Total leaves:** 8


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0004 | Start of menses | DV_DATE_TIME |
| at0005 | Duration of menses | DV_DURATION |
| at0006 | Description of the cycle | DV_TEXT |
| at0007 | Relative flow | DV_CODED_TEXT |
| at0013 | Blood clots | DV_CODED_TEXT |
| at0032 | Comment | DV_TEXT |
| at0021 | Confounding factors | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0019 | Additional details | openEHR-EHR-CLUSTER.symptom_sign(-[a-zA-Z0-9_]+)*.v1 |

# openEHR-EHR-OBSERVATION.blood_pressure.v2

**Concept:** Blood pressure

**Category:** entry/observation

**Element leaves:** 17  |  **Cluster slot leaves:** 3  |  **Total leaves:** 20


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0004 | Systolic | DV_QUANTITY |
| at0005 | Diastolic | DV_QUANTITY |
| at1006 | Mean arterial pressure | DV_QUANTITY |
| at1007 | Pulse pressure | DV_QUANTITY |
| at1059 | Clinical interpretation | DV_TEXT |
| at0033 | Comment | DV_TEXT |
| at0008 | Position | DV_CODED_TEXT |
| at1052 | Confounding factors | DV_TEXT |
| at1043 | Sleep status | DV_CODED_TEXT |
| at1005 | Tilt | DV_QUANTITY |
| at0013 | Cuff size | DV_CODED_TEXT |
| at0014 | Location of measurement | DV_CODED_TEXT / DV_TEXT |
| at1035 | Method | DV_CODED_TEXT |
| at1038 | Mean arterial pressure formula | DV_TEXT |
| at1054 | Systolic pressure formula | DV_TEXT |
| at1055 | Diastolic pressure formula | DV_TEXT |
| at1010 | Diastolic endpoint | DV_CODED_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at1030 | Exertion | openEHR-EHR-CLUSTER.level_of_exertion(-[a-zA-Z0-9_]+)*.v1 |
| at1057 | Structured measurement location | openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 |
| at1025 | Device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |

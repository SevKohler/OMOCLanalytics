# openEHR-EHR-EVALUATION.medication_summary.v1

**Concept:** Medication summary

**Category:** entry/evaluation

**Element leaves:** 19  |  **Cluster slot leaves:** 1  |  **Total leaves:** 20


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0002 | Medication name | DV_TEXT |
| at0007 | Clinical description | DV_TEXT |
| at0028 | Clinical indication | DV_TEXT |
| at0009 | Onset of use | DV_DATE_TIME |
| at0011 | Episode onset | DV_DATE_TIME |
| at0018 | Episode indication | DV_TEXT |
| at0020 | Therapeutic intent | DV_TEXT |
| at0014 | Description | DV_TEXT |
| at0016 | Episode amount | DV_QUANTITY / DV_TEXT |
| at0012 | Episode cessation | DV_DATE_TIME |
| at0031 | Episode duration | DV_DURATION |
| at0013 | Episode reason for cessation | DV_TEXT |
| at0032 | Route | DV_TEXT |
| at0022 | Therapeutic response | DV_TEXT |
| at0015 | Cumulative dose | DV_QUANTITY |
| at0010 | Cessation of use | DV_DATE_TIME |
| at0030 | Reason for cessation | DV_TEXT |
| at0027 | Cumulative duration | DV_DURATION |
| at0006 | Last updated | DV_DATE_TIME |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0029 | Additional details | openEHR-EHR-CLUSTER.dosage(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.dosage(-[a-zA-Z0-9_]+)*.v2 / openEHR-EHR-CLUSTER.medication(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.medication(-[a-zA-Z0-9_]+)*.v2 / openEHR-EHR-CLUSTER.therapeutic_direction.v1 |

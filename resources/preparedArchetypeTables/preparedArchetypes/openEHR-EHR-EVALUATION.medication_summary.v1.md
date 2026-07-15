# openEHR-EHR-EVALUATION.medication_summary.v1

**Concept:** Medication summary

**Category:** entry/evaluation

**Element leaves:** 18  |  **Cluster slot leaves:** 1  |  **Total leaves:** 19


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0002 |  | Medication name | DV_TEXT |
| at0007 |  | Clinical description | DV_TEXT |
| at0028 |  | Clinical indication | DV_TEXT |
| at0009 |  | Onset of use | DV_DATE_TIME |
| at0011 | Episode | Episode onset | DV_DATE_TIME |
| at0018 | Episode | Episode indication | DV_TEXT |
| at0020 | Episode | Therapeutic intent | DV_TEXT |
| at0014 | Episode | Description | DV_TEXT |
| at0016 | Episode | Episode amount | DV_QUANTITY / DV_TEXT |
| at0012 | Episode | Episode cessation | DV_DATE_TIME |
| at0031 | Episode | Episode duration | DV_DURATION |
| at0013 | Episode | Episode reason for cessation | DV_TEXT |
| at0032 | Episode | Route | DV_TEXT |
| at0022 | Episode | Therapeutic response | DV_TEXT |
| at0015 |  | Cumulative dose | DV_QUANTITY |
| at0010 |  | Cessation of use | DV_DATE_TIME |
| at0030 |  | Reason for cessation | DV_TEXT |
| at0027 |  | Cumulative duration | DV_DURATION |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0029 | Episode | Additional details | openEHR-EHR-CLUSTER.dosage(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.dosage(-[a-zA-Z0-9_]+)*.v2 / openEHR-EHR-CLUSTER.medication(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.medication(-[a-zA-Z0-9_]+)*.v2 / openEHR-EHR-CLUSTER.therapeutic_direction.v1 |

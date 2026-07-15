# openEHR-EHR-OBSERVATION.medication_statement.v0

**Concept:** Medication use statement

**Category:** entry/observation

**Element leaves:** 8  |  **Cluster slot leaves:** 3  |  **Total leaves:** 11


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0006 | Medication name | DV_TEXT |
| at0047 | Overall directions description | DV_TEXT |
| at0030 | Route of administration | DV_TEXT |
| at0032 | Description | DV_TEXT |
| at0023 | Clinical indication | DV_TEXT |
| at0026 | Last administered | DV_DATE_TIME |
| at0037 | Endpoint | DV_DATE_TIME / DV_CODED_TEXT |
| at0029 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0046 | Medication details | openEHR-EHR-CLUSTER.medication(-[a-zA-Z0-9_]+)*.v2 |
| at0045 | Structured dose and timing | openEHR-EHR-CLUSTER.timing_daily(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.timing_nondaily(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.therapeutic_direction(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.dosage(-[a-zA-Z0-9_]+)*.v2 |
| at0048 | Addtional details | any archetype |

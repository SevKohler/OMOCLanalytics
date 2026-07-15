# openEHR-EHR-EVALUATION.problem_diagnosis.v1

**Concept:** Problem/Diagnosis

**Category:** entry/evaluation

**Element leaves:** 13  |  **Cluster slot leaves:** 3  |  **Total leaves:** 16


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0002 | Problem/Diagnosis name | DV_TEXT |
| at0079 | Variant | DV_TEXT |
| at0009 | Clinical description | DV_TEXT |
| at0012 | Body site | DV_TEXT |
| at0078 | Cause | DV_TEXT |
| at0077 | Date/time of onset | DV_DATE_TIME |
| at0003 | Date/time clinically recognised | DV_DATE_TIME |
| at0005 | Severity | DV_CODED_TEXT / DV_TEXT |
| at0080 | Impact | DV_TEXT |
| at0072 | Course description | DV_TEXT |
| at0030 | Date/time of resolution | DV_DATE_TIME |
| at0073 | Diagnostic certainty | DV_CODED_TEXT / DV_TEXT |
| at0069 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0039 | Structured body site | openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_circle.v1 / openEHR-EHR-CLUSTER.anatomical_location_relative(-[a-zA-Z0-9_]+)*.v2 |
| at0043 | Specific details | any archetype |
| at0046 | Status | openEHR-EHR-CLUSTER.problem_qualifier(-[a-zA-Z0-9_]+)*.v2 |

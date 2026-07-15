# openEHR-EHR-OBSERVATION.urinalysis.v1

**Concept:** Urinalysis

**Category:** entry/observation

**Element leaves:** 13  |  **Cluster slot leaves:** 4  |  **Total leaves:** 17


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0050 | Glucose | DV_ORDINAL |
| at0062 | Bilirubin | DV_ORDINAL |
| at0037 | Ketones | DV_ORDINAL |
| at0151 | Specific gravity | DV_ORDINAL |
| at0032 | Blood | DV_ORDINAL |
| at0126 | pH | DV_ORDINAL |
| at0095 | Protein | DV_ORDINAL |
| at0056 | Urobilinogen | DV_ORDINAL |
| at0043 | Nitrite | DV_ORDINAL |
| at0068 | Leukocytes | DV_ORDINAL |
| at0181 | Clinical interpretation | DV_TEXT |
| at0030 | Comment | DV_TEXT |
| at0186 | Method | DV_CODED_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0182 | Additional details | openEHR-EHR-CLUSTER.exam_body_fluid(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.specimen(-[a-zA-Z0-9_]+)*.v0 |
| at0185 | Exam not done | openEHR-EHR-CLUSTER.exclusion_exam(-[a-zA-Z0-9_]+)*.v1 |
| at0180 | Reagent Strips | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0183 | Device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |

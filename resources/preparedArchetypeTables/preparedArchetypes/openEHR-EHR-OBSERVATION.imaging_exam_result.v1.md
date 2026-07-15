# openEHR-EHR-OBSERVATION.imaging_exam_result.v1

**Concept:** Imaging examination result

**Category:** entry/observation

**Element leaves:** 36  |  **Cluster slot leaves:** 11  |  **Total leaves:** 47


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0004 |  | Study name | DV_TEXT |
| at0091 |  | Modality | DV_TEXT |
| at0055 |  | Target body site | DV_TEXT |
| at0070 |  | Study date | DV_DATE_TIME |
| at0072 |  | Overall result status | DV_CODED_TEXT / DV_TEXT |
| at0071 |  | Status timestamp | DV_DATE_TIME |
| at0061 |  | Clinical indication | DV_TEXT |
| at0014 |  | Clinical summary | DV_TEXT |
| at0008 |  | Imaging findings | DV_TEXT |
| at0056 |  | Comparison findings | DV_TEXT |
| at0063 |  | Imaging quality | DV_TEXT |
| at0057 |  | Imaging quality description | DV_TEXT |
| at0021 |  | Overall impression | DV_TEXT |
| at0058 |  | Imaging differential diagnosis | DV_TEXT |
| at0020 |  | Imaging diagnosis | DV_TEXT |
| at0059 |  | Recommendation | DV_TEXT |
| at0023 |  | Comment | DV_TEXT |
| at0048 |  | Confounding factors | DV_TEXT |
| at0108 |  | Position | DV_TEXT |
| at0092 |  | Study instance identifier | DV_IDENTIFIER / DV_TEXT |
| at0105 |  | Study description | DV_TEXT |
| at0104 |  | Report identifier | DV_IDENTIFIER / DV_TEXT |
| at0099 |  | Study status | DV_CODED_TEXT / DV_TEXT |
| at0098 |  | Study end point | DV_TEXT / DV_URI |
| at0106 |  | Image details | DV_URI |
| at0087 |  | Technique | DV_TEXT |
| at0049 |  | Technique summary | DV_TEXT |
| at0088 |  | Procedure | DV_TEXT |
| at0062 |  | Procedure summary | DV_TEXT |
| at0094 | Comparison study details | Study name | DV_TEXT |
| at0095 | Comparison study details | Study identifier | DV_IDENTIFIER / DV_TEXT |
| at0096 | Comparison study details | Study date | DV_DATE_TIME |
| at0097 | Comparison study details | Study end point | DV_TEXT / DV_URI |
| at0031 | Examination request details | Receiver order identifier | DV_IDENTIFIER / DV_CODED_TEXT |
| at0028 | Examination request details | Requester order identifier | DV_IDENTIFIER / DV_TEXT |
| at0029 | Examination request details | Examination requested name | DV_TEXT |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0006 |  | Structured target body site | openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 |
| at0044 |  | Structured imaging findings | openEHR-EHR-CLUSTER.imaging_exam(-[a-zA-Z0-9_]+)*.v1 |
| at0045 |  | Report representation | openEHR-EHR-CLUSTER.media_file(-[a-zA-Z0-9_]+)*.v1 |
| at0107 |  | Stabilising appliance | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0026 |  | Imaging service | openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 |
| at0041 |  | Structured technique/procedure | any archetype |
| at0065 |  | Series details | openEHR-EHR-CLUSTER.imaging_series(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.imaging_series(-[a-zA-Z0-9_]+)*.v1 |
| at0069 |  | Device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0067 | Comparison study details | Comparison series details | openEHR-EHR-CLUSTER.imaging_series(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.imaging_series(-[a-zA-Z0-9_]+)*.v1 |
| at0030 | Examination request details | Requester | openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.person(-[a-zA-Z0-9_]+)*.v1 |
| at0083 |  | Distribution list | openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.person(-[a-zA-Z0-9_]+)*.v1 |

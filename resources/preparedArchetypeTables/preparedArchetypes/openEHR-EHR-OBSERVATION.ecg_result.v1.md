# openEHR-EHR-OBSERVATION.ecg_result.v1

**Concept:** ECG result

**Category:** entry/observation

**Element leaves:** 58  |  **Cluster slot leaves:** 6  |  **Total leaves:** 64


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0100 |  | ECG type | DV_TEXT |
| at0094 |  | Atrial heart rate | DV_QUANTITY |
| at0013 |  | Ventricular heart rate | DV_QUANTITY |
| at0007 |  | QT interval global | DV_QUANTITY |
| at0008 |  | QTc interval global | DV_QUANTITY |
| at0012 |  | PR interval global | DV_QUANTITY |
| at0014 |  | QRS duration global | DV_QUANTITY |
| at0105 |  | RR interval global | DV_QUANTITY |
| at0096 |  | Clinical information provided | DV_TEXT |
| at0009 |  | Device interpretation | DV_TEXT |
| at0101 |  | Finding | DV_TEXT |
| at0081 |  | ECG diagnosis | DV_TEXT |
| at0089 |  | Conclusion | DV_TEXT |
| at0090 |  | Comment | DV_TEXT |
| at0020 |  | P axis | DV_QUANTITY / DV_TEXT |
| at0021 |  | QRS axis | DV_QUANTITY / DV_TEXT |
| at0022 |  | T axis | DV_QUANTITY / DV_TEXT |
| at0098 | Per-lead | Description | DV_TEXT |
| at0041 | Per-lead | P amplitude | DV_QUANTITY |
| at0028 | Per-lead | P duration | DV_QUANTITY |
| at0042 | Per-lead | P area | DV_QUANTITY |
| at0043 | Per-lead | P' amplitude | DV_QUANTITY |
| at0044 | Per-lead | P' duration | DV_QUANTITY |
| at0046 | Per-lead | P' area | DV_QUANTITY |
| at0048 | Per-lead | Q amplitude | DV_QUANTITY |
| at0049 | Per-lead | Q duration | DV_QUANTITY |
| at0050 | Per-lead | R amplitude | DV_QUANTITY |
| at0051 | Per-lead | R duration | DV_QUANTITY |
| at0053 | Per-lead | S amplitude | DV_QUANTITY |
| at0054 | Per-lead | S duration | DV_QUANTITY |
| at0055 | Per-lead | R' amplitude | DV_QUANTITY |
| at0056 | Per-lead | R' duration | DV_QUANTITY |
| at0057 | Per-lead | S' amplitude | DV_QUANTITY |
| at0058 | Per-lead | S' duration | DV_QUANTITY |
| at0059 | Per-lead | Ventricular Activation Time (VAT) | DV_QUANTITY |
| at0060 | Per-lead | QRS p-p | DV_QUANTITY |
| at0061 | Per-lead | QRS duration | DV_QUANTITY |
| at0062 | Per-lead | QRS area | DV_QUANTITY |
| at0063 | Per-lead | ST onset | DV_QUANTITY |
| at0064 | Per-lead | ST midpoint | DV_QUANTITY |
| at0065 | Per-lead | ST 80ms | DV_QUANTITY |
| at0106 | Per-lead | ST 60ms | DV_QUANTITY |
| at0066 | Per-lead | ST end | DV_QUANTITY |
| at0067 | Per-lead | ST duration | DV_QUANTITY |
| at0068 | Per-lead | ST slope | DV_QUANTITY |
| at0069 | Per-lead | ST segment morphology | DV_CODED_TEXT / DV_TEXT |
| at0073 | Per-lead | T amplitude | DV_QUANTITY |
| at0074 | Per-lead | T duration | DV_QUANTITY |
| at0075 | Per-lead | T area | DV_QUANTITY |
| at0115 | Per-lead | Lead comment | DV_TEXT |
| at0079 |  | Confounding factors | DV_TEXT |
| at0116 |  | Pacemaker stimulation | DV_TEXT |
| at0107 |  | Position | DV_CODED_TEXT |
| at0078 |  | Tilt | DV_QUANTITY |
| at0102 |  | Technical quality | DV_TEXT |
| at0097 |  | ECG lead placement | DV_TEXT |
| at0025 |  | QTc algorithm | DV_TEXT |
| at0095 |  | Device interpretation comment | DV_TEXT |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0083 |  | Multimedia representation | openEHR-EHR-CLUSTER.media_capture(-[a-zA-Z0-9_]+)*.v0 |
| at0114 | Per-lead | Lead details | any archetype |
| at0113 |  | Additional details | any archetype |
| at0080 |  | Level of exertion | openEHR-EHR-CLUSTER.level_of_exertion(-[a-zA-Z0-9_]+)*.v1 |
| at0076 |  | Recording device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0082 |  | Viewing device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |

# openEHR-EHR-OBSERVATION.ecg_result.v1

**Concept:** ECG result

**Category:** entry/observation

**Element leaves:** 58  |  **Cluster slot leaves:** 6  |  **Total leaves:** 64


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0100 | ECG type | DV_TEXT |
| at0094 | Atrial heart rate | DV_QUANTITY |
| at0013 | Ventricular heart rate | DV_QUANTITY |
| at0007 | QT interval global | DV_QUANTITY |
| at0008 | QTc interval global | DV_QUANTITY |
| at0012 | PR interval global | DV_QUANTITY |
| at0014 | QRS duration global | DV_QUANTITY |
| at0105 | RR interval global | DV_QUANTITY |
| at0096 | Clinical information provided | DV_TEXT |
| at0009 | Device interpretation | DV_TEXT |
| at0101 | Finding | DV_TEXT |
| at0081 | ECG diagnosis | DV_TEXT |
| at0089 | Conclusion | DV_TEXT |
| at0090 | Comment | DV_TEXT |
| at0020 | P axis | DV_QUANTITY / DV_TEXT |
| at0021 | QRS axis | DV_QUANTITY / DV_TEXT |
| at0022 | T axis | DV_QUANTITY / DV_TEXT |
| at0098 | Description | DV_TEXT |
| at0041 | P amplitude | DV_QUANTITY |
| at0028 | P duration | DV_QUANTITY |
| at0042 | P area | DV_QUANTITY |
| at0043 | P' amplitude | DV_QUANTITY |
| at0044 | P' duration | DV_QUANTITY |
| at0046 | P' area | DV_QUANTITY |
| at0048 | Q amplitude | DV_QUANTITY |
| at0049 | Q duration | DV_QUANTITY |
| at0050 | R amplitude | DV_QUANTITY |
| at0051 | R duration | DV_QUANTITY |
| at0053 | S amplitude | DV_QUANTITY |
| at0054 | S duration | DV_QUANTITY |
| at0055 | R' amplitude | DV_QUANTITY |
| at0056 | R' duration | DV_QUANTITY |
| at0057 | S' amplitude | DV_QUANTITY |
| at0058 | S' duration | DV_QUANTITY |
| at0059 | Ventricular Activation Time (VAT) | DV_QUANTITY |
| at0060 | QRS p-p | DV_QUANTITY |
| at0061 | QRS duration | DV_QUANTITY |
| at0062 | QRS area | DV_QUANTITY |
| at0063 | ST onset | DV_QUANTITY |
| at0064 | ST midpoint | DV_QUANTITY |
| at0065 | ST 80ms | DV_QUANTITY |
| at0106 | ST 60ms | DV_QUANTITY |
| at0066 | ST end | DV_QUANTITY |
| at0067 | ST duration | DV_QUANTITY |
| at0068 | ST slope | DV_QUANTITY |
| at0069 | ST segment morphology | DV_CODED_TEXT / DV_TEXT |
| at0073 | T amplitude | DV_QUANTITY |
| at0074 | T duration | DV_QUANTITY |
| at0075 | T area | DV_QUANTITY |
| at0115 | Lead comment | DV_TEXT |
| at0079 | Confounding factors | DV_TEXT |
| at0116 | Pacemaker stimulation | DV_TEXT |
| at0107 | Position | DV_CODED_TEXT |
| at0078 | Tilt | DV_QUANTITY |
| at0102 | Technical quality | DV_TEXT |
| at0097 | ECG lead placement | DV_TEXT |
| at0025 | QTc algorithm | DV_TEXT |
| at0095 | Device interpretation comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0083 | Multimedia representation | openEHR-EHR-CLUSTER.media_capture(-[a-zA-Z0-9_]+)*.v0 |
| at0114 | Lead details | any archetype |
| at0113 | Additional details | any archetype |
| at0080 | Level of exertion | openEHR-EHR-CLUSTER.level_of_exertion(-[a-zA-Z0-9_]+)*.v1 |
| at0076 | Recording device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0082 | Viewing device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |

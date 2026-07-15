# openEHR-EHR-OBSERVATION.laboratory_test_result.v1

**Concept:** Laboratory test result

**Category:** entry/observation

**Element leaves:** 15  |  **Cluster slot leaves:** 9  |  **Total leaves:** 24


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0005 | Test name | DV_TEXT |
| at0073 | Overall test status | DV_CODED_TEXT / DV_TEXT |
| at0075 | Overall test status timestamp | DV_DATE_TIME |
| at0077 | Diagnostic service category | DV_TEXT |
| at0100 | Clinical information provided | DV_TEXT |
| at0057 | Conclusion | DV_TEXT |
| at0098 | Test diagnosis | DV_TEXT |
| at0101 | Comment | DV_TEXT |
| at0113 | Confounding factors | DV_TEXT |
| at0068 | Laboratory internal identifier | DV_IDENTIFIER / DV_TEXT |
| at0106 | Original test requested name | DV_TEXT |
| at0062 | Requester order identifier | DV_IDENTIFIER / DV_TEXT |
| at0063 | Receiver order identifier | DV_IDENTIFIER / DV_TEXT |
| at0111 | Point-of-care test | DV_BOOLEAN |
| at0121 | Test method | any |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0065 | Specimen detail | openEHR-EHR-CLUSTER.specimen(-[a-zA-Z0-9_]+)*.v1 |
| at0097 | Test result | openEHR-EHR-CLUSTER.laboratory_test_analyte(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.laboratory_test_panel(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.laboratory_test_panel(-[a-zA-Z0-9_]+)*.v1 |
| at0122 | Structured test diagnosis | any archetype |
| at0118 | Multimedia representation | openEHR-EHR-CLUSTER.media_file(-[a-zA-Z0-9_]+)*.v1 |
| at0114 | Structured confounding factors | any archetype |
| at0017 | Receiving laboratory | openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 |
| at0090 | Requester | openEHR-EHR-CLUSTER.person(-[a-zA-Z0-9_]+)*.v1 |
| at0035 | Distribution list | openEHR-EHR-CLUSTER.distribution(-[a-zA-Z0-9_]+)*.v1 |
| at0110 | Testing details | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |

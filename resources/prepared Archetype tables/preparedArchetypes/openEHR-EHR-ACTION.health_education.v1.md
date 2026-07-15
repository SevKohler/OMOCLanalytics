# openEHR-EHR-ACTION.health_education.v1

**Concept:** Health education

**Category:** entry/action

**Element leaves:** 11  |  **Cluster slot leaves:** 6  |  **Total leaves:** 17


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0002 | Topic name | DV_TEXT |
| at0003 | Description | DV_TEXT |
| at0035 | Clinical indication | DV_TEXT |
| at0004 | Method | DV_TEXT |
| at0020 | Session Number | DV_COUNT |
| at0010 | Reason | DV_TEXT |
| at0019 | Outcome | DV_TEXT |
| at0026 | Scheduled date/ time | DV_DATE_TIME |
| at0027 | Comment | DV_TEXT |
| at0030 | Requestor order identifier | DV_TEXT / DV_IDENTIFIER |
| at0031 | Receiver order identifier | DV_TEXT / DV_IDENTIFIER |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0025 | Material details | openEHR-EHR-CLUSTER.multimedia(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.multimedia(-[a-zA-Z0-9_]+)*.v0 |
| at0033 | Additional details | any archetype |
| at0028 | Requestor | openEHR-EHR-CLUSTER.individual_professional(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v0 |
| at0029 | Receiver | openEHR-EHR-CLUSTER.individual_professional(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v0 |
| at0032 | Recipient | openEHR-EHR-CLUSTER.individual_personal(-[a-zA-Z0-9_]+)*.v1 |
| at0034 | Interpreter details | openEHR-EHR-CLUSTER.interpreter_details(-[a-zA-Z0-9_]+)*.v0 |

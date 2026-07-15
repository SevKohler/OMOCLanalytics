# openEHR-EHR-EVALUATION.advance_care_directive.v2

**Concept:** Advance care directive

**Category:** entry/evaluation

**Element leaves:** 10  |  **Cluster slot leaves:** 4  |  **Total leaves:** 14


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0005 |  | Type of directive | DV_TEXT |
| at0004 |  | Status | DV_CODED_TEXT / DV_TEXT |
| at0006 |  | Description | DV_TEXT |
| at0007 |  | Condition | DV_TEXT |
| at0038 |  | Comment | DV_TEXT |
| at0053 |  | Valid period start | DV_DATE_TIME |
| at0054 |  | Valid period end | DV_DATE_TIME |
| at0056 |  | Review due date | DV_DATE_TIME |
| at0027 |  | Mandate | DV_TEXT / DV_URI |
| at0030 | Directive location | Location | DV_TEXT / DV_URI |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0052 |  | Directive detail | any archetype |
| at0025 |  | Witness | openEHR-EHR-CLUSTER.person(-[a-zA-Z0-9_]+)*.v1 |
| at0060 |  | Digital representation | openEHR-EHR-CLUSTER.media_file(-[a-zA-Z0-9_]+)*.v1 |
| at0059 | Directive location | Copy holder | openEHR-EHR-CLUSTER.person(-[a-zA-Z0-9_]+)*.v1 |

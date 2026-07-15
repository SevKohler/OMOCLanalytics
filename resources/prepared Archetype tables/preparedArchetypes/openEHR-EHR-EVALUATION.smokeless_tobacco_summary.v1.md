# openEHR-EHR-EVALUATION.smokeless_tobacco_summary.v1

**Concept:** Smokeless tobacco summary

**Category:** entry/evaluation

**Element leaves:** 30  |  **Cluster slot leaves:** 3  |  **Total leaves:** 33


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0089 | Overall status | DV_CODED_TEXT |
| at0043 | Overall description | DV_TEXT |
| at0015 | Regular use commenced | DV_DATE |
| at0080 | Daily use commenced | DV_DATE |
| at0098 | Type | DV_TEXT |
| at0052 | Status | DV_CODED_TEXT |
| at0053 | Description | DV_TEXT |
| at0081 | Episode label | DV_COUNT / DV_TEXT |
| at0013 | Episode start date | DV_DATE |
| at0082 | Episode end date | DV_DATE |
| at0100 | Status | DV_CODED_TEXT |
| at0030 | Pattern | DV_CODED_TEXT / DV_TEXT |
| at0065 | Typical use | DV_QUANTITY |
| at0023 | Typical frequency | DV_QUANTITY |
| at0025 | Number of quit attempts | DV_COUNT |
| at0087 | Episode comment | DV_TEXT |
| at0014 | Quit date | DV_DATE |
| at0017 | Pack years | DV_COUNT |
| at0069 | Comment | DV_TEXT |
| at0016 | Overall quit date | DV_DATE |
| at0074 | Overall pack years | DV_COUNT |
| at0099 | Overall years of use | DV_QUANTITY |
| at0019 | Overall comment | DV_TEXT |
| at0071 | Quit date definition | DV_TEXT |
| at0085 | Quit attempt definition | DV_TEXT |
| at0075 | Current user definition | DV_TEXT |
| at0076 | Former user definition | DV_TEXT |
| at0079 | Never used definition | DV_TEXT |
| at0072 | Pack definition | DV_COUNT / DV_QUANTITY |
| at0022 | Last updated | DV_DATE_TIME |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0026 | Episode details | openEHR-EHR-CLUSTER.cessation_attempts(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.cessation_attempts(-[a-zA-Z0-9_]+)*.v0 |
| at0077 | Type details | any archetype |
| at0086 | Overall details | any archetype |

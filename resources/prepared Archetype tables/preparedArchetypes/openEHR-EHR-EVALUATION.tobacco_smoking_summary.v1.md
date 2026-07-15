# openEHR-EHR-EVALUATION.tobacco_smoking_summary.v1

**Concept:** Tobacco smoking summary

**Category:** entry/evaluation

**Element leaves:** 29  |  **Cluster slot leaves:** 3  |  **Total leaves:** 32


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0089 | Overall status | DV_CODED_TEXT |
| at0043 | Overall description | DV_TEXT |
| at0015 | Regular smoking commenced | DV_DATE |
| at0080 | Daily smoking commenced | DV_DATE |
| at0052 | Status | DV_CODED_TEXT |
| at0053 | Description | DV_TEXT |
| at0081 | Episode label | DV_COUNT / DV_TEXT |
| at0013 | Episode start date | DV_DATE |
| at0082 | Episode end date | DV_DATE |
| at0030 | Pattern | DV_CODED_TEXT / DV_TEXT |
| at0023 | Typical use (units) | DV_QUANTITY |
| at0065 | Typical use (mass) | DV_QUANTITY |
| at0025 | Number of quit attempts | DV_COUNT |
| at0087 | Episode comment | DV_TEXT |
| at0014 | Quit date | DV_DATE |
| at0017 | Pack years | DV_COUNT |
| at0069 | Comment | DV_TEXT |
| at0016 | Overall quit date | DV_DATE |
| at0093 | Overall years of smoking | DV_QUANTITY |
| at0094 | Smoking index | DV_COUNT |
| at0074 | Overall pack years | DV_COUNT |
| at0019 | Overall comment | DV_TEXT |
| at0071 | Quit date definition | DV_TEXT |
| at0085 | Quit attempt definition | DV_TEXT |
| at0075 | Current smoker definition | DV_TEXT |
| at0076 | Former smoker definition | DV_TEXT |
| at0079 | Never smoked definition | DV_TEXT |
| at0072 | Pack definition | DV_COUNT / DV_QUANTITY |
| at0022 | Last updated | DV_DATE_TIME |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0026 | Episode details | openEHR-EHR-CLUSTER.cessation_attempts(-[a-zA-Z0-9_]+)*.v1 |
| at0077 | Type details | any archetype |
| at0086 | Overall details | openEHR-EHR-CLUSTER.change(-[a-zA-Z0-9_]+)*.v1 |

# openEHR-EHR-EVALUATION.tobacco_smoking_summary.v1

**Concept:** Tobacco smoking summary

**Category:** entry/evaluation

**Element leaves:** 28  |  **Cluster slot leaves:** 3  |  **Total leaves:** 31


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0089 |  | Overall status | DV_CODED_TEXT |
| at0043 |  | Overall description | DV_TEXT |
| at0015 |  | Regular smoking commenced | DV_DATE |
| at0080 |  | Daily smoking commenced | DV_DATE |
| at0052 | Per type | Status | DV_CODED_TEXT |
| at0053 | Per type | Description | DV_TEXT |
| at0081 | Per type > Per episode | Episode label | DV_COUNT / DV_TEXT |
| at0013 | Per type > Per episode | Episode start date | DV_DATE |
| at0082 | Per type > Per episode | Episode end date | DV_DATE |
| at0030 | Per type > Per episode | Pattern | DV_CODED_TEXT / DV_TEXT |
| at0023 | Per type > Per episode | Typical use (units) | DV_QUANTITY |
| at0065 | Per type > Per episode | Typical use (mass) | DV_QUANTITY |
| at0025 | Per type > Per episode | Number of quit attempts | DV_COUNT |
| at0087 | Per type > Per episode | Episode comment | DV_TEXT |
| at0014 | Per type | Quit date | DV_DATE |
| at0017 | Per type | Pack years | DV_COUNT |
| at0069 | Per type | Comment | DV_TEXT |
| at0016 |  | Overall quit date | DV_DATE |
| at0093 |  | Overall years of smoking | DV_QUANTITY |
| at0094 |  | Smoking index | DV_COUNT |
| at0074 |  | Overall pack years | DV_COUNT |
| at0019 |  | Overall comment | DV_TEXT |
| at0071 |  | Quit date definition | DV_TEXT |
| at0085 |  | Quit attempt definition | DV_TEXT |
| at0075 |  | Current smoker definition | DV_TEXT |
| at0076 |  | Former smoker definition | DV_TEXT |
| at0079 |  | Never smoked definition | DV_TEXT |
| at0072 |  | Pack definition | DV_COUNT / DV_QUANTITY |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0026 | Per type > Per episode | Episode details | openEHR-EHR-CLUSTER.cessation_attempts(-[a-zA-Z0-9_]+)*.v1 |
| at0077 | Per type | Type details | any archetype |
| at0086 |  | Overall details | openEHR-EHR-CLUSTER.change(-[a-zA-Z0-9_]+)*.v1 |

# openEHR-EHR-EVALUATION.alcohol_consumption_summary.v1

**Concept:** Alcohol consumption summary

**Category:** entry/evaluation

**Element leaves:** 32  |  **Cluster slot leaves:** 3  |  **Total leaves:** 35


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0089 |  | Overall status | DV_CODED_TEXT |
| at0043 |  | Overall description | DV_TEXT |
| at0015 |  | Regular consumption commenced | DV_DATE |
| at0080 |  | Daily consumption commenced | DV_DATE |
| at0114 |  | Date first intoxicated | DV_DATE_TIME |
| at0052 | Per episode | Status | DV_CODED_TEXT |
| at0112 | Per episode | Episode description | DV_TEXT |
| at0081 | Per episode | Episode label | DV_COUNT / DV_TEXT |
| at0013 | Per episode | Episode start date | DV_DATE |
| at0082 | Per episode | Episode end date | DV_DATE |
| at0030 | Per episode | Pattern | DV_CODED_TEXT / DV_TEXT |
| at0097 | Per episode | Binge drinking frequency | DV_QUANTITY / DV_INTERVAL |
| at0113 | Per episode | Binge drinking description | DV_TEXT |
| at0110 | Per episode | Alcohol free days | DV_QUANTITY |
| at0023 | Per episode | Typical consumption (alcohol units) | DV_QUANTITY |
| at0122 | Per episode | Typical consumption (mass) | DV_QUANTITY |
| at0108 | Per episode > Per type | Type | DV_TEXT / DV_CODED_TEXT |
| at0053 | Per episode > Per type | Description | DV_TEXT |
| at0111 | Per episode > Per type | Typical consumption (alcohol units) | DV_QUANTITY |
| at0127 | Per episode > Per type | Typical consumption (mass) | DV_QUANTITY |
| at0069 | Per episode > Per type | Comment | DV_TEXT |
| at0025 | Per episode | Number of quit attempts | DV_COUNT |
| at0014 | Per episode | Quit date | DV_DATE |
| at0087 | Per episode | Episode comment | DV_TEXT |
| at0016 |  | Overall quit date | DV_DATE |
| at0019 |  | Overall comment | DV_TEXT |
| at0071 |  | Quit date definition | DV_TEXT |
| at0085 |  | Quit attempt definition | DV_TEXT |
| at0079 |  | Lifetime non-drinker definition | DV_TEXT |
| at0075 |  | Current drinker definition | DV_TEXT |
| at0076 |  | Former drinker definition | DV_TEXT |
| at0104 |  | Alcohol unit definition (mass) | DV_QUANTITY |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0077 | Per episode > Per type | Type details | .* / openEHR-EHR-CLUSTER.alcohol_consumption.v0 |
| at0026 | Per episode | Episode details | openEHR-EHR-CLUSTER.cessation_attempts(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.alcohol_consumption.v0 |
| at0086 |  | Overall details | any archetype |

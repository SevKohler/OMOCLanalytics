# openEHR-EHR-EVALUATION.alcohol_consumption_summary.v1

**Concept:** Alcohol consumption summary

**Category:** entry/evaluation

**Element leaves:** 33  |  **Cluster slot leaves:** 3  |  **Total leaves:** 36


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0089 | Overall status | DV_CODED_TEXT |
| at0043 | Overall description | DV_TEXT |
| at0015 | Regular consumption commenced | DV_DATE |
| at0080 | Daily consumption commenced | DV_DATE |
| at0114 | Date first intoxicated | DV_DATE_TIME |
| at0052 | Status | DV_CODED_TEXT |
| at0112 | Episode description | DV_TEXT |
| at0081 | Episode label | DV_COUNT / DV_TEXT |
| at0013 | Episode start date | DV_DATE |
| at0082 | Episode end date | DV_DATE |
| at0030 | Pattern | DV_CODED_TEXT / DV_TEXT |
| at0097 | Binge drinking frequency | DV_QUANTITY / DV_INTERVAL |
| at0113 | Binge drinking description | DV_TEXT |
| at0110 | Alcohol free days | DV_QUANTITY |
| at0023 | Typical consumption (alcohol units) | DV_QUANTITY |
| at0122 | Typical consumption (mass) | DV_QUANTITY |
| at0108 | Type | DV_TEXT / DV_CODED_TEXT |
| at0053 | Description | DV_TEXT |
| at0111 | Typical consumption (alcohol units) | DV_QUANTITY |
| at0127 | Typical consumption (mass) | DV_QUANTITY |
| at0069 | Comment | DV_TEXT |
| at0025 | Number of quit attempts | DV_COUNT |
| at0014 | Quit date | DV_DATE |
| at0087 | Episode comment | DV_TEXT |
| at0016 | Overall quit date | DV_DATE |
| at0019 | Overall comment | DV_TEXT |
| at0071 | Quit date definition | DV_TEXT |
| at0085 | Quit attempt definition | DV_TEXT |
| at0079 | Lifetime non-drinker definition | DV_TEXT |
| at0075 | Current drinker definition | DV_TEXT |
| at0076 | Former drinker definition | DV_TEXT |
| at0104 | Alcohol unit definition (mass) | DV_QUANTITY |
| at0022 | Last updated | DV_DATE_TIME |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0077 | Type details | .* / openEHR-EHR-CLUSTER.alcohol_consumption.v0 |
| at0026 | Episode details | openEHR-EHR-CLUSTER.cessation_attempts(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.alcohol_consumption.v0 |
| at0086 | Overall details | any archetype |

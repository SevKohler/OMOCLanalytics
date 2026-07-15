# openEHR-EHR-EVALUATION.alcohol_consumption_summary.v1

**Concept:** Alcohol consumption summary

**Primary OMOP table:** Observation  |  **Leaves:** 35  |  **Mapped to primary:** 3  |  **Externalised to a separate record:** 2  |  **Not mapped (auxiliary):** 30

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0089 | element | Overall status | `value` @ Observation |
| at0015 | element | Regular consumption commenced | `observation_date` @ Observation |
| at0080 | element | Daily consumption commenced | `observation_date` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0023 | element | Per episode > Typical consumption (alcohol units) | `value` @ Observation |
| at0016 | element | Overall quit date | `observation_date` @ Observation |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0043 | element | Overall description |
| at0114 | element | Date first intoxicated |
| at0052 | element | Per episode > Status |
| at0112 | element | Per episode > Episode description |
| at0081 | element | Per episode > Episode label |
| at0013 | element | Per episode > Episode start date |
| at0082 | element | Per episode > Episode end date |
| at0030 | element | Per episode > Pattern |
| at0097 | element | Per episode > Binge drinking frequency |
| at0113 | element | Per episode > Binge drinking description |
| at0110 | element | Per episode > Alcohol free days |
| at0122 | element | Per episode > Typical consumption (mass) |
| at0108 | element | Per episode > Per type > Type |
| at0053 | element | Per episode > Per type > Description |
| at0111 | element | Per episode > Per type > Typical consumption (alcohol units) |
| at0127 | element | Per episode > Per type > Typical consumption (mass) |
| at0069 | element | Per episode > Per type > Comment |
| at0025 | element | Per episode > Number of quit attempts |
| at0014 | element | Per episode > Quit date |
| at0087 | element | Per episode > Episode comment |
| at0019 | element | Overall comment |
| at0071 | element | Quit date definition |
| at0085 | element | Quit attempt definition |
| at0079 | element | Lifetime non-drinker definition |
| at0075 | element | Current drinker definition |
| at0076 | element | Former drinker definition |
| at0104 | element | Alcohol unit definition (mass) |
| at0077 | slot | Per episode > Per type > Type details |
| at0026 | slot | Per episode > Episode details |
| at0086 | slot | Overall details |

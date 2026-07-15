# openEHR-EHR-EVALUATION.smokeless_tobacco_summary.v1

**Concept:** Smokeless tobacco summary

**Primary OMOP table:** Observation  |  **Leaves:** 32  |  **Mapped to primary:** 2  |  **Externalised to a separate record:** 2  |  **Not mapped (auxiliary):** 28

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0089 | element | Overall status | `value` @ Observation |
| at0043 | element | Overall description | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0016 | element | Overall quit date | `value` @ Observation |
| at0074 | element | Overall pack years | `value` @ Measurement |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0015 | element | Regular use commenced |
| at0080 | element | Daily use commenced |
| at0098 | element | Per type > Type |
| at0052 | element | Per type > Status |
| at0053 | element | Per type > Description |
| at0081 | element | Per type > Per episode > Episode label |
| at0013 | element | Per type > Per episode > Episode start date |
| at0082 | element | Per type > Per episode > Episode end date |
| at0100 | element | Per type > Per episode > Status |
| at0030 | element | Per type > Per episode > Pattern |
| at0065 | element | Per type > Per episode > Typical use |
| at0023 | element | Per type > Per episode > Typical frequency |
| at0025 | element | Per type > Per episode > Number of quit attempts |
| at0087 | element | Per type > Per episode > Episode comment |
| at0014 | element | Per type > Quit date |
| at0017 | element | Per type > Pack years |
| at0069 | element | Per type > Comment |
| at0099 | element | Overall years of use |
| at0019 | element | Overall comment |
| at0071 | element | Quit date definition |
| at0085 | element | Quit attempt definition |
| at0075 | element | Current user definition |
| at0076 | element | Former user definition |
| at0079 | element | Never used definition |
| at0072 | element | Pack definition |
| at0026 | slot | Per type > Per episode > Episode details |
| at0077 | slot | Per type > Type details |
| at0086 | slot | Overall details |

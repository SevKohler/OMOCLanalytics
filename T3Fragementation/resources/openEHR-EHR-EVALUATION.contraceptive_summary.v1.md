# openEHR-EHR-EVALUATION.contraceptive_summary.v1

**Concept:** Contraceptive use summary

**Primary OMOP table:** Observation  |  **Leaves:** 21  |  **Mapped to primary:** 2  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 19

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0089 | element | Overall status | `qualifier` @ Observation |
| at0151 | element | Per type > Type | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0043 | element | Overall description |
| at0144 | element | Per type > Status |
| at0053 | element | Per type > Description |
| at0148 | element | Per type > Start date |
| at0081 | element | Per type > Per episode > Episode label |
| at0023 | element | Per type > Per episode > Specific name |
| at0030 | element | Per type > Per episode > Description |
| at0168 | element | Per type > Per episode > Clinical indication |
| at0025 | element | Per type > Per episode > Goal |
| at0013 | element | Per type > Per episode > Episode start date |
| at0082 | element | Per type > Per episode > Episode end date |
| at0074 | element | Per type > Per episode > Reason for cessation |
| at0087 | element | Per type > Per episode > Episode comment |
| at0149 | element | Per type > End date |
| at0069 | element | Per type > Comment |
| at0019 | element | Overall comment |
| at0026 | slot | Per type > Per episode > Episode details |
| at0077 | slot | Per type > Type details |
| at0150 | slot | Overall details |

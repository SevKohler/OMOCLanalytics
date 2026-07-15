# openEHR-EHR-EVALUATION.education_summary.v1

**Concept:** Education summary

**Primary OMOP table:** Observation  |  **Leaves:** 7  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 6

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0018 | element | Description | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0003 | element | Age started |
| at0031 | element | Age ended |
| at0002 | element | Highest level completed |
| at0007 | element | Comment |
| at0029 | slot | Education record |
| at0030 | slot | Additional details |

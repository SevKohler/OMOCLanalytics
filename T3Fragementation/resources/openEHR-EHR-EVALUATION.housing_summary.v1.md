# openEHR-EHR-EVALUATION.housing_summary.v1

**Concept:** Housing summary

**Primary OMOP table:** Observation  |  **Leaves:** 4  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 3

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0002 | element | Description | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0005 | element | Comment |
| at0009 | slot | Housing record |
| at0003 | slot | Additional details |

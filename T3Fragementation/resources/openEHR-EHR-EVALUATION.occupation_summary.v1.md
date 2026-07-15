# openEHR-EHR-EVALUATION.occupation_summary.v1

**Concept:** Occupation summary

**Primary OMOP table:** Observation  |  **Leaves:** 5  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 4

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Employment status | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0002 | element | Description |
| at0006 | element | Comment |
| at0003 | slot | Occupation episode |
| at0005 | slot | Additional details |

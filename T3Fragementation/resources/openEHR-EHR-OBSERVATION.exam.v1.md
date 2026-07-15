# openEHR-EHR-OBSERVATION.exam.v1

**Concept:** Physical examination findings

**Primary OMOP table:** Observation  |  **Leaves:** 7  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 6

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0006 | element | Interpretation | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0004 | element | Description |
| at0011 | element | Comment |
| at0008 | element | Confounding factors |
| at0013 | element | Position |
| at0005 | slot | Examination detail |
| at0010 | slot | Device Details |

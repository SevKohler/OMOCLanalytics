# openEHR-EHR-OBSERVATION.qsofa_score.v1

**Concept:** qSOFA score

**Primary OMOP table:** Measurement  |  **Leaves:** 5  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 4

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0005 | element | qSOFA score | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0006 | element | Respiratory rate |
| at0007 | element | Blood pressure |
| at0008 | element | Mental status |
| at0004 | element | Comment |

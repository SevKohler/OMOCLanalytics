# openEHR-EHR-EVALUATION.precaution.v1

**Concept:** Precaution

**Primary OMOP table:** Observation  |  **Leaves:** 9  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 8

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0002 | element | Condition | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0014 | element | Status |
| at0003 | element | Evidence |
| at0013 | element | Category |
| at0008 | element | Comment |
| at0022 | element | Valid period start |
| at0024 | element | Valid period end |
| at0009 | element | Review date |
| at0025 | slot | Additional details |

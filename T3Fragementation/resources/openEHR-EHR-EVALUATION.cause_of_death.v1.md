# openEHR-EHR-EVALUATION.cause_of_death.v1

**Concept:** Cause of death

**Primary OMOP table:** Observation  |  **Leaves:** 10  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 9

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0002 | element | Direct cause | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0019 | element | Description |
| at0017 | element | Direct cause duration |
| at0004 | element | Antecedent cause(s) > Cause |
| at0005 | element | Antecedent cause(s) > Order |
| at0009 | element | Antecedent cause(s) > Duration |
| at0018 | element | Contributing conditions > Condition |
| at0021 | element | Contributing conditions > Duration |
| at0013 | element | Comment |
| at0012 | slot | Additional details |

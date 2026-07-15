# openEHR-EHR-EVALUATION.communication_capability.v1

**Concept:** Communication capability

**Primary OMOP table:** Observation  |  **Leaves:** 7  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 6

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0003 | slot | Per language > Language | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0002 | element | Description |
| at0021 | element | Per language > Comment |
| at0022 | element | Communication aid |
| at0009 | element | Overall comment |
| at0018 | slot | Per language > Capability details |
| at0005 | slot | Additional details |

# openEHR-EHR-ACTION.service.v1

**Concept:** Service

**Primary OMOP table:** Observation  |  **Leaves:** 15  |  **Mapped to primary:** 3  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 12

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0011 | element | Service name | `value` @ Observation |
| at0032 | element | Planned date/time | `observation_date` @ Observation |
| at0025 | element | Scheduled date/time | `observation_date` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0014 | element | Service type |
| at0013 | element | Description |
| at0021 | element | Sequence |
| at0012 | element | Reason |
| at0028 | element | Comment |
| at0016 | element | Requestor identifier |
| at0018 | element | Service provider identifier |
| at0027 | slot | Service detail |
| at0029 | slot | Multimedia representation |
| at0036 | slot | Additional details |
| at0017 | slot | Requestor |
| at0019 | slot | Receiver |

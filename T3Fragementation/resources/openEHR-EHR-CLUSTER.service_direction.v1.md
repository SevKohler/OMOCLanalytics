# openEHR-EHR-CLUSTER.service_direction.v1

**Concept:** Service direction

**Primary OMOP table:** Observation  |  **Leaves:** 9  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 8

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0001 | element | Direction sequence | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0002 | element | Direction description |
| at0004 | element | Activity > Activity sequence |
| at0005 | element | Activity > Amount |
| at0007 | element | Direction duration |
| at0011 | element | Total amount |
| at0006 | slot | Activity > Intraday timing |
| at0010 | slot | Repetition timing |
| at0012 | slot | Additional details |

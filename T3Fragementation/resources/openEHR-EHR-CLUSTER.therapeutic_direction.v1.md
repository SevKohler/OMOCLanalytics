# openEHR-EHR-CLUSTER.therapeutic_direction.v1

**Concept:** Therapeutic direction

**Primary OMOP table:** Observation  |  **Leaves:** 9  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 8

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0178 | element | Order start date/time | `observation_date` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0057 | element | Direction sequence |
| at0066 | element | Direction duration |
| at0172 | element | Number of administrations |
| at0177 | element | Review criterion |
| at0179 | element | Order stop date/time |
| at0176 | slot | Dosage |
| at0090 | slot | Repetition timing |
| at0156 | slot | Additional details |

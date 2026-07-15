# openEHR-EHR-OBSERVATION.msfc_score.v1

**Concept:** MSFC-Wert

**Primary OMOP table:** Observation  |  **Leaves:** 5  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 4

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | MSFC score | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0006 | element | Reference Population |
| at0007 | element | Timed 25-Foot Walk Record |
| at0008 | element | Nine Hole Peg Test Record |
| at0009 | element | Paced Auditory Serial Addition Test Record |

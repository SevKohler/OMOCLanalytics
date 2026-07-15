# openEHR-EHR-OBSERVATION.timed_25_foot_walk.v1

**Concept:** Timed 25-Foot Walk

**Primary OMOP table:** Observation  |  **Leaves:** 8  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 7

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Zeit | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0005 | element | Test nicht beendet? |
| at0006 | element | Gründe für Nichtbeenden |
| at0010 | element | Begleitumstände |
| at0012 | element | Unilaterale Gehhilfe |
| at0020 | element | Bilaterale Gehhilfen |
| at0017 | element | Mehr als zwei Anläufe? |
| at0018 | element | Gründe für mehr als zwei Anläufe |

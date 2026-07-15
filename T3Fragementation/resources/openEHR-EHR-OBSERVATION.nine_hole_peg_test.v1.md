# openEHR-EHR-OBSERVATION.nine_hole_peg_test.v1

**Concept:** Nine Hole Peg Test

**Primary OMOP table:** Measurement  |  **Leaves:** 13  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 1  |  **Not mapped (auxiliary):** 11

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0017 | element | Gesamtzeit | `value` @ Measurement, `unit` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0083 | element | Dominante Hand | `value` @ Observation |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0035 | element | Zwischenzeit |
| at0050 | element | Anzahl platzierter Stecker |
| at0051 | element | Anzahl zurückgelegter Stecker |
| at0080 | element | Testlauf nicht beendet? |
| at0081 | element | Grund für Nichtbeenden |
| at0064 | element | Begleitumstände |
| at0013 | element | Probelauf dominante Hand? |
| at0082 | element | Probelauf nichtdominante Hand? |
| at0087 | element | Mehr als zwei Anläufe? |
| at0088 | element | Grund für mehr als zwei Anläufe |
| at0084 | element | Stecker platziert aber nicht zurückgelegt |

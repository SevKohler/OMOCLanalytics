# openEHR-EHR-OBSERVATION.paced_auditory_serial_addition_test.v1

**Concept:** Paced Auditory Serial Addition Test

**Primary OMOP table:** Measurement  |  **Leaves:** 13  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 12

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0015 | element | Anzahl korrekter Ergebnisse | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0029 | element | Anzahl korrekter Ergebnisse in der ersten Hälfte |
| at0030 | element | Anzahl korrekter Ergebnisse in der zweiten Hälfte |
| at0031 | element | Anzahl der Rechenfehler |
| at0032 | element | Anzahl der Auslassungsfehler |
| at0063 | element | Prozentwert korrekter Ergebnisse |
| at0055 | element | Test nicht beendet? |
| at0049 | element | Grund für Nichtbeenden |
| at0054 | element | Begleitumstände |
| at0012 | element | Verwendete Zahlensequenz |
| at0068 | element | Übungssequenz durchgeführt? |
| at0069 | element | Zusätzliche Anläufe? |
| at0070 | element | Grund für zusätzliche Anläufe |

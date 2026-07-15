# openEHR-EHR-OBSERVATION.news2.v1

**Concept:** National Early Warning Score 2 (NEWS2)

**Primary OMOP table:** Measurement  |  **Leaves:** 10  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 9

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0028 | element | Total score | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0006 | element | Respiration rate |
| at0029 | element | SpO₂ Scale 1 |
| at0047 | element | SpO₂ Scale 2 |
| at0034 | element | Air or oxygen? |
| at0004 | element | Systolic blood pressure |
| at0005 | element | Pulse |
| at0008 | element | Consciousness |
| at0007 | element | Temperature |
| at0056 | element | Clinical risk category |

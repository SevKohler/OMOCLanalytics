# openEHR-EHR-OBSERVATION.respiration.v2

**Concept:** Respiration

**Primary OMOP table:** Measurement  |  **Leaves:** 11  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 10

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Rate | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0062 | element | Presence |
| at0005 | element | Regularity |
| at0016 | element | Depth |
| at0024 | element | Clinical description |
| at0009 | element | Clinical interpretation |
| at0070 | element | Comment |
| at0065 | element | Body position |
| at0056 | element | Confounding factors |
| at0055 | slot | Inspired oxygen |
| at0037 | slot | Exertion |

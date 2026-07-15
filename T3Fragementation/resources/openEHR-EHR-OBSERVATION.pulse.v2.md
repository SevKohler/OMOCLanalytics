# openEHR-EHR-OBSERVATION.pulse.v2

**Concept:** Pulse/Heart beat

**Primary OMOP table:** Measurement  |  **Leaves:** 14  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 13

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Rate | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at1005 | element | Presence |
| at0005 | element | Regularity |
| at1055 | element | Irregular type |
| at1030 | element | Character |
| at1022 | element | Clinical description |
| at1023 | element | Clinical interpretation |
| at1059 | element | Comment |
| at0013 | element | Position |
| at1018 | element | Confounding factors |
| at1019 | element | Method |
| at1037 | element | Body site |
| at1017 | slot | Exertion |
| at1013 | slot | Device |

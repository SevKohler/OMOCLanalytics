# openEHR-EHR-OBSERVATION.body_weight.v2

**Concept:** Body weight

**Primary OMOP table:** Measurement  |  **Leaves:** 5  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 4

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Weight | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0024 | element | Comment |
| at0009 | element | State of dress |
| at0025 | element | Confounding factors |
| at0020 | slot | Device |

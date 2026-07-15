# openEHR-EHR-OBSERVATION.height.v2

**Concept:** Height/Length

**Primary OMOP table:** Measurement  |  **Leaves:** 5  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 4

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Height/Length | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0018 | element | Comment |
| at0014 | element | Position |
| at0019 | element | Confounding factors |
| at0011 | slot | Device |

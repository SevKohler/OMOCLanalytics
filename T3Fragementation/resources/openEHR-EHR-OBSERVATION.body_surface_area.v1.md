# openEHR-EHR-OBSERVATION.body_surface_area.v1

**Concept:** Body surface area

**Primary OMOP table:** Measurement  |  **Leaves:** 6  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 5

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0008 | slot | Device | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0004 | element | Body Surface Area |
| at0019 | element | Comment |
| at0021 | element | Confounding factors |
| at0009 | element | Method |
| at0006 | element | Formula |

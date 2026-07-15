# openEHR-EHR-OBSERVATION.braden_scale.v1

**Concept:** Braden scale

**Primary OMOP table:** Measurement  |  **Leaves:** 8  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 7

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0022 | element | Total score | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0004 | element | Sensory perception |
| at0009 | element | Moisture |
| at0010 | element | Activity |
| at0019 | element | Mobility |
| at0020 | element | Nutrition |
| at0021 | element | Friction and shear |
| at0034 | element | Comment |

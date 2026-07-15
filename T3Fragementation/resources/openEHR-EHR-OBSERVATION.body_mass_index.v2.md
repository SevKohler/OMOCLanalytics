# openEHR-EHR-OBSERVATION.body_mass_index.v2

**Concept:** Body Mass Index (BMI)

**Primary OMOP table:** Measurement  |  **Leaves:** 6  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 5

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Body mass index | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0013 | element | Clinical interpretation |
| at0012 | element | Comment |
| at0011 | element | Confounding factors |
| at0006 | element | Method |
| at0010 | element | Formula |

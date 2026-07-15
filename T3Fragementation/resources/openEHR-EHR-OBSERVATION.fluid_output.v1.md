# openEHR-EHR-OBSERVATION.fluid_output.v1

**Concept:** Fluid output

**Primary OMOP table:** Measurement  |  **Leaves:** 8  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 1  |  **Not mapped (auxiliary):** 6

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0035 | element | Volume | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0036 | element | Fluid name | `value` @ Observation |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0041 | element | Source |
| at0032 | element | Comment |
| at0031 | element | Method |
| at0038 | slot | Fluid details |
| at0033 | slot | Output device |
| at0028 | slot | Measurement device |

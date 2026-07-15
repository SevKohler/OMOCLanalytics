# openEHR-EHR-OBSERVATION.menstruation.v1

**Concept:** Menstrual cycle

**Primary OMOP table:** Observation  |  **Leaves:** 8  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 2  |  **Not mapped (auxiliary):** 5

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Start of menses | `observation_date` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0005 | element | Duration of menses | `value` @ Measurement |
| at0013 | element | Blood clots | `value` @ Observation |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0006 | element | Description of the cycle |
| at0007 | element | Relative flow |
| at0032 | element | Comment |
| at0021 | element | Confounding factors |
| at0019 | slot | Additional details |

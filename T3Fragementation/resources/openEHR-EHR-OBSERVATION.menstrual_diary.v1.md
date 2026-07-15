# openEHR-EHR-OBSERVATION.menstrual_diary.v1

**Concept:** Menstrual diary

**Primary OMOP table:** Observation  |  **Leaves:** 7  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 2  |  **Not mapped (auxiliary):** 4

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Flow | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0010 | element | Volume | `value` @ Measurement |
| at0014 | element | Blood clots | `value` @ Observation |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0017 | element | Color |
| at0018 | element | Description |
| at0021 | element | Comment |
| at0020 | slot | Additional details |

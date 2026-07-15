# openEHR-EHR-OBSERVATION.nyha_heart_failure.v1

**Concept:** New York Heart Association functional classification

**Primary OMOP table:** Observation  |  **Leaves:** 3  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 1  |  **Not mapped (auxiliary):** 1

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Functional capacity | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0011 | element | Objective assessment | `value` @ Observation |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0017 | element | Confounding factors |

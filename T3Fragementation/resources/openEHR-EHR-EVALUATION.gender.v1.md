# openEHR-EHR-EVALUATION.gender.v1

**Concept:** Gender

**Primary OMOP table:** Observation  |  **Leaves:** 9  |  **Mapped to primary:** 2  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 7

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0022 | element | Administrative gender | `value` @ Observation |
| at0019 | element | Sex assigned at birth | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0026 | element | Legal gender |
| at0025 | element | Gender expression |
| at0001 | element | Gender identity |
| at0020 | element | Preferred pronoun |
| at0027 | element | Gender category |
| at0014 | element | Comment |
| at0023 | slot | Additional details |

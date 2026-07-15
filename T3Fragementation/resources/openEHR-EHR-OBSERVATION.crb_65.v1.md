# openEHR-EHR-OBSERVATION.crb_65.v1

**Concept:** CRB-65 score

**Primary OMOP table:** Measurement  |  **Leaves:** 6  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 5

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0017 | element | Total score | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0004 | element | Confusion |
| at0007 | element | Respiratory rate |
| at0010 | element | Blood pressure |
| at0014 | element | Age |
| at0018 | element | Grade |

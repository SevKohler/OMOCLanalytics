# openEHR-EHR-OBSERVATION.mayo_score.v1

**Concept:** Mayo score

**Primary OMOP table:** Observation  |  **Leaves:** 7  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 6

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0029 | element | Total Mayo score | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0009 | element | Stool frequency |
| at0014 | element | Rectal bleeding |
| at0019 | element | Endoscopy findings |
| at0024 | element | Global assessment |
| at0033 | element | Partial Mayo score |
| at0034 | element | Simplified Mayo score |

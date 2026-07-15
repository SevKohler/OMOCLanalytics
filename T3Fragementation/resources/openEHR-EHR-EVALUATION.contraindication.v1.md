# openEHR-EHR-EVALUATION.contraindication.v1

**Concept:** Contraindication

**Primary OMOP table:** Observation  |  **Leaves:** 10  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 9

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0002 | element | Contraindicated intervention | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0014 | element | Status |
| at0007 | element | Criticality |
| at0021 | element | Clinical indication |
| at0003 | element | Rationale |
| at0013 | element | Category |
| at0008 | element | Comment |
| at0022 | element | Valid period start |
| at0023 | element | Valid period end |
| at0009 | element | Review date |

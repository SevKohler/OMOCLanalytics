# openEHR-EHR-EVALUATION.financial_summary.v1

**Concept:** Financial summary

**Primary OMOP table:** Observation  |  **Leaves:** 6  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 5

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0003 | element | Financial security status | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0002 | element | Description |
| at0013 | element | Financial security description |
| at0007 | element | Main source of income |
| at0009 | element | Comment |
| at0008 | slot | Financial record |

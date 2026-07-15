# openEHR-EHR-OBSERVATION.revised_cardiac_risk_index.v1

**Concept:** Revised cardiac risk index

**Primary OMOP table:** Measurement  |  **Leaves:** 8  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 7

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0026 | element | Total score | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0007 | element | Ischemic heart disease |
| at0010 | element | Congestive heart failure |
| at0013 | element | Cerebrovascular disease |
| at0016 | element | Diabetes mellitus on insulin |
| at0004 | element | Elevated serum creatinine |
| at0022 | element | High risk surgery |
| at0027 | element | Estimated risk |

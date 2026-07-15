# openEHR-EHR-OBSERVATION.four_a_test.v1

**Concept:** 4AT

**Primary OMOP table:** Measurement  |  **Leaves:** 5  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 4

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0019 | element | Total score | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0004 | element | Alertness |
| at0008 | element | Abbreviated Mental Test 4 (AMT-4) score |
| at0012 | element | Attention |
| at0016 | element | Acute change or fluctuating course |

# openEHR-EHR-EVALUATION.last_menstrual_period.v1

**Concept:** Last menstrual period

**Primary OMOP table:** Measurement  |  **Leaves:** 4  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 3

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0002 | element | Date of onset (LMP) | `measurement_date` @ Measurement, `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0009 | element | Certainty |
| at0007 | element | Description |
| at0008 | element | Comment |

# openEHR-EHR-EVALUATION.advance_care_directive.v2

**Concept:** Advance care directive

**Primary OMOP table:** Observation  |  **Leaves:** 14  |  **Mapped to primary:** 3  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 11

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0005 | element | Type of directive | `value` @ Observation |
| at0004 | element | Status | `qualifier` @ Observation |
| at0053 | element | Valid period start | `observation_date` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0006 | element | Description |
| at0007 | element | Condition |
| at0038 | element | Comment |
| at0054 | element | Valid period end |
| at0056 | element | Review due date |
| at0027 | element | Mandate |
| at0030 | element | Directive location > Location |
| at0052 | slot | Directive detail |
| at0025 | slot | Witness |
| at0060 | slot | Digital representation |
| at0059 | slot | Directive location > Copy holder |

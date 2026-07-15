# openEHR-EHR-EVALUATION.advance_intervention_decisions.v1

**Concept:** Advance intervention decisions

**Primary OMOP table:** Observation  |  **Leaves:** 19  |  **Mapped to primary:** 2  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 17

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0002 | element | Intent of care | `qualifier` @ Observation |
| at0009 | element | CPR decision | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0056 | element | Rationale |
| at0008 | element | Decisions description |
| at0015 | element | Per intervention > Intervention |
| at0034 | element | Per intervention > Decision |
| at0039 | element | Per intervention > Precondition |
| at0040 | element | Per intervention > Comment |
| at0042 | element | Patient awareness |
| at0043 | element | Carer awareness |
| at0044 | element | Overall comment |
| at0047 | element | Valid period start |
| at0048 | element | Valid period end |
| at0049 | element | Review due |
| at0050 | element | Mandate |
| at0053 | element | Document location > Location |
| at0041 | slot | Additional details |
| at0051 | slot | Digital representation |
| at0054 | slot | Document location > Copy holder |

# openEHR-EHR-OBSERVATION.social_context_screening.v1

**Concept:** Social context screening questionnaire

**Primary OMOP table:** Observation  |  **Leaves:** 8  |  **Mapped to primary:** 2  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 6

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Specific social context > Context | `value` @ Observation |
| at0005 | element | Specific social context > Presence? | `qualifier` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0034 | element | Screening purpose |
| at0051 | element | Specific social context > Timing |
| at0025 | element | Specific social context > Comment |
| at0052 | element | Overall comment |
| at0026 | slot | Specific social context > Additional details |
| at0044 | slot | Additional details |

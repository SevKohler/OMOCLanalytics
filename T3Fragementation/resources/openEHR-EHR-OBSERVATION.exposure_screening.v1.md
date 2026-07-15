# openEHR-EHR-OBSERVATION.exposure_screening.v1

**Concept:** Exposure screening questionnaire

**Primary OMOP table:** Observation  |  **Leaves:** 10  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 9

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0020 | element | Agent name | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0004 | element | Screening purpose |
| at0005 | element | Any exposure? |
| at0022 | element | Description |
| at0010 | element | Specific exposure > Situation |
| at0011 | element | Specific exposure > Presence? |
| at0015 | element | Specific exposure > Timing |
| at0017 | element | Specific exposure > Comment |
| at0016 | slot | Specific exposure > Additional details |
| at0023 | slot | Additional details |

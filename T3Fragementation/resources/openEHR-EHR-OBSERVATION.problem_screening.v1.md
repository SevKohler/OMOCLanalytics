# openEHR-EHR-OBSERVATION.problem_screening.v1

**Concept:** Problem/Diagnosis screening questionnaire

**Primary OMOP table:** Observation  |  **Leaves:** 9  |  **Mapped to primary:** 3  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 6

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Specific problem or diagnosis > Problem/diagnosis name | `value` @ Observation |
| at0005 | element | Specific problem or diagnosis > Presence? | `qualifier` @ Observation |
| at0040 | element | Specific problem or diagnosis > Timing | `observation_date` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0034 | element | Screening purpose |
| at0028 | element | Any problems or diagnoses? |
| at0043 | element | Description |
| at0025 | element | Specific problem or diagnosis > Comment |
| at0039 | slot | Specific problem or diagnosis > Additional details |
| at0042 | slot | Additional details |

# openEHR-EHR-OBSERVATION.symptom_sign_screening.v1

**Concept:** Symptom/sign screening questionnaire

**Primary OMOP table:** Observation  |  **Leaves:** 10  |  **Mapped to primary:** 3  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 7

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Specific symptom/sign > Symptom/sign name | `value` @ Observation |
| at0005 | element | Specific symptom/sign > Presence? | `qualifier` @ Observation |
| at0037 | element | Specific symptom/sign > Timing | `observation_date` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0034 | element | Screening purpose |
| at0028 | element | Any symptoms or signs? |
| at0029 | element | Onset |
| at0036 | element | Description |
| at0035 | element | Specific symptom/sign > Comment |
| at0026 | slot | Specific symptom/sign > Additional details |
| at0039 | slot | Additional details |

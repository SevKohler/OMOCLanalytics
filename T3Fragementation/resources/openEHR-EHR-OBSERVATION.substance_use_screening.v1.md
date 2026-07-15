# openEHR-EHR-OBSERVATION.substance_use_screening.v1

**Concept:** Substance use screening questionnaire

**Primary OMOP table:** Observation  |  **Leaves:** 11  |  **Mapped to primary:** 3  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 8

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0021 | element | Specific substance > Substance name | `value` @ Observation |
| at0003 | element | Specific substance > Last used | `observation_date` @ Observation |
| at0002 | element | Specific substance > Timing | `observation_date` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0040 | element | Screening purpose |
| at0052 | element | Any substance use? |
| at0042 | element | Description |
| at0024 | element | Specific substance > Used? |
| at0025 | element | Specific substance > Comment |
| at0056 | element | Overall comment |
| at0041 | slot | Specific substance > Additional details |
| at0043 | slot | Additional details |

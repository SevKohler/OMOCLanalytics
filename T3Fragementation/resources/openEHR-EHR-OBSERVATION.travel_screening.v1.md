# openEHR-EHR-OBSERVATION.travel_screening.v1

**Concept:** Travel screening questionnaire

**Primary OMOP table:** Observation  |  **Leaves:** 9  |  **Mapped to primary:** 3  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 6

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0021 | element | Specific travel > Travel activity | `value` @ Observation |
| at0024 | element | Specific travel > Occurred? | `qualifier` @ Observation |
| at0003 | element | Specific travel > Timing | `observation_date` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0027 | element | Any travel? |
| at0040 | element | Screening purpose |
| at0043 | element | Description |
| at0025 | element | Specific travel > Comment |
| at0041 | slot | Specific travel > Additional details |
| at0044 | slot | Additional details |

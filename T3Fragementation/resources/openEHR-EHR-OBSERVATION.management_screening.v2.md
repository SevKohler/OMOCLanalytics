# openEHR-EHR-OBSERVATION.management_screening.v2

**Concept:** Management screening questionnaire

**Primary OMOP table:** Measurement  |  **Leaves:** 9  |  **Mapped to primary:** 3  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 6

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Management activity > Management name | `concept_id` @ Measurement |
| at0005 | element | Management activity > Specific management? | `value` @ Measurement |
| at0037 | element | Management activity > Timing | `measurement_date` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0034 | element | Screening purpose |
| at0039 | element | Any management? |
| at0044 | element | Description |
| at0035 | element | Management activity > Comment |
| at0036 | slot | Management activity > Additional details |
| at0043 | slot | Additional details |

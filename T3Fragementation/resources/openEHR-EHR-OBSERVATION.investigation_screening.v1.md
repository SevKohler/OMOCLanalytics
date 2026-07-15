# openEHR-EHR-OBSERVATION.investigation_screening.v1

**Concept:** Diagnostic investigation screening questionnaire

**Primary OMOP table:** Observation  |  **Leaves:** 11  |  **Mapped to primary:** 3  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 8

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0021 | element | Specific investigation > Investigation name | `concept_id` @ Observation |
| at0003 | element | Specific investigation > Timing | `observation_date` @ Observation |
| at0002 | element | Specific investigation > Conclusion | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0040 | element | Screening purpose |
| at0027 | element | Any investigations? |
| at0043 | element | Description |
| at0024 | element | Specific investigation > Done? |
| at0047 | element | Specific investigation > Type |
| at0025 | element | Specific investigation > Comment |
| at0041 | slot | Specific investigation > Additional details |
| at0044 | slot | Additional details |

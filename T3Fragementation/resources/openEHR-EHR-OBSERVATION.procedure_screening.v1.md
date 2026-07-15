# openEHR-EHR-OBSERVATION.procedure_screening.v1

**Concept:** Procedure screening questionnaire

**Primary OMOP table:** ProcedureOccurrence  |  **Leaves:** 9  |  **Mapped to primary:** 2  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 7

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Specific procedure > Procedure name | `concept_id` @ ProcedureOccurrence |
| at0037 | element | Specific procedure > Timing | `procedure_start_date` @ ProcedureOccurrence, `procedure_end_date` @ ProcedureOccurrence |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0034 | element | Screening purpose |
| at0028 | element | Any previous procedures? |
| at0041 | element | Description |
| at0005 | element | Specific procedure > Carried out? |
| at0025 | element | Specific procedure > Comment |
| at0036 | slot | Specific procedure > Additional details |
| at0040 | slot | Additional details |

# openEHR-EHR-EVALUATION.problem_diagnosis.v1

**Concept:** Problem/Diagnosis

**Primary OMOP table:** ConditionOccurrence  |  **Leaves:** 16  |  **Mapped to primary:** 4  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 12

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0002 | element | Problem/Diagnosis name | `concept_id` @ ConditionOccurrence |
| at0077 | element | Date/time of onset | `condition_start_date` @ ConditionOccurrence |
| at0030 | element | Date/time of resolution | `condition_end_date` @ ConditionOccurrence |
| at0046 | slot | Status | `condition_status_concept_id` @ ConditionOccurrence |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0079 | element | Variant |
| at0009 | element | Clinical description |
| at0012 | element | Body site |
| at0078 | element | Cause |
| at0003 | element | Date/time clinically recognised |
| at0005 | element | Severity |
| at0080 | element | Impact |
| at0072 | element | Course description |
| at0073 | element | Diagnostic certainty |
| at0069 | element | Comment |
| at0039 | slot | Structured body site |
| at0043 | slot | Specific details |

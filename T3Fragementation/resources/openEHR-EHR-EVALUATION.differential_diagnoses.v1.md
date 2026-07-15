# openEHR-EHR-EVALUATION.differential_diagnoses.v1

**Concept:** Differential diagnoses

**Primary OMOP table:** ConditionOccurrence  |  **Leaves:** 7  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 6

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Per differential > Diagnosis name | `concept_id` @ ConditionOccurrence |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0002 | element | Overall description |
| at0005 | element | Per differential > Status |
| at0009 | element | Per differential > Rationale |
| at0011 | element | Per differential > Order |
| at0012 | element | Per differential > Comment |
| at0010 | slot | Per differential > Clinical evidence |

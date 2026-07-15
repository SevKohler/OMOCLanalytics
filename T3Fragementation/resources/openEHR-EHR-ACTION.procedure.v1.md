# openEHR-EHR-ACTION.procedure.v1

**Concept:** Procedure

**Primary OMOP table:** ProcedureOccurrence  |  **Leaves:** 25  |  **Mapped to primary:** 3  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 22

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0002 | element | Procedure name | `concept_id` @ ProcedureOccurrence |
| at0066 | element | Scheduled datetime | `procedure_start_date` @ ProcedureOccurrence |
| at0060 | element | End datetime | `procedure_end_date` @ ProcedureOccurrence |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0049 | element | Description |
| at0070 | element | Indication |
| at0072 | element | Intent |
| at0065 | element | Method |
| at0058 | element | Urgency |
| at0063 | element | Body site |
| at0071 | element | Impact |
| at0048 | element | Outcome |
| at0069 | element | Procedural difficulty |
| at0006 | element | Complication |
| at0073 | element | Start datetime |
| at0061 | element | Total duration |
| at0074 | element | Pathway step duration |
| at0067 | element | Procedure type |
| at0014 | element | Reason |
| at0005 | element | Comment |
| at0054 | element | Requestor order identifier |
| at0056 | element | Receiver order identifier |
| at0003 | slot | Procedure detail |
| at0062 | slot | Multimedia |
| at0055 | slot | Requestor |
| at0057 | slot | Receiver |

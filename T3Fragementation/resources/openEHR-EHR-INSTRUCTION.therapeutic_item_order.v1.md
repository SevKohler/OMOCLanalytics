# openEHR-EHR-INSTRUCTION.therapeutic_item_order.v1

**Concept:** Therapeutic item order

**Primary OMOP table:** ProcedureOccurrence  |  **Leaves:** 15  |  **Mapped to primary:** 3  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 12

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0070 | element | Item name | `concept_id` @ ProcedureOccurrence |
| at0012 | element | Start date/time | `procedure_start_date` @ ProcedureOccurrence |
| at0013 | element | Stop date/time | `procedure_end_date` @ ProcedureOccurrence |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0092 | element | Body site |
| at0009 | element | Directions |
| at0107 | element | Monitoring instruction |
| at0018 | element | Clinical indication |
| at0148 | element | Therapeutic intent |
| at0011 | element | Start criterion |
| at0016 | element | Stop criterion |
| at0167 | element | Comment |
| at0004 | element | Order identifier |
| at0143 | slot | Item details |
| at0093 | slot | Structured body site |
| at0166 | slot | Additional details |

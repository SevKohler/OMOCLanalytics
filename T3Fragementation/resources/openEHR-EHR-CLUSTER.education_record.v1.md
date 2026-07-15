# openEHR-EHR-CLUSTER.education_record.v1

**Concept:** Education record

**Primary OMOP table:** Measurement  |  **Leaves:** 9  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 8

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0008 | element | Description | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0001 | element | Educational institution |
| at0003 | element | Milestone |
| at0004 | element | Field of study |
| at0005 | element | Date started |
| at0006 | element | Date ended |
| at0010 | element | Comment |
| at0002 | slot | Organisation details |
| at0009 | slot | Additional details |

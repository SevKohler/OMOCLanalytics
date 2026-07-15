# openEHR-EHR-CLUSTER.person.v1

**Concept:** Person

**Primary OMOP table:** Observation  |  **Leaves:** 11  |  **Mapped to primary:** 2  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 9

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0001 | element | Name | `value` @ Observation |
| at0003 | element | Identifier | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0011 | element | Label |
| at0004 | element | Role |
| at0010 | element | Comment |
| at0002 | slot | Structured name |
| at0005 | slot | Address |
| at0006 | slot | Electronic communication |
| at0007 | slot | Organisation |
| at0008 | slot | Additional details |
| at0009 | slot | Photo |

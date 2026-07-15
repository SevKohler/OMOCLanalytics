# openEHR-EHR-CLUSTER.media_file.v1

**Concept:** Media file

**Primary OMOP table:** Observation  |  **Leaves:** 9  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 8

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0002 | element | Content name | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0001 | element | Content |
| at0010 | element | Identifier |
| at0005 | element | Description |
| at0004 | element | Created |
| at0007 | element | Comment |
| at0012 | slot | Creator |
| at0011 | slot | Source device |
| at0013 | slot | Additional details |

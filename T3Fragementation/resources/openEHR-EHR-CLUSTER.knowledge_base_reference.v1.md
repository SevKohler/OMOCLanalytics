# openEHR-EHR-CLUSTER.knowledge_base_reference.v1

**Concept:** Knowledge base reference

**Primary OMOP table:** Observation  |  **Leaves:** 8  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 7

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0001 | element | Knowledge base name | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0006 | element | Knowledge base version |
| at0008 | element | Knowledge base URI |
| at0005 | element | Item name |
| at0002 | element | Item version |
| at0007 | element | Item publication |
| at0003 | element | Item URI |
| at0004 | element | Comment |

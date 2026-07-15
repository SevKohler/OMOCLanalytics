# openEHR-EHR-CLUSTER.information_resource.v1

**Concept:** Information resource

**Primary OMOP table:** Observation  |  **Leaves:** 10  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 9

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0002 | element | Resource name | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0010 | element | Identifier |
| at0005 | element | Description |
| at0016 | element | Type of media |
| at0001 | element | Content |
| at0014 | element | Published |
| at0015 | element | Version |
| at0007 | element | Comment |
| at0012 | slot | Author |
| at0013 | slot | Additional details |

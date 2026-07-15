# openEHR-EHR-CLUSTER.occupation_record.v1

**Concept:** Occupation record

**Primary OMOP table:** Observation  |  **Leaves:** 12  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 11

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0005 | element | Job title/role | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0016 | element | Description |
| at0007 | element | Date commenced |
| at0001 | element | Paid employment status |
| at0013 | element | Full time equivalent |
| at0019 | element | Time allocated |
| at0002 | element | Industry category |
| at0006 | element | Job category |
| at0008 | element | Date ceased |
| at0014 | element | Comment |
| at0004 | slot | Organisation details |
| at0018 | slot | Additional details |

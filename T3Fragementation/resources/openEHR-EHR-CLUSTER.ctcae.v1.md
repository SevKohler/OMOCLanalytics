# openEHR-EHR-CLUSTER.ctcae.v1

**Concept:** Common Terminology Criteria for Adverse Events (CTCAE)

**Primary OMOP table:** Measurement  |  **Leaves:** 5  |  **Mapped to primary:** 2  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 3

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0002 | element | Term | `concept_id` @ Measurement |
| at0003 | element | Grade category | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0001 | element | Category |
| at0020 | element | Grade description |
| at0009 | element | CTCAE version |

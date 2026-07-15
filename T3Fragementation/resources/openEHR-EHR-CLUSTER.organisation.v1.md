# openEHR-EHR-CLUSTER.organisation.v1

**Concept:** Organisation

**Primary OMOP table:** Observation  |  **Leaves:** 9  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 8

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0001 | element | Name | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0003 | element | Identifier |
| at0004 | element | Role |
| at0019 | element | Comment |
| at0005 | slot | Address |
| at0022 | slot | Electronic communication |
| at0002 | slot | Contact person |
| at0021 | slot | Parent organisation |
| at0017 | slot | Additional details |

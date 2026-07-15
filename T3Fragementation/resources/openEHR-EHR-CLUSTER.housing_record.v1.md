# openEHR-EHR-CLUSTER.housing_record.v1

**Concept:** Housing record

**Primary OMOP table:** Observation  |  **Leaves:** 9  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 8

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0016 | element | Description | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0005 | element | Name/label |
| at0007 | element | Date commenced |
| at0001 | element | Residential setting |
| at0013 | element | Tenure |
| at0008 | element | Date ceased |
| at0014 | element | Comment |
| at0004 | slot | Address details |
| at0018 | slot | Additional details |

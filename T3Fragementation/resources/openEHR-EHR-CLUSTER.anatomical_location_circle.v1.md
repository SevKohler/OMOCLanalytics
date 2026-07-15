# openEHR-EHR-CLUSTER.anatomical_location_circle.v1

**Concept:** Circular anatomical location

**Primary OMOP table:** Observation  |  **Leaves:** 6  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 5

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0023 | element | Description | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0065 | element | Reference direction |
| at0079 | element | Centre landmark |
| at0061 | element | Circular direction |
| at0080 | element | Distance from landmark |
| at0054 | slot | Multimedia representation |

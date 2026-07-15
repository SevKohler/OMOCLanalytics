# openEHR-EHR-CLUSTER.anatomical_location_relative.v2

**Concept:** Relative anatomical location

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
| at0021 | element | Relative location > Landmark name |
| at0062 | element | Relative location > Laterality |
| at0022 | element | Relative location > Distance from landmark |
| at0006 | element | Relative location > Direction |
| at0054 | slot | Multimedia representation |

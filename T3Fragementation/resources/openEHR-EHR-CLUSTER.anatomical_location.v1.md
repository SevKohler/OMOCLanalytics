# openEHR-EHR-CLUSTER.anatomical_location.v1

**Concept:** Anatomical location

**Primary OMOP table:** Observation  |  **Leaves:** 8  |  **Mapped to primary:** 2  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 6

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0001 | element | Body site name | `value` @ Observation |
| at0065 | element | Specific site | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0002 | element | Laterality |
| at0064 | element | Aspect |
| at0055 | element | Anatomical Line |
| at0023 | element | Description |
| at0053 | slot | Alternative structure |
| at0054 | slot | Multimedia representation |

# openEHR-EHR-CLUSTER.range_of_motion.v1

**Concept:** Range of motion of a joint

**Primary OMOP table:** Observation  |  **Leaves:** 7  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 6

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0027 | element | Range of motion | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0002 | element | Movement |
| at0023 | element | Starting position |
| at0024 | element | Mode of examination |
| at0035 | element | Clinical interpretation |
| at0029 | element | Comment |
| at0028 | slot | Additional details |

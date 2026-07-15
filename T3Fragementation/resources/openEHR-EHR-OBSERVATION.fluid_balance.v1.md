# openEHR-EHR-OBSERVATION.fluid_balance.v1

**Concept:** Fluid balance

**Primary OMOP table:** Measurement  |  **Leaves:** 5  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 3  |  **Not mapped (auxiliary):** 1

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0005 | element | Total input | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0006 | element | Total output | `value` @ Measurement |
| at0004 | element | Insensible loss | `value` @ Measurement |
| at0007 | element | Fluid balance | `value` @ Observation |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0010 | element | Insensible loss formula |

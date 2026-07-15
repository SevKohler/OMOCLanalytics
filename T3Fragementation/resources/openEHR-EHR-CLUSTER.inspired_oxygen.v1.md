# openEHR-EHR-CLUSTER.inspired_oxygen.v1

**Concept:** Inspired oxygen

**Primary OMOP table:** Measurement  |  **Leaves:** 6  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 2  |  **Not mapped (auxiliary):** 3

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0051 | element | Flow rate | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0052 | element | FiO₂ | `value` @ Measurement |
| at0053 | element | Percent O₂ | `value` @ Measurement, `unit` @ Measurement |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0057 | element | On air |
| at0054 | element | Method of oxygen delivery |
| at0058 | slot | Oxygen delivery detail |

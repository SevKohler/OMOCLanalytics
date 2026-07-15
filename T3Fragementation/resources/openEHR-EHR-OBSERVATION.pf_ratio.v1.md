# openEHR-EHR-OBSERVATION.pf_ratio.v1

**Concept:** PaO₂/FiO₂ ratio

**Primary OMOP table:** Measurement  |  **Leaves:** 4  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 3

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Ratio | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0007 | element | Clinical interpretation |
| at0008 | element | Comment |
| at0010 | element | Confounding factors |

# openEHR-EHR-OBSERVATION.apgar.v2

**Concept:** Apgar score

**Primary OMOP table:** Measurement  |  **Leaves:** 6  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 5

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0025 | element | Total | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0009 | element | Respiratory effort |
| at0005 | element | Heart rate |
| at0013 | element | Muscle tone |
| at0017 | element | Reflex irritability |
| at0021 | element | Skin colour |

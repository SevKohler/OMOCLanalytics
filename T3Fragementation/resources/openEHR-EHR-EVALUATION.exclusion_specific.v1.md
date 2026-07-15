# openEHR-EHR-EVALUATION.exclusion_specific.v1

**Concept:** Exclusion - specific

**Primary OMOP table:** Observation  |  **Leaves:** 4  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 3

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0003 | element | Spesifikt konsept | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0002 | element | Eksklusjonsutsagn |
| at0012 | element | Kommentar |
| at0011 | slot | Tilleggsinformasjon |

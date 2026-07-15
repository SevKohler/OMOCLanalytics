# openEHR-EHR-OBSERVATION.tanner.v1

**Concept:** Tanner stages

**Primary OMOP table:** Observation  |  **Leaves:** 5  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 2  |  **Not mapped (auxiliary):** 2

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Genitalia | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0005 | element | Bryst | `value` @ Observation |
| at0006 | element | Pubesbehåring | `value` @ Observation |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0027 | element | Kommentar |
| at0025 | slot | Tilleggsinformasjon |

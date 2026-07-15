# openEHR-EHR-OBSERVATION.capillary_refill.v1

**Concept:** Capillary refill time (CRT)

**Primary OMOP table:** Measurement  |  **Leaves:** 8  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 7

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0009 | element | Refill time | `value` @ Measurement, `unit` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0005 | element | Clinical interpretation |
| at0040 | element | Comment |
| at0023 | element | Confounding factors |
| at0024 | element | Location of measurement |
| at0041 | element | Measurement method |
| at0039 | slot | Structured measurement location |
| at0037 | slot | Device |

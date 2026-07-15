# openEHR-EHR-OBSERVATION.glasgow_coma_scale.v1

**Concept:** Glasgow Coma Scale (GCS)

**Primary OMOP table:** Measurement  |  **Leaves:** 7  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 6

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0026 | element | Total score | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0009 | element | Best eye response (E) |
| at0007 | element | Best verbal response (V) |
| at0008 | element | Best motor response (M) |
| at0030 | element | EVM profile |
| at0037 | element | Comment |
| at0041 | element | Confounding factors |

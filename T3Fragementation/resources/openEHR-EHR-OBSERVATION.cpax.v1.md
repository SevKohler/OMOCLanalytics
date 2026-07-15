# openEHR-EHR-OBSERVATION.cpax.v1

**Concept:** Chelsea Critical Care Physical Assessment (CPAx) tool

**Primary OMOP table:** Measurement  |  **Leaves:** 11  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 10

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0076 | element | Total score | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0004 | element | Respiratory function |
| at0012 | element | Cough |
| at0014 | element | Moving within the bed (e.g. rolling) |
| at0015 | element | Supine to sitting on the edge of the bed |
| at0016 | element | Dynamic sitting (i.e. when sitting on the edge of the bed/unsupported sitting) |
| at0017 | element | Standing balance |
| at0018 | element | Sit to stand (starting position: ≤90º hip flexion) |
| at0019 | element | Transferring from bed to chair |
| at0020 | element | Stepping |
| at0013 | element | Grip strength (predicted mean for age and gender on the strongest hand) |

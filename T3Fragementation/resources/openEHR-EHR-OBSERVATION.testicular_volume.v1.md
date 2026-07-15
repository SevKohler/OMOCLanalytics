# openEHR-EHR-OBSERVATION.testicular_volume.v1

**Concept:** Testicular volume

**Primary OMOP table:** Observation  |  **Leaves:** 7  |  **Mapped to primary:** 2  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 5

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0020 | element | Testicle examined | `qualifier` @ Observation |
| at0010 | element | Testicular volume | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0005 | element | Comment |
| at0012 | element | Confounding factors |
| at0013 | element | Method |
| at0008 | element | Formula |
| at0007 | slot | Device |

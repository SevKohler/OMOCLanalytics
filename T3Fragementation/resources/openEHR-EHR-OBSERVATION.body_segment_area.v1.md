# openEHR-EHR-OBSERVATION.body_segment_area.v1

**Concept:** Body segment area

**Primary OMOP table:** Measurement  |  **Leaves:** 10  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 9

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0008 | element | Area | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0004 | element | Body segment name |
| at0005 | element | Side |
| at0009 | element | Comment |
| at0011 | element | Confounding factors |
| at0031 | element | Body position |
| at0027 | element | Measurement method |
| at0029 | element | Measurement origin/endpoint |
| at0015 | slot | Measuring device |
| at0030 | slot | Structured origin/endpoint |

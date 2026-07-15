# openEHR-EHR-OBSERVATION.malnutrition_screening_tool.v1

**Concept:** Malnutrition Screening Tool (MST)

**Primary OMOP table:** Measurement  |  **Leaves:** 3  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 2

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0019 | element | MST score | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0005 | element | Have you lost weight recently without trying? |
| at0016 | element | Have you been eating poorly because of a decreased appetite? |

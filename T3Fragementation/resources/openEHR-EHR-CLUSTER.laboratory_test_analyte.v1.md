# openEHR-EHR-CLUSTER.laboratory_test_analyte.v1

**Concept:** Laboratory analyte result

**Primary OMOP table:** Measurement  |  **Leaves:** 13  |  **Mapped to primary:** 3  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 10

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0024 | element | Analyte name | `concept_id` @ Measurement |
| at0001 | element | Analyte result | `value` @ Measurement |
| at0025 | element | Validation time | `measurement_date` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0027 | element | Analyte result sequence |
| at0004 | element | Reference range guidance |
| at0028 | element | Test method |
| at0031 | element | Analysis performed time |
| at0005 | element | Result status |
| at0006 | element | Result status time |
| at0026 | element | Specimen |
| at0032 | element | Accredited |
| at0003 | element | Comment |
| at0014 | slot | Analyte result detail |

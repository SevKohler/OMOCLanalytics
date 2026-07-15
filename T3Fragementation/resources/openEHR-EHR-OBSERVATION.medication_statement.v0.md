# openEHR-EHR-OBSERVATION.medication_statement.v0

**Concept:** Medication use statement

**Primary OMOP table:** DrugExposure  |  **Leaves:** 11  |  **Mapped to primary:** 3  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 8

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0006 | element | Medication name | `concept_id` @ DrugExposure |
| at0030 | element | Route of administration | `route_concept_id` @ DrugExposure |
| at0026 | element | Last administered | `drug_exposure_end_date` @ DrugExposure |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0047 | element | Overall directions description |
| at0032 | element | Description |
| at0023 | element | Clinical indication |
| at0037 | element | Endpoint |
| at0029 | element | Comment |
| at0046 | slot | Medication details |
| at0045 | slot | Structured dose and timing |
| at0048 | slot | Addtional details |

# openEHR-EHR-OBSERVATION.medication_screening.v1

**Concept:** Medication screening questionnaire

**Primary OMOP table:** DrugExposure  |  **Leaves:** 10  |  **Mapped to primary:** 4  |  **Externalised to a separate record:** 1  |  **Not mapped (auxiliary):** 5

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0021 | element | Specific medication > Medication name | `concept_id` @ DrugExposure |
| at0003 | element | Specific medication > Latest dose | `drug_exposure_start_date` @ DrugExposure, `drug_exposure_end_date` @ DrugExposure |
| at0002 | element | Specific medication > Timing | `drug_exposure_start_date` @ DrugExposure, `drug_exposure_end_date` @ DrugExposure |
| at0041 | slot | Specific medication > Additional details | `quantity` @ DrugExposure |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0024 | element | Specific medication > Used | `qualifier` @ Observation |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0040 | element | Screening purpose |
| at0027 | element | Any medications used? |
| at0043 | element | Description |
| at0025 | element | Specific medication > Comment |
| at0042 | slot | Additional details |

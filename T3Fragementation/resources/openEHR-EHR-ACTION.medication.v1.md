# openEHR-EHR-ACTION.medication.v1

**Concept:** Medication management

**Primary OMOP table:** DrugExposure  |  **Leaves:** 21  |  **Mapped to primary:** 3  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 18

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0020 | element | Medication item | `concept_id` @ DrugExposure |
| at0043 | element | Original scheduled date/time | `drug_exposure_start_date` @ DrugExposure, `drug_exposure_end_date` @ DrugExposure |
| at0131 | slot | Amount | `quantity` @ DrugExposure |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0156 | element | Clinical indication |
| at0132 | element | Substitution |
| at0133 | element | Substitution reason |
| at0154 | element | Restart date/time |
| at0155 | element | Restart criterion |
| at0021 | element | Reason |
| at0147 | element | Administration details > Route |
| at0141 | element | Administration details > Body site |
| at0143 | element | Administration details > Administration method |
| at0033 | element | Patient guidance |
| at0149 | element | Double-checked? |
| at0025 | element | Sequence number |
| at0024 | element | Comment |
| at0103 | element | Order ID |
| at0104 | slot | Medication details |
| at0142 | slot | Administration details > Structured body site |
| at0144 | slot | Administration details > Administration device |
| at0053 | slot | Additional details |

# openEHR-EHR-EVALUATION.medication_summary.v1

**Concept:** Medication summary

**Primary OMOP table:** DrugExposure  |  **Leaves:** 19  |  **Mapped to primary:** 4  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 15

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0002 | element | Medication name | `concept_id` @ DrugExposure |
| at0009 | element | Onset of use | `drug_exposure_start_date` @ DrugExposure |
| at0015 | element | Cumulative dose | `quantity` @ DrugExposure |
| at0010 | element | Cessation of use | `drug_exposure_end_date` @ DrugExposure |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0007 | element | Clinical description |
| at0028 | element | Clinical indication |
| at0011 | element | Episode > Episode onset |
| at0018 | element | Episode > Episode indication |
| at0020 | element | Episode > Therapeutic intent |
| at0014 | element | Episode > Description |
| at0016 | element | Episode > Episode amount |
| at0012 | element | Episode > Episode cessation |
| at0031 | element | Episode > Episode duration |
| at0013 | element | Episode > Episode reason for cessation |
| at0032 | element | Episode > Route |
| at0022 | element | Episode > Therapeutic response |
| at0030 | element | Reason for cessation |
| at0027 | element | Cumulative duration |
| at0029 | slot | Episode > Additional details |

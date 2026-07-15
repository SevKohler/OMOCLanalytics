# openEHR-EHR-EVALUATION.specimen_summary.v1

**Concept:** Specimen summary

**Primary OMOP table:** Specimen  |  **Leaves:** 20  |  **Mapped to primary:** 4  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 16

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0032 | element | Specimen label | `concept_id` @ Specimen |
| at0002 | element | Stored specimen ID | `specimen_source_id` @ Specimen |
| at0018 | element | Storage started | `specimen_date` @ Specimen |
| at0030 | element | Number remaining | `quantity` @ Specimen |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0031 | element | Description |
| at0023 | element | Use > Reason for use |
| at0024 | element | Use > Date of use |
| at0029 | element | Use > Number used |
| at0027 | element | Use > Use comment |
| at0012 | element | Use by date |
| at0033 | element | Legally expiry date |
| at0010 | element | Disposal reason |
| at0011 | element | Date of disposal |
| at0020 | element | Specimen storage |
| at0016 | element | Comment |
| at0008 | slot | Specimen details |
| at0026 | slot | Use > Amount used |
| at0028 | slot | Amount remaining |
| at0009 | slot | Biobank location |
| at0017 | slot | Additional details |

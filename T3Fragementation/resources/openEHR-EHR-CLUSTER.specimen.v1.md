# openEHR-EHR-CLUSTER.specimen.v1

**Concept:** Specimen

**Primary OMOP table:** Specimen  |  **Leaves:** 29  |  **Mapped to primary:** 6  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 23

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0029 | element | Specimen type | `concept_id` @ Specimen |
| at0098 | element | Specimen label | `concept_id` @ Specimen |
| at0099 | element | Number of fragments | `quantity` @ Specimen |
| at0001 | element | Laboratory specimen identifier | `specimen_source_id` @ Specimen |
| at0034 | element | Date/time received | `specimen_date` @ Specimen |
| at0013 | slot | Structured source site | `anatomic_site_concept` @ Specimen |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0097 | element | Specimen description |
| at0088 | element | External identifier |
| at0008 | element | Sampling context |
| at0007 | element | Collection method |
| at0079 | element | Collection description |
| at0087 | element | Source site |
| at0015 | element | Collection date/time |
| at0005 | element | Hazard warning |
| at0067 | element | Collection setting |
| at0070 | element | Specimen collector identifier |
| at0080 | element | Number of containers |
| at0003 | element | Parent specimen identifier |
| at0042 | element | Specimen quality issue |
| at0041 | element | Adequacy for testing |
| at0045 | element | Comment |
| at0027 | slot | Physical properties |
| at0071 | slot | Specimen collector details |
| at0083 | slot | Additional details |
| at0085 | slot | Container details |
| at0068 | slot | Processing details |
| at0100 | slot | Storage details |
| at0093 | slot | Transport details |
| at0096 | slot | Digital representation |

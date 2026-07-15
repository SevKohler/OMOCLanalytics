# openEHR-EHR-CLUSTER.figo_staging_cancer.v1

**Concept:** FIGO staging of gynaecological cancer

**Primary OMOP table:** Measurement  |  **Leaves:** 5  |  **Mapped to primary:** 2  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 3

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0005 | element | Staging criteria | `concept_id` @ Measurement |
| at0002 | element | FIGO stage | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0003 | element | Molecular subtype |
| at0006 | element | FIGO stage with molecular classification |
| at0004 | element | FIGO version |

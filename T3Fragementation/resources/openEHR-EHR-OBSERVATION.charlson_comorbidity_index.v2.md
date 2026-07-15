# openEHR-EHR-OBSERVATION.charlson_comorbidity_index.v2

**Concept:** Charlson Comorbidity Index (CCI)

**Primary OMOP table:** Measurement  |  **Leaves:** 19  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 18

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0072 | element | CCI total score | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0061 | element | Age group |
| at0012 | element | Myocardial infarction |
| at0009 | element | Congestive heart failure |
| at0006 | element | Peripheral vascular disease |
| at0015 | element | Cerebrovascular disease |
| at0018 | element | Dementia |
| at0021 | element | Chronic pulmonary disease |
| at0024 | element | Ulcer disease |
| at0027 | element | Liver disease |
| at0030 | element | Connective tissue disease |
| at0033 | element | Diabetes mellitus |
| at0036 | element | Hemiplegia |
| at0039 | element | Moderate or severe renal disease |
| at0045 | element | Solid tumor |
| at0047 | element | Leukemia |
| at0050 | element | Lymphoma |
| at0060 | element | AIDS |
| at0073 | element | Estimated 10-year survival |

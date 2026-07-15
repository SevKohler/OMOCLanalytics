# openEHR-EHR-OBSERVATION.news_uk_rcp.v1

**Concept:** National Early Warning Score (NEWS)

**Primary OMOP table:** Measurement  |  **Leaves:** 11  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 10

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0028 | element | Total score | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0006 | element | Respiration rate |
| at0029 | element | Oxygen saturation |
| at0034 | element | Supplemental oxygen |
| at0007 | element | Body temperature |
| at0004 | element | Systolic blood pressure |
| at0005 | element | Heart rate |
| at0008 | element | Level of consciousness |
| at0047 | element | Clinical risk category |
| at0044 | element | Comment |
| at0043 | element | Confounding factors |

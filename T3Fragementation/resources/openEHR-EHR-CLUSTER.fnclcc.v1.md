# openEHR-EHR-CLUSTER.fnclcc.v1

**Concept:** FNCLCC grading system

**Primary OMOP table:** Measurement  |  **Leaves:** 5  |  **Mapped to primary:** 2  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 3

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0021 | element | Total score | `value` @ Measurement |
| at0017 | element | Histological grade | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0005 | element | Tumour differentiation |
| at0006 | element | Mitotic count |
| at0007 | element | Tumour necrosis |

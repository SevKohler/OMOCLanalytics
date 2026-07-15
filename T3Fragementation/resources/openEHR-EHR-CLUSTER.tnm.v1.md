# openEHR-EHR-CLUSTER.tnm.v1

**Concept:** TNM clinical classification

**Primary OMOP table:** Observation  |  **Leaves:** 18  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 17

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0030 | element | TNM assessment | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0001 | element | Anatomical site |
| at0002 | element | Anatomical subsite |
| at0003 | element | Primary tumour (T) |
| at0004 | element | Regional lymph nodes (N) |
| at0005 | element | Distant metastasis (M) |
| at0006 | element | Histopathological grade (G) |
| at0007 | element | Residual tumour (R) |
| at0012 | element | Lymphatic invasion (L) |
| at0016 | element | Venous invasion (V) |
| at0021 | element | Perineural invasion (Pn) |
| at0025 | element | Multiple primary tumours (m) |
| at0026 | element | Multimodality therapy (y) |
| at0027 | element | Recurrent (r) |
| at0028 | element | Autopsy (a) |
| at0029 | element | Carcinoma in situ (is) |
| at0031 | element | Stage grouping |
| at0032 | element | TNM Edition |

# openEHR-EHR-CLUSTER.gist_modified_nih.v1

**Concept:** Modified NIH Criteria for GIST risk assessment

**Primary OMOP table:** Observation  |  **Leaves:** 5  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 4

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Risk category | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0025 | element | Diameter |
| at0033 | element | Mitotic count |
| at0027 | element | Location |
| at0028 | element | Tumour rupture |

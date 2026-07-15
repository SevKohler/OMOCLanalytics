# openEHR-EHR-CLUSTER.problem_qualifier.v2

**Concept:** Problem/Diagnosis qualifier

**Primary OMOP table:** Observation  |  **Leaves:** 15  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 1  |  **Not mapped (auxiliary):** 13

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Diagnostic status | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0060 | element | Current/Past? | `value` @ Observation |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0111 | element | Disorder category |
| at0003 | element | Active/Inactive? |
| at0098 | element | Level of control |
| at0102 | element | Progression |
| at0083 | element | Resolution phase |
| at0089 | element | Remission status |
| at0001 | element | Episodicity |
| at0107 | element | Reason for an ongoing episode |
| at0071 | element | Occurrence |
| at0077 | element | Course label |
| at0063 | element | Diagnostic category |
| at0073 | element | Admission diagnosis? |
| at0110 | element | Comment |

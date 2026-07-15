# openEHR-EHR-CLUSTER.exam.v2

**Concept:** Physical examination findings

**Primary OMOP table:** Observation  |  **Leaves:** 9  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 8

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0003 | element | Clinical description | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0001 | element | System or structure examined |
| at0012 | element | Body site |
| at0006 | element | Clinical interpretation |
| at0007 | element | Comment |
| at0011 | slot | Structured body site |
| at0004 | slot | Examination findings |
| at0005 | slot | Multimedia representation |
| at0008 | slot | Examination not done |

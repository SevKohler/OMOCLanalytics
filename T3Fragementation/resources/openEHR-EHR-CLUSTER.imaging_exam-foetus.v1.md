# openEHR-EHR-CLUSTER.imaging_exam-foetus.v1

**Concept:** Imaging examination of a fetus

**Primary OMOP table:** Observation  |  **Leaves:** 12  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 11

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Imaging findings | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0001.1 | element | Body structure |
| at0002 | element | Body site |
| at0006 | element | Impression |
| at0007 | element | Comment |
| at0.7 | element | Label |
| at0.8 | element | Cardiac activity |
| at0.12 | element | Heart rate |
| at0.15 | element | Estimated weight |
| at0.16 | element | Estimated weight rationale |
| at0003 | slot | Structured body site |
| at0005 | slot | Additional details |

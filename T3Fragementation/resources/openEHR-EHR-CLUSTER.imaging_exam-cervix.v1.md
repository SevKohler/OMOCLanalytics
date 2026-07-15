# openEHR-EHR-CLUSTER.imaging_exam-cervix.v1

**Concept:** Imaging examination of the cervix

**Primary OMOP table:** Observation  |  **Leaves:** 8  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 7

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
| at0.4 | element | Length |
| at0006 | element | Impression |
| at0007 | element | Comment |
| at0003 | slot | Structured body site |
| at0005 | slot | Additional details |

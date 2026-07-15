# openEHR-EHR-CLUSTER.imaging_exam-ovary.v1

**Concept:** Imaging examination of an ovary

**Primary OMOP table:** Observation  |  **Leaves:** 15  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 14

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
| at0.3 | element | Diameter |
| at0.9 | element | Volume |
| at0.4 | element | Largest follicle diameter |
| at0.5 | element | Number of antral follicles |
| at0.10 | element | Follicle distribution |
| at0.11 | element | Per follicle > Label |
| at0.7 | element | Per follicle > Diameter |
| at0.8 | element | Per follicle > Description |
| at0003 | slot | Structured body site |
| at0005 | slot | Additional details |

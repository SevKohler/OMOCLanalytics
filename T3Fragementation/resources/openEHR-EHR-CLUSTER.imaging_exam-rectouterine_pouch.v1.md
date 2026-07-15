# openEHR-EHR-CLUSTER.imaging_exam-rectouterine_pouch.v1

**Concept:** Imaging examination of the rectouterine pouch

**Primary OMOP table:** Observation  |  **Leaves:** 10  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 9

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
| at0.2 | element | Fluid presence |
| at0.9 | element | Diameter |
| at0.5 | element | Amount of free fluid |
| at0003 | slot | Structured body site |
| at0005 | slot | Additional details |

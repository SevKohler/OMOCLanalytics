# openEHR-EHR-EVALUATION.goal.v1

**Concept:** Goal

**Primary OMOP table:** Observation  |  **Leaves:** 17  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 16

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0002 | element | Goal name | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0012 | element | Goal description |
| at0010 | element | Clinical indication |
| at0025 | element | Goal start date |
| at0003 | element | Goal proposed date |
| at0004 | element | Goal end date |
| at0013 | element | Goal outcome |
| at0022 | element | Goal comment |
| at0011 | element | Target > Target name |
| at0007 | element | Target > Target |
| at0024 | element | Target > Target description |
| at0006 | element | Target > Target path |
| at0008 | element | Target > Target proposed date |
| at0009 | element | Target > Target end date |
| at0018 | element | Target > Target outcome |
| at0023 | element | Target > Target comment |
| at0028 | slot | Readiness for change |

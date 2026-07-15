# openEHR-EHR-OBSERVATION.body_segment_discrepancy.v1

**Concept:** Body segment discrepancy

**Primary OMOP table:** Observation  |  **Leaves:** 10  |  **Mapped to primary:** 2  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 8

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Body segment measurement | `concept_id` @ Observation |
| at0008 | element | Discrepancy | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0046 | element | Longest side |
| at0009 | element | Comment |
| at0027 | element | Measurement method |
| at0029 | element | Measurement origin |
| at0033 | element | Measurement endpoint |
| at0015 | slot | Measuring device |
| at0030 | slot | Structured origin |
| at0035 | slot | Structured endpoint |

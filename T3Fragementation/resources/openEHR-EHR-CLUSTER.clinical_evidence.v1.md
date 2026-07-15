# openEHR-EHR-CLUSTER.clinical_evidence.v1

**Concept:** Clinical evidence

**Primary OMOP table:** Observation  |  **Leaves:** 12  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 11

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0003 | element | Evidence | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0004 | element | Summary |
| at0005 | element | Result |
| at0006 | element | Date/time of result |
| at0026 | element | Date/time clinically relevant |
| at0022 | element | Method |
| at0001 | element | Method description |
| at0023 | element | Comment |
| at0025 | slot | Structured result |
| at0007 | slot | Citation |
| at0018 | slot | Multimedia representation |
| at0024 | slot | Additional details |

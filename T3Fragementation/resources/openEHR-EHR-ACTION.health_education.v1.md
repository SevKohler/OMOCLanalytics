# openEHR-EHR-ACTION.health_education.v1

**Concept:** Health education

**Primary OMOP table:** Observation  |  **Leaves:** 17  |  **Mapped to primary:** 2  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 15

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0002 | element | Topic name | `value` @ Observation |
| at0026 | element | Scheduled date/ time | `observation_date` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0003 | element | Description |
| at0035 | element | Clinical indication |
| at0004 | element | Method |
| at0020 | element | Session Number |
| at0010 | element | Reason |
| at0019 | element | Outcome |
| at0027 | element | Comment |
| at0030 | element | Requestor order identifier |
| at0031 | element | Receiver order identifier |
| at0025 | slot | Material details |
| at0033 | slot | Additional details |
| at0028 | slot | Requestor |
| at0029 | slot | Receiver |
| at0032 | slot | Recipient |
| at0034 | slot | Interpreter details |

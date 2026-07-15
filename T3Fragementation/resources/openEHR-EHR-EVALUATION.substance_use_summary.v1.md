# openEHR-EHR-EVALUATION.substance_use_summary.v1

**Concept:** Substance use summary

**Primary OMOP table:** Observation  |  **Leaves:** 21  |  **Mapped to primary:** 5  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 16

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0002 | element | Substance name | `value` @ Observation |
| at0003 | element | Overall status | `qualifier` @ Observation |
| at0008 | element | First ever use | `observation_date` @ Observation |
| at0009 | element | Regular use commenced | `observation_date` @ Observation |
| at0010 | element | Daily use commenced | `observation_date` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0007 | element | Overall description |
| at0013 | element | Per episode > Episode label |
| at0014 | element | Per episode > Episode start date |
| at0016 | element | Per episode > Specific substance name |
| at0017 | element | Per episode > Status |
| at0018 | element | Per episode > Episode description |
| at0019 | element | Per episode > Pattern |
| at0023 | element | Per episode > Typical amount |
| at0036 | element | Per episode > Route |
| at0015 | element | Per episode > Episode end date |
| at0024 | element | Per episode > Number of quit attempts |
| at0026 | element | Per episode > Episode comment |
| at0028 | element | Overall quit date |
| at0030 | element | Overall comment |
| at0025 | slot | Per episode > Episode details |
| at0027 | slot | Overall details |

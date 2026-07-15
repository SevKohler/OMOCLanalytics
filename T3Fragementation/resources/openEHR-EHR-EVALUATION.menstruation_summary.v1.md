# openEHR-EHR-EVALUATION.menstruation_summary.v1

**Concept:** Menstruation summary

**Primary OMOP table:** Observation  |  **Leaves:** 14  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 13

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0003 | element | Menstrual status | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0025 | element | Overall description |
| at0002 | element | Menarche |
| at0011 | element | Per episode > Episode label |
| at0012 | element | Per episode > Episode start date |
| at0013 | element | Per episode > Description |
| at0014 | element | Per episode > Typical pattern |
| at0017 | element | Per episode > Typical cycle length |
| at0018 | element | Per episode > Typical menses duration |
| at0021 | element | Per episode > Episode end date |
| at0022 | element | Per episode > Episode comment |
| at0004 | element | Menopause |
| at0023 | element | Comment |
| at0020 | slot | Per episode > Additional details |

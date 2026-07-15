# openEHR-EHR-OBSERVATION.ipss.v1

**Concept:** International prostate symptom score (IPSS)

**Primary OMOP table:** Measurement  |  **Leaves:** 9  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 8

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0023 | element | Total score (S) | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0004 | element | Incomplete emptying |
| at0011 | element | Frequency |
| at0012 | element | Intermittency |
| at0013 | element | Urgency |
| at0014 | element | Weak Stream |
| at0015 | element | Straining |
| at0016 | element | Nocturia |
| at0024 | element | Quality of life |

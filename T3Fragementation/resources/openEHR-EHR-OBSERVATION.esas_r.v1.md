# openEHR-EHR-OBSERVATION.esas_r.v1

**Concept:** Edmonton Symptom Assessment System Revised (ESAS-r)

**Primary OMOP table:** Measurement  |  **Leaves:** 11  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 10  |  **Not mapped (auxiliary):** 0

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Pain | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0005 | element | Tiredness | `value` @ Measurement |
| at0006 | element | Drowsiness | `value` @ Measurement |
| at0007 | element | Nausea | `value` @ Measurement |
| at0008 | element | Lack of appetite | `value` @ Measurement |
| at0009 | element | Shortness of breath | `value` @ Measurement |
| at0010 | element | Depression | `value` @ Measurement |
| at0011 | element | Anxiety | `value` @ Measurement |
| at0012 | element | Well-being | `value` @ Measurement |
| at0016 | element | Other problem > Problem name | `qualifier` @ Measurement |
| at0017 | element | Other problem > Rating | `value` @ Measurement |

## Auxiliary — not mapped (needs a fact_relationship)

_None._

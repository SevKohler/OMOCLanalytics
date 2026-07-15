# openEHR-EHR-OBSERVATION.urinalysis.v1

**Concept:** Urinalysis

**Primary OMOP table:** Measurement  |  **Leaves:** 17  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 9  |  **Not mapped (auxiliary):** 7

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0050 | element | Glucose | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0062 | element | Bilirubin | `value` @ Measurement |
| at0037 | element | Ketones | `value` @ Measurement |
| at0151 | element | Specific gravity | `value` @ Measurement |
| at0032 | element | Blood | `value` @ Measurement, `qualifier` @ Measurement |
| at0126 | element | pH | `value` @ Measurement |
| at0095 | element | Protein | `value` @ Measurement |
| at0056 | element | Urobilinogen | `value` @ Measurement |
| at0043 | element | Nitrite | `value` @ Measurement |
| at0068 | element | Leukocytes | `value` @ Measurement |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0181 | element | Clinical interpretation |
| at0030 | element | Comment |
| at0186 | element | Method |
| at0182 | slot | Additional details |
| at0185 | slot | Exam not done |
| at0180 | slot | Reagent Strips |
| at0183 | slot | Device |

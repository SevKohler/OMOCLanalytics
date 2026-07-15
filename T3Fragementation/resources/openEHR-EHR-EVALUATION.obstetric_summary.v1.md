# openEHR-EHR-EVALUATION.obstetric_summary.v1

**Concept:** Obstetric summary

**Primary OMOP table:** Measurement  |  **Leaves:** 16  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 11  |  **Not mapped (auxiliary):** 4

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0002 | element | Gravidity | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0003 | element | Parity | `value` @ Measurement |
| at0015 | element | Term births | `value` @ Measurement |
| at0016 | element | Preterm births | `value` @ Measurement |
| at0017 | element | Abortions | `value` @ Measurement |
| at0004 | element | Miscarriages | `value` @ Measurement |
| at0005 | element | Terminations | `value` @ Measurement |
| at0011 | element | Ectopic pregnancies | `value` @ Measurement |
| at0006 | element | Live births | `value` @ Measurement |
| at0012 | element | Stillbirths | `value` @ Measurement |
| at0028 | element | Neonatal deaths | `value` @ Measurement |
| at0027 | element | Caesarean sections | `value` @ Measurement |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0025 | element | Description |
| at0018 | element | Multiple births |
| at0026 | element | Comment |
| at0021 | element | Definition of viability |

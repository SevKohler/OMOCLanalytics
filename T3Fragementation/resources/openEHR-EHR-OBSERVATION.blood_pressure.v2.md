# openEHR-EHR-OBSERVATION.blood_pressure.v2

**Concept:** Blood pressure

**Primary OMOP table:** Measurement  |  **Leaves:** 20  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 1  |  **Not mapped (auxiliary):** 18

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Systolic | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0005 | element | Diastolic | `value` @ Measurement |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at1006 | element | Mean arterial pressure |
| at1007 | element | Pulse pressure |
| at1059 | element | Clinical interpretation |
| at0033 | element | Comment |
| at0008 | element | Position |
| at1052 | element | Confounding factors |
| at1043 | element | Sleep status |
| at1005 | element | Tilt |
| at0013 | element | Cuff size |
| at0014 | element | Location of measurement |
| at1035 | element | Method |
| at1038 | element | Mean arterial pressure formula |
| at1054 | element | Systolic pressure formula |
| at1055 | element | Diastolic pressure formula |
| at1010 | element | Diastolic endpoint |
| at1030 | slot | Exertion |
| at1057 | slot | Structured measurement location |
| at1025 | slot | Device |

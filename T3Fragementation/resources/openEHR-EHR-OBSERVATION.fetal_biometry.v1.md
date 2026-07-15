# openEHR-EHR-OBSERVATION.fetal_biometry.v1

**Concept:** Fetal biometry

**Primary OMOP table:** Measurement  |  **Leaves:** 12  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 8  |  **Not mapped (auxiliary):** 3

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Crown-rump length (CRL) | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0006 | element | Biparietal diameter (BPD) | `value` @ Measurement |
| at0007 | element | Occipito-frontal diameter (OFD) | `value` @ Measurement |
| at0008 | element | Head circumference (HC) | `value` @ Measurement |
| at0009 | element | Trans-cerebellar diameter (TCD) | `value` @ Measurement |
| at0011 | element | Binocular distance (BOD) | `value` @ Measurement |
| at0012 | element | Abdominal circumference (AC) | `value` @ Measurement |
| at0013 | element | Femur length (FL) | `value` @ Measurement |
| at0014 | element | Humeral length (HL) | `value` @ Measurement |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0010 | element | Interocular distance (IOD) |
| at0015 | element | Comment |
| at0017 | element | BPD method |

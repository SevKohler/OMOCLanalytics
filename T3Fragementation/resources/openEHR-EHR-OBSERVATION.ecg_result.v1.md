# openEHR-EHR-OBSERVATION.ecg_result.v1

**Concept:** ECG result

**Primary OMOP table:** Measurement  |  **Leaves:** 64  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 3  |  **Not mapped (auxiliary):** 60

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0101 | element | Finding | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0020 | element | P axis | `value` @ Measurement |
| at0021 | element | QRS axis | `value` @ Measurement |
| at0022 | element | T axis | `value` @ Measurement |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0100 | element | ECG type |
| at0094 | element | Atrial heart rate |
| at0013 | element | Ventricular heart rate |
| at0007 | element | QT interval global |
| at0008 | element | QTc interval global |
| at0012 | element | PR interval global |
| at0014 | element | QRS duration global |
| at0105 | element | RR interval global |
| at0096 | element | Clinical information provided |
| at0009 | element | Device interpretation |
| at0081 | element | ECG diagnosis |
| at0089 | element | Conclusion |
| at0090 | element | Comment |
| at0098 | element | Per-lead > Description |
| at0041 | element | Per-lead > P amplitude |
| at0028 | element | Per-lead > P duration |
| at0042 | element | Per-lead > P area |
| at0043 | element | Per-lead > P' amplitude |
| at0044 | element | Per-lead > P' duration |
| at0046 | element | Per-lead > P' area |
| at0048 | element | Per-lead > Q amplitude |
| at0049 | element | Per-lead > Q duration |
| at0050 | element | Per-lead > R amplitude |
| at0051 | element | Per-lead > R duration |
| at0053 | element | Per-lead > S amplitude |
| at0054 | element | Per-lead > S duration |
| at0055 | element | Per-lead > R' amplitude |
| at0056 | element | Per-lead > R' duration |
| at0057 | element | Per-lead > S' amplitude |
| at0058 | element | Per-lead > S' duration |
| at0059 | element | Per-lead > Ventricular Activation Time (VAT) |
| at0060 | element | Per-lead > QRS p-p |
| at0061 | element | Per-lead > QRS duration |
| at0062 | element | Per-lead > QRS area |
| at0063 | element | Per-lead > ST onset |
| at0064 | element | Per-lead > ST midpoint |
| at0065 | element | Per-lead > ST 80ms |
| at0106 | element | Per-lead > ST 60ms |
| at0066 | element | Per-lead > ST end |
| at0067 | element | Per-lead > ST duration |
| at0068 | element | Per-lead > ST slope |
| at0069 | element | Per-lead > ST segment morphology |
| at0073 | element | Per-lead > T amplitude |
| at0074 | element | Per-lead > T duration |
| at0075 | element | Per-lead > T area |
| at0115 | element | Per-lead > Lead comment |
| at0079 | element | Confounding factors |
| at0116 | element | Pacemaker stimulation |
| at0107 | element | Position |
| at0078 | element | Tilt |
| at0102 | element | Technical quality |
| at0097 | element | ECG lead placement |
| at0025 | element | QTc algorithm |
| at0095 | element | Device interpretation comment |
| at0083 | slot | Multimedia representation |
| at0114 | slot | Per-lead > Lead details |
| at0113 | slot | Additional details |
| at0080 | slot | Level of exertion |
| at0076 | slot | Recording device |
| at0082 | slot | Viewing device |

# openEHR-EHR-OBSERVATION.pulse_oximetry.v1

**Concept:** Pulse oximetry

**Primary OMOP table:** Measurement  |  **Leaves:** 14  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 3  |  **Not mapped (auxiliary):** 10

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0006 | element | SpO₂ | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0044 | element | SpOC | `value` @ Measurement |
| at0045 | element | SpCO | `value` @ Measurement |
| at0046 | element | SpMet | `value` @ Measurement |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0058 | element | Interpretation |
| at0036 | element | Comment |
| at0016 | element | Confounding factors |
| at0009 | element | Sensor site |
| at0061 | element | Pre/post-ductal |
| at0054 | slot | Waveform |
| at0060 | slot | Multimedia image |
| at0034 | slot | Exertion |
| at0015 | slot | Inspired oxygen |
| at0018 | slot | Oximetry device |

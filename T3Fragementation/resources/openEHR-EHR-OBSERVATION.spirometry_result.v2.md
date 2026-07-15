# openEHR-EHR-OBSERVATION.spirometry_result.v2

**Concept:** Spirometry result

**Primary OMOP table:** Measurement  |  **Leaves:** 24  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 4  |  **Not mapped (auxiliary):** 19

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0053 | element | Volume > Result | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0058 | element | Flow rate > Result | `value` @ Measurement |
| at0165 | element | Pressure > Result | `value` @ Measurement |
| at0056 | element | Ratio > Result | `value` @ Measurement |
| at0013 | element | Forced expiratory time (FET) | `value` @ Observation |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0054 | element | Volume > Predicted result |
| at0044 | element | Volume > Measured/predicted ratio |
| at0008 | element | Flow rate > Predicted result |
| at0122 | element | Flow rate > Measured/predicted ratio |
| at0166 | element | Pressure > Predicted result |
| at0167 | element | Pressure > Measured/predicted ratio |
| at0018 | element | Ratio > Predicted result |
| at0130 | element | Clinical interpretation |
| at0101 | element | Comment |
| at0115 | element | Position |
| at0098 | element | Confounding factors |
| at0196 | element | Type of measurement |
| at0199 | element | Method |
| at0192 | element | Challenge/reversibility |
| at0131 | slot | Multimedia representation |
| at0191 | slot | Level of exertion |
| at0209 | slot | Environmental conditions |
| at0030 | slot | Device |
| at0185 | slot | Predicted results source |

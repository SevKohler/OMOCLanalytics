# openEHR-EHR-OBSERVATION.body_temperature.v2

**Concept:** Body temperature

**Primary OMOP table:** Measurement  |  **Leaves:** 11  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 10

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Temperature | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0063 | element | Comment |
| at0030 | element | Body exposure |
| at0041 | element | Description of thermal stress |
| at0065 | element | Day of menstrual cycle |
| at0066 | element | Confounding factors |
| at0021 | element | Location of measurement |
| at0056 | slot | Environmental conditions |
| at0057 | slot | Exertion |
| at0064 | slot | Structured measurement location |
| at0059 | slot | Device |

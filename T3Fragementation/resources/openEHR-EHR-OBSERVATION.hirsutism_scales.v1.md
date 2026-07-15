# openEHR-EHR-OBSERVATION.hirsutism_scales.v1

**Concept:** Hirsutism scales

**Primary OMOP table:** Measurement  |  **Leaves:** 16  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 12  |  **Not mapped (auxiliary):** 3

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0079 | element | Total score | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0005 | element | Upper lip hair | `value` @ Measurement |
| at0019 | element | Chin hair | `value` @ Measurement |
| at0082 | element | Sideburn hair | `value` @ Measurement |
| at0025 | element | Chest hair | `value` @ Measurement |
| at0031 | element | Upper back hair | `value` @ Measurement |
| at0037 | element | Lower back hair | `value` @ Measurement |
| at0043 | element | Upper abdomen hair | `value` @ Measurement |
| at0049 | element | Lower abdomen hair | `value` @ Measurement |
| at0055 | element | Upper arm hair | `value` @ Measurement |
| at0061 | element | Lower arm hair | `value` @ Measurement |
| at0067 | element | Thigh hair | `value` @ Measurement |
| at0073 | element | Lower leg hair | `value` @ Measurement |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0091 | element | Perineum hair |
| at0089 | element | Ferriman-Gallwey score |
| at0090 | element | Modified Ferriman-Gallwey score |

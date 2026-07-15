# openEHR-EHR-CLUSTER.specimen_container.v1

**Concept:** Specimen container

**Primary OMOP table:** Measurement  |  **Leaves:** 10  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 9

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0005 | element | Container type | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0003 | element | Container ID |
| at0013 | element | Description |
| at0037 | element | Components |
| at0026 | element | Additive/s |
| at0035 | element | Capacity |
| at0038 | element | Minimum volum |
| at0036 | element | Comment |
| at0028 | slot | Additional details |
| at0029 | slot | Contents |

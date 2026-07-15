# openEHR-EHR-CLUSTER.item_transport.v1

**Concept:** Transportation of an item

**Primary OMOP table:** Observation  |  **Leaves:** 16  |  **Mapped to primary:** 3  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 13

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0028 | element | Item transported | `value` @ Observation |
| at0004 | element | Pick up date/time | `observation_date` @ Observation |
| at0007 | element | Delivery date/time | `observation_date` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0001 | element | Transport status |
| at0027 | element | Transport instruction |
| at0010 | element | Transport description |
| at0008 | element | Pickup site |
| at0009 | element | Delivery site |
| at0002 | element | Transporter identifier |
| at0015 | element | Transportation step > Transport sequence |
| at0005 | element | Comment |
| at0023 | slot | Pickup details |
| at0022 | slot | Delivery details |
| at0017 | slot | Transporter details |
| at0026 | slot | Transportation step > Transport step detail |
| at0024 | slot | Additional details |

# openEHR-EHR-CLUSTER.address.v1

**Concept:** Address

**Primary OMOP table:** Observation  |  **Leaves:** 15  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 14

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0005 | element | Postal code | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0001 | element | Address line |
| at0002 | element | City/Town |
| at0003 | element | District/County |
| at0004 | element | State/Territory/Province |
| at0006 | element | Country |
| at0021 | element | Geolocation code |
| at0007 | element | Latitude |
| at0008 | element | Longitude |
| at0009 | element | Altitude |
| at0019 | element | Map URL |
| at0010 | element | Type |
| at0014 | element | Use |
| at0018 | element | Comment |
| at0020 | slot | Structured address |

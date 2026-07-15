# openEHR-EHR-CLUSTER.device.v1

**Concept:** Medical device

**Primary OMOP table:** DeviceExposure  |  **Leaves:** 18  |  **Mapped to primary:** 6  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 12

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0001 | element | Device name | `concept_id` @ DeviceExposure |
| at0003 | element | Type | `concept_id` @ DeviceExposure |
| at0021 | element | Unique device identifier (UDI) | `unique_device_id` @ DeviceExposure |
| at0020 | element | Serial number | `production_id` @ DeviceExposure |
| at0008 | element | Comment | `device_exposure_start_date` @ DeviceExposure |
| at0009 | slot | Properties | `device_exposure_end_date` @ DeviceExposure |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0002 | element | Description |
| at0004 | element | Manufacturer |
| at0005 | element | Date of manufacture |
| at0022 | element | Catalogue number |
| at0023 | element | Model number |
| at0006 | element | Batch/Lot number |
| at0025 | element | Software version |
| at0007 | element | Date of expiry |
| at0024 | element | Other identifier |
| at0019 | slot | Asset management |
| at0018 | slot | Components |
| at0027 | slot | Multimedia |

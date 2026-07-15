# openEHR-EHR-CLUSTER.device.v1

**Concept:** Medical device

**Category:** cluster

**Element leaves:** 14  |  **Cluster slot leaves:** 4  |  **Total leaves:** 18


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0001 | Device name | DV_TEXT |
| at0003 | Type | DV_TEXT |
| at0002 | Description | DV_TEXT |
| at0021 | Unique device identifier (UDI) | DV_IDENTIFIER |
| at0004 | Manufacturer | DV_TEXT |
| at0005 | Date of manufacture | DV_DATE_TIME |
| at0020 | Serial number | DV_TEXT |
| at0022 | Catalogue number | DV_TEXT |
| at0023 | Model number | DV_TEXT |
| at0006 | Batch/Lot number | DV_TEXT |
| at0025 | Software version | DV_TEXT |
| at0007 | Date of expiry | DV_DATE_TIME |
| at0024 | Other identifier | DV_IDENTIFIER |
| at0008 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0009 | Properties | any archetype |
| at0019 | Asset management | openEHR-EHR-CLUSTER.device_details(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.device_details(-[a-zA-Z0-9_]+)*.v0 |
| at0018 | Components | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0027 | Multimedia | openEHR-EHR-CLUSTER.media_file(-[a-zA-Z0-9_]+)*.v1 |

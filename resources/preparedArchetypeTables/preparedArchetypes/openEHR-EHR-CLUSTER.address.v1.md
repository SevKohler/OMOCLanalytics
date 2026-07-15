# openEHR-EHR-CLUSTER.address.v1

**Concept:** Address

**Category:** cluster

**Element leaves:** 14  |  **Cluster slot leaves:** 1  |  **Total leaves:** 15


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0001 | Address line | DV_TEXT |
| at0002 | City/Town | DV_TEXT |
| at0003 | District/County | DV_TEXT |
| at0004 | State/Territory/Province | DV_TEXT |
| at0005 | Postal code | DV_TEXT |
| at0006 | Country | DV_TEXT |
| at0021 | Geolocation code | DV_TEXT |
| at0007 | Latitude | DV_QUANTITY |
| at0008 | Longitude | DV_QUANTITY |
| at0009 | Altitude | DV_QUANTITY |
| at0019 | Map URL | DV_TEXT |
| at0010 | Type | DV_CODED_TEXT / DV_TEXT |
| at0014 | Use | DV_CODED_TEXT / DV_TEXT |
| at0018 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0020 | Structured address | openEHR-EHR-CLUSTER.structured_address(-[a-zA-Z0-9_]+)*.v0 |

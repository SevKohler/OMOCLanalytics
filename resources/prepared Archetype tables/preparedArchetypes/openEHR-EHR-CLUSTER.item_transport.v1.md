# openEHR-EHR-CLUSTER.item_transport.v1

**Concept:** Transportation of an item

**Category:** cluster

**Element leaves:** 11  |  **Cluster slot leaves:** 5  |  **Total leaves:** 16


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0028 | Item transported | DV_TEXT |
| at0001 | Transport status | DV_TEXT |
| at0027 | Transport instruction | DV_TEXT |
| at0010 | Transport description | DV_TEXT |
| at0008 | Pickup site | DV_TEXT |
| at0004 | Pick up date/time | DV_DATE_TIME |
| at0009 | Delivery site | DV_TEXT |
| at0007 | Delivery date/time | DV_DATE_TIME |
| at0002 | Transporter identifier | DV_IDENTIFIER / DV_TEXT |
| at0015 | Transport sequence | DV_COUNT / DV_TEXT |
| at0005 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0023 | Pickup details | openEHR-EHR-CLUSTER.person(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.address(-[a-zA-Z0-9_]+)*.v1 |
| at0022 | Delivery details | openEHR-EHR-CLUSTER.person(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.address(-[a-zA-Z0-9_]+)*.v1 |
| at0017 | Transporter details | openEHR-EHR-CLUSTER.person(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.address(-[a-zA-Z0-9_]+)*.v1 |
| at0026 | Transport step detail | openEHR-EHR-CLUSTER.item_transport(-[a-zA-Z0-9_]+)*.v1 |
| at0024 | Additional details | any archetype |

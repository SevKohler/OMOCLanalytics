# openEHR-EHR-CLUSTER.organisation.v1

**Concept:** Organisation

**Category:** cluster

**Element leaves:** 4  |  **Cluster slot leaves:** 5  |  **Total leaves:** 9


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0001 | Name | DV_TEXT |
| at0003 | Identifier | DV_IDENTIFIER / DV_TEXT |
| at0004 | Role | DV_TEXT |
| at0019 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0005 | Address | openEHR-EHR-CLUSTER.address(-[a-zA-Z0-9_]+)*.v1 |
| at0022 | Electronic communication | openEHR-EHR-CLUSTER.electronic_communication(-[a-zA-Z0-9_]+)*.v1 |
| at0002 | Contact person | openEHR-EHR-CLUSTER.person(-[a-zA-Z0-9_]+)*.v1 |
| at0021 | Parent organisation | openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 |
| at0017 | Additional details | any archetype |

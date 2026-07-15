# openEHR-EHR-CLUSTER.specimen_container.v1

**Concept:** Specimen container

**Category:** cluster

**Element leaves:** 8  |  **Cluster slot leaves:** 2  |  **Total leaves:** 10


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0005 | Container type | DV_TEXT |
| at0003 | Container ID | DV_IDENTIFIER / DV_TEXT |
| at0013 | Description | DV_TEXT |
| at0037 | Components | DV_TEXT |
| at0026 | Additive/s | DV_TEXT |
| at0035 | Capacity | DV_TEXT / DV_QUANTITY |
| at0038 | Minimum volum | DV_TEXT / DV_QUANTITY |
| at0036 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0028 | Additional details | openEHR-EHR-CLUSTER.biobank_storage(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.specimen_transport.v0 / openEHR-EHR-CLUSTER.specimen_transport.v1 / openEHR-EHR-CLUSTER.biobank_storage.v0 |
| at0029 | Contents | openEHR-EHR-CLUSTER.specimen(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.specimen_container(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.specimen_container.v1 |

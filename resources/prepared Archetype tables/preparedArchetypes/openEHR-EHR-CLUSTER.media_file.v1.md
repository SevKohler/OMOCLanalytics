# openEHR-EHR-CLUSTER.media_file.v1

**Concept:** Media file

**Category:** cluster

**Element leaves:** 6  |  **Cluster slot leaves:** 3  |  **Total leaves:** 9


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0001 | Content | DV_MULTIMEDIA |
| at0002 | Content name | DV_TEXT |
| at0010 | Identifier | DV_IDENTIFIER / DV_TEXT |
| at0005 | Description | DV_TEXT |
| at0004 | Created | DV_DATE_TIME / DV_INTERVAL |
| at0007 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0012 | Creator | openEHR-EHR-CLUSTER.person(-[a-zA-Z0-9_]+)*.v1 |
| at0011 | Source device | openEHR-EHR-CLUSTER.device.v1 |
| at0013 | Additional details | any archetype |

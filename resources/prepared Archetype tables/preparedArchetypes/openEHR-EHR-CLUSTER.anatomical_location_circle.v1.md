# openEHR-EHR-CLUSTER.anatomical_location_circle.v1

**Concept:** Circular anatomical location

**Category:** cluster

**Element leaves:** 5  |  **Cluster slot leaves:** 1  |  **Total leaves:** 6


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0065 | Reference direction | DV_TEXT |
| at0079 | Centre landmark | DV_TEXT |
| at0061 | Circular direction | DV_CODED_TEXT / DV_DURATION / DV_QUANTITY |
| at0080 | Distance from landmark | DV_QUANTITY |
| at0023 | Description | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0054 | Multimedia representation | openEHR-EHR-CLUSTER.media_file(-[a-zA-Z0-9_]+)*.v1 |

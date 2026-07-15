# openEHR-EHR-CLUSTER.anatomical_location_relative.v2

**Concept:** Relative anatomical location

**Category:** cluster

**Element leaves:** 5  |  **Cluster slot leaves:** 1  |  **Total leaves:** 6


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0021 | Landmark name | DV_TEXT |
| at0062 | Laterality | DV_CODED_TEXT |
| at0022 | Distance from landmark | DV_QUANTITY |
| at0006 | Direction | DV_CODED_TEXT / DV_TEXT |
| at0023 | Description | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0054 | Multimedia representation | openEHR-EHR-CLUSTER.media_file(-[a-zA-Z0-9_]+)*.v1 |

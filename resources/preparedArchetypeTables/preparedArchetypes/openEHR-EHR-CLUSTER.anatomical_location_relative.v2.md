# openEHR-EHR-CLUSTER.anatomical_location_relative.v2

**Concept:** Relative anatomical location

**Category:** cluster

**Element leaves:** 5  |  **Cluster slot leaves:** 1  |  **Total leaves:** 6


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0021 | Relative location | Landmark name | DV_TEXT |
| at0062 | Relative location | Laterality | DV_CODED_TEXT |
| at0022 | Relative location | Distance from landmark | DV_QUANTITY |
| at0006 | Relative location | Direction | DV_CODED_TEXT / DV_TEXT |
| at0023 |  | Description | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0054 | Multimedia representation | openEHR-EHR-CLUSTER.media_file(-[a-zA-Z0-9_]+)*.v1 |

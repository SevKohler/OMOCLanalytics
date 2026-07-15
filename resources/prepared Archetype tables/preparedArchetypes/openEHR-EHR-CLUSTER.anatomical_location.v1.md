# openEHR-EHR-CLUSTER.anatomical_location.v1

**Concept:** Anatomical location

**Category:** cluster

**Element leaves:** 6  |  **Cluster slot leaves:** 2  |  **Total leaves:** 8


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0001 | Body site name | DV_TEXT |
| at0065 | Specific site | DV_TEXT |
| at0002 | Laterality | DV_CODED_TEXT |
| at0064 | Aspect | DV_CODED_TEXT / DV_TEXT |
| at0055 | Anatomical Line | DV_CODED_TEXT / DV_TEXT |
| at0023 | Description | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0053 | Alternative structure | openEHR-EHR-CLUSTER.anatomical_location_circle(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_relative.v2 |
| at0054 | Multimedia representation | openEHR-EHR-CLUSTER.media_file.v1 |

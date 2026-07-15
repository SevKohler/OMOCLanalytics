# openEHR-EHR-OBSERVATION.body_segment_area.v1

**Concept:** Body segment area

**Category:** entry/observation

**Element leaves:** 8  |  **Cluster slot leaves:** 2  |  **Total leaves:** 10


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0004 | Body segment name | DV_TEXT / DV_CODED_TEXT |
| at0005 | Side | DV_CODED_TEXT |
| at0008 | Area | DV_QUANTITY |
| at0009 | Comment | DV_TEXT |
| at0011 | Confounding factors | DV_TEXT |
| at0031 | Body position | DV_CODED_TEXT / DV_TEXT |
| at0027 | Measurement method | DV_TEXT |
| at0029 | Measurement origin/endpoint | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0015 | Measuring device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0030 | Structured origin/endpoint | openEHR-EHR-CLUSTER.anatomical_location.v1 / openEHR-EHR-CLUSTER.anatomical_location_relative.v1 |

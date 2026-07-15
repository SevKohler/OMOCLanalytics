# openEHR-EHR-CLUSTER.imaging_exam-foetus.v1

**Concept:** Imaging examination of a fetus

**Category:** cluster

**Element leaves:** 10  |  **Cluster slot leaves:** 2  |  **Total leaves:** 12


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0001.1 | Body structure | DV_CODED_TEXT |
| at0002 | Body site | DV_TEXT |
| at0004 | Imaging findings | DV_TEXT |
| at0006 | Impression | DV_TEXT |
| at0007 | Comment | DV_TEXT |
| at0.7 | Label | DV_TEXT |
| at0.8 | Cardiac activity | DV_CODED_TEXT |
| at0.12 | Heart rate | DV_QUANTITY |
| at0.15 | Estimated weight | DV_QUANTITY |
| at0.16 | Estimated weight rationale | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0003 | Structured body site | openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_relative(-[a-zA-Z0-9_]+)*.v2 / openEHR-EHR-CLUSTER.anatomical_location_circle(-[a-zA-Z0-9_]+)*.v1 |
| at0005 | Additional details | openEHR-EHR-CLUSTER.imaging_exam-lymph_node(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.imaging_exam-lymph_node_group(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.imaging_exam-lesion(-[a-zA-Z0-9_]+)*.v0 |

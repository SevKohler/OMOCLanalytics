# openEHR-EHR-CLUSTER.imaging_exam-fallopian_tube.v1

**Concept:** Imaging examination of a fallopian tube

**Category:** cluster

**Element leaves:** 7  |  **Cluster slot leaves:** 3  |  **Total leaves:** 10


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0001.1 | Body structure | DV_CODED_TEXT |
| at0002 | Body site | DV_TEXT |
| at0004 | Imaging findings | DV_TEXT |
| at0.3 | Patency | DV_CODED_TEXT |
| at0.7 | Gestational sac presence | DV_CODED_TEXT |
| at0006 | Impression | DV_TEXT |
| at0007 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0003 | Structured body site | openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_relative(-[a-zA-Z0-9_]+)*.v2 / openEHR-EHR-CLUSTER.anatomical_location_circle(-[a-zA-Z0-9_]+)*.v1 |
| at0005 | Additional details | openEHR-EHR-CLUSTER.imaging_exam-lymph_node(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.imaging_exam-lymph_node_group(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.imaging_exam-lesion(-[a-zA-Z0-9_]+)*.v0 |
| at0.11 | Gestational sac details | openEHR-EHR-CLUSTER.imaging_exam-gestational_sac(-[a-zA-Z0-9_]+)*.v0 |

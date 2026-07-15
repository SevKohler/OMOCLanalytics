# openEHR-EHR-CLUSTER.imaging_exam-cervix.v1

**Concept:** Imaging examination of the cervix

**Category:** cluster

**Element leaves:** 6  |  **Cluster slot leaves:** 2  |  **Total leaves:** 8


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0001.1 | Body structure | DV_CODED_TEXT |
| at0002 | Body site | DV_TEXT |
| at0004 | Imaging findings | DV_TEXT |
| at0.4 | Length | DV_QUANTITY |
| at0006 | Impression | DV_TEXT |
| at0007 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0003 | Structured body site | openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_relative(-[a-zA-Z0-9_]+)*.v2 / openEHR-EHR-CLUSTER.anatomical_location_circle(-[a-zA-Z0-9_]+)*.v1 |
| at0005 | Additional details | openEHR-EHR-CLUSTER.imaging_exam-lymph_node(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.imaging_exam-lymph_node_group(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.imaging_exam-lesion-adnexal_mass(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.imaging_exam-lesion(-[a-zA-Z0-9_]+)*.v0 |

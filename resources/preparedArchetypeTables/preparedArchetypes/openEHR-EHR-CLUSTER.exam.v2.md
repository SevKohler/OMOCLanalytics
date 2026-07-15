# openEHR-EHR-CLUSTER.exam.v2

**Concept:** Physical examination findings

**Category:** cluster

**Element leaves:** 5  |  **Cluster slot leaves:** 4  |  **Total leaves:** 9


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0001 | System or structure examined | DV_TEXT |
| at0012 | Body site | DV_TEXT |
| at0003 | Clinical description | DV_TEXT |
| at0006 | Clinical interpretation | DV_TEXT |
| at0007 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0011 | Structured body site | openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_circle(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_relative(-[a-zA-Z0-9_]+)*.v2 |
| at0004 | Examination findings | any archetype |
| at0005 | Multimedia representation | openEHR-EHR-CLUSTER.media_file(-[a-zA-Z0-9_]+)*.v1 |
| at0008 | Examination not done | openEHR-EHR-CLUSTER.exclusion_exam(-[a-zA-Z0-9_]+)*.v1 |

# openEHR-EHR-CLUSTER.clinical_evidence.v1

**Concept:** Clinical evidence

**Category:** cluster

**Element leaves:** 8  |  **Cluster slot leaves:** 4  |  **Total leaves:** 12


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0003 | Evidence | DV_TEXT |
| at0004 | Summary | DV_TEXT |
| at0005 | Result | any |
| at0006 | Date/time of result | DV_DATE_TIME |
| at0026 | Date/time clinically relevant | DV_DATE_TIME |
| at0022 | Method | DV_TEXT |
| at0001 | Method description | DV_TEXT |
| at0023 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0025 | Structured result | any archetype |
| at0007 | Citation | openEHR-EHR-CLUSTER.citation(-[a-zA-Z0-9_]+)*.v1 |
| at0018 | Multimedia representation | openEHR-EHR-CLUSTER.media_file.v1 |
| at0024 | Additional details | any archetype |

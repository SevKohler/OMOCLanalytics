# openEHR-EHR-EVALUATION.device_summary.v0

**Concept:** Medical device summary

**Category:** entry/evaluation

**Element leaves:** 11  |  **Cluster slot leaves:** 3  |  **Total leaves:** 14


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0020 | Device type | DV_TEXT |
| at0002 | Status | DV_CODED_TEXT |
| at0015 | Description | DV_TEXT |
| at0007 | Device name | DV_TEXT |
| at0008 | Start date | DV_DATE_TIME |
| at0012 | Body site | DV_TEXT |
| at0014 | Description | DV_TEXT |
| at0009 | End date | DV_DATE_TIME |
| at0023 | URI to original data | DV_URI |
| at0019 | Next review due | DV_DATE_TIME |
| at0017 | Last updated | DV_DATE_TIME |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0013 | Structured body site | openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 |
| at0010 | Structured detail | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0021 | Multimedia | openEHR-EHR-CLUSTER.multimedia(-[a-zA-Z0-9_]+)*.v1 |

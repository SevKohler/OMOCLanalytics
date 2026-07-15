# openEHR-EHR-EVALUATION.device_summary.v0

**Concept:** Medical device summary

**Category:** entry/evaluation

**Element leaves:** 10  |  **Cluster slot leaves:** 3  |  **Total leaves:** 13


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0020 |  | Device type | DV_TEXT |
| at0002 |  | Status | DV_CODED_TEXT |
| at0015 |  | Description | DV_TEXT |
| at0007 | Device details | Device name | DV_TEXT |
| at0008 | Device details | Start date | DV_DATE_TIME |
| at0012 | Device details | Body site | DV_TEXT |
| at0014 | Device details | Description | DV_TEXT |
| at0009 | Device details | End date | DV_DATE_TIME |
| at0023 | Device details | URI to original data | DV_URI |
| at0019 | Device details | Next review due | DV_DATE_TIME |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0013 | Device details | Structured body site | openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 |
| at0010 | Device details | Structured detail | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0021 | Device details | Multimedia | openEHR-EHR-CLUSTER.multimedia(-[a-zA-Z0-9_]+)*.v1 |

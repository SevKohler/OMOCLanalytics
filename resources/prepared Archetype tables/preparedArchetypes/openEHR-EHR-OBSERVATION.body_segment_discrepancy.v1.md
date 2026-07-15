# openEHR-EHR-OBSERVATION.body_segment_discrepancy.v1

**Concept:** Body segment discrepancy

**Category:** entry/observation

**Element leaves:** 7  |  **Cluster slot leaves:** 3  |  **Total leaves:** 10


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0004 | Body segment measurement | DV_TEXT / DV_CODED_TEXT |
| at0008 | Discrepancy | DV_QUANTITY |
| at0046 | Longest side | DV_CODED_TEXT / DV_TEXT |
| at0009 | Comment | DV_TEXT |
| at0027 | Measurement method | DV_TEXT |
| at0029 | Measurement origin | DV_TEXT |
| at0033 | Measurement endpoint | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0015 | Measuring device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0030 | Structured origin | any archetype |
| at0035 | Structured endpoint | any archetype |

# openEHR-EHR-OBSERVATION.body_segment_length.v1

**Concept:** Body segment length

**Category:** entry/observation

**Element leaves:** 9  |  **Cluster slot leaves:** 3  |  **Total leaves:** 12


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0004 | Body segment name | DV_TEXT / DV_CODED_TEXT |
| at0005 | Laterality | DV_CODED_TEXT |
| at0008 | Length | DV_QUANTITY |
| at0009 | Comment | DV_TEXT |
| at0011 | Confounding factors | DV_TEXT |
| at0031 | Body position | DV_CODED_TEXT / DV_TEXT |
| at0027 | Measurement method | DV_TEXT |
| at0029 | Measurement origin | DV_TEXT |
| at0033 | Measurement endpoint | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0015 | Measuring device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0030 | Structured origin | any archetype |
| at0035 | Structured endpoint | any archetype |

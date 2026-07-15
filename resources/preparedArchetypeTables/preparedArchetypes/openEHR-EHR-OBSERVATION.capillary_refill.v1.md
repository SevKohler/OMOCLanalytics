# openEHR-EHR-OBSERVATION.capillary_refill.v1

**Concept:** Capillary refill time (CRT)

**Category:** entry/observation

**Element leaves:** 6  |  **Cluster slot leaves:** 2  |  **Total leaves:** 8


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0009 | Refill time | DV_QUANTITY |
| at0005 | Clinical interpretation | DV_CODED_TEXT / DV_TEXT |
| at0040 | Comment | DV_TEXT |
| at0023 | Confounding factors | DV_TEXT |
| at0024 | Location of measurement | DV_TEXT |
| at0041 | Measurement method | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0039 | Structured measurement location | openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_relative.v2 |
| at0037 | Device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |

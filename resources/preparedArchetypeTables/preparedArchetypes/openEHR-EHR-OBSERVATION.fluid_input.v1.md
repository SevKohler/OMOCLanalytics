# openEHR-EHR-OBSERVATION.fluid_input.v1

**Concept:** Fluid input

**Category:** entry/observation

**Element leaves:** 5  |  **Cluster slot leaves:** 3  |  **Total leaves:** 8


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0036 | Fluid name | DV_TEXT |
| at0034 | Route | DV_TEXT |
| at0035 | Volume | DV_QUANTITY |
| at0032 | Comment | DV_TEXT |
| at0031 | Method | DV_CODED_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0039 | Fluid details | any archetype |
| at0033 | Input device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0028 | Measurement device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |

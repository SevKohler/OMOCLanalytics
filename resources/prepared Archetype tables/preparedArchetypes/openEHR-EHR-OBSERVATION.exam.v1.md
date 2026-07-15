# openEHR-EHR-OBSERVATION.exam.v1

**Concept:** Physical examination findings

**Category:** entry/observation

**Element leaves:** 5  |  **Cluster slot leaves:** 2  |  **Total leaves:** 7


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0004 | Description | DV_TEXT |
| at0006 | Interpretation | DV_TEXT |
| at0011 | Comment | DV_TEXT |
| at0008 | Confounding factors | DV_TEXT |
| at0013 | Position | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0005 | Examination detail | any archetype |
| at0010 | Device Details | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |

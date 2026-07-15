# openEHR-EHR-EVALUATION.communication_capability.v1

**Concept:** Communication capability

**Category:** entry/evaluation

**Element leaves:** 5  |  **Cluster slot leaves:** 3  |  **Total leaves:** 8


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0002 | Description | DV_TEXT |
| at0021 | Comment | DV_TEXT |
| at0022 | Communication aid | DV_TEXT |
| at0009 | Overall comment | DV_TEXT |
| at0013 | Last updated | DV_DATE_TIME |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0003 | Language | openEHR-EHR-CLUSTER.language(-[a-zA-Z0-9_]+)*.v1 |
| at0018 | Capability details | any archetype |
| at0005 | Additional details | any archetype |

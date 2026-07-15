# openEHR-EHR-EVALUATION.communication_capability.v1

**Concept:** Communication capability

**Category:** entry/evaluation

**Element leaves:** 4  |  **Cluster slot leaves:** 3  |  **Total leaves:** 7


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0002 |  | Description | DV_TEXT |
| at0021 | Per language | Comment | DV_TEXT |
| at0022 |  | Communication aid | DV_TEXT |
| at0009 |  | Overall comment | DV_TEXT |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0003 | Per language | Language | openEHR-EHR-CLUSTER.language(-[a-zA-Z0-9_]+)*.v1 |
| at0018 | Per language | Capability details | any archetype |
| at0005 |  | Additional details | any archetype |

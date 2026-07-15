# openEHR-EHR-EVALUATION.social_network.v1

**Concept:** Social network

**Category:** entry/evaluation

**Element leaves:** 3  |  **Cluster slot leaves:** 2  |  **Total leaves:** 5


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0015 | Description | DV_TEXT |
| at0002 | Partnership status | DV_TEXT |
| at0018 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0016 | Network | openEHR-EHR-CLUSTER.person(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 |
| at0017 | Additional details | any archetype |

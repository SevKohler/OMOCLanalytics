# openEHR-EHR-EVALUATION.housing_summary.v1

**Concept:** Housing summary

**Category:** entry/evaluation

**Element leaves:** 2  |  **Cluster slot leaves:** 2  |  **Total leaves:** 4


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0002 | Description | DV_TEXT |
| at0005 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0009 | Housing record | openEHR-EHR-CLUSTER.housing_record(-[a-zA-Z0-9_]+)*.v1 |
| at0003 | Additional details | any archetype |

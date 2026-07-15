# openEHR-EHR-EVALUATION.occupation_summary.v1

**Concept:** Occupation summary

**Category:** entry/evaluation

**Element leaves:** 4  |  **Cluster slot leaves:** 2  |  **Total leaves:** 6


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0002 | Description | DV_TEXT |
| at0004 | Employment status | DV_TEXT |
| at0006 | Comment | DV_TEXT |
| at0009 | Last updated | DV_DATE_TIME |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0003 | Occupation episode | openEHR-EHR-CLUSTER.occupation_record(-[a-zA-Z0-9_]+)*.v1 |
| at0005 | Additional details | any archetype |

# openEHR-EHR-OBSERVATION.story.v1

**Concept:** Story/History

**Category:** entry/observation

**Element leaves:** 1  |  **Cluster slot leaves:** 1  |  **Total leaves:** 2


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0004 | Story | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0006 | Structured detail | openEHR-EHR-CLUSTER.health_event(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.issue(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.symptom_sign(-[a-zA-Z0-9_]+)*.v2 |

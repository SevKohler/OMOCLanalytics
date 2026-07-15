# openEHR-EHR-ACTION.service.v1

**Concept:** Service

**Category:** entry/action

**Element leaves:** 10  |  **Cluster slot leaves:** 5  |  **Total leaves:** 15


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0011 | Service name | DV_TEXT |
| at0014 | Service type | DV_TEXT |
| at0013 | Description | DV_TEXT |
| at0032 | Planned date/time | DV_DATE_TIME / DV_INTERVAL / DV_DURATION / DV_TEXT |
| at0025 | Scheduled date/time | DV_DATE_TIME |
| at0021 | Sequence | DV_COUNT |
| at0012 | Reason | DV_TEXT |
| at0028 | Comment | DV_TEXT |
| at0016 | Requestor identifier | DV_IDENTIFIER / DV_TEXT |
| at0018 | Service provider identifier | DV_IDENTIFIER / DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0027 | Service detail | any archetype |
| at0029 | Multimedia representation | openEHR-EHR-CLUSTER.media_file(-[a-zA-Z0-9_]+)*.v1 |
| at0036 | Additional details | any archetype |
| at0017 | Requestor | openEHR-EHR-CLUSTER.person(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 |
| at0019 | Receiver | openEHR-EHR-CLUSTER.person(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 |

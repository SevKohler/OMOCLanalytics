# openEHR-EHR-ACTION.procedure.v1

**Concept:** Procedure

**Category:** entry/action

**Element leaves:** 21  |  **Cluster slot leaves:** 4  |  **Total leaves:** 25


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0002 | Procedure name | DV_TEXT |
| at0049 | Description | DV_TEXT |
| at0070 | Indication | DV_TEXT |
| at0072 | Intent | DV_TEXT |
| at0065 | Method | DV_TEXT |
| at0058 | Urgency | DV_TEXT |
| at0063 | Body site | DV_TEXT |
| at0071 | Impact | DV_TEXT |
| at0048 | Outcome | DV_TEXT |
| at0069 | Procedural difficulty | DV_TEXT |
| at0006 | Complication | DV_TEXT |
| at0066 | Scheduled datetime | DV_DATE_TIME |
| at0073 | Start datetime | DV_DATE_TIME |
| at0060 | End datetime | DV_DATE_TIME |
| at0061 | Total duration | DV_DURATION |
| at0074 | Pathway step duration | DV_DURATION |
| at0067 | Procedure type | DV_TEXT |
| at0014 | Reason | DV_TEXT |
| at0005 | Comment | DV_TEXT |
| at0054 | Requestor order identifier | DV_TEXT / DV_IDENTIFIER |
| at0056 | Receiver order identifier | DV_TEXT / DV_IDENTIFIER |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0003 | Procedure detail | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_circle(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_relative(-[a-zA-Z0-9_]+)*.v2 |
| at0062 | Multimedia | openEHR-EHR-CLUSTER.media_file.v1 |
| at0055 | Requestor | any archetype |
| at0057 | Receiver | any archetype |

# openEHR-EHR-CLUSTER.person.v1

**Concept:** Person

**Category:** cluster

**Element leaves:** 5  |  **Cluster slot leaves:** 6  |  **Total leaves:** 11


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0001 | Name | DV_TEXT |
| at0011 | Label | DV_TEXT |
| at0003 | Identifier | DV_IDENTIFIER / DV_TEXT |
| at0004 | Role | DV_TEXT |
| at0010 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0002 | Structured name | openEHR-EHR-CLUSTER.structured_name(-[a-zA-Z0-9_]+)*.v1 |
| at0005 | Address | openEHR-EHR-CLUSTER.address(-[a-zA-Z0-9_]+)*.v1 |
| at0006 | Electronic communication | openEHR-EHR-CLUSTER.electronic_communication(-[a-zA-Z0-9_]+)*.v1 |
| at0007 | Organisation | openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 |
| at0008 | Additional details | any archetype |
| at0009 | Photo | openEHR-EHR-CLUSTER.media_file(-[a-zA-Z0-9_]+)*.v1 |

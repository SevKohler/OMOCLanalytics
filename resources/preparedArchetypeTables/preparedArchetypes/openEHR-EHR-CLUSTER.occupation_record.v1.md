# openEHR-EHR-CLUSTER.occupation_record.v1

**Concept:** Occupation record

**Category:** cluster

**Element leaves:** 10  |  **Cluster slot leaves:** 2  |  **Total leaves:** 12


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0005 | Job title/role | DV_TEXT |
| at0016 | Description | DV_TEXT |
| at0007 | Date commenced | DV_DATE_TIME |
| at0001 | Paid employment status | DV_TEXT |
| at0013 | Full time equivalent | DV_PROPORTION / DV_CODED_TEXT / DV_TEXT |
| at0019 | Time allocated | DV_QUANTITY |
| at0002 | Industry category | DV_TEXT |
| at0006 | Job category | DV_TEXT |
| at0008 | Date ceased | DV_DATE_TIME |
| at0014 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0004 | Organisation details | openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 |
| at0018 | Additional details | any archetype |

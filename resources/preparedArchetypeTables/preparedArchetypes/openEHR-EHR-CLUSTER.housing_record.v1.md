# openEHR-EHR-CLUSTER.housing_record.v1

**Concept:** Housing record

**Category:** cluster

**Element leaves:** 7  |  **Cluster slot leaves:** 2  |  **Total leaves:** 9


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0005 | Name/label | DV_TEXT |
| at0016 | Description | DV_TEXT |
| at0007 | Date commenced | DV_DATE_TIME |
| at0001 | Residential setting | DV_TEXT |
| at0013 | Tenure | DV_TEXT |
| at0008 | Date ceased | DV_DATE_TIME |
| at0014 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0004 | Address details | openEHR-EHR-CLUSTER.address(-[a-zA-Z0-9_]+)*.v1 |
| at0018 | Additional details | openEHR-EHR-CLUSTER.living_arrangement(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.dwelling(-[a-zA-Z0-9_]+)*.v0 |

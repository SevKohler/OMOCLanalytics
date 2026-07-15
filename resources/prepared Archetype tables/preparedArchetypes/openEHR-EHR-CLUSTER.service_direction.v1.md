# openEHR-EHR-CLUSTER.service_direction.v1

**Concept:** Service direction

**Category:** cluster

**Element leaves:** 6  |  **Cluster slot leaves:** 3  |  **Total leaves:** 9


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0001 | Direction sequence | DV_COUNT |
| at0002 | Direction description | DV_TEXT |
| at0004 | Activity sequence | DV_COUNT |
| at0005 | Amount | DV_COUNT / DV_DURATION |
| at0007 | Direction duration | DV_CODED_TEXT / DV_DURATION / DV_TEXT |
| at0011 | Total amount | DV_COUNT / DV_DURATION |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0006 | Intraday timing | openEHR-EHR-CLUSTER.timing_daily.v1 |
| at0010 | Repetition timing | openEHR-EHR-CLUSTER.timing_nondaily.v1 |
| at0012 | Additional details | any archetype |

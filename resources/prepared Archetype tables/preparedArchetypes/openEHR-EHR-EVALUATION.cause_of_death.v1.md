# openEHR-EHR-EVALUATION.cause_of_death.v1

**Concept:** Cause of death

**Category:** entry/evaluation

**Element leaves:** 10  |  **Cluster slot leaves:** 1  |  **Total leaves:** 11


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0019 | Description | DV_TEXT |
| at0002 | Direct cause | DV_TEXT |
| at0017 | Direct cause duration | DV_DURATION / DV_INTERVAL / DV_TEXT |
| at0004 | Cause | DV_TEXT |
| at0005 | Order | DV_TEXT / DV_CODED_TEXT |
| at0009 | Duration | DV_TEXT / DV_INTERVAL / DV_DURATION / DV_DATE_TIME |
| at0018 | Condition | DV_TEXT |
| at0021 | Duration | DV_TEXT / DV_INTERVAL / DV_DURATION / DV_DATE_TIME |
| at0013 | Comment | DV_TEXT |
| at0015 | Last updated | DV_DATE_TIME |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0012 | Additional details | any archetype |

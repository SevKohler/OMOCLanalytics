# openEHR-EHR-EVALUATION.cause_of_death.v1

**Concept:** Cause of death

**Category:** entry/evaluation

**Element leaves:** 9  |  **Cluster slot leaves:** 1  |  **Total leaves:** 10


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0019 |  | Description | DV_TEXT |
| at0002 |  | Direct cause | DV_TEXT |
| at0017 |  | Direct cause duration | DV_DURATION / DV_INTERVAL / DV_TEXT |
| at0004 | Antecedent cause(s) | Cause | DV_TEXT |
| at0005 | Antecedent cause(s) | Order | DV_TEXT / DV_CODED_TEXT |
| at0009 | Antecedent cause(s) | Duration | DV_TEXT / DV_INTERVAL / DV_DURATION / DV_DATE_TIME |
| at0018 | Contributing conditions | Condition | DV_TEXT |
| at0021 | Contributing conditions | Duration | DV_TEXT / DV_INTERVAL / DV_DURATION / DV_DATE_TIME |
| at0013 |  | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0012 | Additional details | any archetype |

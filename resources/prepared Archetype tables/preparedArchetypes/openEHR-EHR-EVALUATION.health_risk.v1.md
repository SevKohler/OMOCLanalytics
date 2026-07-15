# openEHR-EHR-EVALUATION.health_risk.v1

**Concept:** Health risk assessment

**Category:** entry/evaluation

**Element leaves:** 15  |  **Cluster slot leaves:** 1  |  **Total leaves:** 16


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0002 | Health risk | DV_TEXT |
| at0013 | Risk factor | DV_TEXT |
| at0017 | Presence | DV_CODED_TEXT |
| at0014 | Description | DV_TEXT |
| at0029 | Date identified | DV_DATE_TIME |
| at0028 | Mitigated | DV_BOOLEAN |
| at0012 | Link to evidence | DV_URI |
| at0030 | Comment | DV_TEXT |
| at0003 | Risk assessment | DV_TEXT / DV_PROPORTION / DV_QUANTITY |
| at0020 | Assessment type | DV_CODED_TEXT |
| at0023 | Time period | DV_DURATION |
| at0004 | Rationale | DV_TEXT |
| at0015 | Comment | DV_TEXT |
| at0024 | Last updated | DV_DATE_TIME |
| at0025 | Assessment method | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0027 | Detail | openEHR-EHR-CLUSTER.family_prevalence.v1 |

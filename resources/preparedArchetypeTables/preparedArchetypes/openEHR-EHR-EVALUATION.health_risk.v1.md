# openEHR-EHR-EVALUATION.health_risk.v1

**Concept:** Health risk assessment

**Category:** entry/evaluation

**Element leaves:** 14  |  **Cluster slot leaves:** 1  |  **Total leaves:** 15


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0002 |  | Health risk | DV_TEXT |
| at0013 | Risk factors | Risk factor | DV_TEXT |
| at0017 | Risk factors | Presence | DV_CODED_TEXT |
| at0014 | Risk factors | Description | DV_TEXT |
| at0029 | Risk factors | Date identified | DV_DATE_TIME |
| at0028 | Risk factors | Mitigated | DV_BOOLEAN |
| at0012 | Risk factors | Link to evidence | DV_URI |
| at0030 | Risk factors | Comment | DV_TEXT |
| at0003 |  | Risk assessment | DV_TEXT / DV_PROPORTION / DV_QUANTITY |
| at0020 |  | Assessment type | DV_CODED_TEXT |
| at0023 |  | Time period | DV_DURATION |
| at0004 |  | Rationale | DV_TEXT |
| at0015 |  | Comment | DV_TEXT |
| at0025 |  | Assessment method | DV_TEXT |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0027 | Risk factors | Detail | openEHR-EHR-CLUSTER.family_prevalence.v1 |

# openEHR-EHR-EVALUATION.goal.v1

**Concept:** Goal

**Category:** entry/evaluation

**Element leaves:** 17  |  **Cluster slot leaves:** 1  |  **Total leaves:** 18


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0002 | Goal name | DV_TEXT |
| at0012 | Goal description | DV_TEXT |
| at0010 | Clinical indication | DV_TEXT |
| at0025 | Goal start date | DV_DATE_TIME |
| at0003 | Goal proposed date | DV_DATE |
| at0004 | Goal end date | DV_DATE |
| at0013 | Goal outcome | DV_TEXT / DV_CODED_TEXT |
| at0022 | Goal comment | DV_TEXT |
| at0011 | Target name | DV_TEXT |
| at0007 | Target | DV_INTERVAL / DV_COUNT / DV_QUANTITY / DV_DURATION / DV_PROPORTION / DV_TEXT |
| at0024 | Target description | DV_TEXT |
| at0006 | Target path | DV_URI |
| at0008 | Target proposed date | DV_DATE |
| at0009 | Target end date | DV_DATE |
| at0018 | Target outcome | DV_TEXT / DV_CODED_TEXT |
| at0023 | Target comment | DV_TEXT |
| at0029 | Last updated | DV_DATE_TIME |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0028 | Readiness for change | openEHR-EHR-CLUSTER.change(-[a-zA-Z0-9_]+)*.v1 |

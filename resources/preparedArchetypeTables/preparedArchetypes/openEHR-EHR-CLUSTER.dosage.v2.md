# openEHR-EHR-CLUSTER.dosage.v2

**Concept:** Dosage

**Category:** cluster

**Element leaves:** 7  |  **Cluster slot leaves:** 1  |  **Total leaves:** 8


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0164 | Dosage sequence | DV_COUNT |
| at0144 | Dose | DV_QUANTITY / DV_INTERVAL |
| at0135 | Dose formula | DV_TEXT / DV_QUANTITY |
| at0178 | Dose description | DV_TEXT |
| at0134 | Administration rate | DV_QUANTITY / DV_TEXT |
| at0102 | Administration duration | DV_DURATION / DV_INTERVAL |
| at0176 | Alternate dose | DV_QUANTITY / DV_INTERVAL |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0037 | Daily timing | openEHR-EHR-CLUSTER.timing_daily(-[a-zA-Z0-9_]+)*.v1 |

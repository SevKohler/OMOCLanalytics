# openEHR-EHR-CLUSTER.dosage.v1

**Concept:** Dosage

**Category:** cluster

**Element leaves:** 9  |  **Cluster slot leaves:** 1  |  **Total leaves:** 10


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0164 | Dosage sequence | DV_COUNT |
| at0144 | Dose amount | DV_QUANTITY / DV_INTERVAL |
| at0145 | Dose unit | DV_TEXT |
| at0135 | Dose formula | DV_TEXT / DV_QUANTITY |
| at0178 | Dose description | DV_TEXT |
| at0134 | Administration rate | DV_QUANTITY / DV_TEXT |
| at0102 | Administration duration | DV_DURATION |
| at0176 | Alternate dose amount | DV_QUANTITY / DV_INTERVAL |
| at0177 | Alternate dose unit | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0037 | Daily timing | openEHR-EHR-CLUSTER.timing_daily(-[a-zA-Z0-9_]+)*.v1 |

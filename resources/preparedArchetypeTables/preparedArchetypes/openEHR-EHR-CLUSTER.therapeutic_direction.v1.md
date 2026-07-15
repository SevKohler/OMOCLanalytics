# openEHR-EHR-CLUSTER.therapeutic_direction.v1

**Concept:** Therapeutic direction

**Category:** cluster

**Element leaves:** 6  |  **Cluster slot leaves:** 3  |  **Total leaves:** 9


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0057 | Direction sequence | DV_COUNT |
| at0066 | Direction duration | DV_CODED_TEXT / DV_DURATION / DV_TEXT / DV_INTERVAL |
| at0172 | Number of administrations | DV_COUNT / DV_INTERVAL |
| at0177 | Review criterion | DV_QUANTITY / DV_COUNT / DV_TEXT |
| at0178 | Order start date/time | DV_DATE_TIME |
| at0179 | Order stop date/time | DV_DATE_TIME |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0176 | Dosage | openEHR-EHR-CLUSTER.dosage(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.dosage(-[a-zA-Z0-9_]+)*.v2 |
| at0090 | Repetition timing | openEHR-EHR-CLUSTER.timing_nondaily(-[a-zA-Z0-9_]+)*.v1 |
| at0156 | Additional details | openEHR-EHR-CLUSTER.conditional_medication_rules(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.conditional_medication_rules(-[a-zA-Z0-9_]+)*.v1 |

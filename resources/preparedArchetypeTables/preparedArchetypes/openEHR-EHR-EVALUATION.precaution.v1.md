# openEHR-EHR-EVALUATION.precaution.v1

**Concept:** Precaution

**Category:** entry/evaluation

**Element leaves:** 8  |  **Cluster slot leaves:** 1  |  **Total leaves:** 9


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0002 | Condition | DV_TEXT |
| at0014 | Status | DV_CODED_TEXT / DV_TEXT |
| at0003 | Evidence | DV_TEXT |
| at0013 | Category | DV_TEXT |
| at0008 | Comment | DV_TEXT |
| at0022 | Valid period start | DV_DATE_TIME |
| at0024 | Valid period end | DV_DATE_TIME |
| at0009 | Review date | DV_DATE_TIME |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0025 | Additional details | openEHR-EHR-CLUSTER.clinical_evidence.v1 |

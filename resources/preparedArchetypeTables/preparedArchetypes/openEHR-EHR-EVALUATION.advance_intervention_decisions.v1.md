# openEHR-EHR-EVALUATION.advance_intervention_decisions.v1

**Concept:** Advance intervention decisions

**Category:** entry/evaluation

**Element leaves:** 16  |  **Cluster slot leaves:** 3  |  **Total leaves:** 19


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0002 |  | Intent of care | DV_CODED_TEXT / DV_TEXT |
| at0056 |  | Rationale | DV_TEXT |
| at0008 |  | Decisions description | DV_TEXT |
| at0009 |  | CPR decision | DV_TEXT / DV_CODED_TEXT |
| at0015 | Per intervention | Intervention | DV_CODED_TEXT / DV_TEXT |
| at0034 | Per intervention | Decision | DV_CODED_TEXT |
| at0039 | Per intervention | Precondition | DV_TEXT |
| at0040 | Per intervention | Comment | DV_TEXT |
| at0042 |  | Patient awareness | DV_TEXT |
| at0043 |  | Carer awareness | DV_TEXT |
| at0044 |  | Overall comment | DV_TEXT |
| at0047 |  | Valid period start | DV_DATE_TIME |
| at0048 |  | Valid period end | DV_DATE_TIME |
| at0049 |  | Review due | DV_DATE_TIME |
| at0050 |  | Mandate | DV_TEXT / DV_EHR_URI |
| at0053 | Document location | Location | DV_TEXT / DV_URI |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0041 |  | Additional details | any archetype |
| at0051 |  | Digital representation | openEHR-EHR-CLUSTER.multimedia_source.v0 |
| at0054 | Document location | Copy holder | any archetype |

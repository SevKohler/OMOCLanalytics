# openEHR-EHR-EVALUATION.advance_intervention_decisions.v1

**Concept:** Advance intervention decisions

**Category:** entry/evaluation

**Element leaves:** 17  |  **Cluster slot leaves:** 3  |  **Total leaves:** 20


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0002 | Intent of care | DV_CODED_TEXT / DV_TEXT |
| at0056 | Rationale | DV_TEXT |
| at0008 | Decisions description | DV_TEXT |
| at0009 | CPR decision | DV_TEXT / DV_CODED_TEXT |
| at0015 | Intervention | DV_CODED_TEXT / DV_TEXT |
| at0034 | Decision | DV_CODED_TEXT |
| at0039 | Precondition | DV_TEXT |
| at0040 | Comment | DV_TEXT |
| at0042 | Patient awareness | DV_TEXT |
| at0043 | Carer awareness | DV_TEXT |
| at0044 | Overall comment | DV_TEXT |
| at0046 | Last updated | DV_DATE_TIME |
| at0047 | Valid period start | DV_DATE_TIME |
| at0048 | Valid period end | DV_DATE_TIME |
| at0049 | Review due | DV_DATE_TIME |
| at0050 | Mandate | DV_TEXT / DV_EHR_URI |
| at0053 | Location | DV_TEXT / DV_URI |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0041 | Additional details | any archetype |
| at0051 | Digital representation | openEHR-EHR-CLUSTER.multimedia_source.v0 |
| at0054 | Copy holder | any archetype |

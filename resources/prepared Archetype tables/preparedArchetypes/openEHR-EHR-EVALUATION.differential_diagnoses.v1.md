# openEHR-EHR-EVALUATION.differential_diagnoses.v1

**Concept:** Differential diagnoses

**Category:** entry/evaluation

**Element leaves:** 7  |  **Cluster slot leaves:** 1  |  **Total leaves:** 8


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0002 | Overall description | DV_TEXT |
| at0004 | Diagnosis name | DV_TEXT |
| at0005 | Status | DV_CODED_TEXT / DV_TEXT |
| at0009 | Rationale | DV_TEXT |
| at0011 | Order | DV_COUNT |
| at0012 | Comment | DV_TEXT |
| at0015 | Last updated | DV_DATE_TIME |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0010 | Clinical evidence | openEHR-EHR-CLUSTER.clinical_evidence.v1 |

# openEHR-EHR-EVALUATION.differential_diagnoses.v1

**Concept:** Differential diagnoses

**Category:** entry/evaluation

**Element leaves:** 6  |  **Cluster slot leaves:** 1  |  **Total leaves:** 7


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0002 |  | Overall description | DV_TEXT |
| at0004 | Per differential | Diagnosis name | DV_TEXT |
| at0005 | Per differential | Status | DV_CODED_TEXT / DV_TEXT |
| at0009 | Per differential | Rationale | DV_TEXT |
| at0011 | Per differential | Order | DV_COUNT |
| at0012 | Per differential | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0010 | Per differential | Clinical evidence | openEHR-EHR-CLUSTER.clinical_evidence.v1 |

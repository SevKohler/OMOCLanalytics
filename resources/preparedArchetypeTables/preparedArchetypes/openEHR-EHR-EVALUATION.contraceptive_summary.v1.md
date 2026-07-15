# openEHR-EHR-EVALUATION.contraceptive_summary.v1

**Concept:** Contraceptive use summary

**Category:** entry/evaluation

**Element leaves:** 18  |  **Cluster slot leaves:** 3  |  **Total leaves:** 21


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0089 |  | Overall status | DV_CODED_TEXT |
| at0043 |  | Overall description | DV_TEXT |
| at0151 | Per type | Type | DV_TEXT / DV_CODED_TEXT |
| at0144 | Per type | Status | DV_CODED_TEXT |
| at0053 | Per type | Description | DV_TEXT |
| at0148 | Per type | Start date | DV_DATE_TIME |
| at0081 | Per type > Per episode | Episode label | DV_COUNT / DV_TEXT |
| at0023 | Per type > Per episode | Specific name | DV_TEXT |
| at0030 | Per type > Per episode | Description | DV_TEXT |
| at0168 | Per type > Per episode | Clinical indication | DV_TEXT |
| at0025 | Per type > Per episode | Goal | DV_TEXT |
| at0013 | Per type > Per episode | Episode start date | DV_DATE |
| at0082 | Per type > Per episode | Episode end date | DV_DATE |
| at0074 | Per type > Per episode | Reason for cessation | DV_TEXT |
| at0087 | Per type > Per episode | Episode comment | DV_TEXT |
| at0149 | Per type | End date | DV_DATE_TIME |
| at0069 | Per type | Comment | DV_TEXT |
| at0019 |  | Overall comment | DV_TEXT |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0026 | Per type > Per episode | Episode details | any archetype |
| at0077 | Per type | Type details | any archetype |
| at0150 |  | Overall details | any archetype |

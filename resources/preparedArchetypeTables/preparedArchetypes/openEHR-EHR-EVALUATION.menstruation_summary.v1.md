# openEHR-EHR-EVALUATION.menstruation_summary.v1

**Concept:** Menstruation summary

**Category:** entry/evaluation

**Element leaves:** 13  |  **Cluster slot leaves:** 1  |  **Total leaves:** 14


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0025 |  | Overall description | DV_TEXT |
| at0003 |  | Menstrual status | DV_CODED_TEXT |
| at0002 |  | Menarche | DV_DURATION / DV_DATE |
| at0011 | Per episode | Episode label | DV_TEXT |
| at0012 | Per episode | Episode start date | DV_DATE_TIME |
| at0013 | Per episode | Description | DV_TEXT |
| at0014 | Per episode | Typical pattern | DV_CODED_TEXT |
| at0017 | Per episode | Typical cycle length | DV_DURATION / DV_INTERVAL |
| at0018 | Per episode | Typical menses duration | DV_DURATION / DV_INTERVAL |
| at0021 | Per episode | Episode end date | DV_DATE_TIME |
| at0022 | Per episode | Episode comment | DV_TEXT |
| at0004 |  | Menopause | DV_DURATION / DV_DATE |
| at0023 |  | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0020 | Per episode | Additional details | any archetype |

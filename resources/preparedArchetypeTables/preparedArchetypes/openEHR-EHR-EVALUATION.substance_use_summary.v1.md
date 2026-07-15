# openEHR-EHR-EVALUATION.substance_use_summary.v1

**Concept:** Substance use summary

**Category:** entry/evaluation

**Element leaves:** 19  |  **Cluster slot leaves:** 2  |  **Total leaves:** 21


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0002 |  | Substance name | DV_TEXT |
| at0003 |  | Overall status | DV_CODED_TEXT |
| at0007 |  | Overall description | DV_TEXT |
| at0008 |  | First ever use | DV_DATE_TIME |
| at0009 |  | Regular use commenced | DV_DATE_TIME |
| at0010 |  | Daily use commenced | DV_DATE_TIME |
| at0013 | Per episode | Episode label | DV_COUNT / DV_TEXT |
| at0014 | Per episode | Episode start date | DV_DATE_TIME |
| at0016 | Per episode | Specific substance name | DV_TEXT |
| at0017 | Per episode | Status | DV_CODED_TEXT |
| at0018 | Per episode | Episode description | DV_TEXT |
| at0019 | Per episode | Pattern | DV_TEXT / DV_CODED_TEXT / DV_QUANTITY |
| at0023 | Per episode | Typical amount | DV_QUANTITY / DV_TEXT |
| at0036 | Per episode | Route | DV_TEXT |
| at0015 | Per episode | Episode end date | DV_DATE_TIME |
| at0024 | Per episode | Number of quit attempts | DV_COUNT |
| at0026 | Per episode | Episode comment | DV_DATE_TIME |
| at0028 |  | Overall quit date | DV_DATE_TIME |
| at0030 |  | Overall comment | DV_TEXT |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0025 | Per episode | Episode details | any archetype |
| at0027 |  | Overall details | any archetype |

# openEHR-EHR-EVALUATION.substance_use_summary.v1

**Concept:** Substance use summary

**Category:** entry/evaluation

**Element leaves:** 20  |  **Cluster slot leaves:** 2  |  **Total leaves:** 22


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0002 | Substance name | DV_TEXT |
| at0003 | Overall status | DV_CODED_TEXT |
| at0007 | Overall description | DV_TEXT |
| at0008 | First ever use | DV_DATE_TIME |
| at0009 | Regular use commenced | DV_DATE_TIME |
| at0010 | Daily use commenced | DV_DATE_TIME |
| at0013 | Episode label | DV_COUNT / DV_TEXT |
| at0014 | Episode start date | DV_DATE_TIME |
| at0016 | Specific substance name | DV_TEXT |
| at0017 | Status | DV_CODED_TEXT |
| at0018 | Episode description | DV_TEXT |
| at0019 | Pattern | DV_TEXT / DV_CODED_TEXT / DV_QUANTITY |
| at0023 | Typical amount | DV_QUANTITY / DV_TEXT |
| at0036 | Route | DV_TEXT |
| at0015 | Episode end date | DV_DATE_TIME |
| at0024 | Number of quit attempts | DV_COUNT |
| at0026 | Episode comment | DV_DATE_TIME |
| at0028 | Overall quit date | DV_DATE_TIME |
| at0030 | Overall comment | DV_TEXT |
| at0031 | Last updated | DV_DATE_TIME |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0025 | Episode details | any archetype |
| at0027 | Overall details | any archetype |

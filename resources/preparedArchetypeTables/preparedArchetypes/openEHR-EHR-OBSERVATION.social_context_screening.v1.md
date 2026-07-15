# openEHR-EHR-OBSERVATION.social_context_screening.v1

**Concept:** Social context screening questionnaire

**Category:** entry/observation

**Element leaves:** 6  |  **Cluster slot leaves:** 2  |  **Total leaves:** 8


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0034 |  | Screening purpose | DV_TEXT |
| at0004 | Specific social context | Context | DV_TEXT / DV_CODED_TEXT |
| at0005 | Specific social context | Presence? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0051 | Specific social context | Timing | DV_TEXT / DV_DATE_TIME / DV_DURATION / DV_INTERVAL |
| at0025 | Specific social context | Comment | DV_TEXT |
| at0052 |  | Overall comment | DV_TEXT |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0026 | Specific social context | Additional details | any archetype |
| at0044 |  | Additional details | any archetype |

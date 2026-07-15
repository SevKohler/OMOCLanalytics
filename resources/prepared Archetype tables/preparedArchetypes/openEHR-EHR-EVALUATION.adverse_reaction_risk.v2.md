# openEHR-EHR-EVALUATION.adverse_reaction_risk.v2

**Concept:** Adverse reaction risk

**Category:** entry/evaluation

**Element leaves:** 11  |  **Cluster slot leaves:** 1  |  **Total leaves:** 12


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0002 | Substance | DV_TEXT |
| at0130 | Active/inactive status | DV_CODED_TEXT / DV_TEXT |
| at0063 | Verification status | DV_CODED_TEXT / DV_TEXT |
| at0101 | Criticality | DV_CODED_TEXT / DV_TEXT |
| at0120 | Category | DV_CODED_TEXT / DV_TEXT |
| at0117 | Onset of last reaction | DV_DATE_TIME / DV_DURATION / DV_INTERVAL / DV_TEXT |
| at0133 | Onset of first reaction | DV_DATE_TIME / DV_DURATION / DV_TEXT / DV_INTERVAL |
| at0058 | Reaction mechanism | DV_CODED_TEXT / DV_TEXT |
| at0006 | Comment | DV_TEXT |
| at0062 | Last updated | DV_DATE_TIME |
| at0047 | Supporting clinical record information | DV_EHR_URI |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0129 | Reaction event summary | openEHR-EHR-CLUSTER.adverse_reaction_event(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.adverse_reaction_event(-[a-zA-Z0-9_]+)*.v1 |

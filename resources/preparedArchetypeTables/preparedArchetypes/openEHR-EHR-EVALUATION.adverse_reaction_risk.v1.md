# openEHR-EHR-EVALUATION.adverse_reaction_risk.v1

**Concept:** Adverse reaction risk

**Category:** entry/evaluation

**Element leaves:** 25  |  **Cluster slot leaves:** 5  |  **Total leaves:** 30


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0002 |  | Substance | DV_TEXT |
| at0063 |  | Status | DV_CODED_TEXT / DV_TEXT |
| at0101 |  | Criticality | DV_CODED_TEXT |
| at0120 |  | Category | DV_CODED_TEXT / DV_TEXT |
| at0117 |  | Onset of last reaction | DV_DATE_TIME |
| at0058 |  | Reaction mechanism | DV_CODED_TEXT / DV_TEXT |
| at0006 |  | Comment | DV_TEXT |
| at0010 | Reaction event | Specific substance | DV_TEXT |
| at0021 | Reaction event | Certainty | DV_CODED_TEXT |
| at0011 | Reaction event | Manifestation | DV_TEXT |
| at0012 | Reaction event | Reaction description | DV_TEXT |
| at0027 | Reaction event | Onset of reaction | DV_DATE_TIME |
| at0028 | Reaction event | Duration of reaction | DV_DURATION |
| at0089 | Reaction event | Severity of reaction | DV_CODED_TEXT / DV_TEXT |
| at0020 | Reaction event | Initial exposure | DV_DATE_TIME |
| at0025 | Reaction event | Duration of exposure | DV_DURATION |
| at0106 | Reaction event | Route of exposure | DV_TEXT |
| at0018 | Reaction event | Exposure description | DV_TEXT |
| at0040 | Reaction event | Clinical management description | DV_TEXT |
| at0032 | Reaction event | Reaction comment | DV_TEXT |
| at0047 |  | Supporting clinical record information | DV_EHR_URI |
| at0044 |  | Reaction reported? | DV_BOOLEAN |
| at0125 | Report summary | Date of report | DV_DATE_TIME |
| at0048 | Report summary | Report comment | DV_TEXT |
| at0045 | Report summary | Adverse reaction report | DV_URI |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0029 | Reaction event | Reaction details | openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.media_capture(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.anatomical_location_relative(-[a-zA-Z0-9_]+)*.v2 / openEHR-EHR-CLUSTER.symptom_sign(-[a-zA-Z0-9_]+)*.v1 |
| at0096 | Reaction event | Exposure details | openEHR-EHR-CLUSTER.citation(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.citation(-[a-zA-Z0-9_]+)*.v0 |
| at0119 | Reaction event | Clinical management details | any archetype |
| at0041 | Reaction event | Reporting details | any archetype |
| at0116 | Reaction event | Information source | any archetype |

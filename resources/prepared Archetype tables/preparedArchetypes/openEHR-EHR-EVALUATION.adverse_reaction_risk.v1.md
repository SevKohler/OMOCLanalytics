# openEHR-EHR-EVALUATION.adverse_reaction_risk.v1

**Concept:** Adverse reaction risk

**Category:** entry/evaluation

**Element leaves:** 26  |  **Cluster slot leaves:** 5  |  **Total leaves:** 31


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0002 | Substance | DV_TEXT |
| at0063 | Status | DV_CODED_TEXT / DV_TEXT |
| at0101 | Criticality | DV_CODED_TEXT |
| at0120 | Category | DV_CODED_TEXT / DV_TEXT |
| at0117 | Onset of last reaction | DV_DATE_TIME |
| at0058 | Reaction mechanism | DV_CODED_TEXT / DV_TEXT |
| at0006 | Comment | DV_TEXT |
| at0010 | Specific substance | DV_TEXT |
| at0021 | Certainty | DV_CODED_TEXT |
| at0011 | Manifestation | DV_TEXT |
| at0012 | Reaction description | DV_TEXT |
| at0027 | Onset of reaction | DV_DATE_TIME |
| at0028 | Duration of reaction | DV_DURATION |
| at0089 | Severity of reaction | DV_CODED_TEXT / DV_TEXT |
| at0020 | Initial exposure | DV_DATE_TIME |
| at0025 | Duration of exposure | DV_DURATION |
| at0106 | Route of exposure | DV_TEXT |
| at0018 | Exposure description | DV_TEXT |
| at0040 | Clinical management description | DV_TEXT |
| at0032 | Reaction comment | DV_TEXT |
| at0062 | Last updated | DV_DATE_TIME |
| at0047 | Supporting clinical record information | DV_EHR_URI |
| at0044 | Reaction reported? | DV_BOOLEAN |
| at0125 | Date of report | DV_DATE_TIME |
| at0048 | Report comment | DV_TEXT |
| at0045 | Adverse reaction report | DV_URI |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0029 | Reaction details | openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.media_capture(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.anatomical_location_relative(-[a-zA-Z0-9_]+)*.v2 / openEHR-EHR-CLUSTER.symptom_sign(-[a-zA-Z0-9_]+)*.v1 |
| at0096 | Exposure details | openEHR-EHR-CLUSTER.citation(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.citation(-[a-zA-Z0-9_]+)*.v0 |
| at0119 | Clinical management details | any archetype |
| at0041 | Reporting details | any archetype |
| at0116 | Information source | any archetype |

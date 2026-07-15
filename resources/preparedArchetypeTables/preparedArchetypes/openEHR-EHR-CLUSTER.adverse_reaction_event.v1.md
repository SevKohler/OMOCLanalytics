# openEHR-EHR-CLUSTER.adverse_reaction_event.v1

**Concept:** Adverse reaction event

**Category:** cluster

**Element leaves:** 14  |  **Cluster slot leaves:** 5  |  **Total leaves:** 19


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0001 | Specific substance | DV_TEXT |
| at0002 | Certainty | DV_CODED_TEXT / DV_TEXT |
| at0006 | Manifestation | DV_TEXT |
| at0007 | Reaction description | DV_TEXT |
| at0008 | Onset of reaction | DV_DATE_TIME |
| at0009 | Duration of reaction | DV_DURATION |
| at0010 | Severity of reaction | DV_CODED_TEXT / DV_TEXT |
| at0015 | Initial exposure | DV_DATE_TIME |
| at0016 | Duration of exposure | DV_DURATION |
| at0017 | Route of exposure | DV_TEXT |
| at0018 | Exposure description | DV_TEXT |
| at0020 | Clinical management description | DV_TEXT |
| at0025 | Supporting clinical record information | DV_EHR_URI |
| at0024 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0014 | Reaction details | openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.media_file(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_relative(-[a-zA-Z0-9_]+)*.v2 / openEHR-EHR-CLUSTER.symptom_sign(-[a-zA-Z0-9_]+)*.v2 / openEHR-EHR-CLUSTER.ctcae(-[a-zA-Z0-9_]+)*.v1 |
| at0019 | Exposure details | openEHR-EHR-CLUSTER.citation(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.citation(-[a-zA-Z0-9_]+)*.v0 |
| at0021 | Clinical management details | any archetype |
| at0022 | Reporting details | any archetype |
| at0023 | Information source | openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.person(-[a-zA-Z0-9_]+)*.v1 |

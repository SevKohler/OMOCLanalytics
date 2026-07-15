# openEHR-EHR-CLUSTER.specimen.v1

**Concept:** Specimen

**Category:** cluster

**Element leaves:** 20  |  **Cluster slot leaves:** 9  |  **Total leaves:** 29


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0029 | Specimen type | DV_TEXT |
| at0098 | Specimen label | DV_TEXT |
| at0097 | Specimen description | DV_TEXT |
| at0099 | Number of fragments | DV_COUNT |
| at0001 | Laboratory specimen identifier | DV_IDENTIFIER / DV_TEXT |
| at0088 | External identifier | DV_IDENTIFIER / DV_TEXT |
| at0034 | Date/time received | DV_DATE_TIME |
| at0008 | Sampling context | DV_TEXT |
| at0007 | Collection method | DV_TEXT |
| at0079 | Collection description | DV_TEXT |
| at0087 | Source site | DV_TEXT |
| at0015 | Collection date/time | DV_DATE_TIME / DV_INTERVAL |
| at0005 | Hazard warning | DV_TEXT |
| at0067 | Collection setting | DV_TEXT |
| at0070 | Specimen collector identifier | DV_IDENTIFIER / DV_TEXT |
| at0080 | Number of containers | DV_COUNT |
| at0003 | Parent specimen identifier | DV_IDENTIFIER / DV_TEXT |
| at0042 | Specimen quality issue | DV_CODED_TEXT / DV_TEXT |
| at0041 | Adequacy for testing | DV_CODED_TEXT / DV_TEXT |
| at0045 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0027 | Physical properties | openEHR-EHR-CLUSTER.specimen_measurements(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.inspection_body_fluid(-[a-zA-Z0-9_]+)*.v0 |
| at0013 | Structured source site | openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_circle(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_relative(-[a-zA-Z0-9_]+)*.v2 |
| at0071 | Specimen collector details | openEHR-EHR-CLUSTER.person(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 |
| at0083 | Additional details | any archetype |
| at0085 | Container details | openEHR-EHR-CLUSTER.specimen_container(-[a-zA-Z0-9_]+)*.v1 |
| at0068 | Processing details | openEHR-EHR-CLUSTER.specimen_preparation(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.specimen_preparation(-[a-zA-Z0-9_]+)*.v0 |
| at0100 | Storage details | openEHR-EHR-CLUSTER.biobank_storage(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.biobank_storage(-[a-zA-Z0-9_]+)*.v1 |
| at0093 | Transport details | openEHR-EHR-CLUSTER.specimen_transport(-[a-zA-Z0-9_]+)*.v1 |
| at0096 | Digital representation | openEHR-EHR-CLUSTER.media_file(-[a-zA-Z0-9_]+)*.v1 |

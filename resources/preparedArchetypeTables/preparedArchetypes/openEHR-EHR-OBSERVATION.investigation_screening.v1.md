# openEHR-EHR-OBSERVATION.investigation_screening.v1

**Concept:** Diagnostic investigation screening questionnaire

**Category:** entry/observation

**Element leaves:** 9  |  **Cluster slot leaves:** 2  |  **Total leaves:** 11


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0040 |  | Screening purpose | DV_TEXT |
| at0027 |  | Any investigations? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0043 |  | Description | DV_TEXT |
| at0021 | Specific investigation | Investigation name | DV_TEXT |
| at0024 | Specific investigation | Done? | DV_CODED_TEXT / DV_TEXT / DV_BOOLEAN |
| at0047 | Specific investigation | Type | DV_TEXT |
| at0003 | Specific investigation | Timing | DV_DATE_TIME / DV_TEXT / DV_INTERVAL / DV_DURATION |
| at0002 | Specific investigation | Conclusion | DV_TEXT |
| at0025 | Specific investigation | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0041 | Specific investigation | Additional details | openEHR-EHR-CLUSTER.imaging_exam(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.organisation.v1 / openEHR-EHR-CLUSTER.lab_microscopy_parasitology.v0 / openEHR-EHR-CLUSTER.lab_antibody.v0 / openEHR-EHR-CLUSTER.laboratory_test_analyte.v1 / openEHR-EHR-CLUSTER.lab_antigen.v0 / openEHR-EHR-CLUSTER.lab_blood_cell_count.v0 / openEHR-EHR-CLUSTER.lab_microscopy_culture.v0 / openEHR-EHR-CLUSTER.lab_microscopy_stain.v0 / openEHR-EHR-CLUSTER.lab_molecular_microbial.v0 / openEHR-EHR-CLUSTER.specimen.v1 |
| at0044 |  | Additional details | any archetype |

# openEHR-EHR-EVALUATION.specimen_summary.v1

**Concept:** Specimen summary

**Category:** entry/evaluation

**Element leaves:** 15  |  **Cluster slot leaves:** 5  |  **Total leaves:** 20


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0032 |  | Specimen label | DV_TEXT |
| at0031 |  | Description | DV_TEXT |
| at0002 |  | Stored specimen ID | DV_IDENTIFIER / DV_TEXT |
| at0018 |  | Storage started | DV_DATE_TIME |
| at0023 | Use | Reason for use | DV_TEXT |
| at0024 | Use | Date of use | DV_TEXT |
| at0029 | Use | Number used | DV_COUNT |
| at0027 | Use | Use comment | DV_TEXT |
| at0030 |  | Number remaining | DV_COUNT |
| at0012 |  | Use by date | DV_DATE_TIME |
| at0033 |  | Legally expiry date | DV_DATE_TIME |
| at0010 |  | Disposal reason | DV_TEXT |
| at0011 |  | Date of disposal | DV_DATE_TIME |
| at0020 |  | Specimen storage | DV_TEXT |
| at0016 |  | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0008 |  | Specimen details | openEHR-EHR-CLUSTER.specimen(-[a-zA-Z0-9_]+)*.v1 |
| at0026 | Use | Amount used | openEHR-EHR-CLUSTER.specimen_measurements.v1 |
| at0028 |  | Amount remaining | openEHR-EHR-CLUSTER.specimen_measurements.v1 |
| at0009 |  | Biobank location | openEHR-EHR-CLUSTER.organisation.v1 |
| at0017 |  | Additional details | any archetype |

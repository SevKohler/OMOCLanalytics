# openEHR-EHR-CLUSTER.laboratory_test_analyte.v1

**Concept:** Laboratory analyte result

**Category:** cluster

**Element leaves:** 12  |  **Cluster slot leaves:** 1  |  **Total leaves:** 13


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0027 | Analyte result sequence | DV_COUNT |
| at0024 | Analyte name | DV_TEXT |
| at0001 | Analyte result | any |
| at0004 | Reference range guidance | DV_TEXT |
| at0028 | Test method | any |
| at0031 | Analysis performed time | DV_DATE_TIME |
| at0025 | Validation time | DV_DATE_TIME |
| at0005 | Result status | DV_CODED_TEXT / DV_TEXT |
| at0006 | Result status time | DV_DATE_TIME |
| at0026 | Specimen | DV_IDENTIFIER / DV_URI / DV_TEXT |
| at0032 | Accredited | DV_BOOLEAN / DV_TEXT |
| at0003 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0014 | Analyte result detail | any archetype |

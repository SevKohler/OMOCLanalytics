# openEHR-EHR-EVALUATION.death_summary.v1

**Concept:** Death summary

**Category:** entry/evaluation

**Element leaves:** 16  |  **Cluster slot leaves:** 3  |  **Total leaves:** 19


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0092 | Date/time of death | DV_DATE_TIME / DV_INTERVAL |
| at0010 | Manner of death | DV_TEXT |
| at0093 | Manner description | DV_TEXT |
| at0021 | Place category | DV_TEXT |
| at0109 | Place of death | DV_TEXT |
| at0054 | Age at death | DV_DURATION |
| at0119 | Place of injury | DV_TEXT |
| at0120 | Date of injury | DV_DATE_TIME |
| at0121 | Activity at the time of injury | DV_TEXT |
| at0110 | Pregnancy context | DV_CODED_TEXT / DV_TEXT |
| at0106 | Days post partum | DV_DURATION |
| at0044 | Gestation at death | DV_DURATION |
| at0116 | Stillbirth context | DV_CODED_TEXT / DV_TEXT |
| at0105 | Comment | DV_TEXT |
| at0103 | Information source(s) | DV_TEXT |
| at0101 | Last updated | DV_DATE_TIME |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0104 | Date of death alternatives | openEHR-EHR-CLUSTER.dod_alternative.v0 |
| at0100 | Structured place of death | openEHR-EHR-CLUSTER.address(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 |
| at0042 | Additional details | any archetype |

# openEHR-EHR-ADMIN_ENTRY.episode_institution.v0

**Concept:** Admission

**Category:** entry/admin_entry

**Element leaves:** 19  |  **Cluster slot leaves:** 6  |  **Total leaves:** 25


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0014 | Admission ID | DV_IDENTIFIER |
| at0004 | Admission date | DV_DATE_TIME |
| at0008 | Reason for admission | DV_TEXT |
| at0009 | Admission category | DV_TEXT |
| at0007 | Source category | DV_TEXT |
| at0028 | Referral ID | DV_IDENTIFIER / DV_TEXT |
| at0016 | Medical record number | DV_IDENTIFIER / DV_TEXT |
| at0026 | Health insurance category | DV_TEXT |
| at0021 | Attending unit | DV_TEXT |
| at0019 | Location onset | DV_DATE_TIME |
| at0025 | Location category | DV_TEXT |
| at0022 | Ward | DV_TEXT |
| at0023 | Room | DV_TEXT |
| at0024 | Bed | DV_TEXT |
| at0020 | Location end | DV_DATE_TIME |
| at0002 | Discharge date | DV_DATE_TIME |
| at0006 | Outcome | DV_TEXT |
| at0003 | Destination category | DV_TEXT |
| at0010 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0013 | Source | openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.address(-[a-zA-Z0-9_]+)*.v1 |
| at0027 | Referring clinician | openEHR-EHR-CLUSTER.person(-[a-zA-Z0-9_]+)*.v1 |
| at0015 | Attending clinicians | openEHR-EHR-CLUSTER.person(-[a-zA-Z0-9_]+)*.v1 |
| at0017 | Location | openEHR-EHR-CLUSTER.address(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 |
| at0012 | Destination | openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.address(-[a-zA-Z0-9_]+)*.v1 |
| at0011 | Additional details | any archetype |

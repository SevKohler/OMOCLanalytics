# openEHR-EHR-ADMIN_ENTRY.translation_requirements.v1

**Concept:** Translation requirement

**Category:** entry/admin_entry

**Element leaves:** 2  |  **Cluster slot leaves:** 1  |  **Total leaves:** 3


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0003 | Translation required? | DV_BOOLEAN / DV_TEXT / DV_CODED_TEXT |
| at0004 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0002 | Administrative language | openEHR-EHR-CLUSTER.language(-[a-zA-Z0-9_]+)*.v1 |

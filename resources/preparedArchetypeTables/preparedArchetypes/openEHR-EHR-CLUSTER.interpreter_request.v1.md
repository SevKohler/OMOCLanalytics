# openEHR-EHR-CLUSTER.interpreter_request.v1

**Concept:** Interpreter request

**Category:** cluster

**Element leaves:** 4  |  **Cluster slot leaves:** 2  |  **Total leaves:** 6


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0009 |  | Kommunikasjonskanal | DV_CODED_TEXT / DV_TEXT |
| at0035 | Per språk | Kommentar | DV_TEXT |
| at0027 |  | Foretrukket kjønn | DV_CODED_TEXT |
| at0003 |  | Kommentar | DV_TEXT |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0031 | Per språk | Språk | openEHR-EHR-CLUSTER.language(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.language(-[a-zA-Z0-9_]+)*.v1 |
| at0004 |  | Foretrukket tolk | openEHR-EHR-CLUSTER.organisation(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.person_name(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.individual_professional(-[a-zA-Z0-9_]+)*.v0 |

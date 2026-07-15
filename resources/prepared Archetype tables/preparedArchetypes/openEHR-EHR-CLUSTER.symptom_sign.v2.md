# openEHR-EHR-CLUSTER.symptom_sign.v2

**Concept:** Symptom/Sign

**Category:** cluster

**Element leaves:** 28  |  **Cluster slot leaves:** 8  |  **Total leaves:** 36


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0001 | Symptom/Sign name | DV_TEXT |
| at0151 | Body site | DV_TEXT |
| at0002 | Description | DV_TEXT |
| at0175 | Episodicity | DV_CODED_TEXT |
| at0186 | Occurrence | DV_CODED_TEXT |
| at0152 | Episode onset | DV_DATE_TIME / DV_INTERVAL |
| at0164 | Onset timing | DV_TEXT / DV_DURATION / DV_INTERVAL |
| at0200 | Nadir | DV_DATE_TIME |
| at0028 | Episode duration | DV_DURATION / DV_INTERVAL / DV_TEXT |
| at0021 | Severity category | DV_CODED_TEXT / DV_TEXT |
| at0189 | Character | DV_TEXT |
| at0180 | Progression | DV_CODED_TEXT / DV_TEXT |
| at0003 | Pattern | DV_TEXT |
| at0019 | Factor | DV_TEXT |
| at0017 | Effect | DV_CODED_TEXT |
| at0056 | Description | DV_TEXT |
| at0170 | Factor | DV_TEXT |
| at0171 | Time interval | DV_DURATION |
| at0185 | Description | DV_TEXT |
| at0193 | Factor | DV_TEXT |
| at0195 | Time interval | DV_DURATION |
| at0196 | Description | DV_TEXT |
| at0155 | Impact | DV_TEXT |
| at0037 | Episode description | DV_TEXT |
| at0161 | Resolution date/time | DV_DATE_TIME |
| at0057 | Description of previous episodes | DV_TEXT |
| at0031 | Number of previous episodes | DV_COUNT |
| at0163 | Comment | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0147 | Structured body site | openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_circle(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_relative(-[a-zA-Z0-9_]+)*.v2 |
| at0198 | Severity rating | openEHR-EHR-CLUSTER.severity_rating_scale(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.severity_rating_scale(-[a-zA-Z0-9_]+)*.v1 |
| at0197 | Factor detail | openEHR-EHR-CLUSTER.health_event(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.symptom_sign(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.symptom_sign(-[a-zA-Z0-9_]+)*.v2 |
| at0154 | Factor detail | openEHR-EHR-CLUSTER.health_event(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.symptom_sign(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.symptom_sign(-[a-zA-Z0-9_]+)*.v2 |
| at0194 | Factor detail | openEHR-EHR-CLUSTER.health_event(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.symptom_sign(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.symptom_sign(-[a-zA-Z0-9_]+)*.v2 |
| at0153 | Specific details | any archetype |
| at0146 | Previous episodes | openEHR-EHR-CLUSTER.symptom_sign(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.symptom_sign(-[a-zA-Z0-9_]+)*.v2 |
| at0063 | Associated symptom/sign | openEHR-EHR-CLUSTER.symptom_sign(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.symptom_sign(-[a-zA-Z0-9_]+)*.v2 |

# openEHR-EHR-OBSERVATION.pulse_oximetry.v1

**Concept:** Pulse oximetry

**Category:** entry/observation

**Element leaves:** 9  |  **Cluster slot leaves:** 5  |  **Total leaves:** 14


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0006 | SpO₂ | DV_PROPORTION |
| at0044 | SpOC | DV_QUANTITY |
| at0045 | SpCO | DV_PROPORTION |
| at0046 | SpMet | DV_PROPORTION |
| at0058 | Interpretation | DV_TEXT |
| at0036 | Comment | DV_TEXT |
| at0016 | Confounding factors | DV_TEXT |
| at0009 | Sensor site | DV_TEXT |
| at0061 | Pre/post-ductal | DV_CODED_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0054 | Waveform | openEHR-EHR-CLUSTER.waveform(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.waveform(-[a-zA-Z0-9_]+)*.v1 |
| at0060 | Multimedia image | openEHR-EHR-CLUSTER.multimedia(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.multimedia(-[a-zA-Z0-9_]+)*.v1 |
| at0034 | Exertion | openEHR-EHR-CLUSTER.level_of_exertion(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.level_of_exertion(-[a-zA-Z0-9_]+)*.v1 |
| at0015 | Inspired oxygen | openEHR-EHR-CLUSTER.inspired_oxygen(-[a-zA-Z0-9_]+)*.v1 |
| at0018 | Oximetry device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |

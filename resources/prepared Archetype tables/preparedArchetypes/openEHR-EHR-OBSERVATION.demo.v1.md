# openEHR-EHR-OBSERVATION.demo.v1

**Concept:** Demonstration

**Category:** entry/observation

**Element leaves:** 21  |  **Cluster slot leaves:** 2  |  **Total leaves:** 23


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0032 |  | any |
| at0005 | Free Text or Coded | DV_TEXT |
| at0006 | Text That Uses Internal Codes | DV_CODED_TEXT |
| at0011 | Text That is Sourced From an External Terminology | DV_CODED_TEXT |
| at0012 | Quantity | DV_QUANTITY |
| at0023 | Interval of Quantity | DV_INTERVAL / DV_QUANTITY |
| at0013 | Count | DV_COUNT |
| at0022 | Interval of Integer | DV_INTERVAL / DV_COUNT |
| at0028 | Proportion | DV_PROPORTION |
| at0014 | Date/Time | DV_DATE_TIME |
| at0024 | Interval of Date | DV_INTERVAL / DV_DATE_TIME |
| at0021 | Duration | DV_DURATION |
| at0015 | Ordinal | DV_ORDINAL |
| at0016 | Boolean | DV_BOOLEAN |
| at0017 |  | any |
| at0025 | Choice | DV_QUANTITY / DV_CODED_TEXT |
| at0026 | Multimedia | DV_MULTIMEDIA |
| at0027 | URI - resource identifier | DV_URI |
| at0044 | Identifier | DV_IDENTIFIER |
| at0031 |  | any |
| at0037 |  | any |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0019 | Slot To Contain Other Cluster Archetypes | openEHR-EHR-CLUSTER.anatomical_location.v1 / openEHR-EHR-CLUSTER.device.v1 |
| at0020 | Slot To Contain Other Element Archetypes | openEHR-EHR-ELEMENT.ctg_codes.v1 |

# openEHR-EHR-OBSERVATION.demo.v1

**Concept:** Demonstration

**Category:** entry/observation

**Element leaves:** 21  |  **Cluster slot leaves:** 2  |  **Total leaves:** 23


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0032 |  |  | any |
| at0005 | Heading1 | Free Text or Coded | DV_TEXT |
| at0006 | Heading1 | Text That Uses Internal Codes | DV_CODED_TEXT |
| at0011 | Heading1 | Text That is Sourced From an External Terminology | DV_CODED_TEXT |
| at0012 | Heading1 | Quantity | DV_QUANTITY |
| at0023 | Heading1 | Interval of Quantity | DV_INTERVAL / DV_QUANTITY |
| at0013 | Heading1 | Count | DV_COUNT |
| at0022 | Heading1 | Interval of Integer | DV_INTERVAL / DV_COUNT |
| at0028 | Heading1 | Proportion | DV_PROPORTION |
| at0014 | Heading1 | Date/Time | DV_DATE_TIME |
| at0024 | Heading1 | Interval of Date | DV_INTERVAL / DV_DATE_TIME |
| at0021 | Heading1 | Duration | DV_DURATION |
| at0015 | Heading1 | Ordinal | DV_ORDINAL |
| at0016 | Heading1 | Boolean | DV_BOOLEAN |
| at0017 | Heading1 |  | any |
| at0025 | Heading1 | Choice | DV_QUANTITY / DV_CODED_TEXT |
| at0026 | Heading1 | Multimedia | DV_MULTIMEDIA |
| at0027 | Heading1 | URI - resource identifier | DV_URI |
| at0044 | Heading1 | Identifier | DV_IDENTIFIER |
| at0031 |  |  | any |
| at0037 |  |  | any |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0019 | Heading 2 | Slot To Contain Other Cluster Archetypes | openEHR-EHR-CLUSTER.anatomical_location.v1 / openEHR-EHR-CLUSTER.device.v1 |
| at0020 | Heading 2 | Slot To Contain Other Element Archetypes | openEHR-EHR-ELEMENT.ctg_codes.v1 |

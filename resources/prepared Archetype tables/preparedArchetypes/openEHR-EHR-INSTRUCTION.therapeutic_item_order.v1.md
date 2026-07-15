# openEHR-EHR-INSTRUCTION.therapeutic_item_order.v1

**Concept:** Therapeutic item order

**Category:** entry/instruction

**Element leaves:** 12  |  **Cluster slot leaves:** 3  |  **Total leaves:** 15


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0070 | Item name | DV_TEXT |
| at0092 | Body site | DV_TEXT |
| at0009 | Directions | DV_TEXT |
| at0107 | Monitoring instruction | DV_TEXT |
| at0018 | Clinical indication | DV_TEXT |
| at0148 | Therapeutic intent | DV_TEXT |
| at0012 | Start date/time | DV_DATE_TIME |
| at0013 | Stop date/time | DV_DATE_TIME |
| at0011 | Start criterion | DV_TEXT |
| at0016 | Stop criterion | DV_TEXT |
| at0167 | Comment | DV_TEXT |
| at0004 | Order identifier | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0143 | Item details | openEHR-EHR-CLUSTER.device.v1 |
| at0093 | Structured body site | openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_circle(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_relative(-[a-zA-Z0-9_]+)*.v2 |
| at0166 | Additional details | any archetype |

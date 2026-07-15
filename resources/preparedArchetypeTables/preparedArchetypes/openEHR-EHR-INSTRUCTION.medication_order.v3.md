# openEHR-EHR-INSTRUCTION.medication_order.v3

**Concept:** Medication order

**Category:** entry/instruction

**Element leaves:** 35  |  **Cluster slot leaves:** 9  |  **Total leaves:** 44


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0070 |  | Medication item | DV_TEXT |
| at0091 |  | Route | DV_TEXT |
| at0092 |  | Body site | DV_TEXT |
| at0094 |  | Administration method | DV_TEXT |
| at0009 |  | Overall directions description | DV_TEXT |
| at0047 |  | Parsable directions | DV_PARSABLE |
| at0173 |  | Specific directions description | DV_TEXT |
| at0174 |  | Dosage justification | DV_TEXT |
| at0064 | Medication safety | Exceptional safety override? | DV_BOOLEAN |
| at0171 | Medication safety > Safety override | Overriden safety advice | DV_TEXT |
| at0162 | Medication safety > Safety override | Override reason | DV_TEXT |
| at0130 | Medication safety > Maximum dose | Maximum amount | DV_QUANTITY |
| at0053 | Medication safety > Maximum dose | Allowed period | DV_DURATION |
| at0165 | Medication safety > Total daily effective dose | Purpose | DV_TEXT |
| at0151 | Medication safety > Total daily effective dose | Total daily amount | DV_QUANTITY |
| at0044 |  | Additional instruction | DV_TEXT |
| at0105 |  | Patient information | DV_TEXT |
| at0107 |  | Monitoring instruction | DV_TEXT |
| at0018 |  | Clinical indication | DV_TEXT |
| at0148 |  | Therapeutic intent | DV_TEXT |
| at0179 |  | Clinician guidance | DV_TEXT |
| at0012 | Order details | Order start date/time | DV_DATE_TIME |
| at0013 | Order details | Order stop date/time | DV_DATE_TIME |
| at0011 | Order details | Order start criterion | DV_TEXT |
| at0016 | Order details | Order stop criterion | DV_TEXT |
| at0060 | Order details | Administrations completed | DV_COUNT |
| at0050 | Order details | Duration of order completed | DV_DURATION |
| at0106 | Dispense directions | Dispense instruction | DV_TEXT |
| at0132 | Dispense directions | Substitution direction | DV_CODED_TEXT |
| at0154 | Dispense directions | Non-substitution reason | DV_TEXT |
| at0139 | Dispense directions | Priority | DV_TEXT |
| at0155 | Dispense directions | Dispensing start date | DV_DATE_TIME |
| at0161 | Dispense directions | Dispensing expiry date | DV_DATE_TIME |
| at0167 |  | Comment | DV_TEXT |
| at0004 |  | Order identifier | DV_IDENTIFIER |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0143 |  | Medication details | openEHR-EHR-CLUSTER.medication(-[a-zA-Z0-9_]+)*.v2 |
| at0093 |  | Structured body site | openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_circle(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_relative(-[a-zA-Z0-9_]+)*.v2 |
| at0095 |  | Administration device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0177 |  | Structured dose and timing directions | openEHR-EHR-CLUSTER.therapeutic_direction(-[a-zA-Z0-9_]+)*.v1 |
| at0112 | Order details | Order summary | openEHR-EHR-CLUSTER.medication_order_summary(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.medication_order_summary(-[a-zA-Z0-9_]+)*.v1 |
| at0069 |  | Authorisation directions | openEHR-EHR-CLUSTER.medication_authorisation(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.medication_authorisation(-[a-zA-Z0-9_]+)*.v1 |
| at0065 | Dispense directions | Dispense amount | openEHR-EHR-CLUSTER.medication_supply_amount(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.medication_supply_amount(-[a-zA-Z0-9_]+)*.v1 |
| at0170 | Dispense directions | Dispense details | any archetype |
| at0166 |  | Additional details | any archetype |

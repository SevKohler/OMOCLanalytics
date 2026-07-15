# openEHR-EHR-ACTION.medication.v1

**Concept:** Medication management

**Category:** entry/action

**Element leaves:** 16  |  **Cluster slot leaves:** 5  |  **Total leaves:** 21


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0020 |  | Medication item | DV_TEXT |
| at0156 |  | Clinical indication | DV_TEXT |
| at0132 |  | Substitution | DV_CODED_TEXT |
| at0133 |  | Substitution reason | DV_TEXT |
| at0043 |  | Original scheduled date/time | DV_DATE_TIME |
| at0154 |  | Restart date/time | DV_DATE_TIME |
| at0155 |  | Restart criterion | DV_TEXT |
| at0021 |  | Reason | DV_TEXT |
| at0147 | Administration details | Route | DV_TEXT |
| at0141 | Administration details | Body site | DV_TEXT |
| at0143 | Administration details | Administration method | DV_TEXT |
| at0033 |  | Patient guidance | DV_TEXT |
| at0149 |  | Double-checked? | DV_BOOLEAN |
| at0025 |  | Sequence number | DV_COUNT |
| at0024 |  | Comment | DV_TEXT |
| at0103 |  | Order ID | DV_IDENTIFIER / DV_TEXT |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0104 |  | Medication details | openEHR-EHR-CLUSTER.medication(-[a-zA-Z0-9_]+)*.v2 |
| at0131 |  | Amount | openEHR-EHR-CLUSTER.medication_supply_amount(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.medication_supply_amount(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.dosage(-[a-zA-Z0-9_]+)*.v2 |
| at0142 | Administration details | Structured body site | openEHR-EHR-CLUSTER.anatomical_location(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_circle(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.anatomical_location_relative(-[a-zA-Z0-9_]+)*.v2 |
| at0144 | Administration details | Administration device | openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0053 |  | Additional details | openEHR-EHR-CLUSTER.medication_authorisation(-[a-zA-Z0-9_]+)*.v0 / openEHR-EHR-CLUSTER.medication_authorisation(-[a-zA-Z0-9_]+)*.v1 |

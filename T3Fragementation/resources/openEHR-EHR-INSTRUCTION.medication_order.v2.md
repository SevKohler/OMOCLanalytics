# openEHR-EHR-INSTRUCTION.medication_order.v2

**Concept:** Medication order

**Primary OMOP table:** DrugExposure  |  **Leaves:** 45  |  **Mapped to primary:** 4  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 41

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0070 | element | Medication item | `concept_id` @ DrugExposure |
| at0091 | element | Route | `route_concept_id` @ DrugExposure |
| at0012 | element | Order details > Order start date/time | `drug_exposure_start_date` @ DrugExposure |
| at0013 | element | Order details > Order stop date/time | `drug_exposure_end_date` @ DrugExposure |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0092 | element | Body site |
| at0094 | element | Administration method |
| at0009 | element | Overall directions description |
| at0047 | element | Parsable directions |
| at0173 | element | Specific directions description |
| at0174 | element | Dosage justification |
| at0064 | element | Medication safety > Exceptional safety override? |
| at0171 | element | Medication safety > Safety override > Overriden safety advice |
| at0162 | element | Medication safety > Safety override > Override reason |
| at0130 | element | Medication safety > Maximum dose > Maximum amount |
| at0146 | element | Medication safety > Maximum dose > Maximum amount unit |
| at0053 | element | Medication safety > Maximum dose > Allowed period |
| at0165 | element | Medication safety > Total daily effective dose > Purpose |
| at0151 | element | Medication safety > Total daily effective dose > Total daily amount |
| at0152 | element | Medication safety > Total daily effective dose > Total daily amount unit |
| at0044 | element | Additional instruction |
| at0105 | element | Patient information |
| at0107 | element | Monitoring instruction |
| at0018 | element | Clinical indication |
| at0148 | element | Therapeutic intent |
| at0011 | element | Order details > Order start criterion |
| at0016 | element | Order details > Order stop criterion |
| at0060 | element | Order details > Administrations completed |
| at0050 | element | Order details > Duration of order completed |
| at0106 | element | Dispense directions > Dispense instruction |
| at0132 | element | Dispense directions > Substitution direction |
| at0154 | element | Dispense directions > Non-substitution reason |
| at0139 | element | Dispense directions > Priority |
| at0155 | element | Dispense directions > Dispensing start date |
| at0161 | element | Dispense directions > Dispensing expiry date |
| at0167 | element | Comment |
| at0004 | element | Order identifier |
| at0143 | slot | Preparation details |
| at0093 | slot | Structured body site |
| at0095 | slot | Administration device |
| at0177 | slot | Structured dose and timing directions |
| at0112 | slot | Order details > Order summary |
| at0069 | slot | Authorisation directions |
| at0065 | slot | Dispense directions > Dispense amount |
| at0170 | slot | Dispense directions > Dispense details |
| at0166 | slot | Additional details |

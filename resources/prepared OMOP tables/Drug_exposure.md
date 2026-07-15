# Drug exposure

Target table OMOP CDM v5.4 `DRUG_EXPOSURE`. The prepared table lists the content concepts we count archetype leafs against. See the README for how it is derived.

## CDM fields (23)

| Field | Required | Type | Key | Description |
|---|---|---|---|---|
| `drug_exposure_id` | Yes | integer | PK | The unique key given to records of drug dispensings or administrations for a person. Refer to the ETL for how duplicate drugs during the same visit were handled. |
| `person_id` | Yes | integer | FK PERSON | The PERSON_ID of the PERSON for whom the drug dispensing or administration is recorded. This may be a system generated code. |
| `drug_concept_id` | Yes | integer | FK CONCEPT | The DRUG_CONCEPT_ID field is recommended for primary use in analyses, and must be used for network studies. This is the standard concept mapped from the source concept id which represents a drug product or molecule otherwise introduced to the body. The drug concepts can have a varying degree of information about drug strength and dose. This information is relevant in the context of quantity and administration information in the subsequent fields plus strength information from the DRUG_STRENGTH table, provided as part of the standard vocabulary download. |
| `drug_exposure_start_date` | Yes | date |  | Use this date to determine the start date of the drug record. |
| `drug_exposure_start_datetime` | No | datetime |  |  |
| `drug_exposure_end_date` | Yes | date |  | The DRUG_EXPOSURE_END_DATE denotes the day the drug exposure ended for the patient. |
| `drug_exposure_end_datetime` | No | datetime |  |  |
| `verbatim_end_date` | No | date |  | This is the end date of the drug exposure as it appears in the source data, if it is given |
| `drug_type_concept_id` | Yes | integer | FK CONCEPT | You can use the TYPE_CONCEPT_ID to delineate between prescriptions written vs. prescriptions dispensed vs. medication history vs. patient-reported exposure, etc. |
| `stop_reason` | No | varchar(20) |  | The reason a person stopped a medication as it is represented in the source. Reasons include regimen completed, changed, removed, etc. This field will be retired in v6.0. |
| `refills` | No | integer |  | This is only filled in when the record is coming from a prescription written this field is meant to represent intended refills at time of the prescription. |
| `quantity` | No | float |  |  |
| `days_supply` | No | integer |  |  |
| `sig` | No | varchar(MAX) |  | This is the verbatim instruction for the drug as written by the provider. |
| `route_concept_id` | No | integer | FK CONCEPT |  |
| `lot_number` | No | varchar(50) |  |  |
| `provider_id` | No | integer | FK PROVIDER | The Provider associated with drug record, e.g. the provider who wrote the prescription or the provider who administered the drug. |
| `visit_occurrence_id` | No | integer | FK VISIT_OCCURRENCE | The Visit during which the drug was prescribed, administered or dispensed. |
| `visit_detail_id` | No | integer | FK VISIT_DETAIL | The VISIT_DETAIL record during which the drug exposure occurred. For example, if the person was in the ICU at the time of the drug administration the VISIT_OCCURRENCE record would reflect the overall hospital stay and the VISIT_DETAIL record would reflect the ICU stay during the hospital visit. |
| `drug_source_value` | No | varchar(50) |  | This field houses the verbatim value from the source data representing the drug exposure that occurred. For example, this could be an NDC or Gemscript code. |
| `drug_source_concept_id` | No | integer | FK CONCEPT | This is the concept representing the drug source value and may not necessarily be standard. This field is discouraged from use in analysis because it is not required to contain Standard Concepts that are used across the OHDSI community, and should only be used when Standard Concepts do not adequately represent the source detail for the Drug necessary for a given analytic use case. Consider using DRUG_CONCEPT_ID instead to enable standardized analytics that can be consistent across the network. |
| `route_source_value` | No | varchar(50) |  | This field houses the verbatim value from the source data representing the drug route. |
| `dose_unit_source_value` | No | varchar(50) |  | This field houses the verbatim value from the source data representing the dose unit of the drug given. |

## Prepared table

11 content concepts kept, 6 removed.

| Concept | OMOP fields | Kept | Reason |
|---|---|---|---|
| Drug concept | `drug_concept_id`, `drug_source_value`, `drug_source_concept_id` | yes | |
| Drug exposure start date/time | `drug_exposure_start_date`, `drug_exposure_start_datetime` | yes | |
| Drug exposure end date/time | `drug_exposure_end_date`, `drug_exposure_end_datetime` | yes | |
| Drug type / provenance | `drug_type_concept_id` | yes | |
| Stop reason | `stop_reason` | yes | |
| Refills | `refills` | yes | |
| Quantity (DV_QUANTITY) | `quantity` | yes | |
| Days supply | `days_supply` | yes | |
| Sig | `sig` | yes | |
| Route | `route_concept_id`, `route_source_value` | yes | |
| Lot number | `lot_number` | yes | |
| Record identifier | `drug_exposure_id` | no | openEHR RM identifier. |
| Person | `person_id` | no | link to the subject of care. |
| Verbatim end date/time | `verbatim_end_date` | no | the same as the end date, only the end date as written in the source, so not a separate leaf. |
| Provider | `provider_id` | no | link to the recording provider. |
| Visit | `visit_occurrence_id`, `visit_detail_id` | no | link to the encounter. |
| Dose unit | `dose_unit_source_value` | no | deprecated OMOP column with no standard concept. |

## Mapped archetypes

Archetypes whose OMOCL mapping targets this table.

### Single target table (7)

| Archetype | Mapping file |
|---|---|
| `openEHR-EHR-ACTION.medication.v1` | `medical_data/action/Medication_v1.yml` |
| `openEHR-EHR-CLUSTER.dosage.v1` | `medical_data/cluster/Dosage_v1.yml` |
| `openEHR-EHR-CLUSTER.dosage.v2` | `medical_data/cluster/Dosage_v2.yml` |
| `openEHR-EHR-EVALUATION.medication_summary.v1` | `medical_data/evaluation/Medication_summary_v1.yml` |
| `openEHR-EHR-INSTRUCTION.medication_order.v2` | `medical_data/instruction/Medication_order_v2.yml` |
| `openEHR-EHR-INSTRUCTION.medication_order.v3` | `medical_data/instruction/Medication_order_v3.yml` |
| `openEHR-EHR-OBSERVATION.medication_statement.v0` | `medical_data/instruction/Medication_statement_v0.yml` |

### Several target tables (1)

| Archetype | Also maps to | Mapping file |
|---|---|---|
| `openEHR-EHR-OBSERVATION.medication_screening.v1` | `Observation` | `medical_data/observation/Medication_screening_v1.yml` |

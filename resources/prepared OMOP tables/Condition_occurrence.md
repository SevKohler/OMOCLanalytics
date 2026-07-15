# Condition occurrence

Target table OMOP CDM v5.4 `CONDITION_OCCURRENCE`. The prepared table lists the content concepts we count archetype leafs against. See the README for how it is derived.

## CDM fields (16)

| Field | Required | Type | Key | Description |
|---|---|---|---|---|
| `condition_occurrence_id` | Yes | integer | PK | The unique key given to a condition record for a person. Refer to the ETL for how duplicate conditions during the same visit were handled. |
| `person_id` | Yes | integer | FK PERSON | The PERSON_ID of the PERSON for whom the condition is recorded. |
| `condition_concept_id` | Yes | integer | FK CONCEPT | The CONDITION_CONCEPT_ID field is recommended for primary use in analyses, and must be used for network studies. This is the standard concept mapped from the source value which represents a condition |
| `condition_start_date` | Yes | date |  | Use this date to determine the start date of the condition |
| `condition_start_datetime` | No | datetime |  |  |
| `condition_end_date` | No | date |  | Use this date to determine the end date of the condition |
| `condition_end_datetime` | No | datetime |  |  |
| `condition_type_concept_id` | Yes | integer | FK CONCEPT | This field can be used to determine the provenance of the Condition record, as in whether the condition was from an EHR system, insurance claim, registry, or other sources. |
| `condition_status_concept_id` | No | integer | FK CONCEPT | This concept represents the point during the visit the diagnosis was given (admitting diagnosis, final diagnosis), whether the diagnosis was determined due to laboratory findings, if the diagnosis was exclusionary, or if it was a preliminary diagnosis, among others. |
| `stop_reason` | No | varchar(20) |  | The Stop Reason indicates why a Condition is no longer valid with respect to the purpose within the source data. Note that a Stop Reason does not necessarily imply that the condition is no longer occurring. |
| `provider_id` | No | integer | FK PROVIDER | The provider associated with condition record, e.g. the provider who made the diagnosis or the provider who recorded the symptom. |
| `visit_occurrence_id` | No | integer | FK VISIT_OCCURRENCE | The visit during which the condition occurred. |
| `visit_detail_id` | No | integer | FK VISIT_DETAIL | The VISIT_DETAIL record during which the condition occurred. For example, if the person was in the ICU at the time of the diagnosis the VISIT_OCCURRENCE record would reflect the overall hospital stay and the VISIT_DETAIL record would reflect the ICU stay during the hospital visit. |
| `condition_source_value` | No | varchar(50) |  | This field houses the verbatim value from the source data representing the condition that occurred. For example, this could be an ICD10 or Read code. |
| `condition_source_concept_id` | No | integer | FK CONCEPT | This is the concept representing the condition source value and may not necessarily be standard. This field is discouraged from use in analysis because it is not required to contain Standard Concepts that are used across the OHDSI community, and should only be used when Standard Concepts do not adequately represent the source detail for the Condition necessary for a given analytic use case. Consider using CONDITION_CONCEPT_ID instead to enable standardized analytics that can be consistent across the network. |
| `condition_status_source_value` | No | varchar(50) |  | This field houses the verbatim value from the source data representing the condition status. |

## Prepared table

6 content concepts kept, 4 removed.

| Concept | OMOP fields | Kept | Reason |
|---|---|---|---|
| Condition concept | `condition_concept_id`, `condition_source_value`, `condition_source_concept_id` | yes | |
| Condition start date/time | `condition_start_date`, `condition_start_datetime` | yes | |
| Condition end date/time | `condition_end_date`, `condition_end_datetime` | yes | |
| Condition type / provenance | `condition_type_concept_id` | yes | |
| Condition status | `condition_status_concept_id`, `condition_status_source_value` | yes | |
| Stop reason | `stop_reason` | yes | |
| Record identifier | `condition_occurrence_id` | no | openEHR RM identifier. |
| Person | `person_id` | no | link to the subject of care. |
| Provider | `provider_id` | no | link to the recording provider. |
| Visit | `visit_occurrence_id`, `visit_detail_id` | no | link to the encounter. |

## Mapped archetypes

Archetypes whose OMOCL mapping targets this table.

### Single target table (4)

| Archetype | Mapping file |
|---|---|
| `openEHR-EHR-CLUSTER.symptom_sign.v2` | `medical_data/cluster/Symptom_sign_v2.yml` |
| `openEHR-EHR-EVALUATION.differential_diagnoses.v1` | `medical_data/evaluation/Differential_diagnoses_v1.yml` |
| `openEHR-EHR-EVALUATION.problem_diagnosis.v1` | `medical_data/evaluation/Problem_diagnosis_v1.yml` |
| `openEHR-EHR-OBSERVATION.imaging_exam_result.v1` | `medical_data/observation/Imaging_exam_result_v1.yml` |

### Several target tables (0)

None.

# Procedure occurrence

Target table OMOP CDM v5.4 `PROCEDURE_OCCURRENCE`. The prepared table lists the content concepts we count archetype leafs against. See the README for how it is derived.

## CDM fields (16)

| Field | Required | Type | Key | Description |
|---|---|---|---|---|
| `procedure_occurrence_id` | Yes | integer | PK | The unique key given to a procedure record for a person. Refer to the ETL for how duplicate procedures during the same visit were handled. |
| `person_id` | Yes | integer | FK PERSON | The PERSON_ID of the PERSON for whom the procedure is recorded. This may be a system generated code. |
| `procedure_concept_id` | Yes | integer | FK CONCEPT | The PROCEDURE_CONCEPT_ID field is recommended for primary use in analyses, and must be used for network studies. This is the standard concept mapped from the source value which represents a procedure |
| `procedure_date` | Yes | date |  | Use this date to determine the date the procedure started. |
| `procedure_datetime` | No | datetime |  |  |
| `procedure_end_date` | No | date |  | Use this field to house the date that the procedure ended. |
| `procedure_end_datetime` | No | datetime |  | Use this field to house the datetime that the procedure ended. |
| `procedure_type_concept_id` | Yes | integer | FK CONCEPT | This field can be used to determine the provenance of the Procedure record, as in whether the procedure was from an EHR system, insurance claim, registry, or other sources. |
| `modifier_concept_id` | No | integer | FK CONCEPT | The modifiers are intended to give additional information about the procedure but as of now the vocabulary is under review. |
| `quantity` | No | integer |  | If the quantity value is omitted, a single procedure is assumed. |
| `provider_id` | No | integer | FK PROVIDER | The provider associated with the procedure record, e.g. the provider who performed the Procedure. |
| `visit_occurrence_id` | No | integer | FK VISIT_OCCURRENCE | The visit during which the procedure occurred. |
| `visit_detail_id` | No | integer | FK VISIT_DETAIL | The VISIT_DETAIL record during which the Procedure occurred. For example, if the Person was in the ICU at the time of the Procedure the VISIT_OCCURRENCE record would reflect the overall hospital stay and the VISIT_DETAIL record would reflect the ICU stay during the hospital visit. |
| `procedure_source_value` | No | varchar(50) |  | This field houses the verbatim value from the source data representing the procedure that occurred. For example, this could be an CPT4 or OPCS4 code. |
| `procedure_source_concept_id` | No | integer | FK CONCEPT | This is the concept representing the procedure source value and may not necessarily be standard. This field is discouraged from use in analysis because it is not required to contain Standard Concepts that are used across the OHDSI community, and should only be used when Standard Concepts do not adequately represent the source detail for the Procedure necessary for a given analytic use case. Consider using PROCEDURE_CONCEPT_ID instead to enable standardized analytics that can be consistent across the network. |
| `modifier_source_value` | No | varchar(50) |  |  |

## Prepared table

6 content concepts kept, 4 removed.

| Concept | OMOP fields | Kept | Reason |
|---|---|---|---|
| Procedure concept | `procedure_concept_id`, `procedure_source_value`, `procedure_source_concept_id` | yes | |
| Procedure date/time | `procedure_date`, `procedure_datetime` | yes | |
| Procedure end date/time | `procedure_end_date`, `procedure_end_datetime` | yes | |
| Procedure type / provenance | `procedure_type_concept_id` | yes | |
| Modifier | `modifier_concept_id`, `modifier_source_value` | yes | |
| Quantity (DV_QUANTITY) | `quantity` | yes | |
| Record identifier | `procedure_occurrence_id` | no | openEHR RM identifier. |
| Person | `person_id` | no | link to the subject of care. |
| Provider | `provider_id` | no | link to the recording provider. |
| Visit | `visit_occurrence_id`, `visit_detail_id` | no | link to the encounter. |

## Mapped archetypes

Archetypes whose OMOCL mapping targets this table.

### Single target table (4)

| Archetype | Mapping file |
|---|---|
| `openEHR-EHR-ACTION.procedure.v1` | `medical_data/action/Procedure_v1.yml` |
| `openEHR-EHR-EVALUATION.art_cycle_summary.v1` | `medical_data/evaluation/Art_cycle_summary_v1.yml` |
| `openEHR-EHR-INSTRUCTION.therapeutic_item_order.v1` | `medical_data/instruction/Therapeutic_item_order_v1.yml` |
| `openEHR-EHR-OBSERVATION.procedure_screening.v1` | `medical_data/observation/Procedure_screening_v1.yml` |

### Several target tables (1)

| Archetype | Also maps to | Mapping file |
|---|---|---|
| `openEHR-EHR-CLUSTER.imaging_exam-fallopian_tube.v1` | `Observation` | `medical_data/cluster/Imaging_exam_fallopian_tube.yml` |

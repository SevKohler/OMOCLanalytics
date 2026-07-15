# Observation

Target table OMOP CDM v5.4 `OBSERVATION`. The prepared table lists the content concepts we count archetype leafs against. See the README for how it is derived.

## CDM fields (21)

| Field | Required | Type | Key | Description |
|---|---|---|---|---|
| `observation_id` | Yes | integer | PK | The unique key given to an Observation record for a Person. Refer to the ETL for how duplicate Observations during the same Visit were handled. |
| `person_id` | Yes | integer | FK PERSON | The PERSON_ID of the Person for whom the Observation is recorded. This may be a system generated code. |
| `observation_concept_id` | Yes | integer | FK CONCEPT | The OBSERVATION_CONCEPT_ID field is recommended for primary use in analyses, and must be used for network studies. |
| `observation_date` | Yes | date |  | The date of the Observation. Depending on what the Observation represents this could be the date of a lab test, the date of a survey, or the date a patient's family history was taken. |
| `observation_datetime` | No | datetime |  |  |
| `observation_type_concept_id` | Yes | integer | FK CONCEPT | This field can be used to determine the provenance of the Observation record, as in whether the measurement was from an EHR system, insurance claim, registry, or other sources. |
| `value_as_number` | No | float |  | This is the numerical value of the Result of the Observation, if applicable and available. It is not expected that all Observations will have numeric results, rather, this field is here to house values should they exist. |
| `value_as_string` | No | varchar(60) |  | This is the categorical value of the Result of the Observation, if applicable and available. |
| `value_as_concept_id` | No | Integer | FK CONCEPT | It is possible that some records destined for the Observation table have two clinical ideas represented in one source code. This is common with ICD10 codes that describe a family history of some Condition, for example. In OMOP the Vocabulary breaks these two clinical ideas into two codes; one becomes the OBSERVATION_CONCEPT_ID and the other becomes the VALUE_AS_CONCEPT_ID. It is important when using the Observation table to keep this possibility in mind and to examine the VALUE_AS_CONCEPT_ID field for relevant information. |
| `qualifier_concept_id` | No | integer | FK CONCEPT | This field contains all attributes specifying the clinical fact further, such as as degrees, severities, drug-drug interaction alerts etc. |
| `unit_concept_id` | No | integer | FK CONCEPT | There is currently no recommended unit for individual observation concepts. UNIT_SOURCE_VALUES should be mapped to a Standard Concept in the Unit domain that best represents the unit as given in the source data. |
| `provider_id` | No | integer | FK PROVIDER | The provider associated with the observation record, e.g. the provider who ordered the test or the provider who recorded the result. |
| `visit_occurrence_id` | No | integer | FK VISIT_OCCURRENCE | The visit during which the Observation occurred. |
| `visit_detail_id` | No | integer | FK VISIT_DETAIL | The VISIT_DETAIL record during which the Observation occurred. For example, if the Person was in the ICU at the time the VISIT_OCCURRENCE record would reflect the overall hospital stay and the VISIT_DETAIL record would reflect the ICU stay during the hospital visit. |
| `observation_source_value` | No | varchar(50) |  | This field houses the verbatim value from the source data representing the Observation that occurred. For example, this could be an ICD10 or Read code. |
| `observation_source_concept_id` | No | integer | FK CONCEPT | This is the concept representing the OBSERVATION_SOURCE_VALUE and may not necessarily be standard. This field is discouraged from use in analysis because it is not required to contain Standard Concepts that are used across the OHDSI community, and should only be used when Standard Concepts do not adequately represent the source detail for the Observation necessary for a given analytic use case. Consider using OBSERVATION_CONCEPT_ID instead to enable standardized analytics that can be consistent across the network. |
| `unit_source_value` | No | varchar(50) |  | This field houses the verbatim value from the source data representing the unit of the Observation that occurred. |
| `qualifier_source_value` | No | varchar(50) |  | This field houses the verbatim value from the source data representing the qualifier of the Observation that occurred. |
| `value_source_value` | No | varchar(50) |  | This field houses the verbatim result value of the Observation from the source data. Do not get confused with the Observation_source_value which captures source value of the observation mapped to observation_concept_id. This field is the observation result value from the source. |
| `observation_event_id` | No | integer |  | If the Observation record is related to another record in the database, this field is the primary key of the linked record. |
| `obs_event_field_concept_id` | No | integer | FK CONCEPT | If the Observation record is related to another record in the database, this field is the CONCEPT_ID that identifies which table the primary key of the linked record came from. |

## Prepared table

5 content concepts kept, 6 removed.

| Concept | OMOP fields | Kept | Reason |
|---|---|---|---|
| Observation concept | `observation_concept_id`, `observation_source_value`, `observation_source_concept_id` | yes | |
| Observation date/time | `observation_date`, `observation_datetime` | yes | |
| Observation type / provenance | `observation_type_concept_id` | yes | |
| Value (DV_QUANTITY / DV_CODED_TEXT / DV_TEXT / DV_COUNT / DV_ORDINAL / DV_BOOLEAN / DV_DATE_TIME) | `value_as_number`, `value_as_string`, `value_as_concept_id`, `value_source_value` | yes | |
| Qualifier | `qualifier_concept_id`, `qualifier_source_value` | yes | |
| Record identifier | `observation_id` | no | openEHR RM identifier. |
| Person | `person_id` | no | link to the subject of care. |
| Unit | `unit_concept_id`, `unit_source_value` | no | RM attribute of the value (`DV_QUANTITY.units`). In the OMOCL Observation mappings the unit comes from the value or a constant code. The one exception is `adverse_reaction_risk_v1`, where it points to its own node and so does count as a leaf there. |
| Provider | `provider_id` | no | link to the recording provider. |
| Visit | `visit_occurrence_id`, `visit_detail_id` | no | link to the encounter. |
| Event link | `observation_event_id`, `obs_event_field_concept_id` | no | link to another record. |

## Mapped archetypes

Archetypes whose OMOCL mapping targets this table.

### Single target table (98)

| Archetype | Mapping file |
|---|---|
| `openEHR-EHR-ACTION.health_education.v1` | `medical_data/action/Health_education_v1.yml` |
| `openEHR-EHR-ACTION.service.v1` | `medical_data/action/Service_v1.yml` |
| `openEHR-EHR-ADMIN_ENTRY.translation_requirements.v1` | `medical_data/admin_entry/Translation_requirements_v1.yml` |
| `openEHR-EHR-CLUSTER.Oocyte_specimen.v1` | `medical_data/cluster/Oocyte_specimen.yml` |
| `openEHR-EHR-CLUSTER.address.v1` | `medical_data/cluster/Address_v1.yml` |
| `openEHR-EHR-CLUSTER.adverse_reaction_event.v1` | `medical_data/cluster/Adverse_reaction_event_v1.yml` |
| `openEHR-EHR-CLUSTER.anatomical_location.v1` | `medical_data/cluster/Anatomical_location_v1.yml` |
| `openEHR-EHR-CLUSTER.anatomical_location_circle.v1` | `medical_data/cluster/Anatomical_location_circle_v1.yml` |
| `openEHR-EHR-CLUSTER.anatomical_location_relative.v2` | `medical_data/cluster/Anatomical_location_relative_v2.yml` |
| `openEHR-EHR-CLUSTER.clinical_evidence.v1` | `medical_data/cluster/Clinical_evidence_v1.yml` |
| `openEHR-EHR-CLUSTER.exam.v2` | `medical_data/cluster/Exam_v2.yml` |
| `openEHR-EHR-CLUSTER.family_prevalence.v1` | `medical_data/cluster/Family_prevalence_v1.yml` |
| `openEHR-EHR-CLUSTER.genomic_conversion_variant.v1` | `medical_data/cluster/Genomic_conversion_variant_v1.yml` |
| `openEHR-EHR-CLUSTER.genomic_copy_number_variant.v1` | `medical_data/cluster/Genomic_copy_number_variant_v1.yml` |
| `openEHR-EHR-CLUSTER.genomic_deletion_insertion_variant.v1` | `medical_data/cluster/Genomic_deletion_insertion_variant_v1.yml` |
| `openEHR-EHR-CLUSTER.genomic_deletion_variant.v1` | `medical_data/cluster/Genomic_deletion_variant_v1.yml` |
| `openEHR-EHR-CLUSTER.genomic_duplication_variant.v1` | `medical_data/cluster/Genomic_duplication_variant_v1.yml` |
| `openEHR-EHR-CLUSTER.genomic_insertion_variant.v1` | `medical_data/cluster/Genomic_insertion_variant_v1.yml` |
| `openEHR-EHR-CLUSTER.genomic_inversion_variant.v1` | `medical_data/cluster/Genomic_inversion_variant_v1.yml` |
| `openEHR-EHR-CLUSTER.genomic_repeated_sequence_variant.v1` | `medical_data/cluster/Genomic_repeated_sequence_variant_v1.yml` |
| `openEHR-EHR-CLUSTER.genomic_substitution_variant.v1` | `medical_data/cluster/Genomic_substitution_variant_v1.yml` |
| `openEHR-EHR-CLUSTER.genomic_variant_result.v1` | `medical_data/cluster/Genomic_variant_result_v1.yml` |
| `openEHR-EHR-CLUSTER.gist_modified_nih.v1` | `medical_data/cluster/Gist_modified_nih.yml` |
| `openEHR-EHR-CLUSTER.housing_record.v1` | `medical_data/cluster/Housing_record_v1.yml` |
| `openEHR-EHR-CLUSTER.imaging_exam-cervix.v1` | `medical_data/cluster/Imaging_exam_cervix.yml` |
| `openEHR-EHR-CLUSTER.imaging_exam-foetus.v1` | `medical_data/cluster/Imaging_exam_foetus.yml` |
| `openEHR-EHR-CLUSTER.imaging_exam-gestational_sac.v1` | `medical_data/cluster/Imaging_exam_gestational_sac.yml` |
| `openEHR-EHR-CLUSTER.imaging_exam-ovary.v1` | `medical_data/cluster/Imaging_exam_ovary.yml` |
| `openEHR-EHR-CLUSTER.imaging_exam-rectouterine_pouch.v1` | `medical_data/cluster/Imaging_exam_rectouterine_pouch.yml` |
| `openEHR-EHR-CLUSTER.imaging_exam.v1` | `medical_data/cluster/Imaging_exam.yml` |
| `openEHR-EHR-CLUSTER.information_resource.v1` | `medical_data/cluster/Information_resource_v1.yml` |
| `openEHR-EHR-CLUSTER.interpreter_request.v1` | `medical_data/cluster/Interpreter_request_v1.yml` |
| `openEHR-EHR-CLUSTER.item_transport.v1` | `medical_data/cluster/Item_transport_v1.yml` |
| `openEHR-EHR-CLUSTER.knowledge_base_reference.v1` | `medical_data/cluster/Knowledge_base_reference_v1.yml` |
| `openEHR-EHR-CLUSTER.language.v1` | `medical_data/cluster/Language_v1.yml` |
| `openEHR-EHR-CLUSTER.media_file.v1` | `medical_data/cluster/Media_file.yml` |
| `openEHR-EHR-CLUSTER.occupation_record.v1` | `medical_data/cluster/Occupation_record_v1.yml` |
| `openEHR-EHR-CLUSTER.organisation.v1` | `medical_data/cluster/Organisation_v1.yml` |
| `openEHR-EHR-CLUSTER.person.v1` | `medical_data/cluster/Person_v1.yml` |
| `openEHR-EHR-CLUSTER.problem_qualifier.v2` | `medical_data/cluster/Problem_qualifier_v2.yml` |
| `openEHR-EHR-CLUSTER.range_of_motion.v1` | `medical_data/cluster/Range_of_motion_v1.yml` |
| `openEHR-EHR-CLUSTER.religion.v1` | `medical_data/cluster/Religion_v1.yml` |
| `openEHR-EHR-CLUSTER.service_direction.v1` | `medical_data/cluster/Service_direction_v1.yml` |
| `openEHR-EHR-CLUSTER.structured_name.v1` | `medical_data/cluster/Structured_name_v1.yml` |
| `openEHR-EHR-CLUSTER.therapeutic_direction.v1` | `medical_data/cluster/Therapeutic_direction_v1.yml` |
| `openEHR-EHR-CLUSTER.tnm-pathological.v1` | `medical_data/cluster/Tnm-pathological_v1.yml` |
| `openEHR-EHR-CLUSTER.tnm.v1` | `medical_data/cluster/Tnm_v1.yml` |
| `openEHR-EHR-CLUSTER.who_grade_bone_sarcoma.v1` | `medical_data/cluster/Who_grade_bone_sarcoma.yml` |
| `openEHR-EHR-EVALUATION.advance_care_directive.v2` | `medical_data/evaluation/Advance_care_directive_v2.yml` |
| `openEHR-EHR-EVALUATION.advance_intervention_decisions.v1` | `medical_data/evaluation/Advance_intervention_decisions_v1.yml` |
| `openEHR-EHR-EVALUATION.adverse_reaction_risk.v1` | `medical_data/evaluation/adverse_reaction_risk_v1.yml` |
| `openEHR-EHR-EVALUATION.adverse_reaction_risk.v2` | `medical_data/evaluation/Adverse_reaction_risk_v2.yml` |
| `openEHR-EHR-EVALUATION.alcohol_consumption_summary.v1` | `medical_data/evaluation/alcohol_consumption_summary_v1.yml` |
| `openEHR-EHR-EVALUATION.cause_of_death.v1` | `medical_data/evaluation/Cause_of_death_v1.yml` |
| `openEHR-EHR-EVALUATION.communication_capability.v1` | `medical_data/evaluation/Communication_capability_v1.yml` |
| `openEHR-EHR-EVALUATION.contraceptive_summary.v1` | `medical_data/evaluation/Contraceptive_summary_v1.yml` |
| `openEHR-EHR-EVALUATION.contraindication.v1` | `medical_data/evaluation/Contraindication_v1.yml` |
| `openEHR-EHR-EVALUATION.education_summary.v1` | `medical_data/evaluation/Education_summary_v1.yml` |
| `openEHR-EHR-EVALUATION.ethnicity.v1` | `medical_data/evaluation/Ethnicity_v1.yml` |
| `openEHR-EHR-EVALUATION.exclusion_global.v1` | `medical_data/evaluation/Exclusion_global_v1.yml` |
| `openEHR-EHR-EVALUATION.exclusion_specific.v1` | `medical_data/evaluation/Exclusion_specific_v1.yml` |
| `openEHR-EHR-EVALUATION.financial_summary.v1` | `medical_data/evaluation/Financial_summary_v1.yml` |
| `openEHR-EHR-EVALUATION.gender.v1` | `medical_data/evaluation/Gender_v1.yml` |
| `openEHR-EHR-EVALUATION.goal.v1` | `medical_data/evaluation/Goal_v1.yml` |
| `openEHR-EHR-EVALUATION.health_risk.v1` | `medical_data/evaluation/Health_risk_v1.yml` |
| `openEHR-EHR-EVALUATION.housing_summary.v1` | `medical_data/evaluation/Housing_summary_v1.yml` |
| `openEHR-EHR-EVALUATION.menstruation_summary.v1` | `medical_data/evaluation/Menstruation_summary_v1.yml` |
| `openEHR-EHR-EVALUATION.occupation_summary.v1` | `medical_data/evaluation/Occupation_summary_v1.yml` |
| `openEHR-EHR-EVALUATION.precaution.v1` | `medical_data/evaluation/Precaution_v1.yml` |
| `openEHR-EHR-EVALUATION.reason_for_encounter.v1` | `medical_data/evaluation/Reason_for_encounter_v1.yml` |
| `openEHR-EHR-EVALUATION.recommendation.v2` | `medical_data/evaluation/Recommendation_v2.yml` |
| `openEHR-EHR-EVALUATION.social_network.v1` | `medical_data/evaluation/Social_network_v1.yml` |
| `openEHR-EHR-EVALUATION.substance_use_summary.v1` | `medical_data/evaluation/Substance_use_summary_v1.yml` |
| `openEHR-EHR-Evaluation.pregnancy_status.v0` | `medical_data/evaluation/Pregnancy_status_v0.yml` |
| `openEHR-EHR-OBSERVATION.age_assertion.v1` | `medical_data/observation/Age_assertion_v1.yml` |
| `openEHR-EHR-OBSERVATION.body_segment_discrepancy.v1` | `medical_data/observation/Body_segment_discrepancy_v1.yml` |
| `openEHR-EHR-OBSERVATION.bvc.v1` | `medical_data/observation/Bvc_v1.yml` |
| `openEHR-EHR-OBSERVATION.demo.v1` | `medical_data/observation/Demo_v1.yml` |
| `openEHR-EHR-OBSERVATION.ecog.v1` | `medical_data/observation/Ecog_v1.yml` |
| `openEHR-EHR-OBSERVATION.ecog.v2` | `medical_data/observation/Ecog_v2.yml` |
| `openEHR-EHR-OBSERVATION.exam.v1` | `medical_data/observation/Exam_v1.yml` |
| `openEHR-EHR-OBSERVATION.exposure_screening.v1` | `medical_data/observation/Exposure_screening_v1.yml` |
| `openEHR-EHR-OBSERVATION.investigation_screening.v1` | `medical_data/observation/Investigation_screening_v1.yml` |
| `openEHR-EHR-OBSERVATION.lenke_classification.v1` | `medical_data/observation/Lenke_classification_v1.yml` |
| `openEHR-EHR-OBSERVATION.mayo_score.v1` | `medical_data/observation/Mayo_score_v1.yml` |
| `openEHR-EHR-OBSERVATION.mini_bestest.v1` | `medical_data/observation/Mini_bestest_v1.yml` |
| `openEHR-EHR-OBSERVATION.msfc_score.v1` | `medical_data/observation/MSFC_score_v1.yml` |
| `openEHR-EHR-OBSERVATION.msfc_score.v2` | `medical_data/observation/MSFC_score_v2.yml` |
| `openEHR-EHR-OBSERVATION.nyha_heart_failure.v1` | `medical_data/observation/Nyha_heart_failure_v1.yml` |
| `openEHR-EHR-OBSERVATION.problem_screening.v1` | `medical_data/observation/Problem_screening_v1.yml` |
| `openEHR-EHR-OBSERVATION.social_context_screening.v1` | `medical_data/observation/Social_context_screening_v1.yml` |
| `openEHR-EHR-OBSERVATION.story.v1` | `medical_data/observation/Story_v1.yml` |
| `openEHR-EHR-OBSERVATION.substance_use_screening.v1` | `medical_data/observation/Substance_use_screening_v1.yml` |
| `openEHR-EHR-OBSERVATION.symptom_sign_screening.v1` | `medical_data/observation/Symptom_sign_screening_v1.yml` |
| `openEHR-EHR-OBSERVATION.tanner.v1` | `medical_data/observation/Tanner_v1.yml` |
| `openEHR-EHR-OBSERVATION.testicular_volume.v1` | `medical_data/observation/Testicular_volume_v1.yml` |
| `openEHR-EHR-OBSERVATION.timed_25_foot_walk.v1` | `medical_data/observation/Timed_25_foot_walk_v1.yml` |
| `openEHR-EHR-OBSERVATION.travel_screening.v1` | `medical_data/observation/Travel_screening_v1.yml` |

### Several target tables (11)

| Archetype | Also maps to | Mapping file |
|---|---|---|
| `openEHR-EHR-CLUSTER.imaging_exam-fallopian_tube.v1` | `ProcedureOccurrence` | `medical_data/cluster/Imaging_exam_fallopian_tube.yml` |
| `openEHR-EHR-EVALUATION.smokeless_tobacco_summary.v1` | `Measurement` | `medical_data/evaluation/Smokeless_tobacco_summary_v1.yml` |
| `openEHR-EHR-EVALUATION.tobacco_smoking_summary.v1` | `Measurement` | `medical_data/evaluation/Tobacco_smoking_summary_v1.yml` |
| `openEHR-EHR-OBSERVATION.fluid_balance.v1` | `Measurement` | `medical_data/observation/Fluid_balance_v1.yml` |
| `openEHR-EHR-OBSERVATION.fluid_input.v1` | `Measurement` | `medical_data/observation/Fluid_input_v1.yml` |
| `openEHR-EHR-OBSERVATION.fluid_output.v1` | `Measurement` | `medical_data/observation/Fluid_output_v1.yml` |
| `openEHR-EHR-OBSERVATION.medication_screening.v1` | `DrugExposure` | `medical_data/observation/Medication_screening_v1.yml` |
| `openEHR-EHR-OBSERVATION.menstrual_diary.v1` | `Measurement` | `medical_data/observation/Menstrual_diary_v1.yml` |
| `openEHR-EHR-OBSERVATION.menstruation.v1` | `Measurement` | `medical_data/observation/Menstruation_v1.yml` |
| `openEHR-EHR-OBSERVATION.nine_hole_peg_test.v1` | `Measurement` | `medical_data/observation/Nine_hole_peg_test_v1.yml` |
| `openEHR-EHR-OBSERVATION.spirometry_result.v2` | `Measurement` | `medical_data/observation/Spirometry_result_v2.yml` |

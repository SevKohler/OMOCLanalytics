# Measurement

Target table OMOP CDM v5.4 `MEASUREMENT`. The prepared table lists the content concepts we count archetype leafs against. See the README for how it is derived.

## CDM fields (23)

| Field | Required | Type | Key | Description |
|---|---|---|---|---|
| `measurement_id` | Yes | integer | PK | The unique key given to a Measurement record for a Person. Refer to the ETL for how duplicate Measurements during the same Visit were handled. |
| `person_id` | Yes | integer | FK PERSON | The PERSON_ID of the Person for whom the Measurement is recorded. This may be a system generated code. |
| `measurement_concept_id` | Yes | integer | FK CONCEPT | The MEASUREMENT_CONCEPT_ID field is recommended for primary use in analyses, and must be used for network studies. |
| `measurement_date` | Yes | date |  | Use this date to determine the date of the measurement. |
| `measurement_datetime` | No | datetime |  |  |
| `measurement_time` | No | varchar(10) |  |  |
| `measurement_type_concept_id` | Yes | integer | FK CONCEPT | This field can be used to determine the provenance of the Measurement record, as in whether the measurement was from an EHR system, insurance claim, registry, or other sources. |
| `operator_concept_id` | No | integer | FK CONCEPT | The meaning of Concept 4172703 for '=' is identical to omission of a OPERATOR_CONCEPT_ID value. Since the use of this field is rare, it's important when devising analyses to not to forget testing for the content of this field for values different from =. |
| `value_as_number` | No | float |  | This is the numerical value of the Result of the Measurement, if available. Note that measurements such as blood pressures will be split into their component parts i.e. one record for systolic, one record for diastolic. |
| `value_as_concept_id` | No | integer | FK CONCEPT | If the raw data gives a categorial result for measurements those values are captured and mapped to standard concepts in the 'Meas Value' domain. |
| `unit_concept_id` | No | integer | FK CONCEPT | There is currently no recommended unit for individual measurements, i.e. it is not mandatory to represent Hemoglobin a1C measurements as a percentage. UNIT_SOURCE_VALUES should be mapped to a Standard Concept in the Unit domain that best represents the unit as given in the source data. |
| `range_low` | No | float |  | Ranges have the same unit as the VALUE_AS_NUMBER. These ranges are provided by the source and should remain NULL if not given. |
| `range_high` | No | float |  | Ranges have the same unit as the VALUE_AS_NUMBER. These ranges are provided by the source and should remain NULL if not given. |
| `provider_id` | No | integer | FK PROVIDER | The provider associated with measurement record, e.g. the provider who ordered the test or the provider who recorded the result. |
| `visit_occurrence_id` | No | integer | FK VISIT_OCCURRENCE | The visit during which the Measurement occurred. |
| `visit_detail_id` | No | integer | FK VISIT_DETAIL | The VISIT_DETAIL record during which the Measurement occurred. For example, if the Person was in the ICU at the time the VISIT_OCCURRENCE record would reflect the overall hospital stay and the VISIT_DETAIL record would reflect the ICU stay during the hospital visit. |
| `measurement_source_value` | No | varchar(50) |  | This field houses the verbatim value from the source data representing the Measurement that occurred. For example, this could be an ICD10 or Read code. |
| `measurement_source_concept_id` | No | integer | FK CONCEPT | This is the concept representing the MEASUREMENT_SOURCE_VALUE and may not necessarily be standard. This field is discouraged from use in analysis because it is not required to contain Standard Concepts that are used across the OHDSI community, and should only be used when Standard Concepts do not adequately represent the source detail for the Measurement necessary for a given analytic use case. Consider using MEASUREMENT_CONCEPT_ID instead to enable standardized analytics that can be consistent across the network. |
| `unit_source_value` | No | varchar(50) |  | This field houses the verbatim value from the source data representing the unit of the Measurement that occurred. |
| `unit_source_concept_id` | No | integer | FK CONCEPT | "This is the concept representing the UNIT_SOURCE_VALUE and may not necessarily be standard. This field is discouraged from use in analysis because it is not required to contain Standard Concepts that are used across the OHDSI community, and should only be used when Standard Concepts do not adequately represent the source detail for the Measurement necessary for a given analytic use case. Consider using UNIT_CONCEPT_ID instead to enable standardized analytics that can be consistent across the network." |
| `value_source_value` | No | varchar(50) |  | This field houses the verbatim result value of the Measurement from the source data . |
| `measurement_event_id` | No | integer |  | If the Measurement record is related to another record in the database, this field is the primary key of the linked record. |
| `meas_event_field_concept_id` | No | integer | FK CONCEPT | If the Measurement record is related to another record in the database, this field is the CONCEPT_ID that identifies which table the primary key of the linked record came from. |

## Prepared table

4 content concepts kept, 9 removed.

| Concept | OMOP fields | Kept | Reason |
|---|---|---|---|
| Measurement concept | `measurement_concept_id`, `measurement_source_value`, `measurement_source_concept_id` | yes | |
| Measurement date/time | `measurement_date`, `measurement_datetime` | yes | |
| Measurement type / provenance | `measurement_type_concept_id` | yes | |
| Value (DV_QUANTITY / DV_CODED_TEXT / DV_ORDINAL / DV_COUNT / DV_PROPORTION) | `value_as_number`, `value_as_concept_id`, `value_source_value` | yes | |
| Record identifier | `measurement_id` | no | openEHR RM identifier. |
| Person | `person_id` | no | link to the subject of care. |
| Measurement time | `measurement_time` | no | deprecated OMOP column, the date and datetime already carry the timing. |
| Operator | `operator_concept_id` | no | RM attribute of the value (`DV_QUANTIFIED.magnitude_status`). Every operator mapping in OMOCL reads it from the value, so it is not a separate node. |
| Unit | `unit_concept_id`, `unit_source_value`, `unit_source_concept_id` | no | RM attribute of the value (`DV_QUANTITY.units`). In the OMOCL Measurement mappings the unit is always taken from the value or given as a constant code, never from its own node. |
| Reference range | `range_low`, `range_high` | no | RM attribute of the value (`DV_QUANTITY.reference_ranges`). |
| Provider | `provider_id` | no | link to the recording provider. |
| Visit | `visit_occurrence_id`, `visit_detail_id` | no | link to the encounter. |
| Event link | `measurement_event_id`, `meas_event_field_concept_id` | no | link to another record. |

## Mapped archetypes

Archetypes whose OMOCL mapping targets this table.

### Single target table (66)

| Archetype | Mapping file |
|---|---|
| `openEHR-EHR-CLUSTER.boston_bowel_preparation_scale.v1` | `medical_data/cluster/Boston_bowel_preparation_scale_v1.yml` |
| `openEHR-EHR-CLUSTER.ctcae.v1` | `medical_data/cluster/Ctcae_v1.yml` |
| `openEHR-EHR-CLUSTER.education_record.v1` | `medical_data/cluster/Education_record_v1.yml` |
| `openEHR-EHR-CLUSTER.figo_staging_cancer.v1` | `medical_data/cluster/Figo_staging_cancer.yml` |
| `openEHR-EHR-CLUSTER.fnclcc.v1` | `medical_data/cluster/Fnclcc.yml` |
| `openEHR-EHR-CLUSTER.inspired_oxygen.v1` | `medical_data/cluster/Inspired_oxygen_v1.yml` |
| `openEHR-EHR-CLUSTER.laboratory_test_analyte.v1` | `medical_data/cluster/Laboratory_test_analyte_v1.yml` |
| `openEHR-EHR-CLUSTER.reference_sequence.v1` | `medical_data/cluster/Reference_sequence_v1.yml` |
| `openEHR-EHR-CLUSTER.specimen_container.v1` | `medical_data/cluster/Specimen_container_v1.yml` |
| `openEHR-EHR-EVALUATION.clinical_synopsis.v1` | `medical_data/evaluation/Clinical_synopsis_v1.yml` |
| `openEHR-EHR-EVALUATION.last_menstrual_period.v1` | `medical_data/evaluation/Last_menstrual_period_v1.yml` |
| `openEHR-EHR-EVALUATION.obstetric_summary.v1` | `medical_data/evaluation/Obstetric_summary_v1.yml` |
| `openEHR-EHR-OBSERVATION.acvpu.v1` | `medical_data/observation/Acvpu_v1.yml` |
| `openEHR-EHR-OBSERVATION.apgar.v2` | `medical_data/observation/Apgar_v2.yml` |
| `openEHR-EHR-OBSERVATION.asa_status.v1` | `medical_data/observation/Asa_status_v1.yml` |
| `openEHR-EHR-OBSERVATION.blood_pressure.v2` | `medical_data/observation/Blood_pressure_v2.yml` |
| `openEHR-EHR-OBSERVATION.body_mass_index.v2` | `medical_data/observation/Body_mass_index_v2.yml` |
| `openEHR-EHR-OBSERVATION.body_segment_area.v1` | `medical_data/observation/Body_segment_area_v1.yml` |
| `openEHR-EHR-OBSERVATION.body_segment_circumference.v1` | `medical_data/observation/Body_segment_circumference_v1.yml` |
| `openEHR-EHR-OBSERVATION.body_segment_length.v1` | `medical_data/observation/Body_segment_length_v1.yml` |
| `openEHR-EHR-OBSERVATION.body_surface_area.v1` | `medical_data/observation/Body_surface_area_v1.yml` |
| `openEHR-EHR-OBSERVATION.body_temperature.v2` | `medical_data/observation/Body_temperature_v2.yml` |
| `openEHR-EHR-OBSERVATION.body_weight.v2` | `medical_data/observation/Body_weight_v2.yml` |
| `openEHR-EHR-OBSERVATION.braden_scale.v1` | `medical_data/observation/Braden_scale_v1.yml` |
| `openEHR-EHR-OBSERVATION.capillary_refill.v1` | `medical_data/observation/Capillary_refill_v1.yml` |
| `openEHR-EHR-OBSERVATION.cgas.v1` | `medical_data/observation/Cgas_v1.yml` |
| `openEHR-EHR-OBSERVATION.charlson_comorbidity_index.v2` | `medical_data/observation/Charlson_comorbidity_index_v2.yml` |
| `openEHR-EHR-OBSERVATION.clinical_frailty_scale.v1` | `medical_data/observation/Clinical_frailty_scale_v1.yml` |
| `openEHR-EHR-OBSERVATION.clinical_frailty_scale2.v1` | `medical_data/observation/Clinical_frailty_scale2_v1.yml` |
| `openEHR-EHR-OBSERVATION.cormack_lehane.v1` | `medical_data/observation/Cormack_lehane_v1.yml` |
| `openEHR-EHR-OBSERVATION.cpax.v1` | `medical_data/observation/Cpax_v1.yml` |
| `openEHR-EHR-OBSERVATION.crb_65.v1` | `medical_data/observation/Crb_65_v1.yml` |
| `openEHR-EHR-OBSERVATION.curb_65.v1` | `medical_data/observation/Curb_65_v1.yml` |
| `openEHR-EHR-OBSERVATION.ecg_result.v1` | `medical_data/observation/Ecg_result_v1.yml` |
| `openEHR-EHR-OBSERVATION.esas_r.v1` | `medical_data/observation/Esas_r_v1.yml` |
| `openEHR-EHR-OBSERVATION.fetal_biometry.v1` | `medical_data/observation/Fetal_biometry_v1.yml` |
| `openEHR-EHR-OBSERVATION.four_a_test.v1` | `medical_data/observation/Four_a_test_v1.yml` |
| `openEHR-EHR-OBSERVATION.glasgow_coma_scale.v1` | `medical_data/observation/Glasgow_coma_scale_v1.yml` |
| `openEHR-EHR-OBSERVATION.glasgow_outcome_scale_extended.v1` | `medical_data/observation/Glasgow_outcome_scale_extended_v1.yml` |
| `openEHR-EHR-OBSERVATION.head_circumference.v1` | `medical_data/observation/Head_circumference_v1.yml` |
| `openEHR-EHR-OBSERVATION.height.v1` | `medical_data/observation/Body_height_v1.yml` |
| `openEHR-EHR-OBSERVATION.height.v2` | `medical_data/observation/Height_v2.yml` |
| `openEHR-EHR-OBSERVATION.hip_circumference.v1` | `medical_data/observation/Hip_circumference_v1.yml` |
| `openEHR-EHR-OBSERVATION.hirsutism_scales.v1` | `medical_data/observation/Hirsutism_scales_v1.yml` |
| `openEHR-EHR-OBSERVATION.ipss.v1` | `medical_data/observation/Ipss_v1.yml` |
| `openEHR-EHR-OBSERVATION.karnofsky_performance_status_scale.v1` | `medical_data/observation/Karnofsky_performance_status_scale_v1.yml` |
| `openEHR-EHR-OBSERVATION.mallampati_classification.v1` | `medical_data/observation/Mallampati_classification_v1.yml` |
| `openEHR-EHR-OBSERVATION.malnutrition_screening_tool.v1` | `medical_data/observation/Malnutrition_screening_tool_v1.yml` |
| `openEHR-EHR-OBSERVATION.management_screening.v1` | `medical_data/observation/Management_screening_v1.yml` |
| `openEHR-EHR-OBSERVATION.management_screening.v2` | `medical_data/observation/Management_screening_v2.yml` |
| `openEHR-EHR-OBSERVATION.modified_rankin_scale.v1` | `medical_data/observation/Modified_rankin_scale_v1.yml` |
| `openEHR-EHR-OBSERVATION.news2.v1` | `medical_data/observation/News2_v1.yml` |
| `openEHR-EHR-OBSERVATION.news_uk_rcp.v1` | `medical_data/observation/News_uk_rcp_v1.yml` |
| `openEHR-EHR-OBSERVATION.paced_auditory_serial_addition_test.v1` | `medical_data/observation/Paced_auditory_serial_addition_test_v1.yml` |
| `openEHR-EHR-OBSERVATION.pasi_score.v1` | `medical_data/observation/Pasi_score_v1.yml` |
| `openEHR-EHR-OBSERVATION.pf_ratio.v1` | `medical_data/observation/Pf_ratio_v1.yml` |
| `openEHR-EHR-OBSERVATION.progress_note.v1` | `medical_data/observation/Progress_note_v1.yml` |
| `openEHR-EHR-OBSERVATION.pulse.v2` | `medical_data/observation/Pulse_v2.yml` |
| `openEHR-EHR-OBSERVATION.pulse_oximetry.v1` | `medical_data/observation/Pulse_oximetry_v1.yml` |
| `openEHR-EHR-OBSERVATION.qsofa_score.v1` | `medical_data/observation/Qsofa_score_v1.yml` |
| `openEHR-EHR-OBSERVATION.respiration.v2` | `medical_data/observation/Respiration_v2.yml` |
| `openEHR-EHR-OBSERVATION.revised_cardiac_risk_index.v1` | `medical_data/observation/Revised_cardiac_risk_index_v1.yml` |
| `openEHR-EHR-OBSERVATION.simplified_tanner_whitehouse_3.v1` | `medical_data/observation/Simplified_tanner_whitehouse_3_v1.yml` |
| `openEHR-EHR-OBSERVATION.urinalysis.v1` | `medical_data/observation/Urinalysis_v1.yml` |
| `openEHR-EHR-OBSERVATION.waist_circumference.v1` | `medical_data/observation/Waist_circumference_v1.yml` |
| `openEHR-EHR-OBSERVATION.ygtss_revised.v1` | `medical_data/observation/Ygtss_revised_v1.yml` |

### Several target tables (9)

| Archetype | Also maps to | Mapping file |
|---|---|---|
| `openEHR-EHR-EVALUATION.smokeless_tobacco_summary.v1` | `Observation` | `medical_data/evaluation/Smokeless_tobacco_summary_v1.yml` |
| `openEHR-EHR-EVALUATION.tobacco_smoking_summary.v1` | `Observation` | `medical_data/evaluation/Tobacco_smoking_summary_v1.yml` |
| `openEHR-EHR-OBSERVATION.fluid_balance.v1` | `Observation` | `medical_data/observation/Fluid_balance_v1.yml` |
| `openEHR-EHR-OBSERVATION.fluid_input.v1` | `Observation` | `medical_data/observation/Fluid_input_v1.yml` |
| `openEHR-EHR-OBSERVATION.fluid_output.v1` | `Observation` | `medical_data/observation/Fluid_output_v1.yml` |
| `openEHR-EHR-OBSERVATION.menstrual_diary.v1` | `Observation` | `medical_data/observation/Menstrual_diary_v1.yml` |
| `openEHR-EHR-OBSERVATION.menstruation.v1` | `Observation` | `medical_data/observation/Menstruation_v1.yml` |
| `openEHR-EHR-OBSERVATION.nine_hole_peg_test.v1` | `Observation` | `medical_data/observation/Nine_hole_peg_test_v1.yml` |
| `openEHR-EHR-OBSERVATION.spirometry_result.v2` | `Observation` | `medical_data/observation/Spirometry_result_v2.yml` |

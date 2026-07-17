# Field overloading per archetype

Every OMOP field fed by two or more distinct source paths (constant `code` values and conceptMap lookups excluded; reference-model paths kept).

Overloaded OMOP fields: **16** distinct, seen across **159** archetype mappings.

## openEHR-EHR-ACTION.health_education.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/description[at0001]/items[at0026]`<br>`.` |

## openEHR-EHR-ACTION.medication.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| DrugExposure | drug_exposure_end_date | 3 | `/items[at0043]`<br>`../`<br>`.` |
| DrugExposure | drug_exposure_start_date | 3 | `/items[at0043]`<br>`../`<br>`.` |

## openEHR-EHR-ACTION.procedure.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| ProcedureOccurrence | procedure_start_date | 2 | `description[at0001]/items[at0066]`<br>`.` |

## openEHR-EHR-ACTION.service.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 3 | `/description[at0001]/items[at0032]`<br>`/description[at0001]/items[at0025]`<br>`.` |

## openEHR-EHR-ADMIN_ENTRY.person_data.v0

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Person | ethnicity_concept_id | 2 | `/data[at0001]/items[openEHR-EHR-CLUSTER.ethnischer_hintergrund.v0]/items[at0002]`<br>`/data[at0001]/item[openEHR-EHR-EVALUATION.ethnicity.v1]/items[at0003]` |
| Person | year_of_birth | 2 | `/data[at0001]/items[openEHR-EHR-CLUSTER.person_birth_data_iso.v0]/items[at0001]`<br>`../content[openEHR-EHR-OBSERVATION.age.v0]/data[at0001]/events[at0002]/data[at0003]/items[at0004]` |

## openEHR-EHR-CLUSTER.Oocyte_specimen.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.adverse_reaction_event.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 4 | `/items[at0008]`<br>`/items[at0015]`<br>`../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.anatomical_location.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | value | 2 | `/items[at0065]`<br>`/items[at0001]` |

## openEHR-EHR-CLUSTER.boston_bowel_preparation_scale.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.clinical_evidence.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.ctcae.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.device.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| DeviceExposure | concept_id | 2 | `/items[at0001]`<br>`/items[at0003]` |
| DeviceExposure | device_exposure_end_date | 3 | `../items[at0022]/items[at0009]`<br>`../`<br>`../../` |
| DeviceExposure | device_exposure_start_date | 4 | `../items[at0022]/items[at0008]`<br>`../`<br>`../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.dosage.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| DrugExposure | drug_exposure_end_date | 2 | `../items[at0043]`<br>`../../` |
| DrugExposure | drug_exposure_start_date | 2 | `../items[at0043]`<br>`../../` |

## openEHR-EHR-CLUSTER.dosage.v2

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| DrugExposure | drug_exposure_end_date | 2 | `../items[at0043]`<br>`../../` |
| DrugExposure | drug_exposure_start_date | 2 | `../items[at0043]`<br>`../../` |

## openEHR-EHR-CLUSTER.education_record.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.exam.v2

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.family_prevalence.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.figo_staging_cancer.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.fnclcc.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.genomic_conversion_variant.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.genomic_copy_number_variant.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.genomic_deletion_insertion_variant.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.genomic_deletion_variant.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.genomic_duplication_variant.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.genomic_insertion_variant.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.genomic_inversion_variant.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.genomic_repeated_sequence_variant.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.genomic_substitution_variant.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.genomic_variant_result.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.gist_modified_nih.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.housing_record.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.imaging_exam-cervix.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.imaging_exam-fallopian_tube.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |
| ProcedureOccurrence | procedure_start_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.imaging_exam-foetus.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.imaging_exam-gestational_sac.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.imaging_exam-ovary.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.imaging_exam-rectouterine_pouch.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.imaging_exam.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.information_resource.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.inspired_oxygen.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.interpreter_request.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.item_transport.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 4 | `/items[at0007]`<br>`/items[at0004]`<br>`../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.knowledge_base_reference.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.laboratory_test_analyte.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 3 | `/items[at0025]`<br>`../../`<br>`../../../` |

## openEHR-EHR-CLUSTER.language.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.media_file.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.occupation_record.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.organisation.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.person.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |
| Observation | value | 2 | `/items[at0003]`<br>`/items[at0001]` |

## openEHR-EHR-CLUSTER.problem_qualifier.v2

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.range_of_motion.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.reference_sequence.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.religion.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.service_direction.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.specimen.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Specimen | concept_id | 2 | `/items[at0029]`<br>`/items[at0098]` |

## openEHR-EHR-CLUSTER.specimen_container.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.structured_name.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.symptom_sign.v2

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| ConditionOccurrence | condition_start_date | 4 | `/items[at0152]`<br>`/items[at0164]`<br>`../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.therapeutic_direction.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 3 | `/items[at0178]`<br>`../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.tnm-pathological.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.tnm.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-CLUSTER.who_grade_bone_sarcoma.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `../../`<br>`../../../../../context` |

## openEHR-EHR-EVALUATION.advance_care_directive.v2

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/protocol[at0010]/items[at0053]`<br>`../context` |

## openEHR-EHR-EVALUATION.adverse_reaction_risk.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/items[at0027]`<br>`../context` |

## openEHR-EHR-EVALUATION.adverse_reaction_risk.v2

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 3 | `/data[at0001]/items[at0117]`<br>`/data[at0001]/items[at0133]`<br>`../context` |
| Observation | qualifier | 4 | `/data[at0001]/items[at0130]`<br>`/data[at0001]/items[at0063]`<br>`/data[at0001]/items[at0101]`<br>`/data[at0001]/items[at0120]` |

## openEHR-EHR-EVALUATION.alcohol_consumption_summary.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 3 | `/data[at0001]/items[at0015]`<br>`/data[at0001]/items[at0080]`<br>`../context` |

## openEHR-EHR-EVALUATION.art_cycle_summary.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| ProcedureOccurrence | procedure_start_date | 2 | `data[at0001]/items[at0004]`<br>`../context` |

## openEHR-EHR-EVALUATION.gender.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | value | 2 | `/data[at0002]/items[at0019]`<br>`/data[at0002]/items[at0022]` |

## openEHR-EHR-EVALUATION.health_risk.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/events[at0023]`<br>`../context` |

## openEHR-EHR-EVALUATION.last_menstrual_period.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/items[at0002]`<br>`.` |

## openEHR-EHR-EVALUATION.medication_summary.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| DrugExposure | drug_exposure_end_date | 3 | `/data[at0001]/items[at0010]`<br>`../`<br>`.` |
| DrugExposure | drug_exposure_start_date | 3 | `/data[at0001]/items[at0009]`<br>`../`<br>`.` |

## openEHR-EHR-EVALUATION.problem_diagnosis.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| ConditionOccurrence | condition_start_date | 2 | `data[at0001]/items[at0077]`<br>`../context` |

## openEHR-EHR-EVALUATION.smokeless_tobacco_summary.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | value | 2 | `/data[at0001]/items[at0089]`<br>`/data[at0001]/items[at0043]` |

## openEHR-EHR-EVALUATION.specimen_summary.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Specimen | specimen_date | 2 | `/data[at0001]/items[at0018]`<br>`../context` |

## openEHR-EHR-EVALUATION.substance_use_summary.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 4 | `/data[at0001]/items[at0008]`<br>`/data[at0001]/items[at0009]`<br>`/data[at0001]/items[at0010]`<br>`../context` |

## openEHR-EHR-EVALUATION.tobacco_smoking_summary.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | value | 2 | `/data[at0001]/items[at0089]`<br>`/data[at0001]/items[at0043]` |

## openEHR-EHR-INSTRUCTION.therapeutic_item_order.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| ProcedureOccurrence | procedure_start_date | 2 | `description[at0002]/items[at0012]`<br>`.` |

## openEHR-EHR-OBSERVATION.acvpu.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.asa_status.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0015]/events[at0016]`<br>`.` |

## openEHR-EHR-OBSERVATION.body_mass_index.v2

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.body_segment_area.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.body_segment_circumference.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.body_segment_discrepancy.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.body_segment_length.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.body_surface_area.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.body_temperature.v2

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0002]/events[at0003]`<br>`.` |

## openEHR-EHR-OBSERVATION.body_weight.v2

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0002]/events[at0003]`<br>`.` |

## openEHR-EHR-OBSERVATION.braden_scale.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.capillary_refill.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.cgas.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.charlson_comorbidity_index.v2

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.clinical_frailty_scale2.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.cormack_lehane.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0007]/events[at0008]`<br>`../context` |

## openEHR-EHR-OBSERVATION.cpax.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.crb_65.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.curb_65.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.demo.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.ecg_result.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.ecog.v2

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.esas_r.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.exam.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.exposure_screening.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.fetal_biometry.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.fluid_balance.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |
| Observation | observation_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.fluid_input.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.fluid_output.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.four_a_test.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.glasgow_coma_scale.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.glasgow_outcome_scale_extended.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.height.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.height.v2

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.hip_circumference.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0010]`<br>`.` |

## openEHR-EHR-OBSERVATION.hirsutism_scales.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.imaging_exam_result.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| ConditionOccurrence | condition_start_date | 3 | `/data[at0001]/events[at0002]/data[at0003]/items[at0070]`<br>`/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.investigation_screening.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 3 | `/data[at0022]/events[at0023]/data[at0001]/items[at0026]/items[at0003]`<br>`/data[at0022]/events[at0023]`<br>`../context` |

## openEHR-EHR-OBSERVATION.ipss.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | ` /data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.karnofsky_performance_status_scale.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.lenke_classification.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.mallampati_classification.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.malnutrition_screening_tool.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.management_screening.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 3 | `/data[at0001]/events[at0002]/data[at0003]/items[at0022]/items[at0037]`<br>`/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.management_screening.v2

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 3 | `/data[at0001]/events[at0002]/data[at0003]/items[at0022]/items[at0037]`<br>`/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.mayo_score.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.medication_screening.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| DrugExposure | drug_exposure_end_date | 3 | `/data[at0022]/events[at0023]/data[at0001]/items[at0026]/items[at0003]`<br>`/data[at0022]/events[at0023]/data[at0001]/items[at0026]/items[at0002]`<br>`../context` |
| DrugExposure | drug_exposure_start_date | 3 | `/data[at0022]/events[at0023]/data[at0001]/items[at0026]/items[at0003]`<br>`/data[at0022]/events[at0023]/data[at0001]/items[at0026]/items[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.medication_statement.v0

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| DrugExposure | drug_exposure_end_date | 6 | `data[at0003]/items[at0025]`<br>`data[at0003]/items[at0021]`<br>`data[at0003]/items[at0026]`<br>`data[at0003]/items[at0024]`<br>`data[at0003]/items[at0019]`<br>`.` |
| DrugExposure | drug_exposure_start_date | 3 | `data[at0003]/items[at0024]`<br>`data[at0003]/items[at0019]`<br>`.` |

## openEHR-EHR-OBSERVATION.menstrual_diary.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |
| Observation | observation_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |
| Observation | observation_date | 2 | `/data[at0001]/events[at0002]/data[at0003]/items[at0004]`<br>`../context` |

## openEHR-EHR-OBSERVATION.menstruation.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 3 | `/data[at0001]/events[at0002]/data[at0003]/items[at0004]`<br>`/data[at0001]/events[at0002]`<br>`../context` |
| Observation | observation_date | 3 | `/data[at0001]/events[at0002]/data[at0003]/items[at0004]`<br>`/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.mini_bestest.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.modified_rankin_scale.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.msfc_score.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/events[at0010]`<br>`../context` |

## openEHR-EHR-OBSERVATION.msfc_score.v2

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/events[at0010]`<br>`../context` |

## openEHR-EHR-OBSERVATION.news2.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.news_uk_rcp.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.nine_hole_peg_test.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0074]`<br>`../context` |
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0075]`<br>`../context` |
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0076]`<br>`../context` |
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0077]`<br>`../context` |
| Observation | observation_date | 2 | `/data[at0001]/events[at0074]`<br>`../context` |

## openEHR-EHR-OBSERVATION.nyha_heart_failure.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.paced_auditory_serial_addition_test.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0002]/events[at0064]`<br>`../context` |
| Measurement | measurement_date | 2 | `/data[at0002]/events[at0065]`<br>`../context` |

## openEHR-EHR-OBSERVATION.pasi_score.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.pf_ratio.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.problem_screening.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 3 | `/data[at0001]/events[at0002]/data[at0003]/items[at0022]/items[at0040]`<br>`/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.procedure_screening.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| ProcedureOccurrence | procedure_end_date | 3 | `/data[at0001]/events[at0002]/data[at0003]/items[at0022]/items[at0037]`<br>`/data[at0001]/events[at0002]`<br>`../context` |
| ProcedureOccurrence | procedure_start_date | 3 | `/data[at0001]/events[at0002]/data[at0003]/items[at0022]/items[at0037]`<br>`/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.progress_note.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.pulse.v2

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 3 | `/data[at0002]/events[at0003]`<br>`.`<br>`../` |

## openEHR-EHR-OBSERVATION.pulse_oximetry.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.qsofa_score.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.respiration.v2

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `.`<br>`../../` |

## openEHR-EHR-OBSERVATION.revised_cardiac_risk_index.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.simplified_tanner_whitehouse_3.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.social_context_screening.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.spirometry_result.v2

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |
| Observation | observation_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.story.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.substance_use_screening.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 4 | `/data[at0022]/events[at0023]/data[at0001]/items[at0026]/items[at0003]`<br>`/data[at0022]/events[at0023]/data[at0001]/items[at0026]/items[at0002]`<br>`/data[at0022]/events[at0023]`<br>`../context` |

## openEHR-EHR-OBSERVATION.symptom_sign_screening.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 3 | `/data[at0001]/events[at0002]/data[at0003]/items[at0022]/items[at0037]`<br>`/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.tanner.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.testicular_volume.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |

## openEHR-EHR-OBSERVATION.timed_25_foot_walk.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |
| Observation | observation_date | 2 | `/data[at0001]/events[at0007]`<br>`../context` |

## openEHR-EHR-OBSERVATION.travel_screening.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Observation | observation_date | 3 | `/data[at0022]/events[at0023]/data[at0001]/items[at0026]/items[at0003]`<br>`/data[at0022]/events[at0023]`<br>`../context` |

## openEHR-EHR-OBSERVATION.urinalysis.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`.` |

## openEHR-EHR-OBSERVATION.waist_circumference.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0010]`<br>`../context` |

## openEHR-EHR-OBSERVATION.ygtss_revised.v1

| OMOP table | OMOP field | # paths | Source paths |
|---|---|---|---|
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0002]`<br>`../context` |
| Measurement | measurement_date | 2 | `/data[at0001]/events[at0004]`<br>`../context` |

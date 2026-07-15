# Field overloading per archetype

Every OMOP field fed by two or more DISTINCT archetype source paths (constant `code` fallbacks and reference-model context paths excluded).

Overloaded fields: **22** across **18** archetype mappings.

## openEHR-EHR-ACTION.service.v1

| OMOP table | OMOP field | # paths | Archetype paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/description[at0001]/items[at0032]`<br>`/description[at0001]/items[at0025]` |

## openEHR-EHR-ADMIN_ENTRY.person_data.v0

| OMOP table | OMOP field | # paths | Archetype paths |
|---|---|---|---|
| Person | ethnicity_concept_id | 2 | `/data[at0001]/items[openEHR-EHR-CLUSTER.ethnischer_hintergrund.v0]/items[at0002]`<br>`/data[at0001]/item[openEHR-EHR-EVALUATION.ethnicity.v1]/items[at0003]` |
| Person | year_of_birth | 2 | `/data[at0001]/items[openEHR-EHR-CLUSTER.person_birth_data_iso.v0]/items[at0001]`<br>`../content[openEHR-EHR-OBSERVATION.age.v0]/data[at0001]/events[at0002]/data[at0003]/items[at0004]` |

## openEHR-EHR-CLUSTER.adverse_reaction_event.v1

| OMOP table | OMOP field | # paths | Archetype paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/items[at0008]`<br>`/items[at0015]` |

## openEHR-EHR-CLUSTER.anatomical_location.v1

| OMOP table | OMOP field | # paths | Archetype paths |
|---|---|---|---|
| Observation | value | 2 | `/items[at0065]`<br>`/items[at0001]` |

## openEHR-EHR-CLUSTER.device.v1

| OMOP table | OMOP field | # paths | Archetype paths |
|---|---|---|---|
| DeviceExposure | concept_id | 2 | `/items[at0001]`<br>`/items[at0003]` |

## openEHR-EHR-CLUSTER.item_transport.v1

| OMOP table | OMOP field | # paths | Archetype paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/items[at0007]`<br>`/items[at0004]` |

## openEHR-EHR-CLUSTER.person.v1

| OMOP table | OMOP field | # paths | Archetype paths |
|---|---|---|---|
| Observation | value | 2 | `/items[at0003]`<br>`/items[at0001]` |

## openEHR-EHR-CLUSTER.specimen.v1

| OMOP table | OMOP field | # paths | Archetype paths |
|---|---|---|---|
| Specimen | concept_id | 2 | `/items[at0029]`<br>`/items[at0098]` |

## openEHR-EHR-CLUSTER.symptom_sign.v2

| OMOP table | OMOP field | # paths | Archetype paths |
|---|---|---|---|
| ConditionOccurrence | condition_start_date | 2 | `/items[at0152]`<br>`/items[at0164]` |

## openEHR-EHR-EVALUATION.adverse_reaction_risk.v2

| OMOP table | OMOP field | # paths | Archetype paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/items[at0117]`<br>`/data[at0001]/items[at0133]` |
| Observation | qualifier | 4 | `/data[at0001]/items[at0130]`<br>`/data[at0001]/items[at0063]`<br>`/data[at0001]/items[at0101]`<br>`/data[at0001]/items[at0120]` |

## openEHR-EHR-EVALUATION.alcohol_consumption_summary.v1

| OMOP table | OMOP field | # paths | Archetype paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0001]/items[at0015]`<br>`/data[at0001]/items[at0080]` |

## openEHR-EHR-EVALUATION.gender.v1

| OMOP table | OMOP field | # paths | Archetype paths |
|---|---|---|---|
| Observation | value | 2 | `/data[at0002]/items[at0019]`<br>`/data[at0002]/items[at0022]` |

## openEHR-EHR-EVALUATION.smokeless_tobacco_summary.v1

| OMOP table | OMOP field | # paths | Archetype paths |
|---|---|---|---|
| Observation | value | 2 | `/data[at0001]/items[at0089]`<br>`/data[at0001]/items[at0043]` |

## openEHR-EHR-EVALUATION.substance_use_summary.v1

| OMOP table | OMOP field | # paths | Archetype paths |
|---|---|---|---|
| Observation | observation_date | 3 | `/data[at0001]/items[at0008]`<br>`/data[at0001]/items[at0009]`<br>`/data[at0001]/items[at0010]` |

## openEHR-EHR-EVALUATION.tobacco_smoking_summary.v1

| OMOP table | OMOP field | # paths | Archetype paths |
|---|---|---|---|
| Observation | value | 2 | `/data[at0001]/items[at0089]`<br>`/data[at0001]/items[at0043]` |

## openEHR-EHR-OBSERVATION.medication_screening.v1

| OMOP table | OMOP field | # paths | Archetype paths |
|---|---|---|---|
| DrugExposure | drug_exposure_end_date | 2 | `/data[at0022]/events[at0023]/data[at0001]/items[at0026]/items[at0003]`<br>`/data[at0022]/events[at0023]/data[at0001]/items[at0026]/items[at0002]` |
| DrugExposure | drug_exposure_start_date | 2 | `/data[at0022]/events[at0023]/data[at0001]/items[at0026]/items[at0003]`<br>`/data[at0022]/events[at0023]/data[at0001]/items[at0026]/items[at0002]` |

## openEHR-EHR-OBSERVATION.medication_statement.v0

| OMOP table | OMOP field | # paths | Archetype paths |
|---|---|---|---|
| DrugExposure | drug_exposure_end_date | 5 | `data[at0003]/items[at0025]`<br>`data[at0003]/items[at0021]`<br>`data[at0003]/items[at0026]`<br>`data[at0003]/items[at0024]`<br>`data[at0003]/items[at0019]` |
| DrugExposure | drug_exposure_start_date | 2 | `data[at0003]/items[at0024]`<br>`data[at0003]/items[at0019]` |

## openEHR-EHR-OBSERVATION.substance_use_screening.v1

| OMOP table | OMOP field | # paths | Archetype paths |
|---|---|---|---|
| Observation | observation_date | 2 | `/data[at0022]/events[at0023]/data[at0001]/items[at0026]/items[at0003]`<br>`/data[at0022]/events[at0023]/data[at0001]/items[at0026]/items[at0002]` |

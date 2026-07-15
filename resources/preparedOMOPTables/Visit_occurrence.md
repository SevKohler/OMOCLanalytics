# Visit occurrence

Target table OMOP CDM v5.4 `VISIT_OCCURRENCE`. The prepared table lists the content concepts we count archetype leafs against. See the README for how it is derived.

## CDM fields (17)

| Field | Required | Type | Key | Description |
|---|---|---|---|---|
| `visit_occurrence_id` | Yes | integer | PK | Use this to identify unique interactions between a person and the health care system. This identifier links across the other CDM event tables to associate events with a visit. |
| `person_id` | Yes | integer | FK PERSON |  |
| `visit_concept_id` | Yes | integer | FK CONCEPT | This field contains a concept id representing the kind of visit, like inpatient or outpatient. All concepts in this field should be standard and belong to the Visit domain. |
| `visit_start_date` | Yes | date |  | For inpatient visits, the start date is typically the admission date. For outpatient visits the start date and end date will be the same. |
| `visit_start_datetime` | No | datetime |  |  |
| `visit_end_date` | Yes | date |  | For inpatient visits the end date is typically the discharge date. If a Person is still an inpatient in the hospital at the time of the data extract and does not have a visit_end_date, then set the visit_end_date to the date of the data pull. |
| `visit_end_datetime` | No | datetime |  | If a Person is still an inpatient in the hospital at the time of the data extract and does not have a visit_end_datetime, then set the visit_end_datetime to the datetime of the data pull. |
| `visit_type_concept_id` | Yes | Integer | FK CONCEPT | Use this field to understand the provenance of the visit record, or where the record comes from. |
| `provider_id` | No | integer | FK PROVIDER | There will only be one provider per visit record and the ETL document should clearly state how they were chosen (attending, admitting, etc.). If there are multiple providers associated with a visit in the source, this can be reflected in the event tables (CONDITION_OCCURRENCE, PROCEDURE_OCCURRENCE, etc.) or in the VISIT_DETAIL table. |
| `care_site_id` | No | integer | FK CARE_SITE | This field provides information about the Care Site where the Visit took place. |
| `visit_source_value` | No | varchar(50) |  | This field houses the verbatim value from the source data representing the kind of visit that took place (inpatient, outpatient, emergency, etc.) |
| `visit_source_concept_id` | No | integer | FK CONCEPT |  |
| `admitted_from_concept_id` | No | integer | FK CONCEPT | Use this field to determine where the patient was admitted from. This concept is part of the visit domain and can indicate if a patient was admitted to the hospital from a long-term care facility, for example. |
| `admitted_from_source_value` | No | varchar(50) |  |  |
| `discharged_to_concept_id` | No | integer | FK CONCEPT | Use this field to determine where the patient was discharged to after a visit. This concept is part of the visit domain and can indicate if a patient was transferred to another hospital or sent to a long-term care facility, for example. It is assumed that a person is discharged to home therefore there is not a standard concept id for "home". Use concept id = 0 when a person is discharged to home. |
| `discharged_to_source_value` | No | varchar(50) |  |  |
| `preceding_visit_occurrence_id` | No | integer | FK VISIT_OCCURRENCE | Use this field to find the visit that occurred for the person prior to the given visit. There could be a few days or a few years in between. |

## Prepared table

6 content concepts kept, 5 removed.

| Concept | OMOP fields | Kept | Reason |
|---|---|---|---|
| Visit concept | `visit_concept_id`, `visit_source_value`, `visit_source_concept_id` | yes | |
| Visit start date/time | `visit_start_date`, `visit_start_datetime` | yes | |
| Visit end date/time | `visit_end_date`, `visit_end_datetime` | yes | |
| Visit type / provenance | `visit_type_concept_id` | yes | |
| Admitted from | `admitted_from_concept_id`, `admitted_from_source_value` | yes | |
| Discharged to | `discharged_to_concept_id`, `discharged_to_source_value` | yes | |
| Record identifier | `visit_occurrence_id` | no | openEHR RM identifier. |
| Person | `person_id` | no | link to the subject of care. |
| Provider | `provider_id` | no | link to the recording provider. |
| Care site | `care_site_id` | no | link to the care site. |
| Preceding visit occurrence | `preceding_visit_occurrence_id` | no | link to the prior visit record. |

## Mapped archetypes

Archetypes whose OMOCL mapping targets this table.

### Single target table (1)

| Archetype | Mapping file |
|---|---|
| `openEHR-EHR-ADMIN_ENTRY.episode_institution.v0` | `medical_data/admin_entry/Episode_institution_v0.yml` |

### Several target tables (0)

None.

# Person

Target table OMOP CDM v5.4 `PERSON`. The prepared table lists the content concepts we count archetype leafs against. See the README for how it is derived.

## CDM fields (18)

| Field | Required | Type | Key | Description |
|---|---|---|---|---|
| `person_id` | Yes | integer | PK | It is assumed that every person with a different unique identifier is in fact a different person and should be treated independently. |
| `gender_concept_id` | Yes | integer | FK CONCEPT | This field is meant to capture the biological sex at birth of the Person. This field should not be used to study gender identity issues. |
| `year_of_birth` | Yes | integer |  | Compute age using year_of_birth. |
| `month_of_birth` | No | integer |  |  |
| `day_of_birth` | No | integer |  |  |
| `birth_datetime` | No | datetime |  |  |
| `race_concept_id` | Yes | integer | FK CONCEPT | This field captures race or ethnic background of the person. |
| `ethnicity_concept_id` | Yes | integer | FK CONCEPT | This field captures Ethnicity as defined by the Office of Management and Budget (OMB) of the US Government: it distinguishes only between "Hispanic" and "Not Hispanic". Races and ethnic backgrounds are not stored here. |
| `location_id` | No | integer | FK LOCATION | The location refers to the physical address of the person. This field should capture the last known location of the person. |
| `provider_id` | No | integer | FK PROVIDER | The Provider refers to the last known primary care provider (General Practitioner). |
| `care_site_id` | No | integer | FK CARE_SITE | The Care Site refers to where the Provider typically provides the primary care. |
| `person_source_value` | No | varchar(50) |  | Use this field to link back to persons in the source data. This is typically used for error checking of ETL logic. |
| `gender_source_value` | No | varchar(50) |  | This field is used to store the biological sex of the person from the source data. It is not intended for use in standard analytics but for reference only. |
| `gender_source_concept_id` | No | integer | FK CONCEPT | Due to the small number of options, this tends to be zero. |
| `race_source_value` | No | varchar(50) |  | This field is used to store the race of the person from the source data. It is not intended for use in standard analytics but for reference only. |
| `race_source_concept_id` | No | integer | FK CONCEPT | Due to the small number of options, this tends to be zero. |
| `ethnicity_source_value` | No | varchar(50) |  | This field is used to store the ethnicity of the person from the source data. It is not intended for use in standard analytics but for reference only. |
| `ethnicity_source_concept_id` | No | integer | FK CONCEPT | Due to the small number of options, this tends to be zero. |

## Prepared table

4 content concepts kept, 5 removed.

| Concept | OMOP fields | Kept | Reason |
|---|---|---|---|
| Gender | `gender_concept_id`, `gender_source_value`, `gender_source_concept_id` | yes | |
| Birth date | `year_of_birth`, `month_of_birth`, `day_of_birth`, `birth_datetime` | yes | |
| Race | `race_concept_id`, `race_source_value`, `race_source_concept_id` | yes | |
| Ethnicity | `ethnicity_concept_id`, `ethnicity_source_value`, `ethnicity_source_concept_id` | yes | |
| Record identifier | `person_id` | no | openEHR RM identifier. |
| Location | `location_id` | no | link to the location record. |
| Provider | `provider_id` | no | link to the recording provider. |
| Care site | `care_site_id` | no | link to the care site. |
| Person source identifier | `person_source_value` | no | openEHR EHR identifier. |

## Mapped archetypes

Archetypes whose OMOCL mapping targets this table.

### Single target table (1)

| Archetype | Mapping file |
|---|---|
| `openEHR-EHR-ADMIN_ENTRY.person_data.v0` | `person_data/person_data_v0.yml` |

### Several target tables (0)

None.

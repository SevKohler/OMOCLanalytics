# Death

Target table OMOP CDM v5.4 `DEATH`. The prepared table lists the content concepts we count archetype leafs against. See the README for how it is derived.

## CDM fields (7)

| Field | Required | Type | Key | Description |
|---|---|---|---|---|
| `person_id` | Yes | integer | FK PERSON |  |
| `death_date` | Yes | date |  | The date the person was deceased. |
| `death_datetime` | No | datetime |  |  |
| `death_type_concept_id` | No | integer | FK CONCEPT | This is the provenance of the death record, i.e., where it came from. It is possible that an administrative claims database would source death information from a government file so do not assume the Death Type is the same as the Visit Type, etc. |
| `cause_concept_id` | No | integer | FK CONCEPT | This is the Standard Concept representing the Person's cause of death, if available. |
| `cause_source_value` | No | varchar(50) |  |  |
| `cause_source_concept_id` | No | integer | FK CONCEPT |  |

## Prepared table

3 content concepts kept, 1 removed.

| Concept | OMOP fields | Kept | Reason |
|---|---|---|---|
| Death date/time | `death_date`, `death_datetime` | yes | |
| Death type / provenance | `death_type_concept_id` | yes | |
| Cause of death | `cause_concept_id`, `cause_source_value`, `cause_source_concept_id` | yes | |
| Person | `person_id` | no | link to the subject of care. |

## Mapped archetypes

Archetypes whose OMOCL mapping targets this table.

### Single target table (1)

| Archetype | Mapping file |
|---|---|
| `openEHR-EHR-EVALUATION.death_summary.v1` | `medical_data/evaluation/Death_summary_v1.yml` |

### Several target tables (0)

None.

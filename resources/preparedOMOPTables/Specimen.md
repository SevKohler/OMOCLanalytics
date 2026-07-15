# Specimen

Target table OMOP CDM v5.4 `SPECIMEN`. The prepared table lists the content concepts we count archetype leafs against. See the README for how it is derived.

## CDM fields (15)

| Field | Required | Type | Key | Description |
|---|---|---|---|---|
| `specimen_id` | Yes | integer | PK | Unique identifier for each specimen. |
| `person_id` | Yes | integer | FK PERSON | The person from whom the specimen is collected. |
| `specimen_concept_id` | Yes | integer | FK CONCEPT |  |
| `specimen_type_concept_id` | Yes | integer | FK CONCEPT |  |
| `specimen_date` | Yes | date |  | The date the specimen was collected. |
| `specimen_datetime` | No | datetime |  |  |
| `quantity` | No | float |  | The amount of specimen collected from the person. |
| `unit_concept_id` | No | integer | FK CONCEPT | The unit for the quantity of the specimen. |
| `anatomic_site_concept_id` | No | integer | FK CONCEPT | This is the site on the body where the specimen is from. |
| `disease_status_concept_id` | No | integer | FK CONCEPT |  |
| `specimen_source_id` | No | varchar(50) |  | This is the identifier for the specimen from the source system. |
| `specimen_source_value` | No | varchar(50) |  |  |
| `unit_source_value` | No | varchar(50) |  |  |
| `anatomic_site_source_value` | No | varchar(50) |  |  |
| `disease_status_source_value` | No | varchar(50) |  |  |

## Prepared table

7 content concepts kept, 3 removed.

| Concept | OMOP fields | Kept | Reason |
|---|---|---|---|
| Specimen concept | `specimen_concept_id`, `specimen_source_value` | yes | |
| Specimen type / provenance | `specimen_type_concept_id` | yes | |
| Specimen date/time | `specimen_date`, `specimen_datetime` | yes | |
| Quantity (DV_QUANTITY) | `quantity` | yes | |
| Anatomic site | `anatomic_site_concept_id`, `anatomic_site_source_value` | yes | |
| Disease status | `disease_status_concept_id`, `disease_status_source_value` | yes | |
| Specimen source identifier | `specimen_source_id` | yes | |
| Record identifier | `specimen_id` | no | openEHR RM identifier. |
| Person | `person_id` | no | link to the subject of care. |
| Unit | `unit_concept_id`, `unit_source_value` | no | RM attribute of the quantity (`DV_QUANTITY.units`). It is never mapped on its own in the OMOCL mappings, the quantity carries it. |

## Mapped archetypes

Archetypes whose OMOCL mapping targets this table.

### Single target table (2)

| Archetype | Mapping file |
|---|---|
| `openEHR-EHR-CLUSTER.specimen.v1` | `medical_data/cluster/Specimen_v1.yml` |
| `openEHR-EHR-EVALUATION.specimen_summary.v1` | `medical_data/evaluation/Specimen_summary_v1.yml` |

### Several target tables (0)

None.

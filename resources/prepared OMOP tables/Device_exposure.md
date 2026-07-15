# Device exposure

Target table OMOP CDM v5.4 `DEVICE_EXPOSURE`. The prepared table lists the content concepts we count archetype leafs against. See the README for how it is derived.

## CDM fields (19)

| Field | Required | Type | Key | Description |
|---|---|---|---|---|
| `device_exposure_id` | Yes | integer | PK | The unique key given to records a person's exposure to a foreign physical object or instrument. |
| `person_id` | Yes | integer | FK PERSON |  |
| `device_concept_id` | Yes | integer | FK CONCEPT | The DEVICE_CONCEPT_ID field is recommended for primary use in analyses, and must be used for network studies. This is the standard concept mapped from the source concept id which represents a foreign object or instrument the person was exposed to. |
| `device_exposure_start_date` | Yes | date |  | Use this date to determine the start date of the device record. |
| `device_exposure_start_datetime` | No | datetime |  |  |
| `device_exposure_end_date` | No | date |  | The DEVICE_EXPOSURE_END_DATE denotes the day the device exposure ended for the patient, if given. |
| `device_exposure_end_datetime` | No | datetime |  |  |
| `device_type_concept_id` | Yes | integer | FK CONCEPT | You can use the TYPE_CONCEPT_ID to denote the provenance of the record, as in whether the record is from administrative claims or EHR. |
| `unique_device_id` | No | varchar(255) |  | This is the Unique Device Identification (UDI-DI) number for devices regulated by the FDA, if given. |
| `production_id` | No | varchar(255) |  | This is the Production Identifier (UDI-PI) portion of the Unique Device Identification. |
| `quantity` | No | integer |  |  |
| `provider_id` | No | integer | FK PROVIDER | The Provider associated with device record, e.g. the provider who wrote the prescription or the provider who implanted the device. |
| `visit_occurrence_id` | No | integer | FK VISIT_OCCURRENCE | The Visit during which the device was prescribed or given. |
| `visit_detail_id` | No | integer | FK VISIT_DETAIL | The Visit Detail during which the device was prescribed or given. |
| `device_source_value` | No | varchar(50) |  | This field houses the verbatim value from the source data representing the device exposure that occurred. For example, this could be an NDC or Gemscript code. |
| `device_source_concept_id` | No | integer | FK CONCEPT | This is the concept representing the device source value and may not necessarily be standard. This field is discouraged from use in analysis because it is not required to contain Standard Concepts that are used across the OHDSI community, and should only be used when Standard Concepts do not adequately represent the source detail for the Device necessary for a given analytic use case. Consider using DEVICE_CONCEPT_ID instead to enable standardized analytics that can be consistent across the network. |
| `unit_concept_id` | No | integer | FK CONCEPT | UNIT_SOURCE_VALUES should be mapped to a Standard Concept in the Unit domain that best represents the unit as given in the source data. |
| `unit_source_value` | No | varchar(50) |  | This field houses the verbatim value from the source data representing the unit of the Device. For example, blood transfusions are considered devices and can be given in mL quantities. |
| `unit_source_concept_id` | No | integer | FK CONCEPT | This is the concept representing the UNIT_SOURCE_VALUE and may not necessarily be standard. This field is discouraged from use in analysis because it is not required to contain Standard Concepts that are used across the OHDSI community, and should only be used when Standard Concepts do not adequately represent the source detail for the Unit necessary for a given analytic use case. Consider using UNIT_CONCEPT_ID instead to enable standardized analytics that can be consistent across the network. |

## Prepared table

7 content concepts kept, 5 removed.

| Concept | OMOP fields | Kept | Reason |
|---|---|---|---|
| Device concept | `device_concept_id`, `device_source_value`, `device_source_concept_id` | yes | |
| Device exposure start date/time | `device_exposure_start_date`, `device_exposure_start_datetime` | yes | |
| Device exposure end date/time | `device_exposure_end_date`, `device_exposure_end_datetime` | yes | |
| Device type / provenance | `device_type_concept_id` | yes | |
| Unique device | `unique_device_id` | yes | |
| Production | `production_id` | yes | |
| Quantity (DV_QUANTITY) | `quantity` | yes | |
| Record identifier | `device_exposure_id` | no | openEHR RM identifier. |
| Person | `person_id` | no | link to the subject of care. |
| Provider | `provider_id` | no | link to the recording provider. |
| Visit | `visit_occurrence_id`, `visit_detail_id` | no | link to the encounter. |
| Unit | `unit_concept_id`, `unit_source_value`, `unit_source_concept_id` | no | RM attribute of the quantity (`DV_QUANTITY.units`). It is never mapped on its own in the OMOCL mappings, the quantity carries it. |

## Mapped archetypes

Archetypes whose OMOCL mapping targets this table.

### Single target table (1)

| Archetype | Mapping file |
|---|---|
| `openEHR-EHR-CLUSTER.device.v1` | `medical_data/cluster/Device_v1.yml` |

### Several target tables (0)

None.

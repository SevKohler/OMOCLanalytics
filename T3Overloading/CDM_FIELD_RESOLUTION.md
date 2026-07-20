# How OMOCL field names resolve to real OMOP CDM v5.4 columns

`overloading.py` counts overloading per **OMOCL field name** (`concept_id`, `value`, `unit`,
`observation_date`, ...). Those are not CDM column names. OMOCL **converges** several CDM columns
into one mapping slot, so a reviewer may reasonably ask whether the reported rate transfers to the
CDM. This file records the resolution, read out of the Eos implementation, and recomputes the rate
over real CDM columns.

Sources (all paths relative to the Eos repository, `github.com/BIH-CEI/Eos`):

- `setup/ddls/CDM54/OMOPCDM_postgresql_ddl.sql` — authoritative CDM v5.4 column names
- `src/main/java/org/bih/eos/converter/cdt/conversion_entities/*Entity.java` — the setters
- `src/main/java/org/bih/eos/converter/cdt/converter/configurable/generic/CDTConverterWith*Concept.java`
- `src/main/java/org/bih/eos/converter/cdm_field/CDMConverter.java` — alternative resolution
- `src/main/java/org/bih/eos/yaml/cdt_configs/**/` — which OMOCL fields exist per table

## Why alternatives overload a field at all

`CDMConverter.runConversion` walks the `alternatives:` list and **returns on the first one that
resolves**:

```java
for (ValueEntry valueEntry : valueEntries) {
    if (valueEntry.getCode() != null) {
        return convertCode(valueEntry.getCode());
    } else if (valueEntry.getPath() != null && PathProcessor.getItemAtPath(...).isPresent()) {
        Optional<T> convertedPath = convertPath(contentItem, valueEntry.getPath());
        if (convertedPath.isPresent()) { return convertedPath; }
    } else if (valueEntry.getConceptMap() != null && ...) {
        return convertConceptMap(contentItem, valueEntry.getConceptMap());
    }
}
```

Exactly **one** alternative wins per record, and which one wins depends on what the record happens
to contain. That is the mechanism the overloading measure captures: when two or more alternatives
are distinct source paths, the column holds different clinical notions in different records.

## The convergence rules

### `concept_id` → 2 or 3 columns (concept + source concept + source value)

`CDTConverterWithSourceConcept` writes all three, from the same resolved value:

```java
entity.setStandardConcept(standardConceptConverter.convert(contentItem, valueEntries));
entity.setSourceConcept(sourceConceptConverter.convert(contentItem, valueEntries));
entity.setEntitySourceValue(sourceValueConverter.convert(contentItem, valueEntries));
```

`CDTConverterWithStandardConcept` omits the middle line.

| OMOCL | CDM v5.4 columns | n |
|---|---|---|
| `ConditionOccurrence.concept_id` | `condition_concept_id`, `condition_source_concept_id`, `condition_source_value` | 3 |
| `DeviceExposure.concept_id` | `device_concept_id`, `device_source_concept_id`, `device_source_value` | 3 |
| `DrugExposure.concept_id` | `drug_concept_id`, `drug_source_concept_id`, `drug_source_value` | 3 |
| `Measurement.concept_id` | `measurement_concept_id`, `measurement_source_concept_id`, `measurement_source_value` | 3 |
| `Observation.concept_id` | `observation_concept_id`, `observation_source_concept_id`, `observation_source_value` | 3 |
| `ProcedureOccurrence.concept_id` | `procedure_concept_id`, `procedure_source_concept_id`, `procedure_source_value` | 3 |
| `Specimen.concept_id` | `specimen_concept_id`, `specimen_source_value` | 2 |
| `Visit.visit_concept` | `visit_concept_id` only | 1 |

`SpecimenEntity` and `VisitOccurrenceEntity` extend `EntityWithStandardConcept`; the other six
extend `EntityWithSourceConcept`.

`Visit.visit_concept` is a further exception: although `VisitOccurrenceEntity` extends
`EntityWithStandardConcept`, its `setEntitySourceValue` is a no-op (`//ignored field doesnt exist`)
and `VisitConverter.convertVisitConceptId` calls only `setStandardConcept`, so `visit_source_value`
is never written.

### Three more slots that fan out

Not every remaining slot is 1:1. These three write a companion column from the same value:

| OMOCL | CDM v5.4 columns | setter |
|---|---|---|
| `Person.birth_datetime` | `birth_datetime`, `month_of_birth`, `day_of_birth` | `PersonEntity.setBirthDateTime(dateTime, day, month)` |
| `DrugExposure.route_concept_id` | `route_concept_id`, `route_source_value` | `DrugExposureEntity.setRoute` |
| `ConditionOccurrence.condition_status_concept_id` | `condition_status_concept_id`, `condition_status_source_value` | `ConditionOccurrenceEntity.setStatus` |

### The identity default

The remaining nine slots resolve onto an identically named single column: `unique_device_id`,
`production_id`, `DrugExposure.quantity`, `Measurement.operator_concept_id`, `range_low`,
`range_high`, `Person.year_of_birth`, `Specimen.quantity`, `specimen_source_id`. Of these only
`year_of_birth` is overloaded, but all nine count toward the denominator.

### `value` → 3 or 4 columns (datatype dispatch)

Java method overloading picks the target column by openEHR datatype. `ObservationEntity`:

```java
public void setValue(OptionalDouble simpleMagnitude) {      // DV_QUANTITY / DV_COUNT
    ... jpaEntity.setValueAsNumber(magnitudeValue);
        jpaEntity.setValueSourceValue(magnitudeValue.toString()); }

public void setValue(Optional<String> value) {              // DV_TEXT
    ... jpaEntity.setValueAsString(valueValue);
        jpaEntity.setValueSourceValue(valueValue); }

public void setValue(Optional<Concept> concept, Optional<String> sourceValue) {  // DV_CODED_TEXT
    ... jpaEntity.setValueAsConcept(conceptValue);
        jpaEntity.setValueSourceValue(sourceCodeValue); }
```

| OMOCL | CDM v5.4 columns | n |
|---|---|---|
| `Observation.value` | `value_as_number`, `value_as_string`, `value_as_concept_id`, `value_source_value` | 4 |
| `Measurement.value` | `value_as_number`, `value_as_concept_id`, `value_source_value` | 3 |

MEASUREMENT has no `value_as_string` in the CDM; `MeasurementEntity.setValue(Optional<String>)`
accordingly writes only `value_source_value`.

### `*_date` → 2 columns (date + datetime)

`setDateTime` always writes both:

```java
populateFieldIfPresent(date, dateTimeValue -> {
    jpaEntity.setObservationDate(dateTimeValue);
    jpaEntity.setObservationDateTime(dateTimeValue); });
```

| OMOCL | CDM v5.4 columns |
|---|---|
| `Observation.observation_date` | `observation_date`, `observation_datetime` |
| `Measurement.measurement_date` | `measurement_date`, `measurement_datetime` |
| `ConditionOccurrence.condition_start_date` / `_end_date` | `condition_start_date`/`_datetime`, `condition_end_date`/`_datetime` |
| `DrugExposure.drug_exposure_start_date` / `_end_date` | `drug_exposure_start_date`/`_datetime`, `drug_exposure_end_date`/`_datetime` |
| `DeviceExposure.device_exposure_start_date` / `_end_date` | `device_exposure_start_date`/`_datetime`, `device_exposure_end_date`/`_datetime` |
| `ProcedureOccurrence.procedure_start_date` | **`procedure_date`**, `procedure_datetime` |
| `ProcedureOccurrence.procedure_end_date` | `procedure_end_date`, `procedure_end_datetime` |
| `Specimen.specimen_date` | `specimen_date`, `specimen_datetime` |
| `Death.death_date` | `death_date`, `death_datetime` |
| `Visit.start_datetime` / `end_datetime` | `visit_start_date`/`_datetime`, `visit_end_date`/`_datetime` |

Note `ProcedureOccurrence.procedure_start_date`: CDM v5.4 names that column `procedure_date`.

### `unit` and `qualifier`

| OMOCL | CDM v5.4 columns | n |
|---|---|---|
| `Measurement.unit` | `unit_concept_id`, `unit_source_concept_id`, `unit_source_value` | 3 |
| `Observation.unit` | `unit_concept_id`, `unit_source_value` | 2 |
| `Observation.qualifier` | `qualifier_concept_id`, `qualifier_source_value` | 2 |
| `Person.gender_concept` | `gender_concept_id`, `gender_source_value`, `gender_source_concept_id` | 3 |
| `Person.ethnicity_concept_id` | `ethnicity_concept_id`, `ethnicity_source_value`, `ethnicity_source_concept_id` | 3 |
| `Specimen.anatomic_site_concept` | `anatomic_site_concept_id`, `anatomic_site_source_value` | 2 |

### Fields with no CDM target

Four OMOCL fields used in the mapping library have no matching config property, no entity setter
and no CDM v5.4 column. They resolve to nothing:

| OMOCL field | writes in library | why |
|---|---|---|
| `Measurement.qualifier` | 17 | `MeasurementConfig` has no `qualifier`; MEASUREMENT has no qualifier column (that is OBSERVATION) |
| `Observation.range_low` | 1 | `ObservationConfig` has no `rangeLow`; OBSERVATION has no range columns (that is MEASUREMENT) |
| `Observation.range_high` | 1 | as above |
| `Observation.operator_concept_id` | 1 | `ObservationConfig` has no `operatorConceptId`; OBSERVATION has no operator column |
| `ProcedureOccurrence.procedure_end_date` | 4 | key never binds — see below |

The first four look like fields borrowed from the neighbouring table. None is overloaded, so they
do not affect the numerator.

`procedure_end_date` is different and does affect the result. The config property and the entity
setter both exist, but the field is named `procedureOccurrenceEndDate`
(`ProcedureOccurrenceConfig:14`) and keys are bound with `PropertyNamingStrategies.SNAKE_CASE`
(`ConversionAutoConfiguration:148`), so the bindable key is `procedure_occurrence_end_date`. No
`@JsonProperty` alias supplies `procedure_end_date` — the same class annotates
`procedure_start_date` explicitly (line 21) precisely because its name diverges. Unknown keys are
discarded by `@JsonIgnoreProperties(ignoreUnknown = true)` (`OmopMapping:19`). The library writes
`procedure_end_date` in 4 files and `procedure_occurrence_end_date` in 0, so
`ProcedureOccurrenceEntity.setEndDateTime` is never reached and neither `procedure_end_date` nor
`procedure_end_datetime` is ever written.

One of those 4 writes (`Procedure_screening_v1.yml`) has >=2 paths, so excluding the slot removes
two columns from the denominator and two from the numerator. This is a judgement call worth
stating: on the view that the mapping author plainly intended the key to bind — making this an Eos
defect rather than an absent mapping — the slot would count, giving **35 of 87 (40.2%)** with a
21/14 split. The figures above exclude it, following this analysis's criterion of counting the
columns the reference implementation actually writes.

## Effect on the reported rate

The 46 OMOCL fields resolve to **87 distinct CDM v5.4 columns**, out of 175 columns across the ten
tables the library targets.

A CDM column counts as overloaded when it is written from an overloaded OMOCL slot — that is, when
the mapping offers that column two or more distinct source paths. Every column in a fan-out
qualifies. For most the fan-out is unconditional: `setDateTime` writes `_date` **and** `_datetime`
from the same winning alternative, and the source-concept/source-value companions are written
alongside the standard concept, so all of them receive whichever source path won.

The `value_as_number` / `value_as_string` / `value_as_concept_id` triple is the one case where the
fan-out is exclusive rather than unconditional: the winning alternative's openEHR datatype selects
one of the three per record. All three are still counted, because all three are targets the slot's
alternatives can reach and the criterion is the alternatives the mapping declares, not which one
resolves at runtime. This is the same criterion used at slot level, where `Observation.value` counts
once without asking which of its paths resolves in a given record. Applying a stricter rule here
than elsewhere would be the inconsistency; a run restricted to unconditional fan-out gives 32
instead of 35.

| unit | overloaded / total | rate |
|---|---|---|
| **CDM v5.4 columns written** (headline) | **35 / 87** | **40.2%** |
| OMOCL mapping slots (robustness check) | 16 / 46 | 34.8% |
| CDM columns, all ten tables | 35 / 175 | 20.0% |

The two rates agree closely, so the result does not depend on the choice of unit. They are not
independent measurements: 87 columns is the 46 slots expanded, and both use the same overload
criterion. The agreement shows that overloaded slots fan out at roughly the average rate, not that
two methods converged.

Of the 35 overloaded columns, **21 are temporal** and **14 cross-semantic**. The share of all 175
columns is reported for reference only: it counts columns nothing writes to, which cannot be
overloaded by construction.

The 35 overloaded CDM v5.4 columns:

```
CONDITION_OCCURRENCE   condition_start_date, condition_start_datetime
DEVICE_EXPOSURE        device_concept_id, device_source_concept_id, device_source_value
                       device_exposure_start_date, device_exposure_start_datetime
                       device_exposure_end_date, device_exposure_end_datetime
DRUG_EXPOSURE          drug_exposure_start_date, drug_exposure_start_datetime
                       drug_exposure_end_date, drug_exposure_end_datetime
MEASUREMENT            measurement_date, measurement_datetime
OBSERVATION            observation_date, observation_datetime
                       qualifier_concept_id, qualifier_source_value, value_source_value
                       value_as_number, value_as_string, value_as_concept_id
PERSON                 ethnicity_concept_id, ethnicity_source_concept_id, ethnicity_source_value
                       year_of_birth
PROCEDURE_OCCURRENCE   procedure_date, procedure_datetime
                       procedure_end_date, procedure_end_datetime
SPECIMEN               specimen_concept_id, specimen_source_value
                       specimen_date, specimen_datetime
```

The 14 cross-semantic columns trace to five OMOCL slots in nine mapping files:
`Observation.value` (`Anatomical_location_v1`, `Person_v1`, `Gender_v1`,
`Smokeless_tobacco_summary_v1`, `Tobacco_smoking_summary_v1`), `Observation.qualifier`
(`Adverse_reaction_risk_v2`, four competing paths), `DeviceExposure.concept_id` (`Device_v1`),
`Specimen.concept_id` (`Specimen_v1`) and `Person.ethnicity_concept_id` (`person_data_v0`).

**Denominator asymmetry, stated rather than hidden.** A column enters the denominator as soon as
some slot writes it, before the >=2-path test. One slot, `Visit.visit_concept`, is fed only by a
constant `code:` alternative and so has no source paths at all: it can never enter the numerator,
yet contributes `visit_concept_id` to the denominator. This mirrors `overloading.py`, where the same
slot costs one field of the 46. The effect is conservative — it lowers the rate. Excluding it would
give 35 of 86 (40.7%) instead of 35 of 87 (40.2%). It is kept because "columns the library writes"
is the honest denominator, and a column written from a hard-coded constant is still a column
written.

**Robustness: the conceptMap skip does not suppress the count.** A field-write is skipped entirely
when any alternative is a `conceptMap`. That affects 7 slots and is visible in the data
(`Observation.value` assesses 100 of its 121 writes; `Observation.qualifier` 11 of 21, of which only
3 carry a path at all), so it looks like it could hide overloading. Re-running with the skip
disabled adds **zero** overloaded slots: no skipped write has >=2 distinct paths. Both the 16/46 and
the 35/87 figures are therefore insensitive to this choice.

**Reproducibility.** `overloading.py` in this folder computes every figure above and writes
`resources/overloading.csv`, `resources/cdm_overloading.csv` and `resources/README.md`. It verifies
every resolved column against the CDM v5.4 schema transcribed from the Eos DDL, and raises rather
than reporting if any column is unknown.

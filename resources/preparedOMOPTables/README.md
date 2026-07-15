# Prepared OMOP tables

These tables give a fair denominator for the openEHR to OMOP mapping loss analysis. For each OMOP CDM v5.4 table that OMOCL targets we list the content items the table can hold, counted the way an openEHR archetype would carry them, so we can compare archetype element leafs against them.

## How a prepared table is built

First we collapse the redundant OMOP columns. In OMOP a single item is spread over several columns, a standard `_concept_id`, a raw `_source_value`, a `_source_concept_id`, and for a value the `_as_number` and `_as_concept_id` variants. These belong to one concept and are collapsed together.

Then we drop the concepts that an archetype would not carry as a data leaf.

- openEHR Reference Model attributes. An openEHR data value already carries its unit (`DV_QUANTITY.units`), its comparator (`DV_QUANTIFIED.magnitude_status`, the OMOP operator) and its reference range (`DV_QUANTITY.reference_ranges`) inside itself, so these are not separate leafs. We checked this against the OMOCL mappings. Operator is always read from the value, and the unit is always taken from the value or a constant, the only exception being the unit in `adverse_reaction_risk_v1` which points to its own node.
- Record identifiers and links to other records, such as person, provider, visit, care site, location and the preceding visit.
- Deprecated columns (`measurement_time`, `dose_unit_source_value`) and duplicates (`verbatim_end_date`, which is only the end date as written in the source).

A qualifier is kept. Unlike the unit it maps to its own archetype node in most observation mappings, so it is a real leaf.

What remains is the set of content concepts each archetype leaf is counted against.

## Tables

| Table | Content concepts | Removed |
|---|---|---|
| [Measurement](Measurement.md) | 4 | 9 |
| [Observation](Observation.md) | 5 | 6 |
| [Drug exposure](Drug_exposure.md) | 11 | 6 |
| [Condition occurrence](Condition_occurrence.md) | 6 | 4 |
| [Procedure occurrence](Procedure_occurrence.md) | 6 | 4 |
| [Specimen](Specimen.md) | 7 | 3 |
| [Device exposure](Device_exposure.md) | 7 | 5 |
| [Visit occurrence](Visit_occurrence.md) | 6 | 5 |
| [Person](Person.md) | 4 | 5 |
| [Death](Death.md) | 3 | 1 |

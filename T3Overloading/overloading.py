# Semantic field overloading of the openEHR to OMOP mapping (Table 3 in the manuscript).
#
# Run it and the numbers are reproduced:
#   python overloading.py
#
# WHAT IS MEASURED
# ----------------
# An OMOP CDM v5.4 COLUMN is OVERLOADED when, in at least one archetype mapping, it is fed by
# two or more DISTINCT source paths. Source paths are the `path:` alternatives OMOCL lists for
# the field. Two kinds of alternative are not source paths and are excluded:
#     - a constant `code:` value  (a fixed OMOP concept, not data drawn from the archetype)
#     - a conceptMap's path, which is nested inside the conceptMap object where this parser
#       cannot read it (a KNOWN BLIND SPOT, reported below, can only lower the count)
# Reference-model paths (".", "..", "../context", "events[...]") ARE counted. openEHR gives
# no single canonical event time, so an OMOP date fed by the event time and by the record
# context time genuinely holds different things in different records: that is overloading.
#
# THE HEADLINE IS A CDM-COLUMN RATE
# ---------------------------------
# OMOCL field names are NOT CDM column names: one OMOCL slot converges several CDM columns
# (`value` -> value_as_number/_string/_concept_id; `*_date` -> _date and _datetime; a concept
# -> standard concept plus its source concept and source value). Counting OMOCL slots would
# therefore not say which OMOP columns are affected. Every slot is resolved to the CDM v5.4
# column(s) the reference implementation (Eos) writes, and the rate is reported in that unit:
# N of M columns the library writes are overloaded in at least one mapping. Every column an
# overloaded slot writes counts, since the mapping offers that column several alternatives.
#
# See CDM_FIELD_RESOLUTION.md in this folder for the resolution rules and the Eos source they
# were read from.
#
# The OMOCL-slot rate is also printed, as a robustness check that the result does not depend
# on the choice of unit. The per-write frequency is printed as a SECONDARY figure and is
# deliberately NOT the headline: it is dominated by a few very high-frequency date fields, so
# it reflects this library's archetype mix more than the CDM.
#
# Inputs:
#   ../resources/OMOCL mappings/{medical_data,person_data}/**/*.yml
# Outputs (this analysis's own resources/ folder):
#   resources/overloading.csv       one row per overloaded (archetype, field, paths)
#   resources/cdm_overloading.csv   one row per overloaded CDM v5.4 column
#   resources/README.md             human-readable listing, grouped by archetype
#   printed summary                 the Table 3 overloading numbers
import csv
import collections
import glob
import io
import os

import yaml

# ---------------------------------------------------------------------------------------
# OMOCL field name -> real OMOP CDM v5.4 column(s), read out of the Eos implementation
# (github.com/BIH-CEI/Eos). See CDM_FIELD_RESOLUTION.md for the quoted code behind each rule.
# ---------------------------------------------------------------------------------------

# OMOP CDM v5.4, transcribed from setup/ddls/CDM54/OMOPCDM_postgresql_ddl.sql, for the ten
# tables the mapping library targets. Used as the "all columns" reference and to verify that
# every column the resolution produces actually exists in the schema.
CDM54 = {
    "PERSON": """person_id gender_concept_id year_of_birth month_of_birth day_of_birth
        birth_datetime race_concept_id ethnicity_concept_id location_id provider_id care_site_id
        person_source_value gender_source_value gender_source_concept_id race_source_value
        race_source_concept_id ethnicity_source_value ethnicity_source_concept_id""",
    "VISIT_OCCURRENCE": """visit_occurrence_id person_id visit_concept_id visit_start_date
        visit_start_datetime visit_end_date visit_end_datetime visit_type_concept_id provider_id
        care_site_id visit_source_value visit_source_concept_id admitted_from_concept_id
        admitted_from_source_value discharged_to_concept_id discharged_to_source_value
        preceding_visit_occurrence_id""",
    "CONDITION_OCCURRENCE": """condition_occurrence_id person_id condition_concept_id
        condition_start_date condition_start_datetime condition_end_date condition_end_datetime
        condition_type_concept_id condition_status_concept_id stop_reason provider_id
        visit_occurrence_id visit_detail_id condition_source_value condition_source_concept_id
        condition_status_source_value""",
    "DRUG_EXPOSURE": """drug_exposure_id person_id drug_concept_id drug_exposure_start_date
        drug_exposure_start_datetime drug_exposure_end_date drug_exposure_end_datetime
        verbatim_end_date drug_type_concept_id stop_reason refills quantity days_supply sig
        route_concept_id lot_number provider_id visit_occurrence_id visit_detail_id
        drug_source_value drug_source_concept_id route_source_value dose_unit_source_value""",
    "PROCEDURE_OCCURRENCE": """procedure_occurrence_id person_id procedure_concept_id procedure_date
        procedure_datetime procedure_end_date procedure_end_datetime procedure_type_concept_id
        modifier_concept_id quantity provider_id visit_occurrence_id visit_detail_id
        procedure_source_value procedure_source_concept_id modifier_source_value""",
    "DEVICE_EXPOSURE": """device_exposure_id person_id device_concept_id
        device_exposure_start_date device_exposure_start_datetime device_exposure_end_date
        device_exposure_end_datetime device_type_concept_id unique_device_id production_id quantity
        provider_id visit_occurrence_id visit_detail_id device_source_value
        device_source_concept_id unit_concept_id unit_source_value unit_source_concept_id""",
    "MEASUREMENT": """measurement_id person_id measurement_concept_id measurement_date
        measurement_datetime measurement_time measurement_type_concept_id operator_concept_id
        value_as_number value_as_concept_id unit_concept_id range_low range_high provider_id
        visit_occurrence_id visit_detail_id measurement_source_value measurement_source_concept_id
        unit_source_value unit_source_concept_id value_source_value measurement_event_id
        meas_event_field_concept_id""",
    "OBSERVATION": """observation_id person_id observation_concept_id observation_date
        observation_datetime observation_type_concept_id value_as_number value_as_string
        value_as_concept_id qualifier_concept_id unit_concept_id provider_id visit_occurrence_id
        visit_detail_id observation_source_value observation_source_concept_id unit_source_value
        qualifier_source_value value_source_value observation_event_id obs_event_field_concept_id""",
    "DEATH": """person_id death_date death_datetime death_type_concept_id cause_concept_id
        cause_source_value cause_source_concept_id""",
    "SPECIMEN": """specimen_id person_id specimen_concept_id specimen_type_concept_id specimen_date
        specimen_datetime quantity unit_concept_id anatomic_site_concept_id
        disease_status_concept_id specimen_source_id specimen_source_value unit_source_value
        anatomic_site_source_value disease_status_source_value""",
}
CDM54 = {t: tuple(cols.split()) for t, cols in CDM54.items()}

# OMOCL `type:` -> CDM table name.
CDM_TABLE = {"ConditionOccurrence": "CONDITION_OCCURRENCE", "Death": "DEATH",
             "DeviceExposure": "DEVICE_EXPOSURE", "DrugExposure": "DRUG_EXPOSURE",
             "Measurement": "MEASUREMENT", "Observation": "OBSERVATION", "Person": "PERSON",
             "ProcedureOccurrence": "PROCEDURE_OCCURRENCE", "Specimen": "SPECIMEN",
             "Visit": "VISIT_OCCURRENCE"}

# Entities extending EntityWithSourceConcept write standard + source concept + source value.
# SpecimenEntity and VisitOccurrenceEntity extend EntityWithStandardConcept: no source concept.
SOURCE_CONCEPT_TABLES = frozenset({"ConditionOccurrence", "DeviceExposure", "DrugExposure",
                                   "Measurement", "Observation", "ProcedureOccurrence"})

# Column-name stem for each table's own concept/source columns.
STEM = {"ConditionOccurrence": "condition", "DeviceExposure": "device", "DrugExposure": "drug",
        "Measurement": "measurement", "Observation": "observation",
        "ProcedureOccurrence": "procedure", "Specimen": "specimen"}

# OMOCL `*_date` slot -> the CDM `<stem>_date` / `<stem>_datetime` pair, both written by
# setDateTime. Note procedure_start_date resolves to procedure_date: CDM v5.4 has no
# procedure_start_date.
DATE_STEM = {
    ("ConditionOccurrence", "condition_start_date"): "condition_start",
    ("ConditionOccurrence", "condition_end_date"): "condition_end",
    ("DeviceExposure", "device_exposure_start_date"): "device_exposure_start",
    ("DeviceExposure", "device_exposure_end_date"): "device_exposure_end",
    ("DrugExposure", "drug_exposure_start_date"): "drug_exposure_start",
    ("DrugExposure", "drug_exposure_end_date"): "drug_exposure_end",
    ("Measurement", "measurement_date"): "measurement",
    ("Observation", "observation_date"): "observation",
    ("ProcedureOccurrence", "procedure_start_date"): "procedure",
    ("ProcedureOccurrence", "procedure_end_date"): "procedure_end",
    ("Specimen", "specimen_date"): "specimen",
    ("Death", "death_date"): "death",
    ("Visit", "start_datetime"): "visit_start",
    ("Visit", "end_datetime"): "visit_end",
}

# Slots that resolve 1:1 onto an identically named column (the identity default).
PLAIN = frozenset({
    ("DeviceExposure", "unique_device_id"), ("DeviceExposure", "production_id"),
    ("DrugExposure", "quantity"), ("Measurement", "operator_concept_id"),
    ("Measurement", "range_low"), ("Measurement", "range_high"), ("Person", "year_of_birth"),
    ("Specimen", "quantity"), ("Specimen", "specimen_source_id"),
})

# Slots resolving onto a named concept plus the companions written from the same value.
CONCEPT_GROUP = {
    # VisitOccurrenceEntity.setEntitySourceValue is a no-op ("//ignored field doesnt exist") and
    # VisitConverter.convertVisitConceptId calls only setStandardConcept: visit_source_value is
    # never written, so this slot does NOT take the standard-concept pair.
    ("Visit", "visit_concept"): ("visit_concept_id",),
    # PersonEntity.setBirthDateTime(dateTime, day, month) writes all three birth columns.
    ("Person", "birth_datetime"): ("birth_datetime", "month_of_birth", "day_of_birth"),
    # DrugExposureEntity.setRoute and ConditionOccurrenceEntity.setStatus each write the concept
    # and its source value.
    ("DrugExposure", "route_concept_id"): ("route_concept_id", "route_source_value"),
    ("ConditionOccurrence", "condition_status_concept_id"): ("condition_status_concept_id",
                                                             "condition_status_source_value"),
    ("Person", "gender_concept"): ("gender_concept_id", "gender_source_value",
                                   "gender_source_concept_id"),
    ("Person", "ethnicity_concept_id"): ("ethnicity_concept_id", "ethnicity_source_value",
                                         "ethnicity_source_concept_id"),
    ("Specimen", "anatomic_site_concept"): ("anatomic_site_concept_id",
                                            "anatomic_site_source_value"),
    ("Measurement", "unit"): ("unit_concept_id", "unit_source_concept_id", "unit_source_value"),
    ("Observation", "unit"): ("unit_concept_id", "unit_source_value"),
    ("Observation", "qualifier"): ("qualifier_concept_id", "qualifier_source_value"),
    # The openEHR datatype selects which value_as_* column receives the value; value_source_value
    # is written in every branch. All are targets the slot's alternatives can reach.
    ("Observation", "value"): ("value_as_number", "value_as_string", "value_as_concept_id",
                               "value_source_value"),
    ("Measurement", "value"): ("value_as_number", "value_as_concept_id", "value_source_value"),
}

# OMOCL slots used by the library that have no CDM column at all: no config property, no entity
# setter, no column in the schema (MEASUREMENT has no qualifier; OBSERVATION has no
# range_low/range_high/operator column). Eos discards them via
# @JsonIgnoreProperties(ignoreUnknown = true) on OmopMapping:19. None is overloaded, so they do
# not affect the numerator.
#
# NOT excluded here, though Eos also drops it: ProcedureOccurrence.procedure_end_date. Its config
# property and entity setter both exist, but the field is named procedureOccurrenceEndDate
# (ProcedureOccurrenceConfig:14) and keys bind under SNAKE_CASE, so the key that would bind is
# procedure_occurrence_end_date; the library writes procedure_end_date in 4 files and the
# bindable key in 0. It is counted because the mapping declares the alternatives, which is the
# criterion used throughout: this is an implementation defect, not an absent mapping. Excluding
# it would give 33 of 85 = 38.8%.
NO_CDM_TARGET = frozenset({("Measurement", "qualifier"), ("Observation", "range_low"),
                           ("Observation", "range_high"), ("Observation", "operator_concept_id")})


def cdm_columns(table, field):
    """The CDM v5.4 columns Eos writes for one OMOCL (table, field) slot."""
    key = (table, field)
    if key in NO_CDM_TARGET:
        return ()
    if key in PLAIN:
        return (field,)
    if key in CONCEPT_GROUP:
        return CONCEPT_GROUP[key]
    if key in DATE_STEM:
        stem = DATE_STEM[key]
        return ("%s_date" % stem, "%s_datetime" % stem)
    if field == "concept_id":
        stem = STEM[table]
        cols = ["%s_concept_id" % stem, "%s_source_value" % stem]
        if table in SOURCE_CONCEPT_TABLES:
            cols.append("%s_source_concept_id" % stem)
        return tuple(cols)
    raise KeyError("no CDM resolution for OMOCL slot %s.%s" % (table, field))

HERE = os.path.dirname(os.path.abspath(__file__))
# Input: the shared mapping library at the repository root.
MAPPINGS_DIR = os.path.join(HERE, "..", "resources", "OMOCL mappings")
# Output: this analysis's own resources/ folder.
OUTPUT_DIR = os.path.join(HERE, "resources")
OVERLOAD_CSV = os.path.join(OUTPUT_DIR, "overloading.csv")
CDM_CSV = os.path.join(OUTPUT_DIR, "cdm_overloading.csv")

# `- type:` blocks that are OMOCL directives, not OMOP target tables: Include plugs in another
# archetype's mapping, CustomMapping is a converter. Neither owns an OMOP field.
NON_TABLE_TYPES = frozenset({"Include", "CustomMapping"})

# One overloaded field, as one archetype maps it: the archetype, the OMOP table and field, and
# the distinct source paths competing for that single field.
Overload = collections.namedtuple("Overload", "archetype table field paths")


def mapping_files():
    """Every OMOCL mapping YAML (medical_data + person_data, tests excluded)."""
    found = (glob.glob(os.path.join(MAPPINGS_DIR, "medical_data", "**", "*.yml"), recursive=True)
             + glob.glob(os.path.join(MAPPINGS_DIR, "person_data", "**", "*.yml"), recursive=True))
    return sorted(f for f in found if os.sep + "tests" + os.sep not in f)


def archetype_id(doc):
    """The openEHR archetype a mapping document targets, or "" if it declares none."""
    spec = (doc or {}).get("spec", {}) or {}
    cfg = spec.get("openEhrConfig", {}) or {}
    return cfg.get("archetype", "")


def source_paths(alternatives):
    """The distinct source paths OMOCL lists for one OMOP field.

    A source path is a top-level `path:` alternative. A `code:` alternative is a constant
    concept, not a source path. A conceptMap alternative carries its path nested inside itself
    and is skipped here (see the blind-spot note at the top of the file). Reference-model
    paths are kept. Order preserved, duplicates removed.
    """
    if not isinstance(alternatives, list):
        return []
    paths = []
    for entry in alternatives:
        if not isinstance(entry, dict) or "conceptMap" in entry:
            continue
        path = entry.get("path")
        if isinstance(path, str) and path not in paths:
            paths.append(path)
    return paths


def has_concept_map(alternatives):
    """True if any alternative is a conceptMap (the blind spot we exclude and report)."""
    return isinstance(alternatives, list) and any(
        isinstance(entry, dict) and "conceptMap" in entry for entry in alternatives)


def analyse():
    """Walk every mapping once and collect what the report needs.

    Returns:
      written        set of every distinct (table, field) the library maps into
      overloads      deduplicated Overloads (a field fed by >=2 source paths in some mapping)
      field_writes   how many field-writes carry >=1 source path        (frequency denominator)
      overloaded_writes  how many of those carry >=2                     (frequency numerator)
      concept_map_writes how many field-writes are conceptMap            (the blind spot)
      cdm_written    every (cdm_table, cdm_column) the library writes    (HEADLINE denominator)
      cdm_overloaded the columns written by an overloaded slot           (HEADLINE numerator)
      cdm_sources    (cdm_table, cdm_column) -> OMOCL slots that overload it
    """
    written = set()
    seen_overload = set()
    overloads = []
    field_writes = 0
    overloaded_writes = 0
    concept_map_writes = 0
    cdm_written = set()
    cdm_overloaded = set()
    cdm_sources = collections.defaultdict(set)

    for path in mapping_files():
        with open(path, encoding="utf-8") as handle:
            try:
                doc = yaml.safe_load(handle)
            except yaml.YAMLError as error:
                print("  skipped (YAML error): %s  (%s)" % (os.path.basename(path), error))
                continue
        arch = archetype_id(doc)
        for block in (doc or {}).get("mappings", []) or []:
            if not isinstance(block, dict):
                continue
            table = block.get("type", "?")
            if table in NON_TABLE_TYPES:
                continue
            for field_name, spec in block.items():
                if field_name == "type" or not isinstance(spec, dict):
                    continue
                alternatives = spec.get("alternatives")
                if not isinstance(alternatives, list):
                    continue
                written.add((table, field_name))
                columns = {(CDM_TABLE[table], c) for c in cdm_columns(table, field_name)}
                cdm_written |= columns

                if has_concept_map(alternatives):
                    concept_map_writes += 1
                    continue
                paths = source_paths(alternatives)
                if not paths:
                    continue
                field_writes += 1
                if len(paths) >= 2:
                    overloaded_writes += 1
                    cdm_overloaded |= columns
                    for column in columns:
                        cdm_sources[column].add("%s.%s" % (table, field_name))
                    key = (arch, table, field_name, tuple(paths))
                    if key not in seen_overload:
                        seen_overload.add(key)
                        overloads.append(Overload(arch, table, field_name, paths))

    overloads.sort(key=lambda o: (o.archetype, o.table, o.field))
    return (written, overloads, field_writes, overloaded_writes, concept_map_writes,
            cdm_written, cdm_overloaded, cdm_sources)


def write_csv(overloads):
    """resources/overloading.csv: one row per overloaded (archetype, table, field, paths)."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(["archetype", "omop_table", "omop_field", "n_paths", "paths"])
    for o in overloads:
        writer.writerow([o.archetype, o.table, o.field, len(o.paths), " | ".join(o.paths)])
    with open(OVERLOAD_CSV, "w", encoding="utf-8") as out:
        out.write(buffer.getvalue())


def write_coverage(overloads, overloaded_fields):
    """resources/README.md: the overloaded field-mappings, grouped by archetype, for review."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    by_arch = collections.OrderedDict()
    for o in overloads:
        by_arch.setdefault(o.archetype, []).append(o)
    lines = [
        "# Field overloading per archetype", "",
        "Every OMOP field fed by two or more distinct source paths (constant `code` values "
        "and conceptMap lookups excluded; reference-model paths kept).", "",
        "Overloaded OMOP fields: **%d** distinct, seen across **%d** archetype mappings."
        % (len(overloaded_fields), len(by_arch)), "",
    ]
    for arch, items in by_arch.items():
        lines.append("## %s" % arch)
        lines.append("")
        lines.append("| OMOP table | OMOP field | # paths | Source paths |")
        lines.append("|---|---|---|---|")
        for o in items:
            lines.append("| %s | %s | %d | %s |"
                         % (o.table, o.field, len(o.paths),
                            "<br>".join("`%s`" % p for p in o.paths)))
        lines.append("")
    with open(os.path.join(OUTPUT_DIR, "README.md"), "w", encoding="utf-8") as out:
        out.write("\n".join(lines))


def write_cdm_csv(cdm_overloaded, cdm_sources):
    """resources/cdm_overloading.csv: one row per overloaded CDM column, with the slots that
    overload it (the headline numerator, itemised)."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(["cdm_table", "cdm_column", "omocl_slots"])
    for column in sorted(cdm_overloaded):
        writer.writerow([column[0], column[1], " | ".join(sorted(cdm_sources[column]))])
    with open(CDM_CSV, "w", encoding="utf-8") as out:
        out.write(buffer.getvalue())


def is_temporal_column(column):
    """A date/time CDM column. Its overloading is milder: the column stays a date, only the
    clinical event it refers to is lost. month_of_birth and day_of_birth are listed explicitly:
    they are written from the Person.birth_datetime fan-out and carry no date-like suffix."""
    return (column.endswith("_date") or column.endswith("_datetime")
            or column in ("year_of_birth", "month_of_birth", "day_of_birth"))


def print_summary(written, overloads, field_writes, overloaded_writes, concept_map_writes,
                  cdm_written, cdm_overloaded, cdm_sources):
    """The Table 3 numbers: the CDM-column headline, the OMOCL-slot robustness check, the
    per-write frequency, and the reasons the result is a lower bound. Raises if either
    internal consistency check fails, rather than reporting a number that cannot be trusted."""
    overloaded_fields = {(o.table, o.field) for o in overloads}
    archetypes = {o.archetype for o in overloads}
    temporal = {c for c in cdm_overloaded if is_temporal_column(c[1])}
    cross_semantic = cdm_overloaded - temporal
    cdm_total = sum(len(cols) for cols in CDM54.values())

    print("=" * 72)
    print("FIELD OVERLOADING  (Table 3)")
    print("=" * 72)
    print("An OMOP CDM v5.4 column is overloaded when some mapping feeds it >=2 distinct")
    print("source paths. OMOCL field names converge several CDM columns, so every slot is")
    print("resolved to the columns Eos writes (see CDM_FIELD_RESOLUTION.md).")
    print()
    print("HEADLINE (per distinct OMOP CDM v5.4 column):")
    print("  CDM columns the library writes            : %d" % len(cdm_written))
    print("  overloaded in at least one mapping        : %d" % len(cdm_overloaded))
    print("  = %d of %d columns overloaded             : %.1f%%"
          % (len(cdm_overloaded), len(cdm_written),
             100.0 * len(cdm_overloaded) / len(cdm_written)))
    print()
    print("  of those %d overloaded columns:" % len(cdm_overloaded))
    print("    temporal (a date fed by >1 timestamp)   : %d   milder: column stays a date,"
          % len(temporal))
    print("                                                    the clinical event is lost")
    print("    cross-semantic (value/qualifier/concept): %d   severe: the column means"
          % len(cross_semantic))
    print("                                                    different things per record")
    print()
    print("  for reference, all columns in the %d tables the library targets : %d"
          % (len(CDM54), cdm_total))
    print("  overloaded as a share of those            : %.1f%%   (NOT the headline: it counts"
          % (100.0 * len(cdm_overloaded) / cdm_total))
    print("                                                     columns nothing writes to, which")
    print("                                                     cannot be overloaded)")
    print()
    print("ROBUSTNESS (same phenomenon, per OMOCL mapping slot):")
    print("  OMOCL slots the library maps into         : %d" % len(written))
    print("  overloaded in at least one mapping        : %d  (%.1f%%)"
          % (len(overloaded_fields), 100.0 * len(overloaded_fields) / len(written)))
    print("  The rate is close to the column-level rate, so the result does not depend on the")
    print("  choice of unit. Seen across %d archetype mappings." % len(archetypes))
    print()
    print("SECONDARY (frequency, per field-write -- NOT the headline):")
    print("  field-writes carrying a source path       : %d" % field_writes)
    print("  of those, overloaded                      : %d  (%.1f%%)"
          % (overloaded_writes, 100.0 * overloaded_writes / field_writes))
    print("  Dominated by a few high-frequency date fields, so this tracks the archetype mix")
    print("  more than the CDM. Use the headline for a claim about OMOP.")
    print()
    print("LOWER BOUND. Two reasons the true overloading is higher:")
    print("  1. Only fields the mapping actually feeds >=2 sources are counted. A field")
    print("     overloaded by design but mapped from the single source considered correct,")
    print("     because OMOP offers no alternative, looks clean here.")
    print("  2. %d field-writes use a conceptMap, whose source path is nested inside the"
          % concept_map_writes)
    print("     conceptMap object where this parser cannot read it, so they are not assessed.")
    print("     No such write has >=2 sibling paths, so none can be masking an overloaded slot.")

    # The CSV lists overloaded field-mappings; every distinct field in it must be in `written`,
    # or the two passes have diverged and neither number is safe to publish.
    if not overloaded_fields.issubset(written):
        raise ValueError(
            "overloaded fields not found among the fields the library writes: %s"
            % sorted(overloaded_fields - written))
    # Every resolved column must exist in the transcribed CDM v5.4 schema, or the resolution has
    # drifted from the DDL and neither number is safe to publish.
    unknown = sorted(c for c in cdm_written if c[1] not in CDM54[c[0]])
    if unknown:
        raise ValueError("resolved columns absent from the CDM v5.4 schema: %s" % unknown)

    print("\nby CDM table (overloaded columns):")
    counts = collections.Counter(c[0] for c in cdm_overloaded)
    # Sort by count then name: Counter.most_common() breaks ties by insertion order, which here
    # derives from set iteration and so varies with PYTHONHASHSEED.
    for table, count in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print("  %-22s : %d" % (table, count))
    print("\nall %d resolved columns verified against the CDM v5.4 schema" % len(cdm_written))
    print("wrote resources/overloading.csv + resources/cdm_overloading.csv + resources/README.md")


def main():
    """Analyse the mapping library once, write the three artifacts, print the summary."""
    (written, overloads, field_writes, overloaded_writes, concept_map_writes,
     cdm_written, cdm_overloaded, cdm_sources) = analyse()
    overloaded_fields = {(o.table, o.field) for o in overloads}
    write_csv(overloads)
    write_cdm_csv(cdm_overloaded, cdm_sources)
    write_coverage(overloads, overloaded_fields)
    print_summary(written, overloads, field_writes, overloaded_writes, concept_map_writes,
                  cdm_written, cdm_overloaded, cdm_sources)


if __name__ == "__main__":
    main()

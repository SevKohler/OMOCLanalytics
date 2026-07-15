# openEHR-EHR-EVALUATION.death_summary.v1

**Concept:** Death summary

**Primary OMOP table:** Death  |  **Leaves:** 18  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 17

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0092 | element | Date/time of death | `death_date` @ Death |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0010 | element | Manner of death |
| at0093 | element | Manner description |
| at0021 | element | Place category |
| at0109 | element | Place of death |
| at0054 | element | Age at death |
| at0119 | element | Place of injury |
| at0120 | element | Date of injury |
| at0121 | element | Activity at the time of injury |
| at0110 | element | Pregnancy context |
| at0106 | element | Days post partum |
| at0044 | element | Gestation at death |
| at0116 | element | Stillbirth context |
| at0105 | element | Comment |
| at0103 | element | Information source(s) |
| at0104 | slot | Date of death alternatives |
| at0100 | slot | Structured place of death |
| at0042 | slot | Additional details |

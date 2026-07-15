# openEHR-EHR-EVALUATION.adverse_reaction_risk.v1

**Concept:** Adverse reaction risk

**Primary OMOP table:** Observation  |  **Leaves:** 30  |  **Mapped to primary:** 4  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 26

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0002 | element | Substance | `value` @ Observation |
| at0063 | element | Status | `qualifier` @ Observation |
| at0058 | element | Reaction mechanism | `unit` @ Observation |
| at0027 | element | Reaction event > Onset of reaction | `observation_date` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0101 | element | Criticality |
| at0120 | element | Category |
| at0117 | element | Onset of last reaction |
| at0006 | element | Comment |
| at0010 | element | Reaction event > Specific substance |
| at0021 | element | Reaction event > Certainty |
| at0011 | element | Reaction event > Manifestation |
| at0012 | element | Reaction event > Reaction description |
| at0028 | element | Reaction event > Duration of reaction |
| at0089 | element | Reaction event > Severity of reaction |
| at0020 | element | Reaction event > Initial exposure |
| at0025 | element | Reaction event > Duration of exposure |
| at0106 | element | Reaction event > Route of exposure |
| at0018 | element | Reaction event > Exposure description |
| at0040 | element | Reaction event > Clinical management description |
| at0032 | element | Reaction event > Reaction comment |
| at0047 | element | Supporting clinical record information |
| at0044 | element | Reaction reported? |
| at0125 | element | Report summary > Date of report |
| at0048 | element | Report summary > Report comment |
| at0045 | element | Report summary > Adverse reaction report |
| at0029 | slot | Reaction event > Reaction details |
| at0096 | slot | Reaction event > Exposure details |
| at0119 | slot | Reaction event > Clinical management details |
| at0041 | slot | Reaction event > Reporting details |
| at0116 | slot | Reaction event > Information source |

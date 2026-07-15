# openEHR-EHR-CLUSTER.adverse_reaction_event.v1

**Concept:** Adverse reaction event

**Primary OMOP table:** Observation  |  **Leaves:** 19  |  **Mapped to primary:** 3  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 16

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0001 | element | Specific substance | `value` @ Observation |
| at0008 | element | Onset of reaction | `observation_date` @ Observation |
| at0015 | element | Initial exposure | `observation_date` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0002 | element | Certainty |
| at0006 | element | Manifestation |
| at0007 | element | Reaction description |
| at0009 | element | Duration of reaction |
| at0010 | element | Severity of reaction |
| at0016 | element | Duration of exposure |
| at0017 | element | Route of exposure |
| at0018 | element | Exposure description |
| at0020 | element | Clinical management description |
| at0025 | element | Supporting clinical record information |
| at0024 | element | Comment |
| at0014 | slot | Reaction details |
| at0019 | slot | Exposure details |
| at0021 | slot | Clinical management details |
| at0022 | slot | Reporting details |
| at0023 | slot | Information source |

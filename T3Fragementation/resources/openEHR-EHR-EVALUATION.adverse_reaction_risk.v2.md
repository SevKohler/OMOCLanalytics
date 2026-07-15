# openEHR-EHR-EVALUATION.adverse_reaction_risk.v2

**Concept:** Adverse reaction risk

**Primary OMOP table:** Observation  |  **Leaves:** 11  |  **Mapped to primary:** 7  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 4

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0002 | element | Substance | `value` @ Observation |
| at0130 | element | Active/inactive status | `qualifier` @ Observation |
| at0063 | element | Verification status | `qualifier` @ Observation |
| at0101 | element | Criticality | `qualifier` @ Observation |
| at0120 | element | Category | `qualifier` @ Observation |
| at0117 | element | Onset of last reaction | `observation_date` @ Observation |
| at0133 | element | Onset of first reaction | `observation_date` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0058 | element | Reaction mechanism |
| at0006 | element | Comment |
| at0047 | element | Supporting clinical record information |
| at0129 | slot | Reaction event summary |

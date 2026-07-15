# openEHR-EHR-EVALUATION.health_risk.v1

**Concept:** Health risk assessment

**Primary OMOP table:** Observation  |  **Leaves:** 15  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 14

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0013 | element | Risk factors > Risk factor | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0002 | element | Health risk |
| at0017 | element | Risk factors > Presence |
| at0014 | element | Risk factors > Description |
| at0029 | element | Risk factors > Date identified |
| at0028 | element | Risk factors > Mitigated |
| at0012 | element | Risk factors > Link to evidence |
| at0030 | element | Risk factors > Comment |
| at0003 | element | Risk assessment |
| at0020 | element | Assessment type |
| at0023 | element | Time period |
| at0004 | element | Rationale |
| at0015 | element | Comment |
| at0025 | element | Assessment method |
| at0027 | slot | Risk factors > Detail |

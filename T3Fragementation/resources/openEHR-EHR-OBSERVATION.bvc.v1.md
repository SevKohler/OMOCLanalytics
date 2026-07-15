# openEHR-EHR-OBSERVATION.bvc.v1

**Concept:** Brøset Violence Checklist (BVC)

**Primary OMOP table:** Observation  |  **Leaves:** 8  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 7

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0017 | element | Total score | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0004 | element | Confused |
| at0005 | element | Irritable |
| at0006 | element | Boisterous |
| at0008 | element | Physical threats |
| at0007 | element | Verbal threats |
| at0009 | element | Attacking objects |
| at0030 | element | Interpretation |

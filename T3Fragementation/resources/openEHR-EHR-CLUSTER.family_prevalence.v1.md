# openEHR-EHR-CLUSTER.family_prevalence.v1

**Concept:** Family prevalence

**Primary OMOP table:** Observation  |  **Leaves:** 9  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 8

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0030 | element | Description | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0055 | element | Genetic predisposition? |
| at0056 | element | Inheritance type |
| at0032 | element | Affected family > Relationship degree |
| at0057 | element | Affected family > Relationship category |
| at0051 | element | Affected family > Family line |
| at0033 | element | Affected family > Biological sex |
| at0034 | element | Affected family > Number affected |
| at0054 | element | Affected family > Number eligible |

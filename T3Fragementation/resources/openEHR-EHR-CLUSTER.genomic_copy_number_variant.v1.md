# openEHR-EHR-CLUSTER.genomic_copy_number_variant.v1

**Concept:** Genomic copy number variant

**Primary OMOP table:** Observation  |  **Leaves:** 5  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 4

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0003 | element | Total copy number | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0001 | element | Start |
| at0002 | element | End |
| at0005 | element | Copy number change type |
| at0004 | slot | Reference sequence |

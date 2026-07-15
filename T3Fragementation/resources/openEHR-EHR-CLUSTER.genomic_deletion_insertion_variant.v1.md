# openEHR-EHR-CLUSTER.genomic_deletion_insertion_variant.v1

**Concept:** Genomic deletion-insertion variant

**Primary OMOP table:** Observation  |  **Leaves:** 5  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 4

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0005 | element | Deleted sequence | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0001 | element | Start position |
| at0003 | element | End position |
| at0007 | element | Inserted sequence |
| at0008 | slot | Reference sequence |

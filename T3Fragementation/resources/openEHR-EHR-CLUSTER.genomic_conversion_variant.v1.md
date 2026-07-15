# openEHR-EHR-CLUSTER.genomic_conversion_variant.v1

**Concept:** Genomic conversion variant

**Primary OMOP table:** Observation  |  **Leaves:** 6  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 5

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0011 | slot | Converted reference sequence | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0003 | element | Start converted position |
| at0004 | element | End converted position |
| at0009 | element | Replacing sequence start position |
| at0010 | element | Replacing sequence end position |
| at0012 | slot | Replacing reference sequence |

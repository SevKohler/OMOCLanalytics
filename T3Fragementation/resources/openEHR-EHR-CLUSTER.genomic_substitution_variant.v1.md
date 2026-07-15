# openEHR-EHR-CLUSTER.genomic_substitution_variant.v1

**Concept:** Genomic substitution variant

**Primary OMOP table:** Observation  |  **Leaves:** 4  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 3

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0005 | element | New nucleotide | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0001 | element | Position substituted |
| at0003 | element | Reference nucleotide |
| at0006 | slot | Reference sequence |

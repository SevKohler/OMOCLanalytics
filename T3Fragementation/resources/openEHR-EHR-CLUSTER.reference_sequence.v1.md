# openEHR-EHR-CLUSTER.reference_sequence.v1

**Concept:** Reference sequence

**Primary OMOP table:** Measurement  |  **Leaves:** 6  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 5

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0048 | element | Reference genome assembly | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0019 | element | Source name |
| at0020 | element | Accession number |
| at0021 | element | Version number |
| at0022 | element | URL |
| at0023 | element | Chromosome label |

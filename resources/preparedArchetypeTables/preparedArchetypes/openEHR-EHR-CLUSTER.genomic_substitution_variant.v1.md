# openEHR-EHR-CLUSTER.genomic_substitution_variant.v1

**Concept:** Genomic substitution variant

**Category:** cluster

**Element leaves:** 3  |  **Cluster slot leaves:** 1  |  **Total leaves:** 4


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0001 | Position substituted | DV_COUNT |
| at0003 | Reference nucleotide | DV_TEXT |
| at0005 | New nucleotide | DV_TEXT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0006 | Reference sequence | openEHR-EHR-CLUSTER.reference_sequence(-[a-zA-Z0-9_]+)*.v1 |

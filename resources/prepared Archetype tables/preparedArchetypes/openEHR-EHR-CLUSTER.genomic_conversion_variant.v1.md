# openEHR-EHR-CLUSTER.genomic_conversion_variant.v1

**Concept:** Genomic conversion variant

**Category:** cluster

**Element leaves:** 4  |  **Cluster slot leaves:** 2  |  **Total leaves:** 6


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0003 | Start converted position | DV_COUNT |
| at0004 | End converted position | DV_COUNT |
| at0009 | Replacing sequence start position | DV_COUNT |
| at0010 | Replacing sequence end position | DV_COUNT |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0011 | Converted reference sequence | openEHR-EHR-CLUSTER.reference_sequence(-[a-zA-Z0-9_]+)*.v1 |
| at0012 | Replacing reference sequence | openEHR-EHR-CLUSTER.reference_sequence(-[a-zA-Z0-9_]+)*.v1 |

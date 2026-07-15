# openEHR-EHR-CLUSTER.genomic_variant_result.v1

**Concept:** Genomic variant result

**Category:** cluster

**Element leaves:** 32  |  **Cluster slot leaves:** 10  |  **Total leaves:** 42


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0101 | Variant | DV_PARSABLE |
| at0010 | DNA region name | DV_TEXT |
| at0099 | Distance from splicing site | DV_COUNT |
| at0011 | DNA change | DV_PARSABLE |
| at0012 | Amino acid change | DV_PARSABLE |
| at0013 | Amino acid change type | DV_CODED_TEXT / DV_TEXT |
| at0100 | RNA change | DV_PARSABLE |
| at0017 | Score | DV_QUANTITY |
| at0018 | Qualitative prediction | DV_TEXT |
| at0054 | Impact | DV_TEXT |
| at0020 | Gene symbol | DV_TEXT |
| at0021 | Gene name | DV_TEXT |
| at0056 | Copy number overlap | DV_PROPORTION |
| at0057 | Part of fusion | DV_CODED_TEXT |
| at0058 | ACMG classification | DV_CODED_TEXT |
| at0059 | Fusion exon | DV_COUNT |
| at0023 | Best transcript candidate | DV_TEXT |
| at0026 | Score | DV_QUANTITY |
| at0060 | Read depth | DV_COUNT |
| at0028 | Allele depth | DV_COUNT |
| at0047 | Allele frequency | DV_QUANTITY |
| at0031 | Population allele frequency | DV_QUANTITY |
| at0062 | Filter name | DV_TEXT |
| at0063 | Description | DV_TEXT |
| at0064 | Filter passed | DV_BOOLEAN |
| at0067 | Strand bias ratio | DV_QUANTITY |
| at0068 | Strand bias p-value | DV_QUANTITY |
| at0039 | Genotype | DV_TEXT |
| at0040 | Allelic state | DV_CODED_TEXT / DV_TEXT |
| at0041 | Genotype quality | DV_COUNT |
| at0069 | Genotype probability | DV_TEXT |
| at0070 | Specimen identifier | DV_IDENTIFIER / DV_URI |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0001 | Bioinformatic analysis workflow | openEHR-EHR-CLUSTER.knowledge_base_reference(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0002 | Reference genome | openEHR-EHR-CLUSTER.reference_sequence(-[a-zA-Z0-9_]+)*.v1 |
| at0102 | Variant identification | openEHR-EHR-CLUSTER.knowledge_base_reference(-[a-zA-Z0-9_]+)*.v1 |
| at0045 | Structured variant | openEHR-EHR-CLUSTER.genomic_deletion_insertion_variant(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.genomic_duplication_variant(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.genomic_inversion_variant(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.genomic_insertion_variant(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.genomic_conversion_variant(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.genomic_substitution_variant(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.genomic_copy_number_variant(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.genomic_repeated_sequence_variant(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.genomic_deletion_variant(-[a-zA-Z0-9_]+)*.v1 |
| at0009 | Transcript reference sequence | openEHR-EHR-CLUSTER.reference_sequence(-[a-zA-Z0-9_]+)*.v1 |
| at0016 | Predicted impact knowledge base | openEHR-EHR-CLUSTER.knowledge_base_reference(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0053 | Source | openEHR-EHR-CLUSTER.citation(-[a-zA-Z0-9_]+)*.v0 |
| at0025 | Conservation score knowledge base | openEHR-EHR-CLUSTER.knowledge_base_reference(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0030 | Population allele frequency knowledge base | openEHR-EHR-CLUSTER.knowledge_base_reference(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0098 | Additional details | any archetype |

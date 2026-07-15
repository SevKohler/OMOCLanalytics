# openEHR-EHR-CLUSTER.genomic_variant_result.v1

**Concept:** Genomic variant result

**Category:** cluster

**Element leaves:** 32  |  **Cluster slot leaves:** 10  |  **Total leaves:** 42


## Element leaves

| Code | Within cluster | Element | Value type |
|------|----------------|---------|------------|
| at0101 |  | Variant | DV_PARSABLE |
| at0010 | Transcript | DNA region name | DV_TEXT |
| at0099 | Transcript | Distance from splicing site | DV_COUNT |
| at0011 | Transcript | DNA change | DV_PARSABLE |
| at0012 | Transcript | Amino acid change | DV_PARSABLE |
| at0013 | Transcript | Amino acid change type | DV_CODED_TEXT / DV_TEXT |
| at0100 | Transcript | RNA change | DV_PARSABLE |
| at0017 | Transcript > Predicted impact | Score | DV_QUANTITY |
| at0018 | Transcript > Predicted impact | Qualitative prediction | DV_TEXT |
| at0054 | Transcript > Functional impact | Impact | DV_TEXT |
| at0020 | Transcript > Gene | Gene symbol | DV_TEXT |
| at0021 | Transcript > Gene | Gene name | DV_TEXT |
| at0056 | Transcript > Gene | Copy number overlap | DV_PROPORTION |
| at0057 | Transcript > Gene | Part of fusion | DV_CODED_TEXT |
| at0058 | Transcript | ACMG classification | DV_CODED_TEXT |
| at0059 | Transcript | Fusion exon | DV_COUNT |
| at0023 |  | Best transcript candidate | DV_TEXT |
| at0026 | Conservation | Score | DV_QUANTITY |
| at0060 |  | Read depth | DV_COUNT |
| at0028 |  | Allele depth | DV_COUNT |
| at0047 |  | Allele frequency | DV_QUANTITY |
| at0031 | Population allele frequency details | Population allele frequency | DV_QUANTITY |
| at0062 | VCF quality filter | Filter name | DV_TEXT |
| at0063 | VCF quality filter | Description | DV_TEXT |
| at0064 | VCF quality filter | Filter passed | DV_BOOLEAN |
| at0067 |  | Strand bias ratio | DV_QUANTITY |
| at0068 |  | Strand bias p-value | DV_QUANTITY |
| at0039 |  | Genotype | DV_TEXT |
| at0040 |  | Allelic state | DV_CODED_TEXT / DV_TEXT |
| at0041 |  | Genotype quality | DV_COUNT |
| at0069 |  | Genotype probability | DV_TEXT |
| at0070 |  | Specimen identifier | DV_IDENTIFIER / DV_URI |

## Cluster slot leaves

| Code | Within cluster | Slot | Allowed archetypes |
|------|----------------|------|--------------------|
| at0001 |  | Bioinformatic analysis workflow | openEHR-EHR-CLUSTER.knowledge_base_reference(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0002 |  | Reference genome | openEHR-EHR-CLUSTER.reference_sequence(-[a-zA-Z0-9_]+)*.v1 |
| at0102 |  | Variant identification | openEHR-EHR-CLUSTER.knowledge_base_reference(-[a-zA-Z0-9_]+)*.v1 |
| at0045 |  | Structured variant | openEHR-EHR-CLUSTER.genomic_deletion_insertion_variant(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.genomic_duplication_variant(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.genomic_inversion_variant(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.genomic_insertion_variant(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.genomic_conversion_variant(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.genomic_substitution_variant(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.genomic_copy_number_variant(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.genomic_repeated_sequence_variant(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.genomic_deletion_variant(-[a-zA-Z0-9_]+)*.v1 |
| at0009 | Transcript | Transcript reference sequence | openEHR-EHR-CLUSTER.reference_sequence(-[a-zA-Z0-9_]+)*.v1 |
| at0016 | Transcript > Predicted impact | Predicted impact knowledge base | openEHR-EHR-CLUSTER.knowledge_base_reference(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0053 | Transcript > Functional impact | Source | openEHR-EHR-CLUSTER.citation(-[a-zA-Z0-9_]+)*.v0 |
| at0025 | Conservation | Conservation score knowledge base | openEHR-EHR-CLUSTER.knowledge_base_reference(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0030 | Population allele frequency details | Population allele frequency knowledge base | openEHR-EHR-CLUSTER.knowledge_base_reference(-[a-zA-Z0-9_]+)*.v1 / openEHR-EHR-CLUSTER.device(-[a-zA-Z0-9_]+)*.v1 |
| at0098 |  | Additional details | any archetype |

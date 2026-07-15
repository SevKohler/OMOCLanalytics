# openEHR-EHR-CLUSTER.genomic_variant_result.v1

**Concept:** Genomic variant result

**Primary OMOP table:** Observation  |  **Leaves:** 42  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 41

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0101 | element | Variant | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0010 | element | Transcript > DNA region name |
| at0099 | element | Transcript > Distance from splicing site |
| at0011 | element | Transcript > DNA change |
| at0012 | element | Transcript > Amino acid change |
| at0013 | element | Transcript > Amino acid change type |
| at0100 | element | Transcript > RNA change |
| at0017 | element | Transcript > Predicted impact > Score |
| at0018 | element | Transcript > Predicted impact > Qualitative prediction |
| at0054 | element | Transcript > Functional impact > Impact |
| at0020 | element | Transcript > Gene > Gene symbol |
| at0021 | element | Transcript > Gene > Gene name |
| at0056 | element | Transcript > Gene > Copy number overlap |
| at0057 | element | Transcript > Gene > Part of fusion |
| at0058 | element | Transcript > ACMG classification |
| at0059 | element | Transcript > Fusion exon |
| at0023 | element | Best transcript candidate |
| at0026 | element | Conservation > Score |
| at0060 | element | Read depth |
| at0028 | element | Allele depth |
| at0047 | element | Allele frequency |
| at0031 | element | Population allele frequency details > Population allele frequency |
| at0062 | element | VCF quality filter > Filter name |
| at0063 | element | VCF quality filter > Description |
| at0064 | element | VCF quality filter > Filter passed |
| at0067 | element | Strand bias ratio |
| at0068 | element | Strand bias p-value |
| at0039 | element | Genotype |
| at0040 | element | Allelic state |
| at0041 | element | Genotype quality |
| at0069 | element | Genotype probability |
| at0070 | element | Specimen identifier |
| at0001 | slot | Bioinformatic analysis workflow |
| at0002 | slot | Reference genome |
| at0102 | slot | Variant identification |
| at0045 | slot | Structured variant |
| at0009 | slot | Transcript > Transcript reference sequence |
| at0016 | slot | Transcript > Predicted impact > Predicted impact knowledge base |
| at0053 | slot | Transcript > Functional impact > Source |
| at0025 | slot | Conservation > Conservation score knowledge base |
| at0030 | slot | Population allele frequency details > Population allele frequency knowledge base |
| at0098 | slot | Additional details |

# OMOCL analytics

Analytics for the paper *Bridging openEHR and OMOP: Expanded Mappings and Systematic
Analysis of Semantic and Structural Limitations in the OMOP CDM*.

This repository holds the prepared data and scripts used to measure the openEHR to OMOP
mapping loss, so the figures in the paper can be reproduced and audited.

## Contents

- `resources/prepared Archetype tables/` — the archetype side of the comparison: the leaf
  inventory (data ELEMENTs + CLUSTER slots) extracted from the mapped archetypes, plus the
  scripts that build and verify it (`extract_leaves.py`, `qa_leaves.py`).
- `resources/prepared OMOP tables/` — the OMOP CDM side: the content concepts each OMOP
  table can hold, counted the same way, to give a fair denominator.
- `resources/OMOCL mappings/` — the OMOCL archetype-to-CDM mappings the analysis is based on.

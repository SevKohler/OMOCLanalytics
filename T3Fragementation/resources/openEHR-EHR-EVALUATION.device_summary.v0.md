# openEHR-EHR-EVALUATION.device_summary.v0

**Concept:** Medical device summary

**Primary OMOP table:** -  |  **Leaves:** 13  |  **Mapped to primary:** 0  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 13

## Mapped to the primary record

_None._

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0020 | element | Device type |
| at0002 | element | Status |
| at0015 | element | Description |
| at0007 | element | Device details > Device name |
| at0008 | element | Device details > Start date |
| at0012 | element | Device details > Body site |
| at0014 | element | Device details > Description |
| at0009 | element | Device details > End date |
| at0023 | element | Device details > URI to original data |
| at0019 | element | Device details > Next review due |
| at0013 | slot | Device details > Structured body site |
| at0010 | slot | Device details > Structured detail |
| at0021 | slot | Device details > Multimedia |

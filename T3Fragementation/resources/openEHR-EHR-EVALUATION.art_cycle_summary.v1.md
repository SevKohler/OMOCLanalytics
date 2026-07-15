# openEHR-EHR-EVALUATION.art_cycle_summary.v1

**Concept:** Assisted reproduction treatment cycle summary

**Primary OMOP table:** ProcedureOccurrence  |  **Leaves:** 30  |  **Mapped to primary:** 2  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 28

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Start date | `procedure_start_date` @ ProcedureOccurrence |
| at0012 | element | Activities | `concept_id` @ ProcedureOccurrence |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0002 | element | Cycle sequence |
| at0003 | element | Cycle identifier |
| at0005 | element | Description |
| at0006 | element | Intent |
| at0021 | element | Donation received |
| at0026 | element | Hormone protocol |
| at0072 | element | Cumulative gonadotropin dose |
| at0073 | element | Duration of gonadotropin administration |
| at0042 | element | Number of oocytes collected |
| at0043 | element | Number of mature (M2) oocytes collected |
| at0044 | element | Number of oocytes attempted fertilized |
| at0071 | element | Number of 2PN zygotes |
| at0045 | element | Number of embryos transferred |
| at0046 | element | Transferred embryo quality |
| at0047 | element | Number of embryos frozen |
| at0048 | element | Number of oocytes frozen |
| at0049 | element | Number of embryos thawed |
| at0050 | element | Number of embryos surviving thaw |
| at0051 | element | Number of embryos biopsied |
| at0052 | element | Number of embryos surviving biopsy |
| at0034 | element | Cycle outcome |
| at0054 | element | Pregnancy test outcome |
| at0053 | element | Number of viable fetuses |
| at0058 | element | Complications > Condition |
| at0065 | element | Complications > Description |
| at0066 | element | Complications > Date of onset |
| at0067 | element | Comment |
| at0074 | slot | Additional details |

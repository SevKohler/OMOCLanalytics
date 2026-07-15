# openEHR-EHR-CLUSTER.dosage.v1

**Concept:** Dosage

**Primary OMOP table:** DrugExposure  |  **Leaves:** 10  |  **Mapped to primary:** 2  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 8

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0164 | element | Dosage sequence | `quantity` @ DrugExposure |
| at0144 | element | Dose amount | `quantity` @ DrugExposure |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0145 | element | Dose unit |
| at0135 | element | Dose formula |
| at0178 | element | Dose description |
| at0134 | element | Administration rate |
| at0102 | element | Administration duration |
| at0176 | element | Alternate dose amount |
| at0177 | element | Alternate dose unit |
| at0037 | slot | Daily timing |

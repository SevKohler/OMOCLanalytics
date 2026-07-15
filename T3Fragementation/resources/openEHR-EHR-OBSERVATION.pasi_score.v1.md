# openEHR-EHR-OBSERVATION.pasi_score.v1

**Concept:** Psoriasis Area Severity Index (PASI)

**Primary OMOP table:** Measurement  |  **Leaves:** 21  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 20

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0035 | element | Total PASI-score | `value` @ Measurement |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0005 | element | Head region (h) > Erythema (E) |
| at0011 | element | Head region (h) > Infiltration (I) |
| at0017 | element | Head region (h) > Desquamation (D) |
| at0023 | element | Head region (h) > Body surface area involvement (A) |
| at0038 | element | Head region (h) > Score head region |
| at0005 | element | Trunk region (t) > Erythema (E) |
| at0011 | element | Trunk region (t) > Infiltration (I) |
| at0017 | element | Trunk region (t) > Desquamation (D) |
| at0023 | element | Trunk region (t) > Body surface area involvement (A) |
| at0039 | element | Trunk region (t) > Score trunk region |
| at0005 | element | Upper extremities region (u) > Erythema (E) |
| at0011 | element | Upper extremities region (u) > Infiltration (I) |
| at0017 | element | Upper extremities region (u) > Desquamation (D) |
| at0023 | element | Upper extremities region (u) > Body surface area involvement (A) |
| at0040 | element | Upper extremities region (u) > Score upper extremities region |
| at0005 | element | Lower extremities region (l) > Erythema (E) |
| at0011 | element | Lower extremities region (l) > Infiltration (I) |
| at0017 | element | Lower extremities region (l) > Desquamation (D) |
| at0023 | element | Lower extremities region (l) > Body surface area involvement (A) |
| at0041 | element | Lower extremities region (l) > Score lower extremities region |

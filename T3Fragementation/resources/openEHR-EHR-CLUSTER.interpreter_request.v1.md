# openEHR-EHR-CLUSTER.interpreter_request.v1

**Concept:** Interpreter request

**Primary OMOP table:** Observation  |  **Leaves:** 6  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 5

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0003 | element | Kommentar | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0009 | element | Kommunikasjonskanal |
| at0035 | element | Per språk > Kommentar |
| at0027 | element | Foretrukket kjønn |
| at0031 | slot | Per språk > Språk |
| at0004 | slot | Foretrukket tolk |

# openEHR-EHR-OBSERVATION.laboratory_test_result.v1

**Concept:** Laboratory test result

**Primary OMOP table:** -  |  **Leaves:** 24  |  **Mapped to primary:** 0  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 24

## Mapped to the primary record

_None._

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0005 | element | Test name |
| at0073 | element | Overall test status |
| at0075 | element | Overall test status timestamp |
| at0077 | element | Diagnostic service category |
| at0100 | element | Clinical information provided |
| at0057 | element | Conclusion |
| at0098 | element | Test diagnosis |
| at0101 | element | Comment |
| at0113 | element | Confounding factors |
| at0068 | element | Laboratory internal identifier |
| at0106 | element | Test request details > Original test requested name |
| at0062 | element | Test request details > Requester order identifier |
| at0063 | element | Test request details > Receiver order identifier |
| at0111 | element | Point-of-care test |
| at0121 | element | Test method |
| at0065 | slot | Specimen detail |
| at0097 | slot | Test result |
| at0122 | slot | Structured test diagnosis |
| at0118 | slot | Multimedia representation |
| at0114 | slot | Structured confounding factors |
| at0017 | slot | Receiving laboratory |
| at0090 | slot | Test request details > Requester |
| at0035 | slot | Test request details > Distribution list |
| at0110 | slot | Testing details |

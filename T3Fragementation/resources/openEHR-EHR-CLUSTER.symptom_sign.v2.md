# openEHR-EHR-CLUSTER.symptom_sign.v2

**Concept:** Symptom/Sign

**Primary OMOP table:** ConditionOccurrence  |  **Leaves:** 36  |  **Mapped to primary:** 3  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 33

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0001 | element | Symptom/Sign name | `concept_id` @ ConditionOccurrence |
| at0152 | element | Episode onset | `condition_start_date` @ ConditionOccurrence |
| at0164 | element | Onset timing | `condition_start_date` @ ConditionOccurrence |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0151 | element | Body site |
| at0002 | element | Description |
| at0175 | element | Episodicity |
| at0186 | element | Occurrence |
| at0200 | element | Nadir |
| at0028 | element | Episode duration |
| at0021 | element | Severity category |
| at0189 | element | Character |
| at0180 | element | Progression |
| at0003 | element | Pattern |
| at0019 | element | Modifying factor > Factor |
| at0017 | element | Modifying factor > Effect |
| at0056 | element | Modifying factor > Description |
| at0170 | element | Precipitating factor > Factor |
| at0171 | element | Precipitating factor > Time interval |
| at0185 | element | Precipitating factor > Description |
| at0193 | element | Resolving factor > Factor |
| at0195 | element | Resolving factor > Time interval |
| at0196 | element | Resolving factor > Description |
| at0155 | element | Impact |
| at0037 | element | Episode description |
| at0161 | element | Resolution date/time |
| at0057 | element | Description of previous episodes |
| at0031 | element | Number of previous episodes |
| at0163 | element | Comment |
| at0147 | slot | Structured body site |
| at0198 | slot | Severity rating |
| at0197 | slot | Modifying factor > Factor detail |
| at0154 | slot | Precipitating factor > Factor detail |
| at0194 | slot | Resolving factor > Factor detail |
| at0153 | slot | Specific details |
| at0146 | slot | Previous episodes |
| at0063 | slot | Associated symptom/sign |

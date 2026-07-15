# openEHR-EHR-OBSERVATION.imaging_exam_result.v1

**Concept:** Imaging examination result

**Primary OMOP table:** ConditionOccurrence  |  **Leaves:** 47  |  **Mapped to primary:** 2  |  **Externalised to a separate record:** 1  |  **Not mapped (auxiliary):** 44

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0070 | element | Study date | `condition_start_date` @ ConditionOccurrence |
| at0058 | element | Imaging differential diagnosis | `concept_id` @ ConditionOccurrence |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0020 | element | Imaging diagnosis | `concept_id` @ ConditionOccurrence |

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0004 | element | Study name |
| at0091 | element | Modality |
| at0055 | element | Target body site |
| at0072 | element | Overall result status |
| at0071 | element | Status timestamp |
| at0061 | element | Clinical indication |
| at0014 | element | Clinical summary |
| at0008 | element | Imaging findings |
| at0056 | element | Comparison findings |
| at0063 | element | Imaging quality |
| at0057 | element | Imaging quality description |
| at0021 | element | Overall impression |
| at0059 | element | Recommendation |
| at0023 | element | Comment |
| at0048 | element | Confounding factors |
| at0108 | element | Position |
| at0092 | element | Study instance identifier |
| at0105 | element | Study description |
| at0104 | element | Report identifier |
| at0099 | element | Study status |
| at0098 | element | Study end point |
| at0106 | element | Image details |
| at0087 | element | Technique |
| at0049 | element | Technique summary |
| at0088 | element | Procedure |
| at0062 | element | Procedure summary |
| at0094 | element | Comparison study details > Study name |
| at0095 | element | Comparison study details > Study identifier |
| at0096 | element | Comparison study details > Study date |
| at0097 | element | Comparison study details > Study end point |
| at0031 | element | Examination request details > Receiver order identifier |
| at0028 | element | Examination request details > Requester order identifier |
| at0029 | element | Examination request details > Examination requested name |
| at0006 | slot | Structured target body site |
| at0044 | slot | Structured imaging findings |
| at0045 | slot | Report representation |
| at0107 | slot | Stabilising appliance |
| at0026 | slot | Imaging service |
| at0041 | slot | Structured technique/procedure |
| at0065 | slot | Series details |
| at0069 | slot | Device |
| at0067 | slot | Comparison study details > Comparison series details |
| at0030 | slot | Examination request details > Requester |
| at0083 | slot | Distribution list |

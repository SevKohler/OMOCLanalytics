# openEHR-EHR-ADMIN_ENTRY.episode_institution.v0

**Concept:** Admission

**Primary OMOP table:** Visit  |  **Leaves:** 25  |  **Mapped to primary:** 2  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 23

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0004 | element | Admission date | `start_datetime` @ Visit |
| at0002 | element | Discharge date | `end_datetime` @ Visit |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0014 | element | Admission ID |
| at0008 | element | Reason for admission |
| at0009 | element | Admission category |
| at0007 | element | Source category |
| at0028 | element | Referral ID |
| at0016 | element | Medical record number |
| at0026 | element | Health insurance category |
| at0021 | element | Attending unit |
| at0019 | element | Physical location > Location onset |
| at0025 | element | Physical location > Location category |
| at0022 | element | Physical location > Ward |
| at0023 | element | Physical location > Room |
| at0024 | element | Physical location > Bed |
| at0020 | element | Physical location > Location end |
| at0006 | element | Outcome |
| at0003 | element | Destination category |
| at0010 | element | Comment |
| at0013 | slot | Source |
| at0027 | slot | Referring clinician |
| at0015 | slot | Attending clinicians |
| at0017 | slot | Physical location > Location |
| at0012 | slot | Destination |
| at0011 | slot | Additional details |

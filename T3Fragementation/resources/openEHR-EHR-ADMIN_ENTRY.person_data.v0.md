# openEHR-EHR-ADMIN_ENTRY.person_data.v0

**Concept:** Personendaten

**Primary OMOP table:** Person  |  **Leaves:** 8  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 7

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0028 | slot | Details zur Geburt | `year_of_birth` @ Person, `birth_datetime` @ Person |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0008 | element | Art der Person |
| at0025 | element | Angaben zum Tod > Verstorben? |
| at0026 | slot | Personenname |
| at0013 | slot | Angaben zum Tod > Details zum Tod |
| at0005 | slot | Adresse |
| at0031 | slot | Kontaktangaben |
| at0007 | slot | Erweiterungen |

# openEHR-EHR-ADMIN_ENTRY.person_data.v0

**Concept:** Personendaten

**Category:** entry

**Element leaves:** 2  |  **Cluster slot leaves:** 6  |  **Total leaves:** 8


## Element leaves

| Code | Element | Value type |
|------|---------|------------|
| at0008 | Art der Person | DV_CODED_TEXT / DV_TEXT |
| at0025 | Verstorben? | DV_BOOLEAN |

## Cluster slot leaves

| Code | Slot | Allowed archetypes |
|------|------|--------------------|
| at0026 | Personenname | .* / openEHR-EHR-CLUSTER.person_name.v0 |
| at0028 | Details zur Geburt | .* / openEHR-EHR-CLUSTER.person_birth_data_iso.v0 |
| at0013 | Details zum Tod | .* / openEHR-EHR-CLUSTER.death_details.v1 |
| at0005 | Adresse | .* / openEHR-EHR-CLUSTER.address_cc.v0 |
| at0031 | Kontaktangaben | .* / openEHR-EHR-CLUSTER.telecom_details.v0 |
| at0007 | Erweiterungen | any archetype |

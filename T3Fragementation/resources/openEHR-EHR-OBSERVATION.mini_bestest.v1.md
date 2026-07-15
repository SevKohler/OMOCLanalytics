# openEHR-EHR-OBSERVATION.mini_bestest.v1

**Concept:** Mini-Balance Evaluation Systems Test (Mini-BESTest)

**Primary OMOP table:** Observation  |  **Leaves:** 31  |  **Mapped to primary:** 1  |  **Externalised to a separate record:** 0  |  **Not mapped (auxiliary):** 30

## Mapped to the primary record

| Code | Kind | Leaf | OMOP field |
|------|------|------|------------|
| at0100 | element | Total score | `value` @ Observation |

## Auxiliary — externalised to a separate OMOP record (another instance of the same table, or a different table; see the OMOP field column)

_None._

## Auxiliary — not mapped (needs a fact_relationship)

| Code | Kind | Leaf |
|------|------|------|
| at0006 | element | Anticipatory > 1. Sit to stand |
| at0010 | element | Anticipatory > 2. Rise to toes |
| at0024 | element | Anticipatory > 3. Stand on one leg > Time left leg trial 1 |
| at0025 | element | Anticipatory > 3. Stand on one leg > Time left leg trial 2 |
| at0016 | element | Anticipatory > 3. Stand on one leg > Left stand on one leg |
| at0026 | element | Anticipatory > 3. Stand on one leg > Time right leg trial 1 |
| at0027 | element | Anticipatory > 3. Stand on one leg > Time right leg trial 2 |
| at0020 | element | Anticipatory > 3. Stand on one leg > Right stand on one leg |
| at0028 | element | Anticipatory > Sub score |
| at0030 | element | Reactive postural control > 4. Compensatory stepping correction - forward |
| at0034 | element | Reactive postural control > 5. Compensatory stepping correction - backward |
| at0040 | element | Reactive postural control > 6. Compensatory stepping correction - lateral > Left |
| at0044 | element | Reactive postural control > 6. Compensatory stepping correction - lateral > Right |
| at0052 | element | Reactive postural control > Sub score |
| at0102 | element | Sensory orientation > Stance time - eyes open |
| at0056 | element | Sensory orientation > 7. Stance (feet together); eyes open, firm surface |
| at0103 | element | Sensory orientation > Stance time - eyes closed |
| at0060 | element | Sensory orientation > 8. Stance (feet together); eyes closed, foam surface |
| at0104 | element | Sensory orientation > Incline time |
| at0064 | element | Sensory orientation > 9. Incline - eyes closed |
| at0068 | element | Sensory orientation > Sub score |
| at0070 | element | Dynamic gait > 10. Change in gait speed |
| at0079 | element | Dynamic gait > 11. Walk with head turns - horizontal |
| at0074 | element | Dynamic gait > 12. Walk with pivot turns |
| at0083 | element | Dynamic gait > 13. Step over obstacles |
| at0097 | element | Dynamic gait > 14. Timed up & go with dual task [3 meter walk] > Time TUG |
| at0098 | element | Dynamic gait > 14. Timed up & go with dual task [3 meter walk] > Time Dual Task TUG |
| at0105 | element | Dynamic gait > 14. Timed up & go with dual task [3 meter walk] > Speed change |
| at0093 | element | Dynamic gait > 14. Timed up & go with dual task [3 meter walk] > Dual Task TUG |
| at0099 | element | Dynamic gait > Sub score |

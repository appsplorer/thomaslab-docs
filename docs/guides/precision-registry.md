# Precision-medicine and registry workflows

Version 0.9 connects the previously separate EHR, medication, PGx, temporal, and outcome layers into reusable patient-level registry workflows.

## Design principle

The registry layer is **event-definition agnostic**. The library does not contain hidden PCI/ACS code lists. A study supplies reviewed procedure/diagnosis code sets, index-event rules, PGx linkage rules, and follow-up windows.

```text
canonical person
      +
index events
      +
PGx result
      +
baseline clinical features
      +
medication summary
      +
outcome summary
      ↓
precision registry / analysis dataset
```

## Build an index event

```python
from thomaslab.registry import build_index_event

index = build_index_event(
    procedures,
    patient_col="patient_id",
    date_col="event_date",
    event_col="procedure_code",
    allowed_events=reviewed_pci_codes,
    selection="first",
)
```

`allowed_events` is an explicit study artifact. The library does not decide which codes define PCI.

## Link PGx to the index event

```python
from thomaslab.registry import link_index_event_to_pgx

linked = link_index_event_to_pgx(
    index,
    pgx_results,
    max_abs_days=30,
)
```

The output records `pgx_days_from_index` so the temporal relationship stays auditable.

## Classify study-defined indications

```python
from thomaslab.registry import classify_index_indication

indication = classify_index_indication(
    diagnoses,
    index,
    patient_col="patient_id",
    diagnosis_date_col="event_date",
    code_col="icd_code",
    code_sets={
        "acs": reviewed_acs_codes,
        "stemi": reviewed_stemi_codes,
        "nstemi": reviewed_nstemi_codes,
    },
)
```

## Follow-up schedule

```python
schedule = build_followup_schedule(
    registry,
    target_days=[30, 180, 365],
)
```

`validate_registry_followup` links observed follow-ups to planned targets using a configurable tolerance.

## Precision patient representation

`PrecisionPatient` is a small serializable research object for a single patient. For cohort analysis, use `build_precision_dataset`, which prefixes domains to prevent silent column collisions.

## Important limitations

- A registry contract proves structure, not that a code set is clinically valid.
- PGx linkage by nearest date is a temporal association rule, not proof that the test caused the index treatment.
- Multiple PGx results per patient must be reduced according to a prespecified study rule before a one-row-per-patient merge.
- Follow-up windows and outcome definitions remain protocol-specific.

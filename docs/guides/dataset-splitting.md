# Study dataset construction and validation splitting

Version 0.12 separates cohort construction from model training.

## Dataset construction

Use explicit index dates and temporal windows:

```python
from thomaslab.dataset import apply_lookback_window, create_time_to_event_dataset

baseline = apply_lookback_window(events, index, lookback_days=365)
survival = create_time_to_event_dataset(index, outcomes, fixed_followup_days=365)
```

`join_patient_domains` requires one row per patient for every static domain and uses provenance prefixes if column names collide.

## Splitting

For EHR data, row-level random splitting is usually unsafe because repeated rows from one patient can cross folds.

Use one of:

- `patient_level_split`
- `grouped_split`
- `temporal_split`
- `site_holdout_split`
- `stratified_group_split`
- `grouped_cv_folds`
- `external_validation_split`

A site holdout is a transportability design feature; the function does not itself prove that a dataset is an independent external validation cohort.

## Recommended order

```text
canonical inputs
→ cohort/index
→ baseline/follow-up windows
→ analysis dataset
→ split assignment
→ leakage audit
→ modeling
```

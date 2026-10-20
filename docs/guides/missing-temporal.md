# Missing data and temporal EHR workflows

Version 0.6 separates two problems that are often mixed together in EHR studies: **why a value is absent** and **when an observed value occurred relative to time zero**.

## Missingness workflow

```python
from thomaslab.missing import generate_missingness_report

report = generate_missingness_report(
    cohort,
    site_col="site_id",
    date_col="event_date",
    columns=["creatinine", "hemoglobin", "bmi"],
)
```

Inspect overall, site-specific, and temporal patterns before selecting an imputation method.
`detect_structural_missingness` is deliberately described as a heuristic: a variable can be absent at one site because it was not collected, because the extract omitted it, or because of a clinical/workflow process. Observed data alone do not establish MCAR, MAR, or MNAR.

## Imputation

`simple_impute` is transparent and appropriate for baselines/sensitivity checks when justified. `iterative_impute_clinical` creates one deterministic completed numeric dataset; it is **not** equivalent to formal multiple imputation with Rubin's rules. `longitudinal_impute` can carry values within a patient trajectory with a maximum allowed time gap.

Use `compare_imputation_strategies` only as a reconstruction diagnostic on artificially masked observed values. It does not choose the correct missing-data model for the study.

## Temporal alignment

```python
from thomaslab.temporal import assign_time_zero, generate_temporal_features

labs = assign_time_zero(labs, index_table)
features = generate_temporal_features(
    labs,
    feature_col="lab_name",
    value_col="lab_value",
    windows=[30, 90, 365],
    aggregations=["latest", "mean", "min", "max", "count", "slope"],
)
```

The feature generator uses **pre-index observations only**. Use `detect_future_information` before modeling to identify timestamps beyond the protocol's allowed boundary.

## Follow-up and censoring

Use `calculate_time_to_event` and `censor_followup` to make first-event and censoring rules explicit. A censor date before index is rejected.

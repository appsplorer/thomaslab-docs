# Publication reporting

## Table 1

```python
from thomaslab.viz import generate_table_one

text = generate_table_one(
    cohort,
    group_col="treatment",
    categorical_cols=["sex", "diabetes"],
    continuous_cols=["age", "egfr"],
)
print(text)
```

The utility returns Markdown and LaTeX representations. Statistical tests should match the manuscript analysis plan; Table 1 p-values are not a substitute for covariate-balance diagnostics in propensity analyses.

## ROC and precision-recall curves

```python
from thomaslab.viz import plot_roc_pr_curves

plot_roc_pr_curves(y_true, y_pred_prob, "figures/roc_pr.svg")
```

## Calibration

```python
from thomaslab.viz import plot_calibration_curve

plot_calibration_curve(y_true, y_pred_prob, "figures/calibration.svg")
```

## Kaplan-Meier

```python
from thomaslab.viz import plot_kaplan_meier

plot_kaplan_meier(
    survival_df,
    time_col="days",
    event_col="event",
    group_col="treatment",
    save_path="figures/km.svg",
)
```

The Kaplan-Meier plot includes an at-risk table. For adjusted causal effects, pair descriptive KM curves with the protocol-specified adjusted model rather than interpreting crude curves as adjusted treatment effects.

## Additional publication figures

- `plot_sankey_treatment_pathways` collapses consecutive duplicate medications and visualizes staged treatment transitions.
- `plot_forest_subgroups` creates 300-DPI subgroup effect/HR forest plots with confidence intervals.
- `plot_cumulative_incidence_competing` uses the Aalen-Johansen estimator so competing causes are not treated as ordinary censoring.

# Evaluation & fairness

## Classification performance

```python
from thomaslab.eval import calculate_clinical_metrics

metrics = calculate_clinical_metrics(y_true, y_pred_prob, threshold=0.5)
```

Returned measures include sensitivity, specificity, PPV, NPV, AUROC, and AUPRC.

## Calibration

```python
from thomaslab.eval import compute_calibration

cal = compute_calibration(y_true, y_pred_prob, n_bins=10)
```

Calibration should be assessed independently from discrimination. The module reports Brier score plus calibration intercept/slope and grouped observed/expected information.

## Decision-curve analysis

```python
from thomaslab.eval import decision_curve_analysis

dca = decision_curve_analysis(y_true, y_pred_prob)
```

Net benefit at threshold probability \(p_t\) is computed as:

\[
NB = \frac{TP}{N} - \frac{FP}{N}\left(\frac{p_t}{1-p_t}\right)
\]

Decision curves are only meaningful over clinically plausible threshold ranges.

## Group audits

```python
from thomaslab.eval import audit_fairness

by_group = audit_fairness(
    predictions,
    y_true_col="outcome",
    y_pred_prob_col="risk",
    demographic_col="race",
)
```

Treat group comparisons as an audit, not a single fairness verdict. Small groups can produce unstable estimates; report sample sizes and uncertainty where possible.

## SHAP

```python
from thomaslab.eval import explain_model_shap

explanation = explain_model_shap(model, X_test)
```

SHAP explains model behavior; it does not establish causal effects of predictors.

## Drift, uncertainty, and incremental value

`compute_population_stability_index` reports PSI for numeric/categorical features, Wasserstein distance for numeric variables, and missingness drift.

`bootstrap_confidence_intervals_fast` performs paired deterministic bootstrap resampling through joblib. Record the seed, replicate count, confidence level, and metric implementation in the manuscript analysis configuration.

`calculate_idi_and_nri` reports binary-outcome IDI and category-free continuous NRI. These measures should complement—not replace—discrimination, calibration, and decision-curve analysis.

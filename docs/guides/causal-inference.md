# Causal inference

`thomaslab.causal` provides building blocks for observational treatment-effect analyses. The functions do not replace study-design reasoning.

## Propensity scores

```python
from thomaslab.causal import calculate_propensity_scores

cohort["ps"] = calculate_propensity_scores(
    cohort,
    treatment_col="treated",
    covariates=["age", "sex", "egfr", "diabetes", "prior_mi"],
)
```

The current estimator uses regularized logistic regression with preprocessing for numeric and categorical covariates.

### Confounder selection

Do **not** choose propensity covariates solely by statistical significance. Prefer a causal estimand and prespecified confounder set supported by domain knowledge/DAG reasoning. Avoid adjusting for post-treatment variables, colliders, or mediators when they do not belong in the estimand.

## Stabilized IPTW

```python
from thomaslab.causal import calculate_stabilized_ipw

cohort["sw"] = calculate_stabilized_ipw(
    cohort,
    treatment_col="treated",
    propensity_score_col="ps",
)
```

Inspect weight distributions, positivity, effective sample size, and covariate balance. If the protocol uses truncation/winsorization, state the exact percentiles and run sensitivity analyses.

## Propensity-score matching

```python
from thomaslab.causal import match_cohorts

matched = match_cohorts(
    cohort,
    treatment_col="treated",
    propensity_score_col="ps",
    ratio=1,
    caliper=0.2,
)
```

The caliper is interpreted relative to the propensity-score standard deviation as implemented in the function. Confirm whether the target paper instead specifies the SD of the **logit** of the propensity score; those are not interchangeable.

## Covariate balance

```python
from thomaslab.causal import check_covariate_balance

balance = check_covariate_balance(
    matched,
    treatment_col="treated",
    covariates=["age", "egfr", "diabetes"],
)
```

Standardized mean differences are descriptive balance diagnostics. A common heuristic is `|SMD| < 0.1`, but the threshold should not be treated as a proof of exchangeability.

## Cox proportional hazards

```python
from thomaslab.causal import fit_survival_model

result = fit_survival_model(
    cohort,
    time_col="days_to_event_or_censor",
    event_col="event",
    treatment_col="treated",
    covariates=["age", "egfr"],
)
```

Always assess the proportional-hazards assumption and consider competing risks or recurrent events when clinically appropriate.

## Time-varying treatment and sensitivity analysis

`fit_time_varying_cox` fits start-stop Cox models and rejects overlapping intervals within a patient.

`calculate_e_value` implements VanderWeele-Ding E-values. For outcomes that are not rare, set `rare_outcome=False` so the hazard ratio is approximately converted to a risk-ratio scale before the E-value calculation.

`instrumental_variable_2sls` uses statsmodels 2SLS and reports the treatment coefficient plus a first-stage instrument F statistic. A strong first stage does not establish the exclusion restriction or instrument-outcome exchangeability.

`fast_gpu_propensity_matching` uses deterministic greedy 1:1 matching with NumPy/Numba by default and an explicitly requested CuPy backend when available.


## Higher-level workflow diagnostics

Version 0.13 adds `thomaslab.causal_workflows` for propensity overlap, near-positivity diagnostics, effective sample size, weighted balance, AIPW estimation, E-values, and standardized effect tables.

These helpers make diagnostics easier to reproduce but do not establish the causal assumptions required for interpretation. Continue with [Epidemiology and causal workflow layer](causal-epi-workflow.md).

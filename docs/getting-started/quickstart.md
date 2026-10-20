# Quickstart

This example connects the main stages of a typical observational EHR/PGx analysis without pretending that one fixed pipeline is appropriate for every protocol.

## 1. Clean demographics

```python
from thomaslab.data import clean_demographics

cohort = clean_demographics(raw_cohort)
```

Expected inputs include standard demographic fields such as age, sex, race, and ethnicity when available. Always inspect the normalized categories before analysis.

## 2. Build a baseline lab feature table

```python
from thomaslab.data import aggregate_lab_features

baseline_labs = aggregate_lab_features(
    labs,
    patient_id_col="patient_id",
    lab_col="lab_name",
    value_col="result_value",
    date_col="result_date",
    index_date_col="index_date",
    window_days=30,
)
```

The window is a **lookback** relative to the index date. Do not include post-index measurements in baseline features.

## 3. Map CYP2C19 phenotype

```python
from thomaslab.pgx import map_star_alleles_to_phenotype

cohort["cyp2c19_phenotype"] = map_star_alleles_to_phenotype(
    cohort,
    allele_1_col="allele_1",
    allele_2_col="allele_2",
)
```

Unknown/unsupported diplotypes are returned as `Unknown` rather than guessed.

## 4. Estimate treatment propensity

```python
from thomaslab.causal import calculate_propensity_scores, calculate_stabilized_ipw

cohort["ps"] = calculate_propensity_scores(
    cohort,
    treatment_col="alternative_p2y12",
    covariates=["age", "sex", "diabetes", "egfr"],
)
cohort["sw"] = calculate_stabilized_ipw(
    cohort,
    treatment_col="alternative_p2y12",
    propensity_score_col="ps",
)
```

Propensity methods require a prespecified causal question, defensible confounder set, positivity, and appropriate diagnostics.

## 5. Evaluate a prediction model

```python
from thomaslab.eval import calculate_clinical_metrics, compute_calibration

metrics = calculate_clinical_metrics(y_true, y_pred_prob)
calibration = compute_calibration(y_true, y_pred_prob)
```

Report discrimination **and** calibration. For clinical decision models, consider decision-curve analysis and subgroup audits as separate analyses.

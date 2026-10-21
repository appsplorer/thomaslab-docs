# thomaslab.eval

Clinical prediction evaluation, calibration, utility, fairness, and explainability.

## Research-use boundary

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

## Self-service orientation

- Related guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 8

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.eval.calculate_clinical_metrics -->
## calculate_clinical_metrics

### Purpose

Calculate discrimination and threshold-based clinical classification metrics.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_clinical_metrics( y_true: np.ndarray, y_pred_prob: np.ndarray, threshold: float = 0.5, ) -> dict[str, float]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `y_true` | `y_true: np.ndarray` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `y_pred_prob` | `y_pred_prob: np.ndarray` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `threshold` | `threshold: float = 0.5` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `y_true`, `y_pred_prob`.

### Returns

`dict[str, float]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import numpy as np

sample_values = np.array([0.2, 0.8, 0.4, 0.6])

from thomaslab.eval import calculate_clinical_metrics

result = calculate_clinical_metrics(
    y_true=sample_values,
    y_pred_prob=sample_values
)

print(result)
~~~

### Related functions

- `compute_calibration`
- `decision_curve_analysis`
- `audit_fairness`
- `explain_model_shap`
- `compute_population_stability_index`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/eval.py#L33`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/eval.py#L33)
- Repository search: [calculate_clinical_metrics](https://github.com/appsplorer/thomaslab-core/search?q=calculate_clinical_metrics&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate discrimination and threshold-based clinical classification metrics.

### API inspection

~~~python
import inspect
from thomaslab.eval import calculate_clinical_metrics

print(inspect.signature(calculate_clinical_metrics))
print(calculate_clinical_metrics.__doc__)
~~~

### Source

[`src/thomaslab/eval.py#L33`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/eval.py#L33)

---

<!-- callable:thomaslab.eval.compute_calibration -->
## compute_calibration

### Purpose

Estimate calibration table, Brier score, intercept, and slope.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def compute_calibration( y_true: np.ndarray, y_pred_prob: np.ndarray, n_bins: int = 10, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `y_true` | `y_true: np.ndarray` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `y_pred_prob` | `y_pred_prob: np.ndarray` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `n_bins` | `n_bins: int = 10` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `y_true`, `y_pred_prob`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import numpy as np

sample_values = np.array([0.2, 0.8, 0.4, 0.6])

from thomaslab.eval import compute_calibration

result = compute_calibration(
    y_true=sample_values,
    y_pred_prob=sample_values
)

print(result)
~~~

### Related functions

- `calculate_clinical_metrics`
- `decision_curve_analysis`
- `audit_fairness`
- `explain_model_shap`
- `compute_population_stability_index`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/eval.py#L59`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/eval.py#L59)
- Repository search: [compute_calibration](https://github.com/appsplorer/thomaslab-core/search?q=compute_calibration&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate calibration table, Brier score, intercept, and slope.

### API inspection

~~~python
import inspect
from thomaslab.eval import compute_calibration

print(inspect.signature(compute_calibration))
print(compute_calibration.__doc__)
~~~

### Source

[`src/thomaslab/eval.py#L59`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/eval.py#L59)

---

<!-- callable:thomaslab.eval.decision_curve_analysis -->
## decision_curve_analysis

### Purpose

Calculate model, treat-all, and treat-none net benefit across thresholds.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def decision_curve_analysis( y_true: np.ndarray, y_pred_prob: np.ndarray, thresholds: np.ndarray | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `y_true` | `y_true: np.ndarray` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `y_pred_prob` | `y_pred_prob: np.ndarray` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `thresholds` | `thresholds: np.ndarray \| None = None` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `y_true`, `y_pred_prob`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import numpy as np

sample_values = np.array([0.2, 0.8, 0.4, 0.6])

from thomaslab.eval import decision_curve_analysis

result = decision_curve_analysis(
    y_true=sample_values,
    y_pred_prob=sample_values
)

print(result)
~~~

### Related functions

- `calculate_clinical_metrics`
- `compute_calibration`
- `audit_fairness`
- `explain_model_shap`
- `compute_population_stability_index`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/eval.py#L96`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/eval.py#L96)
- Repository search: [decision_curve_analysis](https://github.com/appsplorer/thomaslab-core/search?q=decision_curve_analysis&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate model, treat-all, and treat-none net benefit across thresholds.

### API inspection

~~~python
import inspect
from thomaslab.eval import decision_curve_analysis

print(inspect.signature(decision_curve_analysis))
print(decision_curve_analysis.__doc__)
~~~

### Source

[`src/thomaslab/eval.py#L96`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/eval.py#L96)

---

<!-- callable:thomaslab.eval.audit_fairness -->
## audit_fairness

### Purpose

Report group-wise performance and equalized-odds components.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_fairness( df: pd.DataFrame, y_true_col: str, y_pred_prob_col: str, demographic_col: str, threshold: float = 0.5, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `y_true_col` | `y_true_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `y_pred_prob_col` | `y_pred_prob_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `demographic_col` | `demographic_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `threshold` | `threshold: float = 0.5` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `y_true_col`, `y_pred_prob_col`, `demographic_col`.
- Referenced columns must exist in the input table: `y_true_col`, `y_pred_prob_col`, `demographic_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_df = pd.DataFrame(
    {
        "patient_id": ["P001", "P001", "P002", "P002"],
        "event_date": pd.to_datetime(["2026-01-01", "2026-02-01", "2026-01-05", "2026-02-07"]),
        "treatment": [1, 1, 0, 0],
        "outcome": [0, 1, 0, 0],
        "event": [0, 1, 0, 0],
        "duration": [31.0, 62.0, 33.0, 66.0],
        "weight": [1.0, 0.9, 1.1, 1.0],
        "propensity": [0.70, 0.65, 0.35, 0.30],
        "site": ["A", "A", "B", "B"],
        "feature_a": [1.0, 1.4, 0.7, 0.9],
        "feature_b": [2.0, 2.2, 1.5, 1.7],
    }
)

from thomaslab.eval import audit_fairness

result = audit_fairness(
    df=sample_df,
    y_true_col='y_true',
    y_pred_prob_col='y_pred_prob',
    demographic_col='demographic'
)

print(result)
~~~

### Related functions

- `calculate_clinical_metrics`
- `compute_calibration`
- `decision_curve_analysis`
- `explain_model_shap`
- `compute_population_stability_index`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/eval.py#L129`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/eval.py#L129)
- Repository search: [audit_fairness](https://github.com/appsplorer/thomaslab-core/search?q=audit_fairness&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Report group-wise performance and equalized-odds components.

Equalized odds is represented through TPR and FPR by group plus absolute gaps from the
pooled population. No normative conclusion is assigned automatically.

### API inspection

~~~python
import inspect
from thomaslab.eval import audit_fairness

print(inspect.signature(audit_fairness))
print(audit_fairness.__doc__)
~~~

### Source

[`src/thomaslab/eval.py#L129`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/eval.py#L129)

---

<!-- callable:thomaslab.eval.explain_model_shap -->
## explain_model_shap

### Purpose

Compute SHAP values and mean-absolute feature importance rankings.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def explain_model_shap(model: Any, X_df: pd.DataFrame) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `model` | `model: Any` | Yes | Model or model setting. Fit/tune only within the training design and preserve independent evaluation. |
| `X_df` | `X_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `model`, `X_df`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_df = pd.DataFrame(
    {
        "patient_id": ["P001", "P001", "P002", "P002"],
        "event_date": pd.to_datetime(["2026-01-01", "2026-02-01", "2026-01-05", "2026-02-07"]),
        "treatment": [1, 1, 0, 0],
        "outcome": [0, 1, 0, 0],
        "event": [0, 1, 0, 0],
        "duration": [31.0, 62.0, 33.0, 66.0],
        "weight": [1.0, 0.9, 1.1, 1.0],
        "propensity": [0.70, 0.65, 0.35, 0.30],
        "site": ["A", "A", "B", "B"],
        "feature_a": [1.0, 1.4, 0.7, 0.9],
        "feature_b": [2.0, 2.2, 1.5, 1.7],
    }
)

sample_value = "replace_with_validated_value"

from thomaslab.eval import explain_model_shap

result = explain_model_shap(
    model=sample_value,
    X_df=sample_df
)

print(result)
~~~

### Related functions

- `calculate_clinical_metrics`
- `compute_calibration`
- `decision_curve_analysis`
- `audit_fairness`
- `compute_population_stability_index`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/eval.py#L173`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/eval.py#L173)
- Repository search: [explain_model_shap](https://github.com/appsplorer/thomaslab-core/search?q=explain_model_shap&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compute SHAP values and mean-absolute feature importance rankings.

### API inspection

~~~python
import inspect
from thomaslab.eval import explain_model_shap

print(inspect.signature(explain_model_shap))
print(explain_model_shap.__doc__)
~~~

### Source

[`src/thomaslab/eval.py#L173`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/eval.py#L173)

---

<!-- callable:thomaslab.eval.compute_population_stability_index -->
## compute_population_stability_index

### Purpose

Quantify feature distribution drift with PSI and Wasserstein distance.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def compute_population_stability_index( df_train: pd.DataFrame, df_test: pd.DataFrame, feature_cols: list[str], *, n_bins: int = 10, epsilon: float = 1e-6, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df_train` | `df_train: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `df_test` | `df_test: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `feature_cols` | `feature_cols: list[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `n_bins` | `n_bins: int = 10` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `epsilon` | `epsilon: float = 1e-06` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df_train`, `df_test`, `feature_cols`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_df = pd.DataFrame(
    {
        "patient_id": ["P001", "P001", "P002", "P002"],
        "event_date": pd.to_datetime(["2026-01-01", "2026-02-01", "2026-01-05", "2026-02-07"]),
        "treatment": [1, 1, 0, 0],
        "outcome": [0, 1, 0, 0],
        "event": [0, 1, 0, 0],
        "duration": [31.0, 62.0, 33.0, 66.0],
        "weight": [1.0, 0.9, 1.1, 1.0],
        "propensity": [0.70, 0.65, 0.35, 0.30],
        "site": ["A", "A", "B", "B"],
        "feature_a": [1.0, 1.4, 0.7, 0.9],
        "feature_b": [2.0, 2.2, 1.5, 1.7],
    }
)

from thomaslab.eval import compute_population_stability_index

result = compute_population_stability_index(
    df_train=sample_df,
    df_test=sample_df,
    feature_cols=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `calculate_clinical_metrics`
- `compute_calibration`
- `decision_curve_analysis`
- `audit_fairness`
- `explain_model_shap`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/eval.py#L191`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/eval.py#L191)
- Repository search: [compute_population_stability_index](https://github.com/appsplorer/thomaslab-core/search?q=compute_population_stability_index&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Quantify feature distribution drift with PSI and Wasserstein distance.

Numeric variables use training-set quantile bins so the reference distribution
defines the cut points. Categorical variables use the union of observed levels.
Missingness is treated as an explicit PSI category and reported separately.

### API inspection

~~~python
import inspect
from thomaslab.eval import compute_population_stability_index

print(inspect.signature(compute_population_stability_index))
print(compute_population_stability_index.__doc__)
~~~

### Source

[`src/thomaslab/eval.py#L191`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/eval.py#L191)

---

<!-- callable:thomaslab.eval.bootstrap_confidence_intervals_fast -->
## bootstrap_confidence_intervals_fast

### Purpose

Compute paired nonparametric bootstrap confidence intervals in parallel.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def bootstrap_confidence_intervals_fast( metric_func: Any, y_true: np.ndarray, y_pred: np.ndarray, n_bootstraps: int = 1000, n_jobs: int = -1, *, confidence: float = 0.95, random_state: int = 42, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `metric_func` | `metric_func: Any` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `y_true` | `y_true: np.ndarray` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `y_pred` | `y_pred: np.ndarray` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `n_bootstraps` | `n_bootstraps: int = 1000` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `n_jobs` | `n_jobs: int = -1` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `confidence` | `confidence: float = 0.95` | No | Identifier or identifier column. Confirm uniqueness/grouping semantics before analysis. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `metric_func`, `y_true`, `y_pred`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import numpy as np

sample_values = np.array([0.2, 0.8, 0.4, 0.6])

sample_value = "replace_with_validated_value"

from thomaslab.eval import bootstrap_confidence_intervals_fast

result = bootstrap_confidence_intervals_fast(
    metric_func=sample_value,
    y_true=sample_values,
    y_pred=sample_values
)

print(result)
~~~

### Related functions

- `calculate_clinical_metrics`
- `compute_calibration`
- `decision_curve_analysis`
- `audit_fairness`
- `explain_model_shap`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/eval.py#L263`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/eval.py#L263)
- Repository search: [bootstrap_confidence_intervals_fast](https://github.com/appsplorer/thomaslab-core/search?q=bootstrap_confidence_intervals_fast&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compute paired nonparametric bootstrap confidence intervals in parallel.

``metric_func`` must return a scalar when called as ``metric_func(y_true,
y_pred)``. Sampling is paired and reproducible across process counts because
each bootstrap replicate receives its own deterministic seed.

### API inspection

~~~python
import inspect
from thomaslab.eval import bootstrap_confidence_intervals_fast

print(inspect.signature(bootstrap_confidence_intervals_fast))
print(bootstrap_confidence_intervals_fast.__doc__)
~~~

### Source

[`src/thomaslab/eval.py#L263`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/eval.py#L263)

---

<!-- callable:thomaslab.eval.calculate_idi_and_nri -->
## calculate_idi_and_nri

### Purpose

Calculate binary-outcome IDI and category-free (continuous) NRI.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_idi_and_nri( y_true: np.ndarray, baseline_pred: np.ndarray, new_pred: np.ndarray, ) -> dict[str, float]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `y_true` | `y_true: np.ndarray` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `baseline_pred` | `baseline_pred: np.ndarray` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `new_pred` | `new_pred: np.ndarray` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `y_true`, `baseline_pred`, `new_pred`.

### Returns

`dict[str, float]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import numpy as np

sample_values = np.array([0.2, 0.8, 0.4, 0.6])

from thomaslab.eval import calculate_idi_and_nri

result = calculate_idi_and_nri(
    y_true=sample_values,
    baseline_pred=sample_values,
    new_pred=sample_values
)

print(result)
~~~

### Related functions

- `calculate_clinical_metrics`
- `compute_calibration`
- `decision_curve_analysis`
- `audit_fairness`
- `explain_model_shap`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/eval.py#L325`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/eval.py#L325)
- Repository search: [calculate_idi_and_nri](https://github.com/appsplorer/thomaslab-core/search?q=calculate_idi_and_nri&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate binary-outcome IDI and category-free (continuous) NRI.

IDI is the change in discrimination slope. Continuous NRI is the sum of the
net proportion of events moving upward in predicted risk and non-events moving
downward. Ties contribute zero.

### API inspection

~~~python
import inspect
from thomaslab.eval import calculate_idi_and_nri

print(inspect.signature(calculate_idi_and_nri))
print(calculate_idi_and_nri.__doc__)
~~~

### Source

[`src/thomaslab/eval.py#L325`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/eval.py#L325)

# thomaslab.longitudinal_dr

Cross-fitted longitudinal doubly robust estimation utilities.

This module complements the weighting/MSM layer in thomaslab.longitudinal_causal
and the parametric g-formula layer in thomaslab.gformula. It implements a
transparent longitudinal augmented inverse-probability-weighted (AIPW) estimator for
binary cumulative risk under prespecified static or dynamic treatment regimes.

Panel convention:

    H_t (pre-treatment history) -> A_t -> Y_t -> C_(t+1)/H_(t+1)

Y_t is an absorbing interval event. Outcome regressions are fitted backwards in
time; treatment and censoring nuisance models are cross-fitted by patient; and the
longitudinal influence contribution uses cumulative regime-adherence and
uncensoring weights.

Successful estimation does not establish exchangeability, positivity, consistency,
correct temporal ordering, or correct nuisance-model specification. Dynamic
strategy functions receive only explicitly declared pre-treatment history.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 5

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.longitudinal_dr.validate_sequential_dr_panel -->
## validate_sequential_dr_panel

### Purpose

Audit a monotone person-period panel for longitudinal DR estimation.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_sequential_dr_panel( panel: pd.DataFrame, *, history_covariates: Sequence[str], horizon: int, patient_col: str = "patient_id", time_col: str = "period", treatment_col: str = "treatment", outcome_col: str = "interval_event", censoring_col: str | None = "interval_censored", ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `panel` | `panel: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `history_covariates` | `history_covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `horizon` | `horizon: int` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str = 'treatment'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str = 'interval_event'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `censoring_col` | `censoring_col: str \| None = 'interval_censored'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `panel`, `history_covariates`, `horizon`.
- Referenced columns must exist in the input table: `patient_col`, `time_col`, `treatment_col`, `outcome_col`, `censoring_col`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

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

from thomaslab.longitudinal_dr import validate_sequential_dr_panel

result = validate_sequential_dr_panel(
    panel=sample_df,
    history_covariates=["feature_a", "feature_b"],
    horizon=2
)

print(result)
~~~

### Related functions

- `audit_longitudinal_dr_nuisance`
- `estimate_sequential_aipw_regime`
- `estimate_regime_set_sequential_aipw`
- `triangulate_longitudinal_estimators`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/longitudinal_dr.py#L62`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_dr.py#L62)
- Repository search: [validate_sequential_dr_panel](https://github.com/appsplorer/thomaslab-core/search?q=validate_sequential_dr_panel&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Audit a monotone person-period panel for longitudinal DR estimation.

### API inspection

~~~python
import inspect
from thomaslab.longitudinal_dr import validate_sequential_dr_panel

print(inspect.signature(validate_sequential_dr_panel))
print(validate_sequential_dr_panel.__doc__)
~~~

### Source

[`src/thomaslab/longitudinal_dr.py#L62`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_dr.py#L62)

---

<!-- callable:thomaslab.longitudinal_dr.audit_longitudinal_dr_nuisance -->
## audit_longitudinal_dr_nuisance

### Purpose

Summarize held-out nuisance prediction and weight diagnostics.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_longitudinal_dr_nuisance( nuisance: pd.DataFrame, *, treatment_col: str = "treatment", outcome_col: str = "interval_event", time_col: str = "period", probability_threshold: float = 0.05, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `nuisance` | `nuisance: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str = 'treatment'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str = 'interval_event'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `probability_threshold` | `probability_threshold: float = 0.05` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `nuisance`.
- Referenced columns must exist in the input table: `treatment_col`, `outcome_col`, `time_col`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

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

from thomaslab.longitudinal_dr import audit_longitudinal_dr_nuisance

result = audit_longitudinal_dr_nuisance(
    nuisance=sample_df
)

print(result)
~~~

### Related functions

- `validate_sequential_dr_panel`
- `estimate_sequential_aipw_regime`
- `estimate_regime_set_sequential_aipw`
- `triangulate_longitudinal_estimators`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/longitudinal_dr.py#L637`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_dr.py#L637)
- Repository search: [audit_longitudinal_dr_nuisance](https://github.com/appsplorer/thomaslab-core/search?q=audit_longitudinal_dr_nuisance&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize held-out nuisance prediction and weight diagnostics.

### API inspection

~~~python
import inspect
from thomaslab.longitudinal_dr import audit_longitudinal_dr_nuisance

print(inspect.signature(audit_longitudinal_dr_nuisance))
print(audit_longitudinal_dr_nuisance.__doc__)
~~~

### Source

[`src/thomaslab/longitudinal_dr.py#L637`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_dr.py#L637)

---

<!-- callable:thomaslab.longitudinal_dr.estimate_sequential_aipw_regime -->
## estimate_sequential_aipw_regime

### Purpose

Estimate regime cumulative risk with cross-fitted longitudinal AIPW.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def estimate_sequential_aipw_regime( panel: pd.DataFrame, *, strategy: StrategyRule, strategy_name: str, history_covariates: Sequence[str], horizon: int, patient_col: str = "patient_id", time_col: str = "period", treatment_col: str = "treatment", outcome_col: str = "interval_event", censoring_col: str | None = "interval_censored", n_splits: int = 5, probability_clip: float = 0.01, ridge_alpha: float = 1.0, ci: float = 0.95, random_state: int = 42, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `panel` | `panel: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `strategy` | `strategy: StrategyRule` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strategy_name` | `strategy_name: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `history_covariates` | `history_covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `horizon` | `horizon: int` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str = 'treatment'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str = 'interval_event'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `censoring_col` | `censoring_col: str \| None = 'interval_censored'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `n_splits` | `n_splits: int = 5` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `probability_clip` | `probability_clip: float = 0.01` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `ridge_alpha` | `ridge_alpha: float = 1.0` | No | Identifier or identifier column. Confirm uniqueness/grouping semantics before analysis. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `panel`, `strategy`, `strategy_name`, `history_covariates`, `horizon`.
- Referenced columns must exist in the input table: `patient_col`, `time_col`, `treatment_col`, `outcome_col`, `censoring_col`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

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

from thomaslab.longitudinal_dr import estimate_sequential_aipw_regime

result = estimate_sequential_aipw_regime(
    panel=sample_df,
    strategy="value",
    strategy_name="value",
    history_covariates=["feature_a", "feature_b"],
    horizon=2
)

print(result)
~~~

### Related functions

- `validate_sequential_dr_panel`
- `audit_longitudinal_dr_nuisance`
- `estimate_regime_set_sequential_aipw`
- `triangulate_longitudinal_estimators`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/longitudinal_dr.py#L760`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_dr.py#L760)
- Repository search: [estimate_sequential_aipw_regime](https://github.com/appsplorer/thomaslab-core/search?q=estimate_sequential_aipw_regime&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate regime cumulative risk with cross-fitted longitudinal AIPW.

### API inspection

~~~python
import inspect
from thomaslab.longitudinal_dr import estimate_sequential_aipw_regime

print(inspect.signature(estimate_sequential_aipw_regime))
print(estimate_sequential_aipw_regime.__doc__)
~~~

### Source

[`src/thomaslab/longitudinal_dr.py#L760`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_dr.py#L760)

---

<!-- callable:thomaslab.longitudinal_dr.estimate_regime_set_sequential_aipw -->
## estimate_regime_set_sequential_aipw

### Purpose

Estimate multiple regimes and paired risk contrasts.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def estimate_regime_set_sequential_aipw( panel: pd.DataFrame, *, strategies: Mapping[str, StrategyRule], reference: str, history_covariates: Sequence[str], horizon: int, patient_col: str = "patient_id", time_col: str = "period", treatment_col: str = "treatment", outcome_col: str = "interval_event", censoring_col: str | None = "interval_censored", n_splits: int = 5, probability_clip: float = 0.01, ridge_alpha: float = 1.0, ci: float = 0.95, random_state: int = 42, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `panel` | `panel: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `strategies` | `strategies: Mapping[str, StrategyRule]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `reference` | `reference: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `history_covariates` | `history_covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `horizon` | `horizon: int` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str = 'treatment'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str = 'interval_event'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `censoring_col` | `censoring_col: str \| None = 'interval_censored'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `n_splits` | `n_splits: int = 5` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `probability_clip` | `probability_clip: float = 0.01` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `ridge_alpha` | `ridge_alpha: float = 1.0` | No | Identifier or identifier column. Confirm uniqueness/grouping semantics before analysis. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `panel`, `strategies`, `reference`, `history_covariates`, `horizon`.
- Referenced columns must exist in the input table: `patient_col`, `time_col`, `treatment_col`, `outcome_col`, `censoring_col`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

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

from thomaslab.longitudinal_dr import estimate_regime_set_sequential_aipw

result = estimate_regime_set_sequential_aipw(
    panel=sample_df,
    strategies={},
    reference="value",
    history_covariates=["feature_a", "feature_b"],
    horizon=2
)

print(result)
~~~

### Related functions

- `validate_sequential_dr_panel`
- `audit_longitudinal_dr_nuisance`
- `estimate_sequential_aipw_regime`
- `triangulate_longitudinal_estimators`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/longitudinal_dr.py#L886`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_dr.py#L886)
- Repository search: [estimate_regime_set_sequential_aipw](https://github.com/appsplorer/thomaslab-core/search?q=estimate_regime_set_sequential_aipw&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate multiple regimes and paired risk contrasts.

### API inspection

~~~python
import inspect
from thomaslab.longitudinal_dr import estimate_regime_set_sequential_aipw

print(inspect.signature(estimate_regime_set_sequential_aipw))
print(estimate_regime_set_sequential_aipw.__doc__)
~~~

### Source

[`src/thomaslab/longitudinal_dr.py#L886`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_dr.py#L886)

---

<!-- callable:thomaslab.longitudinal_dr.triangulate_longitudinal_estimators -->
## triangulate_longitudinal_estimators

### Purpose

Build an estimator-triangulation table without an automatic verdict.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def triangulate_longitudinal_estimators( dr_comparison: pd.DataFrame, *, gformula_comparison: pd.DataFrame | None = None, msm_estimates: pd.DataFrame | None = None, strategy_col: str = "strategy", msm_treatment_term: str = "treatment", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `dr_comparison` | `dr_comparison: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `gformula_comparison` | `gformula_comparison: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `msm_estimates` | `msm_estimates: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `strategy_col` | `strategy_col: str = 'strategy'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `msm_treatment_term` | `msm_treatment_term: str = 'treatment'` | No | Treatment/exposure definition supplied by the study specification; do not infer clinical meaning from labels alone. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `dr_comparison`.
- Referenced columns must exist in the input table: `strategy_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

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

from thomaslab.longitudinal_dr import triangulate_longitudinal_estimators

result = triangulate_longitudinal_estimators(
    dr_comparison=sample_df
)

print(result)
~~~

### Related functions

- `validate_sequential_dr_panel`
- `audit_longitudinal_dr_nuisance`
- `estimate_sequential_aipw_regime`
- `estimate_regime_set_sequential_aipw`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/longitudinal_dr.py#L999`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_dr.py#L999)
- Repository search: [triangulate_longitudinal_estimators](https://github.com/appsplorer/thomaslab-core/search?q=triangulate_longitudinal_estimators&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build an estimator-triangulation table without an automatic verdict.

### API inspection

~~~python
import inspect
from thomaslab.longitudinal_dr import triangulate_longitudinal_estimators

print(inspect.signature(triangulate_longitudinal_estimators))
print(triangulate_longitudinal_estimators.__doc__)
~~~

### Source

[`src/thomaslab/longitudinal_dr.py#L999`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_dr.py#L999)

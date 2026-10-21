# thomaslab.quasi_experimental

Quasi-experimental causal research utilities.

This module provides guarded implementations of instrumental-variable estimation,
two-period difference-in-differences, regression discontinuity, and interrupted
time-series models.

The software computes estimators and diagnostics; it does not establish the
identification assumptions required for causal interpretation. In particular:

* IV relevance does not establish instrument independence or the exclusion
  restriction;
* a conventional first-stage F threshold is a screening rule, not proof that an
  instrument is strong or valid;
* DiD requires a defensible parallel-trends counterfactual;
* RD requires continuity around the cutoff and absence of problematic sorting or
  manipulation;
* interrupted time series can be biased by concurrent interventions, shocks, or
  misspecified trends.

All design choices such as cutoffs, bandwidths, treatment dates, clustering units,
and HAC lags are explicit caller inputs.

## Research-use boundary

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

## Self-service orientation

- Related guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 9

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.quasi_experimental.validate_iv_inputs -->
## validate_iv_inputs

### Purpose

Validate numeric IV inputs and basic rank/support requirements.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_iv_inputs( df: pd.DataFrame, *, outcome_col: str, treatment_col: str, instrument_cols: Sequence[str], covariates: Sequence[str] = (), ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `instrument_cols` | `instrument_cols: Sequence[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `covariates` | `covariates: Sequence[str] = ()` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `outcome_col`, `treatment_col`, `instrument_cols`.
- Referenced columns must exist in the input table: `outcome_col`, `treatment_col`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

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

from thomaslab.quasi_experimental import validate_iv_inputs

result = validate_iv_inputs(
    df=sample_df,
    outcome_col='outcome',
    treatment_col='treatment',
    instrument_cols=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `iv_first_stage_diagnostics`
- `estimate_2sls`
- `estimate_two_period_did`
- `did_pretrend_diagnostic`
- `estimate_regression_discontinuity`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/quasi_experimental.py#L105`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quasi_experimental.py#L105)
- Repository search: [validate_iv_inputs](https://github.com/appsplorer/thomaslab-core/search?q=validate_iv_inputs&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate numeric IV inputs and basic rank/support requirements.

### API inspection

~~~python
import inspect
from thomaslab.quasi_experimental import validate_iv_inputs

print(inspect.signature(validate_iv_inputs))
print(validate_iv_inputs.__doc__)
~~~

### Source

[`src/thomaslab/quasi_experimental.py#L105`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quasi_experimental.py#L105)

---

<!-- callable:thomaslab.quasi_experimental.iv_first_stage_diagnostics -->
## iv_first_stage_diagnostics

### Purpose

Compute classical excluded-instrument first-stage diagnostics.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def iv_first_stage_diagnostics( df: pd.DataFrame, *, treatment_col: str, instrument_cols: Sequence[str], covariates: Sequence[str] = (), weak_f_threshold: float = 10.0, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `instrument_cols` | `instrument_cols: Sequence[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `covariates` | `covariates: Sequence[str] = ()` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `weak_f_threshold` | `weak_f_threshold: float = 10.0` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `instrument_cols`.
- Referenced columns must exist in the input table: `treatment_col`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

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

from thomaslab.quasi_experimental import iv_first_stage_diagnostics

result = iv_first_stage_diagnostics(
    df=sample_df,
    treatment_col='treatment',
    instrument_cols=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `validate_iv_inputs`
- `estimate_2sls`
- `estimate_two_period_did`
- `did_pretrend_diagnostic`
- `estimate_regression_discontinuity`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/quasi_experimental.py#L154`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quasi_experimental.py#L154)
- Repository search: [iv_first_stage_diagnostics](https://github.com/appsplorer/thomaslab-core/search?q=iv_first_stage_diagnostics&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compute classical excluded-instrument first-stage diagnostics.

The F statistic is the conventional homoskedastic partial F from nested OLS
first-stage models. weak_f_threshold is an analyst-specified screening
threshold and is not a universal validity rule.

### API inspection

~~~python
import inspect
from thomaslab.quasi_experimental import iv_first_stage_diagnostics

print(inspect.signature(iv_first_stage_diagnostics))
print(iv_first_stage_diagnostics.__doc__)
~~~

### Source

[`src/thomaslab/quasi_experimental.py#L154`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quasi_experimental.py#L154)

---

<!-- callable:thomaslab.quasi_experimental.estimate_2sls -->
## estimate_2sls

### Purpose

Estimate a linear 2SLS model with HC1 or homoskedastic covariance.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def estimate_2sls( df: pd.DataFrame, *, outcome_col: str, treatment_col: str, instrument_cols: Sequence[str], covariates: Sequence[str] = (), ci: float = 0.95, robust: bool = True, weak_f_threshold: float = 10.0, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `instrument_cols` | `instrument_cols: Sequence[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `covariates` | `covariates: Sequence[str] = ()` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `robust` | `robust: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `weak_f_threshold` | `weak_f_threshold: float = 10.0` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `outcome_col`, `treatment_col`, `instrument_cols`.
- Referenced columns must exist in the input table: `outcome_col`, `treatment_col`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

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

from thomaslab.quasi_experimental import estimate_2sls

result = estimate_2sls(
    df=sample_df,
    outcome_col='outcome',
    treatment_col='treatment',
    instrument_cols=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `validate_iv_inputs`
- `iv_first_stage_diagnostics`
- `estimate_two_period_did`
- `did_pretrend_diagnostic`
- `estimate_regression_discontinuity`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/quasi_experimental.py#L217`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quasi_experimental.py#L217)
- Repository search: [estimate_2sls](https://github.com/appsplorer/thomaslab-core/search?q=estimate_2sls&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate a linear 2SLS model with HC1 or homoskedastic covariance.

### API inspection

~~~python
import inspect
from thomaslab.quasi_experimental import estimate_2sls

print(inspect.signature(estimate_2sls))
print(estimate_2sls.__doc__)
~~~

### Source

[`src/thomaslab/quasi_experimental.py#L217`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quasi_experimental.py#L217)

---

<!-- callable:thomaslab.quasi_experimental.estimate_two_period_did -->
## estimate_two_period_did

### Purpose

Estimate a canonical two-group, two-period difference-in-differences model.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def estimate_two_period_did( df: pd.DataFrame, *, outcome_col: str, treated_group_col: str, post_col: str, covariates: Sequence[str] = (), cluster_col: str | None = None, ci: float = 0.95, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treated_group_col` | `treated_group_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `post_col` | `post_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str] = ()` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `cluster_col` | `cluster_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `outcome_col`, `treated_group_col`, `post_col`.
- Referenced columns must exist in the input table: `outcome_col`, `treated_group_col`, `post_col`, `cluster_col`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

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

from thomaslab.quasi_experimental import estimate_two_period_did

result = estimate_two_period_did(
    df=sample_df,
    outcome_col='outcome',
    treated_group_col='treated_group',
    post_col='post'
)

print(result)
~~~

### Related functions

- `validate_iv_inputs`
- `iv_first_stage_diagnostics`
- `estimate_2sls`
- `did_pretrend_diagnostic`
- `estimate_regression_discontinuity`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/quasi_experimental.py#L307`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quasi_experimental.py#L307)
- Repository search: [estimate_two_period_did](https://github.com/appsplorer/thomaslab-core/search?q=estimate_two_period_did&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate a canonical two-group, two-period difference-in-differences model.

### API inspection

~~~python
import inspect
from thomaslab.quasi_experimental import estimate_two_period_did

print(inspect.signature(estimate_two_period_did))
print(estimate_two_period_did.__doc__)
~~~

### Source

[`src/thomaslab/quasi_experimental.py#L307`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quasi_experimental.py#L307)

---

<!-- callable:thomaslab.quasi_experimental.did_pretrend_diagnostic -->
## did_pretrend_diagnostic

### Purpose

Test a differential linear pre-trend before a common intervention time.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def did_pretrend_diagnostic( df: pd.DataFrame, *, outcome_col: str, treated_group_col: str, time_col: str, intervention_time: float, covariates: Sequence[str] = (), cluster_col: str | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treated_group_col` | `treated_group_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `intervention_time` | `intervention_time: float` | Yes | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `covariates` | `covariates: Sequence[str] = ()` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `cluster_col` | `cluster_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `outcome_col`, `treated_group_col`, `time_col`, `intervention_time`.
- Referenced columns must exist in the input table: `outcome_col`, `treated_group_col`, `time_col`, `cluster_col`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

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

from thomaslab.quasi_experimental import did_pretrend_diagnostic

result = did_pretrend_diagnostic(
    df=sample_df,
    outcome_col='outcome',
    treated_group_col='treated_group',
    time_col='event_date',
    intervention_time=2
)

print(result)
~~~

### Related functions

- `validate_iv_inputs`
- `iv_first_stage_diagnostics`
- `estimate_2sls`
- `estimate_two_period_did`
- `estimate_regression_discontinuity`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/quasi_experimental.py#L406`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quasi_experimental.py#L406)
- Repository search: [did_pretrend_diagnostic](https://github.com/appsplorer/thomaslab-core/search?q=did_pretrend_diagnostic&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Test a differential linear pre-trend before a common intervention time.

### API inspection

~~~python
import inspect
from thomaslab.quasi_experimental import did_pretrend_diagnostic

print(inspect.signature(did_pretrend_diagnostic))
print(did_pretrend_diagnostic.__doc__)
~~~

### Source

[`src/thomaslab/quasi_experimental.py#L406`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quasi_experimental.py#L406)

---

<!-- callable:thomaslab.quasi_experimental.estimate_regression_discontinuity -->
## estimate_regression_discontinuity

### Purpose

Estimate a local-linear sharp RD discontinuity with separate slopes.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def estimate_regression_discontinuity( df: pd.DataFrame, *, outcome_col: str, running_col: str, cutoff: float, bandwidth: float, covariates: Sequence[str] = (), kernel: str = "triangular", ci: float = 0.95, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `running_col` | `running_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `cutoff` | `cutoff: float` | Yes | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |
| `bandwidth` | `bandwidth: float` | Yes | Identifier or identifier column. Confirm uniqueness/grouping semantics before analysis. |
| `covariates` | `covariates: Sequence[str] = ()` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `kernel` | `kernel: str = 'triangular'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `outcome_col`, `running_col`, `cutoff`, `bandwidth`.
- Referenced columns must exist in the input table: `outcome_col`, `running_col`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

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

from thomaslab.quasi_experimental import estimate_regression_discontinuity

result = estimate_regression_discontinuity(
    df=sample_df,
    outcome_col='outcome',
    running_col='running',
    cutoff=0.5,
    bandwidth=0.5
)

print(result)
~~~

### Related functions

- `validate_iv_inputs`
- `iv_first_stage_diagnostics`
- `estimate_2sls`
- `estimate_two_period_did`
- `did_pretrend_diagnostic`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/quasi_experimental.py#L470`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quasi_experimental.py#L470)
- Repository search: [estimate_regression_discontinuity](https://github.com/appsplorer/thomaslab-core/search?q=estimate_regression_discontinuity&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate a local-linear sharp RD discontinuity with separate slopes.

### API inspection

~~~python
import inspect
from thomaslab.quasi_experimental import estimate_regression_discontinuity

print(inspect.signature(estimate_regression_discontinuity))
print(estimate_regression_discontinuity.__doc__)
~~~

### Source

[`src/thomaslab/quasi_experimental.py#L470`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quasi_experimental.py#L470)

---

<!-- callable:thomaslab.quasi_experimental.rd_bandwidth_sensitivity -->
## rd_bandwidth_sensitivity

### Purpose

Repeat local-linear RD over caller-specified bandwidths.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def rd_bandwidth_sensitivity( df: pd.DataFrame, *, outcome_col: str, running_col: str, cutoff: float, bandwidths: Sequence[float], covariates: Sequence[str] = (), kernel: str = "triangular", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `running_col` | `running_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `cutoff` | `cutoff: float` | Yes | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |
| `bandwidths` | `bandwidths: Sequence[float]` | Yes | Identifier or identifier column. Confirm uniqueness/grouping semantics before analysis. |
| `covariates` | `covariates: Sequence[str] = ()` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `kernel` | `kernel: str = 'triangular'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `outcome_col`, `running_col`, `cutoff`, `bandwidths`.
- Referenced columns must exist in the input table: `outcome_col`, `running_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

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

from thomaslab.quasi_experimental import rd_bandwidth_sensitivity

result = rd_bandwidth_sensitivity(
    df=sample_df,
    outcome_col='outcome',
    running_col='running',
    cutoff=0.5,
    bandwidths=0.5
)

print(result)
~~~

### Related functions

- `validate_iv_inputs`
- `iv_first_stage_diagnostics`
- `estimate_2sls`
- `estimate_two_period_did`
- `did_pretrend_diagnostic`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/quasi_experimental.py#L560`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quasi_experimental.py#L560)
- Repository search: [rd_bandwidth_sensitivity](https://github.com/appsplorer/thomaslab-core/search?q=rd_bandwidth_sensitivity&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Repeat local-linear RD over caller-specified bandwidths.

### API inspection

~~~python
import inspect
from thomaslab.quasi_experimental import rd_bandwidth_sensitivity

print(inspect.signature(rd_bandwidth_sensitivity))
print(rd_bandwidth_sensitivity.__doc__)
~~~

### Source

[`src/thomaslab/quasi_experimental.py#L560`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quasi_experimental.py#L560)

---

<!-- callable:thomaslab.quasi_experimental.estimate_interrupted_time_series -->
## estimate_interrupted_time_series

### Purpose

Estimate segmented regression for a single interrupted time series.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def estimate_interrupted_time_series( df: pd.DataFrame, *, outcome_col: str, time_col: str, intervention_time: float, covariates: Sequence[str] = (), hac_lags: int = 1, ci: float = 0.95, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `intervention_time` | `intervention_time: float` | Yes | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `covariates` | `covariates: Sequence[str] = ()` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `hac_lags` | `hac_lags: int = 1` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `outcome_col`, `time_col`, `intervention_time`.
- Referenced columns must exist in the input table: `outcome_col`, `time_col`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

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

from thomaslab.quasi_experimental import estimate_interrupted_time_series

result = estimate_interrupted_time_series(
    df=sample_df,
    outcome_col='outcome',
    time_col='event_date',
    intervention_time=2
)

print(result)
~~~

### Related functions

- `validate_iv_inputs`
- `iv_first_stage_diagnostics`
- `estimate_2sls`
- `estimate_two_period_did`
- `did_pretrend_diagnostic`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/quasi_experimental.py#L616`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quasi_experimental.py#L616)
- Repository search: [estimate_interrupted_time_series](https://github.com/appsplorer/thomaslab-core/search?q=estimate_interrupted_time_series&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate segmented regression for a single interrupted time series.

### API inspection

~~~python
import inspect
from thomaslab.quasi_experimental import estimate_interrupted_time_series

print(inspect.signature(estimate_interrupted_time_series))
print(estimate_interrupted_time_series.__doc__)
~~~

### Source

[`src/thomaslab/quasi_experimental.py#L616`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quasi_experimental.py#L616)

---

<!-- callable:thomaslab.quasi_experimental.quasi_experimental_effect_table -->
## quasi_experimental_effect_table

### Purpose

Normalize supported quasi-experimental result dictionaries to effect rows.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def quasi_experimental_effect_table(result: dict[str, Any]) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `result` | `result: dict[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `result`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.quasi_experimental import quasi_experimental_effect_table

result = quasi_experimental_effect_table(
    result={}
)

print(result)
~~~

### Related functions

- `validate_iv_inputs`
- `iv_first_stage_diagnostics`
- `estimate_2sls`
- `estimate_two_period_did`
- `did_pretrend_diagnostic`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/quasi_experimental.py#L713`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quasi_experimental.py#L713)
- Repository search: [quasi_experimental_effect_table](https://github.com/appsplorer/thomaslab-core/search?q=quasi_experimental_effect_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Normalize supported quasi-experimental result dictionaries to effect rows.

### API inspection

~~~python
import inspect
from thomaslab.quasi_experimental import quasi_experimental_effect_table

print(inspect.signature(quasi_experimental_effect_table))
print(quasi_experimental_effect_table.__doc__)
~~~

### Source

[`src/thomaslab/quasi_experimental.py#L713`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quasi_experimental.py#L713)

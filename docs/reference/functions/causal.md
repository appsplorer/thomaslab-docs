# thomaslab.causal

Causal inference and time-to-event utilities for observational clinical studies.

## Research-use boundary

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

## Self-service orientation

- Related guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 10

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.causal.calculate_propensity_scores -->
## calculate_propensity_scores

### Purpose

Estimate treatment propensity using regularized logistic regression.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_propensity_scores( df: pd.DataFrame, treatment_col: str, covariates: list[str], ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: list[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `covariates`.
- Referenced columns must exist in the input table: `treatment_col`.

### Returns

`pd.Series`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

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

from thomaslab.causal import calculate_propensity_scores

result = calculate_propensity_scores(
    df=sample_df,
    treatment_col='treatment',
    covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `calculate_stabilized_ipw`
- `match_cohorts`
- `check_covariate_balance`
- `fit_survival_model`
- `compute_iptw_weights`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal.py#L23`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L23)
- Repository search: [calculate_propensity_scores](https://github.com/appsplorer/thomaslab-core/search?q=calculate_propensity_scores&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate treatment propensity using regularized logistic regression.

### API inspection

~~~python
import inspect
from thomaslab.causal import calculate_propensity_scores

print(inspect.signature(calculate_propensity_scores))
print(calculate_propensity_scores.__doc__)
~~~

### Source

[`src/thomaslab/causal.py#L23`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L23)

---

<!-- callable:thomaslab.causal.calculate_stabilized_ipw -->
## calculate_stabilized_ipw

### Purpose

Calculate stabilized inverse-probability-of-treatment weights.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_stabilized_ipw( df: pd.DataFrame, treatment_col: str, propensity_score_col: str, trim_quantiles: tuple[float, float] | None = (0.01, 0.99), ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `propensity_score_col` | `propensity_score_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `trim_quantiles` | `trim_quantiles: tuple[float, float] \| None = (0.01, 0.99)` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `propensity_score_col`.
- Referenced columns must exist in the input table: `treatment_col`, `propensity_score_col`.

### Returns

`pd.Series`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

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

from thomaslab.causal import calculate_stabilized_ipw

result = calculate_stabilized_ipw(
    df=sample_df,
    treatment_col='treatment',
    propensity_score_col='propensity_score'
)

print(result)
~~~

### Related functions

- `calculate_propensity_scores`
- `match_cohorts`
- `check_covariate_balance`
- `fit_survival_model`
- `compute_iptw_weights`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal.py#L69`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L69)
- Repository search: [calculate_stabilized_ipw](https://github.com/appsplorer/thomaslab-core/search?q=calculate_stabilized_ipw&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate stabilized inverse-probability-of-treatment weights.

### API inspection

~~~python
import inspect
from thomaslab.causal import calculate_stabilized_ipw

print(inspect.signature(calculate_stabilized_ipw))
print(calculate_stabilized_ipw.__doc__)
~~~

### Source

[`src/thomaslab/causal.py#L69`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L69)

---

<!-- callable:thomaslab.causal.match_cohorts -->
## match_cohorts

### Purpose

Perform greedy nearest-neighbor propensity-score matching without replacement.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def match_cohorts( df: pd.DataFrame, treatment_col: str, propensity_score_col: str, ratio: int = 1, caliper: float = 0.2, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `propensity_score_col` | `propensity_score_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `ratio` | `ratio: int = 1` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `caliper` | `caliper: float = 0.2` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `propensity_score_col`.
- Referenced columns must exist in the input table: `treatment_col`, `propensity_score_col`.

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

from thomaslab.causal import match_cohorts

result = match_cohorts(
    df=sample_df,
    treatment_col='treatment',
    propensity_score_col='propensity_score'
)

print(result)
~~~

### Related functions

- `calculate_propensity_scores`
- `calculate_stabilized_ipw`
- `check_covariate_balance`
- `fit_survival_model`
- `compute_iptw_weights`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal.py#L95`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L95)
- Repository search: [match_cohorts](https://github.com/appsplorer/thomaslab-core/search?q=match_cohorts&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Perform greedy nearest-neighbor propensity-score matching without replacement.

The returned data preserve all input rows and add ``_matched``, ``match_id``, and
``match_distance`` columns. The caliper is ``caliper * SD(propensity score)``.

### API inspection

~~~python
import inspect
from thomaslab.causal import match_cohorts

print(inspect.signature(match_cohorts))
print(match_cohorts.__doc__)
~~~

### Source

[`src/thomaslab/causal.py#L95`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L95)

---

<!-- callable:thomaslab.causal.check_covariate_balance -->
## check_covariate_balance

### Purpose

Calculate absolute standardized mean differences before and after matching.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def check_covariate_balance( df: pd.DataFrame, treatment_col: str, covariates: list[str], ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: list[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `covariates`.
- Referenced columns must exist in the input table: `treatment_col`.

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

from thomaslab.causal import check_covariate_balance

result = check_covariate_balance(
    df=sample_df,
    treatment_col='treatment',
    covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `calculate_propensity_scores`
- `calculate_stabilized_ipw`
- `match_cohorts`
- `fit_survival_model`
- `compute_iptw_weights`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal.py#L164`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L164)
- Repository search: [check_covariate_balance](https://github.com/appsplorer/thomaslab-core/search?q=check_covariate_balance&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate absolute standardized mean differences before and after matching.

### API inspection

~~~python
import inspect
from thomaslab.causal import check_covariate_balance

print(inspect.signature(check_covariate_balance))
print(check_covariate_balance.__doc__)
~~~

### Source

[`src/thomaslab/causal.py#L164`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L164)

---

<!-- callable:thomaslab.causal.fit_survival_model -->
## fit_survival_model

### Purpose

Fit a Cox proportional-hazards model and return HRs, 95% CIs, and p-values.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fit_survival_model( df: pd.DataFrame, time_col: str, event_col: str, treatment_col: str, covariates: list[str] | None = None, weight_col: str | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: list[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `weight_col` | `weight_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `time_col`, `event_col`, `treatment_col`.
- Referenced columns must exist in the input table: `time_col`, `event_col`, `treatment_col`, `weight_col`.

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

from thomaslab.causal import fit_survival_model

result = fit_survival_model(
    df=sample_df,
    time_col='event_date',
    event_col='event',
    treatment_col='treatment'
)

print(result)
~~~

### Related functions

- `calculate_propensity_scores`
- `calculate_stabilized_ipw`
- `match_cohorts`
- `check_covariate_balance`
- `compute_iptw_weights`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal.py#L195`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L195)
- Repository search: [fit_survival_model](https://github.com/appsplorer/thomaslab-core/search?q=fit_survival_model&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Fit a Cox proportional-hazards model and return HRs, 95% CIs, and p-values.

### API inspection

~~~python
import inspect
from thomaslab.causal import fit_survival_model

print(inspect.signature(fit_survival_model))
print(fit_survival_model.__doc__)
~~~

### Source

[`src/thomaslab/causal.py#L195`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L195)

---

<!-- callable:thomaslab.causal.compute_iptw_weights -->
## compute_iptw_weights

### Purpose

Compute inverse probability of treatment weights (IPTW).

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def compute_iptw_weights( df: pd.DataFrame, propensity_col: str, treatment_col: str, stabilize: bool = True, *, clip: float = 1e-6, trim_quantiles: tuple[float, float] | None = None, ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `propensity_col` | `propensity_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `stabilize` | `stabilize: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `clip` | `clip: float = 1e-06` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `trim_quantiles` | `trim_quantiles: tuple[float, float] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `propensity_col`, `treatment_col`.
- Referenced columns must exist in the input table: `propensity_col`, `treatment_col`.

### Returns

`pd.Series`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

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

from thomaslab.causal import compute_iptw_weights

result = compute_iptw_weights(
    df=sample_df,
    propensity_col='propensity',
    treatment_col='treatment'
)

print(result)
~~~

### Related functions

- `calculate_propensity_scores`
- `calculate_stabilized_ipw`
- `match_cohorts`
- `check_covariate_balance`
- `fit_survival_model`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal.py#L249`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L249)
- Repository search: [compute_iptw_weights](https://github.com/appsplorer/thomaslab-core/search?q=compute_iptw_weights&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compute inverse probability of treatment weights (IPTW).

Parameters
----------
df:
    Analysis cohort.
propensity_col:
    Estimated probability of the observed binary treatment.
treatment_col:
    Binary treatment indicator (0/1).
stabilize:
    If True, use marginal treatment probabilities in the numerator.
clip:
    Numerical guard applied to propensity scores before inversion.
trim_quantiles:
    Optional lower/upper quantiles used to winsorize the resulting weights.

Returns
-------
pandas.Series
    IPTW aligned to the original DataFrame index.

### API inspection

~~~python
import inspect
from thomaslab.causal import compute_iptw_weights

print(inspect.signature(compute_iptw_weights))
print(compute_iptw_weights.__doc__)
~~~

### Source

[`src/thomaslab/causal.py#L249`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L249)

---

<!-- callable:thomaslab.causal.fast_gpu_propensity_matching -->
## fast_gpu_propensity_matching

### Purpose

Fast greedy 1:1 nearest-neighbor propensity matching without replacement.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fast_gpu_propensity_matching( df: pd.DataFrame, treatment_col: str, propensity_col: str, caliper: float = 0.2, *, backend: str = "auto", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `propensity_col` | `propensity_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `caliper` | `caliper: float = 0.2` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `backend` | `backend: str = 'auto'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `propensity_col`.
- Referenced columns must exist in the input table: `treatment_col`, `propensity_col`.

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

from thomaslab.causal import fast_gpu_propensity_matching

result = fast_gpu_propensity_matching(
    df=sample_df,
    treatment_col='treatment',
    propensity_col='propensity'
)

print(result)
~~~

### Related functions

- `calculate_propensity_scores`
- `calculate_stabilized_ipw`
- `match_cohorts`
- `check_covariate_balance`
- `fit_survival_model`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal.py#L351`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L351)
- Repository search: [fast_gpu_propensity_matching](https://github.com/appsplorer/thomaslab-core/search?q=fast_gpu_propensity_matching&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Fast greedy 1:1 nearest-neighbor propensity matching without replacement.

The implementation uses a Numba-compiled sorted-search kernel when Numba is
available. ``backend='gpu'`` attempts the same computation with CuPy only when
CuPy is installed; otherwise it fails explicitly. Because exact greedy matching
is sequential, the Numba path is usually more memory-efficient than constructing
an O(N²) GPU distance matrix.

The caliper is ``caliper * SD(propensity score)``. The full cohort is returned
with ``_matched``, ``match_id``, and ``match_distance`` columns.

### API inspection

~~~python
import inspect
from thomaslab.causal import fast_gpu_propensity_matching

print(inspect.signature(fast_gpu_propensity_matching))
print(fast_gpu_propensity_matching.__doc__)
~~~

### Source

[`src/thomaslab/causal.py#L351`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L351)

---

<!-- callable:thomaslab.causal.fit_time_varying_cox -->
## fit_time_varying_cox

### Purpose

Fit a start-stop time-varying Cox proportional-hazards model.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fit_time_varying_cox( df: pd.DataFrame, id_col: str, start_col: str, stop_col: str, event_col: str, treatment_col: str, covariates: list[str], *, weight_col: str | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `id_col` | `id_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `stop_col` | `stop_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: list[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `weight_col` | `weight_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `id_col`, `start_col`, `stop_col`, `event_col`, `treatment_col`, `covariates`.
- Referenced columns must exist in the input table: `id_col`, `start_col`, `stop_col`, `event_col`, `treatment_col`, `weight_col`.

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

from thomaslab.causal import fit_time_varying_cox

result = fit_time_varying_cox(
    df=sample_df,
    id_col='patient_id',
    start_col='start',
    stop_col='stop',
    event_col='event',
    treatment_col='treatment',
    covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `calculate_propensity_scores`
- `calculate_stabilized_ipw`
- `match_cohorts`
- `check_covariate_balance`
- `fit_survival_model`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal.py#L462`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L462)
- Repository search: [fit_time_varying_cox](https://github.com/appsplorer/thomaslab-core/search?q=fit_time_varying_cox&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Fit a start-stop time-varying Cox proportional-hazards model.

### API inspection

~~~python
import inspect
from thomaslab.causal import fit_time_varying_cox

print(inspect.signature(fit_time_varying_cox))
print(fit_time_varying_cox.__doc__)
~~~

### Source

[`src/thomaslab/causal.py#L462`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L462)

---

<!-- callable:thomaslab.causal.calculate_e_value -->
## calculate_e_value

### Purpose

Calculate VanderWeele-Ding E-values for a hazard ratio and confidence interval.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_e_value( hazard_ratio: float, lower_ci: float, upper_ci: float, *, rare_outcome: bool = True, ) -> dict[str, float | bool]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `hazard_ratio` | `hazard_ratio: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `lower_ci` | `lower_ci: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `upper_ci` | `upper_ci: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `rare_outcome` | `rare_outcome: bool = True` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `hazard_ratio`, `lower_ci`, `upper_ci`.

### Returns

`dict[str, float | bool]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.causal import calculate_e_value

result = calculate_e_value(
    hazard_ratio=0.5,
    lower_ci=0.5,
    upper_ci=0.5
)

print(result)
~~~

### Related functions

- `calculate_propensity_scores`
- `calculate_stabilized_ipw`
- `match_cohorts`
- `check_covariate_balance`
- `fit_survival_model`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal.py#L544`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L544)
- Repository search: [calculate_e_value](https://github.com/appsplorer/thomaslab-core/search?q=calculate_e_value&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate VanderWeele-Ding E-values for a hazard ratio and confidence interval.

For rare outcomes (<~15% by end of follow-up), the hazard ratio is treated as a
risk-ratio approximation. For common outcomes set ``rare_outcome=False`` to use
the standard approximate HR-to-RR conversion used by the EValue reference
implementation. The CI E-value is based on the confidence bound closest to 1;
it equals 1 when the interval includes the null.

### API inspection

~~~python
import inspect
from thomaslab.causal import calculate_e_value

print(inspect.signature(calculate_e_value))
print(calculate_e_value.__doc__)
~~~

### Source

[`src/thomaslab/causal.py#L544`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L544)

---

<!-- callable:thomaslab.causal.instrumental_variable_2sls -->
## instrumental_variable_2sls

### Purpose

Fit a linear two-stage least-squares instrumental-variable model.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def instrumental_variable_2sls( df: pd.DataFrame, outcome_col: str, treatment_col: str, instrument_col: str, covariates: list[str], ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `instrument_col` | `instrument_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: list[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `outcome_col`, `treatment_col`, `instrument_col`, `covariates`.
- Referenced columns must exist in the input table: `outcome_col`, `treatment_col`, `instrument_col`.

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

from thomaslab.causal import instrumental_variable_2sls

result = instrumental_variable_2sls(
    df=sample_df,
    outcome_col='outcome',
    treatment_col='treatment',
    instrument_col='instrument',
    covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `calculate_propensity_scores`
- `calculate_stabilized_ipw`
- `match_cohorts`
- `check_covariate_balance`
- `fit_survival_model`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal.py#L590`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L590)
- Repository search: [instrumental_variable_2sls](https://github.com/appsplorer/thomaslab-core/search?q=instrumental_variable_2sls&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Fit a linear two-stage least-squares instrumental-variable model.

Exogenous covariates are included in both the structural design matrix and the
instrument matrix, as required by ``statsmodels`` IV2SLS. The function also
reports a first-stage partial F test for the instrument. Instrument relevance,
exclusion restriction, and exchangeability are design assumptions and cannot be
proven by this function.

### API inspection

~~~python
import inspect
from thomaslab.causal import instrumental_variable_2sls

print(inspect.signature(instrumental_variable_2sls))
print(instrumental_variable_2sls.__doc__)
~~~

### Source

[`src/thomaslab/causal.py#L590`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal.py#L590)

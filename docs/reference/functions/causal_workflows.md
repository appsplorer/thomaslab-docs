# thomaslab.causal_workflows

Higher-level diagnostics and estimators for observational causal workflows.

These utilities make assumptions and diagnostics visible. No function can establish
exchangeability or eliminate unmeasured confounding from observational data.

## Research-use boundary

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

## Self-service orientation

- Related guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 10

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.causal_workflows.effective_sample_size -->
## effective_sample_size

### Purpose

Return Kish effective sample size for non-negative weights.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def effective_sample_size(weights: pd.Series | np.ndarray) -> float
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `weights` | `weights: pd.Series \| np.ndarray` | Yes | Analysis weight/propensity input. Inspect support, positivity, extremes, and effective sample size where applicable. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `weights`.

### Returns

`float`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.causal_workflows import effective_sample_size

result = effective_sample_size(
    weights=sample_series
)

print(result)
~~~

### Related functions

- `assess_propensity_overlap`
- `assess_positivity`
- `trim_extreme_weights`
- `weighted_smd_table`
- `estimate_iptw_binary_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_workflows.py#L36`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L36)
- Repository search: [effective_sample_size](https://github.com/appsplorer/thomaslab-core/search?q=effective_sample_size&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return Kish effective sample size for non-negative weights.

### API inspection

~~~python
import inspect
from thomaslab.causal_workflows import effective_sample_size

print(inspect.signature(effective_sample_size))
print(effective_sample_size.__doc__)
~~~

### Source

[`src/thomaslab/causal_workflows.py#L36`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L36)

---

<!-- callable:thomaslab.causal_workflows.assess_propensity_overlap -->
## assess_propensity_overlap

### Purpose

Summarize empirical propensity-score overlap and common support.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def assess_propensity_overlap( df: pd.DataFrame, treatment_col: str, propensity_col: str, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `propensity_col` | `propensity_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `propensity_col`.
- Referenced columns must exist in the input table: `treatment_col`, `propensity_col`.

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

from thomaslab.causal_workflows import assess_propensity_overlap

result = assess_propensity_overlap(
    df=sample_df,
    treatment_col='treatment',
    propensity_col='propensity'
)

print(result)
~~~

### Related functions

- `effective_sample_size`
- `assess_positivity`
- `trim_extreme_weights`
- `weighted_smd_table`
- `estimate_iptw_binary_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_workflows.py#L45`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L45)
- Repository search: [assess_propensity_overlap](https://github.com/appsplorer/thomaslab-core/search?q=assess_propensity_overlap&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize empirical propensity-score overlap and common support.

### API inspection

~~~python
import inspect
from thomaslab.causal_workflows import assess_propensity_overlap

print(inspect.signature(assess_propensity_overlap))
print(assess_propensity_overlap.__doc__)
~~~

### Source

[`src/thomaslab/causal_workflows.py#L45`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L45)

---

<!-- callable:thomaslab.causal_workflows.assess_positivity -->
## assess_positivity

### Purpose

Summarize empirical near-positivity violations and optional weight stability.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def assess_positivity( df: pd.DataFrame, treatment_col: str, propensity_col: str, *, lower: float = 0.05, upper: float = 0.95, weight_col: str | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `propensity_col` | `propensity_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `lower` | `lower: float = 0.05` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `upper` | `upper: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `weight_col` | `weight_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `propensity_col`.
- Referenced columns must exist in the input table: `treatment_col`, `propensity_col`, `weight_col`.

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

from thomaslab.causal_workflows import assess_positivity

result = assess_positivity(
    df=sample_df,
    treatment_col='treatment',
    propensity_col='propensity'
)

print(result)
~~~

### Related functions

- `effective_sample_size`
- `assess_propensity_overlap`
- `trim_extreme_weights`
- `weighted_smd_table`
- `estimate_iptw_binary_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_workflows.py#L80`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L80)
- Repository search: [assess_positivity](https://github.com/appsplorer/thomaslab-core/search?q=assess_positivity&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize empirical near-positivity violations and optional weight stability.

### API inspection

~~~python
import inspect
from thomaslab.causal_workflows import assess_positivity

print(inspect.signature(assess_positivity))
print(assess_positivity.__doc__)
~~~

### Source

[`src/thomaslab/causal_workflows.py#L80`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L80)

---

<!-- callable:thomaslab.causal_workflows.trim_extreme_weights -->
## trim_extreme_weights

### Purpose

Winsorize weights at explicit quantiles while preserving index/name.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def trim_extreme_weights( weights: pd.Series, *, quantiles: tuple[float, float] = (0.01, 0.99), ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `weights` | `weights: pd.Series` | Yes | Analysis weight/propensity input. Inspect support, positivity, extremes, and effective sample size where applicable. |
| `quantiles` | `quantiles: tuple[float, float] = (0.01, 0.99)` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `weights`.

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

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.causal_workflows import trim_extreme_weights

result = trim_extreme_weights(
    weights=sample_series
)

print(result)
~~~

### Related functions

- `effective_sample_size`
- `assess_propensity_overlap`
- `assess_positivity`
- `weighted_smd_table`
- `estimate_iptw_binary_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_workflows.py#L124`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L124)
- Repository search: [trim_extreme_weights](https://github.com/appsplorer/thomaslab-core/search?q=trim_extreme_weights&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Winsorize weights at explicit quantiles while preserving index/name.

### API inspection

~~~python
import inspect
from thomaslab.causal_workflows import trim_extreme_weights

print(inspect.signature(trim_extreme_weights))
print(trim_extreme_weights.__doc__)
~~~

### Source

[`src/thomaslab/causal_workflows.py#L124`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L124)

---

<!-- callable:thomaslab.causal_workflows.weighted_smd_table -->
## weighted_smd_table

### Purpose

Calculate absolute standardized mean differences with optional weights.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def weighted_smd_table( df: pd.DataFrame, treatment_col: str, covariates: list[str], *, weight_col: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: list[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `weight_col` | `weight_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `covariates`.
- Referenced columns must exist in the input table: `treatment_col`, `weight_col`.

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

from thomaslab.causal_workflows import weighted_smd_table

result = weighted_smd_table(
    df=sample_df,
    treatment_col='treatment',
    covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `effective_sample_size`
- `assess_propensity_overlap`
- `assess_positivity`
- `trim_extreme_weights`
- `estimate_iptw_binary_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_workflows.py#L157`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L157)
- Repository search: [weighted_smd_table](https://github.com/appsplorer/thomaslab-core/search?q=weighted_smd_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate absolute standardized mean differences with optional weights.

Categorical variables use the maximum one-vs-rest absolute SMD across observed
levels. The 0.1 column is a reporting convention, not a universal pass/fail law.

### API inspection

~~~python
import inspect
from thomaslab.causal_workflows import weighted_smd_table

print(inspect.signature(weighted_smd_table))
print(weighted_smd_table.__doc__)
~~~

### Source

[`src/thomaslab/causal_workflows.py#L157`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L157)

---

<!-- callable:thomaslab.causal_workflows.estimate_iptw_binary_effects -->
## estimate_iptw_binary_effects

### Purpose

Estimate weighted binary risks, risk difference and risk ratio.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def estimate_iptw_binary_effects( df: pd.DataFrame, treatment_col: str, outcome_col: str, weight_col: str, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `weight_col` | `weight_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `outcome_col`, `weight_col`.
- Referenced columns must exist in the input table: `treatment_col`, `outcome_col`, `weight_col`.

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

from thomaslab.causal_workflows import estimate_iptw_binary_effects

result = estimate_iptw_binary_effects(
    df=sample_df,
    treatment_col='treatment',
    outcome_col='outcome',
    weight_col='weight'
)

print(result)
~~~

### Related functions

- `effective_sample_size`
- `assess_propensity_overlap`
- `assess_positivity`
- `trim_extreme_weights`
- `weighted_smd_table`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_workflows.py#L246`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L246)
- Repository search: [estimate_iptw_binary_effects](https://github.com/appsplorer/thomaslab-core/search?q=estimate_iptw_binary_effects&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate weighted binary risks, risk difference and risk ratio.

The function treats supplied weights as fixed and therefore returns point
estimates only. Obtain uncertainty with a design-appropriate bootstrap or robust
estimator that re-fits all nuisance models required by the study protocol.

### API inspection

~~~python
import inspect
from thomaslab.causal_workflows import estimate_iptw_binary_effects

print(inspect.signature(estimate_iptw_binary_effects))
print(estimate_iptw_binary_effects.__doc__)
~~~

### Source

[`src/thomaslab/causal_workflows.py#L246`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L246)

---

<!-- callable:thomaslab.causal_workflows.calculate_e_value -->
## calculate_e_value

### Purpose

Calculate the E-value for a positive risk-ratio-scale association.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_e_value( risk_ratio: float, *, ci_lower: float | None = None, ci_upper: float | None = None, ) -> dict[str, float | None]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `risk_ratio` | `risk_ratio: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `ci_lower` | `ci_lower: float \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `ci_upper` | `ci_upper: float \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `risk_ratio`.

### Returns

`dict[str, float | None]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.causal_workflows import calculate_e_value

result = calculate_e_value(
    risk_ratio=0.5
)

print(result)
~~~

### Related functions

- `effective_sample_size`
- `assess_propensity_overlap`
- `assess_positivity`
- `trim_extreme_weights`
- `weighted_smd_table`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_workflows.py#L287`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L287)
- Repository search: [calculate_e_value](https://github.com/appsplorer/thomaslab-core/search?q=calculate_e_value&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate the E-value for a positive risk-ratio-scale association.

Ratios below 1 are inverted before applying the standard E-value formula. If a
confidence interval is supplied, the bound closest to the null is used. This is a
sensitivity metric for unmeasured confounding, not proof that confounding is absent.

### API inspection

~~~python
import inspect
from thomaslab.causal_workflows import calculate_e_value

print(inspect.signature(calculate_e_value))
print(calculate_e_value.__doc__)
~~~

### Source

[`src/thomaslab/causal_workflows.py#L287`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L287)

---

<!-- callable:thomaslab.causal_workflows.estimate_aipw_ate -->
## estimate_aipw_ate

### Purpose

Estimate an average treatment effect using cross-fitted AIPW.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def estimate_aipw_ate( df: pd.DataFrame, treatment_col: str, outcome_col: str, covariates: list[str], *, outcome_type: str = "binary", n_splits: int = 5, propensity_clip: float = 0.01, random_state: int = 42, alpha: float = 0.05, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: list[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `outcome_type` | `outcome_type: str = 'binary'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `n_splits` | `n_splits: int = 5` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `propensity_clip` | `propensity_clip: float = 0.01` | No | Analysis weight/propensity input. Inspect support, positivity, extremes, and effective sample size where applicable. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |
| `alpha` | `alpha: float = 0.05` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `outcome_col`, `covariates`.
- Referenced columns must exist in the input table: `treatment_col`, `outcome_col`.

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

from thomaslab.causal_workflows import estimate_aipw_ate

result = estimate_aipw_ate(
    df=sample_df,
    treatment_col='treatment',
    outcome_col='outcome',
    covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `effective_sample_size`
- `assess_propensity_overlap`
- `assess_positivity`
- `trim_extreme_weights`
- `weighted_smd_table`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_workflows.py#L333`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L333)
- Repository search: [estimate_aipw_ate](https://github.com/appsplorer/thomaslab-core/search?q=estimate_aipw_ate&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate an average treatment effect using cross-fitted AIPW.

For binary outcomes the effect is an absolute risk difference. Confidence
intervals use the empirical influence-function standard error. Valid causal
interpretation still requires consistency, exchangeability, positivity, and a
well-defined intervention; doubly robust estimation does not solve unmeasured
confounding.

### API inspection

~~~python
import inspect
from thomaslab.causal_workflows import estimate_aipw_ate

print(inspect.signature(estimate_aipw_ate))
print(estimate_aipw_ate.__doc__)
~~~

### Source

[`src/thomaslab/causal_workflows.py#L333`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L333)

---

<!-- callable:thomaslab.causal_workflows.run_iptw_diagnostics -->
## run_iptw_diagnostics

### Purpose

Estimate propensity scores/weights and return overlap and balance diagnostics.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def run_iptw_diagnostics( df: pd.DataFrame, treatment_col: str, covariates: list[str], *, trim_quantiles: tuple[float, float] | None = (0.01, 0.99), ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: list[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `trim_quantiles` | `trim_quantiles: tuple[float, float] \| None = (0.01, 0.99)` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `covariates`.
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

from thomaslab.causal_workflows import run_iptw_diagnostics

result = run_iptw_diagnostics(
    df=sample_df,
    treatment_col='treatment',
    covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `effective_sample_size`
- `assess_propensity_overlap`
- `assess_positivity`
- `trim_extreme_weights`
- `weighted_smd_table`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_workflows.py#L469`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L469)
- Repository search: [run_iptw_diagnostics](https://github.com/appsplorer/thomaslab-core/search?q=run_iptw_diagnostics&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate propensity scores/weights and return overlap and balance diagnostics.

### API inspection

~~~python
import inspect
from thomaslab.causal_workflows import run_iptw_diagnostics

print(inspect.signature(run_iptw_diagnostics))
print(run_iptw_diagnostics.__doc__)
~~~

### Source

[`src/thomaslab/causal_workflows.py#L469`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L469)

---

<!-- callable:thomaslab.causal_workflows.standardize_effect_table -->
## standardize_effect_table

### Purpose

Normalize heterogeneous effect-result dictionaries into one reporting table.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def standardize_effect_table(records: list[dict[str, Any]]) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `records` | `records: list[dict[str, Any]]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `records`.

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
from thomaslab.causal_workflows import standardize_effect_table

result = standardize_effect_table(
    records={}
)

print(result)
~~~

### Related functions

- `effective_sample_size`
- `assess_propensity_overlap`
- `assess_positivity`
- `trim_extreme_weights`
- `weighted_smd_table`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_workflows.py#L493`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L493)
- Repository search: [standardize_effect_table](https://github.com/appsplorer/thomaslab-core/search?q=standardize_effect_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Normalize heterogeneous effect-result dictionaries into one reporting table.

### API inspection

~~~python
import inspect
from thomaslab.causal_workflows import standardize_effect_table

print(inspect.signature(standardize_effect_table))
print(standardize_effect_table.__doc__)
~~~

### Source

[`src/thomaslab/causal_workflows.py#L493`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_workflows.py#L493)

# thomaslab.transportability

Causal transportability and multisite generalizability utilities.

This module supports source-to-target causal-effect transport under explicit
sampling/participation assumptions. Source cohorts contain treatment and outcome
data; external target populations may contain only baseline covariates.

Successful computation does not establish conditional exchangeability across
populations, treatment exchangeability within the source, positivity, consistency,
measurement comparability, or transportability.

## Research-use boundary

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

## Self-service orientation

- Related guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 9

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.transportability.validate_transport_inputs -->
## validate_transport_inputs

### Purpose

Validate source and target inputs without requiring target outcomes.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_transport_inputs( source_df: pd.DataFrame, target_df: pd.DataFrame, *, covariates: Sequence[str], treatment_col: str, outcome_col: str, outcome_type: str = "binary", ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `source_df` | `source_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `target_df` | `target_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `covariates` | `covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_type` | `outcome_type: str = 'binary'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `source_df`, `target_df`, `covariates`, `treatment_col`, `outcome_col`.
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

from thomaslab.transportability import validate_transport_inputs

result = validate_transport_inputs(
    source_df=sample_df,
    target_df=sample_df,
    covariates=["feature_a", "feature_b"],
    treatment_col='treatment',
    outcome_col='outcome'
)

print(result)
~~~

### Related functions

- `fit_sampling_odds_weights`
- `transport_positivity_diagnostics`
- `estimate_target_standardization`
- `estimate_transport_aipw`
- `bootstrap_transport_aipw`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/transportability.py#L84`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/transportability.py#L84)
- Repository search: [validate_transport_inputs](https://github.com/appsplorer/thomaslab-core/search?q=validate_transport_inputs&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate source and target inputs without requiring target outcomes.

### API inspection

~~~python
import inspect
from thomaslab.transportability import validate_transport_inputs

print(inspect.signature(validate_transport_inputs))
print(validate_transport_inputs.__doc__)
~~~

### Source

[`src/thomaslab/transportability.py#L84`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/transportability.py#L84)

---

<!-- callable:thomaslab.transportability.fit_sampling_odds_weights -->
## fit_sampling_odds_weights

### Purpose

Fit P(source|X) and source inverse-odds-of-sampling weights.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fit_sampling_odds_weights( source_df: pd.DataFrame, target_df: pd.DataFrame, *, covariates: Sequence[str], probability_clip: float = 0.01, stabilized: bool = False, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `source_df` | `source_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `target_df` | `target_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `covariates` | `covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `probability_clip` | `probability_clip: float = 0.01` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `stabilized` | `stabilized: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `source_df`, `target_df`, `covariates`.

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

from thomaslab.transportability import fit_sampling_odds_weights

result = fit_sampling_odds_weights(
    source_df=sample_df,
    target_df=sample_df,
    covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `validate_transport_inputs`
- `transport_positivity_diagnostics`
- `estimate_target_standardization`
- `estimate_transport_aipw`
- `bootstrap_transport_aipw`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/transportability.py#L124`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/transportability.py#L124)
- Repository search: [fit_sampling_odds_weights](https://github.com/appsplorer/thomaslab-core/search?q=fit_sampling_odds_weights&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Fit P(source|X) and source inverse-odds-of-sampling weights.

### API inspection

~~~python
import inspect
from thomaslab.transportability import fit_sampling_odds_weights

print(inspect.signature(fit_sampling_odds_weights))
print(fit_sampling_odds_weights.__doc__)
~~~

### Source

[`src/thomaslab/transportability.py#L124`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/transportability.py#L124)

---

<!-- callable:thomaslab.transportability.transport_positivity_diagnostics -->
## transport_positivity_diagnostics

### Purpose

Summarize sampling support and source transport-weight stability.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def transport_positivity_diagnostics( sampling_result: dict[str, Any], *, low_source_probability: float = 0.05, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `sampling_result` | `sampling_result: dict[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `low_source_probability` | `low_source_probability: float = 0.05` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `sampling_result`.

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
from thomaslab.transportability import transport_positivity_diagnostics

result = transport_positivity_diagnostics(
    sampling_result={}
)

print(result)
~~~

### Related functions

- `validate_transport_inputs`
- `fit_sampling_odds_weights`
- `estimate_target_standardization`
- `estimate_transport_aipw`
- `bootstrap_transport_aipw`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/transportability.py#L183`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/transportability.py#L183)
- Repository search: [transport_positivity_diagnostics](https://github.com/appsplorer/thomaslab-core/search?q=transport_positivity_diagnostics&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize sampling support and source transport-weight stability.

### API inspection

~~~python
import inspect
from thomaslab.transportability import transport_positivity_diagnostics

print(inspect.signature(transport_positivity_diagnostics))
print(transport_positivity_diagnostics.__doc__)
~~~

### Source

[`src/thomaslab/transportability.py#L183`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/transportability.py#L183)

---

<!-- callable:thomaslab.transportability.estimate_target_standardization -->
## estimate_target_standardization

### Purpose

Standardize source outcome models over external target covariates.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def estimate_target_standardization( source_df: pd.DataFrame, target_df: pd.DataFrame, *, covariates: Sequence[str], treatment_col: str, outcome_col: str, outcome_type: str = "binary", ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `source_df` | `source_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `target_df` | `target_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `covariates` | `covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_type` | `outcome_type: str = 'binary'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `source_df`, `target_df`, `covariates`, `treatment_col`, `outcome_col`.
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

from thomaslab.transportability import estimate_target_standardization

result = estimate_target_standardization(
    source_df=sample_df,
    target_df=sample_df,
    covariates=["feature_a", "feature_b"],
    treatment_col='treatment',
    outcome_col='outcome'
)

print(result)
~~~

### Related functions

- `validate_transport_inputs`
- `fit_sampling_odds_weights`
- `transport_positivity_diagnostics`
- `estimate_transport_aipw`
- `bootstrap_transport_aipw`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/transportability.py#L263`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/transportability.py#L263)
- Repository search: [estimate_target_standardization](https://github.com/appsplorer/thomaslab-core/search?q=estimate_target_standardization&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Standardize source outcome models over external target covariates.

### API inspection

~~~python
import inspect
from thomaslab.transportability import estimate_target_standardization

print(inspect.signature(estimate_target_standardization))
print(estimate_target_standardization.__doc__)
~~~

### Source

[`src/thomaslab/transportability.py#L263`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/transportability.py#L263)

---

<!-- callable:thomaslab.transportability.estimate_transport_aipw -->
## estimate_transport_aipw

### Purpose

Estimate a target-population effect with cross-fitted transport AIPW.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def estimate_transport_aipw( source_df: pd.DataFrame, target_df: pd.DataFrame, *, covariates: Sequence[str], treatment_col: str, outcome_col: str, outcome_type: str = "binary", n_splits: int = 5, sampling_clip: float = 0.01, treatment_clip: float = 0.01, random_state: int = 42, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `source_df` | `source_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `target_df` | `target_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `covariates` | `covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_type` | `outcome_type: str = 'binary'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `n_splits` | `n_splits: int = 5` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `sampling_clip` | `sampling_clip: float = 0.01` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `treatment_clip` | `treatment_clip: float = 0.01` | No | Treatment/exposure definition supplied by the study specification; do not infer clinical meaning from labels alone. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `source_df`, `target_df`, `covariates`, `treatment_col`, `outcome_col`.
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

from thomaslab.transportability import estimate_transport_aipw

result = estimate_transport_aipw(
    source_df=sample_df,
    target_df=sample_df,
    covariates=["feature_a", "feature_b"],
    treatment_col='treatment',
    outcome_col='outcome'
)

print(result)
~~~

### Related functions

- `validate_transport_inputs`
- `fit_sampling_odds_weights`
- `transport_positivity_diagnostics`
- `estimate_target_standardization`
- `bootstrap_transport_aipw`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/transportability.py#L315`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/transportability.py#L315)
- Repository search: [estimate_transport_aipw](https://github.com/appsplorer/thomaslab-core/search?q=estimate_transport_aipw&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate a target-population effect with cross-fitted transport AIPW.

Sampling nuisance models use pooled source and target training rows.
Treatment and outcome nuisance models use source training rows only.
Target outcomes are never required or used.

### API inspection

~~~python
import inspect
from thomaslab.transportability import estimate_transport_aipw

print(inspect.signature(estimate_transport_aipw))
print(estimate_transport_aipw.__doc__)
~~~

### Source

[`src/thomaslab/transportability.py#L315`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/transportability.py#L315)

---

<!-- callable:thomaslab.transportability.bootstrap_transport_aipw -->
## bootstrap_transport_aipw

### Purpose

Bootstrap source and target populations independently and refit nuisances.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def bootstrap_transport_aipw( source_df: pd.DataFrame, target_df: pd.DataFrame, *, covariates: Sequence[str], treatment_col: str, outcome_col: str, outcome_type: str = "binary", n_bootstrap: int = 200, n_splits: int = 5, sampling_clip: float = 0.01, treatment_clip: float = 0.01, ci: float = 0.95, random_state: int = 42, ) -> dict[str, pd.DataFrame]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `source_df` | `source_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `target_df` | `target_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `covariates` | `covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_type` | `outcome_type: str = 'binary'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `n_bootstrap` | `n_bootstrap: int = 200` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `n_splits` | `n_splits: int = 5` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `sampling_clip` | `sampling_clip: float = 0.01` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `treatment_clip` | `treatment_clip: float = 0.01` | No | Treatment/exposure definition supplied by the study specification; do not infer clinical meaning from labels alone. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `source_df`, `target_df`, `covariates`, `treatment_col`, `outcome_col`.
- Referenced columns must exist in the input table: `treatment_col`, `outcome_col`.

### Returns

`dict[str, pd.DataFrame]`

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

from thomaslab.transportability import bootstrap_transport_aipw

result = bootstrap_transport_aipw(
    source_df=sample_df,
    target_df=sample_df,
    covariates=["feature_a", "feature_b"],
    treatment_col='treatment',
    outcome_col='outcome'
)

print(result)
~~~

### Related functions

- `validate_transport_inputs`
- `fit_sampling_odds_weights`
- `transport_positivity_diagnostics`
- `estimate_target_standardization`
- `estimate_transport_aipw`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/transportability.py#L485`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/transportability.py#L485)
- Repository search: [bootstrap_transport_aipw](https://github.com/appsplorer/thomaslab-core/search?q=bootstrap_transport_aipw&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Bootstrap source and target populations independently and refit nuisances.

### API inspection

~~~python
import inspect
from thomaslab.transportability import bootstrap_transport_aipw

print(inspect.signature(bootstrap_transport_aipw))
print(bootstrap_transport_aipw.__doc__)
~~~

### Source

[`src/thomaslab/transportability.py#L485`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/transportability.py#L485)

---

<!-- callable:thomaslab.transportability.site_specific_causal_effects -->
## site_specific_causal_effects

### Purpose

Estimate within-site AIPW contrasts without ranking sites.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def site_specific_causal_effects( df: pd.DataFrame, *, site_col: str, treatment_col: str, outcome_col: str, covariates: Sequence[str], outcome_type: str = "binary", n_splits: int = 5, random_state: int = 42, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `site_col` | `site_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `outcome_type` | `outcome_type: str = 'binary'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `n_splits` | `n_splits: int = 5` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `site_col`, `treatment_col`, `outcome_col`, `covariates`.
- Referenced columns must exist in the input table: `site_col`, `treatment_col`, `outcome_col`.

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

from thomaslab.transportability import site_specific_causal_effects

result = site_specific_causal_effects(
    df=sample_df,
    site_col='site',
    treatment_col='treatment',
    outcome_col='outcome',
    covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `validate_transport_inputs`
- `fit_sampling_odds_weights`
- `transport_positivity_diagnostics`
- `estimate_target_standardization`
- `estimate_transport_aipw`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/transportability.py#L566`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/transportability.py#L566)
- Repository search: [site_specific_causal_effects](https://github.com/appsplorer/thomaslab-core/search?q=site_specific_causal_effects&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate within-site AIPW contrasts without ranking sites.

### API inspection

~~~python
import inspect
from thomaslab.transportability import site_specific_causal_effects

print(inspect.signature(site_specific_causal_effects))
print(site_specific_causal_effects.__doc__)
~~~

### Source

[`src/thomaslab/transportability.py#L566`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/transportability.py#L566)

---

<!-- callable:thomaslab.transportability.meta_analyze_site_effects -->
## meta_analyze_site_effects

### Purpose

Pool site effects using fixed or DerSimonian-Laird random effects.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def meta_analyze_site_effects( effects: pd.DataFrame, *, effect_col: str = "estimate", se_col: str = "std_error", method: str = "random", ci: float = 0.95, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `effects` | `effects: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `effect_col` | `effect_col: str = 'estimate'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `se_col` | `se_col: str = 'std_error'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `method` | `method: str = 'random'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `effects`.
- Referenced columns must exist in the input table: `effect_col`, `se_col`.

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

from thomaslab.transportability import meta_analyze_site_effects

result = meta_analyze_site_effects(
    effects=sample_df
)

print(result)
~~~

### Related functions

- `validate_transport_inputs`
- `fit_sampling_odds_weights`
- `transport_positivity_diagnostics`
- `estimate_target_standardization`
- `estimate_transport_aipw`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/transportability.py#L624`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/transportability.py#L624)
- Repository search: [meta_analyze_site_effects](https://github.com/appsplorer/thomaslab-core/search?q=meta_analyze_site_effects&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Pool site effects using fixed or DerSimonian-Laird random effects.

### API inspection

~~~python
import inspect
from thomaslab.transportability import meta_analyze_site_effects

print(inspect.signature(meta_analyze_site_effects))
print(meta_analyze_site_effects.__doc__)
~~~

### Source

[`src/thomaslab/transportability.py#L624`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/transportability.py#L624)

---

<!-- callable:thomaslab.transportability.leave_one_site_out_meta_analysis -->
## leave_one_site_out_meta_analysis

### Purpose

Repeat meta-analysis after leaving out each site.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def leave_one_site_out_meta_analysis( effects: pd.DataFrame, *, site_col: str = "site", effect_col: str = "estimate", se_col: str = "std_error", method: str = "random", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `effects` | `effects: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `site_col` | `site_col: str = 'site'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `effect_col` | `effect_col: str = 'estimate'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `se_col` | `se_col: str = 'std_error'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `method` | `method: str = 'random'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `effects`.
- Referenced columns must exist in the input table: `site_col`, `effect_col`, `se_col`.

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

from thomaslab.transportability import leave_one_site_out_meta_analysis

result = leave_one_site_out_meta_analysis(
    effects=sample_df
)

print(result)
~~~

### Related functions

- `validate_transport_inputs`
- `fit_sampling_odds_weights`
- `transport_positivity_diagnostics`
- `estimate_target_standardization`
- `estimate_transport_aipw`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/transportability.py#L672`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/transportability.py#L672)
- Repository search: [leave_one_site_out_meta_analysis](https://github.com/appsplorer/thomaslab-core/search?q=leave_one_site_out_meta_analysis&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Repeat meta-analysis after leaving out each site.

### API inspection

~~~python
import inspect
from thomaslab.transportability import leave_one_site_out_meta_analysis

print(inspect.signature(leave_one_site_out_meta_analysis))
print(leave_one_site_out_meta_analysis.__doc__)
~~~

### Source

[`src/thomaslab/transportability.py#L672`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/transportability.py#L672)

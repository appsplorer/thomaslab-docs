# thomaslab.causal_mediation

Causal mediation and treatment-mechanism research utilities.

The module supports transparent parametric mediation analyses for a binary exposure,
one mediator at a time, and continuous or binary outcomes. Effects are standardized
by Monte Carlo g-computation and are labelled interventional analogues rather than
automatically interpreted as natural direct/indirect effects.

The software does not establish the assumptions needed for causal mediation.
In particular, treatment-outcome, treatment-mediator, and mediator-outcome
exchangeability, correct temporal ordering, consistency, positivity, and adequate
model specification remain study-design requirements.

## Research-use boundary

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

## Self-service orientation

- Related guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 8

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.causal_mediation.validate_mediation_inputs -->
## validate_mediation_inputs

### Purpose

Validate a single-mediator analysis table without asserting causal validity.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_mediation_inputs( df: pd.DataFrame, *, treatment_col: str, mediator_col: str, outcome_col: str, covariates: Sequence[str] = (), mediator_type: str = "continuous", outcome_type: str = "continuous", ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `mediator_col` | `mediator_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str] = ()` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `mediator_type` | `mediator_type: str = 'continuous'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `outcome_type` | `outcome_type: str = 'continuous'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `mediator_col`, `outcome_col`.
- Referenced columns must exist in the input table: `treatment_col`, `mediator_col`, `outcome_col`.

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

from thomaslab.causal_mediation import validate_mediation_inputs

result = validate_mediation_inputs(
    df=sample_df,
    treatment_col='treatment',
    mediator_col='mediator',
    outcome_col='outcome'
)

print(result)
~~~

### Related functions

- `validate_mediation_temporality`
- `fit_interventional_mediation`
- `mediation_effect_table`
- `mediation_design_diagnostics`
- `bootstrap_mediation_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_mediation.py#L44`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_mediation.py#L44)
- Repository search: [validate_mediation_inputs](https://github.com/appsplorer/thomaslab-core/search?q=validate_mediation_inputs&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate a single-mediator analysis table without asserting causal validity.

### API inspection

~~~python
import inspect
from thomaslab.causal_mediation import validate_mediation_inputs

print(inspect.signature(validate_mediation_inputs))
print(validate_mediation_inputs.__doc__)
~~~

### Source

[`src/thomaslab/causal_mediation.py#L44`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_mediation.py#L44)

---

<!-- callable:thomaslab.causal_mediation.validate_mediation_temporality -->
## validate_mediation_temporality

### Purpose

Audit exposure→mediator→outcome temporal ordering.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_mediation_temporality( df: pd.DataFrame, *, exposure_time_col: str, mediator_time_col: str, outcome_time_col: str, allow_ties: bool = False, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `exposure_time_col` | `exposure_time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `mediator_time_col` | `mediator_time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_time_col` | `outcome_time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `allow_ties` | `allow_ties: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `exposure_time_col`, `mediator_time_col`, `outcome_time_col`.
- Referenced columns must exist in the input table: `exposure_time_col`, `mediator_time_col`, `outcome_time_col`.

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

from thomaslab.causal_mediation import validate_mediation_temporality

result = validate_mediation_temporality(
    df=sample_df,
    exposure_time_col='exposure_time',
    mediator_time_col='mediator_time',
    outcome_time_col='outcome_time'
)

print(result)
~~~

### Related functions

- `validate_mediation_inputs`
- `fit_interventional_mediation`
- `mediation_effect_table`
- `mediation_design_diagnostics`
- `bootstrap_mediation_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_mediation.py#L94`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_mediation.py#L94)
- Repository search: [validate_mediation_temporality](https://github.com/appsplorer/thomaslab-core/search?q=validate_mediation_temporality&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Audit exposure→mediator→outcome temporal ordering.

### API inspection

~~~python
import inspect
from thomaslab.causal_mediation import validate_mediation_temporality

print(inspect.signature(validate_mediation_temporality))
print(validate_mediation_temporality.__doc__)
~~~

### Source

[`src/thomaslab/causal_mediation.py#L94`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_mediation.py#L94)

---

<!-- callable:thomaslab.causal_mediation.fit_interventional_mediation -->
## fit_interventional_mediation

### Purpose

Estimate standardized interventional direct, indirect and total effects.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fit_interventional_mediation( df: pd.DataFrame, *, treatment_col: str, mediator_col: str, outcome_col: str, covariates: Sequence[str] = (), mediator_type: str = "continuous", outcome_type: str = "continuous", include_interaction: bool = True, n_mc: int = 5000, random_state: int | None = None, mediator_shift_sd: float = 0.0, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `mediator_col` | `mediator_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str] = ()` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `mediator_type` | `mediator_type: str = 'continuous'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `outcome_type` | `outcome_type: str = 'continuous'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `include_interaction` | `include_interaction: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `n_mc` | `n_mc: int = 5000` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int \| None = None` | No | Reproducibility seed. Record it in the study bundle. |
| `mediator_shift_sd` | `mediator_shift_sd: float = 0.0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `mediator_col`, `outcome_col`.
- Referenced columns must exist in the input table: `treatment_col`, `mediator_col`, `outcome_col`.

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

from thomaslab.causal_mediation import fit_interventional_mediation

result = fit_interventional_mediation(
    df=sample_df,
    treatment_col='treatment',
    mediator_col='mediator',
    outcome_col='outcome'
)

print(result)
~~~

### Related functions

- `validate_mediation_inputs`
- `validate_mediation_temporality`
- `mediation_effect_table`
- `mediation_design_diagnostics`
- `bootstrap_mediation_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_mediation.py#L265`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_mediation.py#L265)
- Repository search: [fit_interventional_mediation](https://github.com/appsplorer/thomaslab-core/search?q=fit_interventional_mediation&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate standardized interventional direct, indirect and total effects.

The decomposition uses:
  total = E[Y(1,M(1))] - E[Y(0,M(0))]
  direct = E[Y(1,M(0))] - E[Y(0,M(0))]
  indirect = E[Y(1,M(1))] - E[Y(1,M(0))]

For binary outcomes, all effects are risk differences.

### API inspection

~~~python
import inspect
from thomaslab.causal_mediation import fit_interventional_mediation

print(inspect.signature(fit_interventional_mediation))
print(fit_interventional_mediation.__doc__)
~~~

### Source

[`src/thomaslab/causal_mediation.py#L265`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_mediation.py#L265)

---

<!-- callable:thomaslab.causal_mediation.mediation_effect_table -->
## mediation_effect_table

### Purpose

Normalize a mediation result into one row per effect component.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def mediation_effect_table(result: Mapping[str, Any]) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `result` | `result: Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

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
from thomaslab.causal_mediation import mediation_effect_table

result = mediation_effect_table(
    result={}
)

print(result)
~~~

### Related functions

- `validate_mediation_inputs`
- `validate_mediation_temporality`
- `fit_interventional_mediation`
- `mediation_design_diagnostics`
- `bootstrap_mediation_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_mediation.py#L362`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_mediation.py#L362)
- Repository search: [mediation_effect_table](https://github.com/appsplorer/thomaslab-core/search?q=mediation_effect_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Normalize a mediation result into one row per effect component.

### API inspection

~~~python
import inspect
from thomaslab.causal_mediation import mediation_effect_table

print(inspect.signature(mediation_effect_table))
print(mediation_effect_table.__doc__)
~~~

### Source

[`src/thomaslab/causal_mediation.py#L362`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_mediation.py#L362)

---

<!-- callable:thomaslab.causal_mediation.mediation_design_diagnostics -->
## mediation_design_diagnostics

### Purpose

Summarize measured support and explicitly mark untestable assumptions.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def mediation_design_diagnostics( df: pd.DataFrame, *, treatment_col: str, mediator_col: str, outcome_col: str, covariates: Sequence[str] = (), mediator_type: str = "continuous", outcome_type: str = "continuous", propensity_threshold: float = 0.05, exposure_time_col: str | None = None, mediator_time_col: str | None = None, outcome_time_col: str | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `mediator_col` | `mediator_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str] = ()` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `mediator_type` | `mediator_type: str = 'continuous'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `outcome_type` | `outcome_type: str = 'continuous'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `propensity_threshold` | `propensity_threshold: float = 0.05` | No | Analysis weight/propensity input. Inspect support, positivity, extremes, and effective sample size where applicable. |
| `exposure_time_col` | `exposure_time_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `mediator_time_col` | `mediator_time_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_time_col` | `outcome_time_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `mediator_col`, `outcome_col`.
- Referenced columns must exist in the input table: `treatment_col`, `mediator_col`, `outcome_col`, `exposure_time_col`, `mediator_time_col`, `outcome_time_col`.

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

from thomaslab.causal_mediation import mediation_design_diagnostics

result = mediation_design_diagnostics(
    df=sample_df,
    treatment_col='treatment',
    mediator_col='mediator',
    outcome_col='outcome'
)

print(result)
~~~

### Related functions

- `validate_mediation_inputs`
- `validate_mediation_temporality`
- `fit_interventional_mediation`
- `mediation_effect_table`
- `bootstrap_mediation_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_mediation.py#L387`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_mediation.py#L387)
- Repository search: [mediation_design_diagnostics](https://github.com/appsplorer/thomaslab-core/search?q=mediation_design_diagnostics&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize measured support and explicitly mark untestable assumptions.

### API inspection

~~~python
import inspect
from thomaslab.causal_mediation import mediation_design_diagnostics

print(inspect.signature(mediation_design_diagnostics))
print(mediation_design_diagnostics.__doc__)
~~~

### Source

[`src/thomaslab/causal_mediation.py#L387`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_mediation.py#L387)

---

<!-- callable:thomaslab.causal_mediation.bootstrap_mediation_effects -->
## bootstrap_mediation_effects

### Purpose

Bootstrap the direct, indirect and total mediation effects.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def bootstrap_mediation_effects( df: pd.DataFrame, *, treatment_col: str, mediator_col: str, outcome_col: str, covariates: Sequence[str] = (), mediator_type: str = "continuous", outcome_type: str = "continuous", include_interaction: bool = True, cluster_col: str | None = None, n_boot: int = 500, n_mc: int = 2000, ci: float = 0.95, random_state: int | None = None, min_success_fraction: float = 0.8, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `mediator_col` | `mediator_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str] = ()` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `mediator_type` | `mediator_type: str = 'continuous'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `outcome_type` | `outcome_type: str = 'continuous'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `include_interaction` | `include_interaction: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `cluster_col` | `cluster_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `n_boot` | `n_boot: int = 500` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `n_mc` | `n_mc: int = 2000` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int \| None = None` | No | Reproducibility seed. Record it in the study bundle. |
| `min_success_fraction` | `min_success_fraction: float = 0.8` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `mediator_col`, `outcome_col`.
- Referenced columns must exist in the input table: `treatment_col`, `mediator_col`, `outcome_col`, `cluster_col`.

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

from thomaslab.causal_mediation import bootstrap_mediation_effects

result = bootstrap_mediation_effects(
    df=sample_df,
    treatment_col='treatment',
    mediator_col='mediator',
    outcome_col='outcome'
)

print(result)
~~~

### Related functions

- `validate_mediation_inputs`
- `validate_mediation_temporality`
- `fit_interventional_mediation`
- `mediation_effect_table`
- `mediation_design_diagnostics`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_mediation.py#L455`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_mediation.py#L455)
- Repository search: [bootstrap_mediation_effects](https://github.com/appsplorer/thomaslab-core/search?q=bootstrap_mediation_effects&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Bootstrap the direct, indirect and total mediation effects.

### API inspection

~~~python
import inspect
from thomaslab.causal_mediation import bootstrap_mediation_effects

print(inspect.signature(bootstrap_mediation_effects))
print(bootstrap_mediation_effects.__doc__)
~~~

### Source

[`src/thomaslab/causal_mediation.py#L455`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_mediation.py#L455)

---

<!-- callable:thomaslab.causal_mediation.mediator_shift_sensitivity -->
## mediator_shift_sensitivity

### Purpose

Perturb the treated mediator distribution by residual-SD units.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def mediator_shift_sensitivity( df: pd.DataFrame, *, treatment_col: str, mediator_col: str, outcome_col: str, covariates: Sequence[str] = (), outcome_type: str = "continuous", shift_sd_values: Sequence[float] = (-1.0, -0.5, 0.0, 0.5, 1.0), include_interaction: bool = True, n_mc: int = 3000, random_state: int | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `mediator_col` | `mediator_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str] = ()` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `outcome_type` | `outcome_type: str = 'continuous'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `shift_sd_values` | `shift_sd_values: Sequence[float] = (-1.0, -0.5, 0.0, 0.5, 1.0)` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `include_interaction` | `include_interaction: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `n_mc` | `n_mc: int = 3000` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int \| None = None` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `mediator_col`, `outcome_col`.
- Referenced columns must exist in the input table: `treatment_col`, `mediator_col`, `outcome_col`.

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

from thomaslab.causal_mediation import mediator_shift_sensitivity

result = mediator_shift_sensitivity(
    df=sample_df,
    treatment_col='treatment',
    mediator_col='mediator',
    outcome_col='outcome'
)

print(result)
~~~

### Related functions

- `validate_mediation_inputs`
- `validate_mediation_temporality`
- `fit_interventional_mediation`
- `mediation_effect_table`
- `mediation_design_diagnostics`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_mediation.py#L555`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_mediation.py#L555)
- Repository search: [mediator_shift_sensitivity](https://github.com/appsplorer/thomaslab-core/search?q=mediator_shift_sensitivity&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Perturb the treated mediator distribution by residual-SD units.

This is a mediator-model sensitivity analysis. It is not an unmeasured
mediator-outcome-confounding correction.

### API inspection

~~~python
import inspect
from thomaslab.causal_mediation import mediator_shift_sensitivity

print(inspect.signature(mediator_shift_sensitivity))
print(mediator_shift_sensitivity.__doc__)
~~~

### Source

[`src/thomaslab/causal_mediation.py#L555`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_mediation.py#L555)

---

<!-- callable:thomaslab.causal_mediation.analyze_multiple_mediators -->
## analyze_multiple_mediators

### Purpose

Run auditable one-mediator-at-a-time analyses for several mediators.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def analyze_multiple_mediators( df: pd.DataFrame, *, treatment_col: str, mediator_cols: Sequence[str], outcome_col: str, covariates: Sequence[str] = (), mediator_types: Mapping[str, str] | None = None, outcome_type: str = "continuous", include_interaction: bool = True, n_mc: int = 3000, random_state: int | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `mediator_cols` | `mediator_cols: Sequence[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str] = ()` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `mediator_types` | `mediator_types: Mapping[str, str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `outcome_type` | `outcome_type: str = 'continuous'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `include_interaction` | `include_interaction: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `n_mc` | `n_mc: int = 3000` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int \| None = None` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `mediator_cols`, `outcome_col`.
- Referenced columns must exist in the input table: `treatment_col`, `outcome_col`.

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

from thomaslab.causal_mediation import analyze_multiple_mediators

result = analyze_multiple_mediators(
    df=sample_df,
    treatment_col='treatment',
    mediator_cols=["feature_a", "feature_b"],
    outcome_col='outcome'
)

print(result)
~~~

### Related functions

- `validate_mediation_inputs`
- `validate_mediation_temporality`
- `fit_interventional_mediation`
- `mediation_effect_table`
- `mediation_design_diagnostics`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_mediation.py#L605`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_mediation.py#L605)
- Repository search: [analyze_multiple_mediators](https://github.com/appsplorer/thomaslab-core/search?q=analyze_multiple_mediators&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Run auditable one-mediator-at-a-time analyses for several mediators.

Results are not a joint/path-specific multi-mediator decomposition.

### API inspection

~~~python
import inspect
from thomaslab.causal_mediation import analyze_multiple_mediators

print(inspect.signature(analyze_multiple_mediators))
print(analyze_multiple_mediators.__doc__)
~~~

### Source

[`src/thomaslab/causal_mediation.py#L605`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_mediation.py#L605)

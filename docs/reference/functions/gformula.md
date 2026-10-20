# thomaslab.gformula

Parametric g-formula and sequential g-computation utilities.

This module complements the longitudinal weighting tools in
thomaslab.longitudinal_causal with outcome/state modeling and Monte Carlo
standardization under prespecified static or dynamic treatment regimes.

The implementation is deliberately explicit about temporal ordering:

* covariates on row t are interpreted as available at the start of period t;
* treatment A_t is assigned from the current history;
* the interval outcome Y_t is generated conditional on current history and A_t;
* among survivors, next-period time-varying covariates L_(t+1) are generated from
  current history and A_t.

These utilities do not establish sequential exchangeability, consistency,
positivity, correct model specification, or causal identification. They are
research tools for protocol-driven observational analyses.

## Research-use boundary

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

## Self-service orientation

- Related guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 8

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.gformula.validate_gformula_panel -->
## validate_gformula_panel

### Purpose

Audit the temporal panel expected by the parametric g-formula engine.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_gformula_panel( panel: pd.DataFrame, *, baseline_covariates: Sequence[str], time_varying_types: Mapping[str, str], patient_col: str = "patient_id", time_col: str = "period", treatment_col: str = "treatment", outcome_col: str = "interval_event", ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `panel` | `panel: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `baseline_covariates` | `baseline_covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `time_varying_types` | `time_varying_types: Mapping[str, str]` | Yes | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str = 'treatment'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str = 'interval_event'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `panel`, `baseline_covariates`, `time_varying_types`.
- Referenced columns must exist in the input table: `patient_col`, `time_col`, `treatment_col`, `outcome_col`.

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

from thomaslab.gformula import validate_gformula_panel

result = validate_gformula_panel(
    panel=sample_df,
    baseline_covariates=["feature_a", "feature_b"],
    time_varying_types={}
)

print(result)
~~~

### Related functions

- `fit_parametric_gformula`
- `simulate_gformula_regime`
- `summarize_regime_risk`
- `compare_regime_risks`
- `simulate_regime_set`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/gformula.py#L109`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/gformula.py#L109)
- Repository search: [validate_gformula_panel](https://github.com/appsplorer/thomaslab-core/search?q=validate_gformula_panel&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Audit the temporal panel expected by the parametric g-formula engine.

### API inspection

~~~python
import inspect
from thomaslab.gformula import validate_gformula_panel

print(inspect.signature(validate_gformula_panel))
print(validate_gformula_panel.__doc__)
~~~

### Source

[`src/thomaslab/gformula.py#L109`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/gformula.py#L109)

---

<!-- callable:thomaslab.gformula.fit_parametric_gformula -->
## fit_parametric_gformula

### Purpose

Fit pooled outcome and next-state models for sequential g-computation.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fit_parametric_gformula( panel: pd.DataFrame, *, baseline_covariates: Sequence[str], time_varying_types: Mapping[str, str], patient_col: str = "patient_id", time_col: str = "period", treatment_col: str = "treatment", outcome_col: str = "interval_event", random_state: int = 42, ) -> GFormulaModelBundle
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `panel` | `panel: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `baseline_covariates` | `baseline_covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `time_varying_types` | `time_varying_types: Mapping[str, str]` | Yes | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str = 'treatment'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str = 'interval_event'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `panel`, `baseline_covariates`, `time_varying_types`.
- Referenced columns must exist in the input table: `patient_col`, `time_col`, `treatment_col`, `outcome_col`.

### Returns

`GFormulaModelBundle`

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

from thomaslab.gformula import fit_parametric_gformula

result = fit_parametric_gformula(
    panel=sample_df,
    baseline_covariates=["feature_a", "feature_b"],
    time_varying_types={}
)

print(result)
~~~

### Related functions

- `validate_gformula_panel`
- `simulate_gformula_regime`
- `summarize_regime_risk`
- `compare_regime_risks`
- `simulate_regime_set`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/gformula.py#L337`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/gformula.py#L337)
- Repository search: [fit_parametric_gformula](https://github.com/appsplorer/thomaslab-core/search?q=fit_parametric_gformula&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Fit pooled outcome and next-state models for sequential g-computation.

### API inspection

~~~python
import inspect
from thomaslab.gformula import fit_parametric_gformula

print(inspect.signature(fit_parametric_gformula))
print(fit_parametric_gformula.__doc__)
~~~

### Source

[`src/thomaslab/gformula.py#L337`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/gformula.py#L337)

---

<!-- callable:thomaslab.gformula.simulate_gformula_regime -->
## simulate_gformula_regime

### Purpose

Monte Carlo simulate trajectories under one static or dynamic regime.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def simulate_gformula_regime( bundle: GFormulaModelBundle, *, strategy: StrategyRule, strategy_name: str = "strategy", baseline_population: pd.DataFrame | None = None, n_simulations: int | None = None, horizon: int | None = None, continuous_bounds: Mapping[str, tuple[float, float]] | None = None, random_state: int = 42, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `bundle` | `bundle: GFormulaModelBundle` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strategy` | `strategy: StrategyRule` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strategy_name` | `strategy_name: str = 'strategy'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `baseline_population` | `baseline_population: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `n_simulations` | `n_simulations: int \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `horizon` | `horizon: int \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `continuous_bounds` | `continuous_bounds: Mapping[str, tuple[float, float]] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `bundle`, `strategy`.

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
sample_value = "replace_with_validated_value"

from thomaslab.gformula import simulate_gformula_regime

result = simulate_gformula_regime(
    bundle=sample_value,
    strategy="value"
)

print(result)
~~~

### Related functions

- `validate_gformula_panel`
- `fit_parametric_gformula`
- `summarize_regime_risk`
- `compare_regime_risks`
- `simulate_regime_set`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/gformula.py#L479`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/gformula.py#L479)
- Repository search: [simulate_gformula_regime](https://github.com/appsplorer/thomaslab-core/search?q=simulate_gformula_regime&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Monte Carlo simulate trajectories under one static or dynamic regime.

### API inspection

~~~python
import inspect
from thomaslab.gformula import simulate_gformula_regime

print(inspect.signature(simulate_gformula_regime))
print(simulate_gformula_regime.__doc__)
~~~

### Source

[`src/thomaslab/gformula.py#L479`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/gformula.py#L479)

---

<!-- callable:thomaslab.gformula.summarize_regime_risk -->
## summarize_regime_risk

### Purpose

Calculate Monte Carlo cumulative risk over time for one simulated regime.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_regime_risk( trajectories: pd.DataFrame, *, sim_id_col: str = "_sim_id", time_col: str = "period", event_col: str = "simulated_event", strategy_col: str = "strategy", horizon: int | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `trajectories` | `trajectories: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `sim_id_col` | `sim_id_col: str = '_sim_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str = 'simulated_event'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `strategy_col` | `strategy_col: str = 'strategy'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `horizon` | `horizon: int \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `trajectories`.
- Referenced columns must exist in the input table: `sim_id_col`, `time_col`, `event_col`, `strategy_col`.

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

from thomaslab.gformula import summarize_regime_risk

result = summarize_regime_risk(
    trajectories=sample_df
)

print(result)
~~~

### Related functions

- `validate_gformula_panel`
- `fit_parametric_gformula`
- `simulate_gformula_regime`
- `compare_regime_risks`
- `simulate_regime_set`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/gformula.py#L581`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/gformula.py#L581)
- Repository search: [summarize_regime_risk](https://github.com/appsplorer/thomaslab-core/search?q=summarize_regime_risk&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate Monte Carlo cumulative risk over time for one simulated regime.

### API inspection

~~~python
import inspect
from thomaslab.gformula import summarize_regime_risk

print(inspect.signature(summarize_regime_risk))
print(summarize_regime_risk.__doc__)
~~~

### Source

[`src/thomaslab/gformula.py#L581`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/gformula.py#L581)

---

<!-- callable:thomaslab.gformula.compare_regime_risks -->
## compare_regime_risks

### Purpose

Compare final Monte Carlo risks across regimes on risk difference/ratio scales.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def compare_regime_risks( regime_trajectories: Mapping[str, pd.DataFrame], *, reference: str, horizon: int | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `regime_trajectories` | `regime_trajectories: Mapping[str, pd.DataFrame]` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `reference` | `reference: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `horizon` | `horizon: int \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `regime_trajectories`, `reference`.

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

from thomaslab.gformula import compare_regime_risks

result = compare_regime_risks(
    regime_trajectories=sample_df,
    reference="value"
)

print(result)
~~~

### Related functions

- `validate_gformula_panel`
- `fit_parametric_gformula`
- `simulate_gformula_regime`
- `summarize_regime_risk`
- `simulate_regime_set`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/gformula.py#L625`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/gformula.py#L625)
- Repository search: [compare_regime_risks](https://github.com/appsplorer/thomaslab-core/search?q=compare_regime_risks&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compare final Monte Carlo risks across regimes on risk difference/ratio scales.

### API inspection

~~~python
import inspect
from thomaslab.gformula import compare_regime_risks

print(inspect.signature(compare_regime_risks))
print(compare_regime_risks.__doc__)
~~~

### Source

[`src/thomaslab/gformula.py#L625`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/gformula.py#L625)

---

<!-- callable:thomaslab.gformula.simulate_regime_set -->
## simulate_regime_set

### Purpose

Simulate multiple prespecified regimes using the same reproducible seed.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def simulate_regime_set( bundle: GFormulaModelBundle, *, strategies: Mapping[str, StrategyRule], reference: str, n_simulations: int | None = None, horizon: int | None = None, continuous_bounds: Mapping[str, tuple[float, float]] | None = None, random_state: int = 42, ) -> tuple[dict[str, pd.DataFrame], pd.DataFrame]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `bundle` | `bundle: GFormulaModelBundle` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strategies` | `strategies: Mapping[str, StrategyRule]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `reference` | `reference: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `n_simulations` | `n_simulations: int \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `horizon` | `horizon: int \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `continuous_bounds` | `continuous_bounds: Mapping[str, tuple[float, float]] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `bundle`, `strategies`, `reference`.

### Returns

`tuple[dict[str, pd.DataFrame], pd.DataFrame]`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
sample_value = "replace_with_validated_value"

from thomaslab.gformula import simulate_regime_set

result = simulate_regime_set(
    bundle=sample_value,
    strategies={},
    reference="value"
)

print(result)
~~~

### Related functions

- `validate_gformula_panel`
- `fit_parametric_gformula`
- `simulate_gformula_regime`
- `summarize_regime_risk`
- `compare_regime_risks`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/gformula.py#L668`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/gformula.py#L668)
- Repository search: [simulate_regime_set](https://github.com/appsplorer/thomaslab-core/search?q=simulate_regime_set&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Simulate multiple prespecified regimes using the same reproducible seed.

### API inspection

~~~python
import inspect
from thomaslab.gformula import simulate_regime_set

print(inspect.signature(simulate_regime_set))
print(simulate_regime_set.__doc__)
~~~

### Source

[`src/thomaslab/gformula.py#L668`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/gformula.py#L668)

---

<!-- callable:thomaslab.gformula.bootstrap_gformula_contrasts -->
## bootstrap_gformula_contrasts

### Purpose

Patient-bootstrap uncertainty for g-formula regime risks and contrasts.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def bootstrap_gformula_contrasts( panel: pd.DataFrame, *, baseline_covariates: Sequence[str], time_varying_types: Mapping[str, str], strategies: Mapping[str, StrategyRule], reference: str, patient_col: str = "patient_id", time_col: str = "period", treatment_col: str = "treatment", outcome_col: str = "interval_event", n_bootstrap: int = 200, n_simulations: int | None = None, horizon: int | None = None, continuous_bounds: Mapping[str, tuple[float, float]] | None = None, ci: float = 0.95, random_state: int = 42, ) -> dict[str, pd.DataFrame]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `panel` | `panel: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `baseline_covariates` | `baseline_covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `time_varying_types` | `time_varying_types: Mapping[str, str]` | Yes | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `strategies` | `strategies: Mapping[str, StrategyRule]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `reference` | `reference: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str = 'treatment'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str = 'interval_event'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `n_bootstrap` | `n_bootstrap: int = 200` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `n_simulations` | `n_simulations: int \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `horizon` | `horizon: int \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `continuous_bounds` | `continuous_bounds: Mapping[str, tuple[float, float]] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `panel`, `baseline_covariates`, `time_varying_types`, `strategies`, `reference`.
- Referenced columns must exist in the input table: `patient_col`, `time_col`, `treatment_col`, `outcome_col`.

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

from thomaslab.gformula import bootstrap_gformula_contrasts

result = bootstrap_gformula_contrasts(
    panel=sample_df,
    baseline_covariates=["feature_a", "feature_b"],
    time_varying_types={},
    strategies={},
    reference="value"
)

print(result)
~~~

### Related functions

- `validate_gformula_panel`
- `fit_parametric_gformula`
- `simulate_gformula_regime`
- `summarize_regime_risk`
- `compare_regime_risks`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/gformula.py#L718`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/gformula.py#L718)
- Repository search: [bootstrap_gformula_contrasts](https://github.com/appsplorer/thomaslab-core/search?q=bootstrap_gformula_contrasts&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Patient-bootstrap uncertainty for g-formula regime risks and contrasts.

### API inspection

~~~python
import inspect
from thomaslab.gformula import bootstrap_gformula_contrasts

print(inspect.signature(bootstrap_gformula_contrasts))
print(bootstrap_gformula_contrasts.__doc__)
~~~

### Source

[`src/thomaslab/gformula.py#L718`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/gformula.py#L718)

---

<!-- callable:thomaslab.gformula.compare_gformula_with_msm -->
## compare_gformula_with_msm

### Purpose

Create a method-sensitivity table without equating different effect scales.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def compare_gformula_with_msm( gformula_comparison: pd.DataFrame, msm_estimates: pd.DataFrame, *, gformula_effect_measure: str = "risk_ratio", msm_effect_measure: str = "odds_ratio", msm_treatment_term: str = "treatment", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `gformula_comparison` | `gformula_comparison: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `msm_estimates` | `msm_estimates: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `gformula_effect_measure` | `gformula_effect_measure: str = 'risk_ratio'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `msm_effect_measure` | `msm_effect_measure: str = 'odds_ratio'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `msm_treatment_term` | `msm_treatment_term: str = 'treatment'` | No | Treatment/exposure definition supplied by the study specification; do not infer clinical meaning from labels alone. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `gformula_comparison`, `msm_estimates`.

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

from thomaslab.gformula import compare_gformula_with_msm

result = compare_gformula_with_msm(
    gformula_comparison=sample_df,
    msm_estimates=sample_df
)

print(result)
~~~

### Related functions

- `validate_gformula_panel`
- `fit_parametric_gformula`
- `simulate_gformula_regime`
- `summarize_regime_risk`
- `compare_regime_risks`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/gformula.py#L799`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/gformula.py#L799)
- Repository search: [compare_gformula_with_msm](https://github.com/appsplorer/thomaslab-core/search?q=compare_gformula_with_msm&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create a method-sensitivity table without equating different effect scales.

### API inspection

~~~python
import inspect
from thomaslab.gformula import compare_gformula_with_msm

print(inspect.signature(compare_gformula_with_msm))
print(compare_gformula_with_msm.__doc__)
~~~

### Source

[`src/thomaslab/gformula.py#L799`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/gformula.py#L799)

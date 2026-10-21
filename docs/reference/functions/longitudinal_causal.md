# thomaslab.longitudinal_causal

Longitudinal causal-inference and marginal structural model utilities.

Supports person-period construction, longitudinal treatment/censoring weights,
positivity diagnostics, marginal structural models, and
cloning-censoring-weighting scaffolding for observational target-trial research.

These helpers do not establish exchangeability, positivity, consistency, correct
model specification, or causal identification. Study teams remain responsible for
protocol design, covariate timing, estimand definition, and sensitivity analyses.

## Research-use boundary

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

## Self-service orientation

- Related guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 12

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.longitudinal_causal.build_person_period_dataset -->
## build_person_period_dataset

### Purpose

Split patient follow-up into discrete inclusive person-period rows.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_person_period_dataset( cohort: pd.DataFrame, *, patient_col: str = "patient_id", time_zero_col: str = "time_zero", followup_end_col: str = "followup_end", outcome_date_col: str | None = None, censor_date_col: str | None = None, period_days: int = 30, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `cohort` | `cohort: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_zero_col` | `time_zero_col: str = 'time_zero'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `followup_end_col` | `followup_end_col: str = 'followup_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_date_col` | `outcome_date_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `censor_date_col` | `censor_date_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `period_days` | `period_days: int = 30` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `cohort`.
- Referenced columns must exist in the input table: `patient_col`, `time_zero_col`, `followup_end_col`, `outcome_date_col`, `censor_date_col`.

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

from thomaslab.longitudinal_causal import build_person_period_dataset

result = build_person_period_dataset(
    cohort=sample_df
)

print(result)
~~~

### Related functions

- `validate_person_period_panel`
- `add_lagged_history`
- `estimate_stabilized_treatment_weights`
- `estimate_stabilized_censoring_weights`
- `combine_longitudinal_weights`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/longitudinal_causal.py#L46`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L46)
- Repository search: [build_person_period_dataset](https://github.com/appsplorer/thomaslab-core/search?q=build_person_period_dataset&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Split patient follow-up into discrete inclusive person-period rows.

### API inspection

~~~python
import inspect
from thomaslab.longitudinal_causal import build_person_period_dataset

print(inspect.signature(build_person_period_dataset))
print(build_person_period_dataset.__doc__)
~~~

### Source

[`src/thomaslab/longitudinal_causal.py#L46`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L46)

---

<!-- callable:thomaslab.longitudinal_causal.validate_person_period_panel -->
## validate_person_period_panel

### Purpose

Audit uniqueness, ordering, binary fields, and absorbing follow-up events.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_person_period_panel( panel: pd.DataFrame, *, patient_col: str = "patient_id", time_col: str = "period", treatment_col: str | None = None, event_col: str | None = None, uncensored_col: str | None = None, require_contiguous_time: bool = True, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `panel` | `panel: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `uncensored_col` | `uncensored_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `require_contiguous_time` | `require_contiguous_time: bool = True` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `panel`.
- Referenced columns must exist in the input table: `patient_col`, `time_col`, `treatment_col`, `event_col`, `uncensored_col`.

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

from thomaslab.longitudinal_causal import validate_person_period_panel

result = validate_person_period_panel(
    panel=sample_df
)

print(result)
~~~

### Related functions

- `build_person_period_dataset`
- `add_lagged_history`
- `estimate_stabilized_treatment_weights`
- `estimate_stabilized_censoring_weights`
- `combine_longitudinal_weights`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/longitudinal_causal.py#L131`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L131)
- Repository search: [validate_person_period_panel](https://github.com/appsplorer/thomaslab-core/search?q=validate_person_period_panel&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Audit uniqueness, ordering, binary fields, and absorbing follow-up events.

### API inspection

~~~python
import inspect
from thomaslab.longitudinal_causal import validate_person_period_panel

print(inspect.signature(validate_person_period_panel))
print(validate_person_period_panel.__doc__)
~~~

### Source

[`src/thomaslab/longitudinal_causal.py#L131`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L131)

---

<!-- callable:thomaslab.longitudinal_causal.add_lagged_history -->
## add_lagged_history

### Purpose

Add within-patient lagged treatment/covariate history columns.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def add_lagged_history( panel: pd.DataFrame, *, columns: Sequence[str], lags: Sequence[int] = (1,), patient_col: str = "patient_id", time_col: str = "period", fill_value: float | int | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `panel` | `panel: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `columns` | `columns: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `lags` | `lags: Sequence[int] = (1,)` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `fill_value` | `fill_value: float \| int \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `panel`, `columns`.
- Referenced columns must exist in the input table: `patient_col`, `time_col`.

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

from thomaslab.longitudinal_causal import add_lagged_history

result = add_lagged_history(
    panel=sample_df,
    columns=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `build_person_period_dataset`
- `validate_person_period_panel`
- `estimate_stabilized_treatment_weights`
- `estimate_stabilized_censoring_weights`
- `combine_longitudinal_weights`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/longitudinal_causal.py#L176`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L176)
- Repository search: [add_lagged_history](https://github.com/appsplorer/thomaslab-core/search?q=add_lagged_history&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Add within-patient lagged treatment/covariate history columns.

### API inspection

~~~python
import inspect
from thomaslab.longitudinal_causal import add_lagged_history

print(inspect.signature(add_lagged_history))
print(add_lagged_history.__doc__)
~~~

### Source

[`src/thomaslab/longitudinal_causal.py#L176`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L176)

---

<!-- callable:thomaslab.longitudinal_causal.estimate_stabilized_treatment_weights -->
## estimate_stabilized_treatment_weights

### Purpose

Estimate cumulative stabilized treatment weights with pooled logistic models.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def estimate_stabilized_treatment_weights( panel: pd.DataFrame, *, treatment_col: str, denominator_covariates: Sequence[str], numerator_covariates: Sequence[str] = (), patient_col: str = "patient_id", time_col: str = "period", probability_clip: float = 0.01, random_state: int = 42, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `panel` | `panel: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `denominator_covariates` | `denominator_covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `numerator_covariates` | `numerator_covariates: Sequence[str] = ()` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `probability_clip` | `probability_clip: float = 0.01` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `panel`, `treatment_col`, `denominator_covariates`.
- Referenced columns must exist in the input table: `treatment_col`, `patient_col`, `time_col`.

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

from thomaslab.longitudinal_causal import estimate_stabilized_treatment_weights

result = estimate_stabilized_treatment_weights(
    panel=sample_df,
    treatment_col='treatment',
    denominator_covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `build_person_period_dataset`
- `validate_person_period_panel`
- `add_lagged_history`
- `estimate_stabilized_censoring_weights`
- `combine_longitudinal_weights`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/longitudinal_causal.py#L258`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L258)
- Repository search: [estimate_stabilized_treatment_weights](https://github.com/appsplorer/thomaslab-core/search?q=estimate_stabilized_treatment_weights&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate cumulative stabilized treatment weights with pooled logistic models.

### API inspection

~~~python
import inspect
from thomaslab.longitudinal_causal import estimate_stabilized_treatment_weights

print(inspect.signature(estimate_stabilized_treatment_weights))
print(estimate_stabilized_treatment_weights.__doc__)
~~~

### Source

[`src/thomaslab/longitudinal_causal.py#L258`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L258)

---

<!-- callable:thomaslab.longitudinal_causal.estimate_stabilized_censoring_weights -->
## estimate_stabilized_censoring_weights

### Purpose

Estimate cumulative stabilized inverse-probability-of-censoring weights.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def estimate_stabilized_censoring_weights( panel: pd.DataFrame, *, uncensored_col: str, denominator_covariates: Sequence[str], numerator_covariates: Sequence[str] = (), patient_col: str = "patient_id", time_col: str = "period", probability_clip: float = 0.01, random_state: int = 42, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `panel` | `panel: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `uncensored_col` | `uncensored_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `denominator_covariates` | `denominator_covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `numerator_covariates` | `numerator_covariates: Sequence[str] = ()` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `probability_clip` | `probability_clip: float = 0.01` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `panel`, `uncensored_col`, `denominator_covariates`.
- Referenced columns must exist in the input table: `uncensored_col`, `patient_col`, `time_col`.

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

from thomaslab.longitudinal_causal import estimate_stabilized_censoring_weights

result = estimate_stabilized_censoring_weights(
    panel=sample_df,
    uncensored_col='uncensored',
    denominator_covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `build_person_period_dataset`
- `validate_person_period_panel`
- `add_lagged_history`
- `estimate_stabilized_treatment_weights`
- `combine_longitudinal_weights`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/longitudinal_causal.py#L305`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L305)
- Repository search: [estimate_stabilized_censoring_weights](https://github.com/appsplorer/thomaslab-core/search?q=estimate_stabilized_censoring_weights&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate cumulative stabilized inverse-probability-of-censoring weights.

### API inspection

~~~python
import inspect
from thomaslab.longitudinal_causal import estimate_stabilized_censoring_weights

print(inspect.signature(estimate_stabilized_censoring_weights))
print(estimate_stabilized_censoring_weights.__doc__)
~~~

### Source

[`src/thomaslab/longitudinal_causal.py#L305`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L305)

---

<!-- callable:thomaslab.longitudinal_causal.combine_longitudinal_weights -->
## combine_longitudinal_weights

### Purpose

Multiply longitudinal weights and optionally truncate empirical tails.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def combine_longitudinal_weights( panel: pd.DataFrame, *, treatment_weight_col: str = "stabilized_treatment_weight", censoring_weight_col: str | None = "stabilized_censoring_weight", output_col: str = "longitudinal_weight", truncate_quantiles: tuple[float, float] | None = (0.01, 0.99), ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `panel` | `panel: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_weight_col` | `treatment_weight_col: str = 'stabilized_treatment_weight'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `censoring_weight_col` | `censoring_weight_col: str \| None = 'stabilized_censoring_weight'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `output_col` | `output_col: str = 'longitudinal_weight'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `truncate_quantiles` | `truncate_quantiles: tuple[float, float] \| None = (0.01, 0.99)` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `panel`.
- Referenced columns must exist in the input table: `treatment_weight_col`, `censoring_weight_col`, `output_col`.

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

from thomaslab.longitudinal_causal import combine_longitudinal_weights

result = combine_longitudinal_weights(
    panel=sample_df
)

print(result)
~~~

### Related functions

- `build_person_period_dataset`
- `validate_person_period_panel`
- `add_lagged_history`
- `estimate_stabilized_treatment_weights`
- `estimate_stabilized_censoring_weights`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/longitudinal_causal.py#L347`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L347)
- Repository search: [combine_longitudinal_weights](https://github.com/appsplorer/thomaslab-core/search?q=combine_longitudinal_weights&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Multiply longitudinal weights and optionally truncate empirical tails.

### API inspection

~~~python
import inspect
from thomaslab.longitudinal_causal import combine_longitudinal_weights

print(inspect.signature(combine_longitudinal_weights))
print(combine_longitudinal_weights.__doc__)
~~~

### Source

[`src/thomaslab/longitudinal_causal.py#L347`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L347)

---

<!-- callable:thomaslab.longitudinal_causal.longitudinal_positivity_diagnostics -->
## longitudinal_positivity_diagnostics

### Purpose

Summarize empirical support and treatment probabilities over time.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def longitudinal_positivity_diagnostics( panel: pd.DataFrame, *, treatment_col: str, probability_col: str = "treatment_probability_denominator", time_col: str = "period", threshold: float = 0.05, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `panel` | `panel: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `probability_col` | `probability_col: str = 'treatment_probability_denominator'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `threshold` | `threshold: float = 0.05` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `panel`, `treatment_col`.
- Referenced columns must exist in the input table: `treatment_col`, `probability_col`, `time_col`.

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

from thomaslab.longitudinal_causal import longitudinal_positivity_diagnostics

result = longitudinal_positivity_diagnostics(
    panel=sample_df,
    treatment_col='treatment'
)

print(result)
~~~

### Related functions

- `build_person_period_dataset`
- `validate_person_period_panel`
- `add_lagged_history`
- `estimate_stabilized_treatment_weights`
- `estimate_stabilized_censoring_weights`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/longitudinal_causal.py#L383`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L383)
- Repository search: [longitudinal_positivity_diagnostics](https://github.com/appsplorer/thomaslab-core/search?q=longitudinal_positivity_diagnostics&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize empirical support and treatment probabilities over time.

### API inspection

~~~python
import inspect
from thomaslab.longitudinal_causal import longitudinal_positivity_diagnostics

print(inspect.signature(longitudinal_positivity_diagnostics))
print(longitudinal_positivity_diagnostics.__doc__)
~~~

### Source

[`src/thomaslab/longitudinal_causal.py#L383`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L383)

---

<!-- callable:thomaslab.longitudinal_causal.weight_diagnostics -->
## weight_diagnostics

### Purpose

Summarize weight tails and effective sample size.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def weight_diagnostics( panel: pd.DataFrame, *, weight_col: str, time_col: str | None = "period", ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `panel` | `panel: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `weight_col` | `weight_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str \| None = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `panel`, `weight_col`.
- Referenced columns must exist in the input table: `weight_col`, `time_col`.

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

from thomaslab.longitudinal_causal import weight_diagnostics

result = weight_diagnostics(
    panel=sample_df,
    weight_col='weight'
)

print(result)
~~~

### Related functions

- `build_person_period_dataset`
- `validate_person_period_panel`
- `add_lagged_history`
- `estimate_stabilized_treatment_weights`
- `estimate_stabilized_censoring_weights`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/longitudinal_causal.py#L424`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L424)
- Repository search: [weight_diagnostics](https://github.com/appsplorer/thomaslab-core/search?q=weight_diagnostics&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize weight tails and effective sample size.

### API inspection

~~~python
import inspect
from thomaslab.longitudinal_causal import weight_diagnostics

print(inspect.signature(weight_diagnostics))
print(weight_diagnostics.__doc__)
~~~

### Source

[`src/thomaslab/longitudinal_causal.py#L424`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L424)

---

<!-- callable:thomaslab.longitudinal_causal.fit_weighted_pooled_logistic_msm -->
## fit_weighted_pooled_logistic_msm

### Purpose

Fit a weighted pooled-logistic marginal structural model.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fit_weighted_pooled_logistic_msm( panel: pd.DataFrame, *, outcome_col: str, treatment_col: str, weight_col: str, patient_col: str = "patient_id", time_col: str = "period", additional_terms: Sequence[str] = (), ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `panel` | `panel: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `weight_col` | `weight_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `additional_terms` | `additional_terms: Sequence[str] = ()` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `panel`, `outcome_col`, `treatment_col`, `weight_col`.
- Referenced columns must exist in the input table: `outcome_col`, `treatment_col`, `weight_col`, `patient_col`, `time_col`.

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

from thomaslab.longitudinal_causal import fit_weighted_pooled_logistic_msm

result = fit_weighted_pooled_logistic_msm(
    panel=sample_df,
    outcome_col='outcome',
    treatment_col='treatment',
    weight_col='weight'
)

print(result)
~~~

### Related functions

- `build_person_period_dataset`
- `validate_person_period_panel`
- `add_lagged_history`
- `estimate_stabilized_treatment_weights`
- `estimate_stabilized_censoring_weights`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/longitudinal_causal.py#L464`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L464)
- Repository search: [fit_weighted_pooled_logistic_msm](https://github.com/appsplorer/thomaslab-core/search?q=fit_weighted_pooled_logistic_msm&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Fit a weighted pooled-logistic marginal structural model.

### API inspection

~~~python
import inspect
from thomaslab.longitudinal_causal import fit_weighted_pooled_logistic_msm

print(inspect.signature(fit_weighted_pooled_logistic_msm))
print(fit_weighted_pooled_logistic_msm.__doc__)
~~~

### Source

[`src/thomaslab/longitudinal_causal.py#L464`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L464)

---

<!-- callable:thomaslab.longitudinal_causal.build_clone_censor_dataset -->
## build_clone_censor_dataset

### Purpose

Clone patients into strategies and censor each clone at first deviation.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_clone_censor_dataset( panel: pd.DataFrame, *, strategies: Mapping[str, int | Mapping[int, int] | Callable[[pd.Series], int]], treatment_col: str, patient_col: str = "patient_id", time_col: str = "period", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `panel` | `panel: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `strategies` | `strategies: Mapping[str, int \| Mapping[int, int] \| Callable[[pd.Series], int]]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `panel`, `strategies`, `treatment_col`.
- Referenced columns must exist in the input table: `treatment_col`, `patient_col`, `time_col`.

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

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.longitudinal_causal import build_clone_censor_dataset

result = build_clone_censor_dataset(
    panel=sample_df,
    strategies=sample_series,
    treatment_col='treatment'
)

print(result)
~~~

### Related functions

- `build_person_period_dataset`
- `validate_person_period_panel`
- `add_lagged_history`
- `estimate_stabilized_treatment_weights`
- `estimate_stabilized_censoring_weights`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/longitudinal_causal.py#L549`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L549)
- Repository search: [build_clone_censor_dataset](https://github.com/appsplorer/thomaslab-core/search?q=build_clone_censor_dataset&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Clone patients into strategies and censor each clone at first deviation.

### API inspection

~~~python
import inspect
from thomaslab.longitudinal_causal import build_clone_censor_dataset

print(inspect.signature(build_clone_censor_dataset))
print(build_clone_censor_dataset.__doc__)
~~~

### Source

[`src/thomaslab/longitudinal_causal.py#L549`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L549)

---

<!-- callable:thomaslab.longitudinal_causal.audit_clone_censor_dataset -->
## audit_clone_censor_dataset

### Purpose

Audit clone counts and first-deviation artificial censoring.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_clone_censor_dataset( clones: pd.DataFrame, *, patient_col: str = "patient_id", time_col: str = "period", ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `clones` | `clones: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `clones`.
- Referenced columns must exist in the input table: `patient_col`, `time_col`.

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

from thomaslab.longitudinal_causal import audit_clone_censor_dataset

result = audit_clone_censor_dataset(
    clones=sample_df
)

print(result)
~~~

### Related functions

- `build_person_period_dataset`
- `validate_person_period_panel`
- `add_lagged_history`
- `estimate_stabilized_treatment_weights`
- `estimate_stabilized_censoring_weights`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/longitudinal_causal.py#L594`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L594)
- Repository search: [audit_clone_censor_dataset](https://github.com/appsplorer/thomaslab-core/search?q=audit_clone_censor_dataset&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Audit clone counts and first-deviation artificial censoring.

### API inspection

~~~python
import inspect
from thomaslab.longitudinal_causal import audit_clone_censor_dataset

print(inspect.signature(audit_clone_censor_dataset))
print(audit_clone_censor_dataset.__doc__)
~~~

### Source

[`src/thomaslab/longitudinal_causal.py#L594`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L594)

---

<!-- callable:thomaslab.longitudinal_causal.estimate_clone_censoring_weights -->
## estimate_clone_censoring_weights

### Purpose

Estimate stabilized artificial-censoring weights within cloned strategies.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def estimate_clone_censoring_weights( clones: pd.DataFrame, *, denominator_covariates: Sequence[str], numerator_covariates: Sequence[str] = (), clone_col: str = "clone_id", time_col: str = "period", probability_clip: float = 0.01, random_state: int = 42, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `clones` | `clones: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `denominator_covariates` | `denominator_covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `numerator_covariates` | `numerator_covariates: Sequence[str] = ()` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `clone_col` | `clone_col: str = 'clone_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `probability_clip` | `probability_clip: float = 0.01` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `clones`, `denominator_covariates`.
- Referenced columns must exist in the input table: `clone_col`, `time_col`.

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

from thomaslab.longitudinal_causal import estimate_clone_censoring_weights

result = estimate_clone_censoring_weights(
    clones=sample_df,
    denominator_covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `build_person_period_dataset`
- `validate_person_period_panel`
- `add_lagged_history`
- `estimate_stabilized_treatment_weights`
- `estimate_stabilized_censoring_weights`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/longitudinal_causal.py#L643`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L643)
- Repository search: [estimate_clone_censoring_weights](https://github.com/appsplorer/thomaslab-core/search?q=estimate_clone_censoring_weights&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate stabilized artificial-censoring weights within cloned strategies.

### API inspection

~~~python
import inspect
from thomaslab.longitudinal_causal import estimate_clone_censoring_weights

print(inspect.signature(estimate_clone_censoring_weights))
print(estimate_clone_censoring_weights.__doc__)
~~~

### Source

[`src/thomaslab/longitudinal_causal.py#L643`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/longitudinal_causal.py#L643)

# thomaslab.survival

Advanced survival-analysis preparation and competing-risk utilities.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 7

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.survival.validate_survival_outcome -->
## validate_survival_outcome

### Purpose

Validate one-row-per-patient right-censored survival data.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_survival_outcome( df: pd.DataFrame, *, patient_col: str, time_col: str, event_col: str, cause_col: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `cause_col` | `cause_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `patient_col`, `time_col`, `event_col`.
- Referenced columns must exist in the input table: `patient_col`, `time_col`, `event_col`, `cause_col`.

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

from thomaslab.survival import validate_survival_outcome

result = validate_survival_outcome(
    df=sample_df,
    patient_col='patient_id',
    time_col='event_date',
    event_col='event'
)

print(result)
~~~

### Related functions

- `aalen_johansen_cif`
- `fit_cause_specific_cox`
- `build_time_varying_intervals`
- `fit_time_varying_cox`
- `build_landmark_dataset`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/survival.py#L17`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/survival.py#L17)
- Repository search: [validate_survival_outcome](https://github.com/appsplorer/thomaslab-core/search?q=validate_survival_outcome&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate one-row-per-patient right-censored survival data.

``event_col`` must be binary. When ``cause_col`` is supplied, censored rows
must use cause 0 or missing and event rows must use positive integer causes.

### API inspection

~~~python
import inspect
from thomaslab.survival import validate_survival_outcome

print(inspect.signature(validate_survival_outcome))
print(validate_survival_outcome.__doc__)
~~~

### Source

[`src/thomaslab/survival.py#L17`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/survival.py#L17)

---

<!-- callable:thomaslab.survival.aalen_johansen_cif -->
## aalen_johansen_cif

### Purpose

Estimate nonparametric cumulative incidence by the Aalen–Johansen recursion.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def aalen_johansen_cif( df: pd.DataFrame, *, time_col: str, event_col: str, cause_col: str, causes: Sequence[int] | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `cause_col` | `cause_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `causes` | `causes: Sequence[int] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `time_col`, `event_col`, `cause_col`.
- Referenced columns must exist in the input table: `time_col`, `event_col`, `cause_col`.

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

from thomaslab.survival import aalen_johansen_cif

result = aalen_johansen_cif(
    df=sample_df,
    time_col='event_date',
    event_col='event',
    cause_col='cause'
)

print(result)
~~~

### Related functions

- `validate_survival_outcome`
- `fit_cause_specific_cox`
- `build_time_varying_intervals`
- `fit_time_varying_cox`
- `build_landmark_dataset`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/survival.py#L57`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/survival.py#L57)
- Repository search: [aalen_johansen_cif](https://github.com/appsplorer/thomaslab-core/search?q=aalen_johansen_cif&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate nonparametric cumulative incidence by the Aalen–Johansen recursion.

Returns long-form rows ``time, cause, cumulative_incidence, overall_survival,
n_at_risk, n_all_events, n_cause_events``.

Notes
-----
This estimates cumulative incidence in the presence of competing events. It is
not a Fine–Gray regression model and does not adjust for covariates.

### API inspection

~~~python
import inspect
from thomaslab.survival import aalen_johansen_cif

print(inspect.signature(aalen_johansen_cif))
print(aalen_johansen_cif.__doc__)
~~~

### Source

[`src/thomaslab/survival.py#L57`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/survival.py#L57)

---

<!-- callable:thomaslab.survival.fit_cause_specific_cox -->
## fit_cause_specific_cox

### Purpose

Fit a cause-specific Cox model, treating competing causes as censored.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fit_cause_specific_cox( df: pd.DataFrame, *, time_col: str, cause_col: str, cause: int, covariates: Sequence[str], weights_col: str | None = None, robust: bool = False, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `cause_col` | `cause_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `cause` | `cause: int` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `covariates` | `covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `weights_col` | `weights_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `robust` | `robust: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `time_col`, `cause_col`, `cause`, `covariates`.
- Referenced columns must exist in the input table: `time_col`, `cause_col`, `weights_col`.

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

from thomaslab.survival import fit_cause_specific_cox

result = fit_cause_specific_cox(
    df=sample_df,
    time_col='event_date',
    cause_col='cause',
    cause=2,
    covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `validate_survival_outcome`
- `aalen_johansen_cif`
- `build_time_varying_intervals`
- `fit_time_varying_cox`
- `build_landmark_dataset`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/survival.py#L127`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/survival.py#L127)
- Repository search: [fit_cause_specific_cox](https://github.com/appsplorer/thomaslab-core/search?q=fit_cause_specific_cox&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Fit a cause-specific Cox model, treating competing causes as censored.

The returned hazard ratios are *cause-specific hazard ratios*. They are not
subdistribution hazard ratios and should not be interpreted as direct effects
on the cumulative-incidence function.

### API inspection

~~~python
import inspect
from thomaslab.survival import fit_cause_specific_cox

print(inspect.signature(fit_cause_specific_cox))
print(fit_cause_specific_cox.__doc__)
~~~

### Source

[`src/thomaslab/survival.py#L127`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/survival.py#L127)

---

<!-- callable:thomaslab.survival.build_time_varying_intervals -->
## build_time_varying_intervals

### Purpose

Construct start/stop long format from covariate-change records.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_time_varying_intervals( cohort: pd.DataFrame, changes: pd.DataFrame, *, patient_col: str, followup_end_col: str, event_col: str, change_time_col: str, covariates: Sequence[str], initial_values: dict[str, object] | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `cohort` | `cohort: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `changes` | `changes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `followup_end_col` | `followup_end_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `change_time_col` | `change_time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `initial_values` | `initial_values: dict[str, object] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `cohort`, `changes`, `patient_col`, `followup_end_col`, `event_col`, `change_time_col`, `covariates`.
- Referenced columns must exist in the input table: `patient_col`, `followup_end_col`, `event_col`, `change_time_col`.

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

from thomaslab.survival import build_time_varying_intervals

result = build_time_varying_intervals(
    cohort=sample_df,
    changes=sample_df,
    patient_col='patient_id',
    followup_end_col='followup_end',
    event_col='event',
    change_time_col='change_time',
    covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `validate_survival_outcome`
- `aalen_johansen_cif`
- `fit_cause_specific_cox`
- `fit_time_varying_cox`
- `build_landmark_dataset`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/survival.py#L188`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/survival.py#L188)
- Repository search: [build_time_varying_intervals](https://github.com/appsplorer/thomaslab-core/search?q=build_time_varying_intervals&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Construct start/stop long format from covariate-change records.

Change times are measured from time zero. Values become active *after* their
change time, so each interval is ``[start, stop)`` except the event indicator
is attached to the final interval ending at the observed event/censoring time.

### API inspection

~~~python
import inspect
from thomaslab.survival import build_time_varying_intervals

print(inspect.signature(build_time_varying_intervals))
print(build_time_varying_intervals.__doc__)
~~~

### Source

[`src/thomaslab/survival.py#L188`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/survival.py#L188)

---

<!-- callable:thomaslab.survival.fit_time_varying_cox -->
## fit_time_varying_cox

### Purpose

Fit a Cox time-varying model to explicit start/stop intervals.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fit_time_varying_cox( long_df: pd.DataFrame, *, patient_col: str, start_col: str = "start", stop_col: str = "stop", event_col: str = "event", covariates: Sequence[str], weights_col: str | None = None, robust: bool = False, penalizer: float = 0.0, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `long_df` | `long_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `stop_col` | `stop_col: str = 'stop'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str = 'event'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `weights_col` | `weights_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `robust` | `robust: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `penalizer` | `penalizer: float = 0.0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `long_df`, `patient_col`, `covariates`.
- Referenced columns must exist in the input table: `patient_col`, `start_col`, `stop_col`, `event_col`, `weights_col`.

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

from thomaslab.survival import fit_time_varying_cox

result = fit_time_varying_cox(
    long_df=sample_df,
    patient_col='patient_id',
    covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `validate_survival_outcome`
- `aalen_johansen_cif`
- `fit_cause_specific_cox`
- `build_time_varying_intervals`
- `build_landmark_dataset`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/survival.py#L261`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/survival.py#L261)
- Repository search: [fit_time_varying_cox](https://github.com/appsplorer/thomaslab-core/search?q=fit_time_varying_cox&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Fit a Cox time-varying model to explicit start/stop intervals.

### API inspection

~~~python
import inspect
from thomaslab.survival import fit_time_varying_cox

print(inspect.signature(fit_time_varying_cox))
print(fit_time_varying_cox.__doc__)
~~~

### Source

[`src/thomaslab/survival.py#L261`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/survival.py#L261)

---

<!-- callable:thomaslab.survival.build_landmark_dataset -->
## build_landmark_dataset

### Purpose

Construct a survivor-at-landmark analysis dataset.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_landmark_dataset( df: pd.DataFrame, *, time_col: str, event_col: str, landmark_time: float, exposure_time_col: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `landmark_time` | `landmark_time: float` | Yes | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `exposure_time_col` | `exposure_time_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `time_col`, `event_col`, `landmark_time`.
- Referenced columns must exist in the input table: `time_col`, `event_col`, `exposure_time_col`.

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

from thomaslab.survival import build_landmark_dataset

result = build_landmark_dataset(
    df=sample_df,
    time_col='event_date',
    event_col='event',
    landmark_time=0.5
)

print(result)
~~~

### Related functions

- `validate_survival_outcome`
- `aalen_johansen_cif`
- `fit_cause_specific_cox`
- `build_time_varying_intervals`
- `fit_time_varying_cox`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/survival.py#L319`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/survival.py#L319)
- Repository search: [build_landmark_dataset](https://github.com/appsplorer/thomaslab-core/search?q=build_landmark_dataset&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Construct a survivor-at-landmark analysis dataset.

Patients with an event or censoring at/before the landmark are excluded.
Follow-up is reset to zero at the landmark. If ``exposure_time_col`` is supplied,
``exposed_at_landmark`` is defined only from exposures occurring on/before the
landmark.

### API inspection

~~~python
import inspect
from thomaslab.survival import build_landmark_dataset

print(inspect.signature(build_landmark_dataset))
print(build_landmark_dataset.__doc__)
~~~

### Source

[`src/thomaslab/survival.py#L319`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/survival.py#L319)

---

<!-- callable:thomaslab.survival.audit_immortal_time_assignment -->
## audit_immortal_time_assignment

### Purpose

Flag baseline exposure assignments that depend on future exposure.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_immortal_time_assignment( df: pd.DataFrame, *, assigned_exposure_col: str, first_exposure_time_col: str, ) -> dict[str, object]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `assigned_exposure_col` | `assigned_exposure_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `first_exposure_time_col` | `first_exposure_time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `assigned_exposure_col`, `first_exposure_time_col`.
- Referenced columns must exist in the input table: `assigned_exposure_col`, `first_exposure_time_col`.

### Returns

`dict[str, object]`

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

from thomaslab.survival import audit_immortal_time_assignment

result = audit_immortal_time_assignment(
    df=sample_df,
    assigned_exposure_col='assigned_exposure',
    first_exposure_time_col='first_exposure_time'
)

print(result)
~~~

### Related functions

- `validate_survival_outcome`
- `aalen_johansen_cif`
- `fit_cause_specific_cox`
- `build_time_varying_intervals`
- `fit_time_varying_cox`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/survival.py#L351`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/survival.py#L351)
- Repository search: [audit_immortal_time_assignment](https://github.com/appsplorer/thomaslab-core/search?q=audit_immortal_time_assignment&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Flag baseline exposure assignments that depend on future exposure.

A row is flagged when assigned baseline exposure is truthy but the first
exposure occurs strictly after time zero.

### API inspection

~~~python
import inspect
from thomaslab.survival import audit_immortal_time_assignment

print(inspect.signature(audit_immortal_time_assignment))
print(audit_immortal_time_assignment.__doc__)
~~~

### Source

[`src/thomaslab/survival.py#L351`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/survival.py#L351)

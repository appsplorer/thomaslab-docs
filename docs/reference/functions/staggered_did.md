# thomaslab.staggered_did

Staggered-adoption difference-in-differences research utilities.

This module supports panel studies where treatment is adopted at different times.
It deliberately keeps cohort-time effects visible instead of silently reducing a
heterogeneous staggered design to one conventional two-way fixed-effects coefficient.

The implemented estimator is an auditable group-time difference-in-changes contrast.
For adoption cohort g and target period t, outcomes are differenced from the last
pre-adoption reference period g-1 and compared with never-treated or not-yet-treated
controls. Unit-cluster bootstrap uncertainty is available for event-study summaries.

These utilities do not establish causal identification. Interpretation still requires
a defensible parallel-trends counterfactual for the chosen controls, no anticipation
over the reference window, consistency, correct treatment timing, and adequate support.

## Research-use boundary

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

## Self-service orientation

- Related guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 8

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.staggered_did.validate_staggered_panel -->
## validate_staggered_panel

### Purpose

Validate panel structure and summarize treatment-adoption timing.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_staggered_panel( df: pd.DataFrame, *, unit_col: str, time_col: str, outcome_col: str, treatment_col: str, require_absorbing: bool = True, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `unit_col` | `unit_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `require_absorbing` | `require_absorbing: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `unit_col`, `time_col`, `outcome_col`, `treatment_col`.
- Referenced columns must exist in the input table: `unit_col`, `time_col`, `outcome_col`, `treatment_col`.

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

from thomaslab.staggered_did import validate_staggered_panel

result = validate_staggered_panel(
    df=sample_df,
    unit_col='unit',
    time_col='event_date',
    outcome_col='outcome',
    treatment_col='treatment'
)

print(result)
~~~

### Related functions

- `treatment_timing_diagnostics`
- `estimate_group_time_effects`
- `aggregate_event_study`
- `aggregate_cohort_effects`
- `preperiod_placebo_diagnostic`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/staggered_did.py#L118`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/staggered_did.py#L118)
- Repository search: [validate_staggered_panel](https://github.com/appsplorer/thomaslab-core/search?q=validate_staggered_panel&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate panel structure and summarize treatment-adoption timing.

### API inspection

~~~python
import inspect
from thomaslab.staggered_did import validate_staggered_panel

print(inspect.signature(validate_staggered_panel))
print(validate_staggered_panel.__doc__)
~~~

### Source

[`src/thomaslab/staggered_did.py#L118`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/staggered_did.py#L118)

---

<!-- callable:thomaslab.staggered_did.treatment_timing_diagnostics -->
## treatment_timing_diagnostics

### Purpose

Report cohort sizes and control support for each cohort/target period.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def treatment_timing_diagnostics( df: pd.DataFrame, *, unit_col: str, time_col: str, outcome_col: str, treatment_col: str, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `unit_col` | `unit_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `unit_col`, `time_col`, `outcome_col`, `treatment_col`.
- Referenced columns must exist in the input table: `unit_col`, `time_col`, `outcome_col`, `treatment_col`.

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

from thomaslab.staggered_did import treatment_timing_diagnostics

result = treatment_timing_diagnostics(
    df=sample_df,
    unit_col='unit',
    time_col='event_date',
    outcome_col='outcome',
    treatment_col='treatment'
)

print(result)
~~~

### Related functions

- `validate_staggered_panel`
- `estimate_group_time_effects`
- `aggregate_event_study`
- `aggregate_cohort_effects`
- `preperiod_placebo_diagnostic`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/staggered_did.py#L161`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/staggered_did.py#L161)
- Repository search: [treatment_timing_diagnostics](https://github.com/appsplorer/thomaslab-core/search?q=treatment_timing_diagnostics&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Report cohort sizes and control support for each cohort/target period.

### API inspection

~~~python
import inspect
from thomaslab.staggered_did import treatment_timing_diagnostics

print(inspect.signature(treatment_timing_diagnostics))
print(treatment_timing_diagnostics.__doc__)
~~~

### Source

[`src/thomaslab/staggered_did.py#L161`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/staggered_did.py#L161)

---

<!-- callable:thomaslab.staggered_did.estimate_group_time_effects -->
## estimate_group_time_effects

### Purpose

Estimate visible adoption-cohort by target-period DiD contrasts.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def estimate_group_time_effects( df: pd.DataFrame, *, unit_col: str, time_col: str, outcome_col: str, treatment_col: str, control_group: str = "not_yet_treated", min_group_units: int = 2, min_control_units: int = 2, min_event_time: int | None = None, max_event_time: int | None = None, include_reference: bool = True, ci: float = 0.95, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `unit_col` | `unit_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `control_group` | `control_group: str = 'not_yet_treated'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `min_group_units` | `min_group_units: int = 2` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `min_control_units` | `min_control_units: int = 2` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `min_event_time` | `min_event_time: int \| None = None` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `max_event_time` | `max_event_time: int \| None = None` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `include_reference` | `include_reference: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `unit_col`, `time_col`, `outcome_col`, `treatment_col`.
- Referenced columns must exist in the input table: `unit_col`, `time_col`, `outcome_col`, `treatment_col`.

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

from thomaslab.staggered_did import estimate_group_time_effects

result = estimate_group_time_effects(
    df=sample_df,
    unit_col='unit',
    time_col='event_date',
    outcome_col='outcome',
    treatment_col='treatment'
)

print(result)
~~~

### Related functions

- `validate_staggered_panel`
- `treatment_timing_diagnostics`
- `aggregate_event_study`
- `aggregate_cohort_effects`
- `preperiod_placebo_diagnostic`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/staggered_did.py#L257`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/staggered_did.py#L257)
- Repository search: [estimate_group_time_effects](https://github.com/appsplorer/thomaslab-core/search?q=estimate_group_time_effects&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate visible adoption-cohort by target-period DiD contrasts.

### API inspection

~~~python
import inspect
from thomaslab.staggered_did import estimate_group_time_effects

print(inspect.signature(estimate_group_time_effects))
print(estimate_group_time_effects.__doc__)
~~~

### Source

[`src/thomaslab/staggered_did.py#L257`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/staggered_did.py#L257)

---

<!-- callable:thomaslab.staggered_did.aggregate_event_study -->
## aggregate_event_study

### Purpose

Aggregate cohort-time effects by event time without hiding source cells.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def aggregate_event_study( group_time_effects: pd.DataFrame, *, weighting: str = "cohort_size", ci: float = 0.95, include_reference: bool = True, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `group_time_effects` | `group_time_effects: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `weighting` | `weighting: str = 'cohort_size'` | No | Analysis weight/propensity input. Inspect support, positivity, extremes, and effective sample size where applicable. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `include_reference` | `include_reference: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `group_time_effects`.

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

from thomaslab.staggered_did import aggregate_event_study

result = aggregate_event_study(
    group_time_effects=sample_df
)

print(result)
~~~

### Related functions

- `validate_staggered_panel`
- `treatment_timing_diagnostics`
- `estimate_group_time_effects`
- `aggregate_cohort_effects`
- `preperiod_placebo_diagnostic`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/staggered_did.py#L414`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/staggered_did.py#L414)
- Repository search: [aggregate_event_study](https://github.com/appsplorer/thomaslab-core/search?q=aggregate_event_study&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Aggregate cohort-time effects by event time without hiding source cells.

### API inspection

~~~python
import inspect
from thomaslab.staggered_did import aggregate_event_study

print(inspect.signature(aggregate_event_study))
print(aggregate_event_study.__doc__)
~~~

### Source

[`src/thomaslab/staggered_did.py#L414`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/staggered_did.py#L414)

---

<!-- callable:thomaslab.staggered_did.aggregate_cohort_effects -->
## aggregate_cohort_effects

### Purpose

Summarize each adoption cohort across estimable target periods.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def aggregate_cohort_effects( group_time_effects: pd.DataFrame, *, weighting: str = "treated_units", post_only: bool = True, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `group_time_effects` | `group_time_effects: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `weighting` | `weighting: str = 'treated_units'` | No | Analysis weight/propensity input. Inspect support, positivity, extremes, and effective sample size where applicable. |
| `post_only` | `post_only: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `group_time_effects`.

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

from thomaslab.staggered_did import aggregate_cohort_effects

result = aggregate_cohort_effects(
    group_time_effects=sample_df
)

print(result)
~~~

### Related functions

- `validate_staggered_panel`
- `treatment_timing_diagnostics`
- `estimate_group_time_effects`
- `aggregate_event_study`
- `preperiod_placebo_diagnostic`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/staggered_did.py#L505`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/staggered_did.py#L505)
- Repository search: [aggregate_cohort_effects](https://github.com/appsplorer/thomaslab-core/search?q=aggregate_cohort_effects&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize each adoption cohort across estimable target periods.

### API inspection

~~~python
import inspect
from thomaslab.staggered_did import aggregate_cohort_effects

print(inspect.signature(aggregate_cohort_effects))
print(aggregate_cohort_effects.__doc__)
~~~

### Source

[`src/thomaslab/staggered_did.py#L505`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/staggered_did.py#L505)

---

<!-- callable:thomaslab.staggered_did.preperiod_placebo_diagnostic -->
## preperiod_placebo_diagnostic

### Purpose

Summarize event-time placebo estimates before the reference period.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def preperiod_placebo_diagnostic(event_study: pd.DataFrame) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `event_study` | `event_study: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `event_study`.

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

from thomaslab.staggered_did import preperiod_placebo_diagnostic

result = preperiod_placebo_diagnostic(
    event_study=sample_df
)

print(result)
~~~

### Related functions

- `validate_staggered_panel`
- `treatment_timing_diagnostics`
- `estimate_group_time_effects`
- `aggregate_event_study`
- `aggregate_cohort_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/staggered_did.py#L567`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/staggered_did.py#L567)
- Repository search: [preperiod_placebo_diagnostic](https://github.com/appsplorer/thomaslab-core/search?q=preperiod_placebo_diagnostic&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize event-time placebo estimates before the reference period.

### API inspection

~~~python
import inspect
from thomaslab.staggered_did import preperiod_placebo_diagnostic

print(inspect.signature(preperiod_placebo_diagnostic))
print(preperiod_placebo_diagnostic.__doc__)
~~~

### Source

[`src/thomaslab/staggered_did.py#L567`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/staggered_did.py#L567)

---

<!-- callable:thomaslab.staggered_did.bootstrap_event_study -->
## bootstrap_event_study

### Purpose

Unit-cluster bootstrap for aggregated staggered-adoption event studies.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def bootstrap_event_study( df: pd.DataFrame, *, unit_col: str, time_col: str, outcome_col: str, treatment_col: str, control_group: str = "not_yet_treated", weighting: str = "cohort_size", min_event_time: int | None = None, max_event_time: int | None = None, n_boot: int = 500, ci: float = 0.95, random_state: int | None = None, min_success_fraction: float = 0.5, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `unit_col` | `unit_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `control_group` | `control_group: str = 'not_yet_treated'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `weighting` | `weighting: str = 'cohort_size'` | No | Analysis weight/propensity input. Inspect support, positivity, extremes, and effective sample size where applicable. |
| `min_event_time` | `min_event_time: int \| None = None` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `max_event_time` | `max_event_time: int \| None = None` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `n_boot` | `n_boot: int = 500` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int \| None = None` | No | Reproducibility seed. Record it in the study bundle. |
| `min_success_fraction` | `min_success_fraction: float = 0.5` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `unit_col`, `time_col`, `outcome_col`, `treatment_col`.
- Referenced columns must exist in the input table: `unit_col`, `time_col`, `outcome_col`, `treatment_col`.

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

from thomaslab.staggered_did import bootstrap_event_study

result = bootstrap_event_study(
    df=sample_df,
    unit_col='unit',
    time_col='event_date',
    outcome_col='outcome',
    treatment_col='treatment'
)

print(result)
~~~

### Related functions

- `validate_staggered_panel`
- `treatment_timing_diagnostics`
- `estimate_group_time_effects`
- `aggregate_event_study`
- `aggregate_cohort_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/staggered_did.py#L593`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/staggered_did.py#L593)
- Repository search: [bootstrap_event_study](https://github.com/appsplorer/thomaslab-core/search?q=bootstrap_event_study&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Unit-cluster bootstrap for aggregated staggered-adoption event studies.

### API inspection

~~~python
import inspect
from thomaslab.staggered_did import bootstrap_event_study

print(inspect.signature(bootstrap_event_study))
print(bootstrap_event_study.__doc__)
~~~

### Source

[`src/thomaslab/staggered_did.py#L593`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/staggered_did.py#L593)

---

<!-- callable:thomaslab.staggered_did.timing_shift_sensitivity -->
## timing_shift_sensitivity

### Purpose

Re-estimate event studies after explicit adoption-time shifts.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def timing_shift_sensitivity( df: pd.DataFrame, *, unit_col: str, time_col: str, outcome_col: str, treatment_col: str, shifts: Sequence[int] = (-1, 0, 1), control_group: str = "not_yet_treated", weighting: str = "cohort_size", min_event_time: int | None = None, max_event_time: int | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `unit_col` | `unit_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `shifts` | `shifts: Sequence[int] = (-1, 0, 1)` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `control_group` | `control_group: str = 'not_yet_treated'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `weighting` | `weighting: str = 'cohort_size'` | No | Analysis weight/propensity input. Inspect support, positivity, extremes, and effective sample size where applicable. |
| `min_event_time` | `min_event_time: int \| None = None` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `max_event_time` | `max_event_time: int \| None = None` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `unit_col`, `time_col`, `outcome_col`, `treatment_col`.
- Referenced columns must exist in the input table: `unit_col`, `time_col`, `outcome_col`, `treatment_col`.

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

from thomaslab.staggered_did import timing_shift_sensitivity

result = timing_shift_sensitivity(
    df=sample_df,
    unit_col='unit',
    time_col='event_date',
    outcome_col='outcome',
    treatment_col='treatment'
)

print(result)
~~~

### Related functions

- `validate_staggered_panel`
- `treatment_timing_diagnostics`
- `estimate_group_time_effects`
- `aggregate_event_study`
- `aggregate_cohort_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/staggered_did.py#L698`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/staggered_did.py#L698)
- Repository search: [timing_shift_sensitivity](https://github.com/appsplorer/thomaslab-core/search?q=timing_shift_sensitivity&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Re-estimate event studies after explicit adoption-time shifts.

### API inspection

~~~python
import inspect
from thomaslab.staggered_did import timing_shift_sensitivity

print(inspect.signature(timing_shift_sensitivity))
print(timing_shift_sensitivity.__doc__)
~~~

### Source

[`src/thomaslab/staggered_did.py#L698`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/staggered_did.py#L698)

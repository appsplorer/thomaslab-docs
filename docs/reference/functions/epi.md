# thomaslab.epi

Descriptive epidemiology and transparent effect-measure utilities.

These functions calculate descriptive association measures. They do not establish
causality and do not adjust for confounding unless an upstream design/estimator has
already produced suitable weighted or standardized data.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 9

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.epi.calculate_prevalence -->
## calculate_prevalence

### Purpose

Calculate prevalence with Wilson confidence intervals.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_prevalence( df: pd.DataFrame, outcome_col: str, *, group_col: str | None = None, alpha: float = 0.05, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `group_col` | `group_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `alpha` | `alpha: float = 0.05` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `outcome_col`.
- Referenced columns must exist in the input table: `outcome_col`, `group_col`.

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

from thomaslab.epi import calculate_prevalence

result = calculate_prevalence(
    df=sample_df,
    outcome_col='outcome'
)

print(result)
~~~

### Related functions

- `calculate_cumulative_incidence`
- `calculate_person_time`
- `calculate_incidence_rate`
- `calculate_risk_difference`
- `calculate_risk_ratio`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/epi.py#L47`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/epi.py#L47)
- Repository search: [calculate_prevalence](https://github.com/appsplorer/thomaslab-core/search?q=calculate_prevalence&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate prevalence with Wilson confidence intervals.

Missing outcome values are excluded and reported through ``n_nonmissing``.

### API inspection

~~~python
import inspect
from thomaslab.epi import calculate_prevalence

print(inspect.signature(calculate_prevalence))
print(calculate_prevalence.__doc__)
~~~

### Source

[`src/thomaslab/epi.py#L47`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/epi.py#L47)

---

<!-- callable:thomaslab.epi.calculate_cumulative_incidence -->
## calculate_cumulative_incidence

### Purpose

Calculate crude cumulative incidence over the supplied fixed follow-up window.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_cumulative_incidence( df: pd.DataFrame, event_col: str, *, group_col: str | None = None, alpha: float = 0.05, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `event_col` | `event_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `group_col` | `group_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `alpha` | `alpha: float = 0.05` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `event_col`.
- Referenced columns must exist in the input table: `event_col`, `group_col`.

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

from thomaslab.epi import calculate_cumulative_incidence

result = calculate_cumulative_incidence(
    df=sample_df,
    event_col='event'
)

print(result)
~~~

### Related functions

- `calculate_prevalence`
- `calculate_person_time`
- `calculate_incidence_rate`
- `calculate_risk_difference`
- `calculate_risk_ratio`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/epi.py#L87`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/epi.py#L87)
- Repository search: [calculate_cumulative_incidence](https://github.com/appsplorer/thomaslab-core/search?q=calculate_cumulative_incidence&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate crude cumulative incidence over the supplied fixed follow-up window.

This is only appropriate when the input cohort has a scientifically meaningful,
sufficiently complete risk window. For variable follow-up/censoring use survival
methods rather than interpreting this as Kaplan-Meier risk.

### API inspection

~~~python
import inspect
from thomaslab.epi import calculate_cumulative_incidence

print(inspect.signature(calculate_cumulative_incidence))
print(calculate_cumulative_incidence.__doc__)
~~~

### Source

[`src/thomaslab/epi.py#L87`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/epi.py#L87)

---

<!-- callable:thomaslab.epi.calculate_person_time -->
## calculate_person_time

### Purpose

Sum positive follow-up time after dividing by ``time_scale``.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_person_time( df: pd.DataFrame, time_col: str, *, time_scale: float = 1.0, ) -> float
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_scale` | `time_scale: float = 1.0` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `time_col`.
- Referenced columns must exist in the input table: `time_col`.

### Returns

`float`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

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

from thomaslab.epi import calculate_person_time

result = calculate_person_time(
    df=sample_df,
    time_col='event_date'
)

print(result)
~~~

### Related functions

- `calculate_prevalence`
- `calculate_cumulative_incidence`
- `calculate_incidence_rate`
- `calculate_risk_difference`
- `calculate_risk_ratio`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/epi.py#L104`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/epi.py#L104)
- Repository search: [calculate_person_time](https://github.com/appsplorer/thomaslab-core/search?q=calculate_person_time&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Sum positive follow-up time after dividing by ``time_scale``.

Examples: if ``time_col`` is days, ``time_scale=365.25`` returns person-years.

### API inspection

~~~python
import inspect
from thomaslab.epi import calculate_person_time

print(inspect.signature(calculate_person_time))
print(calculate_person_time.__doc__)
~~~

### Source

[`src/thomaslab/epi.py#L104`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/epi.py#L104)

---

<!-- callable:thomaslab.epi.calculate_incidence_rate -->
## calculate_incidence_rate

### Purpose

Calculate crude incidence rate and exact Poisson confidence interval.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_incidence_rate( df: pd.DataFrame, event_col: str, time_col: str, *, time_scale: float = 1.0, multiplier: float = 100.0, alpha: float = 0.05, group_col: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `event_col` | `event_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_scale` | `time_scale: float = 1.0` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `multiplier` | `multiplier: float = 100.0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `alpha` | `alpha: float = 0.05` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `group_col` | `group_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `event_col`, `time_col`.
- Referenced columns must exist in the input table: `event_col`, `time_col`, `group_col`.

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

from thomaslab.epi import calculate_incidence_rate

result = calculate_incidence_rate(
    df=sample_df,
    event_col='event',
    time_col='event_date'
)

print(result)
~~~

### Related functions

- `calculate_prevalence`
- `calculate_cumulative_incidence`
- `calculate_person_time`
- `calculate_risk_difference`
- `calculate_risk_ratio`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/epi.py#L123`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/epi.py#L123)
- Repository search: [calculate_incidence_rate](https://github.com/appsplorer/thomaslab-core/search?q=calculate_incidence_rate&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate crude incidence rate and exact Poisson confidence interval.

``event_col`` may contain 0/1 event indicators or non-negative event counts.

### API inspection

~~~python
import inspect
from thomaslab.epi import calculate_incidence_rate

print(inspect.signature(calculate_incidence_rate))
print(calculate_incidence_rate.__doc__)
~~~

### Source

[`src/thomaslab/epi.py#L123`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/epi.py#L123)

---

<!-- callable:thomaslab.epi.calculate_risk_difference -->
## calculate_risk_difference

### Purpose

Calculate crude risk difference (treated/exposed minus comparator).

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_risk_difference( df: pd.DataFrame, treatment_col: str, outcome_col: str, *, alpha: float = 0.05, ) -> dict[str, float | str]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `alpha` | `alpha: float = 0.05` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `outcome_col`.
- Referenced columns must exist in the input table: `treatment_col`, `outcome_col`.

### Returns

`dict[str, float | str]`

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

from thomaslab.epi import calculate_risk_difference

result = calculate_risk_difference(
    df=sample_df,
    treatment_col='treatment',
    outcome_col='outcome'
)

print(result)
~~~

### Related functions

- `calculate_prevalence`
- `calculate_cumulative_incidence`
- `calculate_person_time`
- `calculate_incidence_rate`
- `calculate_risk_ratio`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/epi.py#L194`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/epi.py#L194)
- Repository search: [calculate_risk_difference](https://github.com/appsplorer/thomaslab-core/search?q=calculate_risk_difference&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate crude risk difference (treated/exposed minus comparator).

### API inspection

~~~python
import inspect
from thomaslab.epi import calculate_risk_difference

print(inspect.signature(calculate_risk_difference))
print(calculate_risk_difference.__doc__)
~~~

### Source

[`src/thomaslab/epi.py#L194`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/epi.py#L194)

---

<!-- callable:thomaslab.epi.calculate_risk_ratio -->
## calculate_risk_ratio

### Purpose

Calculate crude risk ratio with log-scale confidence interval.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_risk_ratio( df: pd.DataFrame, treatment_col: str, outcome_col: str, *, alpha: float = 0.05, continuity_correction: float = 0.5, ) -> dict[str, float | bool | str]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `alpha` | `alpha: float = 0.05` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `continuity_correction` | `continuity_correction: float = 0.5` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `outcome_col`.
- Referenced columns must exist in the input table: `treatment_col`, `outcome_col`.

### Returns

`dict[str, float | bool | str]`

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

from thomaslab.epi import calculate_risk_ratio

result = calculate_risk_ratio(
    df=sample_df,
    treatment_col='treatment',
    outcome_col='outcome'
)

print(result)
~~~

### Related functions

- `calculate_prevalence`
- `calculate_cumulative_incidence`
- `calculate_person_time`
- `calculate_incidence_rate`
- `calculate_risk_difference`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/epi.py#L219`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/epi.py#L219)
- Repository search: [calculate_risk_ratio](https://github.com/appsplorer/thomaslab-core/search?q=calculate_risk_ratio&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate crude risk ratio with log-scale confidence interval.

A Haldane-Anscombe-style continuity correction is applied only when required by
zero cells and is explicitly reported.

### API inspection

~~~python
import inspect
from thomaslab.epi import calculate_risk_ratio

print(inspect.signature(calculate_risk_ratio))
print(calculate_risk_ratio.__doc__)
~~~

### Source

[`src/thomaslab/epi.py#L219`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/epi.py#L219)

---

<!-- callable:thomaslab.epi.calculate_odds_ratio -->
## calculate_odds_ratio

### Purpose

Calculate crude odds ratio with log-scale confidence interval.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_odds_ratio( df: pd.DataFrame, treatment_col: str, outcome_col: str, *, alpha: float = 0.05, continuity_correction: float = 0.5, ) -> dict[str, float | bool | str]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `alpha` | `alpha: float = 0.05` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `continuity_correction` | `continuity_correction: float = 0.5` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `outcome_col`.
- Referenced columns must exist in the input table: `treatment_col`, `outcome_col`.

### Returns

`dict[str, float | bool | str]`

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

from thomaslab.epi import calculate_odds_ratio

result = calculate_odds_ratio(
    df=sample_df,
    treatment_col='treatment',
    outcome_col='outcome'
)

print(result)
~~~

### Related functions

- `calculate_prevalence`
- `calculate_cumulative_incidence`
- `calculate_person_time`
- `calculate_incidence_rate`
- `calculate_risk_difference`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/epi.py#L256`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/epi.py#L256)
- Repository search: [calculate_odds_ratio](https://github.com/appsplorer/thomaslab-core/search?q=calculate_odds_ratio&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate crude odds ratio with log-scale confidence interval.

### API inspection

~~~python
import inspect
from thomaslab.epi import calculate_odds_ratio

print(inspect.signature(calculate_odds_ratio))
print(calculate_odds_ratio.__doc__)
~~~

### Source

[`src/thomaslab/epi.py#L256`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/epi.py#L256)

---

<!-- callable:thomaslab.epi.calculate_rate_ratio -->
## calculate_rate_ratio

### Purpose

Calculate crude incidence-rate ratio from event counts and person-time.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_rate_ratio( events_treated: int, person_time_treated: float, events_control: int, person_time_control: float, *, alpha: float = 0.05, continuity_correction: float = 0.5, ) -> dict[str, float | bool | str]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events_treated` | `events_treated: int` | Yes | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `person_time_treated` | `person_time_treated: float` | Yes | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `events_control` | `events_control: int` | Yes | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `person_time_control` | `person_time_control: float` | Yes | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `alpha` | `alpha: float = 0.05` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `continuity_correction` | `continuity_correction: float = 0.5` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events_treated`, `person_time_treated`, `events_control`, `person_time_control`.

### Returns

`dict[str, float | bool | str]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.epi import calculate_rate_ratio

result = calculate_rate_ratio(
    events_treated=2,
    person_time_treated=0.5,
    events_control=2,
    person_time_control=0.5
)

print(result)
~~~

### Related functions

- `calculate_prevalence`
- `calculate_cumulative_incidence`
- `calculate_person_time`
- `calculate_incidence_rate`
- `calculate_risk_difference`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/epi.py#L287`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/epi.py#L287)
- Repository search: [calculate_rate_ratio](https://github.com/appsplorer/thomaslab-core/search?q=calculate_rate_ratio&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate crude incidence-rate ratio from event counts and person-time.

### API inspection

~~~python
import inspect
from thomaslab.epi import calculate_rate_ratio

print(inspect.signature(calculate_rate_ratio))
print(calculate_rate_ratio.__doc__)
~~~

### Source

[`src/thomaslab/epi.py#L287`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/epi.py#L287)

---

<!-- callable:thomaslab.epi.calculate_number_needed -->
## calculate_number_needed

### Purpose

Convert an absolute risk difference into a descriptive NNT/NNH-style value.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_number_needed(risk_difference: float) -> dict[str, float | str]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `risk_difference` | `risk_difference: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `risk_difference`.

### Returns

`dict[str, float | str]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.epi import calculate_number_needed

result = calculate_number_needed(
    risk_difference=0.5
)

print(result)
~~~

### Related functions

- `calculate_prevalence`
- `calculate_cumulative_incidence`
- `calculate_person_time`
- `calculate_incidence_rate`
- `calculate_risk_difference`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/epi.py#L321`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/epi.py#L321)
- Repository search: [calculate_number_needed](https://github.com/appsplorer/thomaslab-core/search?q=calculate_number_needed&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Convert an absolute risk difference into a descriptive NNT/NNH-style value.

Positive differences are labelled ``number_needed_to_harm`` and negative
differences ``number_needed_to_treat`` under the explicit assumption that the
outcome is adverse. A zero difference returns infinity.

### API inspection

~~~python
import inspect
from thomaslab.epi import calculate_number_needed

print(inspect.signature(calculate_number_needed))
print(calculate_number_needed.__doc__)
~~~

### Source

[`src/thomaslab/epi.py#L321`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/epi.py#L321)

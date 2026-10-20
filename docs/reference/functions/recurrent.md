# thomaslab.recurrent

Recurrent-event dataset construction and descriptive utilities.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 6

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.recurrent.validate_recurrent_events -->
## validate_recurrent_events

### Purpose

Validate recurrent event rows with unique patient/event-time pairs.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_recurrent_events( events: pd.DataFrame, *, patient_col: str, event_time_col: str, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_time_col` | `event_time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`, `patient_col`, `event_time_col`.
- Referenced columns must exist in the input table: `patient_col`, `event_time_col`.

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

from thomaslab.recurrent import validate_recurrent_events

result = validate_recurrent_events(
    events=sample_df,
    patient_col='patient_id',
    event_time_col='event_time'
)

print(result)
~~~

### Related functions

- `count_recurrent_events`
- `build_andersen_gill_intervals`
- `build_pwp_total_time_strata`
- `recurrent_event_rate`
- `summarize_recurrent_events`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/recurrent.py#L16`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/recurrent.py#L16)
- Repository search: [validate_recurrent_events](https://github.com/appsplorer/thomaslab-core/search?q=validate_recurrent_events&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate recurrent event rows with unique patient/event-time pairs.

### API inspection

~~~python
import inspect
from thomaslab.recurrent import validate_recurrent_events

print(inspect.signature(validate_recurrent_events))
print(validate_recurrent_events.__doc__)
~~~

### Source

[`src/thomaslab/recurrent.py#L16`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/recurrent.py#L16)

---

<!-- callable:thomaslab.recurrent.count_recurrent_events -->
## count_recurrent_events

### Purpose

Return one-row-per-patient recurrent-event counts and first/last event times.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def count_recurrent_events( events: pd.DataFrame, *, patient_col: str, event_time_col: str, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_time_col` | `event_time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`, `patient_col`, `event_time_col`.
- Referenced columns must exist in the input table: `patient_col`, `event_time_col`.

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

from thomaslab.recurrent import count_recurrent_events

result = count_recurrent_events(
    events=sample_df,
    patient_col='patient_id',
    event_time_col='event_time'
)

print(result)
~~~

### Related functions

- `validate_recurrent_events`
- `build_andersen_gill_intervals`
- `build_pwp_total_time_strata`
- `recurrent_event_rate`
- `summarize_recurrent_events`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/recurrent.py#L37`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/recurrent.py#L37)
- Repository search: [count_recurrent_events](https://github.com/appsplorer/thomaslab-core/search?q=count_recurrent_events&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return one-row-per-patient recurrent-event counts and first/last event times.

### API inspection

~~~python
import inspect
from thomaslab.recurrent import count_recurrent_events

print(inspect.signature(count_recurrent_events))
print(count_recurrent_events.__doc__)
~~~

### Source

[`src/thomaslab/recurrent.py#L37`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/recurrent.py#L37)

---

<!-- callable:thomaslab.recurrent.build_andersen_gill_intervals -->
## build_andersen_gill_intervals

### Purpose

Prepare total-time counting-process intervals for recurrent events.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_andersen_gill_intervals( cohort: pd.DataFrame, events: pd.DataFrame, *, patient_col: str, followup_end_col: str, event_time_col: str, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `cohort` | `cohort: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `followup_end_col` | `followup_end_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_time_col` | `event_time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `cohort`, `events`, `patient_col`, `followup_end_col`, `event_time_col`.
- Referenced columns must exist in the input table: `patient_col`, `followup_end_col`, `event_time_col`.

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

from thomaslab.recurrent import build_andersen_gill_intervals

result = build_andersen_gill_intervals(
    cohort=sample_df,
    events=sample_df,
    patient_col='patient_id',
    followup_end_col='followup_end',
    event_time_col='event_time'
)

print(result)
~~~

### Related functions

- `validate_recurrent_events`
- `count_recurrent_events`
- `build_pwp_total_time_strata`
- `recurrent_event_rate`
- `summarize_recurrent_events`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/recurrent.py#L52`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/recurrent.py#L52)
- Repository search: [build_andersen_gill_intervals](https://github.com/appsplorer/thomaslab-core/search?q=build_andersen_gill_intervals&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Prepare total-time counting-process intervals for recurrent events.

This prepares Andersen–Gill-style start/stop data but does not fit a model or
claim robust subject-level inference.

### API inspection

~~~python
import inspect
from thomaslab.recurrent import build_andersen_gill_intervals

print(inspect.signature(build_andersen_gill_intervals))
print(build_andersen_gill_intervals.__doc__)
~~~

### Source

[`src/thomaslab/recurrent.py#L52`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/recurrent.py#L52)

---

<!-- callable:thomaslab.recurrent.build_pwp_total_time_strata -->
## build_pwp_total_time_strata

### Purpose

Prepare PWP total-time rows with event-order strata.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_pwp_total_time_strata( cohort: pd.DataFrame, events: pd.DataFrame, *, patient_col: str, followup_end_col: str, event_time_col: str, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `cohort` | `cohort: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `followup_end_col` | `followup_end_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_time_col` | `event_time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `cohort`, `events`, `patient_col`, `followup_end_col`, `event_time_col`.
- Referenced columns must exist in the input table: `patient_col`, `followup_end_col`, `event_time_col`.

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

from thomaslab.recurrent import build_pwp_total_time_strata

result = build_pwp_total_time_strata(
    cohort=sample_df,
    events=sample_df,
    patient_col='patient_id',
    followup_end_col='followup_end',
    event_time_col='event_time'
)

print(result)
~~~

### Related functions

- `validate_recurrent_events`
- `count_recurrent_events`
- `build_andersen_gill_intervals`
- `recurrent_event_rate`
- `summarize_recurrent_events`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/recurrent.py#L104`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/recurrent.py#L104)
- Repository search: [build_pwp_total_time_strata](https://github.com/appsplorer/thomaslab-core/search?q=build_pwp_total_time_strata&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Prepare PWP total-time rows with event-order strata.

Patients enter stratum k only after experiencing event k-1.

### API inspection

~~~python
import inspect
from thomaslab.recurrent import build_pwp_total_time_strata

print(inspect.signature(build_pwp_total_time_strata))
print(build_pwp_total_time_strata.__doc__)
~~~

### Source

[`src/thomaslab/recurrent.py#L104`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/recurrent.py#L104)

---

<!-- callable:thomaslab.recurrent.recurrent_event_rate -->
## recurrent_event_rate

### Purpose

Calculate a crude recurrent-event rate per person-time.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def recurrent_event_rate( cohort: pd.DataFrame, events: pd.DataFrame, *, patient_col: str, followup_end_col: str, event_time_col: str, scale: float = 100.0, ) -> dict[str, float | int]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `cohort` | `cohort: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `followup_end_col` | `followup_end_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_time_col` | `event_time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `scale` | `scale: float = 100.0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `cohort`, `events`, `patient_col`, `followup_end_col`, `event_time_col`.
- Referenced columns must exist in the input table: `patient_col`, `followup_end_col`, `event_time_col`.

### Returns

`dict[str, float | int]`

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

from thomaslab.recurrent import recurrent_event_rate

result = recurrent_event_rate(
    cohort=sample_df,
    events=sample_df,
    patient_col='patient_id',
    followup_end_col='followup_end',
    event_time_col='event_time'
)

print(result)
~~~

### Related functions

- `validate_recurrent_events`
- `count_recurrent_events`
- `build_andersen_gill_intervals`
- `build_pwp_total_time_strata`
- `summarize_recurrent_events`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/recurrent.py#L127`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/recurrent.py#L127)
- Repository search: [recurrent_event_rate](https://github.com/appsplorer/thomaslab-core/search?q=recurrent_event_rate&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate a crude recurrent-event rate per person-time.

### API inspection

~~~python
import inspect
from thomaslab.recurrent import recurrent_event_rate

print(inspect.signature(recurrent_event_rate))
print(recurrent_event_rate.__doc__)
~~~

### Source

[`src/thomaslab/recurrent.py#L127`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/recurrent.py#L127)

---

<!-- callable:thomaslab.recurrent.summarize_recurrent_events -->
## summarize_recurrent_events

### Purpose

Return descriptive recurrent-event burden and crude rate.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_recurrent_events( cohort: pd.DataFrame, events: pd.DataFrame, *, patient_col: str, followup_end_col: str, event_time_col: str, ) -> dict[str, object]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `cohort` | `cohort: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `followup_end_col` | `followup_end_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_time_col` | `event_time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `cohort`, `events`, `patient_col`, `followup_end_col`, `event_time_col`.
- Referenced columns must exist in the input table: `patient_col`, `followup_end_col`, `event_time_col`.

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

from thomaslab.recurrent import summarize_recurrent_events

result = summarize_recurrent_events(
    cohort=sample_df,
    events=sample_df,
    patient_col='patient_id',
    followup_end_col='followup_end',
    event_time_col='event_time'
)

print(result)
~~~

### Related functions

- `validate_recurrent_events`
- `count_recurrent_events`
- `build_andersen_gill_intervals`
- `build_pwp_total_time_strata`
- `recurrent_event_rate`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/recurrent.py#L159`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/recurrent.py#L159)
- Repository search: [summarize_recurrent_events](https://github.com/appsplorer/thomaslab-core/search?q=summarize_recurrent_events&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return descriptive recurrent-event burden and crude rate.

### API inspection

~~~python
import inspect
from thomaslab.recurrent import summarize_recurrent_events

print(inspect.signature(summarize_recurrent_events))
print(summarize_recurrent_events.__doc__)
~~~

### Source

[`src/thomaslab/recurrent.py#L159`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/recurrent.py#L159)

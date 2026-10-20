# thomaslab.temporal

Temporal alignment and leakage-safe feature utilities for longitudinal EHR research.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 8

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.temporal.assign_time_zero -->
## assign_time_zero

### Purpose

Attach one explicit index date per patient to an event table.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def assign_time_zero( events: pd.DataFrame, index_events: pd.DataFrame, *, patient_id_col: str = "patient_id", event_date_col: str = "event_date", index_date_col: str = "index_date", index_selection: str = "first", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `index_events` | `index_events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_id_col` | `patient_id_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_date_col` | `event_date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_selection` | `index_selection: str = 'first'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`, `index_events`.
- Referenced columns must exist in the input table: `patient_id_col`, `event_date_col`, `index_date_col`.

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

from thomaslab.temporal import assign_time_zero

result = assign_time_zero(
    events=sample_df,
    index_events=sample_df
)

print(result)
~~~

### Related functions

- `days_from_index`
- `select_time_window`
- `merge_intervals`
- `calculate_time_to_event`
- `censor_followup`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/temporal.py#L11`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/temporal.py#L11)
- Repository search: [assign_time_zero](https://github.com/appsplorer/thomaslab-core/search?q=assign_time_zero&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Attach one explicit index date per patient to an event table.

### API inspection

~~~python
import inspect
from thomaslab.temporal import assign_time_zero

print(inspect.signature(assign_time_zero))
print(assign_time_zero.__doc__)
~~~

### Source

[`src/thomaslab/temporal.py#L11`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/temporal.py#L11)

---

<!-- callable:thomaslab.temporal.days_from_index -->
## days_from_index

### Purpose

Calculate signed event-time distance from index in fractional days.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def days_from_index( df: pd.DataFrame, *, event_date_col: str = "event_date", index_date_col: str = "index_date", output_col: str = "days_from_index", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `event_date_col` | `event_date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `output_col` | `output_col: str = 'days_from_index'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.
- Referenced columns must exist in the input table: `event_date_col`, `index_date_col`, `output_col`.

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

from thomaslab.temporal import days_from_index

result = days_from_index(
    df=sample_df
)

print(result)
~~~

### Related functions

- `assign_time_zero`
- `select_time_window`
- `merge_intervals`
- `calculate_time_to_event`
- `censor_followup`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/temporal.py#L42`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/temporal.py#L42)
- Repository search: [days_from_index](https://github.com/appsplorer/thomaslab-core/search?q=days_from_index&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate signed event-time distance from index in fractional days.

### API inspection

~~~python
import inspect
from thomaslab.temporal import days_from_index

print(inspect.signature(days_from_index))
print(days_from_index.__doc__)
~~~

### Source

[`src/thomaslab/temporal.py#L42`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/temporal.py#L42)

---

<!-- callable:thomaslab.temporal.select_time_window -->
## select_time_window

### Purpose

Select events within a protocol-defined window relative to index.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def select_time_window( df: pd.DataFrame, *, event_date_col: str = "event_date", index_date_col: str = "index_date", start_day: float, end_day: float, inclusive: str = "both", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `event_date_col` | `event_date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_day` | `start_day: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `end_day` | `end_day: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `inclusive` | `inclusive: str = 'both'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `start_day`, `end_day`.
- Referenced columns must exist in the input table: `event_date_col`, `index_date_col`.

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

from thomaslab.temporal import select_time_window

result = select_time_window(
    df=sample_df,
    start_day=0.5,
    end_day=0.5
)

print(result)
~~~

### Related functions

- `assign_time_zero`
- `days_from_index`
- `merge_intervals`
- `calculate_time_to_event`
- `censor_followup`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/temporal.py#L60`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/temporal.py#L60)
- Repository search: [select_time_window](https://github.com/appsplorer/thomaslab-core/search?q=select_time_window&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Select events within a protocol-defined window relative to index.

### API inspection

~~~python
import inspect
from thomaslab.temporal import select_time_window

print(inspect.signature(select_time_window))
print(select_time_window.__doc__)
~~~

### Source

[`src/thomaslab/temporal.py#L60`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/temporal.py#L60)

---

<!-- callable:thomaslab.temporal.merge_intervals -->
## merge_intervals

### Purpose

Merge overlapping or near-contiguous intervals within patient.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def merge_intervals( df: pd.DataFrame, *, patient_id_col: str = "patient_id", start_col: str = "start_date", end_col: str = "end_date", gap_days: float = 0.0, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_id_col` | `patient_id_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'start_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'end_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `gap_days` | `gap_days: float = 0.0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.
- Referenced columns must exist in the input table: `patient_id_col`, `start_col`, `end_col`.

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

from thomaslab.temporal import merge_intervals

result = merge_intervals(
    df=sample_df
)

print(result)
~~~

### Related functions

- `assign_time_zero`
- `days_from_index`
- `select_time_window`
- `calculate_time_to_event`
- `censor_followup`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/temporal.py#L81`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/temporal.py#L81)
- Repository search: [merge_intervals](https://github.com/appsplorer/thomaslab-core/search?q=merge_intervals&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Merge overlapping or near-contiguous intervals within patient.

### API inspection

~~~python
import inspect
from thomaslab.temporal import merge_intervals

print(inspect.signature(merge_intervals))
print(merge_intervals.__doc__)
~~~

### Source

[`src/thomaslab/temporal.py#L81`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/temporal.py#L81)

---

<!-- callable:thomaslab.temporal.calculate_time_to_event -->
## calculate_time_to_event

### Purpose

Construct first-event/censoring time from a cohort and event table.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_time_to_event( cohort: pd.DataFrame, events: pd.DataFrame, *, patient_id_col: str = "patient_id", index_date_col: str = "index_date", event_date_col: str = "event_date", censor_date_col: str | None = None, followup_days: float | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `cohort` | `cohort: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_id_col` | `patient_id_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_date_col` | `event_date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `censor_date_col` | `censor_date_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `followup_days` | `followup_days: float \| None = None` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `cohort`, `events`.
- Referenced columns must exist in the input table: `patient_id_col`, `index_date_col`, `event_date_col`, `censor_date_col`.

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

from thomaslab.temporal import calculate_time_to_event

result = calculate_time_to_event(
    cohort=sample_df,
    events=sample_df
)

print(result)
~~~

### Related functions

- `assign_time_zero`
- `days_from_index`
- `select_time_window`
- `merge_intervals`
- `censor_followup`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/temporal.py#L138`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/temporal.py#L138)
- Repository search: [calculate_time_to_event](https://github.com/appsplorer/thomaslab-core/search?q=calculate_time_to_event&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Construct first-event/censoring time from a cohort and event table.

### API inspection

~~~python
import inspect
from thomaslab.temporal import calculate_time_to_event

print(inspect.signature(calculate_time_to_event))
print(calculate_time_to_event.__doc__)
~~~

### Source

[`src/thomaslab/temporal.py#L138`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/temporal.py#L138)

---

<!-- callable:thomaslab.temporal.censor_followup -->
## censor_followup

### Purpose

Derive earliest valid follow-up end from loss/death/admin dates.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def censor_followup( df: pd.DataFrame, *, index_date_col: str = "index_date", candidate_end_cols: Sequence[str], administrative_end: str | pd.Timestamp | None = None, output_col: str = "censor_date", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `candidate_end_cols` | `candidate_end_cols: Sequence[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `administrative_end` | `administrative_end: str \| pd.Timestamp \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `output_col` | `output_col: str = 'censor_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `candidate_end_cols`.
- Referenced columns must exist in the input table: `index_date_col`, `output_col`.

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

from thomaslab.temporal import censor_followup

result = censor_followup(
    df=sample_df,
    candidate_end_cols=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `assign_time_zero`
- `days_from_index`
- `select_time_window`
- `merge_intervals`
- `calculate_time_to_event`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/temporal.py#L183`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/temporal.py#L183)
- Repository search: [censor_followup](https://github.com/appsplorer/thomaslab-core/search?q=censor_followup&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Derive earliest valid follow-up end from loss/death/admin dates.

### API inspection

~~~python
import inspect
from thomaslab.temporal import censor_followup

print(inspect.signature(censor_followup))
print(censor_followup.__doc__)
~~~

### Source

[`src/thomaslab/temporal.py#L183`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/temporal.py#L183)

---

<!-- callable:thomaslab.temporal.generate_temporal_features -->
## generate_temporal_features

### Purpose

Generate pre-index window features from long-form longitudinal measurements.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def generate_temporal_features( events: pd.DataFrame, *, patient_id_col: str = "patient_id", event_date_col: str = "event_date", index_date_col: str = "index_date", value_col: str = "value", feature_col: str | None = None, windows: Sequence[int] = (30, 90, 365), aggregations: Sequence[str] = ("latest", "mean", "min", "max", "count"), ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_id_col` | `patient_id_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_date_col` | `event_date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `value_col` | `value_col: str = 'value'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `feature_col` | `feature_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `windows` | `windows: Sequence[int] = (30, 90, 365)` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `aggregations` | `aggregations: Sequence[str] = ('latest', 'mean', 'min', 'max', 'count')` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`.
- Referenced columns must exist in the input table: `patient_id_col`, `event_date_col`, `index_date_col`, `value_col`, `feature_col`.

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

from thomaslab.temporal import generate_temporal_features

result = generate_temporal_features(
    events=sample_df
)

print(result)
~~~

### Related functions

- `assign_time_zero`
- `days_from_index`
- `select_time_window`
- `merge_intervals`
- `calculate_time_to_event`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/temporal.py#L218`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/temporal.py#L218)
- Repository search: [generate_temporal_features](https://github.com/appsplorer/thomaslab-core/search?q=generate_temporal_features&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Generate pre-index window features from long-form longitudinal measurements.

### API inspection

~~~python
import inspect
from thomaslab.temporal import generate_temporal_features

print(inspect.signature(generate_temporal_features))
print(generate_temporal_features.__doc__)
~~~

### Source

[`src/thomaslab/temporal.py#L218`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/temporal.py#L218)

---

<!-- callable:thomaslab.temporal.detect_future_information -->
## detect_future_information

### Purpose

Return rows whose feature timestamp exceeds the allowed index boundary.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_future_information( df: pd.DataFrame, *, feature_date_col: str, index_date_col: str = "index_date", allowed_post_index_days: float = 0.0, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `feature_date_col` | `feature_date_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `allowed_post_index_days` | `allowed_post_index_days: float = 0.0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `feature_date_col`.
- Referenced columns must exist in the input table: `feature_date_col`, `index_date_col`.

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

from thomaslab.temporal import detect_future_information

result = detect_future_information(
    df=sample_df,
    feature_date_col='feature_date'
)

print(result)
~~~

### Related functions

- `assign_time_zero`
- `days_from_index`
- `select_time_window`
- `merge_intervals`
- `calculate_time_to_event`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/temporal.py#L277`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/temporal.py#L277)
- Repository search: [detect_future_information](https://github.com/appsplorer/thomaslab-core/search?q=detect_future_information&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return rows whose feature timestamp exceeds the allowed index boundary.

### API inspection

~~~python
import inspect
from thomaslab.temporal import detect_future_information

print(inspect.signature(detect_future_information))
print(detect_future_information.__doc__)
~~~

### Source

[`src/thomaslab/temporal.py#L277`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/temporal.py#L277)

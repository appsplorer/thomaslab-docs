# thomaslab.dataset

Configuration-driven study dataset construction utilities.

The dataset layer assembles research-ready tables from already-onboarded canonical
inputs. It keeps cohort criteria, temporal windows, joins, and derived output
structure explicit rather than hiding study decisions inside model code.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 14

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.dataset.load_study_dataset_config -->
## load_study_dataset_config

### Purpose

Load a dataset-builder YAML/dictionary configuration.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def load_study_dataset_config(source: str | Path | Mapping[str, Any]) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `source` | `source: str \| Path \| Mapping[str, Any]` | Yes | Input source/path accepted by this callable. Keep raw-source provenance and do not overwrite the source. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `source`.

### Returns

`dict[str, Any]`

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

from thomaslab.dataset import load_study_dataset_config

result = load_study_dataset_config(
    source=sample_df
)

print(result)
~~~

### Related functions

- `define_index_date`
- `apply_inclusion_criteria`
- `apply_exclusion_criteria`
- `attach_index_dates`
- `apply_lookback_window`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/dataset.py#L27`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L27)
- Repository search: [load_study_dataset_config](https://github.com/appsplorer/thomaslab-core/search?q=load_study_dataset_config&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Load a dataset-builder YAML/dictionary configuration.

The function validates structure only. Clinical criteria remain study-defined.

### API inspection

~~~python
import inspect
from thomaslab.dataset import load_study_dataset_config

print(inspect.signature(load_study_dataset_config))
print(load_study_dataset_config.__doc__)
~~~

### Source

[`src/thomaslab/dataset.py#L27`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L27)

---

<!-- callable:thomaslab.dataset.define_index_date -->
## define_index_date

### Purpose

Define one index date per patient from an explicit event table.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def define_index_date( events: pd.DataFrame, *, patient_col: str = "patient_id", date_col: str = "event_date", selection: str = "first", event_col: str | None = None, allowed_events: Iterable[object] | None = None, output_col: str = "index_date", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `selection` | `selection: str = 'first'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `event_col` | `event_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `allowed_events` | `allowed_events: Iterable[object] \| None = None` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `output_col` | `output_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`.
- Referenced columns must exist in the input table: `patient_col`, `date_col`, `event_col`, `output_col`.

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

from thomaslab.dataset import define_index_date

result = define_index_date(
    events=sample_df
)

print(result)
~~~

### Related functions

- `load_study_dataset_config`
- `apply_inclusion_criteria`
- `apply_exclusion_criteria`
- `attach_index_dates`
- `apply_lookback_window`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/dataset.py#L52`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L52)
- Repository search: [define_index_date](https://github.com/appsplorer/thomaslab-core/search?q=define_index_date&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Define one index date per patient from an explicit event table.

### API inspection

~~~python
import inspect
from thomaslab.dataset import define_index_date

print(inspect.signature(define_index_date))
print(define_index_date.__doc__)
~~~

### Source

[`src/thomaslab/dataset.py#L52`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L52)

---

<!-- callable:thomaslab.dataset.apply_inclusion_criteria -->
## apply_inclusion_criteria

### Purpose

Apply named inclusion predicates sequentially and return a cohort-flow audit.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def apply_inclusion_criteria( cohort: pd.DataFrame, criteria: Mapping[str, Callable[[pd.DataFrame], pd.Series]], *, patient_col: str = "patient_id", ) -> tuple[pd.DataFrame, pd.DataFrame]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `cohort` | `cohort: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `criteria` | `criteria: Mapping[str, Callable[[pd.DataFrame], pd.Series]]` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `cohort`, `criteria`.
- Referenced columns must exist in the input table: `patient_col`.

### Returns

`tuple[pd.DataFrame, pd.DataFrame]`

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

from thomaslab.dataset import apply_inclusion_criteria

result = apply_inclusion_criteria(
    cohort=sample_df,
    criteria=sample_df
)

print(result)
~~~

### Related functions

- `load_study_dataset_config`
- `define_index_date`
- `apply_exclusion_criteria`
- `attach_index_dates`
- `apply_lookback_window`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/dataset.py#L85`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L85)
- Repository search: [apply_inclusion_criteria](https://github.com/appsplorer/thomaslab-core/search?q=apply_inclusion_criteria&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Apply named inclusion predicates sequentially and return a cohort-flow audit.

### API inspection

~~~python
import inspect
from thomaslab.dataset import apply_inclusion_criteria

print(inspect.signature(apply_inclusion_criteria))
print(apply_inclusion_criteria.__doc__)
~~~

### Source

[`src/thomaslab/dataset.py#L85`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L85)

---

<!-- callable:thomaslab.dataset.apply_exclusion_criteria -->
## apply_exclusion_criteria

### Purpose

Apply named exclusion predicates sequentially and return a cohort-flow audit.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def apply_exclusion_criteria( cohort: pd.DataFrame, criteria: Mapping[str, Callable[[pd.DataFrame], pd.Series]], *, patient_col: str = "patient_id", ) -> tuple[pd.DataFrame, pd.DataFrame]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `cohort` | `cohort: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `criteria` | `criteria: Mapping[str, Callable[[pd.DataFrame], pd.Series]]` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `cohort`, `criteria`.
- Referenced columns must exist in the input table: `patient_col`.

### Returns

`tuple[pd.DataFrame, pd.DataFrame]`

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

from thomaslab.dataset import apply_exclusion_criteria

result = apply_exclusion_criteria(
    cohort=sample_df,
    criteria=sample_df
)

print(result)
~~~

### Related functions

- `load_study_dataset_config`
- `define_index_date`
- `apply_inclusion_criteria`
- `attach_index_dates`
- `apply_lookback_window`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/dataset.py#L114`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L114)
- Repository search: [apply_exclusion_criteria](https://github.com/appsplorer/thomaslab-core/search?q=apply_exclusion_criteria&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Apply named exclusion predicates sequentially and return a cohort-flow audit.

### API inspection

~~~python
import inspect
from thomaslab.dataset import apply_exclusion_criteria

print(inspect.signature(apply_exclusion_criteria))
print(apply_exclusion_criteria.__doc__)
~~~

### Source

[`src/thomaslab/dataset.py#L114`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L114)

---

<!-- callable:thomaslab.dataset.attach_index_dates -->
## attach_index_dates

### Purpose

Attach one index date per patient to a longitudinal event table.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def attach_index_dates( events: pd.DataFrame, index: pd.DataFrame, *, patient_col: str = "patient_id", event_date_col: str = "event_date", index_date_col: str = "index_date", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `index` | `index: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_date_col` | `event_date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`, `index`.
- Referenced columns must exist in the input table: `patient_col`, `event_date_col`, `index_date_col`.

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

from thomaslab.dataset import attach_index_dates

result = attach_index_dates(
    events=sample_df,
    index=sample_df
)

print(result)
~~~

### Related functions

- `load_study_dataset_config`
- `define_index_date`
- `apply_inclusion_criteria`
- `apply_exclusion_criteria`
- `apply_lookback_window`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/dataset.py#L143`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L143)
- Repository search: [attach_index_dates](https://github.com/appsplorer/thomaslab-core/search?q=attach_index_dates&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Attach one index date per patient to a longitudinal event table.

### API inspection

~~~python
import inspect
from thomaslab.dataset import attach_index_dates

print(inspect.signature(attach_index_dates))
print(attach_index_dates.__doc__)
~~~

### Source

[`src/thomaslab/dataset.py#L143`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L143)

---

<!-- callable:thomaslab.dataset.apply_lookback_window -->
## apply_lookback_window

### Purpose

Keep events in the explicit pre-index baseline window.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def apply_lookback_window( events: pd.DataFrame, index: pd.DataFrame, *, lookback_days: int, include_index_day: bool = True, patient_col: str = "patient_id", event_date_col: str = "event_date", index_date_col: str = "index_date", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `index` | `index: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `lookback_days` | `lookback_days: int` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `include_index_day` | `include_index_day: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_date_col` | `event_date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`, `index`, `lookback_days`.
- Referenced columns must exist in the input table: `patient_col`, `event_date_col`, `index_date_col`.

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

from thomaslab.dataset import apply_lookback_window

result = apply_lookback_window(
    events=sample_df,
    index=sample_df,
    lookback_days=2
)

print(result)
~~~

### Related functions

- `load_study_dataset_config`
- `define_index_date`
- `apply_inclusion_criteria`
- `apply_exclusion_criteria`
- `attach_index_dates`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/dataset.py#L169`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L169)
- Repository search: [apply_lookback_window](https://github.com/appsplorer/thomaslab-core/search?q=apply_lookback_window&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Keep events in the explicit pre-index baseline window.

### API inspection

~~~python
import inspect
from thomaslab.dataset import apply_lookback_window

print(inspect.signature(apply_lookback_window))
print(apply_lookback_window.__doc__)
~~~

### Source

[`src/thomaslab/dataset.py#L169`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L169)

---

<!-- callable:thomaslab.dataset.apply_followup_window -->
## apply_followup_window

### Purpose

Keep events in the explicit post-index outcome/follow-up window.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def apply_followup_window( events: pd.DataFrame, index: pd.DataFrame, *, followup_days: int, include_index_day: bool = False, patient_col: str = "patient_id", event_date_col: str = "event_date", index_date_col: str = "index_date", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `index` | `index: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `followup_days` | `followup_days: int` | Yes | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `include_index_day` | `include_index_day: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_date_col` | `event_date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`, `index`, `followup_days`.
- Referenced columns must exist in the input table: `patient_col`, `event_date_col`, `index_date_col`.

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

from thomaslab.dataset import apply_followup_window

result = apply_followup_window(
    events=sample_df,
    index=sample_df,
    followup_days=2
)

print(result)
~~~

### Related functions

- `load_study_dataset_config`
- `define_index_date`
- `apply_inclusion_criteria`
- `apply_exclusion_criteria`
- `attach_index_dates`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/dataset.py#L195`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L195)
- Repository search: [apply_followup_window](https://github.com/appsplorer/thomaslab-core/search?q=apply_followup_window&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Keep events in the explicit post-index outcome/follow-up window.

### API inspection

~~~python
import inspect
from thomaslab.dataset import apply_followup_window

print(inspect.signature(apply_followup_window))
print(apply_followup_window.__doc__)
~~~

### Source

[`src/thomaslab/dataset.py#L195`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L195)

---

<!-- callable:thomaslab.dataset.aggregate_baseline_features -->
## aggregate_baseline_features

### Purpose

Aggregate long baseline features to one row per patient and feature.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def aggregate_baseline_features( events: pd.DataFrame, *, patient_col: str = "patient_id", feature_col: str = "feature", value_col: str = "value", date_col: str = "event_date", aggregation: str = "latest", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `feature_col` | `feature_col: str = 'feature'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `value_col` | `value_col: str = 'value'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `aggregation` | `aggregation: str = 'latest'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`.
- Referenced columns must exist in the input table: `patient_col`, `feature_col`, `value_col`, `date_col`.

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

from thomaslab.dataset import aggregate_baseline_features

result = aggregate_baseline_features(
    events=sample_df
)

print(result)
~~~

### Related functions

- `load_study_dataset_config`
- `define_index_date`
- `apply_inclusion_criteria`
- `apply_exclusion_criteria`
- `attach_index_dates`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/dataset.py#L221`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L221)
- Repository search: [aggregate_baseline_features](https://github.com/appsplorer/thomaslab-core/search?q=aggregate_baseline_features&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Aggregate long baseline features to one row per patient and feature.

### API inspection

~~~python
import inspect
from thomaslab.dataset import aggregate_baseline_features

print(inspect.signature(aggregate_baseline_features))
print(aggregate_baseline_features.__doc__)
~~~

### Source

[`src/thomaslab/dataset.py#L221`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L221)

---

<!-- callable:thomaslab.dataset.join_patient_domains -->
## join_patient_domains

### Purpose

Merge one-row-per-patient domains with explicit provenance prefixes.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def join_patient_domains( base: pd.DataFrame, domains: Mapping[str, pd.DataFrame], *, patient_col: str = "patient_id", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `base` | `base: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `domains` | `domains: Mapping[str, pd.DataFrame]` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `base`, `domains`.
- Referenced columns must exist in the input table: `patient_col`.

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

from thomaslab.dataset import join_patient_domains

result = join_patient_domains(
    base=sample_df,
    domains=sample_df
)

print(result)
~~~

### Related functions

- `load_study_dataset_config`
- `define_index_date`
- `apply_inclusion_criteria`
- `apply_exclusion_criteria`
- `attach_index_dates`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/dataset.py#L265`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L265)
- Repository search: [join_patient_domains](https://github.com/appsplorer/thomaslab-core/search?q=join_patient_domains&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Merge one-row-per-patient domains with explicit provenance prefixes.

### API inspection

~~~python
import inspect
from thomaslab.dataset import join_patient_domains

print(inspect.signature(join_patient_domains))
print(join_patient_domains.__doc__)
~~~

### Source

[`src/thomaslab/dataset.py#L265`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L265)

---

<!-- callable:thomaslab.dataset.create_patient_level_dataset -->
## create_patient_level_dataset

### Purpose

Create a one-row-per-patient analysis frame from index plus static domains.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def create_patient_level_dataset( index: pd.DataFrame, *, static_domains: Mapping[str, pd.DataFrame] | None = None, patient_col: str = "patient_id", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `index` | `index: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `static_domains` | `static_domains: Mapping[str, pd.DataFrame] \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `index`.
- Referenced columns must exist in the input table: `patient_col`.

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

from thomaslab.dataset import create_patient_level_dataset

result = create_patient_level_dataset(
    index=sample_df
)

print(result)
~~~

### Related functions

- `load_study_dataset_config`
- `define_index_date`
- `apply_inclusion_criteria`
- `apply_exclusion_criteria`
- `attach_index_dates`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/dataset.py#L288`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L288)
- Repository search: [create_patient_level_dataset](https://github.com/appsplorer/thomaslab-core/search?q=create_patient_level_dataset&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create a one-row-per-patient analysis frame from index plus static domains.

### API inspection

~~~python
import inspect
from thomaslab.dataset import create_patient_level_dataset

print(inspect.signature(create_patient_level_dataset))
print(create_patient_level_dataset.__doc__)
~~~

### Source

[`src/thomaslab/dataset.py#L288`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L288)

---

<!-- callable:thomaslab.dataset.create_event_level_dataset -->
## create_event_level_dataset

### Purpose

Create event-level data with explicit days-from-index.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def create_event_level_dataset( index: pd.DataFrame, events: pd.DataFrame, *, patient_col: str = "patient_id", event_date_col: str = "event_date", index_date_col: str = "index_date", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `index` | `index: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_date_col` | `event_date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `index`, `events`.
- Referenced columns must exist in the input table: `patient_col`, `event_date_col`, `index_date_col`.

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

from thomaslab.dataset import create_event_level_dataset

result = create_event_level_dataset(
    index=sample_df,
    events=sample_df
)

print(result)
~~~

### Related functions

- `load_study_dataset_config`
- `define_index_date`
- `apply_inclusion_criteria`
- `apply_exclusion_criteria`
- `attach_index_dates`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/dataset.py#L301`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L301)
- Repository search: [create_event_level_dataset](https://github.com/appsplorer/thomaslab-core/search?q=create_event_level_dataset&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create event-level data with explicit days-from-index.

### API inspection

~~~python
import inspect
from thomaslab.dataset import create_event_level_dataset

print(inspect.signature(create_event_level_dataset))
print(create_event_level_dataset.__doc__)
~~~

### Source

[`src/thomaslab/dataset.py#L301`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L301)

---

<!-- callable:thomaslab.dataset.create_time_to_event_dataset -->
## create_time_to_event_dataset

### Purpose

Create one-row-per-patient time-to-first-event data with explicit censoring.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def create_time_to_event_dataset( index: pd.DataFrame, outcomes: pd.DataFrame, *, patient_col: str = "patient_id", index_date_col: str = "index_date", event_date_col: str = "event_date", censor_date_col: str | None = None, fixed_followup_days: int | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `index` | `index: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcomes` | `outcomes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_date_col` | `event_date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `censor_date_col` | `censor_date_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `fixed_followup_days` | `fixed_followup_days: int \| None = None` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `index`, `outcomes`.
- Referenced columns must exist in the input table: `patient_col`, `index_date_col`, `event_date_col`, `censor_date_col`.

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

from thomaslab.dataset import create_time_to_event_dataset

result = create_time_to_event_dataset(
    index=sample_df,
    outcomes=sample_df
)

print(result)
~~~

### Related functions

- `load_study_dataset_config`
- `define_index_date`
- `apply_inclusion_criteria`
- `apply_exclusion_criteria`
- `attach_index_dates`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/dataset.py#L319`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L319)
- Repository search: [create_time_to_event_dataset](https://github.com/appsplorer/thomaslab-core/search?q=create_time_to_event_dataset&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create one-row-per-patient time-to-first-event data with explicit censoring.

### API inspection

~~~python
import inspect
from thomaslab.dataset import create_time_to_event_dataset

print(inspect.signature(create_time_to_event_dataset))
print(create_time_to_event_dataset.__doc__)
~~~

### Source

[`src/thomaslab/dataset.py#L319`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L319)

---

<!-- callable:thomaslab.dataset.build_dataset_manifest -->
## build_dataset_manifest

### Purpose

Create a JSON-serializable dataset manifest with deterministic schema hash.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_dataset_manifest( dataset: pd.DataFrame, *, study_name: str, patient_col: str = "patient_id", target_col: str | None = None, config: Mapping[str, Any] | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `dataset` | `dataset: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `study_name` | `study_name: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `target_col` | `target_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `config` | `config: Mapping[str, Any] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `dataset`, `study_name`.
- Referenced columns must exist in the input table: `patient_col`, `target_col`.

### Returns

`dict[str, Any]`

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

from thomaslab.dataset import build_dataset_manifest

result = build_dataset_manifest(
    dataset=sample_df,
    study_name="value"
)

print(result)
~~~

### Related functions

- `load_study_dataset_config`
- `define_index_date`
- `apply_inclusion_criteria`
- `apply_exclusion_criteria`
- `attach_index_dates`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/dataset.py#L370`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L370)
- Repository search: [build_dataset_manifest](https://github.com/appsplorer/thomaslab-core/search?q=build_dataset_manifest&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create a JSON-serializable dataset manifest with deterministic schema hash.

### API inspection

~~~python
import inspect
from thomaslab.dataset import build_dataset_manifest

print(inspect.signature(build_dataset_manifest))
print(build_dataset_manifest.__doc__)
~~~

### Source

[`src/thomaslab/dataset.py#L370`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L370)

---

<!-- callable:thomaslab.dataset.audit_dataset_build -->
## audit_dataset_build

### Purpose

Return structural checks for an analysis dataset before splitting/modeling.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_dataset_build( dataset: pd.DataFrame, *, patient_col: str = "patient_id", target_col: str | None = None, index_date_col: str | None = "index_date", ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `dataset` | `dataset: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `target_col` | `target_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str \| None = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `dataset`.
- Referenced columns must exist in the input table: `patient_col`, `target_col`, `index_date_col`.

### Returns

`dict[str, Any]`

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

from thomaslab.dataset import audit_dataset_build

result = audit_dataset_build(
    dataset=sample_df
)

print(result)
~~~

### Related functions

- `load_study_dataset_config`
- `define_index_date`
- `apply_inclusion_criteria`
- `apply_exclusion_criteria`
- `attach_index_dates`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/dataset.py#L404`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L404)
- Repository search: [audit_dataset_build](https://github.com/appsplorer/thomaslab-core/search?q=audit_dataset_build&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return structural checks for an analysis dataset before splitting/modeling.

### API inspection

~~~python
import inspect
from thomaslab.dataset import audit_dataset_build

print(inspect.signature(audit_dataset_build))
print(audit_dataset_build.__doc__)
~~~

### Source

[`src/thomaslab/dataset.py#L404`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/dataset.py#L404)

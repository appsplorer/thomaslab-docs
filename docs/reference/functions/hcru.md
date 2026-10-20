# thomaslab.hcru

Healthcare resource utilization (HCRU) research utilities.

All encounter categories are study-defined. The module does not infer clinical setting from
free-text facility names or billing codes without an explicit reviewed mapping.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 7

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.hcru.map_encounter_type -->
## map_encounter_type

### Purpose

Map local encounter labels/codes to reviewed canonical categories.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def map_encounter_type( series: pd.Series, mapping: Mapping[str, str], *, strict: bool = False, ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `series` | `series: pd.Series` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `mapping` | `mapping: Mapping[str, str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strict` | `strict: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `series`, `mapping`.

### Returns

`pd.Series`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.hcru import map_encounter_type

result = map_encounter_type(
    series=sample_series,
    mapping={}
)

print(result)
~~~

### Related functions

- `build_encounter_episodes`
- `calculate_length_of_stay`
- `identify_readmissions`
- `summarize_utilization`
- `calculate_utilization_rate`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/hcru.py#L21`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/hcru.py#L21)
- Repository search: [map_encounter_type](https://github.com/appsplorer/thomaslab-core/search?q=map_encounter_type&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Map local encounter labels/codes to reviewed canonical categories.

Mapping is case-insensitive on the source side. Unknown values remain ``Unknown`` unless
``strict=True``.

### API inspection

~~~python
import inspect
from thomaslab.hcru import map_encounter_type

print(inspect.signature(map_encounter_type))
print(map_encounter_type.__doc__)
~~~

### Source

[`src/thomaslab/hcru.py#L21`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/hcru.py#L21)

---

<!-- callable:thomaslab.hcru.build_encounter_episodes -->
## build_encounter_episodes

### Purpose

Validate and merge overlapping/near-contiguous encounters of the same type.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_encounter_episodes( encounters: pd.DataFrame, *, patient_col: str = "patient_id", start_col: str = "encounter_start", end_col: str = "encounter_end", type_col: str = "encounter_type", merge_gap_days: int = 0, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `encounters` | `encounters: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'encounter_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'encounter_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `type_col` | `type_col: str = 'encounter_type'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `merge_gap_days` | `merge_gap_days: int = 0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `encounters`.
- Referenced columns must exist in the input table: `patient_col`, `start_col`, `end_col`, `type_col`.

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

from thomaslab.hcru import build_encounter_episodes

result = build_encounter_episodes(
    encounters=sample_df
)

print(result)
~~~

### Related functions

- `map_encounter_type`
- `calculate_length_of_stay`
- `identify_readmissions`
- `summarize_utilization`
- `calculate_utilization_rate`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/hcru.py#L50`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/hcru.py#L50)
- Repository search: [build_encounter_episodes](https://github.com/appsplorer/thomaslab-core/search?q=build_encounter_episodes&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate and merge overlapping/near-contiguous encounters of the same type.

``encounter_end`` is inclusive. Single-date encounters should have identical start/end.

### API inspection

~~~python
import inspect
from thomaslab.hcru import build_encounter_episodes

print(inspect.signature(build_encounter_episodes))
print(build_encounter_episodes.__doc__)
~~~

### Source

[`src/thomaslab/hcru.py#L50`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/hcru.py#L50)

---

<!-- callable:thomaslab.hcru.calculate_length_of_stay -->
## calculate_length_of_stay

### Purpose

Calculate encounter length of stay in days.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_length_of_stay( encounters: pd.DataFrame, *, start_col: str = "episode_start", end_col: str = "episode_end", output_col: str = "length_of_stay_days", inclusive: bool = False, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `encounters` | `encounters: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `start_col` | `start_col: str = 'episode_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'episode_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `output_col` | `output_col: str = 'length_of_stay_days'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `inclusive` | `inclusive: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `encounters`.
- Referenced columns must exist in the input table: `start_col`, `end_col`, `output_col`.

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

from thomaslab.hcru import calculate_length_of_stay

result = calculate_length_of_stay(
    encounters=sample_df
)

print(result)
~~~

### Related functions

- `map_encounter_type`
- `build_encounter_episodes`
- `identify_readmissions`
- `summarize_utilization`
- `calculate_utilization_rate`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/hcru.py#L121`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/hcru.py#L121)
- Repository search: [calculate_length_of_stay](https://github.com/appsplorer/thomaslab-core/search?q=calculate_length_of_stay&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate encounter length of stay in days.

By default this uses elapsed days (discharge - admission). Set ``inclusive=True`` only when
the study definition counts both calendar endpoints.

### API inspection

~~~python
import inspect
from thomaslab.hcru import calculate_length_of_stay

print(inspect.signature(calculate_length_of_stay))
print(calculate_length_of_stay.__doc__)
~~~

### Source

[`src/thomaslab/hcru.py#L121`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/hcru.py#L121)

---

<!-- callable:thomaslab.hcru.identify_readmissions -->
## identify_readmissions

### Purpose

Flag subsequent inpatient admissions within a configurable post-discharge window.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def identify_readmissions( episodes: pd.DataFrame, *, patient_col: str = "patient_id", start_col: str = "episode_start", end_col: str = "episode_end", inpatient_values: Sequence[str] = ("inpatient",), type_col: str = "encounter_type", window_days: int = 30, include_same_day: bool = False, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `episodes` | `episodes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'episode_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'episode_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `inpatient_values` | `inpatient_values: Sequence[str] = ('inpatient',)` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `type_col` | `type_col: str = 'encounter_type'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `window_days` | `window_days: int = 30` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `include_same_day` | `include_same_day: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `episodes`.
- Referenced columns must exist in the input table: `patient_col`, `start_col`, `end_col`, `type_col`.

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

from thomaslab.hcru import identify_readmissions

result = identify_readmissions(
    episodes=sample_df
)

print(result)
~~~

### Related functions

- `map_encounter_type`
- `build_encounter_episodes`
- `calculate_length_of_stay`
- `summarize_utilization`
- `calculate_utilization_rate`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/hcru.py#L147`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/hcru.py#L147)
- Repository search: [identify_readmissions](https://github.com/appsplorer/thomaslab-core/search?q=identify_readmissions&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Flag subsequent inpatient admissions within a configurable post-discharge window.

This is a timing rule only; it does not determine whether a readmission is planned or
clinically preventable.

### API inspection

~~~python
import inspect
from thomaslab.hcru import identify_readmissions

print(inspect.signature(identify_readmissions))
print(identify_readmissions.__doc__)
~~~

### Source

[`src/thomaslab/hcru.py#L147`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/hcru.py#L147)

---

<!-- callable:thomaslab.hcru.summarize_utilization -->
## summarize_utilization

### Purpose

Create one-row-per-patient encounter counts and utilization days by category.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_utilization( episodes: pd.DataFrame, *, patient_col: str = "patient_id", type_col: str = "encounter_type", start_col: str = "episode_start", end_col: str = "episode_end", categories: Sequence[str] | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `episodes` | `episodes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `type_col` | `type_col: str = 'encounter_type'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'episode_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'episode_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `categories` | `categories: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `episodes`.
- Referenced columns must exist in the input table: `patient_col`, `type_col`, `start_col`, `end_col`.

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

from thomaslab.hcru import summarize_utilization

result = summarize_utilization(
    episodes=sample_df
)

print(result)
~~~

### Related functions

- `map_encounter_type`
- `build_encounter_episodes`
- `calculate_length_of_stay`
- `identify_readmissions`
- `calculate_utilization_rate`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/hcru.py#L190`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/hcru.py#L190)
- Repository search: [summarize_utilization](https://github.com/appsplorer/thomaslab-core/search?q=summarize_utilization&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create one-row-per-patient encounter counts and utilization days by category.

### API inspection

~~~python
import inspect
from thomaslab.hcru import summarize_utilization

print(inspect.signature(summarize_utilization))
print(summarize_utilization.__doc__)
~~~

### Source

[`src/thomaslab/hcru.py#L190`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/hcru.py#L190)

---

<!-- callable:thomaslab.hcru.calculate_utilization_rate -->
## calculate_utilization_rate

### Purpose

Calculate patient-level event rates per requested person-years of observation.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_utilization_rate( events: pd.DataFrame, observation: pd.DataFrame, *, patient_col: str = "patient_id", obs_start_col: str = "observation_start", obs_end_col: str = "observation_end", event_date_col: str = "episode_start", rate_per_person_years: float = 100.0, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `observation` | `observation: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `obs_start_col` | `obs_start_col: str = 'observation_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `obs_end_col` | `obs_end_col: str = 'observation_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_date_col` | `event_date_col: str = 'episode_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `rate_per_person_years` | `rate_per_person_years: float = 100.0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`, `observation`.
- Referenced columns must exist in the input table: `patient_col`, `obs_start_col`, `obs_end_col`, `event_date_col`.

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

from thomaslab.hcru import calculate_utilization_rate

result = calculate_utilization_rate(
    events=sample_df,
    observation=sample_df
)

print(result)
~~~

### Related functions

- `map_encounter_type`
- `build_encounter_episodes`
- `calculate_length_of_stay`
- `identify_readmissions`
- `summarize_utilization`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/hcru.py#L218`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/hcru.py#L218)
- Repository search: [calculate_utilization_rate](https://github.com/appsplorer/thomaslab-core/search?q=calculate_utilization_rate&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate patient-level event rates per requested person-years of observation.

### API inspection

~~~python
import inspect
from thomaslab.hcru import calculate_utilization_rate

print(inspect.signature(calculate_utilization_rate))
print(calculate_utilization_rate.__doc__)
~~~

### Source

[`src/thomaslab/hcru.py#L218`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/hcru.py#L218)

---

<!-- callable:thomaslab.hcru.build_hcru_endpoint_table -->
## build_hcru_endpoint_table

### Purpose

Build a patient-level HCRU endpoint table from encounter episodes and observation windows.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_hcru_endpoint_table( episodes: pd.DataFrame, observation: pd.DataFrame, *, patient_col: str = "patient_id", type_col: str = "encounter_type", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `episodes` | `episodes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `observation` | `observation: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `type_col` | `type_col: str = 'encounter_type'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `episodes`, `observation`.
- Referenced columns must exist in the input table: `patient_col`, `type_col`.

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

from thomaslab.hcru import build_hcru_endpoint_table

result = build_hcru_endpoint_table(
    episodes=sample_df,
    observation=sample_df
)

print(result)
~~~

### Related functions

- `map_encounter_type`
- `build_encounter_episodes`
- `calculate_length_of_stay`
- `identify_readmissions`
- `summarize_utilization`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/hcru.py#L265`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/hcru.py#L265)
- Repository search: [build_hcru_endpoint_table](https://github.com/appsplorer/thomaslab-core/search?q=build_hcru_endpoint_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build a patient-level HCRU endpoint table from encounter episodes and observation windows.

### API inspection

~~~python
import inspect
from thomaslab.hcru import build_hcru_endpoint_table

print(inspect.signature(build_hcru_endpoint_table))
print(build_hcru_endpoint_table.__doc__)
~~~

### Source

[`src/thomaslab/hcru.py#L265`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/hcru.py#L265)

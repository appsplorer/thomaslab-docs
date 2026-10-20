# thomaslab.registry

Registry and index-event construction utilities.

The module is intentionally code-set agnostic. Procedure/diagnosis definitions must
be supplied by the study rather than hardcoded into the library.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 9

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.registry.build_index_event -->
## build_index_event

### Purpose

Select one auditable index event per patient.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_index_event( events: pd.DataFrame, *, patient_col: str, date_col: str, event_col: str | None = None, allowed_events: Iterable[object] | None = None, selection: str = "first", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `allowed_events` | `allowed_events: Iterable[object] \| None = None` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `selection` | `selection: str = 'first'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`, `patient_col`, `date_col`.
- Referenced columns must exist in the input table: `patient_col`, `date_col`, `event_col`.

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

from thomaslab.registry import build_index_event

result = build_index_event(
    events=sample_df,
    patient_col='patient_id',
    date_col='event_date'
)

print(result)
~~~

### Related functions

- `link_index_event_to_pgx`
- `classify_index_indication`
- `build_registry_baseline`
- `build_followup_schedule`
- `validate_registry_followup`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/registry.py#L28`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/registry.py#L28)
- Repository search: [build_index_event](https://github.com/appsplorer/thomaslab-core/search?q=build_index_event&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Select one auditable index event per patient.

If ``allowed_events`` is supplied, ``event_col`` is required and matching is
exact after uppercase/dot-removal normalization.

### API inspection

~~~python
import inspect
from thomaslab.registry import build_index_event

print(inspect.signature(build_index_event))
print(build_index_event.__doc__)
~~~

### Source

[`src/thomaslab/registry.py#L28`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/registry.py#L28)

---

<!-- callable:thomaslab.registry.link_index_event_to_pgx -->
## link_index_event_to_pgx

### Purpose

Link each index event to the nearest dated PGx result for the same patient.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def link_index_event_to_pgx( index_events: pd.DataFrame, pgx_results: pd.DataFrame, *, patient_col: str = "patient_id", index_date_col: str = "index_date", pgx_date_col: str = "event_date", max_abs_days: int | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `index_events` | `index_events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `pgx_results` | `pgx_results: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `pgx_date_col` | `pgx_date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `max_abs_days` | `max_abs_days: int \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `index_events`, `pgx_results`.
- Referenced columns must exist in the input table: `patient_col`, `index_date_col`, `pgx_date_col`.

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

from thomaslab.registry import link_index_event_to_pgx

result = link_index_event_to_pgx(
    index_events=sample_df,
    pgx_results=sample_df
)

print(result)
~~~

### Related functions

- `build_index_event`
- `classify_index_indication`
- `build_registry_baseline`
- `build_followup_schedule`
- `validate_registry_followup`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/registry.py#L67`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/registry.py#L67)
- Repository search: [link_index_event_to_pgx](https://github.com/appsplorer/thomaslab-core/search?q=link_index_event_to_pgx&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Link each index event to the nearest dated PGx result for the same patient.

### API inspection

~~~python
import inspect
from thomaslab.registry import link_index_event_to_pgx

print(inspect.signature(link_index_event_to_pgx))
print(link_index_event_to_pgx.__doc__)
~~~

### Source

[`src/thomaslab/registry.py#L67`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/registry.py#L67)

---

<!-- callable:thomaslab.registry.classify_index_indication -->
## classify_index_indication

### Purpose

Classify study-defined diagnosis groups around each index event.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def classify_index_indication( diagnoses: pd.DataFrame, index_events: pd.DataFrame, *, patient_col: str, diagnosis_date_col: str, code_col: str, code_sets: Mapping[str, Iterable[object]], window_days: int = 1, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `diagnoses` | `diagnoses: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `index_events` | `index_events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `diagnosis_date_col` | `diagnosis_date_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `code_col` | `code_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `code_sets` | `code_sets: Mapping[str, Iterable[object]]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `window_days` | `window_days: int = 1` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `diagnoses`, `index_events`, `patient_col`, `diagnosis_date_col`, `code_col`, `code_sets`.
- Referenced columns must exist in the input table: `patient_col`, `diagnosis_date_col`, `code_col`.

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

from thomaslab.registry import classify_index_indication

result = classify_index_indication(
    diagnoses=sample_df,
    index_events=sample_df,
    patient_col='patient_id',
    diagnosis_date_col='diagnosis_date',
    code_col='code',
    code_sets={}
)

print(result)
~~~

### Related functions

- `build_index_event`
- `link_index_event_to_pgx`
- `build_registry_baseline`
- `build_followup_schedule`
- `validate_registry_followup`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/registry.py#L110`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/registry.py#L110)
- Repository search: [classify_index_indication](https://github.com/appsplorer/thomaslab-core/search?q=classify_index_indication&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Classify study-defined diagnosis groups around each index event.

``code_sets`` may contain labels such as ``acs``, ``stemi`` and ``nstemi``,
but the library does not supply the clinical code lists.

### API inspection

~~~python
import inspect
from thomaslab.registry import classify_index_indication

print(inspect.signature(classify_index_indication))
print(classify_index_indication.__doc__)
~~~

### Source

[`src/thomaslab/registry.py#L110`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/registry.py#L110)

---

<!-- callable:thomaslab.registry.build_registry_baseline -->
## build_registry_baseline

### Purpose

Build one-row-per-patient registry baseline table.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_registry_baseline( person: pd.DataFrame, index_events: pd.DataFrame, *, patient_col: str = "patient_id", baseline_features: pd.DataFrame | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `person` | `person: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `index_events` | `index_events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `baseline_features` | `baseline_features: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `person`, `index_events`.
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

from thomaslab.registry import build_registry_baseline

result = build_registry_baseline(
    person=sample_df,
    index_events=sample_df
)

print(result)
~~~

### Related functions

- `build_index_event`
- `link_index_event_to_pgx`
- `classify_index_indication`
- `build_followup_schedule`
- `validate_registry_followup`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/registry.py#L151`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/registry.py#L151)
- Repository search: [build_registry_baseline](https://github.com/appsplorer/thomaslab-core/search?q=build_registry_baseline&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build one-row-per-patient registry baseline table.

### API inspection

~~~python
import inspect
from thomaslab.registry import build_registry_baseline

print(inspect.signature(build_registry_baseline))
print(build_registry_baseline.__doc__)
~~~

### Source

[`src/thomaslab/registry.py#L151`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/registry.py#L151)

---

<!-- callable:thomaslab.registry.build_followup_schedule -->
## build_followup_schedule

### Purpose

Generate planned follow-up dates from a registry index date.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_followup_schedule( registry: pd.DataFrame, *, patient_col: str = "patient_id", index_date_col: str = "index_date", target_days: Sequence[int] = (30, 180, 365), ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `registry` | `registry: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `target_days` | `target_days: Sequence[int] = (30, 180, 365)` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `registry`.
- Referenced columns must exist in the input table: `patient_col`, `index_date_col`.

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

from thomaslab.registry import build_followup_schedule

result = build_followup_schedule(
    registry=sample_df
)

print(result)
~~~

### Related functions

- `build_index_event`
- `link_index_event_to_pgx`
- `classify_index_indication`
- `build_registry_baseline`
- `validate_registry_followup`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/registry.py#L182`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/registry.py#L182)
- Repository search: [build_followup_schedule](https://github.com/appsplorer/thomaslab-core/search?q=build_followup_schedule&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Generate planned follow-up dates from a registry index date.

### API inspection

~~~python
import inspect
from thomaslab.registry import build_followup_schedule

print(inspect.signature(build_followup_schedule))
print(build_followup_schedule.__doc__)
~~~

### Source

[`src/thomaslab/registry.py#L182`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/registry.py#L182)

---

<!-- callable:thomaslab.registry.validate_registry_followup -->
## validate_registry_followup

### Purpose

Match each planned follow-up to the nearest observed follow-up date.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_registry_followup( schedule: pd.DataFrame, observed_followup: pd.DataFrame, *, patient_col: str = "patient_id", observed_date_col: str = "followup_date", tolerance_days: int = 30, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `schedule` | `schedule: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `observed_followup` | `observed_followup: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `observed_date_col` | `observed_date_col: str = 'followup_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `tolerance_days` | `tolerance_days: int = 30` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `schedule`, `observed_followup`.
- Referenced columns must exist in the input table: `patient_col`, `observed_date_col`.

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

from thomaslab.registry import validate_registry_followup

result = validate_registry_followup(
    schedule=sample_df,
    observed_followup=sample_df
)

print(result)
~~~

### Related functions

- `build_index_event`
- `link_index_event_to_pgx`
- `classify_index_indication`
- `build_registry_baseline`
- `build_followup_schedule`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/registry.py#L209`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/registry.py#L209)
- Repository search: [validate_registry_followup](https://github.com/appsplorer/thomaslab-core/search?q=validate_registry_followup&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Match each planned follow-up to the nearest observed follow-up date.

### API inspection

~~~python
import inspect
from thomaslab.registry import validate_registry_followup

print(inspect.signature(validate_registry_followup))
print(validate_registry_followup.__doc__)
~~~

### Source

[`src/thomaslab/registry.py#L209`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/registry.py#L209)

---

<!-- callable:thomaslab.registry.summarize_registry_followup -->
## summarize_registry_followup

### Purpose

Summarize completion rates by planned follow-up day.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_registry_followup( validation: pd.DataFrame, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `validation` | `validation: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `validation`.

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

from thomaslab.registry import summarize_registry_followup

result = summarize_registry_followup(
    validation=sample_df
)

print(result)
~~~

### Related functions

- `build_index_event`
- `link_index_event_to_pgx`
- `classify_index_indication`
- `build_registry_baseline`
- `build_followup_schedule`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/registry.py#L247`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/registry.py#L247)
- Repository search: [summarize_registry_followup](https://github.com/appsplorer/thomaslab-core/search?q=summarize_registry_followup&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize completion rates by planned follow-up day.

### API inspection

~~~python
import inspect
from thomaslab.registry import summarize_registry_followup

print(inspect.signature(summarize_registry_followup))
print(summarize_registry_followup.__doc__)
~~~

### Source

[`src/thomaslab/registry.py#L247`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/registry.py#L247)

---

<!-- callable:thomaslab.registry.build_precision_registry -->
## build_precision_registry

### Purpose

Build a generic precision-medicine registry baseline.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_precision_registry( person: pd.DataFrame, index_events: pd.DataFrame, *, pgx_results: pd.DataFrame | None = None, baseline_features: pd.DataFrame | None = None, patient_col: str = "patient_id", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `person` | `person: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `index_events` | `index_events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `pgx_results` | `pgx_results: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `baseline_features` | `baseline_features: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `person`, `index_events`.
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

from thomaslab.registry import build_precision_registry

result = build_precision_registry(
    person=sample_df,
    index_events=sample_df
)

print(result)
~~~

### Related functions

- `build_index_event`
- `link_index_event_to_pgx`
- `classify_index_indication`
- `build_registry_baseline`
- `build_followup_schedule`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/registry.py#L259`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/registry.py#L259)
- Repository search: [build_precision_registry](https://github.com/appsplorer/thomaslab-core/search?q=build_precision_registry&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build a generic precision-medicine registry baseline.

This function deliberately does not assume PCI, ACS, or a particular gene.

### API inspection

~~~python
import inspect
from thomaslab.registry import build_precision_registry

print(inspect.signature(build_precision_registry))
print(build_precision_registry.__doc__)
~~~

### Source

[`src/thomaslab/registry.py#L259`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/registry.py#L259)

---

<!-- callable:thomaslab.registry.audit_registry -->
## audit_registry

### Purpose

Return compact registry integrity diagnostics.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_registry( registry: pd.DataFrame, *, patient_col: str = "patient_id", index_date_col: str = "index_date", ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `registry` | `registry: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `registry`.
- Referenced columns must exist in the input table: `patient_col`, `index_date_col`.

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

from thomaslab.registry import audit_registry

result = audit_registry(
    registry=sample_df
)

print(result)
~~~

### Related functions

- `build_index_event`
- `link_index_event_to_pgx`
- `classify_index_indication`
- `build_registry_baseline`
- `build_followup_schedule`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/registry.py#L287`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/registry.py#L287)
- Repository search: [audit_registry](https://github.com/appsplorer/thomaslab-core/search?q=audit_registry&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return compact registry integrity diagnostics.

### API inspection

~~~python
import inspect
from thomaslab.registry import audit_registry

print(inspect.signature(audit_registry))
print(audit_registry.__doc__)
~~~

### Source

[`src/thomaslab/registry.py#L287`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/registry.py#L287)

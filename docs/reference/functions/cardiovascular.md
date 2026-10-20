# thomaslab.cardiovascular

Cardiovascular endpoint helpers built on explicit event-component definitions.

## Research-use boundary

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

## Self-service orientation

- Related guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 4

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.cardiovascular.build_mae_endpoint -->
## build_mae_endpoint

### Purpose

Build a first-event major atherothrombotic event (MAE) composite.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_mae_endpoint( events: pd.DataFrame, *, components: Iterable[str] = THOMAS_JAHA_2022_MAE_COMPONENTS, patient_col: str = "patient_id", date_col: str = "event_date", component_col: str = "component", patient_universe: Iterable[object] | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `components` | `components: Iterable[str] = THOMAS_JAHA_2022_MAE_COMPONENTS` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `component_col` | `component_col: str = 'component'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `patient_universe` | `patient_universe: Iterable[object] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`.
- Referenced columns must exist in the input table: `patient_col`, `date_col`, `component_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

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

from thomaslab.cardiovascular import build_mae_endpoint

result = build_mae_endpoint(
    events=sample_df
)

print(result)
~~~

### Related functions

- `build_mace_endpoint`
- `restrict_endpoint_window`
- `summarize_endpoint_incidence`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cardiovascular.py#L20`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cardiovascular.py#L20)
- Repository search: [build_mae_endpoint](https://github.com/appsplorer/thomaslab-core/search?q=build_mae_endpoint&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build a first-event major atherothrombotic event (MAE) composite.

The default component labels reproduce the component structure used in Thomas et
al. JAHA 2022. They are event labels only; this function does not define or infer
the ICD/procedure/NLP rules used to ascertain each component.

### API inspection

~~~python
import inspect
from thomaslab.cardiovascular import build_mae_endpoint

print(inspect.signature(build_mae_endpoint))
print(build_mae_endpoint.__doc__)
~~~

### Source

[`src/thomaslab/cardiovascular.py#L20`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cardiovascular.py#L20)

---

<!-- callable:thomaslab.cardiovascular.build_mace_endpoint -->
## build_mace_endpoint

### Purpose

Build a MACE composite from study-specified components.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_mace_endpoint( events: pd.DataFrame, *, components: Iterable[str], patient_col: str = "patient_id", date_col: str = "event_date", component_col: str = "component", patient_universe: Iterable[object] | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `components` | `components: Iterable[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `component_col` | `component_col: str = 'component'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `patient_universe` | `patient_universe: Iterable[object] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`, `components`.
- Referenced columns must exist in the input table: `patient_col`, `date_col`, `component_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

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

from thomaslab.cardiovascular import build_mace_endpoint

result = build_mace_endpoint(
    events=sample_df,
    components="value"
)

print(result)
~~~

### Related functions

- `build_mae_endpoint`
- `restrict_endpoint_window`
- `summarize_endpoint_incidence`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cardiovascular.py#L46`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cardiovascular.py#L46)
- Repository search: [build_mace_endpoint](https://github.com/appsplorer/thomaslab-core/search?q=build_mace_endpoint&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build a MACE composite from study-specified components.

MACE definitions vary materially across studies, so components are required and
no universal default is assumed.

### API inspection

~~~python
import inspect
from thomaslab.cardiovascular import build_mace_endpoint

print(inspect.signature(build_mace_endpoint))
print(build_mace_endpoint.__doc__)
~~~

### Source

[`src/thomaslab/cardiovascular.py#L46`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cardiovascular.py#L46)

---

<!-- callable:thomaslab.cardiovascular.restrict_endpoint_window -->
## restrict_endpoint_window

### Purpose

Restrict outcome events to 0..max_days after each patient's index date.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def restrict_endpoint_window( events: pd.DataFrame, index_dates: pd.DataFrame, *, max_days: int, patient_col: str = "patient_id", event_date_col: str = "event_date", index_date_col: str = "index_date", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `index_dates` | `index_dates: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `max_days` | `max_days: int` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_date_col` | `event_date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`, `index_dates`, `max_days`.
- Referenced columns must exist in the input table: `patient_col`, `event_date_col`, `index_date_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

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

from thomaslab.cardiovascular import restrict_endpoint_window

result = restrict_endpoint_window(
    events=sample_df,
    index_dates=sample_df,
    max_days=2
)

print(result)
~~~

### Related functions

- `build_mae_endpoint`
- `build_mace_endpoint`
- `summarize_endpoint_incidence`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cardiovascular.py#L71`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cardiovascular.py#L71)
- Repository search: [restrict_endpoint_window](https://github.com/appsplorer/thomaslab-core/search?q=restrict_endpoint_window&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Restrict outcome events to 0..max_days after each patient's index date.

### API inspection

~~~python
import inspect
from thomaslab.cardiovascular import restrict_endpoint_window

print(inspect.signature(restrict_endpoint_window))
print(restrict_endpoint_window.__doc__)
~~~

### Source

[`src/thomaslab/cardiovascular.py#L71`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cardiovascular.py#L71)

---

<!-- callable:thomaslab.cardiovascular.summarize_endpoint_incidence -->
## summarize_endpoint_incidence

### Purpose

Summarize crude cumulative incidence and optional events per 100 person-years.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_endpoint_incidence( endpoint: pd.DataFrame, *, endpoint_col: str, followup_days: int | float | None = None, ) -> dict[str, float | int]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `endpoint` | `endpoint: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `endpoint_col` | `endpoint_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `followup_days` | `followup_days: int \| float \| None = None` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `endpoint`, `endpoint_col`.
- Referenced columns must exist in the input table: `endpoint_col`.

### Returns

`dict[str, float | int]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

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

from thomaslab.cardiovascular import summarize_endpoint_incidence

result = summarize_endpoint_incidence(
    endpoint=sample_df,
    endpoint_col='endpoint'
)

print(result)
~~~

### Related functions

- `build_mae_endpoint`
- `build_mace_endpoint`
- `restrict_endpoint_window`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cardiovascular.py#L101`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cardiovascular.py#L101)
- Repository search: [summarize_endpoint_incidence](https://github.com/appsplorer/thomaslab-core/search?q=summarize_endpoint_incidence&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize crude cumulative incidence and optional events per 100 person-years.

### API inspection

~~~python
import inspect
from thomaslab.cardiovascular import summarize_endpoint_incidence

print(inspect.signature(summarize_endpoint_incidence))
print(summarize_endpoint_incidence.__doc__)
~~~

### Source

[`src/thomaslab/cardiovascular.py#L101`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cardiovascular.py#L101)

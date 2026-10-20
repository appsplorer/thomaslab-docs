# thomaslab.platelet

Platelet-function testing utilities for research workflows.

## Research-use boundary

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

## Self-service orientation

- Related guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 6

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.platelet.parse_pru -->
## parse_pru

### Purpose

Parse VerifyNow P2Y12 reaction units (PRU) conservatively.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def parse_pru( values: pd.Series | Sequence[object], *, minimum: float = 0.0, maximum: float | None = None ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `values` | `values: pd.Series \| Sequence[object]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `minimum` | `minimum: float = 0.0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `maximum` | `maximum: float \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `values`.

### Returns

`pd.Series`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.platelet import parse_pru

result = parse_pru(
    values=sample_series
)

print(result)
~~~

### Related functions

- `classify_high_platelet_reactivity`
- `calculate_pru_change`
- `link_pru_to_context`
- `build_platelet_pgx_dataset`
- `summarize_pru`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/platelet.py#L17`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/platelet.py#L17)
- Repository search: [parse_pru](https://github.com/appsplorer/thomaslab-core/search?q=parse_pru&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Parse VerifyNow P2Y12 reaction units (PRU) conservatively.

### API inspection

~~~python
import inspect
from thomaslab.platelet import parse_pru

print(inspect.signature(parse_pru))
print(parse_pru.__doc__)
~~~

### Source

[`src/thomaslab/platelet.py#L17`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/platelet.py#L17)

---

<!-- callable:thomaslab.platelet.classify_high_platelet_reactivity -->
## classify_high_platelet_reactivity

### Purpose

Classify high platelet reactivity using a study-supplied PRU threshold.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def classify_high_platelet_reactivity( values: pd.Series | Sequence[object], *, threshold: float, inclusive: bool = True ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `values` | `values: pd.Series \| Sequence[object]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `threshold` | `threshold: float` | Yes | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |
| `inclusive` | `inclusive: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `values`, `threshold`.

### Returns

`pd.Series`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.platelet import classify_high_platelet_reactivity

result = classify_high_platelet_reactivity(
    values=sample_series,
    threshold=0.5
)

print(result)
~~~

### Related functions

- `parse_pru`
- `calculate_pru_change`
- `link_pru_to_context`
- `build_platelet_pgx_dataset`
- `summarize_pru`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/platelet.py#L29`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/platelet.py#L29)
- Repository search: [classify_high_platelet_reactivity](https://github.com/appsplorer/thomaslab-core/search?q=classify_high_platelet_reactivity&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Classify high platelet reactivity using a study-supplied PRU threshold.

### API inspection

~~~python
import inspect
from thomaslab.platelet import classify_high_platelet_reactivity

print(inspect.signature(classify_high_platelet_reactivity))
print(classify_high_platelet_reactivity.__doc__)
~~~

### Source

[`src/thomaslab/platelet.py#L29`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/platelet.py#L29)

---

<!-- callable:thomaslab.platelet.calculate_pru_change -->
## calculate_pru_change

### Purpose

Calculate within-patient PRU change from an explicit baseline.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_pru_change( df: pd.DataFrame, *, patient_col: str, pru_col: str, time_col: str, baseline_time: float = 0.0, followup_time: float | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `pru_col` | `pru_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `baseline_time` | `baseline_time: float = 0.0` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `followup_time` | `followup_time: float \| None = None` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `patient_col`, `pru_col`, `time_col`.
- Referenced columns must exist in the input table: `patient_col`, `pru_col`, `time_col`.

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

from thomaslab.platelet import calculate_pru_change

result = calculate_pru_change(
    df=sample_df,
    patient_col='patient_id',
    pru_col='pru',
    time_col='event_date'
)

print(result)
~~~

### Related functions

- `parse_pru`
- `classify_high_platelet_reactivity`
- `link_pru_to_context`
- `build_platelet_pgx_dataset`
- `summarize_pru`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/platelet.py#L43`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/platelet.py#L43)
- Repository search: [calculate_pru_change](https://github.com/appsplorer/thomaslab-core/search?q=calculate_pru_change&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate within-patient PRU change from an explicit baseline.

### API inspection

~~~python
import inspect
from thomaslab.platelet import calculate_pru_change

print(inspect.signature(calculate_pru_change))
print(calculate_pru_change.__doc__)
~~~

### Source

[`src/thomaslab/platelet.py#L43`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/platelet.py#L43)

---

<!-- callable:thomaslab.platelet.link_pru_to_context -->
## link_pru_to_context

### Purpose

Join patient-level PRU data to optional PGx/drug summaries.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def link_pru_to_context( platelet: pd.DataFrame, *, patient_col: str, pru_col: str, pgx: pd.DataFrame | None = None, drug: pd.DataFrame | None = None, threshold: float | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `platelet` | `platelet: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `pru_col` | `pru_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `pgx` | `pgx: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `drug` | `drug: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `threshold` | `threshold: float \| None = None` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `platelet`, `patient_col`, `pru_col`.
- Referenced columns must exist in the input table: `patient_col`, `pru_col`.

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

from thomaslab.platelet import link_pru_to_context

result = link_pru_to_context(
    platelet=sample_df,
    patient_col='patient_id',
    pru_col='pru'
)

print(result)
~~~

### Related functions

- `parse_pru`
- `classify_high_platelet_reactivity`
- `calculate_pru_change`
- `build_platelet_pgx_dataset`
- `summarize_pru`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/platelet.py#L87`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/platelet.py#L87)
- Repository search: [link_pru_to_context](https://github.com/appsplorer/thomaslab-core/search?q=link_pru_to_context&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Join patient-level PRU data to optional PGx/drug summaries.

### API inspection

~~~python
import inspect
from thomaslab.platelet import link_pru_to_context

print(inspect.signature(link_pru_to_context))
print(link_pru_to_context.__doc__)
~~~

### Source

[`src/thomaslab/platelet.py#L87`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/platelet.py#L87)

---

<!-- callable:thomaslab.platelet.build_platelet_pgx_dataset -->
## build_platelet_pgx_dataset

### Purpose

Build a platelet-function + PGx research table with explicit HPR threshold.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_platelet_pgx_dataset( platelet: pd.DataFrame, *, patient_col: str, pru_col: str, pgx: pd.DataFrame, drug: pd.DataFrame | None = None, threshold: float, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `platelet` | `platelet: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `pru_col` | `pru_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `pgx` | `pgx: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `drug` | `drug: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `threshold` | `threshold: float` | Yes | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `platelet`, `patient_col`, `pru_col`, `pgx`, `threshold`.
- Referenced columns must exist in the input table: `patient_col`, `pru_col`.

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

from thomaslab.platelet import build_platelet_pgx_dataset

result = build_platelet_pgx_dataset(
    platelet=sample_df,
    patient_col='patient_id',
    pru_col='pru',
    pgx=sample_df,
    threshold=0.5
)

print(result)
~~~

### Related functions

- `parse_pru`
- `classify_high_platelet_reactivity`
- `calculate_pru_change`
- `link_pru_to_context`
- `summarize_pru`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/platelet.py#L115`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/platelet.py#L115)
- Repository search: [build_platelet_pgx_dataset](https://github.com/appsplorer/thomaslab-core/search?q=build_platelet_pgx_dataset&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build a platelet-function + PGx research table with explicit HPR threshold.

### API inspection

~~~python
import inspect
from thomaslab.platelet import build_platelet_pgx_dataset

print(inspect.signature(build_platelet_pgx_dataset))
print(build_platelet_pgx_dataset.__doc__)
~~~

### Source

[`src/thomaslab/platelet.py#L115`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/platelet.py#L115)

---

<!-- callable:thomaslab.platelet.summarize_pru -->
## summarize_pru

### Purpose

Summarize PRU distribution and optional high-reactivity frequency.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_pru( df: pd.DataFrame, *, pru_col: str, group_col: str | None = None, threshold: float | None = None ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `pru_col` | `pru_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `group_col` | `group_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `threshold` | `threshold: float \| None = None` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `pru_col`.
- Referenced columns must exist in the input table: `pru_col`, `group_col`.

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

from thomaslab.platelet import summarize_pru

result = summarize_pru(
    df=sample_df,
    pru_col='pru'
)

print(result)
~~~

### Related functions

- `parse_pru`
- `classify_high_platelet_reactivity`
- `calculate_pru_change`
- `link_pru_to_context`
- `build_platelet_pgx_dataset`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/platelet.py#L130`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/platelet.py#L130)
- Repository search: [summarize_pru](https://github.com/appsplorer/thomaslab-core/search?q=summarize_pru&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize PRU distribution and optional high-reactivity frequency.

### API inspection

~~~python
import inspect
from thomaslab.platelet import summarize_pru

print(inspect.signature(summarize_pru))
print(summarize_pru.__doc__)
~~~

### Source

[`src/thomaslab/platelet.py#L130`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/platelet.py#L130)

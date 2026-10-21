# thomaslab.onboard

Self-service onboarding for previously unseen research datasets.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 13

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.onboard.inspect_source -->
## inspect_source

### Purpose

Inspect an unfamiliar source and return profile, semantics, and domain ranking.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def inspect_source(source: str | Path | pd.DataFrame, *, sample_rows: int = 5000) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `source` | `source: str \| Path \| pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `sample_rows` | `sample_rows: int = 5000` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

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

from thomaslab.onboard import inspect_source

result = inspect_source(
    source=sample_df
)

print(result)
~~~

### Related functions

- `infer_dataset_domains`
- `suggest_unit_mapping`
- `infer_code_vocabulary`
- `generate_adapter_bundle`
- `propose_adapter_revision`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/onboard.py#L46`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L46)
- Repository search: [inspect_source](https://github.com/appsplorer/thomaslab-core/search?q=inspect_source&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Inspect an unfamiliar source and return profile, semantics, and domain ranking.

### API inspection

~~~python
import inspect
from thomaslab.onboard import inspect_source

print(inspect.signature(inspect_source))
print(inspect_source.__doc__)
~~~

### Source

[`src/thomaslab/onboard.py#L46`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L46)

---

<!-- callable:thomaslab.onboard.infer_dataset_domains -->
## infer_dataset_domains

### Purpose

Return plausible canonical domains above a structural score threshold.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def infer_dataset_domains(data: pd.DataFrame, *, min_score: float = 0.45) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `data` | `data: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `min_score` | `min_score: float = 0.45` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `data`.

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

from thomaslab.onboard import infer_dataset_domains

result = infer_dataset_domains(
    data=sample_df
)

print(result)
~~~

### Related functions

- `inspect_source`
- `suggest_unit_mapping`
- `infer_code_vocabulary`
- `generate_adapter_bundle`
- `propose_adapter_revision`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/onboard.py#L57`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L57)
- Repository search: [infer_dataset_domains](https://github.com/appsplorer/thomaslab-core/search?q=infer_dataset_domains&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return plausible canonical domains above a structural score threshold.

### API inspection

~~~python
import inspect
from thomaslab.onboard import infer_dataset_domains

print(inspect.signature(infer_dataset_domains))
print(infer_dataset_domains.__doc__)
~~~

### Source

[`src/thomaslab/onboard.py#L57`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L57)

---

<!-- callable:thomaslab.onboard.suggest_unit_mapping -->
## suggest_unit_mapping

### Purpose

Summarize source units for manual review; no conversion is guessed.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def suggest_unit_mapping( df: pd.DataFrame, unit_col: str, *, measure_col: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `unit_col` | `unit_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `measure_col` | `measure_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `unit_col`.
- Referenced columns must exist in the input table: `unit_col`, `measure_col`.

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

from thomaslab.onboard import suggest_unit_mapping

result = suggest_unit_mapping(
    df=sample_df,
    unit_col='unit'
)

print(result)
~~~

### Related functions

- `inspect_source`
- `infer_dataset_domains`
- `infer_code_vocabulary`
- `generate_adapter_bundle`
- `propose_adapter_revision`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/onboard.py#L63`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L63)
- Repository search: [suggest_unit_mapping](https://github.com/appsplorer/thomaslab-core/search?q=suggest_unit_mapping&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize source units for manual review; no conversion is guessed.

### API inspection

~~~python
import inspect
from thomaslab.onboard import suggest_unit_mapping

print(inspect.signature(suggest_unit_mapping))
print(suggest_unit_mapping.__doc__)
~~~

### Source

[`src/thomaslab/onboard.py#L63`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L63)

---

<!-- callable:thomaslab.onboard.infer_code_vocabulary -->
## infer_code_vocabulary

### Purpose

Return conservative vocabulary candidates from code-shape evidence.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def infer_code_vocabulary(series: pd.Series) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `series` | `series: pd.Series` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `series`.

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

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.onboard import infer_code_vocabulary

result = infer_code_vocabulary(
    series=sample_series
)

print(result)
~~~

### Related functions

- `inspect_source`
- `infer_dataset_domains`
- `suggest_unit_mapping`
- `generate_adapter_bundle`
- `propose_adapter_revision`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/onboard.py#L89`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L89)
- Repository search: [infer_code_vocabulary](https://github.com/appsplorer/thomaslab-core/search?q=infer_code_vocabulary&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return conservative vocabulary candidates from code-shape evidence.

Numeric identifiers are intentionally reported as ambiguous because RxNorm,
SNOMED CT, local concepts, and other systems can overlap in shape.

### API inspection

~~~python
import inspect
from thomaslab.onboard import infer_code_vocabulary

print(inspect.signature(infer_code_vocabulary))
print(infer_code_vocabulary.__doc__)
~~~

### Source

[`src/thomaslab/onboard.py#L89`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L89)

---

<!-- callable:thomaslab.onboard.generate_adapter_bundle -->
## generate_adapter_bundle

### Purpose

Create a new *draft* bundle without replacing prior review artifacts.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def generate_adapter_bundle( data: pd.DataFrame, output_dir: str | Path, *, dataset_name: str, required_columns: Sequence[str] | None = None, domain: str | None = None, overwrite: bool = False, ) -> dict[str, Path]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `data` | `data: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `output_dir` | `output_dir: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `dataset_name` | `dataset_name: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `required_columns` | `required_columns: Sequence[str] \| None = None` | No | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `domain` | `domain: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `overwrite` | `overwrite: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `data`, `output_dir`, `dataset_name`.

### Returns

`dict[str, Path]`

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

from thomaslab.onboard import generate_adapter_bundle

result = generate_adapter_bundle(
    data=sample_df,
    output_dir="value",
    dataset_name="value"
)

print(result)
~~~

### Related functions

- `inspect_source`
- `infer_dataset_domains`
- `suggest_unit_mapping`
- `infer_code_vocabulary`
- `propose_adapter_revision`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/onboard.py#L127`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L127)
- Repository search: [generate_adapter_bundle](https://github.com/appsplorer/thomaslab-core/search?q=generate_adapter_bundle&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create a new *draft* bundle without replacing prior review artifacts.

An existing bundle requires an explicit versioned revision; ``overwrite``
is retained as a compatibility keyword but deliberately cannot bypass this
safety boundary.

### API inspection

~~~python
import inspect
from thomaslab.onboard import generate_adapter_bundle

print(inspect.signature(generate_adapter_bundle))
print(generate_adapter_bundle.__doc__)
~~~

### Source

[`src/thomaslab/onboard.py#L127`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L127)

---

<!-- callable:thomaslab.onboard.propose_adapter_revision -->
## propose_adapter_revision

### Purpose

Compare current and proposed explicit mappings without writing files.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def propose_adapter_revision( existing: str | Path | Mapping[str, Any], proposed: str | Path | Mapping[str, Any], ) -> MappingDiff
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `existing` | `existing: str \| Path \| Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `proposed` | `proposed: str \| Path \| Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `existing`, `proposed`.

### Returns

`MappingDiff`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.onboard import propose_adapter_revision

result = propose_adapter_revision(
    existing={},
    proposed={}
)

print(result)
~~~

### Related functions

- `inspect_source`
- `infer_dataset_domains`
- `suggest_unit_mapping`
- `infer_code_vocabulary`
- `generate_adapter_bundle`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/onboard.py#L207`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L207)
- Repository search: [propose_adapter_revision](https://github.com/appsplorer/thomaslab-core/search?q=propose_adapter_revision&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compare current and proposed explicit mappings without writing files.

### API inspection

~~~python
import inspect
from thomaslab.onboard import propose_adapter_revision

print(inspect.signature(propose_adapter_revision))
print(propose_adapter_revision.__doc__)
~~~

### Source

[`src/thomaslab/onboard.py#L207`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L207)

---

<!-- callable:thomaslab.onboard.validate_adapter_bundle -->
## validate_adapter_bundle

### Purpose

Apply a schema mapping and optionally validate the standardized table contract.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_adapter_bundle( data: pd.DataFrame, schema: str | Path | Mapping[str, Any], contract: str | Path | Mapping[str, Any] | None = None, *, required_columns: Sequence[str] | None = None, strict: bool = True, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `data` | `data: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `schema` | `schema: str \| Path \| Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `contract` | `contract: str \| Path \| Mapping[str, Any] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `required_columns` | `required_columns: Sequence[str] \| None = None` | No | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `strict` | `strict: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `data`, `schema`.

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

from thomaslab.onboard import validate_adapter_bundle

result = validate_adapter_bundle(
    data=sample_df,
    schema={}
)

print(result)
~~~

### Related functions

- `inspect_source`
- `infer_dataset_domains`
- `suggest_unit_mapping`
- `infer_code_vocabulary`
- `generate_adapter_bundle`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/onboard.py#L227`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L227)
- Repository search: [validate_adapter_bundle](https://github.com/appsplorer/thomaslab-core/search?q=validate_adapter_bundle&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Apply a schema mapping and optionally validate the standardized table contract.

### API inspection

~~~python
import inspect
from thomaslab.onboard import validate_adapter_bundle

print(inspect.signature(validate_adapter_bundle))
print(validate_adapter_bundle.__doc__)
~~~

### Source

[`src/thomaslab/onboard.py#L227`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L227)

---

<!-- callable:thomaslab.onboard.register_dataset_adapter -->
## register_dataset_adapter

### Purpose

Deprecated unsafe registration; requires migration to reviewed workflow.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def register_dataset_adapter( schema_path: str | Path, registry_dir: str | Path, *, dataset_name: str, version: str = "1", contract_path: str | Path | None = None, overwrite: bool = False, ) -> Path
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `schema_path` | `schema_path: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `registry_dir` | `registry_dir: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `dataset_name` | `dataset_name: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `version` | `version: str = '1'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `contract_path` | `contract_path: str \| Path \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `overwrite` | `overwrite: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `schema_path`, `registry_dir`, `dataset_name`.

### Returns

`Path`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.onboard import register_dataset_adapter

result = register_dataset_adapter(
    schema_path="path/to/input.csv",
    registry_dir="value",
    dataset_name="value"
)

print(result)
~~~

### Related functions

- `inspect_source`
- `infer_dataset_domains`
- `suggest_unit_mapping`
- `infer_code_vocabulary`
- `generate_adapter_bundle`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/onboard.py#L257`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L257)
- Repository search: [register_dataset_adapter](https://github.com/appsplorer/thomaslab-core/search?q=register_dataset_adapter&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Deprecated unsafe registration; requires migration to reviewed workflow.

### API inspection

~~~python
import inspect
from thomaslab.onboard import register_dataset_adapter

print(inspect.signature(register_dataset_adapter))
print(register_dataset_adapter.__doc__)
~~~

### Source

[`src/thomaslab/onboard.py#L257`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L257)

---

<!-- callable:thomaslab.onboard.generate_onboarding_report -->
## generate_onboarding_report

### Purpose

Create a JSON-serializable onboarding summary for review and audit.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def generate_onboarding_report( data: pd.DataFrame, *, mapping_report: pd.DataFrame | None = None, contract_report: Mapping[str, Any] | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `data` | `data: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `mapping_report` | `mapping_report: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `contract_report` | `contract_report: Mapping[str, Any] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `data`.

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

from thomaslab.onboard import generate_onboarding_report

result = generate_onboarding_report(
    data=sample_df
)

print(result)
~~~

### Related functions

- `inspect_source`
- `infer_dataset_domains`
- `suggest_unit_mapping`
- `infer_code_vocabulary`
- `generate_adapter_bundle`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/onboard.py#L274`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L274)
- Repository search: [generate_onboarding_report](https://github.com/appsplorer/thomaslab-core/search?q=generate_onboarding_report&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create a JSON-serializable onboarding summary for review and audit.

### API inspection

~~~python
import inspect
from thomaslab.onboard import generate_onboarding_report

print(inspect.signature(generate_onboarding_report))
print(generate_onboarding_report.__doc__)
~~~

### Source

[`src/thomaslab/onboard.py#L274`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L274)

---

<!-- callable:thomaslab.onboard.DatasetOnboarder.inspect -->
## DatasetOnboarder.inspect

### Purpose

Profile the sampled source and infer conservative structural candidates.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def inspect(self) -> dict[str, Any]
~~~

### Parameters

This callable has no public parameters beyond instance/class binding.

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- This callable has no required public arguments beyond instance/class construction.

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
from thomaslab.onboard import DatasetOnboarder

# Construct DatasetOnboarder with its documented constructor first.
# instance = DatasetOnboarder(...)
result = instance.inspect()

print(result)
~~~

### Related functions

- `inspect_source`
- `infer_dataset_domains`
- `suggest_unit_mapping`
- `infer_code_vocabulary`
- `generate_adapter_bundle`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/onboard.py#L327`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L327)
- Repository search: [DatasetOnboarder.inspect](https://github.com/appsplorer/thomaslab-core/search?q=DatasetOnboarder.inspect&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Profile the sampled source and infer conservative structural candidates.

### API inspection

~~~python
import inspect
from thomaslab.onboard import DatasetOnboarder

print(inspect.signature(DatasetOnboarder.inspect))
print(DatasetOnboarder.inspect.__doc__)
~~~

### Source

[`src/thomaslab/onboard.py#L327`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L327)

---

<!-- callable:thomaslab.onboard.DatasetOnboarder.generate -->
## DatasetOnboarder.generate

### Purpose

Generate a reviewable schema/contract adapter bundle for this source.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def generate( self, output_dir: str | Path, *, dataset_name: str, required_columns: Sequence[str] | None = None, domain: str | None = None, ) -> dict[str, Path]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `output_dir` | `output_dir: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `dataset_name` | `dataset_name: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `required_columns` | `required_columns: Sequence[str] \| None = None` | No | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `domain` | `domain: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `output_dir`, `dataset_name`.

### Returns

`dict[str, Path]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.onboard import DatasetOnboarder

# Construct DatasetOnboarder with its documented constructor first.
# instance = DatasetOnboarder(...)
result = instance.generate(
    output_dir="value",
    dataset_name="value"
)

print(result)
~~~

### Related functions

- `inspect_source`
- `infer_dataset_domains`
- `suggest_unit_mapping`
- `infer_code_vocabulary`
- `generate_adapter_bundle`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/onboard.py#L332`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L332)
- Repository search: [DatasetOnboarder.generate](https://github.com/appsplorer/thomaslab-core/search?q=DatasetOnboarder.generate&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Generate a reviewable schema/contract adapter bundle for this source.

### API inspection

~~~python
import inspect
from thomaslab.onboard import DatasetOnboarder

print(inspect.signature(DatasetOnboarder.generate))
print(DatasetOnboarder.generate.__doc__)
~~~

### Source

[`src/thomaslab/onboard.py#L332`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L332)

---

<!-- callable:thomaslab.onboard.DatasetOnboarder.validate -->
## DatasetOnboarder.validate

### Purpose

Preview validation by default; full_dataset runs every source row.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate( self, *, required_columns: Sequence[str] | None = None, strict: bool = True, full_dataset: bool = False, ) -> Any
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `required_columns` | `required_columns: Sequence[str] \| None = None` | No | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `strict` | `strict: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `full_dataset` | `full_dataset: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- This callable has no required public arguments beyond instance/class construction.

### Returns

`Any`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.onboard import DatasetOnboarder

# Construct DatasetOnboarder with its documented constructor first.
# instance = DatasetOnboarder(...)
result = instance.validate()

print(result)
~~~

### Related functions

- `inspect_source`
- `infer_dataset_domains`
- `suggest_unit_mapping`
- `infer_code_vocabulary`
- `generate_adapter_bundle`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/onboard.py#L350`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L350)
- Repository search: [DatasetOnboarder.validate](https://github.com/appsplorer/thomaslab-core/search?q=DatasetOnboarder.validate&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Preview validation by default; full_dataset runs every source row.

### API inspection

~~~python
import inspect
from thomaslab.onboard import DatasetOnboarder

print(inspect.signature(DatasetOnboarder.validate))
print(DatasetOnboarder.validate.__doc__)
~~~

### Source

[`src/thomaslab/onboard.py#L350`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L350)

---

<!-- callable:thomaslab.onboard.DatasetOnboarder.freeze -->
## DatasetOnboarder.freeze

### Purpose

Approve a new immutable adapter only with complete scientific review.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def freeze( self, registry_dir: str | Path, *, dataset_name: str, version: str = "1", overwrite: bool = False, reviewer: str = "", rationale: str = "", full_validation: Any = None, reviewed_mappings: Any = None, owner: str = "", source_institution: str = "", dataset_grain: str = "", data_classification: str = "", ) -> Path
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `registry_dir` | `registry_dir: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `dataset_name` | `dataset_name: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `version` | `version: str = '1'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `overwrite` | `overwrite: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `reviewer` | `reviewer: str = ''` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `rationale` | `rationale: str = ''` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `full_validation` | `full_validation: Any = None` | No | Identifier or identifier column. Confirm uniqueness/grouping semantics before analysis. |
| `reviewed_mappings` | `reviewed_mappings: Any = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `owner` | `owner: str = ''` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `source_institution` | `source_institution: str = ''` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `dataset_grain` | `dataset_grain: str = ''` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `data_classification` | `data_classification: str = ''` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `registry_dir`, `dataset_name`.

### Returns

`Path`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.onboard import DatasetOnboarder

# Construct DatasetOnboarder with its documented constructor first.
# instance = DatasetOnboarder(...)
result = instance.freeze(
    registry_dir="value",
    dataset_name="value"
)

print(result)
~~~

### Related functions

- `inspect_source`
- `infer_dataset_domains`
- `suggest_unit_mapping`
- `infer_code_vocabulary`
- `generate_adapter_bundle`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/onboard.py#L378`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L378)
- Repository search: [DatasetOnboarder.freeze](https://github.com/appsplorer/thomaslab-core/search?q=DatasetOnboarder.freeze&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Approve a new immutable adapter only with complete scientific review.

### API inspection

~~~python
import inspect
from thomaslab.onboard import DatasetOnboarder

print(inspect.signature(DatasetOnboarder.freeze))
print(DatasetOnboarder.freeze.__doc__)
~~~

### Source

[`src/thomaslab/onboard.py#L378`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/onboard.py#L378)

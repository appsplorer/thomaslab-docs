# thomaslab.data

Data ingestion, cohort construction, and clinical feature utilities.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 19

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.data.load_schema_config -->
## load_schema_config

### Purpose

Load and validate a schema-adapter configuration.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def load_schema_config(mapping: str | Path | Mapping[str, Any] | None) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `mapping` | `mapping: str \| Path \| Mapping[str, Any] \| None` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `mapping`.

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
from thomaslab.data import load_schema_config

result = load_schema_config(
    mapping={}
)

print(result)
~~~

### Related functions

- `infer_schema_mapping`
- `validate_canonical_schema`
- `standardize_schema`
- `generate_schema_template`
- `connect_db`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/data.py#L550`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L550)
- Repository search: [load_schema_config](https://github.com/appsplorer/thomaslab-core/search?q=load_schema_config&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Load and validate a schema-adapter configuration.

A configuration may be a YAML path, {"columns": {canonical: source}} mapping,
or a direct {canonical: source} mapping. Explicit mappings always take
precedence over automatic matching.

### API inspection

~~~python
import inspect
from thomaslab.data import load_schema_config

print(inspect.signature(load_schema_config))
print(load_schema_config.__doc__)
~~~

### Source

[`src/thomaslab/data.py#L550`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L550)

---

<!-- callable:thomaslab.data.infer_schema_mapping -->
## infer_schema_mapping

### Purpose

Infer source-to-canonical mappings without silently resolving ambiguous matches.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def infer_schema_mapping( source_columns: Iterable[object], *, canonical_schema: Mapping[str, Sequence[str]] | None = None, fuzzy_cutoff: float = 0.88, ambiguity_margin: float = 0.05, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `source_columns` | `source_columns: Iterable[object]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `canonical_schema` | `canonical_schema: Mapping[str, Sequence[str]] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `fuzzy_cutoff` | `fuzzy_cutoff: float = 0.88` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |
| `ambiguity_margin` | `ambiguity_margin: float = 0.05` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `source_columns`.

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
from thomaslab.data import infer_schema_mapping

result = infer_schema_mapping(
    source_columns=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `load_schema_config`
- `validate_canonical_schema`
- `standardize_schema`
- `generate_schema_template`
- `connect_db`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/data.py#L604`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L604)
- Repository search: [infer_schema_mapping](https://github.com/appsplorer/thomaslab-core/search?q=infer_schema_mapping&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Infer source-to-canonical mappings without silently resolving ambiguous matches.

Matching proceeds in descending trust order: canonical name, exact synonym,
regex pattern, then fuzzy similarity. If multiple exact/regex candidates exist,
or the best fuzzy match is too close to the runner-up, the target is marked
"ambiguous" rather than guessed.

### API inspection

~~~python
import inspect
from thomaslab.data import infer_schema_mapping

print(inspect.signature(infer_schema_mapping))
print(infer_schema_mapping.__doc__)
~~~

### Source

[`src/thomaslab/data.py#L604`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L604)

---

<!-- callable:thomaslab.data.validate_canonical_schema -->
## validate_canonical_schema

### Purpose

Validate that a table exposes the requested canonical columns.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_canonical_schema( data: Any, required_columns: Iterable[str] | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `data` | `data: Any` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `required_columns` | `required_columns: Iterable[str] \| None = None` | No | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |

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

from thomaslab.data import validate_canonical_schema

result = validate_canonical_schema(
    data=sample_df
)

print(result)
~~~

### Related functions

- `load_schema_config`
- `infer_schema_mapping`
- `standardize_schema`
- `generate_schema_template`
- `connect_db`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/data.py#L766`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L766)
- Repository search: [validate_canonical_schema](https://github.com/appsplorer/thomaslab-core/search?q=validate_canonical_schema&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate that a table exposes the requested canonical columns.

### API inspection

~~~python
import inspect
from thomaslab.data import validate_canonical_schema

print(inspect.signature(validate_canonical_schema))
print(validate_canonical_schema.__doc__)
~~~

### Source

[`src/thomaslab/data.py#L766`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L766)

---

<!-- callable:thomaslab.data.standardize_schema -->
## standardize_schema

### Purpose

Standardize unfamiliar source columns to the thomaslab canonical schema.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def standardize_schema( data: Any, mapping: str | Path | Mapping[str, Any] | None = None, auto_fuzzy: bool = True, *, required_columns: Iterable[str] | None = None, fuzzy_cutoff: float = 0.88, ambiguity_margin: float = 0.05, strict: bool = True, return_report: bool = False, ) -> Any
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `data` | `data: Any` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `mapping` | `mapping: str \| Path \| Mapping[str, Any] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `auto_fuzzy` | `auto_fuzzy: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `required_columns` | `required_columns: Iterable[str] \| None = None` | No | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `fuzzy_cutoff` | `fuzzy_cutoff: float = 0.88` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |
| `ambiguity_margin` | `ambiguity_margin: float = 0.05` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strict` | `strict: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `return_report` | `return_report: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `data`.

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

from thomaslab.data import standardize_schema

result = standardize_schema(
    data=sample_df
)

print(result)
~~~

### Related functions

- `load_schema_config`
- `infer_schema_mapping`
- `validate_canonical_schema`
- `generate_schema_template`
- `connect_db`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/data.py#L820`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L820)
- Repository search: [standardize_schema](https://github.com/appsplorer/thomaslab-core/search?q=standardize_schema&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Standardize unfamiliar source columns to the thomaslab canonical schema.

Explicit YAML/dictionary mappings are applied first. Remaining columns may be
resolved by exact aliases, regex rules, then conservative fuzzy matching.
Ambiguous matches are never renamed automatically.

### API inspection

~~~python
import inspect
from thomaslab.data import standardize_schema

print(inspect.signature(standardize_schema))
print(standardize_schema.__doc__)
~~~

### Source

[`src/thomaslab/data.py#L820`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L820)

---

<!-- callable:thomaslab.data.generate_schema_template -->
## generate_schema_template

### Purpose

Generate reviewable YAML without replacing earlier reviewed files.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def generate_schema_template( source_columns: Iterable[object], output_path: str | Path | None = None, *, dataset_name: str = "new_dataset", required_columns: Iterable[str] | None = None, fuzzy_cutoff: float = 0.88, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `source_columns` | `source_columns: Iterable[object]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `output_path` | `output_path: str \| Path \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `dataset_name` | `dataset_name: str = 'new_dataset'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `required_columns` | `required_columns: Iterable[str] \| None = None` | No | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `fuzzy_cutoff` | `fuzzy_cutoff: float = 0.88` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `source_columns`.

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
from thomaslab.data import generate_schema_template

result = generate_schema_template(
    source_columns=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `load_schema_config`
- `infer_schema_mapping`
- `validate_canonical_schema`
- `standardize_schema`
- `connect_db`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/data.py#L948`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L948)
- Repository search: [generate_schema_template](https://github.com/appsplorer/thomaslab-core/search?q=generate_schema_template&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Generate reviewable YAML without replacing earlier reviewed files.

A fresh versioned filename is required for another mapping revision.
Exclusive creation also prevents concurrent writers from truncating data.

### API inspection

~~~python
import inspect
from thomaslab.data import generate_schema_template

print(inspect.signature(generate_schema_template))
print(generate_schema_template.__doc__)
~~~

### Source

[`src/thomaslab/data.py#L948`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L948)

---

<!-- callable:thomaslab.data.connect_db -->
## connect_db

### Purpose

Create a SQLAlchemy engine from JSON or YAML configuration.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def connect_db(config_path: str) -> Any
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `config_path` | `config_path: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `config_path`.

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
from thomaslab.data import connect_db

result = connect_db(
    config_path="path/to/input.csv"
)

print(result)
~~~

### Related functions

- `load_schema_config`
- `infer_schema_mapping`
- `validate_canonical_schema`
- `standardize_schema`
- `generate_schema_template`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/data.py#L986`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L986)
- Repository search: [connect_db](https://github.com/appsplorer/thomaslab-core/search?q=connect_db&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create a SQLAlchemy engine from JSON or YAML configuration.

Parameters
----------
config_path:
    Path to a JSON/YAML file. Supported forms are either ``{"url": "..."}`` or
    components such as ``driver``, ``username``, ``password``, ``host``, ``port``,
    and ``database``. ``driver='duckdb'`` creates ``duckdb:///...``.

Returns
-------
sqlalchemy.engine.Engine
    Connection engine. Credentials are never logged by this function.

### API inspection

~~~python
import inspect
from thomaslab.data import connect_db

print(inspect.signature(connect_db))
print(connect_db.__doc__)
~~~

### Source

[`src/thomaslab/data.py#L986`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L986)

---

<!-- callable:thomaslab.data.clean_demographics -->
## clean_demographics

### Purpose

Normalize common demographic fields while preserving raw source values.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def clean_demographics(df: pd.DataFrame) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.

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

from thomaslab.data import clean_demographics

result = clean_demographics(
    df=sample_df
)

print(result)
~~~

### Related functions

- `load_schema_config`
- `infer_schema_mapping`
- `validate_canonical_schema`
- `standardize_schema`
- `generate_schema_template`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/data.py#L1041`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1041)
- Repository search: [clean_demographics](https://github.com/appsplorer/thomaslab-core/search?q=clean_demographics&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Normalize common demographic fields while preserving raw source values.

### API inspection

~~~python
import inspect
from thomaslab.data import clean_demographics

print(inspect.signature(clean_demographics))
print(clean_demographics.__doc__)
~~~

### Source

[`src/thomaslab/data.py#L1041`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1041)

---

<!-- callable:thomaslab.data.filter_cohort -->
## filter_cohort

### Purpose

Build a first-exposure cohort around a drug index date.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def filter_cohort( df: pd.DataFrame, drug_code: str, min_age: int = 18, start_date: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `drug_code` | `drug_code: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `min_age` | `min_age: int = 18` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `start_date` | `start_date: str \| None = None` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `drug_code`.

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

from thomaslab.data import filter_cohort

result = filter_cohort(
    df=sample_df,
    drug_code="value"
)

print(result)
~~~

### Related functions

- `load_schema_config`
- `infer_schema_mapping`
- `validate_canonical_schema`
- `standardize_schema`
- `generate_schema_template`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/data.py#L1062`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1062)
- Repository search: [filter_cohort](https://github.com/appsplorer/thomaslab-core/search?q=filter_cohort&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build a first-exposure cohort around a drug index date.

The input must contain ``patient_id``, ``age``, ``drug_code``, and either
``event_date`` or ``index_date``. The first qualifying exposure per patient is
used as time zero.

### API inspection

~~~python
import inspect
from thomaslab.data import filter_cohort

print(inspect.signature(filter_cohort))
print(filter_cohort.__doc__)
~~~

### Source

[`src/thomaslab/data.py#L1062`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1062)

---

<!-- callable:thomaslab.data.map_omop_codes -->
## map_omop_codes

### Purpose

Map source codes to OMOP standard concept IDs using an explicit vocabulary table.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def map_omop_codes( df: pd.DataFrame, source_col: str, vocabulary: str, concept_mapping: pd.DataFrame | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `source_col` | `source_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `vocabulary` | `vocabulary: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `concept_mapping` | `concept_mapping: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `source_col`, `vocabulary`.
- Referenced columns must exist in the input table: `source_col`.

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

from thomaslab.data import map_omop_codes

result = map_omop_codes(
    df=sample_df,
    source_col='source',
    vocabulary="value"
)

print(result)
~~~

### Related functions

- `load_schema_config`
- `infer_schema_mapping`
- `validate_canonical_schema`
- `standardize_schema`
- `generate_schema_template`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/data.py#L1092`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1092)
- Repository search: [map_omop_codes](https://github.com/appsplorer/thomaslab-core/search?q=map_omop_codes&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Map source codes to OMOP standard concept IDs using an explicit vocabulary table.

``concept_mapping`` must contain ``source_code``, ``vocabulary_id``, and
``concept_id``; an optional ``concept_name`` is preserved. No concept IDs are
guessed when a mapping is unavailable.

### API inspection

~~~python
import inspect
from thomaslab.data import map_omop_codes

print(inspect.signature(map_omop_codes))
print(map_omop_codes.__doc__)
~~~

### Source

[`src/thomaslab/data.py#L1092`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1092)

---

<!-- callable:thomaslab.data.compute_charlson_index -->
## compute_charlson_index

### Purpose

Calculate diagnosis-based Charlson Comorbidity Index by patient.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def compute_charlson_index( df: pd.DataFrame, icd10_col: str, patient_id_col: str, ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `icd10_col` | `icd10_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `patient_id_col` | `patient_id_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `icd10_col`, `patient_id_col`.
- Referenced columns must exist in the input table: `icd10_col`, `patient_id_col`.

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

from thomaslab.data import compute_charlson_index

result = compute_charlson_index(
    df=sample_df,
    icd10_col='icd10',
    patient_id_col='patient_id'
)

print(result)
~~~

### Related functions

- `load_schema_config`
- `infer_schema_mapping`
- `validate_canonical_schema`
- `standardize_schema`
- `generate_schema_template`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/data.py#L1133`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1133)
- Repository search: [compute_charlson_index](https://github.com/appsplorer/thomaslab-core/search?q=compute_charlson_index&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate diagnosis-based Charlson Comorbidity Index by patient.

Notes
-----
This implements a Quan-style ICD-10 prefix mapping. It does not add age points.
Diabetes with complications supersedes uncomplicated diabetes; moderate/severe
liver disease supersedes mild liver disease; metastatic disease supersedes
non-metastatic malignancy.

### API inspection

~~~python
import inspect
from thomaslab.data import compute_charlson_index

print(inspect.signature(compute_charlson_index))
print(compute_charlson_index.__doc__)
~~~

### Source

[`src/thomaslab/data.py#L1133`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1133)

---

<!-- callable:thomaslab.data.aggregate_lab_features -->
## aggregate_lab_features

### Purpose

Aggregate baseline laboratory measurements in ``[index-window, index]``.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def aggregate_lab_features( df: pd.DataFrame, patient_id_col: str, lab_col: str, value_col: str, date_col: str, index_date_col: str, window_days: int = 30, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_id_col` | `patient_id_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `lab_col` | `lab_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `value_col` | `value_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `window_days` | `window_days: int = 30` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `patient_id_col`, `lab_col`, `value_col`, `date_col`, `index_date_col`.
- Referenced columns must exist in the input table: `patient_id_col`, `lab_col`, `value_col`, `date_col`, `index_date_col`.

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

from thomaslab.data import aggregate_lab_features

result = aggregate_lab_features(
    df=sample_df,
    patient_id_col='patient_id',
    lab_col='lab',
    value_col='value',
    date_col='event_date',
    index_date_col='index_date'
)

print(result)
~~~

### Related functions

- `load_schema_config`
- `infer_schema_mapping`
- `validate_canonical_schema`
- `standardize_schema`
- `generate_schema_template`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/data.py#L1179`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1179)
- Repository search: [aggregate_lab_features](https://github.com/appsplorer/thomaslab-core/search?q=aggregate_lab_features&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Aggregate baseline laboratory measurements in ``[index-window, index]``.

### API inspection

~~~python
import inspect
from thomaslab.data import aggregate_lab_features

print(inspect.signature(aggregate_lab_features))
print(aggregate_lab_features.__doc__)
~~~

### Source

[`src/thomaslab/data.py#L1179`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1179)

---

<!-- callable:thomaslab.data.calculate_ckd_epi_2021 -->
## calculate_ckd_epi_2021

### Purpose

Calculate race-free 2021 CKD-EPI creatinine eGFR.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_ckd_epi_2021(scr: float, age: int, sex: str) -> float
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `scr` | `scr: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `age` | `age: int` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `sex` | `sex: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `scr`, `age`, `sex`.

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
from thomaslab.data import calculate_ckd_epi_2021

result = calculate_ckd_epi_2021(
    scr=0.5,
    age=2,
    sex="value"
)

print(result)
~~~

### Related functions

- `load_schema_config`
- `infer_schema_mapping`
- `validate_canonical_schema`
- `standardize_schema`
- `generate_schema_template`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/data.py#L1207`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1207)
- Repository search: [calculate_ckd_epi_2021](https://github.com/appsplorer/thomaslab-core/search?q=calculate_ckd_epi_2021&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate race-free 2021 CKD-EPI creatinine eGFR.

Parameters
----------
scr:
    Serum creatinine in mg/dL.
age:
    Age in years.
sex:
    ``'female'`` or ``'male'`` (case-insensitive).

### API inspection

~~~python
import inspect
from thomaslab.data import calculate_ckd_epi_2021

print(inspect.signature(calculate_ckd_epi_2021))
print(calculate_ckd_epi_2021.__doc__)
~~~

### Source

[`src/thomaslab/data.py#L1207`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1207)

---

<!-- callable:thomaslab.data.flag_drug_interactions -->
## flag_drug_interactions

### Purpose

Flag rows containing an interacting medication when the target drug is present.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def flag_drug_interactions( df: pd.DataFrame, med_col: str, target_drug: str, interacting_drugs: list[str], ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `med_col` | `med_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `target_drug` | `target_drug: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `interacting_drugs` | `interacting_drugs: list[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `med_col`, `target_drug`, `interacting_drugs`.
- Referenced columns must exist in the input table: `med_col`.

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

from thomaslab.data import flag_drug_interactions

result = flag_drug_interactions(
    df=sample_df,
    med_col='med',
    target_drug="value",
    interacting_drugs=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `load_schema_config`
- `infer_schema_mapping`
- `validate_canonical_schema`
- `standardize_schema`
- `generate_schema_template`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/data.py#L1240`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1240)
- Repository search: [flag_drug_interactions](https://github.com/appsplorer/thomaslab-core/search?q=flag_drug_interactions&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Flag rows containing an interacting medication when the target drug is present.

Medication strings may contain delimiters such as commas, semicolons, pipes, or spaces.
Matching is case-insensitive and token-aware for simple generic/brand names.

### API inspection

~~~python
import inspect
from thomaslab.data import flag_drug_interactions

print(inspect.signature(flag_drug_interactions))
print(flag_drug_interactions.__doc__)
~~~

### Source

[`src/thomaslab/data.py#L1240`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1240)

---

<!-- callable:thomaslab.data.connect_duckdb_parquet -->
## connect_duckdb_parquet

### Purpose

Create an in-memory DuckDB connection over one or more Parquet files.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def connect_duckdb_parquet( parquet_dir_path: str, view_name: str = "ehr_parquet", hive_partitioning: bool = True, ) -> Any
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `parquet_dir_path` | `parquet_dir_path: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `view_name` | `view_name: str = 'ehr_parquet'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `hive_partitioning` | `hive_partitioning: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `parquet_dir_path`.

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
from thomaslab.data import connect_duckdb_parquet

result = connect_duckdb_parquet(
    parquet_dir_path="path/to/input.csv"
)

print(result)
~~~

### Related functions

- `load_schema_config`
- `infer_schema_mapping`
- `validate_canonical_schema`
- `standardize_schema`
- `generate_schema_template`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/data.py#L1266`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1266)
- Repository search: [connect_duckdb_parquet](https://github.com/appsplorer/thomaslab-core/search?q=connect_duckdb_parquet&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create an in-memory DuckDB connection over one or more Parquet files.

Parameters
----------
parquet_dir_path:
    Path to a Parquet file, a directory containing Parquet files, or a DuckDB
    glob expression. Directories are scanned recursively with ``**/*.parquet``.
view_name:
    Name of the read-only DuckDB view that exposes the Parquet dataset.
hive_partitioning:
    Whether DuckDB should decode Hive-style ``key=value`` directory partitions.

Returns
-------
duckdb.DuckDBPyConnection
    An open in-memory connection containing ``view_name``.

Notes
-----
The Parquet data are not copied into DuckDB. Queries are pushed down to the
files and can therefore operate out of core.

### API inspection

~~~python
import inspect
from thomaslab.data import connect_duckdb_parquet

print(inspect.signature(connect_duckdb_parquet))
print(connect_duckdb_parquet.__doc__)
~~~

### Source

[`src/thomaslab/data.py#L1266`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1266)

---

<!-- callable:thomaslab.data.convert_schema_to_omop -->
## convert_schema_to_omop

### Purpose

Convert a single source table to an OMOP-CDM-shaped table.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def convert_schema_to_omop( df: pd.DataFrame, source_schema: str = "MIMIC-IV", source_table: str | None = None, concept_mapping: pd.DataFrame | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `source_schema` | `source_schema: str = 'MIMIC-IV'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `source_table` | `source_table: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `concept_mapping` | `concept_mapping: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.

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

from thomaslab.data import convert_schema_to_omop

result = convert_schema_to_omop(
    df=sample_df
)

print(result)
~~~

### Related functions

- `load_schema_config`
- `infer_schema_mapping`
- `validate_canonical_schema`
- `standardize_schema`
- `generate_schema_template`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/data.py#L1357`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1357)
- Repository search: [convert_schema_to_omop](https://github.com/appsplorer/thomaslab-core/search?q=convert_schema_to_omop&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Convert a single source table to an OMOP-CDM-shaped table.

This is a structural adapter, not a full vocabulary ETL. Standard OMOP
``concept_id`` fields remain ``0`` unless an explicit source-to-standard mapping
is supplied. The target table is inferred from common source columns when safe;
ambiguous tables require ``source_table``.

Supported structural adapters are MIMIC-IV, PCORnet, and TriNetX-like exports.
The returned DataFrame stores the selected OMOP target table in
``result.attrs['omop_target_table']``.

### API inspection

~~~python
import inspect
from thomaslab.data import convert_schema_to_omop

print(inspect.signature(convert_schema_to_omop))
print(convert_schema_to_omop.__doc__)
~~~

### Source

[`src/thomaslab/data.py#L1357`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1357)

---

<!-- callable:thomaslab.data.extract_longitudinal_features_polars -->
## extract_longitudinal_features_polars

### Purpose

Compute Polars-accelerated longitudinal lab summaries across lookback windows.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def extract_longitudinal_features_polars( df: Any, patient_id_col: str, lab_col: str, window_days_list: list[int] | tuple[int, ...] = (7, 30, 90, 365), *, value_col: str = "value", date_col: str = "date", index_date_col: str = "index_date", ) -> Any
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: Any` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_id_col` | `patient_id_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `lab_col` | `lab_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `window_days_list` | `window_days_list: list[int] \| tuple[int, ...] = (7, 30, 90, 365)` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `value_col` | `value_col: str = 'value'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str = 'date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `patient_id_col`, `lab_col`.
- Referenced columns must exist in the input table: `patient_id_col`, `lab_col`, `value_col`, `date_col`, `index_date_col`.

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

from thomaslab.data import extract_longitudinal_features_polars

result = extract_longitudinal_features_polars(
    df=sample_df,
    patient_id_col='patient_id',
    lab_col='lab'
)

print(result)
~~~

### Related functions

- `load_schema_config`
- `infer_schema_mapping`
- `validate_canonical_schema`
- `standardize_schema`
- `generate_schema_template`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/data.py#L1605`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1605)
- Repository search: [extract_longitudinal_features_polars](https://github.com/appsplorer/thomaslab-core/search?q=extract_longitudinal_features_polars&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compute Polars-accelerated longitudinal lab summaries across lookback windows.

Returns a long-form Polars DataFrame with one row per patient/lab/window and
``mean``, ``min``, ``max``, ``count``, and least-squares ``slope_per_day``.
Baseline measurements are restricted to dates on or before ``index_date``.

### API inspection

~~~python
import inspect
from thomaslab.data import extract_longitudinal_features_polars

print(inspect.signature(extract_longitudinal_features_polars))
print(extract_longitudinal_features_polars.__doc__)
~~~

### Source

[`src/thomaslab/data.py#L1605`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1605)

---

<!-- callable:thomaslab.data.build_episodes_of_care -->
## build_episodes_of_care

### Purpose

Merge overlapping/nearby visits into continuous episodes of care.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_episodes_of_care( df: pd.DataFrame, patient_id_col: str, visit_start_col: str, visit_end_col: str, max_gap_days: int = 30, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_id_col` | `patient_id_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `visit_start_col` | `visit_start_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `visit_end_col` | `visit_end_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `max_gap_days` | `max_gap_days: int = 30` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `patient_id_col`, `visit_start_col`, `visit_end_col`.
- Referenced columns must exist in the input table: `patient_id_col`, `visit_start_col`, `visit_end_col`.

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

from thomaslab.data import build_episodes_of_care

result = build_episodes_of_care(
    df=sample_df,
    patient_id_col='patient_id',
    visit_start_col='visit_start',
    visit_end_col='visit_end'
)

print(result)
~~~

### Related functions

- `load_schema_config`
- `infer_schema_mapping`
- `validate_canonical_schema`
- `standardize_schema`
- `generate_schema_template`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/data.py#L1683`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1683)
- Repository search: [build_episodes_of_care](https://github.com/appsplorer/thomaslab-core/search?q=build_episodes_of_care&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Merge overlapping/nearby visits into continuous episodes of care.

### API inspection

~~~python
import inspect
from thomaslab.data import build_episodes_of_care

print(inspect.signature(build_episodes_of_care))
print(build_episodes_of_care.__doc__)
~~~

### Source

[`src/thomaslab/data.py#L1683`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1683)

---

<!-- callable:thomaslab.data.impute_missing_clinical_data_fast -->
## impute_missing_clinical_data_fast

### Purpose

Impute missing numeric clinical features with deterministic fast strategies.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def impute_missing_clinical_data_fast( df: Any, strategy: str = "mice_polars", *, exclude_cols: list[str] | None = None, random_state: int = 42, max_iter: int = 10, ) -> Any
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: Any` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `strategy` | `strategy: str = 'mice_polars'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `exclude_cols` | `exclude_cols: list[str] \| None = None` | No | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |
| `max_iter` | `max_iter: int = 10` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.

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

from thomaslab.data import impute_missing_clinical_data_fast

result = impute_missing_clinical_data_fast(
    df=sample_df
)

print(result)
~~~

### Related functions

- `load_schema_config`
- `infer_schema_mapping`
- `validate_canonical_schema`
- `standardize_schema`
- `generate_schema_template`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/data.py#L1755`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1755)
- Repository search: [impute_missing_clinical_data_fast](https://github.com/appsplorer/thomaslab-core/search?q=impute_missing_clinical_data_fast&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Impute missing numeric clinical features with deterministic fast strategies.

``mice_polars`` uses scikit-learn's MICE-style ``IterativeImputer`` on the
numeric matrix and converts back to Polars when the input is Polars. This avoids
falsely labeling a simple mean-fill as MICE while preserving a Polars-friendly API.
Non-numeric columns are preserved unchanged.

### API inspection

~~~python
import inspect
from thomaslab.data import impute_missing_clinical_data_fast

print(inspect.signature(impute_missing_clinical_data_fast))
print(impute_missing_clinical_data_fast.__doc__)
~~~

### Source

[`src/thomaslab/data.py#L1755`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1755)

---

<!-- callable:thomaslab.data.extract_drug_exposure_episodes -->
## extract_drug_exposure_episodes

### Purpose

Construct medication persistence episodes and medication possession ratios.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def extract_drug_exposure_episodes( df: pd.DataFrame, drug_col: str, dose_col: str, max_refill_gap: int = 14, *, patient_id_col: str = "patient_id", date_col: str = "start_date", days_supply_col: str = "days_supply", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `drug_col` | `drug_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `dose_col` | `dose_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `max_refill_gap` | `max_refill_gap: int = 14` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `patient_id_col` | `patient_id_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str = 'start_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `days_supply_col` | `days_supply_col: str = 'days_supply'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `drug_col`, `dose_col`.
- Referenced columns must exist in the input table: `drug_col`, `dose_col`, `patient_id_col`, `date_col`, `days_supply_col`.

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

from thomaslab.data import extract_drug_exposure_episodes

result = extract_drug_exposure_episodes(
    df=sample_df,
    drug_col='drug',
    dose_col='dose'
)

print(result)
~~~

### Related functions

- `load_schema_config`
- `infer_schema_mapping`
- `validate_canonical_schema`
- `standardize_schema`
- `generate_schema_template`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/data.py#L1816`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1816)
- Repository search: [extract_drug_exposure_episodes](https://github.com/appsplorer/thomaslab-core/search?q=extract_drug_exposure_episodes&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Construct medication persistence episodes and medication possession ratios.

A new episode begins when the next fill starts more than ``max_refill_gap`` days
after the previous coverage end. MPR is based on observed days supplied; dose
is reported descriptively and is not used as a substitute for days supplied.

### API inspection

~~~python
import inspect
from thomaslab.data import extract_drug_exposure_episodes

print(inspect.signature(extract_drug_exposure_episodes))
print(extract_drug_exposure_episodes.__doc__)
~~~

### Source

[`src/thomaslab/data.py#L1816`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/data.py#L1816)

# thomaslab.cleaning

Auditable cleaning utilities for heterogeneous EHR and drug datasets.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 18

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.cleaning.profile_dataset -->
## profile_dataset

### Purpose

Return an auditable structural profile without modifying the input table.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def profile_dataset(df: pd.DataFrame, *, max_examples: int = 3) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `max_examples` | `max_examples: int = 3` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.

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

from thomaslab.cleaning import profile_dataset

result = profile_dataset(
    df=sample_df
)

print(result)
~~~

### Related functions

- `infer_column_semantics`
- `normalize_missing_tokens`
- `standardize_dates`
- `standardize_units`
- `detect_unit_conflicts`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cleaning.py#L33`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L33)
- Repository search: [profile_dataset](https://github.com/appsplorer/thomaslab-core/search?q=profile_dataset&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return an auditable structural profile without modifying the input table.

### API inspection

~~~python
import inspect
from thomaslab.cleaning import profile_dataset

print(inspect.signature(profile_dataset))
print(profile_dataset.__doc__)
~~~

### Source

[`src/thomaslab/cleaning.py#L33`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L33)

---

<!-- callable:thomaslab.cleaning.infer_column_semantics -->
## infer_column_semantics

### Purpose

Infer coarse source-column semantics from names, dtype, and sampled values.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def infer_column_semantics(df: pd.DataFrame, *, sample_size: int = 500) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `sample_size` | `sample_size: int = 500` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

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

from thomaslab.cleaning import infer_column_semantics

result = infer_column_semantics(
    df=sample_df
)

print(result)
~~~

### Related functions

- `profile_dataset`
- `normalize_missing_tokens`
- `standardize_dates`
- `standardize_units`
- `detect_unit_conflicts`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cleaning.py#L63`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L63)
- Repository search: [infer_column_semantics](https://github.com/appsplorer/thomaslab-core/search?q=infer_column_semantics&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Infer coarse source-column semantics from names, dtype, and sampled values.

### API inspection

~~~python
import inspect
from thomaslab.cleaning import infer_column_semantics

print(inspect.signature(infer_column_semantics))
print(infer_column_semantics.__doc__)
~~~

### Source

[`src/thomaslab/cleaning.py#L63`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L63)

---

<!-- callable:thomaslab.cleaning.normalize_missing_tokens -->
## normalize_missing_tokens

### Purpose

Replace configured textual missing-value sentinels with ``pd.NA``.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def normalize_missing_tokens( df: pd.DataFrame, *, tokens: Iterable[str] | None = None, per_column: Mapping[str, Iterable[str]] | None = None, return_report: bool = False, ) -> pd.DataFrame | tuple[pd.DataFrame, pd.DataFrame]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `tokens` | `tokens: Iterable[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `per_column` | `per_column: Mapping[str, Iterable[str]] \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `return_report` | `return_report: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.
- Referenced columns must exist in the input table: `per_column`.

### Returns

`pd.DataFrame | tuple[pd.DataFrame, pd.DataFrame]`

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

from thomaslab.cleaning import normalize_missing_tokens

result = normalize_missing_tokens(
    df=sample_df
)

print(result)
~~~

### Related functions

- `profile_dataset`
- `infer_column_semantics`
- `standardize_dates`
- `standardize_units`
- `detect_unit_conflicts`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cleaning.py#L125`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L125)
- Repository search: [normalize_missing_tokens](https://github.com/appsplorer/thomaslab-core/search?q=normalize_missing_tokens&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Replace configured textual missing-value sentinels with ``pd.NA``.

### API inspection

~~~python
import inspect
from thomaslab.cleaning import normalize_missing_tokens

print(inspect.signature(normalize_missing_tokens))
print(normalize_missing_tokens.__doc__)
~~~

### Source

[`src/thomaslab/cleaning.py#L125`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L125)

---

<!-- callable:thomaslab.cleaning.standardize_dates -->
## standardize_dates

### Purpose

Parse configured date/time columns and report non-missing values that fail parsing.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def standardize_dates( df: pd.DataFrame, columns: Sequence[str] | None = None, *, utc: bool = False, return_report: bool = False, ) -> pd.DataFrame | tuple[pd.DataFrame, pd.DataFrame]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `columns` | `columns: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `utc` | `utc: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `return_report` | `return_report: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.

### Returns

`pd.DataFrame | tuple[pd.DataFrame, pd.DataFrame]`

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

from thomaslab.cleaning import standardize_dates

result = standardize_dates(
    df=sample_df
)

print(result)
~~~

### Related functions

- `profile_dataset`
- `infer_column_semantics`
- `normalize_missing_tokens`
- `standardize_units`
- `detect_unit_conflicts`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cleaning.py#L151`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L151)
- Repository search: [standardize_dates](https://github.com/appsplorer/thomaslab-core/search?q=standardize_dates&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Parse configured date/time columns and report non-missing values that fail parsing.

### API inspection

~~~python
import inspect
from thomaslab.cleaning import standardize_dates

print(inspect.signature(standardize_dates))
print(standardize_dates.__doc__)
~~~

### Source

[`src/thomaslab/cleaning.py#L151`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L151)

---

<!-- callable:thomaslab.cleaning.standardize_units -->
## standardize_units

### Purpose

Convert a numeric value column to one explicitly requested target unit.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def standardize_units( df: pd.DataFrame, value_col: str, unit_col: str, target_unit: str, *, analyte: str | None = None, conversions: Mapping[str, float] | None = None, strict: bool = True, return_report: bool = False, ) -> pd.DataFrame | tuple[pd.DataFrame, dict[str, Any]]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `value_col` | `value_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `unit_col` | `unit_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `target_unit` | `target_unit: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `analyte` | `analyte: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `conversions` | `conversions: Mapping[str, float] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strict` | `strict: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `return_report` | `return_report: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `value_col`, `unit_col`, `target_unit`.
- Referenced columns must exist in the input table: `value_col`, `unit_col`.

### Returns

`pd.DataFrame | tuple[pd.DataFrame, dict[str, Any]]`

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

from thomaslab.cleaning import standardize_units

result = standardize_units(
    df=sample_df,
    value_col='value',
    unit_col='unit',
    target_unit="value"
)

print(result)
~~~

### Related functions

- `profile_dataset`
- `infer_column_semantics`
- `normalize_missing_tokens`
- `standardize_dates`
- `detect_unit_conflicts`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cleaning.py#L221`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L221)
- Repository search: [standardize_units](https://github.com/appsplorer/thomaslab-core/search?q=standardize_units&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Convert a numeric value column to one explicitly requested target unit.

Built-ins intentionally require an explicit target. Molecular conversions such as
creatinine µmol/L↔mg/dL and glucose mmol/L↔mg/dL additionally require ``analyte``
because the conversion factor is analyte-specific. Caller-supplied ``conversions`` maps a
normalized source unit to a multiplicative factor into ``target_unit``.

### API inspection

~~~python
import inspect
from thomaslab.cleaning import standardize_units

print(inspect.signature(standardize_units))
print(standardize_units.__doc__)
~~~

### Source

[`src/thomaslab/cleaning.py#L221`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L221)

---

<!-- callable:thomaslab.cleaning.detect_unit_conflicts -->
## detect_unit_conflicts

### Purpose

Report measures observed with more than one non-empty unit.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_unit_conflicts(df: pd.DataFrame, measure_col: str, unit_col: str) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `measure_col` | `measure_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `unit_col` | `unit_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `measure_col`, `unit_col`.
- Referenced columns must exist in the input table: `measure_col`, `unit_col`.

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

from thomaslab.cleaning import detect_unit_conflicts

result = detect_unit_conflicts(
    df=sample_df,
    measure_col='measure',
    unit_col='unit'
)

print(result)
~~~

### Related functions

- `profile_dataset`
- `infer_column_semantics`
- `normalize_missing_tokens`
- `standardize_dates`
- `standardize_units`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cleaning.py#L278`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L278)
- Repository search: [detect_unit_conflicts](https://github.com/appsplorer/thomaslab-core/search?q=detect_unit_conflicts&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Report measures observed with more than one non-empty unit.

### API inspection

~~~python
import inspect
from thomaslab.cleaning import detect_unit_conflicts

print(inspect.signature(detect_unit_conflicts))
print(detect_unit_conflicts.__doc__)
~~~

### Source

[`src/thomaslab/cleaning.py#L278`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L278)

---

<!-- callable:thomaslab.cleaning.detect_impossible_values -->
## detect_impossible_values

### Purpose

Return long-form violations of caller-defined numeric plausibility ranges.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_impossible_values( df: pd.DataFrame, rules: Mapping[str, Mapping[str, float]] ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `rules` | `rules: Mapping[str, Mapping[str, float]]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `rules`.

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

from thomaslab.cleaning import detect_impossible_values

result = detect_impossible_values(
    df=sample_df,
    rules={}
)

print(result)
~~~

### Related functions

- `profile_dataset`
- `infer_column_semantics`
- `normalize_missing_tokens`
- `standardize_dates`
- `standardize_units`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cleaning.py#L299`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L299)
- Repository search: [detect_impossible_values](https://github.com/appsplorer/thomaslab-core/search?q=detect_impossible_values&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return long-form violations of caller-defined numeric plausibility ranges.

### API inspection

~~~python
import inspect
from thomaslab.cleaning import detect_impossible_values

print(inspect.signature(detect_impossible_values))
print(detect_impossible_values.__doc__)
~~~

### Source

[`src/thomaslab/cleaning.py#L299`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L299)

---

<!-- callable:thomaslab.cleaning.detect_outliers -->
## detect_outliers

### Purpose

Return long-form statistical outlier flags using MAD or IQR.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_outliers( df: pd.DataFrame, columns: Sequence[str] | None = None, *, method: str = "mad", threshold: float = 3.5, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `columns` | `columns: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `method` | `method: str = 'mad'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `threshold` | `threshold: float = 3.5` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |

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

from thomaslab.cleaning import detect_outliers

result = detect_outliers(
    df=sample_df
)

print(result)
~~~

### Related functions

- `profile_dataset`
- `infer_column_semantics`
- `normalize_missing_tokens`
- `standardize_dates`
- `standardize_units`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cleaning.py#L322`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L322)
- Repository search: [detect_outliers](https://github.com/appsplorer/thomaslab-core/search?q=detect_outliers&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return long-form statistical outlier flags using MAD or IQR.

### API inspection

~~~python
import inspect
from thomaslab.cleaning import detect_outliers

print(inspect.signature(detect_outliers))
print(detect_outliers.__doc__)
~~~

### Source

[`src/thomaslab/cleaning.py#L322`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L322)

---

<!-- callable:thomaslab.cleaning.normalize_icd_codes -->
## normalize_icd_codes

### Purpose

Normalize ICD-like strings without asserting the ICD version.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def normalize_icd_codes(series: pd.Series, *, preserve_decimal: bool = False) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `series` | `series: pd.Series` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `preserve_decimal` | `preserve_decimal: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `series`.

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

from thomaslab.cleaning import normalize_icd_codes

result = normalize_icd_codes(
    series=sample_series
)

print(result)
~~~

### Related functions

- `profile_dataset`
- `infer_column_semantics`
- `normalize_missing_tokens`
- `standardize_dates`
- `standardize_units`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cleaning.py#L363`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L363)
- Repository search: [normalize_icd_codes](https://github.com/appsplorer/thomaslab-core/search?q=normalize_icd_codes&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Normalize ICD-like strings without asserting the ICD version.

### API inspection

~~~python
import inspect
from thomaslab.cleaning import normalize_icd_codes

print(inspect.signature(normalize_icd_codes))
print(normalize_icd_codes.__doc__)
~~~

### Source

[`src/thomaslab/cleaning.py#L363`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L363)

---

<!-- callable:thomaslab.cleaning.normalize_ndc_codes -->
## normalize_ndc_codes

### Purpose

Normalize NDC strings conservatively.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def normalize_ndc_codes(series: pd.Series, *, output_digits: int = 11) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `series` | `series: pd.Series` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `output_digits` | `output_digits: int = 11` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `series`.

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

from thomaslab.cleaning import normalize_ndc_codes

result = normalize_ndc_codes(
    series=sample_series
)

print(result)
~~~

### Related functions

- `profile_dataset`
- `infer_column_semantics`
- `normalize_missing_tokens`
- `standardize_dates`
- `standardize_units`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cleaning.py#L372`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L372)
- Repository search: [normalize_ndc_codes](https://github.com/appsplorer/thomaslab-core/search?q=normalize_ndc_codes&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Normalize NDC strings conservatively.

Hyphenated 10-digit NDCs are expanded to 11 digits according to segment length.
Unhyphenated 10-digit strings are left unresolved because the segment format is
ambiguous. Already 11-digit numeric NDCs are retained.

### API inspection

~~~python
import inspect
from thomaslab.cleaning import normalize_ndc_codes

print(inspect.signature(normalize_ndc_codes))
print(normalize_ndc_codes.__doc__)
~~~

### Source

[`src/thomaslab/cleaning.py#L372`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L372)

---

<!-- callable:thomaslab.cleaning.deduplicate_records -->
## deduplicate_records

### Purpose

Remove exact duplicates over the selected key columns.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def deduplicate_records( df: pd.DataFrame, *, subset: Sequence[str] | None = None, keep: str | bool = "first", return_report: bool = False, ) -> pd.DataFrame | tuple[pd.DataFrame, dict[str, int]]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `subset` | `subset: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `keep` | `keep: str \| bool = 'first'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `return_report` | `return_report: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.

### Returns

`pd.DataFrame | tuple[pd.DataFrame, dict[str, int]]`

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

from thomaslab.cleaning import deduplicate_records

result = deduplicate_records(
    df=sample_df
)

print(result)
~~~

### Related functions

- `profile_dataset`
- `infer_column_semantics`
- `normalize_missing_tokens`
- `standardize_dates`
- `standardize_units`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cleaning.py#L403`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L403)
- Repository search: [deduplicate_records](https://github.com/appsplorer/thomaslab-core/search?q=deduplicate_records&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Remove exact duplicates over the selected key columns.

### API inspection

~~~python
import inspect
from thomaslab.cleaning import deduplicate_records

print(inspect.signature(deduplicate_records))
print(deduplicate_records.__doc__)
~~~

### Source

[`src/thomaslab/cleaning.py#L403`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L403)

---

<!-- callable:thomaslab.cleaning.resolve_temporal_duplicates -->
## resolve_temporal_duplicates

### Purpose

Collapse records sharing keys when timestamps occur within ``tolerance``.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def resolve_temporal_duplicates( df: pd.DataFrame, key_cols: Sequence[str], time_col: str, *, tolerance: str | pd.Timedelta = "5min", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `key_cols` | `key_cols: Sequence[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `tolerance` | `tolerance: str \| pd.Timedelta = '5min'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `key_cols`, `time_col`.
- Referenced columns must exist in the input table: `time_col`.

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

from thomaslab.cleaning import resolve_temporal_duplicates

result = resolve_temporal_duplicates(
    df=sample_df,
    key_cols=["feature_a", "feature_b"],
    time_col='event_date'
)

print(result)
~~~

### Related functions

- `profile_dataset`
- `infer_column_semantics`
- `normalize_missing_tokens`
- `standardize_dates`
- `standardize_units`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cleaning.py#L421`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L421)
- Repository search: [resolve_temporal_duplicates](https://github.com/appsplorer/thomaslab-core/search?q=resolve_temporal_duplicates&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Collapse records sharing keys when timestamps occur within ``tolerance``.

The earliest record is retained. This operation is intentionally explicit and
should only be used when near-duplicates are scientifically defensible.

### API inspection

~~~python
import inspect
from thomaslab.cleaning import resolve_temporal_duplicates

print(inspect.signature(resolve_temporal_duplicates))
print(resolve_temporal_duplicates.__doc__)
~~~

### Source

[`src/thomaslab/cleaning.py#L421`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L421)

---

<!-- callable:thomaslab.cleaning.clean_lab_table -->
## clean_lab_table

### Purpose

Clean a canonical lab/measurement table without inventing units.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def clean_lab_table( df: pd.DataFrame, *, value_col: str = "lab_value", unit_col: str = "lab_unit", date_col: str = "event_date", ) -> tuple[pd.DataFrame, dict[str, Any]]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `value_col` | `value_col: str = 'lab_value'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `unit_col` | `unit_col: str = 'lab_unit'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.
- Referenced columns must exist in the input table: `value_col`, `unit_col`, `date_col`.

### Returns

`tuple[pd.DataFrame, dict[str, Any]]`

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

from thomaslab.cleaning import clean_lab_table

result = clean_lab_table(
    df=sample_df
)

print(result)
~~~

### Related functions

- `profile_dataset`
- `infer_column_semantics`
- `normalize_missing_tokens`
- `standardize_dates`
- `standardize_units`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cleaning.py#L456`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L456)
- Repository search: [clean_lab_table](https://github.com/appsplorer/thomaslab-core/search?q=clean_lab_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Clean a canonical lab/measurement table without inventing units.

### API inspection

~~~python
import inspect
from thomaslab.cleaning import clean_lab_table

print(inspect.signature(clean_lab_table))
print(clean_lab_table.__doc__)
~~~

### Source

[`src/thomaslab/cleaning.py#L456`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L456)

---

<!-- callable:thomaslab.cleaning.clean_medication_table -->
## clean_medication_table

### Purpose

Clean a canonical medication table while preserving the original drug code.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def clean_medication_table( df: pd.DataFrame, *, code_col: str = "rx_code", date_col: str = "event_date", ) -> tuple[pd.DataFrame, dict[str, Any]]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `code_col` | `code_col: str = 'rx_code'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.
- Referenced columns must exist in the input table: `code_col`, `date_col`.

### Returns

`tuple[pd.DataFrame, dict[str, Any]]`

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

from thomaslab.cleaning import clean_medication_table

result = clean_medication_table(
    df=sample_df
)

print(result)
~~~

### Related functions

- `profile_dataset`
- `infer_column_semantics`
- `normalize_missing_tokens`
- `standardize_dates`
- `standardize_units`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cleaning.py#L489`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L489)
- Repository search: [clean_medication_table](https://github.com/appsplorer/thomaslab-core/search?q=clean_medication_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Clean a canonical medication table while preserving the original drug code.

### API inspection

~~~python
import inspect
from thomaslab.cleaning import clean_medication_table

print(inspect.signature(clean_medication_table))
print(clean_medication_table.__doc__)
~~~

### Source

[`src/thomaslab/cleaning.py#L489`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L489)

---

<!-- callable:thomaslab.cleaning.clean_diagnosis_table -->
## clean_diagnosis_table

### Purpose

Clean diagnosis codes and dates while preserving the raw source code.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def clean_diagnosis_table( df: pd.DataFrame, *, code_col: str = "icd_code", date_col: str = "event_date", ) -> tuple[pd.DataFrame, dict[str, Any]]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `code_col` | `code_col: str = 'icd_code'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.
- Referenced columns must exist in the input table: `code_col`, `date_col`.

### Returns

`tuple[pd.DataFrame, dict[str, Any]]`

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

from thomaslab.cleaning import clean_diagnosis_table

result = clean_diagnosis_table(
    df=sample_df
)

print(result)
~~~

### Related functions

- `profile_dataset`
- `infer_column_semantics`
- `normalize_missing_tokens`
- `standardize_dates`
- `standardize_units`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cleaning.py#L509`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L509)
- Repository search: [clean_diagnosis_table](https://github.com/appsplorer/thomaslab-core/search?q=clean_diagnosis_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Clean diagnosis codes and dates while preserving the raw source code.

### API inspection

~~~python
import inspect
from thomaslab.cleaning import clean_diagnosis_table

print(inspect.signature(clean_diagnosis_table))
print(clean_diagnosis_table.__doc__)
~~~

### Source

[`src/thomaslab/cleaning.py#L509`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L509)

---

<!-- callable:thomaslab.cleaning.clean_encounter_table -->
## clean_encounter_table

### Purpose

Clean encounter identifiers/dates and remove exact duplicate encounter rows.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def clean_encounter_table( df: pd.DataFrame, *, patient_col: str = "patient_id", encounter_col: str = "encounter_id", date_col: str = "event_date", ) -> tuple[pd.DataFrame, dict[str, Any]]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `encounter_col` | `encounter_col: str = 'encounter_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.
- Referenced columns must exist in the input table: `patient_col`, `encounter_col`, `date_col`.

### Returns

`tuple[pd.DataFrame, dict[str, Any]]`

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

from thomaslab.cleaning import clean_encounter_table

result = clean_encounter_table(
    df=sample_df
)

print(result)
~~~

### Related functions

- `profile_dataset`
- `infer_column_semantics`
- `normalize_missing_tokens`
- `standardize_dates`
- `standardize_units`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cleaning.py#L529`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L529)
- Repository search: [clean_encounter_table](https://github.com/appsplorer/thomaslab-core/search?q=clean_encounter_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Clean encounter identifiers/dates and remove exact duplicate encounter rows.

### API inspection

~~~python
import inspect
from thomaslab.cleaning import clean_encounter_table

print(inspect.signature(clean_encounter_table))
print(clean_encounter_table.__doc__)
~~~

### Source

[`src/thomaslab/cleaning.py#L529`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L529)

---

<!-- callable:thomaslab.cleaning.load_cleaning_config -->
## load_cleaning_config

### Purpose

Load a YAML/dictionary cleaning configuration.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def load_cleaning_config(config: str | Path | Mapping[str, Any] | None) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `config` | `config: str \| Path \| Mapping[str, Any] \| None` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `config`.

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
from thomaslab.cleaning import load_cleaning_config

result = load_cleaning_config(
    config={}
)

print(result)
~~~

### Related functions

- `profile_dataset`
- `infer_column_semantics`
- `normalize_missing_tokens`
- `standardize_dates`
- `standardize_units`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cleaning.py#L551`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L551)
- Repository search: [load_cleaning_config](https://github.com/appsplorer/thomaslab-core/search?q=load_cleaning_config&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Load a YAML/dictionary cleaning configuration.

### API inspection

~~~python
import inspect
from thomaslab.cleaning import load_cleaning_config

print(inspect.signature(load_cleaning_config))
print(load_cleaning_config.__doc__)
~~~

### Source

[`src/thomaslab/cleaning.py#L551`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L551)

---

<!-- callable:thomaslab.cleaning.clean_ehr_dataset -->
## clean_ehr_dataset

### Purpose

Run the guarded generic cleaning pipeline for an unfamiliar EHR table.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def clean_ehr_dataset( df: pd.DataFrame, *, schema: str | Path | Mapping[str, Any] | None = None, config: str | Path | Mapping[str, Any] | None = None, required_columns: Sequence[str] | None = None, strict_schema: bool = True, ) -> tuple[pd.DataFrame, dict[str, Any]]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `schema` | `schema: str \| Path \| Mapping[str, Any] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `config` | `config: str \| Path \| Mapping[str, Any] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `required_columns` | `required_columns: Sequence[str] \| None = None` | No | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `strict_schema` | `strict_schema: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.

### Returns

`tuple[pd.DataFrame, dict[str, Any]]`

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

from thomaslab.cleaning import clean_ehr_dataset

result = clean_ehr_dataset(
    df=sample_df
)

print(result)
~~~

### Related functions

- `profile_dataset`
- `infer_column_semantics`
- `normalize_missing_tokens`
- `standardize_dates`
- `standardize_units`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/cleaning.py#L570`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L570)
- Repository search: [clean_ehr_dataset](https://github.com/appsplorer/thomaslab-core/search?q=clean_ehr_dataset&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Run the guarded generic cleaning pipeline for an unfamiliar EHR table.

The function standardizes column names using :func:`thomaslab.data.standardize_schema`,
replaces configured missing tokens, parses configured dates, runs caller-defined
plausibility ranges, and removes exact duplicates. Domain-specific transformations
remain explicit because a generic cleaner should not guess clinical semantics.

### API inspection

~~~python
import inspect
from thomaslab.cleaning import clean_ehr_dataset

print(inspect.signature(clean_ehr_dataset))
print(clean_ehr_dataset.__doc__)
~~~

### Source

[`src/thomaslab/cleaning.py#L570`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/cleaning.py#L570)

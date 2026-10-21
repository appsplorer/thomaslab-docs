# thomaslab.missing

Missing-data diagnostics and reproducible imputation utilities for clinical research.

The module describes observed missingness patterns; it does not infer that data are MCAR,
MAR, or MNAR from observed data alone. Study-specific assumptions remain the researcher's
responsibility.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 11

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.missing.summarize_missingness -->
## summarize_missingness

### Purpose

Return per-column missing counts, percentages, dtype, and non-missing cardinality.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_missingness( df: pd.DataFrame, *, columns: Sequence[str] | None = None ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `columns` | `columns: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

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

from thomaslab.missing import summarize_missingness

result = summarize_missingness(
    df=sample_df
)

print(result)
~~~

### Related functions

- `missingness_by_group`
- `missingness_over_time`
- `detect_structural_missingness`
- `create_missingness_indicators`
- `simple_impute`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/missing.py#L18`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L18)
- Repository search: [summarize_missingness](https://github.com/appsplorer/thomaslab-core/search?q=summarize_missingness&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return per-column missing counts, percentages, dtype, and non-missing cardinality.

### API inspection

~~~python
import inspect
from thomaslab.missing import summarize_missingness

print(inspect.signature(summarize_missingness))
print(summarize_missingness.__doc__)
~~~

### Source

[`src/thomaslab/missing.py#L18`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L18)

---

<!-- callable:thomaslab.missing.missingness_by_group -->
## missingness_by_group

### Purpose

Summarize missingness by site, treatment arm, demographic group, or another stratum.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def missingness_by_group( df: pd.DataFrame, group_col: str, *, columns: Sequence[str] | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `group_col` | `group_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `columns` | `columns: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `group_col`.
- Referenced columns must exist in the input table: `group_col`.

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

from thomaslab.missing import missingness_by_group

result = missingness_by_group(
    df=sample_df,
    group_col='group'
)

print(result)
~~~

### Related functions

- `summarize_missingness`
- `missingness_over_time`
- `detect_structural_missingness`
- `create_missingness_indicators`
- `simple_impute`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/missing.py#L50`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L50)
- Repository search: [missingness_by_group](https://github.com/appsplorer/thomaslab-core/search?q=missingness_by_group&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize missingness by site, treatment arm, demographic group, or another stratum.

### API inspection

~~~python
import inspect
from thomaslab.missing import missingness_by_group

print(inspect.signature(missingness_by_group))
print(missingness_by_group.__doc__)
~~~

### Source

[`src/thomaslab/missing.py#L50`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L50)

---

<!-- callable:thomaslab.missing.missingness_over_time -->
## missingness_over_time

### Purpose

Track missingness over calendar periods to reveal extract/system changes.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def missingness_over_time( df: pd.DataFrame, date_col: str, *, columns: Sequence[str] | None = None, freq: str = "M", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `date_col` | `date_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `columns` | `columns: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `freq` | `freq: str = 'M'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `date_col`.
- Referenced columns must exist in the input table: `date_col`.

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

from thomaslab.missing import missingness_over_time

result = missingness_over_time(
    df=sample_df,
    date_col='event_date'
)

print(result)
~~~

### Related functions

- `summarize_missingness`
- `missingness_by_group`
- `detect_structural_missingness`
- `create_missingness_indicators`
- `simple_impute`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/missing.py#L79`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L79)
- Repository search: [missingness_over_time](https://github.com/appsplorer/thomaslab-core/search?q=missingness_over_time&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Track missingness over calendar periods to reveal extract/system changes.

### API inspection

~~~python
import inspect
from thomaslab.missing import missingness_over_time

print(inspect.signature(missingness_over_time))
print(missingness_over_time.__doc__)
~~~

### Source

[`src/thomaslab/missing.py#L79`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L79)

---

<!-- callable:thomaslab.missing.detect_structural_missingness -->
## detect_structural_missingness

### Purpose

Flag variables that are nearly absent at one site but materially observed elsewhere.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_structural_missingness( df: pd.DataFrame, site_col: str, *, columns: Sequence[str] | None = None, site_missing_threshold: float = 0.95, contrast_threshold: float = 0.20, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `site_col` | `site_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `columns` | `columns: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `site_missing_threshold` | `site_missing_threshold: float = 0.95` | No | Site/domain identifier used for grouping, validation, or transportability analysis. |
| `contrast_threshold` | `contrast_threshold: float = 0.2` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `site_col`.
- Referenced columns must exist in the input table: `site_col`.

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

from thomaslab.missing import detect_structural_missingness

result = detect_structural_missingness(
    df=sample_df,
    site_col='site'
)

print(result)
~~~

### Related functions

- `summarize_missingness`
- `missingness_by_group`
- `missingness_over_time`
- `create_missingness_indicators`
- `simple_impute`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/missing.py#L106`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L106)
- Repository search: [detect_structural_missingness](https://github.com/appsplorer/thomaslab-core/search?q=detect_structural_missingness&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Flag variables that are nearly absent at one site but materially observed elsewhere.

This is a heuristic for *structural/site-specific* missingness, not proof of a causal
missing-data mechanism.

### API inspection

~~~python
import inspect
from thomaslab.missing import detect_structural_missingness

print(inspect.signature(detect_structural_missingness))
print(detect_structural_missingness.__doc__)
~~~

### Source

[`src/thomaslab/missing.py#L106`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L106)

---

<!-- callable:thomaslab.missing.create_missingness_indicators -->
## create_missingness_indicators

### Purpose

Append deterministic binary missingness indicators without imputing values.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def create_missingness_indicators( df: pd.DataFrame, columns: Sequence[str] | None = None, *, suffix: str = "__missing", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `columns` | `columns: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `suffix` | `suffix: str = '__missing'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

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

from thomaslab.missing import create_missingness_indicators

result = create_missingness_indicators(
    df=sample_df
)

print(result)
~~~

### Related functions

- `summarize_missingness`
- `missingness_by_group`
- `missingness_over_time`
- `detect_structural_missingness`
- `simple_impute`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/missing.py#L159`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L159)
- Repository search: [create_missingness_indicators](https://github.com/appsplorer/thomaslab-core/search?q=create_missingness_indicators&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Append deterministic binary missingness indicators without imputing values.

### API inspection

~~~python
import inspect
from thomaslab.missing import create_missingness_indicators

print(inspect.signature(create_missingness_indicators))
print(create_missingness_indicators.__doc__)
~~~

### Source

[`src/thomaslab/missing.py#L159`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L159)

---

<!-- callable:thomaslab.missing.simple_impute -->
## simple_impute

### Purpose

Impute selected columns with transparent univariate rules.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def simple_impute( df: pd.DataFrame, *, numeric_strategy: str = "median", categorical_strategy: str = "mode", constant_value: Any = "Missing", columns: Sequence[str] | None = None, return_report: bool = False, ) -> pd.DataFrame | tuple[pd.DataFrame, pd.DataFrame]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `numeric_strategy` | `numeric_strategy: str = 'median'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `categorical_strategy` | `categorical_strategy: str = 'mode'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `constant_value` | `constant_value: Any = 'Missing'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `columns` | `columns: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
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

from thomaslab.missing import simple_impute

result = simple_impute(
    df=sample_df
)

print(result)
~~~

### Related functions

- `summarize_missingness`
- `missingness_by_group`
- `missingness_over_time`
- `detect_structural_missingness`
- `create_missingness_indicators`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/missing.py#L180`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L180)
- Repository search: [simple_impute](https://github.com/appsplorer/thomaslab-core/search?q=simple_impute&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Impute selected columns with transparent univariate rules.

### API inspection

~~~python
import inspect
from thomaslab.missing import simple_impute

print(inspect.signature(simple_impute))
print(simple_impute.__doc__)
~~~

### Source

[`src/thomaslab/missing.py#L180`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L180)

---

<!-- callable:thomaslab.missing.iterative_impute_clinical -->
## iterative_impute_clinical

### Purpose

Apply sklearn IterativeImputer to explicitly selected numeric columns.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def iterative_impute_clinical( df: pd.DataFrame, numeric_columns: Sequence[str], *, max_iter: int = 10, random_state: int = 42, return_report: bool = False, ) -> pd.DataFrame | tuple[pd.DataFrame, pd.DataFrame]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `numeric_columns` | `numeric_columns: Sequence[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `max_iter` | `max_iter: int = 10` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |
| `return_report` | `return_report: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `numeric_columns`.

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

from thomaslab.missing import iterative_impute_clinical

result = iterative_impute_clinical(
    df=sample_df,
    numeric_columns=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `summarize_missingness`
- `missingness_by_group`
- `missingness_over_time`
- `detect_structural_missingness`
- `create_missingness_indicators`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/missing.py#L230`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L230)
- Repository search: [iterative_impute_clinical](https://github.com/appsplorer/thomaslab-core/search?q=iterative_impute_clinical&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Apply sklearn IterativeImputer to explicitly selected numeric columns.

This is a deterministic single completed dataset, not Rubin-style multiple imputation.

### API inspection

~~~python
import inspect
from thomaslab.missing import iterative_impute_clinical

print(inspect.signature(iterative_impute_clinical))
print(iterative_impute_clinical.__doc__)
~~~

### Source

[`src/thomaslab/missing.py#L230`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L230)

---

<!-- callable:thomaslab.missing.longitudinal_impute -->
## longitudinal_impute

### Purpose

Carry measurements within a patient trajectory with optional maximum time gap.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def longitudinal_impute( df: pd.DataFrame, patient_id_col: str, date_col: str, columns: Sequence[str], *, method: str = "ffill", max_gap_days: float | None = None, return_report: bool = False, ) -> pd.DataFrame | tuple[pd.DataFrame, pd.DataFrame]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_id_col` | `patient_id_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `columns` | `columns: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `method` | `method: str = 'ffill'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `max_gap_days` | `max_gap_days: float \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `return_report` | `return_report: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `patient_id_col`, `date_col`, `columns`.
- Referenced columns must exist in the input table: `patient_id_col`, `date_col`.

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

from thomaslab.missing import longitudinal_impute

result = longitudinal_impute(
    df=sample_df,
    patient_id_col='patient_id',
    date_col='event_date',
    columns=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `summarize_missingness`
- `missingness_by_group`
- `missingness_over_time`
- `detect_structural_missingness`
- `create_missingness_indicators`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/missing.py#L268`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L268)
- Repository search: [longitudinal_impute](https://github.com/appsplorer/thomaslab-core/search?q=longitudinal_impute&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Carry measurements within a patient trajectory with optional maximum time gap.

### API inspection

~~~python
import inspect
from thomaslab.missing import longitudinal_impute

print(inspect.signature(longitudinal_impute))
print(longitudinal_impute.__doc__)
~~~

### Source

[`src/thomaslab/missing.py#L268`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L268)

---

<!-- callable:thomaslab.missing.compare_imputation_strategies -->
## compare_imputation_strategies

### Purpose

Compare imputation reconstruction error on a deterministic masked subset of observed values.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def compare_imputation_strategies( df: pd.DataFrame, numeric_columns: Sequence[str], *, strategies: Sequence[str] = ("median", "mean", "iterative"), mask_fraction: float = 0.10, random_state: int = 42, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `numeric_columns` | `numeric_columns: Sequence[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `strategies` | `strategies: Sequence[str] = ('median', 'mean', 'iterative')` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `mask_fraction` | `mask_fraction: float = 0.1` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `numeric_columns`.

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

from thomaslab.missing import compare_imputation_strategies

result = compare_imputation_strategies(
    df=sample_df,
    numeric_columns=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `summarize_missingness`
- `missingness_by_group`
- `missingness_over_time`
- `detect_structural_missingness`
- `create_missingness_indicators`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/missing.py#L320`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L320)
- Repository search: [compare_imputation_strategies](https://github.com/appsplorer/thomaslab-core/search?q=compare_imputation_strategies&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compare imputation reconstruction error on a deterministic masked subset of observed values.

### API inspection

~~~python
import inspect
from thomaslab.missing import compare_imputation_strategies

print(inspect.signature(compare_imputation_strategies))
print(compare_imputation_strategies.__doc__)
~~~

### Source

[`src/thomaslab/missing.py#L320`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L320)

---

<!-- callable:thomaslab.missing.missingness_group_association -->
## missingness_group_association

### Purpose

Test whether observed missingness differs across a categorical grouping variable.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def missingness_group_association( df: pd.DataFrame, value_col: str, group_col: str ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `value_col` | `value_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `group_col` | `group_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `value_col`, `group_col`.
- Referenced columns must exist in the input table: `value_col`, `group_col`.

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

from thomaslab.missing import missingness_group_association

result = missingness_group_association(
    df=sample_df,
    value_col='value',
    group_col='group'
)

print(result)
~~~

### Related functions

- `summarize_missingness`
- `missingness_by_group`
- `missingness_over_time`
- `detect_structural_missingness`
- `create_missingness_indicators`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/missing.py#L385`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L385)
- Repository search: [missingness_group_association](https://github.com/appsplorer/thomaslab-core/search?q=missingness_group_association&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Test whether observed missingness differs across a categorical grouping variable.

The chi-square association is descriptive evidence that missingness varies by group; it
does not identify MCAR/MAR/MNAR mechanisms.

### API inspection

~~~python
import inspect
from thomaslab.missing import missingness_group_association

print(inspect.signature(missingness_group_association))
print(missingness_group_association.__doc__)
~~~

### Source

[`src/thomaslab/missing.py#L385`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L385)

---

<!-- callable:thomaslab.missing.generate_missingness_report -->
## generate_missingness_report

### Purpose

Generate a compact missingness audit bundle without imputing the source data.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def generate_missingness_report( df: pd.DataFrame, *, site_col: str | None = None, date_col: str | None = None, columns: Sequence[str] | None = None, ) -> dict[str, pd.DataFrame]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `site_col` | `site_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `columns` | `columns: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.
- Referenced columns must exist in the input table: `site_col`, `date_col`.

### Returns

`dict[str, pd.DataFrame]`

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

from thomaslab.missing import generate_missingness_report

result = generate_missingness_report(
    df=sample_df
)

print(result)
~~~

### Related functions

- `summarize_missingness`
- `missingness_by_group`
- `missingness_over_time`
- `detect_structural_missingness`
- `create_missingness_indicators`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/missing.py#L415`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L415)
- Repository search: [generate_missingness_report](https://github.com/appsplorer/thomaslab-core/search?q=generate_missingness_report&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Generate a compact missingness audit bundle without imputing the source data.

### API inspection

~~~python
import inspect
from thomaslab.missing import generate_missingness_report

print(inspect.signature(generate_missingness_report))
print(generate_missingness_report.__doc__)
~~~

### Source

[`src/thomaslab/missing.py#L415`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/missing.py#L415)

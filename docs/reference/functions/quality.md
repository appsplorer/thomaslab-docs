# thomaslab.quality

Clinical data quality, schema validation, leakage checks, and site-comparison utilities.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 7

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.quality.validate_clinical_schema -->
## validate_clinical_schema

### Purpose

Validate a clinical table against a lightweight schema contract.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_clinical_schema( df: pd.DataFrame, required_columns: Sequence[str], column_types: Mapping[str, str] | None = None, *, allow_extra: bool = True, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `required_columns` | `required_columns: Sequence[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `column_types` | `column_types: Mapping[str, str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `allow_extra` | `allow_extra: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `required_columns`.

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

from thomaslab.quality import validate_clinical_schema

result = validate_clinical_schema(
    df=sample_df,
    required_columns=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `summarize_missingness`
- `detect_duplicate_records`
- `check_numeric_ranges`
- `detect_temporal_leakage`
- `compare_site_distributions`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/quality.py#L18`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quality.py#L18)
- Repository search: [validate_clinical_schema](https://github.com/appsplorer/thomaslab-core/search?q=validate_clinical_schema&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate a clinical table against a lightweight schema contract.

Parameters
----------
df:
    Input clinical table.
required_columns:
    Columns that must be present.
column_types:
    Optional mapping from column name to one of ``numeric``, ``datetime``, ``string``,
    or ``boolean``. Validation is non-destructive and reports incompatible values rather
    than coercing the input.
allow_extra:
    If ``False``, columns not present in ``required_columns`` or ``column_types`` are
    reported as unexpected.

Returns
-------
dict
    ``valid`` plus detailed missing/unexpected/type issue diagnostics.

### API inspection

~~~python
import inspect
from thomaslab.quality import validate_clinical_schema

print(inspect.signature(validate_clinical_schema))
print(validate_clinical_schema.__doc__)
~~~

### Source

[`src/thomaslab/quality.py#L18`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quality.py#L18)

---

<!-- callable:thomaslab.quality.summarize_missingness -->
## summarize_missingness

### Purpose

Summarize missing values overall or stratified by a cohort/site column.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_missingness( df: pd.DataFrame, group_col: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `group_col` | `group_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.
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

from thomaslab.quality import summarize_missingness

result = summarize_missingness(
    df=sample_df
)

print(result)
~~~

### Related functions

- `validate_clinical_schema`
- `detect_duplicate_records`
- `check_numeric_ranges`
- `detect_temporal_leakage`
- `compare_site_distributions`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/quality.py#L99`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quality.py#L99)
- Repository search: [summarize_missingness](https://github.com/appsplorer/thomaslab-core/search?q=summarize_missingness&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize missing values overall or stratified by a cohort/site column.

### API inspection

~~~python
import inspect
from thomaslab.quality import summarize_missingness

print(inspect.signature(summarize_missingness))
print(summarize_missingness.__doc__)
~~~

### Source

[`src/thomaslab/quality.py#L99`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quality.py#L99)

---

<!-- callable:thomaslab.quality.detect_duplicate_records -->
## detect_duplicate_records

### Purpose

Return duplicate clinical rows with duplicate-group metadata.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_duplicate_records( df: pd.DataFrame, subset: Sequence[str], *, keep: str | bool = False, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `subset` | `subset: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `keep` | `keep: str \| bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `subset`.

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

from thomaslab.quality import detect_duplicate_records

result = detect_duplicate_records(
    df=sample_df,
    subset=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `validate_clinical_schema`
- `summarize_missingness`
- `check_numeric_ranges`
- `detect_temporal_leakage`
- `compare_site_distributions`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/quality.py#L136`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quality.py#L136)
- Repository search: [detect_duplicate_records](https://github.com/appsplorer/thomaslab-core/search?q=detect_duplicate_records&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return duplicate clinical rows with duplicate-group metadata.

### API inspection

~~~python
import inspect
from thomaslab.quality import detect_duplicate_records

print(inspect.signature(detect_duplicate_records))
print(detect_duplicate_records.__doc__)
~~~

### Source

[`src/thomaslab/quality.py#L136`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quality.py#L136)

---

<!-- callable:thomaslab.quality.check_numeric_ranges -->
## check_numeric_ranges

### Purpose

Audit numeric values against protocol- or physiology-informed bounds.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def check_numeric_ranges( df: pd.DataFrame, ranges: Mapping[str, tuple[float | None, float | None]], ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `ranges` | `ranges: Mapping[str, tuple[float \| None, float \| None]]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `ranges`.

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

from thomaslab.quality import check_numeric_ranges

result = check_numeric_ranges(
    df=sample_df,
    ranges={}
)

print(result)
~~~

### Related functions

- `validate_clinical_schema`
- `summarize_missingness`
- `detect_duplicate_records`
- `detect_temporal_leakage`
- `compare_site_distributions`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/quality.py#L160`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quality.py#L160)
- Repository search: [check_numeric_ranges](https://github.com/appsplorer/thomaslab-core/search?q=check_numeric_ranges&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Audit numeric values against protocol- or physiology-informed bounds.

Bounds are supplied by the caller; this function intentionally does not embed universal
physiological cutoffs because valid ranges vary by units, population, and study protocol.

### API inspection

~~~python
import inspect
from thomaslab.quality import check_numeric_ranges

print(inspect.signature(check_numeric_ranges))
print(check_numeric_ranges.__doc__)
~~~

### Source

[`src/thomaslab/quality.py#L160`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quality.py#L160)

---

<!-- callable:thomaslab.quality.detect_temporal_leakage -->
## detect_temporal_leakage

### Purpose

Detect feature timestamps occurring after the permitted index-date boundary.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_temporal_leakage( df: pd.DataFrame, index_date_col: str, feature_date_cols: Sequence[str], *, allowed_lag_days: int = 0, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `index_date_col` | `index_date_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `feature_date_cols` | `feature_date_cols: Sequence[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `allowed_lag_days` | `allowed_lag_days: int = 0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `index_date_col`, `feature_date_cols`.
- Referenced columns must exist in the input table: `index_date_col`.

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

from thomaslab.quality import detect_temporal_leakage

result = detect_temporal_leakage(
    df=sample_df,
    index_date_col='index_date',
    feature_date_cols=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `validate_clinical_schema`
- `summarize_missingness`
- `detect_duplicate_records`
- `check_numeric_ranges`
- `compare_site_distributions`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/quality.py#L210`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quality.py#L210)
- Repository search: [detect_temporal_leakage](https://github.com/appsplorer/thomaslab-core/search?q=detect_temporal_leakage&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Detect feature timestamps occurring after the permitted index-date boundary.

### API inspection

~~~python
import inspect
from thomaslab.quality import detect_temporal_leakage

print(inspect.signature(detect_temporal_leakage))
print(detect_temporal_leakage.__doc__)
~~~

### Source

[`src/thomaslab/quality.py#L210`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quality.py#L210)

---

<!-- callable:thomaslab.quality.compare_site_distributions -->
## compare_site_distributions

### Purpose

Compare feature distributions across sites using standardized shifts.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def compare_site_distributions( df: pd.DataFrame, site_col: str, feature_cols: Sequence[str], *, reference_site: object | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `site_col` | `site_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `feature_cols` | `feature_cols: Sequence[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `reference_site` | `reference_site: object \| None = None` | No | Site/domain identifier used for grouping, validation, or transportability analysis. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `site_col`, `feature_cols`.
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

from thomaslab.quality import compare_site_distributions

result = compare_site_distributions(
    df=sample_df,
    site_col='site',
    feature_cols=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `validate_clinical_schema`
- `summarize_missingness`
- `detect_duplicate_records`
- `check_numeric_ranges`
- `detect_temporal_leakage`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/quality.py#L251`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quality.py#L251)
- Repository search: [compare_site_distributions](https://github.com/appsplorer/thomaslab-core/search?q=compare_site_distributions&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compare feature distributions across sites using standardized shifts.

Numeric features report standardized mean difference and Wasserstein distance. Categorical
features report total variation distance between category distributions.

### API inspection

~~~python
import inspect
from thomaslab.quality import compare_site_distributions

print(inspect.signature(compare_site_distributions))
print(compare_site_distributions.__doc__)
~~~

### Source

[`src/thomaslab/quality.py#L251`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quality.py#L251)

---

<!-- callable:thomaslab.quality.generate_data_quality_report -->
## generate_data_quality_report

### Purpose

Generate a compact, serializable clinical data-quality report.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def generate_data_quality_report( df: pd.DataFrame, *, required_columns: Sequence[str] | None = None, column_types: Mapping[str, str] | None = None, numeric_ranges: Mapping[str, tuple[float | None, float | None]] | None = None, duplicate_key: Sequence[str] | None = None, index_date_col: str | None = None, feature_date_cols: Sequence[str] | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `required_columns` | `required_columns: Sequence[str] \| None = None` | No | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `column_types` | `column_types: Mapping[str, str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `numeric_ranges` | `numeric_ranges: Mapping[str, tuple[float \| None, float \| None]] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `duplicate_key` | `duplicate_key: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `index_date_col` | `index_date_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `feature_date_cols` | `feature_date_cols: Sequence[str] \| None = None` | No | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.
- Referenced columns must exist in the input table: `index_date_col`.

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

from thomaslab.quality import generate_data_quality_report

result = generate_data_quality_report(
    df=sample_df
)

print(result)
~~~

### Related functions

- `validate_clinical_schema`
- `summarize_missingness`
- `detect_duplicate_records`
- `check_numeric_ranges`
- `detect_temporal_leakage`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/quality.py#L333`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quality.py#L333)
- Repository search: [generate_data_quality_report](https://github.com/appsplorer/thomaslab-core/search?q=generate_data_quality_report&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Generate a compact, serializable clinical data-quality report.

### API inspection

~~~python
import inspect
from thomaslab.quality import generate_data_quality_report

print(inspect.signature(generate_data_quality_report))
print(generate_data_quality_report.__doc__)
~~~

### Source

[`src/thomaslab/quality.py#L333`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/quality.py#L333)

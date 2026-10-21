# thomaslab.harmonize

Multi-site harmonisation diagnostics for heterogeneous clinical datasets.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 9

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.harmonize.compare_site_schemas -->
## compare_site_schemas

### Purpose

Create a site-by-column presence matrix and commonality summary.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def compare_site_schemas(tables: Mapping[str, pd.DataFrame]) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `tables` | `tables: Mapping[str, pd.DataFrame]` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `tables`.

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

from thomaslab.harmonize import compare_site_schemas

result = compare_site_schemas(
    tables=sample_df
)

print(result)
~~~

### Related functions

- `compare_site_units`
- `compare_site_missingness`
- `compare_site_code_coverage`
- `harmonize_categories`
- `harmonize_measurement_units`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/harmonize.py#L14`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/harmonize.py#L14)
- Repository search: [compare_site_schemas](https://github.com/appsplorer/thomaslab-core/search?q=compare_site_schemas&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create a site-by-column presence matrix and commonality summary.

### API inspection

~~~python
import inspect
from thomaslab.harmonize import compare_site_schemas

print(inspect.signature(compare_site_schemas))
print(compare_site_schemas.__doc__)
~~~

### Source

[`src/thomaslab/harmonize.py#L14`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/harmonize.py#L14)

---

<!-- callable:thomaslab.harmonize.compare_site_units -->
## compare_site_units

### Purpose

Report unit vocabularies per site and measurement.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def compare_site_units( df: pd.DataFrame, site_col: str, measure_col: str, unit_col: str ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `site_col` | `site_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `measure_col` | `measure_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `unit_col` | `unit_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `site_col`, `measure_col`, `unit_col`.
- Referenced columns must exist in the input table: `site_col`, `measure_col`, `unit_col`.

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

from thomaslab.harmonize import compare_site_units

result = compare_site_units(
    df=sample_df,
    site_col='site',
    measure_col='measure',
    unit_col='unit'
)

print(result)
~~~

### Related functions

- `compare_site_schemas`
- `compare_site_missingness`
- `compare_site_code_coverage`
- `harmonize_categories`
- `harmonize_measurement_units`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/harmonize.py#L34`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/harmonize.py#L34)
- Repository search: [compare_site_units](https://github.com/appsplorer/thomaslab-core/search?q=compare_site_units&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Report unit vocabularies per site and measurement.

### API inspection

~~~python
import inspect
from thomaslab.harmonize import compare_site_units

print(inspect.signature(compare_site_units))
print(compare_site_units.__doc__)
~~~

### Source

[`src/thomaslab/harmonize.py#L34`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/harmonize.py#L34)

---

<!-- callable:thomaslab.harmonize.compare_site_missingness -->
## compare_site_missingness

### Purpose

Return site-level missingness percentages for selected variables.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def compare_site_missingness( df: pd.DataFrame, site_col: str, *, columns: Sequence[str] | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `site_col` | `site_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `columns` | `columns: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

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

from thomaslab.harmonize import compare_site_missingness

result = compare_site_missingness(
    df=sample_df,
    site_col='site'
)

print(result)
~~~

### Related functions

- `compare_site_schemas`
- `compare_site_units`
- `compare_site_code_coverage`
- `harmonize_categories`
- `harmonize_measurement_units`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/harmonize.py#L49`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/harmonize.py#L49)
- Repository search: [compare_site_missingness](https://github.com/appsplorer/thomaslab-core/search?q=compare_site_missingness&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return site-level missingness percentages for selected variables.

### API inspection

~~~python
import inspect
from thomaslab.harmonize import compare_site_missingness

print(inspect.signature(compare_site_missingness))
print(compare_site_missingness.__doc__)
~~~

### Source

[`src/thomaslab/harmonize.py#L49`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/harmonize.py#L49)

---

<!-- callable:thomaslab.harmonize.compare_site_code_coverage -->
## compare_site_code_coverage

### Purpose

Summarize distinct code coverage and optional reference-set coverage per site.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def compare_site_code_coverage( df: pd.DataFrame, site_col: str, code_col: str, *, reference_codes: Sequence[str] | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `site_col` | `site_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `code_col` | `code_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `reference_codes` | `reference_codes: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `site_col`, `code_col`.
- Referenced columns must exist in the input table: `site_col`, `code_col`.

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

from thomaslab.harmonize import compare_site_code_coverage

result = compare_site_code_coverage(
    df=sample_df,
    site_col='site',
    code_col='code'
)

print(result)
~~~

### Related functions

- `compare_site_schemas`
- `compare_site_units`
- `compare_site_missingness`
- `harmonize_categories`
- `harmonize_measurement_units`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/harmonize.py#L75`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/harmonize.py#L75)
- Repository search: [compare_site_code_coverage](https://github.com/appsplorer/thomaslab-core/search?q=compare_site_code_coverage&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize distinct code coverage and optional reference-set coverage per site.

### API inspection

~~~python
import inspect
from thomaslab.harmonize import compare_site_code_coverage

print(inspect.signature(compare_site_code_coverage))
print(compare_site_code_coverage.__doc__)
~~~

### Source

[`src/thomaslab/harmonize.py#L75`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/harmonize.py#L75)

---

<!-- callable:thomaslab.harmonize.harmonize_categories -->
## harmonize_categories

### Purpose

Map site-specific category labels to a reviewed common representation.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def harmonize_categories( df: pd.DataFrame, column: str, mapping: Mapping[Any, Any], *, unknown_value: Any | None = None, strict: bool = False, preserve_source: bool = True, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `column` | `column: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `mapping` | `mapping: Mapping[Any, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `unknown_value` | `unknown_value: Any \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strict` | `strict: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `preserve_source` | `preserve_source: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `column`, `mapping`.

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

from thomaslab.harmonize import harmonize_categories

result = harmonize_categories(
    df=sample_df,
    column="value",
    mapping={}
)

print(result)
~~~

### Related functions

- `compare_site_schemas`
- `compare_site_units`
- `compare_site_missingness`
- `compare_site_code_coverage`
- `harmonize_measurement_units`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/harmonize.py#L105`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/harmonize.py#L105)
- Repository search: [harmonize_categories](https://github.com/appsplorer/thomaslab-core/search?q=harmonize_categories&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Map site-specific category labels to a reviewed common representation.

### API inspection

~~~python
import inspect
from thomaslab.harmonize import harmonize_categories

print(inspect.signature(harmonize_categories))
print(harmonize_categories.__doc__)
~~~

### Source

[`src/thomaslab/harmonize.py#L105`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/harmonize.py#L105)

---

<!-- callable:thomaslab.harmonize.harmonize_measurement_units -->
## harmonize_measurement_units

### Purpose

Harmonize units measure-by-measure using analyte-aware conversions.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def harmonize_measurement_units( df: pd.DataFrame, *, measure_col: str, value_col: str, unit_col: str, target_units: Mapping[str, str], strict: bool = True, ) -> tuple[pd.DataFrame, pd.DataFrame]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `measure_col` | `measure_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `value_col` | `value_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `unit_col` | `unit_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `target_units` | `target_units: Mapping[str, str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strict` | `strict: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `measure_col`, `value_col`, `unit_col`, `target_units`.
- Referenced columns must exist in the input table: `measure_col`, `value_col`, `unit_col`.

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

from thomaslab.harmonize import harmonize_measurement_units

result = harmonize_measurement_units(
    df=sample_df,
    measure_col='measure',
    value_col='value',
    unit_col='unit',
    target_units={}
)

print(result)
~~~

### Related functions

- `compare_site_schemas`
- `compare_site_units`
- `compare_site_missingness`
- `compare_site_code_coverage`
- `harmonize_categories`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/harmonize.py#L135`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/harmonize.py#L135)
- Repository search: [harmonize_measurement_units](https://github.com/appsplorer/thomaslab-core/search?q=harmonize_measurement_units&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Harmonize units measure-by-measure using analyte-aware conversions.

### API inspection

~~~python
import inspect
from thomaslab.harmonize import harmonize_measurement_units

print(inspect.signature(harmonize_measurement_units))
print(harmonize_measurement_units.__doc__)
~~~

### Source

[`src/thomaslab/harmonize.py#L135`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/harmonize.py#L135)

---

<!-- callable:thomaslab.harmonize.detect_site_shift -->
## detect_site_shift

### Purpose

Quantify simple site distribution shift using SMD or total-variation distance.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_site_shift( df: pd.DataFrame, site_col: str, columns: Sequence[str], *, reference_site: Any | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `site_col` | `site_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `columns` | `columns: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `reference_site` | `reference_site: Any \| None = None` | No | Site/domain identifier used for grouping, validation, or transportability analysis. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `site_col`, `columns`.
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

from thomaslab.harmonize import detect_site_shift

result = detect_site_shift(
    df=sample_df,
    site_col='site',
    columns=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `compare_site_schemas`
- `compare_site_units`
- `compare_site_missingness`
- `compare_site_code_coverage`
- `harmonize_categories`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/harmonize.py#L179`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/harmonize.py#L179)
- Repository search: [detect_site_shift](https://github.com/appsplorer/thomaslab-core/search?q=detect_site_shift&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Quantify simple site distribution shift using SMD or total-variation distance.

### API inspection

~~~python
import inspect
from thomaslab.harmonize import detect_site_shift

print(inspect.signature(detect_site_shift))
print(detect_site_shift.__doc__)
~~~

### Source

[`src/thomaslab/harmonize.py#L179`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/harmonize.py#L179)

---

<!-- callable:thomaslab.harmonize.build_common_data_dictionary -->
## build_common_data_dictionary

### Purpose

Build a cross-site data dictionary from columns/dtypes/missingness.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_common_data_dictionary(tables: Mapping[str, pd.DataFrame]) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `tables` | `tables: Mapping[str, pd.DataFrame]` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `tables`.

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

from thomaslab.harmonize import build_common_data_dictionary

result = build_common_data_dictionary(
    tables=sample_df
)

print(result)
~~~

### Related functions

- `compare_site_schemas`
- `compare_site_units`
- `compare_site_missingness`
- `compare_site_code_coverage`
- `harmonize_categories`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/harmonize.py#L239`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/harmonize.py#L239)
- Repository search: [build_common_data_dictionary](https://github.com/appsplorer/thomaslab-core/search?q=build_common_data_dictionary&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build a cross-site data dictionary from columns/dtypes/missingness.

### API inspection

~~~python
import inspect
from thomaslab.harmonize import build_common_data_dictionary

print(inspect.signature(build_common_data_dictionary))
print(build_common_data_dictionary.__doc__)
~~~

### Source

[`src/thomaslab/harmonize.py#L239`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/harmonize.py#L239)

---

<!-- callable:thomaslab.harmonize.generate_harmonization_report -->
## generate_harmonization_report

### Purpose

Generate a compact multi-site harmonization audit bundle.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def generate_harmonization_report( tables: Mapping[str, pd.DataFrame], *, site_col: str | None = None, shift_columns: Sequence[str] | None = None, ) -> dict[str, pd.DataFrame]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `tables` | `tables: Mapping[str, pd.DataFrame]` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `site_col` | `site_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `shift_columns` | `shift_columns: Sequence[str] \| None = None` | No | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `tables`.
- Referenced columns must exist in the input table: `site_col`.

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

from thomaslab.harmonize import generate_harmonization_report

result = generate_harmonization_report(
    tables=sample_df
)

print(result)
~~~

### Related functions

- `compare_site_schemas`
- `compare_site_units`
- `compare_site_missingness`
- `compare_site_code_coverage`
- `harmonize_categories`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/harmonize.py#L274`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/harmonize.py#L274)
- Repository search: [generate_harmonization_report](https://github.com/appsplorer/thomaslab-core/search?q=generate_harmonization_report&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Generate a compact multi-site harmonization audit bundle.

### API inspection

~~~python
import inspect
from thomaslab.harmonize import generate_harmonization_report

print(inspect.signature(generate_harmonization_report))
print(generate_harmonization_report.__doc__)
~~~

### Source

[`src/thomaslab/harmonize.py#L274`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/harmonize.py#L274)

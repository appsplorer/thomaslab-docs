# thomaslab.sdoh

Governed social-determinants-of-health (SDOH) enrichment utilities.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 7

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.sdoh.normalize_zip_code -->
## normalize_zip_code

### Purpose

Normalize U.S. ZIP codes to five-character strings where possible.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def normalize_zip_code(values: pd.Series | Sequence[object]) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `values` | `values: pd.Series \| Sequence[object]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

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

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.sdoh import normalize_zip_code

result = normalize_zip_code(
    values=sample_series
)

print(result)
~~~

### Related functions

- `map_zip_to_zcta`
- `attach_area_index`
- `attach_multiple_area_indices`
- `audit_geographic_linkage`
- `remove_direct_geography`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/sdoh.py#L17`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/sdoh.py#L17)
- Repository search: [normalize_zip_code](https://github.com/appsplorer/thomaslab-core/search?q=normalize_zip_code&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Normalize U.S. ZIP codes to five-character strings where possible.

### API inspection

~~~python
import inspect
from thomaslab.sdoh import normalize_zip_code

print(inspect.signature(normalize_zip_code))
print(normalize_zip_code.__doc__)
~~~

### Source

[`src/thomaslab/sdoh.py#L17`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/sdoh.py#L17)

---

<!-- callable:thomaslab.sdoh.map_zip_to_zcta -->
## map_zip_to_zcta

### Purpose

Map ZIP to ZCTA using an explicit supplied crosswalk.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def map_zip_to_zcta( df: pd.DataFrame, crosswalk: pd.DataFrame, *, zip_col: str, crosswalk_zip_col: str, zcta_col: str, weight_col: str | None = None, strategy: str = "highest_weight", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `crosswalk` | `crosswalk: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `zip_col` | `zip_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `crosswalk_zip_col` | `crosswalk_zip_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `zcta_col` | `zcta_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `weight_col` | `weight_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `strategy` | `strategy: str = 'highest_weight'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `crosswalk`, `zip_col`, `crosswalk_zip_col`, `zcta_col`.
- Referenced columns must exist in the input table: `zip_col`, `crosswalk_zip_col`, `zcta_col`, `weight_col`.

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

from thomaslab.sdoh import map_zip_to_zcta

result = map_zip_to_zcta(
    df=sample_df,
    crosswalk=sample_df,
    zip_col='zip',
    crosswalk_zip_col='crosswalk_zip',
    zcta_col='zcta'
)

print(result)
~~~

### Related functions

- `normalize_zip_code`
- `attach_area_index`
- `attach_multiple_area_indices`
- `audit_geographic_linkage`
- `remove_direct_geography`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/sdoh.py#L28`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/sdoh.py#L28)
- Repository search: [map_zip_to_zcta](https://github.com/appsplorer/thomaslab-core/search?q=map_zip_to_zcta&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Map ZIP to ZCTA using an explicit supplied crosswalk.

### API inspection

~~~python
import inspect
from thomaslab.sdoh import map_zip_to_zcta

print(inspect.signature(map_zip_to_zcta))
print(map_zip_to_zcta.__doc__)
~~~

### Source

[`src/thomaslab/sdoh.py#L28`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/sdoh.py#L28)

---

<!-- callable:thomaslab.sdoh.attach_area_index -->
## attach_area_index

### Purpose

Attach reviewed area-level contextual indices by geography.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def attach_area_index( df: pd.DataFrame, index_table: pd.DataFrame, *, geography_col: str, index_geography_col: str, value_columns: Sequence[str], prefix: str, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `index_table` | `index_table: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `geography_col` | `geography_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_geography_col` | `index_geography_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `value_columns` | `value_columns: Sequence[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `prefix` | `prefix: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `index_table`, `geography_col`, `index_geography_col`, `value_columns`, `prefix`.
- Referenced columns must exist in the input table: `geography_col`, `index_geography_col`.

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

from thomaslab.sdoh import attach_area_index

result = attach_area_index(
    df=sample_df,
    index_table=sample_df,
    geography_col='geography',
    index_geography_col='index_geography',
    value_columns=["feature_a", "feature_b"],
    prefix="value"
)

print(result)
~~~

### Related functions

- `normalize_zip_code`
- `map_zip_to_zcta`
- `attach_multiple_area_indices`
- `audit_geographic_linkage`
- `remove_direct_geography`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/sdoh.py#L80`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/sdoh.py#L80)
- Repository search: [attach_area_index](https://github.com/appsplorer/thomaslab-core/search?q=attach_area_index&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Attach reviewed area-level contextual indices by geography.

### API inspection

~~~python
import inspect
from thomaslab.sdoh import attach_area_index

print(inspect.signature(attach_area_index))
print(attach_area_index.__doc__)
~~~

### Source

[`src/thomaslab/sdoh.py#L80`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/sdoh.py#L80)

---

<!-- callable:thomaslab.sdoh.attach_multiple_area_indices -->
## attach_multiple_area_indices

### Purpose

Attach multiple explicit area-index tables with provenance prefixes.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def attach_multiple_area_indices( df: pd.DataFrame, *, geography_col: str, indices: Mapping[str, tuple[pd.DataFrame, str, Sequence[str]]], ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `geography_col` | `geography_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `indices` | `indices: Mapping[str, tuple[pd.DataFrame, str, Sequence[str]]]` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `geography_col`, `indices`.
- Referenced columns must exist in the input table: `geography_col`.

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

from thomaslab.sdoh import attach_multiple_area_indices

result = attach_multiple_area_indices(
    df=sample_df,
    geography_col='geography',
    indices=sample_df
)

print(result)
~~~

### Related functions

- `normalize_zip_code`
- `map_zip_to_zcta`
- `attach_area_index`
- `audit_geographic_linkage`
- `remove_direct_geography`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/sdoh.py#L104`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/sdoh.py#L104)
- Repository search: [attach_multiple_area_indices](https://github.com/appsplorer/thomaslab-core/search?q=attach_multiple_area_indices&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Attach multiple explicit area-index tables with provenance prefixes.

### API inspection

~~~python
import inspect
from thomaslab.sdoh import attach_multiple_area_indices

print(inspect.signature(attach_multiple_area_indices))
print(attach_multiple_area_indices.__doc__)
~~~

### Source

[`src/thomaslab/sdoh.py#L104`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/sdoh.py#L104)

---

<!-- callable:thomaslab.sdoh.audit_geographic_linkage -->
## audit_geographic_linkage

### Purpose

Audit mapping completeness overall and optionally by site.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_geographic_linkage( df: pd.DataFrame, *, source_geography_col: str, mapped_geography_col: str, site_col: str | None = None, ) -> dict[str, object]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `source_geography_col` | `source_geography_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `mapped_geography_col` | `mapped_geography_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `site_col` | `site_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `source_geography_col`, `mapped_geography_col`.
- Referenced columns must exist in the input table: `source_geography_col`, `mapped_geography_col`, `site_col`.

### Returns

`dict[str, object]`

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

from thomaslab.sdoh import audit_geographic_linkage

result = audit_geographic_linkage(
    df=sample_df,
    source_geography_col='source_geography',
    mapped_geography_col='mapped_geography'
)

print(result)
~~~

### Related functions

- `normalize_zip_code`
- `map_zip_to_zcta`
- `attach_area_index`
- `attach_multiple_area_indices`
- `remove_direct_geography`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/sdoh.py#L124`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/sdoh.py#L124)
- Repository search: [audit_geographic_linkage](https://github.com/appsplorer/thomaslab-core/search?q=audit_geographic_linkage&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Audit mapping completeness overall and optionally by site.

### API inspection

~~~python
import inspect
from thomaslab.sdoh import audit_geographic_linkage

print(inspect.signature(audit_geographic_linkage))
print(audit_geographic_linkage.__doc__)
~~~

### Source

[`src/thomaslab/sdoh.py#L124`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/sdoh.py#L124)

---

<!-- callable:thomaslab.sdoh.remove_direct_geography -->
## remove_direct_geography

### Purpose

Drop named direct-geography columns; this is not a de-identification guarantee.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def remove_direct_geography( df: pd.DataFrame, *, columns: Sequence[str], strict: bool = True ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `columns` | `columns: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strict` | `strict: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `columns`.

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

from thomaslab.sdoh import remove_direct_geography

result = remove_direct_geography(
    df=sample_df,
    columns=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `normalize_zip_code`
- `map_zip_to_zcta`
- `attach_area_index`
- `attach_multiple_area_indices`
- `audit_geographic_linkage`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/sdoh.py#L167`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/sdoh.py#L167)
- Repository search: [remove_direct_geography](https://github.com/appsplorer/thomaslab-core/search?q=remove_direct_geography&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Drop named direct-geography columns; this is not a de-identification guarantee.

### API inspection

~~~python
import inspect
from thomaslab.sdoh import remove_direct_geography

print(inspect.signature(remove_direct_geography))
print(remove_direct_geography.__doc__)
~~~

### Source

[`src/thomaslab/sdoh.py#L167`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/sdoh.py#L167)

---

<!-- callable:thomaslab.sdoh.build_sdoh_enriched_dataset -->
## build_sdoh_enriched_dataset

### Purpose

Build a governed ZCTA-linked SDOH research table.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_sdoh_enriched_dataset( df: pd.DataFrame, *, zip_col: str, zip_zcta_crosswalk: pd.DataFrame, crosswalk_zip_col: str, crosswalk_zcta_col: str, indices: Mapping[str, tuple[pd.DataFrame, str, Sequence[str]]], crosswalk_weight_col: str | None = None, mapping_strategy: str = "highest_weight", drop_direct_geography: bool = False, ) -> tuple[pd.DataFrame, dict[str, object]]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `zip_col` | `zip_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `zip_zcta_crosswalk` | `zip_zcta_crosswalk: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `crosswalk_zip_col` | `crosswalk_zip_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `crosswalk_zcta_col` | `crosswalk_zcta_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `indices` | `indices: Mapping[str, tuple[pd.DataFrame, str, Sequence[str]]]` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `crosswalk_weight_col` | `crosswalk_weight_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `mapping_strategy` | `mapping_strategy: str = 'highest_weight'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `drop_direct_geography` | `drop_direct_geography: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `zip_col`, `zip_zcta_crosswalk`, `crosswalk_zip_col`, `crosswalk_zcta_col`, `indices`.
- Referenced columns must exist in the input table: `zip_col`, `crosswalk_zip_col`, `crosswalk_zcta_col`, `crosswalk_weight_col`.

### Returns

`tuple[pd.DataFrame, dict[str, object]]`

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

from thomaslab.sdoh import build_sdoh_enriched_dataset

result = build_sdoh_enriched_dataset(
    df=sample_df,
    zip_col='zip',
    zip_zcta_crosswalk=sample_df,
    crosswalk_zip_col='crosswalk_zip',
    crosswalk_zcta_col='crosswalk_zcta',
    indices=sample_df
)

print(result)
~~~

### Related functions

- `normalize_zip_code`
- `map_zip_to_zcta`
- `attach_area_index`
- `attach_multiple_area_indices`
- `audit_geographic_linkage`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/sdoh.py#L177`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/sdoh.py#L177)
- Repository search: [build_sdoh_enriched_dataset](https://github.com/appsplorer/thomaslab-core/search?q=build_sdoh_enriched_dataset&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build a governed ZCTA-linked SDOH research table.

### API inspection

~~~python
import inspect
from thomaslab.sdoh import build_sdoh_enriched_dataset

print(inspect.signature(build_sdoh_enriched_dataset))
print(build_sdoh_enriched_dataset.__doc__)
~~~

### Source

[`src/thomaslab/sdoh.py#L177`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/sdoh.py#L177)

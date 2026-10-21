# thomaslab.codes

Versioned terminology and code-set helpers.

These utilities validate syntax and apply explicit reviewed mappings. They do not replace
licensed/current terminology services and never infer a clinical crosswalk from code strings.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 10

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.codes.normalize_loinc_codes -->
## normalize_loinc_codes

### Purpose

Normalize LOINC-like codes to uppercase hyphenated strings without validating existence.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def normalize_loinc_codes(series: pd.Series) -> pd.Series
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

from thomaslab.codes import normalize_loinc_codes

result = normalize_loinc_codes(
    series=sample_series
)

print(result)
~~~

### Related functions

- `normalize_rxnorm_codes`
- `validate_codeset`
- `load_codeset`
- `codeset_manifest`
- `compare_codesets`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/codes.py#L22`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L22)
- Repository search: [normalize_loinc_codes](https://github.com/appsplorer/thomaslab-core/search?q=normalize_loinc_codes&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Normalize LOINC-like codes to uppercase hyphenated strings without validating existence.

### API inspection

~~~python
import inspect
from thomaslab.codes import normalize_loinc_codes

print(inspect.signature(normalize_loinc_codes))
print(normalize_loinc_codes.__doc__)
~~~

### Source

[`src/thomaslab/codes.py#L22`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L22)

---

<!-- callable:thomaslab.codes.normalize_rxnorm_codes -->
## normalize_rxnorm_codes

### Purpose

Normalize RxNorm concept identifiers as digit strings without asserting concept validity.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def normalize_rxnorm_codes(series: pd.Series) -> pd.Series
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

from thomaslab.codes import normalize_rxnorm_codes

result = normalize_rxnorm_codes(
    series=sample_series
)

print(result)
~~~

### Related functions

- `normalize_loinc_codes`
- `validate_codeset`
- `load_codeset`
- `codeset_manifest`
- `compare_codesets`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/codes.py#L28`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L28)
- Repository search: [normalize_rxnorm_codes](https://github.com/appsplorer/thomaslab-core/search?q=normalize_rxnorm_codes&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Normalize RxNorm concept identifiers as digit strings without asserting concept validity.

### API inspection

~~~python
import inspect
from thomaslab.codes import normalize_rxnorm_codes

print(inspect.signature(normalize_rxnorm_codes))
print(normalize_rxnorm_codes.__doc__)
~~~

### Source

[`src/thomaslab/codes.py#L28`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L28)

---

<!-- callable:thomaslab.codes.validate_codeset -->
## validate_codeset

### Purpose

Perform format-level validation for common vocabularies.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_codeset(codes: Iterable[Any], vocabulary: str) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `codes` | `codes: Iterable[Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `vocabulary` | `vocabulary: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `codes`, `vocabulary`.

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
sample_value = "replace_with_validated_value"

from thomaslab.codes import validate_codeset

result = validate_codeset(
    codes=sample_value,
    vocabulary="value"
)

print(result)
~~~

### Related functions

- `normalize_loinc_codes`
- `normalize_rxnorm_codes`
- `load_codeset`
- `codeset_manifest`
- `compare_codesets`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/codes.py#L35`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L35)
- Repository search: [validate_codeset](https://github.com/appsplorer/thomaslab-core/search?q=validate_codeset&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Perform format-level validation for common vocabularies.

A valid format does not establish that a code exists in a specific terminology release.

### API inspection

~~~python
import inspect
from thomaslab.codes import validate_codeset

print(inspect.signature(validate_codeset))
print(validate_codeset.__doc__)
~~~

### Source

[`src/thomaslab/codes.py#L35`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L35)

---

<!-- callable:thomaslab.codes.load_codeset -->
## load_codeset

### Purpose

Load a YAML/JSON code set with metadata and a non-empty codes list.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def load_codeset(path: str | Path) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `path` | `path: str \| Path` | Yes | Input source/path accepted by this callable. Keep raw-source provenance and do not overwrite the source. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `path`.

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
from thomaslab.codes import load_codeset

result = load_codeset(
    path="path/to/input.csv"
)

print(result)
~~~

### Related functions

- `normalize_loinc_codes`
- `normalize_rxnorm_codes`
- `validate_codeset`
- `codeset_manifest`
- `compare_codesets`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/codes.py#L63`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L63)
- Repository search: [load_codeset](https://github.com/appsplorer/thomaslab-core/search?q=load_codeset&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Load a YAML/JSON code set with metadata and a non-empty codes list.

### API inspection

~~~python
import inspect
from thomaslab.codes import load_codeset

print(inspect.signature(load_codeset))
print(load_codeset.__doc__)
~~~

### Source

[`src/thomaslab/codes.py#L63`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L63)

---

<!-- callable:thomaslab.codes.codeset_manifest -->
## codeset_manifest

### Purpose

Create a stable SHA-256 manifest for provenance/version tracking.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def codeset_manifest(codeset: Mapping[str, Any]) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `codeset` | `codeset: Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `codeset`.

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
from thomaslab.codes import codeset_manifest

result = codeset_manifest(
    codeset={}
)

print(result)
~~~

### Related functions

- `normalize_loinc_codes`
- `normalize_rxnorm_codes`
- `validate_codeset`
- `load_codeset`
- `compare_codesets`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/codes.py#L85`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L85)
- Repository search: [codeset_manifest](https://github.com/appsplorer/thomaslab-core/search?q=codeset_manifest&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create a stable SHA-256 manifest for provenance/version tracking.

### API inspection

~~~python
import inspect
from thomaslab.codes import codeset_manifest

print(inspect.signature(codeset_manifest))
print(codeset_manifest.__doc__)
~~~

### Source

[`src/thomaslab/codes.py#L85`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L85)

---

<!-- callable:thomaslab.codes.compare_codesets -->
## compare_codesets

### Purpose

Compare two code collections without implying clinical equivalence.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def compare_codesets(left: Sequence[Any], right: Sequence[Any]) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `left` | `left: Sequence[Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `right` | `right: Sequence[Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `left`, `right`.

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
sample_value = "replace_with_validated_value"

from thomaslab.codes import compare_codesets

result = compare_codesets(
    left=sample_value,
    right=sample_value
)

print(result)
~~~

### Related functions

- `normalize_loinc_codes`
- `normalize_rxnorm_codes`
- `validate_codeset`
- `load_codeset`
- `codeset_manifest`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/codes.py#L99`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L99)
- Repository search: [compare_codesets](https://github.com/appsplorer/thomaslab-core/search?q=compare_codesets&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compare two code collections without implying clinical equivalence.

### API inspection

~~~python
import inspect
from thomaslab.codes import compare_codesets

print(inspect.signature(compare_codesets))
print(compare_codesets.__doc__)
~~~

### Source

[`src/thomaslab/codes.py#L99`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L99)

---

<!-- callable:thomaslab.codes.codeset_diff -->
## codeset_diff

### Purpose

Return long-form additions/removals between two versions of a code set.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def codeset_diff(left: Sequence[Any], right: Sequence[Any]) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `left` | `left: Sequence[Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `right` | `right: Sequence[Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `left`, `right`.

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
sample_value = "replace_with_validated_value"

from thomaslab.codes import codeset_diff

result = codeset_diff(
    left=sample_value,
    right=sample_value
)

print(result)
~~~

### Related functions

- `normalize_loinc_codes`
- `normalize_rxnorm_codes`
- `validate_codeset`
- `load_codeset`
- `codeset_manifest`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/codes.py#L113`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L113)
- Repository search: [codeset_diff](https://github.com/appsplorer/thomaslab-core/search?q=codeset_diff&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return long-form additions/removals between two versions of a code set.

### API inspection

~~~python
import inspect
from thomaslab.codes import codeset_diff

print(inspect.signature(codeset_diff))
print(codeset_diff.__doc__)
~~~

### Source

[`src/thomaslab/codes.py#L113`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L113)

---

<!-- callable:thomaslab.codes.expand_code_prefixes -->
## expand_code_prefixes

### Purpose

Expand reviewed wildcard/prefix definitions against an explicit code universe.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def expand_code_prefixes(codes: Sequence[str], universe: Sequence[str]) -> list[str]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `codes` | `codes: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `universe` | `universe: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `codes`, `universe`.

### Returns

`list[str]`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.codes import expand_code_prefixes

result = expand_code_prefixes(
    codes=["feature_a", "feature_b"],
    universe=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `normalize_loinc_codes`
- `normalize_rxnorm_codes`
- `validate_codeset`
- `load_codeset`
- `codeset_manifest`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/codes.py#L121`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L121)
- Repository search: [expand_code_prefixes](https://github.com/appsplorer/thomaslab-core/search?q=expand_code_prefixes&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Expand reviewed wildcard/prefix definitions against an explicit code universe.

### API inspection

~~~python
import inspect
from thomaslab.codes import expand_code_prefixes

print(inspect.signature(expand_code_prefixes))
print(expand_code_prefixes.__doc__)
~~~

### Source

[`src/thomaslab/codes.py#L121`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L121)

---

<!-- callable:thomaslab.codes.map_codes -->
## map_codes

### Purpose

Apply an explicit one-to-one reviewed code mapping with audit status.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def map_codes( df: pd.DataFrame, code_col: str, mapping: pd.DataFrame, *, source_col: str = "source_code", target_col: str = "target_code", strict: bool = False, preserve_source: bool = True, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `code_col` | `code_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `mapping` | `mapping: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `source_col` | `source_col: str = 'source_code'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `target_col` | `target_col: str = 'target_code'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `strict` | `strict: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `preserve_source` | `preserve_source: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `code_col`, `mapping`.
- Referenced columns must exist in the input table: `code_col`, `source_col`, `target_col`.

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

from thomaslab.codes import map_codes

result = map_codes(
    df=sample_df,
    code_col='code',
    mapping=sample_df
)

print(result)
~~~

### Related functions

- `normalize_loinc_codes`
- `normalize_rxnorm_codes`
- `validate_codeset`
- `load_codeset`
- `codeset_manifest`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/codes.py#L136`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L136)
- Repository search: [map_codes](https://github.com/appsplorer/thomaslab-core/search?q=map_codes&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Apply an explicit one-to-one reviewed code mapping with audit status.

### API inspection

~~~python
import inspect
from thomaslab.codes import map_codes

print(inspect.signature(map_codes))
print(map_codes.__doc__)
~~~

### Source

[`src/thomaslab/codes.py#L136`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L136)

---

<!-- callable:thomaslab.codes.normalize_codes -->
## normalize_codes

### Purpose

Dispatch conservative syntax normalization for selected vocabularies.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def normalize_codes(series: pd.Series, vocabulary: str) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `series` | `series: pd.Series` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `vocabulary` | `vocabulary: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `series`, `vocabulary`.

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

from thomaslab.codes import normalize_codes

result = normalize_codes(
    series=sample_series,
    vocabulary="value"
)

print(result)
~~~

### Related functions

- `normalize_loinc_codes`
- `normalize_rxnorm_codes`
- `validate_codeset`
- `load_codeset`
- `codeset_manifest`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/codes.py#L171`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L171)
- Repository search: [normalize_codes](https://github.com/appsplorer/thomaslab-core/search?q=normalize_codes&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Dispatch conservative syntax normalization for selected vocabularies.

### API inspection

~~~python
import inspect
from thomaslab.codes import normalize_codes

print(inspect.signature(normalize_codes))
print(normalize_codes.__doc__)
~~~

### Source

[`src/thomaslab/codes.py#L171`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/codes.py#L171)

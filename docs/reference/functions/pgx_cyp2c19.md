# thomaslab.pgx_cyp2c19

CYP2C19 genotype-to-function and phenotype translation utilities.

## Research-use boundary

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

## Self-service orientation

- Related guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 5

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.pgx_cyp2c19.cyp2c19_allele_function -->
## cyp2c19_allele_function

### Purpose

Return the function label for one CYP2C19 allele or ``unknown_function``.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def cyp2c19_allele_function(allele: object, function_table: pd.DataFrame | None = None) -> str
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `allele` | `allele: object` | Yes | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |
| `function_table` | `function_table: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `allele`.

### Returns

`str`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.pgx_cyp2c19 import cyp2c19_allele_function

result = cyp2c19_allele_function(
    allele="*1"
)

print(result)
~~~

### Related functions

- `assign_cyp2c19_phenotype`
- `count_cyp2c19_no_function_alleles`
- `translate_cyp2c19_diplotype`
- `translate_cyp2c19_table`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_cyp2c19.py#L27`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2c19.py#L27)
- Repository search: [cyp2c19_allele_function](https://github.com/appsplorer/thomaslab-core/search?q=cyp2c19_allele_function&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return the function label for one CYP2C19 allele or ``unknown_function``.

### API inspection

~~~python
import inspect
from thomaslab.pgx_cyp2c19 import cyp2c19_allele_function

print(inspect.signature(cyp2c19_allele_function))
print(cyp2c19_allele_function.__doc__)
~~~

### Source

[`src/thomaslab/pgx_cyp2c19.py#L27`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2c19.py#L27)

---

<!-- callable:thomaslab.pgx_cyp2c19.assign_cyp2c19_phenotype -->
## assign_cyp2c19_phenotype

### Purpose

Translate a CYP2C19 diplotype to a standardized metabolizer phenotype.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def assign_cyp2c19_phenotype( diplotype: object, function_table: pd.DataFrame | None = None, ) -> str
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `diplotype` | `diplotype: object` | Yes | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |
| `function_table` | `function_table: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `diplotype`.

### Returns

`str`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.pgx_cyp2c19 import assign_cyp2c19_phenotype

result = assign_cyp2c19_phenotype(
    diplotype="*1/*2"
)

print(result)
~~~

### Related functions

- `cyp2c19_allele_function`
- `count_cyp2c19_no_function_alleles`
- `translate_cyp2c19_diplotype`
- `translate_cyp2c19_table`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_cyp2c19.py#L37`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2c19.py#L37)
- Repository search: [assign_cyp2c19_phenotype](https://github.com/appsplorer/thomaslab-core/search?q=assign_cyp2c19_phenotype&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Translate a CYP2C19 diplotype to a standardized metabolizer phenotype.

Supports confirmed, ``Likely`` and ``Indeterminate`` categories. Unknown allele
functions return ``Unknown`` rather than being treated as reference/normal.

### API inspection

~~~python
import inspect
from thomaslab.pgx_cyp2c19 import assign_cyp2c19_phenotype

print(inspect.signature(assign_cyp2c19_phenotype))
print(assign_cyp2c19_phenotype.__doc__)
~~~

### Source

[`src/thomaslab/pgx_cyp2c19.py#L37`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2c19.py#L37)

---

<!-- callable:thomaslab.pgx_cyp2c19.count_cyp2c19_no_function_alleles -->
## count_cyp2c19_no_function_alleles

### Purpose

Count resolved no-function alleles; return ``None`` if any allele is unresolved.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def count_cyp2c19_no_function_alleles( diplotype: object, function_table: pd.DataFrame | None = None, ) -> int | None
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `diplotype` | `diplotype: object` | Yes | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |
| `function_table` | `function_table: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `diplotype`.

### Returns

`int | None`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.pgx_cyp2c19 import count_cyp2c19_no_function_alleles

result = count_cyp2c19_no_function_alleles(
    diplotype="*1/*2"
)

print(result)
~~~

### Related functions

- `cyp2c19_allele_function`
- `assign_cyp2c19_phenotype`
- `translate_cyp2c19_diplotype`
- `translate_cyp2c19_table`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_cyp2c19.py#L79`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2c19.py#L79)
- Repository search: [count_cyp2c19_no_function_alleles](https://github.com/appsplorer/thomaslab-core/search?q=count_cyp2c19_no_function_alleles&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Count resolved no-function alleles; return ``None`` if any allele is unresolved.

### API inspection

~~~python
import inspect
from thomaslab.pgx_cyp2c19 import count_cyp2c19_no_function_alleles

print(inspect.signature(count_cyp2c19_no_function_alleles))
print(count_cyp2c19_no_function_alleles.__doc__)
~~~

### Source

[`src/thomaslab/pgx_cyp2c19.py#L79`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2c19.py#L79)

---

<!-- callable:thomaslab.pgx_cyp2c19.translate_cyp2c19_diplotype -->
## translate_cyp2c19_diplotype

### Purpose

Return normalized diplotype, allele functions, LOF count and phenotype.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def translate_cyp2c19_diplotype( diplotype: object, function_table: pd.DataFrame | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `diplotype` | `diplotype: object` | Yes | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |
| `function_table` | `function_table: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `diplotype`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.pgx_cyp2c19 import translate_cyp2c19_diplotype

result = translate_cyp2c19_diplotype(
    diplotype="*1/*2"
)

print(result)
~~~

### Related functions

- `cyp2c19_allele_function`
- `assign_cyp2c19_phenotype`
- `count_cyp2c19_no_function_alleles`
- `translate_cyp2c19_table`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_cyp2c19.py#L93`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2c19.py#L93)
- Repository search: [translate_cyp2c19_diplotype](https://github.com/appsplorer/thomaslab-core/search?q=translate_cyp2c19_diplotype&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return normalized diplotype, allele functions, LOF count and phenotype.

### API inspection

~~~python
import inspect
from thomaslab.pgx_cyp2c19 import translate_cyp2c19_diplotype

print(inspect.signature(translate_cyp2c19_diplotype))
print(translate_cyp2c19_diplotype.__doc__)
~~~

### Source

[`src/thomaslab/pgx_cyp2c19.py#L93`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2c19.py#L93)

---

<!-- callable:thomaslab.pgx_cyp2c19.translate_cyp2c19_table -->
## translate_cyp2c19_table

### Purpose

Batch-translate CYP2C19 diplotypes while preserving the original index.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def translate_cyp2c19_table( df: pd.DataFrame, *, allele_1_col: str | None = None, allele_2_col: str | None = None, diplotype_col: str | None = None, function_table: pd.DataFrame | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `allele_1_col` | `allele_1_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `allele_2_col` | `allele_2_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `diplotype_col` | `diplotype_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `function_table` | `function_table: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.
- Referenced columns must exist in the input table: `allele_1_col`, `allele_2_col`, `diplotype_col`.

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

from thomaslab.pgx_cyp2c19 import translate_cyp2c19_table

result = translate_cyp2c19_table(
    df=sample_df
)

print(result)
~~~

### Related functions

- `cyp2c19_allele_function`
- `assign_cyp2c19_phenotype`
- `count_cyp2c19_no_function_alleles`
- `translate_cyp2c19_diplotype`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_cyp2c19.py#L116`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2c19.py#L116)
- Repository search: [translate_cyp2c19_table](https://github.com/appsplorer/thomaslab-core/search?q=translate_cyp2c19_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Batch-translate CYP2C19 diplotypes while preserving the original index.

### API inspection

~~~python
import inspect
from thomaslab.pgx_cyp2c19 import translate_cyp2c19_table

print(inspect.signature(translate_cyp2c19_table))
print(translate_cyp2c19_table.__doc__)
~~~

### Source

[`src/thomaslab/pgx_cyp2c19.py#L116`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2c19.py#L116)

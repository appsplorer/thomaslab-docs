# thomaslab.pgx_core

Core pharmacogenomics normalization and allele-function utilities.

These helpers standardize star-allele/diplotype representations and load versioned
allele-function tables. They are research infrastructure, not a replacement for a
validated laboratory caller or current clinical guideline source.

## Research-use boundary

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

## Self-service orientation

- Related guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 6

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.pgx_core.normalize_star_allele -->
## normalize_star_allele

### Purpose

Normalize a star-allele label while preserving explicit copy-number suffixes.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def normalize_star_allele(value: object, gene: str | None = None) -> str
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `value` | `value: object` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `gene` | `gene: str \| None = None` | No | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `value`.

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
from thomaslab.pgx_core import normalize_star_allele

result = normalize_star_allele(
    value={"key": "value"}
)

print(result)
~~~

### Related functions

- `split_allele_copy_number`
- `normalize_diplotype`
- `load_allele_function_table`
- `get_allele_function`
- `summarize_diplotype_functions`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_core.py#L28`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_core.py#L28)
- Repository search: [normalize_star_allele](https://github.com/appsplorer/thomaslab-core/search?q=normalize_star_allele&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Normalize a star-allele label while preserving explicit copy-number suffixes.

Examples
--------
``CYP2D6*1x2`` -> ``*1x2``
``2`` with ``gene='CYP2C19'`` -> ``*2``

### API inspection

~~~python
import inspect
from thomaslab.pgx_core import normalize_star_allele

print(inspect.signature(normalize_star_allele))
print(normalize_star_allele.__doc__)
~~~

### Source

[`src/thomaslab/pgx_core.py#L28`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_core.py#L28)

---

<!-- callable:thomaslab.pgx_core.split_allele_copy_number -->
## split_allele_copy_number

### Purpose

Return the base star allele and explicit copy count.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def split_allele_copy_number(value: object, gene: str | None = None) -> tuple[str, int]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `value` | `value: object` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `gene` | `gene: str \| None = None` | No | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `value`.

### Returns

`tuple[str, int]`

### Output guidance

Returns multiple ordered outputs. Keep the complete tuple contract rather than using one component without its companion diagnostics.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.pgx_core import split_allele_copy_number

result = split_allele_copy_number(
    value={"key": "value"}
)

print(result)
~~~

### Related functions

- `normalize_star_allele`
- `normalize_diplotype`
- `load_allele_function_table`
- `get_allele_function`
- `summarize_diplotype_functions`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_core.py#L52`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_core.py#L52)
- Repository search: [split_allele_copy_number](https://github.com/appsplorer/thomaslab-core/search?q=split_allele_copy_number&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return the base star allele and explicit copy count.

``*1`` returns ``('*1', 1)``; ``*1x3`` returns ``('*1', 3)``.
Symbolic copy numbers such as ``xN`` are deliberately unsupported because an
activity score cannot be computed without the actual copy count.

### API inspection

~~~python
import inspect
from thomaslab.pgx_core import split_allele_copy_number

print(inspect.signature(split_allele_copy_number))
print(split_allele_copy_number.__doc__)
~~~

### Source

[`src/thomaslab/pgx_core.py#L52`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_core.py#L52)

---

<!-- callable:thomaslab.pgx_core.normalize_diplotype -->
## normalize_diplotype

### Purpose

Normalize a two-haplotype diplotype string.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def normalize_diplotype(value: object, gene: str | None = None) -> str
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `value` | `value: object` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `gene` | `gene: str \| None = None` | No | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `value`.

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
from thomaslab.pgx_core import normalize_diplotype

result = normalize_diplotype(
    value={"key": "value"}
)

print(result)
~~~

### Related functions

- `normalize_star_allele`
- `split_allele_copy_number`
- `load_allele_function_table`
- `get_allele_function`
- `summarize_diplotype_functions`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_core.py#L71`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_core.py#L71)
- Repository search: [normalize_diplotype](https://github.com/appsplorer/thomaslab-core/search?q=normalize_diplotype&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Normalize a two-haplotype diplotype string.

The function does not infer phase or transform an unresolved genotype into a
diplotype. Inputs must already represent two reported haplotypes.

### API inspection

~~~python
import inspect
from thomaslab.pgx_core import normalize_diplotype

print(inspect.signature(normalize_diplotype))
print(normalize_diplotype.__doc__)
~~~

### Source

[`src/thomaslab/pgx_core.py#L71`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_core.py#L71)

---

<!-- callable:thomaslab.pgx_core.load_allele_function_table -->
## load_allele_function_table

### Purpose

Load a versioned allele-function table from YAML/CSV/DataFrame/mapping.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def load_allele_function_table( source: str | Path | pd.DataFrame | Mapping[str, Any], ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `source` | `source: str \| Path \| pd.DataFrame \| Mapping[str, Any]` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `source`.

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

from thomaslab.pgx_core import load_allele_function_table

result = load_allele_function_table(
    source=sample_df
)

print(result)
~~~

### Related functions

- `normalize_star_allele`
- `split_allele_copy_number`
- `normalize_diplotype`
- `get_allele_function`
- `summarize_diplotype_functions`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_core.py#L88`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_core.py#L88)
- Repository search: [load_allele_function_table](https://github.com/appsplorer/thomaslab-core/search?q=load_allele_function_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Load a versioned allele-function table from YAML/CSV/DataFrame/mapping.

Required columns are ``gene``, ``allele`` and ``function``. ``activity_value``
is optional for genes that use an activity-score system.

### API inspection

~~~python
import inspect
from thomaslab.pgx_core import load_allele_function_table

print(inspect.signature(load_allele_function_table))
print(load_allele_function_table.__doc__)
~~~

### Source

[`src/thomaslab/pgx_core.py#L88`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_core.py#L88)

---

<!-- callable:thomaslab.pgx_core.get_allele_function -->
## get_allele_function

### Purpose

Resolve one allele against an explicit function table.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def get_allele_function( allele: object, gene: str, function_table: pd.DataFrame, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `allele` | `allele: object` | Yes | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |
| `gene` | `gene: str` | Yes | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |
| `function_table` | `function_table: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `allele`, `gene`, `function_table`.

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

from thomaslab.pgx_core import get_allele_function

result = get_allele_function(
    allele="*1",
    gene="CYP2C19",
    function_table=sample_df
)

print(result)
~~~

### Related functions

- `normalize_star_allele`
- `split_allele_copy_number`
- `normalize_diplotype`
- `load_allele_function_table`
- `summarize_diplotype_functions`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_core.py#L138`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_core.py#L138)
- Repository search: [get_allele_function](https://github.com/appsplorer/thomaslab-core/search?q=get_allele_function&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Resolve one allele against an explicit function table.

### API inspection

~~~python
import inspect
from thomaslab.pgx_core import get_allele_function

print(inspect.signature(get_allele_function))
print(get_allele_function.__doc__)
~~~

### Source

[`src/thomaslab/pgx_core.py#L138`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_core.py#L138)

---

<!-- callable:thomaslab.pgx_core.summarize_diplotype_functions -->
## summarize_diplotype_functions

### Purpose

Resolve both reported haplotypes and retain copy-number metadata.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_diplotype_functions( diplotype: object, gene: str, function_table: pd.DataFrame, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `diplotype` | `diplotype: object` | Yes | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |
| `gene` | `gene: str` | Yes | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |
| `function_table` | `function_table: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `diplotype`, `gene`, `function_table`.

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

from thomaslab.pgx_core import summarize_diplotype_functions

result = summarize_diplotype_functions(
    diplotype="*1/*2",
    gene="CYP2C19",
    function_table=sample_df
)

print(result)
~~~

### Related functions

- `normalize_star_allele`
- `split_allele_copy_number`
- `normalize_diplotype`
- `load_allele_function_table`
- `get_allele_function`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_core.py#L168`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_core.py#L168)
- Repository search: [summarize_diplotype_functions](https://github.com/appsplorer/thomaslab-core/search?q=summarize_diplotype_functions&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Resolve both reported haplotypes and retain copy-number metadata.

### API inspection

~~~python
import inspect
from thomaslab.pgx_core import summarize_diplotype_functions

print(inspect.signature(summarize_diplotype_functions))
print(summarize_diplotype_functions.__doc__)
~~~

### Source

[`src/thomaslab/pgx_core.py#L168`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_core.py#L168)

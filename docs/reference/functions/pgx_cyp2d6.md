# thomaslab.pgx_cyp2d6

CYP2D6 activity-score and phenotype translation utilities.

## Research-use boundary

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

## Self-service orientation

- Related guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 5

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.pgx_cyp2d6.cyp2d6_activity_to_phenotype -->
## cyp2d6_activity_to_phenotype

### Purpose

Translate CYP2D6 activity score using the current standardized thresholds.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def cyp2d6_activity_to_phenotype(activity_score: float | int) -> str
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `activity_score` | `activity_score: float \| int` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `activity_score`.

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
from thomaslab.pgx_cyp2d6 import cyp2d6_activity_to_phenotype

result = cyp2d6_activity_to_phenotype(
    activity_score=2
)

print(result)
~~~

### Related functions

- `calculate_cyp2d6_activity_score`
- `assign_cyp2d6_phenotype`
- `translate_cyp2d6_diplotype`
- `translate_cyp2d6_table`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_cyp2d6.py#L69`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2d6.py#L69)
- Repository search: [cyp2d6_activity_to_phenotype](https://github.com/appsplorer/thomaslab-core/search?q=cyp2d6_activity_to_phenotype&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Translate CYP2D6 activity score using the current standardized thresholds.

### API inspection

~~~python
import inspect
from thomaslab.pgx_cyp2d6 import cyp2d6_activity_to_phenotype

print(inspect.signature(cyp2d6_activity_to_phenotype))
print(cyp2d6_activity_to_phenotype.__doc__)
~~~

### Source

[`src/thomaslab/pgx_cyp2d6.py#L69`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2d6.py#L69)

---

<!-- callable:thomaslab.pgx_cyp2d6.calculate_cyp2d6_activity_score -->
## calculate_cyp2d6_activity_score

### Purpose

Calculate CYP2D6 activity score with explicit allele copy-number support.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_cyp2d6_activity_score( diplotype: object, function_table: pd.DataFrame | None = None, ) -> float | None
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

`float | None`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.pgx_cyp2d6 import calculate_cyp2d6_activity_score

result = calculate_cyp2d6_activity_score(
    diplotype="*1/*2"
)

print(result)
~~~

### Related functions

- `cyp2d6_activity_to_phenotype`
- `assign_cyp2d6_phenotype`
- `translate_cyp2d6_diplotype`
- `translate_cyp2d6_table`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_cyp2d6.py#L83`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2d6.py#L83)
- Repository search: [calculate_cyp2d6_activity_score](https://github.com/appsplorer/thomaslab-core/search?q=calculate_cyp2d6_activity_score&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate CYP2D6 activity score with explicit allele copy-number support.

Unknown or uncertain allele function returns ``None``. Structural variants that
cannot be represented as a resolved star allele plus numeric copy count must be
called upstream by a validated CYP2D6 caller.

### API inspection

~~~python
import inspect
from thomaslab.pgx_cyp2d6 import calculate_cyp2d6_activity_score

print(inspect.signature(calculate_cyp2d6_activity_score))
print(calculate_cyp2d6_activity_score.__doc__)
~~~

### Source

[`src/thomaslab/pgx_cyp2d6.py#L83`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2d6.py#L83)

---

<!-- callable:thomaslab.pgx_cyp2d6.assign_cyp2d6_phenotype -->
## assign_cyp2d6_phenotype

### Purpose

Translate a CYP2D6 diplotype to phenotype, returning Indeterminate/Unknown safely.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def assign_cyp2d6_phenotype( diplotype: object, function_table: pd.DataFrame | None = None, ) -> str
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
from thomaslab.pgx_cyp2d6 import assign_cyp2d6_phenotype

result = assign_cyp2d6_phenotype(
    diplotype="*1/*2"
)

print(result)
~~~

### Related functions

- `cyp2d6_activity_to_phenotype`
- `calculate_cyp2d6_activity_score`
- `translate_cyp2d6_diplotype`
- `translate_cyp2d6_table`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_cyp2d6.py#L107`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2d6.py#L107)
- Repository search: [assign_cyp2d6_phenotype](https://github.com/appsplorer/thomaslab-core/search?q=assign_cyp2d6_phenotype&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Translate a CYP2D6 diplotype to phenotype, returning Indeterminate/Unknown safely.

### API inspection

~~~python
import inspect
from thomaslab.pgx_cyp2d6 import assign_cyp2d6_phenotype

print(inspect.signature(assign_cyp2d6_phenotype))
print(assign_cyp2d6_phenotype.__doc__)
~~~

### Source

[`src/thomaslab/pgx_cyp2d6.py#L107`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2d6.py#L107)

---

<!-- callable:thomaslab.pgx_cyp2d6.translate_cyp2d6_diplotype -->
## translate_cyp2d6_diplotype

### Purpose

Return normalized CYP2D6 diplotype, activity score and phenotype metadata.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def translate_cyp2d6_diplotype( diplotype: object, function_table: pd.DataFrame | None = None, ) -> dict[str, Any]
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
from thomaslab.pgx_cyp2d6 import translate_cyp2d6_diplotype

result = translate_cyp2d6_diplotype(
    diplotype="*1/*2"
)

print(result)
~~~

### Related functions

- `cyp2d6_activity_to_phenotype`
- `calculate_cyp2d6_activity_score`
- `assign_cyp2d6_phenotype`
- `translate_cyp2d6_table`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_cyp2d6.py#L122`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2d6.py#L122)
- Repository search: [translate_cyp2d6_diplotype](https://github.com/appsplorer/thomaslab-core/search?q=translate_cyp2d6_diplotype&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return normalized CYP2D6 diplotype, activity score and phenotype metadata.

### API inspection

~~~python
import inspect
from thomaslab.pgx_cyp2d6 import translate_cyp2d6_diplotype

print(inspect.signature(translate_cyp2d6_diplotype))
print(translate_cyp2d6_diplotype.__doc__)
~~~

### Source

[`src/thomaslab/pgx_cyp2d6.py#L122`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2d6.py#L122)

---

<!-- callable:thomaslab.pgx_cyp2d6.translate_cyp2d6_table -->
## translate_cyp2d6_table

### Purpose

Batch-translate CYP2D6 diplotypes while preserving the input index.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def translate_cyp2d6_table( df: pd.DataFrame, *, diplotype_col: str, function_table: pd.DataFrame | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `diplotype_col` | `diplotype_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `function_table` | `function_table: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `diplotype_col`.
- Referenced columns must exist in the input table: `diplotype_col`.

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

from thomaslab.pgx_cyp2d6 import translate_cyp2d6_table

result = translate_cyp2d6_table(
    df=sample_df,
    diplotype_col='diplotype'
)

print(result)
~~~

### Related functions

- `cyp2d6_activity_to_phenotype`
- `calculate_cyp2d6_activity_score`
- `assign_cyp2d6_phenotype`
- `translate_cyp2d6_diplotype`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_cyp2d6.py#L144`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2d6.py#L144)
- Repository search: [translate_cyp2d6_table](https://github.com/appsplorer/thomaslab-core/search?q=translate_cyp2d6_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Batch-translate CYP2D6 diplotypes while preserving the input index.

### API inspection

~~~python
import inspect
from thomaslab.pgx_cyp2d6 import translate_cyp2d6_table

print(inspect.signature(translate_cyp2d6_table))
print(translate_cyp2d6_table.__doc__)
~~~

### Source

[`src/thomaslab/pgx_cyp2d6.py#L144`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_cyp2d6.py#L144)

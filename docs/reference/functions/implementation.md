# thomaslab.implementation

Pharmacogenomics implementation-science metrics.

These utilities quantify testing, turnaround, actionability, concordance and adoption
for retrospective or implementation research. They do not issue clinical decisions.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 13

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.implementation.calculate_test_order_rate -->
## calculate_test_order_rate

### Purpose

Calculate PGx test ordering among study-defined eligible patients.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_test_order_rate( df: pd.DataFrame, *, eligible_col: str, ordered_col: str, ) -> dict[str, float | int]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `eligible_col` | `eligible_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `ordered_col` | `ordered_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `eligible_col`, `ordered_col`.
- Referenced columns must exist in the input table: `eligible_col`, `ordered_col`.

### Returns

`dict[str, float | int]`

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

from thomaslab.implementation import calculate_test_order_rate

result = calculate_test_order_rate(
    df=sample_df,
    eligible_col='eligible',
    ordered_col='ordered'
)

print(result)
~~~

### Related functions

- `calculate_test_completion_rate`
- `calculate_genotype_turnaround_time`
- `summarize_turnaround_time`
- `calculate_result_before_prescribing_rate`
- `calculate_actionable_genotype_rate`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/implementation.py#L26`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L26)
- Repository search: [calculate_test_order_rate](https://github.com/appsplorer/thomaslab-core/search?q=calculate_test_order_rate&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate PGx test ordering among study-defined eligible patients.

### API inspection

~~~python
import inspect
from thomaslab.implementation import calculate_test_order_rate

print(inspect.signature(calculate_test_order_rate))
print(calculate_test_order_rate.__doc__)
~~~

### Source

[`src/thomaslab/implementation.py#L26`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L26)

---

<!-- callable:thomaslab.implementation.calculate_test_completion_rate -->
## calculate_test_completion_rate

### Purpose

Calculate completed results among ordered tests.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_test_completion_rate( df: pd.DataFrame, *, ordered_col: str, completed_col: str, ) -> dict[str, float | int]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `ordered_col` | `ordered_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `completed_col` | `completed_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `ordered_col`, `completed_col`.
- Referenced columns must exist in the input table: `ordered_col`, `completed_col`.

### Returns

`dict[str, float | int]`

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

from thomaslab.implementation import calculate_test_completion_rate

result = calculate_test_completion_rate(
    df=sample_df,
    ordered_col='ordered',
    completed_col='completed'
)

print(result)
~~~

### Related functions

- `calculate_test_order_rate`
- `calculate_genotype_turnaround_time`
- `summarize_turnaround_time`
- `calculate_result_before_prescribing_rate`
- `calculate_actionable_genotype_rate`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/implementation.py#L45`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L45)
- Repository search: [calculate_test_completion_rate](https://github.com/appsplorer/thomaslab-core/search?q=calculate_test_completion_rate&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate completed results among ordered tests.

### API inspection

~~~python
import inspect
from thomaslab.implementation import calculate_test_completion_rate

print(inspect.signature(calculate_test_completion_rate))
print(calculate_test_completion_rate.__doc__)
~~~

### Source

[`src/thomaslab/implementation.py#L45`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L45)

---

<!-- callable:thomaslab.implementation.calculate_genotype_turnaround_time -->
## calculate_genotype_turnaround_time

### Purpose

Calculate non-negative order-to-result turnaround time in days.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_genotype_turnaround_time( df: pd.DataFrame, *, order_date_col: str, result_date_col: str, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `order_date_col` | `order_date_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `result_date_col` | `result_date_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `order_date_col`, `result_date_col`.
- Referenced columns must exist in the input table: `order_date_col`, `result_date_col`.

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

from thomaslab.implementation import calculate_genotype_turnaround_time

result = calculate_genotype_turnaround_time(
    df=sample_df,
    order_date_col='order_date',
    result_date_col='result_date'
)

print(result)
~~~

### Related functions

- `calculate_test_order_rate`
- `calculate_test_completion_rate`
- `summarize_turnaround_time`
- `calculate_result_before_prescribing_rate`
- `calculate_actionable_genotype_rate`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/implementation.py#L64`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L64)
- Repository search: [calculate_genotype_turnaround_time](https://github.com/appsplorer/thomaslab-core/search?q=calculate_genotype_turnaround_time&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate non-negative order-to-result turnaround time in days.

### API inspection

~~~python
import inspect
from thomaslab.implementation import calculate_genotype_turnaround_time

print(inspect.signature(calculate_genotype_turnaround_time))
print(calculate_genotype_turnaround_time.__doc__)
~~~

### Source

[`src/thomaslab/implementation.py#L64`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L64)

---

<!-- callable:thomaslab.implementation.summarize_turnaround_time -->
## summarize_turnaround_time

### Purpose

Summarize valid turnaround times.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_turnaround_time(turnaround: pd.DataFrame) -> dict[str, float | int]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `turnaround` | `turnaround: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `turnaround`.

### Returns

`dict[str, float | int]`

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

from thomaslab.implementation import summarize_turnaround_time

result = summarize_turnaround_time(
    turnaround=sample_df
)

print(result)
~~~

### Related functions

- `calculate_test_order_rate`
- `calculate_test_completion_rate`
- `calculate_genotype_turnaround_time`
- `calculate_result_before_prescribing_rate`
- `calculate_actionable_genotype_rate`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/implementation.py#L82`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L82)
- Repository search: [summarize_turnaround_time](https://github.com/appsplorer/thomaslab-core/search?q=summarize_turnaround_time&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize valid turnaround times.

### API inspection

~~~python
import inspect
from thomaslab.implementation import summarize_turnaround_time

print(inspect.signature(summarize_turnaround_time))
print(summarize_turnaround_time.__doc__)
~~~

### Source

[`src/thomaslab/implementation.py#L82`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L82)

---

<!-- callable:thomaslab.implementation.calculate_result_before_prescribing_rate -->
## calculate_result_before_prescribing_rate

### Purpose

Calculate how often a PGx result was available on/before prescribing.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_result_before_prescribing_rate( df: pd.DataFrame, *, result_date_col: str, prescribing_date_col: str, ) -> dict[str, float | int]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `result_date_col` | `result_date_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `prescribing_date_col` | `prescribing_date_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `result_date_col`, `prescribing_date_col`.
- Referenced columns must exist in the input table: `result_date_col`, `prescribing_date_col`.

### Returns

`dict[str, float | int]`

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

from thomaslab.implementation import calculate_result_before_prescribing_rate

result = calculate_result_before_prescribing_rate(
    df=sample_df,
    result_date_col='result_date',
    prescribing_date_col='prescribing_date'
)

print(result)
~~~

### Related functions

- `calculate_test_order_rate`
- `calculate_test_completion_rate`
- `calculate_genotype_turnaround_time`
- `summarize_turnaround_time`
- `calculate_actionable_genotype_rate`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/implementation.py#L98`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L98)
- Repository search: [calculate_result_before_prescribing_rate](https://github.com/appsplorer/thomaslab-core/search?q=calculate_result_before_prescribing_rate&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate how often a PGx result was available on/before prescribing.

### API inspection

~~~python
import inspect
from thomaslab.implementation import calculate_result_before_prescribing_rate

print(inspect.signature(calculate_result_before_prescribing_rate))
print(calculate_result_before_prescribing_rate.__doc__)
~~~

### Source

[`src/thomaslab/implementation.py#L98`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L98)

---

<!-- callable:thomaslab.implementation.calculate_actionable_genotype_rate -->
## calculate_actionable_genotype_rate

### Purpose

Calculate frequency of a study-defined actionable phenotype set.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_actionable_genotype_rate( df: pd.DataFrame, *, phenotype_col: str, actionable_phenotypes: Iterable[object], ) -> dict[str, float | int]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `phenotype_col` | `phenotype_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `actionable_phenotypes` | `actionable_phenotypes: Iterable[object]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `phenotype_col`, `actionable_phenotypes`.
- Referenced columns must exist in the input table: `phenotype_col`.

### Returns

`dict[str, float | int]`

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

sample_value = "replace_with_validated_value"

from thomaslab.implementation import calculate_actionable_genotype_rate

result = calculate_actionable_genotype_rate(
    df=sample_df,
    phenotype_col='phenotype',
    actionable_phenotypes=sample_value
)

print(result)
~~~

### Related functions

- `calculate_test_order_rate`
- `calculate_test_completion_rate`
- `calculate_genotype_turnaround_time`
- `summarize_turnaround_time`
- `calculate_result_before_prescribing_rate`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/implementation.py#L119`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L119)
- Repository search: [calculate_actionable_genotype_rate](https://github.com/appsplorer/thomaslab-core/search?q=calculate_actionable_genotype_rate&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate frequency of a study-defined actionable phenotype set.

### API inspection

~~~python
import inspect
from thomaslab.implementation import calculate_actionable_genotype_rate

print(inspect.signature(calculate_actionable_genotype_rate))
print(calculate_actionable_genotype_rate.__doc__)
~~~

### Source

[`src/thomaslab/implementation.py#L119`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L119)

---

<!-- callable:thomaslab.implementation.calculate_recommendation_acceptance -->
## calculate_recommendation_acceptance

### Purpose

Calculate acceptance among rows with a study-defined recommendation.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_recommendation_acceptance( df: pd.DataFrame, *, recommended_col: str, accepted_col: str, ) -> dict[str, float | int]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `recommended_col` | `recommended_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `accepted_col` | `accepted_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `recommended_col`, `accepted_col`.
- Referenced columns must exist in the input table: `recommended_col`, `accepted_col`.

### Returns

`dict[str, float | int]`

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

from thomaslab.implementation import calculate_recommendation_acceptance

result = calculate_recommendation_acceptance(
    df=sample_df,
    recommended_col='recommended',
    accepted_col='accepted'
)

print(result)
~~~

### Related functions

- `calculate_test_order_rate`
- `calculate_test_completion_rate`
- `calculate_genotype_turnaround_time`
- `summarize_turnaround_time`
- `calculate_result_before_prescribing_rate`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/implementation.py#L140`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L140)
- Repository search: [calculate_recommendation_acceptance](https://github.com/appsplorer/thomaslab-core/search?q=calculate_recommendation_acceptance&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate acceptance among rows with a study-defined recommendation.

### API inspection

~~~python
import inspect
from thomaslab.implementation import calculate_recommendation_acceptance

print(inspect.signature(calculate_recommendation_acceptance))
print(calculate_recommendation_acceptance.__doc__)
~~~

### Source

[`src/thomaslab/implementation.py#L140`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L140)

---

<!-- callable:thomaslab.implementation.calculate_guideline_concordance_rate -->
## calculate_guideline_concordance_rate

### Purpose

Summarize an explicit research-concordance table.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_guideline_concordance_rate( concordance: pd.DataFrame, *, concordant_col: str = "concordant", status_col: str | None = "status", ) -> dict[str, float | int]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `concordance` | `concordance: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `concordant_col` | `concordant_col: str = 'concordant'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `status_col` | `status_col: str \| None = 'status'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `concordance`.
- Referenced columns must exist in the input table: `concordant_col`, `status_col`.

### Returns

`dict[str, float | int]`

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

from thomaslab.implementation import calculate_guideline_concordance_rate

result = calculate_guideline_concordance_rate(
    concordance=sample_df
)

print(result)
~~~

### Related functions

- `calculate_test_order_rate`
- `calculate_test_completion_rate`
- `calculate_genotype_turnaround_time`
- `summarize_turnaround_time`
- `calculate_result_before_prescribing_rate`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/implementation.py#L155`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L155)
- Repository search: [calculate_guideline_concordance_rate](https://github.com/appsplorer/thomaslab-core/search?q=calculate_guideline_concordance_rate&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize an explicit research-concordance table.

### API inspection

~~~python
import inspect
from thomaslab.implementation import calculate_guideline_concordance_rate

print(inspect.signature(calculate_guideline_concordance_rate))
print(calculate_guideline_concordance_rate.__doc__)
~~~

### Source

[`src/thomaslab/implementation.py#L155`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L155)

---

<!-- callable:thomaslab.implementation.calculate_provider_adoption -->
## calculate_provider_adoption

### Purpose

Calculate study-defined PGx adoption rates by provider.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_provider_adoption( df: pd.DataFrame, *, provider_col: str, eligible_col: str, adopted_col: str, min_eligible: int = 1, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `provider_col` | `provider_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `eligible_col` | `eligible_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `adopted_col` | `adopted_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `min_eligible` | `min_eligible: int = 1` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `provider_col`, `eligible_col`, `adopted_col`.
- Referenced columns must exist in the input table: `provider_col`, `eligible_col`, `adopted_col`.

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

from thomaslab.implementation import calculate_provider_adoption

result = calculate_provider_adoption(
    df=sample_df,
    provider_col='provider',
    eligible_col='eligible',
    adopted_col='adopted'
)

print(result)
~~~

### Related functions

- `calculate_test_order_rate`
- `calculate_test_completion_rate`
- `calculate_genotype_turnaround_time`
- `summarize_turnaround_time`
- `calculate_result_before_prescribing_rate`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/implementation.py#L177`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L177)
- Repository search: [calculate_provider_adoption](https://github.com/appsplorer/thomaslab-core/search?q=calculate_provider_adoption&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate study-defined PGx adoption rates by provider.

### API inspection

~~~python
import inspect
from thomaslab.implementation import calculate_provider_adoption

print(inspect.signature(calculate_provider_adoption))
print(calculate_provider_adoption.__doc__)
~~~

### Source

[`src/thomaslab/implementation.py#L177`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L177)

---

<!-- callable:thomaslab.implementation.calculate_pgx_eligible_population -->
## calculate_pgx_eligible_population

### Purpose

Summarize unique patient eligibility.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_pgx_eligible_population( df: pd.DataFrame, *, eligibility_col: str, patient_col: str = "patient_id", ) -> dict[str, float | int]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `eligibility_col` | `eligibility_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `eligibility_col`.
- Referenced columns must exist in the input table: `eligibility_col`, `patient_col`.

### Returns

`dict[str, float | int]`

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

from thomaslab.implementation import calculate_pgx_eligible_population

result = calculate_pgx_eligible_population(
    df=sample_df,
    eligibility_col='eligibility'
)

print(result)
~~~

### Related functions

- `calculate_test_order_rate`
- `calculate_test_completion_rate`
- `calculate_genotype_turnaround_time`
- `summarize_turnaround_time`
- `calculate_result_before_prescribing_rate`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/implementation.py#L209`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L209)
- Repository search: [calculate_pgx_eligible_population](https://github.com/appsplorer/thomaslab-core/search?q=calculate_pgx_eligible_population&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize unique patient eligibility.

### API inspection

~~~python
import inspect
from thomaslab.implementation import calculate_pgx_eligible_population

print(inspect.signature(calculate_pgx_eligible_population))
print(calculate_pgx_eligible_population.__doc__)
~~~

### Source

[`src/thomaslab/implementation.py#L209`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L209)

---

<!-- callable:thomaslab.implementation.calculate_number_needed_to_genotype -->
## calculate_number_needed_to_genotype

### Purpose

Return 1/actionable_rate as a descriptive implementation metric.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_number_needed_to_genotype( *, actionable_rate: float, ) -> float
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `actionable_rate` | `actionable_rate: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `actionable_rate`.

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
from thomaslab.implementation import calculate_number_needed_to_genotype

result = calculate_number_needed_to_genotype(
    actionable_rate=0.5
)

print(result)
~~~

### Related functions

- `calculate_test_order_rate`
- `calculate_test_completion_rate`
- `calculate_genotype_turnaround_time`
- `summarize_turnaround_time`
- `calculate_result_before_prescribing_rate`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/implementation.py#L228`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L228)
- Repository search: [calculate_number_needed_to_genotype](https://github.com/appsplorer/thomaslab-core/search?q=calculate_number_needed_to_genotype&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return 1/actionable_rate as a descriptive implementation metric.

### API inspection

~~~python
import inspect
from thomaslab.implementation import calculate_number_needed_to_genotype

print(inspect.signature(calculate_number_needed_to_genotype))
print(calculate_number_needed_to_genotype.__doc__)
~~~

### Source

[`src/thomaslab/implementation.py#L228`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L228)

---

<!-- callable:thomaslab.implementation.build_pgx_implementation_funnel -->
## build_pgx_implementation_funnel

### Purpose

Build sequential implementation counts with explicit denominators.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_pgx_implementation_funnel( df: pd.DataFrame, *, eligible_col: str, ordered_col: str, completed_col: str, actionable_col: str | None = None, acted_on_col: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `eligible_col` | `eligible_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `ordered_col` | `ordered_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `completed_col` | `completed_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `actionable_col` | `actionable_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `acted_on_col` | `acted_on_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `eligible_col`, `ordered_col`, `completed_col`.
- Referenced columns must exist in the input table: `eligible_col`, `ordered_col`, `completed_col`, `actionable_col`, `acted_on_col`.

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

from thomaslab.implementation import build_pgx_implementation_funnel

result = build_pgx_implementation_funnel(
    df=sample_df,
    eligible_col='eligible',
    ordered_col='ordered',
    completed_col='completed'
)

print(result)
~~~

### Related functions

- `calculate_test_order_rate`
- `calculate_test_completion_rate`
- `calculate_genotype_turnaround_time`
- `summarize_turnaround_time`
- `calculate_result_before_prescribing_rate`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/implementation.py#L239`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L239)
- Repository search: [build_pgx_implementation_funnel](https://github.com/appsplorer/thomaslab-core/search?q=build_pgx_implementation_funnel&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build sequential implementation counts with explicit denominators.

### API inspection

~~~python
import inspect
from thomaslab.implementation import build_pgx_implementation_funnel

print(inspect.signature(build_pgx_implementation_funnel))
print(build_pgx_implementation_funnel.__doc__)
~~~

### Source

[`src/thomaslab/implementation.py#L239`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L239)

---

<!-- callable:thomaslab.implementation.audit_implementation_pipeline -->
## audit_implementation_pipeline

### Purpose

Return key integrity and implementation metrics in one audit dictionary.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_implementation_pipeline( df: pd.DataFrame, *, eligible_col: str, ordered_col: str, completed_col: str, order_date_col: str | None = None, result_date_col: str | None = None, prescribing_date_col: str | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `eligible_col` | `eligible_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `ordered_col` | `ordered_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `completed_col` | `completed_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `order_date_col` | `order_date_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `result_date_col` | `result_date_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `prescribing_date_col` | `prescribing_date_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `eligible_col`, `ordered_col`, `completed_col`.
- Referenced columns must exist in the input table: `eligible_col`, `ordered_col`, `completed_col`, `order_date_col`, `result_date_col`, `prescribing_date_col`.

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

from thomaslab.implementation import audit_implementation_pipeline

result = audit_implementation_pipeline(
    df=sample_df,
    eligible_col='eligible',
    ordered_col='ordered',
    completed_col='completed'
)

print(result)
~~~

### Related functions

- `calculate_test_order_rate`
- `calculate_test_completion_rate`
- `calculate_genotype_turnaround_time`
- `summarize_turnaround_time`
- `calculate_result_before_prescribing_rate`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/implementation.py#L284`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L284)
- Repository search: [audit_implementation_pipeline](https://github.com/appsplorer/thomaslab-core/search?q=audit_implementation_pipeline&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return key integrity and implementation metrics in one audit dictionary.

### API inspection

~~~python
import inspect
from thomaslab.implementation import audit_implementation_pipeline

print(inspect.signature(audit_implementation_pipeline))
print(audit_implementation_pipeline.__doc__)
~~~

### Source

[`src/thomaslab/implementation.py#L284`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/implementation.py#L284)

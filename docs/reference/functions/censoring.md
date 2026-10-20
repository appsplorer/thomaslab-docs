# thomaslab.censoring

Right-censoring summaries and marginal IPCW diagnostics.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 6

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.censoring.estimate_censoring_survival -->
## estimate_censoring_survival

### Purpose

Estimate marginal censoring survival G(t) with Kaplan–Meier recursion.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def estimate_censoring_survival( df: pd.DataFrame, *, time_col: str, event_col: str, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `time_col`, `event_col`.
- Referenced columns must exist in the input table: `time_col`, `event_col`.

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

from thomaslab.censoring import estimate_censoring_survival

result = estimate_censoring_survival(
    df=sample_df,
    time_col='event_date',
    event_col='event'
)

print(result)
~~~

### Related functions

- `calculate_marginal_ipcw`
- `truncate_ipcw`
- `audit_ipcw`
- `summarize_censoring`
- `censoring_covariate_smd`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/censoring.py#L17`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/censoring.py#L17)
- Repository search: [estimate_censoring_survival](https://github.com/appsplorer/thomaslab-core/search?q=estimate_censoring_survival&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate marginal censoring survival G(t) with Kaplan–Meier recursion.

``event_col=1`` denotes the clinical event, so censoring is ``1-event``.

### API inspection

~~~python
import inspect
from thomaslab.censoring import estimate_censoring_survival

print(inspect.signature(estimate_censoring_survival))
print(estimate_censoring_survival.__doc__)
~~~

### Source

[`src/thomaslab/censoring.py#L17`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/censoring.py#L17)

---

<!-- callable:thomaslab.censoring.calculate_marginal_ipcw -->
## calculate_marginal_ipcw

### Purpose

Calculate simple marginal inverse-probability-of-censoring weights.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_marginal_ipcw( df: pd.DataFrame, *, time_col: str, event_col: str, minimum_survival: float = 0.01, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `minimum_survival` | `minimum_survival: float = 0.01` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `time_col`, `event_col`.
- Referenced columns must exist in the input table: `time_col`, `event_col`.

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

from thomaslab.censoring import calculate_marginal_ipcw

result = calculate_marginal_ipcw(
    df=sample_df,
    time_col='event_date',
    event_col='event'
)

print(result)
~~~

### Related functions

- `estimate_censoring_survival`
- `truncate_ipcw`
- `audit_ipcw`
- `summarize_censoring`
- `censoring_covariate_smd`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/censoring.py#L56`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/censoring.py#L56)
- Repository search: [calculate_marginal_ipcw](https://github.com/appsplorer/thomaslab-core/search?q=calculate_marginal_ipcw&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate simple marginal inverse-probability-of-censoring weights.

Each row receives ``1/G(T-)`` using the marginal censoring KM. This is a
diagnostic/research utility, not a substitute for a covariate-dependent
censoring model when censoring depends on patient characteristics.

### API inspection

~~~python
import inspect
from thomaslab.censoring import calculate_marginal_ipcw

print(inspect.signature(calculate_marginal_ipcw))
print(calculate_marginal_ipcw.__doc__)
~~~

### Source

[`src/thomaslab/censoring.py#L56`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/censoring.py#L56)

---

<!-- callable:thomaslab.censoring.truncate_ipcw -->
## truncate_ipcw

### Purpose

Winsorize positive IPCW values at explicit empirical quantiles.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def truncate_ipcw( weights: pd.Series | Sequence[float], *, lower_quantile: float = 0.01, upper_quantile: float = 0.99, ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `weights` | `weights: pd.Series \| Sequence[float]` | Yes | Analysis weight/propensity input. Inspect support, positivity, extremes, and effective sample size where applicable. |
| `lower_quantile` | `lower_quantile: float = 0.01` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `upper_quantile` | `upper_quantile: float = 0.99` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `weights`.

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

from thomaslab.censoring import truncate_ipcw

result = truncate_ipcw(
    weights=sample_series
)

print(result)
~~~

### Related functions

- `estimate_censoring_survival`
- `calculate_marginal_ipcw`
- `audit_ipcw`
- `summarize_censoring`
- `censoring_covariate_smd`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/censoring.py#L88`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/censoring.py#L88)
- Repository search: [truncate_ipcw](https://github.com/appsplorer/thomaslab-core/search?q=truncate_ipcw&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Winsorize positive IPCW values at explicit empirical quantiles.

### API inspection

~~~python
import inspect
from thomaslab.censoring import truncate_ipcw

print(inspect.signature(truncate_ipcw))
print(truncate_ipcw.__doc__)
~~~

### Source

[`src/thomaslab/censoring.py#L88`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/censoring.py#L88)

---

<!-- callable:thomaslab.censoring.audit_ipcw -->
## audit_ipcw

### Purpose

Summarize IPCW instability and effective sample size.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_ipcw( weights: pd.Series | Sequence[float], *, extreme_threshold: float = 10.0, ) -> dict[str, float | int]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `weights` | `weights: pd.Series \| Sequence[float]` | Yes | Analysis weight/propensity input. Inspect support, positivity, extremes, and effective sample size where applicable. |
| `extreme_threshold` | `extreme_threshold: float = 10.0` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `weights`.

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

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.censoring import audit_ipcw

result = audit_ipcw(
    weights=sample_series
)

print(result)
~~~

### Related functions

- `estimate_censoring_survival`
- `calculate_marginal_ipcw`
- `truncate_ipcw`
- `summarize_censoring`
- `censoring_covariate_smd`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/censoring.py#L104`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/censoring.py#L104)
- Repository search: [audit_ipcw](https://github.com/appsplorer/thomaslab-core/search?q=audit_ipcw&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize IPCW instability and effective sample size.

### API inspection

~~~python
import inspect
from thomaslab.censoring import audit_ipcw

print(inspect.signature(audit_ipcw))
print(audit_ipcw.__doc__)
~~~

### Source

[`src/thomaslab/censoring.py#L104`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/censoring.py#L104)

---

<!-- callable:thomaslab.censoring.summarize_censoring -->
## summarize_censoring

### Purpose

Summarize censoring frequency, optionally by group and recorded reason.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_censoring( df: pd.DataFrame, *, event_col: str, reason_col: str | None = None, group_col: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `event_col` | `event_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `reason_col` | `reason_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `group_col` | `group_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `event_col`.
- Referenced columns must exist in the input table: `event_col`, `reason_col`, `group_col`.

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

from thomaslab.censoring import summarize_censoring

result = summarize_censoring(
    df=sample_df,
    event_col='event'
)

print(result)
~~~

### Related functions

- `estimate_censoring_survival`
- `calculate_marginal_ipcw`
- `truncate_ipcw`
- `audit_ipcw`
- `censoring_covariate_smd`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/censoring.py#L129`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/censoring.py#L129)
- Repository search: [summarize_censoring](https://github.com/appsplorer/thomaslab-core/search?q=summarize_censoring&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize censoring frequency, optionally by group and recorded reason.

### API inspection

~~~python
import inspect
from thomaslab.censoring import summarize_censoring

print(inspect.signature(summarize_censoring))
print(summarize_censoring.__doc__)
~~~

### Source

[`src/thomaslab/censoring.py#L129`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/censoring.py#L129)

---

<!-- callable:thomaslab.censoring.censoring_covariate_smd -->
## censoring_covariate_smd

### Purpose

Compute descriptive SMDs comparing censored vs event-observed rows.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def censoring_covariate_smd( df: pd.DataFrame, *, event_col: str, covariates: Sequence[str], ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `event_col` | `event_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `event_col`, `covariates`.
- Referenced columns must exist in the input table: `event_col`.

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

from thomaslab.censoring import censoring_covariate_smd

result = censoring_covariate_smd(
    df=sample_df,
    event_col='event',
    covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `estimate_censoring_survival`
- `calculate_marginal_ipcw`
- `truncate_ipcw`
- `audit_ipcw`
- `summarize_censoring`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/censoring.py#L168`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/censoring.py#L168)
- Repository search: [censoring_covariate_smd](https://github.com/appsplorer/thomaslab-core/search?q=censoring_covariate_smd&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compute descriptive SMDs comparing censored vs event-observed rows.

This is a diagnostic of measured differences; it cannot prove censoring is
non-informative or identify unmeasured determinants of censoring.

### API inspection

~~~python
import inspect
from thomaslab.censoring import censoring_covariate_smd

print(inspect.signature(censoring_covariate_smd))
print(censoring_covariate_smd.__doc__)
~~~

### Source

[`src/thomaslab/censoring.py#L168`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/censoring.py#L168)

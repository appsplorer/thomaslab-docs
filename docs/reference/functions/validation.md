# thomaslab.validation

Site and external-cohort validation reporting for binary prediction models.

## Research-use boundary

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

## Self-service orientation

- Related guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 5

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.validation.calculate_binary_validation_metrics -->
## calculate_binary_validation_metrics

### Purpose

Calculate discrimination, calibration and threshold metrics for one cohort.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_binary_validation_metrics( df: pd.DataFrame, outcome_col: str, probability_col: str, *, threshold: float = 0.5, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `probability_col` | `probability_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `threshold` | `threshold: float = 0.5` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `outcome_col`, `probability_col`.
- Referenced columns must exist in the input table: `outcome_col`, `probability_col`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

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

from thomaslab.validation import calculate_binary_validation_metrics

result = calculate_binary_validation_metrics(
    df=sample_df,
    outcome_col='outcome',
    probability_col='probability'
)

print(result)
~~~

### Related functions

- `bootstrap_metric_interval`
- `site_validation_report`
- `external_validation_report`
- `summarize_validation_gaps`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/validation.py#L43`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/validation.py#L43)
- Repository search: [calculate_binary_validation_metrics](https://github.com/appsplorer/thomaslab-core/search?q=calculate_binary_validation_metrics&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate discrimination, calibration and threshold metrics for one cohort.

### API inspection

~~~python
import inspect
from thomaslab.validation import calculate_binary_validation_metrics

print(inspect.signature(calculate_binary_validation_metrics))
print(calculate_binary_validation_metrics.__doc__)
~~~

### Source

[`src/thomaslab/validation.py#L43`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/validation.py#L43)

---

<!-- callable:thomaslab.validation.bootstrap_metric_interval -->
## bootstrap_metric_interval

### Purpose

Bootstrap a binary-prediction metric within the supplied evaluation cohort.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def bootstrap_metric_interval( df: pd.DataFrame, outcome_col: str, probability_col: str, *, metric: str = "auroc", n_bootstrap: int = 500, alpha: float = 0.05, random_state: int = 42, ) -> dict[str, float | int | str]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `probability_col` | `probability_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `metric` | `metric: str = 'auroc'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `n_bootstrap` | `n_bootstrap: int = 500` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `alpha` | `alpha: float = 0.05` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `outcome_col`, `probability_col`.
- Referenced columns must exist in the input table: `outcome_col`, `probability_col`.

### Returns

`dict[str, float | int | str]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

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

from thomaslab.validation import bootstrap_metric_interval

result = bootstrap_metric_interval(
    df=sample_df,
    outcome_col='outcome',
    probability_col='probability'
)

print(result)
~~~

### Related functions

- `calculate_binary_validation_metrics`
- `site_validation_report`
- `external_validation_report`
- `summarize_validation_gaps`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/validation.py#L80`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/validation.py#L80)
- Repository search: [bootstrap_metric_interval](https://github.com/appsplorer/thomaslab-core/search?q=bootstrap_metric_interval&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Bootstrap a binary-prediction metric within the supplied evaluation cohort.

### API inspection

~~~python
import inspect
from thomaslab.validation import bootstrap_metric_interval

print(inspect.signature(bootstrap_metric_interval))
print(bootstrap_metric_interval.__doc__)
~~~

### Source

[`src/thomaslab/validation.py#L80`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/validation.py#L80)

---

<!-- callable:thomaslab.validation.site_validation_report -->
## site_validation_report

### Purpose

Return pooled and per-site performance without ranking sites.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def site_validation_report( df: pd.DataFrame, outcome_col: str, probability_col: str, site_col: str, *, threshold: float = 0.5, include_pooled: bool = True, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `probability_col` | `probability_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `site_col` | `site_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `threshold` | `threshold: float = 0.5` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |
| `include_pooled` | `include_pooled: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `outcome_col`, `probability_col`, `site_col`.
- Referenced columns must exist in the input table: `outcome_col`, `probability_col`, `site_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

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

from thomaslab.validation import site_validation_report

result = site_validation_report(
    df=sample_df,
    outcome_col='outcome',
    probability_col='probability',
    site_col='site'
)

print(result)
~~~

### Related functions

- `calculate_binary_validation_metrics`
- `bootstrap_metric_interval`
- `external_validation_report`
- `summarize_validation_gaps`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/validation.py#L134`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/validation.py#L134)
- Repository search: [site_validation_report](https://github.com/appsplorer/thomaslab-core/search?q=site_validation_report&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return pooled and per-site performance without ranking sites.

### API inspection

~~~python
import inspect
from thomaslab.validation import site_validation_report

print(inspect.signature(site_validation_report))
print(site_validation_report.__doc__)
~~~

### Source

[`src/thomaslab/validation.py#L134`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/validation.py#L134)

---

<!-- callable:thomaslab.validation.external_validation_report -->
## external_validation_report

### Purpose

Compare derivation and additional evaluation cohorts with provenance labeling.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def external_validation_report( derivation_df: pd.DataFrame, evaluation_df: pd.DataFrame, outcome_col: str, probability_col: str, *, derivation_name: str = "derivation", evaluation_name: str = "evaluation", independent_source: bool = False, threshold: float = 0.5, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `derivation_df` | `derivation_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `evaluation_df` | `evaluation_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `probability_col` | `probability_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `derivation_name` | `derivation_name: str = 'derivation'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `evaluation_name` | `evaluation_name: str = 'evaluation'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `independent_source` | `independent_source: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `threshold` | `threshold: float = 0.5` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `derivation_df`, `evaluation_df`, `outcome_col`, `probability_col`.
- Referenced columns must exist in the input table: `outcome_col`, `probability_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

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

from thomaslab.validation import external_validation_report

result = external_validation_report(
    derivation_df=sample_df,
    evaluation_df=sample_df,
    outcome_col='outcome',
    probability_col='probability'
)

print(result)
~~~

### Related functions

- `calculate_binary_validation_metrics`
- `bootstrap_metric_interval`
- `site_validation_report`
- `summarize_validation_gaps`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/validation.py#L167`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/validation.py#L167)
- Repository search: [external_validation_report](https://github.com/appsplorer/thomaslab-core/search?q=external_validation_report&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compare derivation and additional evaluation cohorts with provenance labeling.

``independent_source=True`` records the user's study-design assertion that the
evaluation data originate from an independent source. The function does not prove
geographic/temporal/external validity by itself.

### API inspection

~~~python
import inspect
from thomaslab.validation import external_validation_report

print(inspect.signature(external_validation_report))
print(external_validation_report.__doc__)
~~~

### Source

[`src/thomaslab/validation.py#L167`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/validation.py#L167)

---

<!-- callable:thomaslab.validation.summarize_validation_gaps -->
## summarize_validation_gaps

### Purpose

Calculate descriptive metric differences versus one named reference cohort.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_validation_gaps( report: pd.DataFrame, *, reference_cohort: str, metrics: tuple[str, ...] = ("auroc", "auprc", "brier", "calibration_slope"), ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `report` | `report: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `reference_cohort` | `reference_cohort: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `metrics` | `metrics: tuple[str, ...] = ('auroc', 'auprc', 'brier', 'calibration_slope')` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `report`, `reference_cohort`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

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

from thomaslab.validation import summarize_validation_gaps

result = summarize_validation_gaps(
    report=sample_df,
    reference_cohort="value"
)

print(result)
~~~

### Related functions

- `calculate_binary_validation_metrics`
- `bootstrap_metric_interval`
- `site_validation_report`
- `external_validation_report`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/validation.py#L208`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/validation.py#L208)
- Repository search: [summarize_validation_gaps](https://github.com/appsplorer/thomaslab-core/search?q=summarize_validation_gaps&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate descriptive metric differences versus one named reference cohort.

### API inspection

~~~python
import inspect
from thomaslab.validation import summarize_validation_gaps

print(inspect.signature(summarize_validation_gaps))
print(summarize_validation_gaps.__doc__)
~~~

### Source

[`src/thomaslab/validation.py#L208`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/validation.py#L208)

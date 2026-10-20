# thomaslab.easy

High-level, collaborator-friendly workflows for common clinical research tasks.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 9

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.easy.load_clinical_table -->
## load_clinical_table

### Purpose

Load clinical tables without silently coercing CSV/TSV codes or IDs.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def load_clinical_table(path: str | Path, **kwargs: Any) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `path` | `path: str \| Path` | Yes | Input source/path accepted by this callable. Keep raw-source provenance and do not overwrite the source. |
| `kwargs` | `**kwargs: Any` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `path`.

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
from thomaslab.easy import load_clinical_table

result = load_clinical_table(
    path="path/to/input.csv"
)

print(result)
~~~

### Related functions

- `quick_cohort_summary`
- `compute_incidence_rate`
- `compute_binary_effect_measures`
- `build_patient_timeline`
- `make_cohort_flow`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/easy.py#L16`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/easy.py#L16)
- Repository search: [load_clinical_table](https://github.com/appsplorer/thomaslab-core/search?q=load_clinical_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Load clinical tables without silently coercing CSV/TSV codes or IDs.

CSV/TSV cells remain text by default, so numeric/date roles must be
validated and explicitly converted before analysis. Providing a ``dtype``
or ``converters`` argument opts into deliberate parsing. Excel numeric
formatting cannot reconstruct leading zeros; code cells must be text.

### API inspection

~~~python
import inspect
from thomaslab.easy import load_clinical_table

print(inspect.signature(load_clinical_table))
print(load_clinical_table.__doc__)
~~~

### Source

[`src/thomaslab/easy.py#L16`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/easy.py#L16)

---

<!-- callable:thomaslab.easy.quick_cohort_summary -->
## quick_cohort_summary

### Purpose

Create a non-technical cohort overview with counts, missingness, and optional outcomes.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def quick_cohort_summary( df: pd.DataFrame, *, outcome_col: str | None = None, group_col: str | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcome_col` | `outcome_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `group_col` | `group_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.
- Referenced columns must exist in the input table: `outcome_col`, `group_col`.

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

from thomaslab.easy import quick_cohort_summary

result = quick_cohort_summary(
    df=sample_df
)

print(result)
~~~

### Related functions

- `load_clinical_table`
- `compute_incidence_rate`
- `compute_binary_effect_measures`
- `build_patient_timeline`
- `make_cohort_flow`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/easy.py#L54`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/easy.py#L54)
- Repository search: [quick_cohort_summary](https://github.com/appsplorer/thomaslab-core/search?q=quick_cohort_summary&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create a non-technical cohort overview with counts, missingness, and optional outcomes.

### API inspection

~~~python
import inspect
from thomaslab.easy import quick_cohort_summary

print(inspect.signature(quick_cohort_summary))
print(quick_cohort_summary.__doc__)
~~~

### Source

[`src/thomaslab/easy.py#L54`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/easy.py#L54)

---

<!-- callable:thomaslab.easy.compute_incidence_rate -->
## compute_incidence_rate

### Purpose

Compute an incidence rate from binary events and observed person-time.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def compute_incidence_rate( df: pd.DataFrame, event_col: str, followup_col: str, *, followup_unit: str = "days", rate_per: float = 100.0, ) -> dict[str, float]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `event_col` | `event_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `followup_col` | `followup_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `followup_unit` | `followup_unit: str = 'days'` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `rate_per` | `rate_per: float = 100.0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `event_col`, `followup_col`.
- Referenced columns must exist in the input table: `event_col`, `followup_col`.

### Returns

`dict[str, float]`

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

from thomaslab.easy import compute_incidence_rate

result = compute_incidence_rate(
    df=sample_df,
    event_col='event',
    followup_col='followup'
)

print(result)
~~~

### Related functions

- `load_clinical_table`
- `quick_cohort_summary`
- `compute_binary_effect_measures`
- `build_patient_timeline`
- `make_cohort_flow`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/easy.py#L88`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/easy.py#L88)
- Repository search: [compute_incidence_rate](https://github.com/appsplorer/thomaslab-core/search?q=compute_incidence_rate&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compute an incidence rate from binary events and observed person-time.

``followup_unit`` may be ``days``, ``months``, or ``years``. The returned rate is per
``rate_per`` person-years.

### API inspection

~~~python
import inspect
from thomaslab.easy import compute_incidence_rate

print(inspect.signature(compute_incidence_rate))
print(compute_incidence_rate.__doc__)
~~~

### Source

[`src/thomaslab/easy.py#L88`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/easy.py#L88)

---

<!-- callable:thomaslab.easy.compute_binary_effect_measures -->
## compute_binary_effect_measures

### Purpose

Compute crude risk difference, risk ratio, odds ratio, and NNT/NNH.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def compute_binary_effect_measures( df: pd.DataFrame, outcome_col: str, treatment_col: str, ) -> dict[str, float | int | str]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `outcome_col`, `treatment_col`.
- Referenced columns must exist in the input table: `outcome_col`, `treatment_col`.

### Returns

`dict[str, float | int | str]`

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

from thomaslab.easy import compute_binary_effect_measures

result = compute_binary_effect_measures(
    df=sample_df,
    outcome_col='outcome',
    treatment_col='treatment'
)

print(result)
~~~

### Related functions

- `load_clinical_table`
- `quick_cohort_summary`
- `compute_incidence_rate`
- `build_patient_timeline`
- `make_cohort_flow`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/easy.py#L127`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/easy.py#L127)
- Repository search: [compute_binary_effect_measures](https://github.com/appsplorer/thomaslab-core/search?q=compute_binary_effect_measures&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compute crude risk difference, risk ratio, odds ratio, and NNT/NNH.

### API inspection

~~~python
import inspect
from thomaslab.easy import compute_binary_effect_measures

print(inspect.signature(compute_binary_effect_measures))
print(compute_binary_effect_measures.__doc__)
~~~

### Source

[`src/thomaslab/easy.py#L127`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/easy.py#L127)

---

<!-- callable:thomaslab.easy.build_patient_timeline -->
## build_patient_timeline

### Purpose

Create a chronologically ordered patient-event timeline with relative-day offsets.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_patient_timeline( df: pd.DataFrame, patient_id_col: str, date_col: str, event_col: str, *, value_cols: list[str] | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_id_col` | `patient_id_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `value_cols` | `value_cols: list[str] \| None = None` | No | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `patient_id_col`, `date_col`, `event_col`.
- Referenced columns must exist in the input table: `patient_id_col`, `date_col`, `event_col`.

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

from thomaslab.easy import build_patient_timeline

result = build_patient_timeline(
    df=sample_df,
    patient_id_col='patient_id',
    date_col='event_date',
    event_col='event'
)

print(result)
~~~

### Related functions

- `load_clinical_table`
- `quick_cohort_summary`
- `compute_incidence_rate`
- `compute_binary_effect_measures`
- `make_cohort_flow`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/easy.py#L166`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/easy.py#L166)
- Repository search: [build_patient_timeline](https://github.com/appsplorer/thomaslab-core/search?q=build_patient_timeline&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create a chronologically ordered patient-event timeline with relative-day offsets.

### API inspection

~~~python
import inspect
from thomaslab.easy import build_patient_timeline

print(inspect.signature(build_patient_timeline))
print(build_patient_timeline.__doc__)
~~~

### Source

[`src/thomaslab/easy.py#L166`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/easy.py#L166)

---

<!-- callable:thomaslab.easy.make_cohort_flow -->
## make_cohort_flow

### Purpose

Build a publication-friendly cohort-flow table from sequential counts.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def make_cohort_flow(steps: list[dict[str, Any]]) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `steps` | `steps: list[dict[str, Any]]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `steps`.

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
from thomaslab.easy import make_cohort_flow

result = make_cohort_flow(
    steps={}
)

print(result)
~~~

### Related functions

- `load_clinical_table`
- `quick_cohort_summary`
- `compute_incidence_rate`
- `compute_binary_effect_measures`
- `build_patient_timeline`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/easy.py#L188`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/easy.py#L188)
- Repository search: [make_cohort_flow](https://github.com/appsplorer/thomaslab-core/search?q=make_cohort_flow&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build a publication-friendly cohort-flow table from sequential counts.

Each step requires ``label`` and ``n``. Counts must be non-increasing.

### API inspection

~~~python
import inspect
from thomaslab.easy import make_cohort_flow

print(inspect.signature(make_cohort_flow))
print(make_cohort_flow.__doc__)
~~~

### Source

[`src/thomaslab/easy.py#L188`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/easy.py#L188)

---

<!-- callable:thomaslab.easy.quick_binary_model -->
## quick_binary_model

### Purpose

Leakage-checked baseline prediction with aggregate diagnostics only.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def quick_binary_model( df: pd.DataFrame, outcome_col: str, feature_cols: list[str], *, test_size: float = 0.25, random_state: int = 42, split_strategy: str | None = None, patient_id_col: str | None = None, site_id_col: str | None = None, time_col: str | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `feature_cols` | `feature_cols: list[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `test_size` | `test_size: float = 0.25` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |
| `split_strategy` | `split_strategy: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `patient_id_col` | `patient_id_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `site_id_col` | `site_id_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `outcome_col`, `feature_cols`.
- Referenced columns must exist in the input table: `outcome_col`, `patient_id_col`, `site_id_col`, `time_col`.

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

from thomaslab.easy import quick_binary_model

result = quick_binary_model(
    df=sample_df,
    outcome_col='outcome',
    feature_cols=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `load_clinical_table`
- `quick_cohort_summary`
- `compute_incidence_rate`
- `compute_binary_effect_measures`
- `build_patient_timeline`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/easy.py#L221`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/easy.py#L221)
- Repository search: [quick_binary_model](https://github.com/appsplorer/thomaslab-core/search?q=quick_binary_model&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Leakage-checked baseline prediction with aggregate diagnostics only.

A split strategy must be explicit. Missing/unsafe strategies return a
blocked design, not a fitted row-random baseline. Even a successful fit
still requires independent scientific review before publication.

### API inspection

~~~python
import inspect
from thomaslab.easy import quick_binary_model

print(inspect.signature(quick_binary_model))
print(quick_binary_model.__doc__)
~~~

### Source

[`src/thomaslab/easy.py#L221`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/easy.py#L221)

---

<!-- callable:thomaslab.easy.export_analysis_bundle -->
## export_analysis_bundle

### Purpose

Export tables, metadata, and existing figures into a portable analysis folder.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def export_analysis_bundle( output_dir: str | Path, *, tables: dict[str, pd.DataFrame] | None = None, metadata: dict[str, Any] | None = None, figures: list[str | Path] | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `output_dir` | `output_dir: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `tables` | `tables: dict[str, pd.DataFrame] \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `metadata` | `metadata: dict[str, Any] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `figures` | `figures: list[str \| Path] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `output_dir`.

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
from thomaslab.easy import export_analysis_bundle

result = export_analysis_bundle(
    output_dir="value"
)

print(result)
~~~

### Related functions

- `load_clinical_table`
- `quick_cohort_summary`
- `compute_incidence_rate`
- `compute_binary_effect_measures`
- `build_patient_timeline`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/easy.py#L256`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/easy.py#L256)
- Repository search: [export_analysis_bundle](https://github.com/appsplorer/thomaslab-core/search?q=export_analysis_bundle&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Export tables, metadata, and existing figures into a portable analysis folder.

### API inspection

~~~python
import inspect
from thomaslab.easy import export_analysis_bundle

print(inspect.signature(export_analysis_bundle))
print(export_analysis_bundle.__doc__)
~~~

### Source

[`src/thomaslab/easy.py#L256`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/easy.py#L256)

---

<!-- callable:thomaslab.easy.load_and_profile -->
## load_and_profile

### Purpose

One-call helper for notebook users: load a table and generate basic quality/cohort summaries.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def load_and_profile( path: str | Path, *, outcome_col: str | None = None, group_col: str | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `path` | `path: str \| Path` | Yes | Input source/path accepted by this callable. Keep raw-source provenance and do not overwrite the source. |
| `outcome_col` | `outcome_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `group_col` | `group_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `path`.
- Referenced columns must exist in the input table: `outcome_col`, `group_col`.

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
from thomaslab.easy import load_and_profile

result = load_and_profile(
    path="path/to/input.csv"
)

print(result)
~~~

### Related functions

- `load_clinical_table`
- `quick_cohort_summary`
- `compute_incidence_rate`
- `compute_binary_effect_measures`
- `build_patient_timeline`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/easy.py#L302`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/easy.py#L302)
- Repository search: [load_and_profile](https://github.com/appsplorer/thomaslab-core/search?q=load_and_profile&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

One-call helper for notebook users: load a table and generate basic quality/cohort summaries.

### API inspection

~~~python
import inspect
from thomaslab.easy import load_and_profile

print(inspect.signature(load_and_profile))
print(load_and_profile.__doc__)
~~~

### Source

[`src/thomaslab/easy.py#L302`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/easy.py#L302)

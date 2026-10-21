# thomaslab.viz

Publication-oriented tabulation and visualization utilities.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 7

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.viz.generate_table_one -->
## generate_table_one

### Purpose

Generate a baseline Table 1 in Markdown and LaTeX.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def generate_table_one( df: pd.DataFrame, group_col: str, categorical_cols: list[str], continuous_cols: list[str], ) -> str
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `group_col` | `group_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `categorical_cols` | `categorical_cols: list[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `continuous_cols` | `continuous_cols: list[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `group_col`, `categorical_cols`, `continuous_cols`.
- Referenced columns must exist in the input table: `group_col`.

### Returns

`str`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

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

from thomaslab.viz import generate_table_one

result = generate_table_one(
    df=sample_df,
    group_col='group',
    categorical_cols=["feature_a", "feature_b"],
    continuous_cols=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `plot_roc_pr_curves`
- `plot_calibration_curve`
- `plot_kaplan_meier`
- `plot_sankey_treatment_pathways`
- `plot_forest_subgroups`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/viz.py#L26`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/viz.py#L26)
- Repository search: [generate_table_one](https://github.com/appsplorer/thomaslab-core/search?q=generate_table_one&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Generate a baseline Table 1 in Markdown and LaTeX.

Continuous variables are summarized mean (SD) and compared by Welch t-test for two groups
or Kruskal-Wallis for >2 groups. Categorical variables use chi-square, falling back to
Fisher's exact test for 2x2 tables with small expected counts.

### API inspection

~~~python
import inspect
from thomaslab.viz import generate_table_one

print(inspect.signature(generate_table_one))
print(generate_table_one.__doc__)
~~~

### Source

[`src/thomaslab/viz.py#L26`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/viz.py#L26)

---

<!-- callable:thomaslab.viz.plot_roc_pr_curves -->
## plot_roc_pr_curves

### Purpose

Plot ROC and precision-recall curves side-by-side.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def plot_roc_pr_curves( y_true: np.ndarray, y_pred_prob: np.ndarray, save_path: str | None = None, ) -> None
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `y_true` | `y_true: np.ndarray` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `y_pred_prob` | `y_pred_prob: np.ndarray` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `save_path` | `save_path: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `y_true`, `y_pred_prob`.

### Returns

`None`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import numpy as np

sample_values = np.array([0.2, 0.8, 0.4, 0.6])

from thomaslab.viz import plot_roc_pr_curves

result = plot_roc_pr_curves(
    y_true=sample_values,
    y_pred_prob=sample_values
)

print(result)
~~~

### Related functions

- `generate_table_one`
- `plot_calibration_curve`
- `plot_kaplan_meier`
- `plot_sankey_treatment_pathways`
- `plot_forest_subgroups`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/viz.py#L95`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/viz.py#L95)
- Repository search: [plot_roc_pr_curves](https://github.com/appsplorer/thomaslab-core/search?q=plot_roc_pr_curves&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Plot ROC and precision-recall curves side-by-side.

### API inspection

~~~python
import inspect
from thomaslab.viz import plot_roc_pr_curves

print(inspect.signature(plot_roc_pr_curves))
print(plot_roc_pr_curves.__doc__)
~~~

### Source

[`src/thomaslab/viz.py#L95`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/viz.py#L95)

---

<!-- callable:thomaslab.viz.plot_calibration_curve -->
## plot_calibration_curve

### Purpose

Plot observed versus predicted event probabilities.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def plot_calibration_curve( y_true: np.ndarray, y_pred_prob: np.ndarray, save_path: str | None = None, ) -> None
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `y_true` | `y_true: np.ndarray` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `y_pred_prob` | `y_pred_prob: np.ndarray` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `save_path` | `save_path: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `y_true`, `y_pred_prob`.

### Returns

`None`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import numpy as np

sample_values = np.array([0.2, 0.8, 0.4, 0.6])

from thomaslab.viz import plot_calibration_curve

result = plot_calibration_curve(
    y_true=sample_values,
    y_pred_prob=sample_values
)

print(result)
~~~

### Related functions

- `generate_table_one`
- `plot_roc_pr_curves`
- `plot_kaplan_meier`
- `plot_sankey_treatment_pathways`
- `plot_forest_subgroups`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/viz.py#L120`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/viz.py#L120)
- Repository search: [plot_calibration_curve](https://github.com/appsplorer/thomaslab-core/search?q=plot_calibration_curve&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Plot observed versus predicted event probabilities.

### API inspection

~~~python
import inspect
from thomaslab.viz import plot_calibration_curve

print(inspect.signature(plot_calibration_curve))
print(plot_calibration_curve.__doc__)
~~~

### Source

[`src/thomaslab/viz.py#L120`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/viz.py#L120)

---

<!-- callable:thomaslab.viz.plot_kaplan_meier -->
## plot_kaplan_meier

### Purpose

Plot Kaplan-Meier curves with an at-risk count table.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def plot_kaplan_meier( df: pd.DataFrame, time_col: str, event_col: str, group_col: str, save_path: str | None = None, ) -> None
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `group_col` | `group_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `save_path` | `save_path: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `time_col`, `event_col`, `group_col`.
- Referenced columns must exist in the input table: `time_col`, `event_col`, `group_col`.

### Returns

`None`

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

from thomaslab.viz import plot_kaplan_meier

result = plot_kaplan_meier(
    df=sample_df,
    time_col='event_date',
    event_col='event',
    group_col='group'
)

print(result)
~~~

### Related functions

- `generate_table_one`
- `plot_roc_pr_curves`
- `plot_calibration_curve`
- `plot_sankey_treatment_pathways`
- `plot_forest_subgroups`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/viz.py#L143`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/viz.py#L143)
- Repository search: [plot_kaplan_meier](https://github.com/appsplorer/thomaslab-core/search?q=plot_kaplan_meier&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Plot Kaplan-Meier curves with an at-risk count table.

### API inspection

~~~python
import inspect
from thomaslab.viz import plot_kaplan_meier

print(inspect.signature(plot_kaplan_meier))
print(plot_kaplan_meier.__doc__)
~~~

### Source

[`src/thomaslab/viz.py#L143`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/viz.py#L143)

---

<!-- callable:thomaslab.viz.plot_sankey_treatment_pathways -->
## plot_sankey_treatment_pathways

### Purpose

Create an interactive Sankey diagram of sequential treatment transitions.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def plot_sankey_treatment_pathways( df: pd.DataFrame, patient_id_col: str, drug_col: str, date_col: str, max_lines: int = 4, *, save_path: str | None = None, ) -> object
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_id_col` | `patient_id_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `max_lines` | `max_lines: int = 4` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `save_path` | `save_path: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `patient_id_col`, `drug_col`, `date_col`.
- Referenced columns must exist in the input table: `patient_id_col`, `drug_col`, `date_col`.

### Returns

`object`

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

from thomaslab.viz import plot_sankey_treatment_pathways

result = plot_sankey_treatment_pathways(
    df=sample_df,
    patient_id_col='patient_id',
    drug_col='drug',
    date_col='event_date'
)

print(result)
~~~

### Related functions

- `generate_table_one`
- `plot_roc_pr_curves`
- `plot_calibration_curve`
- `plot_kaplan_meier`
- `plot_forest_subgroups`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/viz.py#L215`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/viz.py#L215)
- Repository search: [plot_sankey_treatment_pathways](https://github.com/appsplorer/thomaslab-core/search?q=plot_sankey_treatment_pathways&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create an interactive Sankey diagram of sequential treatment transitions.

Repeated consecutive records for the same drug are collapsed before assigning
1st-, 2nd-, ..., ``max_lines``-line therapy. Nodes are stage-specific so a drug
reappearing later in a pathway is not conflated with its earlier use.

### API inspection

~~~python
import inspect
from thomaslab.viz import plot_sankey_treatment_pathways

print(inspect.signature(plot_sankey_treatment_pathways))
print(plot_sankey_treatment_pathways.__doc__)
~~~

### Source

[`src/thomaslab/viz.py#L215`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/viz.py#L215)

---

<!-- callable:thomaslab.viz.plot_forest_subgroups -->
## plot_forest_subgroups

### Purpose

Plot publication-ready subgroup effect estimates with 95% confidence intervals.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def plot_forest_subgroups( subgroup_results_df: pd.DataFrame, save_path: str | None = None, ) -> plt.Figure
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `subgroup_results_df` | `subgroup_results_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `save_path` | `save_path: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `subgroup_results_df`.

### Returns

`plt.Figure`

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

from thomaslab.viz import plot_forest_subgroups

result = plot_forest_subgroups(
    subgroup_results_df=sample_df
)

print(result)
~~~

### Related functions

- `generate_table_one`
- `plot_roc_pr_curves`
- `plot_calibration_curve`
- `plot_kaplan_meier`
- `plot_sankey_treatment_pathways`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/viz.py#L293`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/viz.py#L293)
- Repository search: [plot_forest_subgroups](https://github.com/appsplorer/thomaslab-core/search?q=plot_forest_subgroups&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Plot publication-ready subgroup effect estimates with 95% confidence intervals.

Recognized estimate columns include ``hazard_ratio``, ``hr``, and ``estimate``;
confidence limits may be ``ci_lower``/``ci_upper``, ``lower_ci``/``upper_ci``,
or ``ci_lower_95``/``ci_upper_95``.

### API inspection

~~~python
import inspect
from thomaslab.viz import plot_forest_subgroups

print(inspect.signature(plot_forest_subgroups))
print(plot_forest_subgroups.__doc__)
~~~

### Source

[`src/thomaslab/viz.py#L293`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/viz.py#L293)

---

<!-- callable:thomaslab.viz.plot_cumulative_incidence_competing -->
## plot_cumulative_incidence_competing

### Purpose

Plot Aalen-Johansen cumulative incidence under competing risks.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def plot_cumulative_incidence_competing( df: pd.DataFrame, time_col: str, event_col: str, group_col: str, *, event_of_interest: int = 1, save_path: str | None = None, ) -> plt.Figure
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `group_col` | `group_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_of_interest` | `event_of_interest: int = 1` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `save_path` | `save_path: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `time_col`, `event_col`, `group_col`.
- Referenced columns must exist in the input table: `time_col`, `event_col`, `group_col`.

### Returns

`plt.Figure`

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

from thomaslab.viz import plot_cumulative_incidence_competing

result = plot_cumulative_incidence_competing(
    df=sample_df,
    time_col='event_date',
    event_col='event',
    group_col='group'
)

print(result)
~~~

### Related functions

- `generate_table_one`
- `plot_roc_pr_curves`
- `plot_calibration_curve`
- `plot_kaplan_meier`
- `plot_sankey_treatment_pathways`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/viz.py#L360`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/viz.py#L360)
- Repository search: [plot_cumulative_incidence_competing](https://github.com/appsplorer/thomaslab-core/search?q=plot_cumulative_incidence_competing&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Plot Aalen-Johansen cumulative incidence under competing risks.

``event_col`` must use ``0`` for censoring and positive integers for event
causes. ``event_of_interest`` selects the cause whose cumulative incidence is
shown separately for each group.

### API inspection

~~~python
import inspect
from thomaslab.viz import plot_cumulative_incidence_competing

print(inspect.signature(plot_cumulative_incidence_competing))
print(plot_cumulative_incidence_competing.__doc__)
~~~

### Source

[`src/thomaslab/viz.py#L360`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/viz.py#L360)

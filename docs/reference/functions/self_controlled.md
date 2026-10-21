# thomaslab.self_controlled

Self-controlled medication-safety study-design utilities.

The module supports self-controlled case-series (SCCS) and case-crossover data
construction, diagnostics, and transparent within-person estimators. These designs
control time-invariant measured and unmeasured person-level factors by construction,
but they still depend on design-specific assumptions about event-dependent exposure,
event-dependent observation, time-varying confounding, exposure timing, risk-window
specification, and outcome ascertainment.

Outputs are research estimates, not adverse-drug-reaction adjudications or treatment
recommendations.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 11

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.self_controlled.validate_observation_periods -->
## validate_observation_periods

### Purpose

Validate one inclusive observation period per patient.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_observation_periods( observation: pd.DataFrame, *, patient_col: str = "patient_id", start_col: str = "observation_start", end_col: str = "observation_end", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `observation` | `observation: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'observation_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'observation_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `observation`.
- Referenced columns must exist in the input table: `patient_col`, `start_col`, `end_col`.

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

from thomaslab.self_controlled import validate_observation_periods

result = validate_observation_periods(
    observation=sample_df
)

print(result)
~~~

### Related functions

- `build_sccs_intervals`
- `audit_sccs_intervals`
- `summarize_sccs_periods`
- `fit_sccs_conditional_poisson`
- `audit_event_dependent_exposure`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/self_controlled.py#L43`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L43)
- Repository search: [validate_observation_periods](https://github.com/appsplorer/thomaslab-core/search?q=validate_observation_periods&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate one inclusive observation period per patient.

### API inspection

~~~python
import inspect
from thomaslab.self_controlled import validate_observation_periods

print(inspect.signature(validate_observation_periods))
print(validate_observation_periods.__doc__)
~~~

### Source

[`src/thomaslab/self_controlled.py#L43`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L43)

---

<!-- callable:thomaslab.self_controlled.build_sccs_intervals -->
## build_sccs_intervals

### Purpose

Partition observation time into mutually exclusive SCCS periods.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_sccs_intervals( observation: pd.DataFrame, exposures: pd.DataFrame, events: pd.DataFrame, *, risk_windows: Mapping[str, Sequence[int]], patient_col: str = "patient_id", observation_start_col: str = "observation_start", observation_end_col: str = "observation_end", drug_col: str = "drug", exposure_start_col: str = "episode_start", exposure_end_col: str = "episode_end", event_date_col: str = "event_date", event_term_col: str | None = None, target_event_terms: Sequence[str] | None = None, target_drugs: Sequence[str] | None = None, anchor: str = "start", baseline_label: str = "baseline", overlap_policy: str = "error", case_only: bool = True, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `observation` | `observation: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `exposures` | `exposures: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `risk_windows` | `risk_windows: Mapping[str, Sequence[int]]` | Yes | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `observation_start_col` | `observation_start_col: str = 'observation_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `observation_end_col` | `observation_end_col: str = 'observation_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `exposure_start_col` | `exposure_start_col: str = 'episode_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `exposure_end_col` | `exposure_end_col: str = 'episode_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_date_col` | `event_date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_term_col` | `event_term_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `target_event_terms` | `target_event_terms: Sequence[str] \| None = None` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `target_drugs` | `target_drugs: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `anchor` | `anchor: str = 'start'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `baseline_label` | `baseline_label: str = 'baseline'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `overlap_policy` | `overlap_policy: str = 'error'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `case_only` | `case_only: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `observation`, `exposures`, `events`, `risk_windows`.
- Referenced columns must exist in the input table: `patient_col`, `observation_start_col`, `observation_end_col`, `drug_col`, `exposure_start_col`, `exposure_end_col`, `event_date_col`, `event_term_col`.

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

from thomaslab.self_controlled import build_sccs_intervals

result = build_sccs_intervals(
    observation=sample_df,
    exposures=sample_df,
    events=sample_df,
    risk_windows={}
)

print(result)
~~~

### Related functions

- `validate_observation_periods`
- `audit_sccs_intervals`
- `summarize_sccs_periods`
- `fit_sccs_conditional_poisson`
- `audit_event_dependent_exposure`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/self_controlled.py#L81`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L81)
- Repository search: [build_sccs_intervals](https://github.com/appsplorer/thomaslab-core/search?q=build_sccs_intervals&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Partition observation time into mutually exclusive SCCS periods.

risk_windows is an explicit mapping such as:
{"pre_exposure": [-7, -1], "risk_0_7": [0, 7], "risk_8_30": [8, 30]}.
Uncovered observation time is assigned to baseline_label.

Repeated exposures can generate overlapping risk periods. The default policy is
to fail closed. latest_exposure and earliest_exposure are available only when the
protocol explicitly defines that precedence rule.

### API inspection

~~~python
import inspect
from thomaslab.self_controlled import build_sccs_intervals

print(inspect.signature(build_sccs_intervals))
print(build_sccs_intervals.__doc__)
~~~

### Source

[`src/thomaslab/self_controlled.py#L81`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L81)

---

<!-- callable:thomaslab.self_controlled.audit_sccs_intervals -->
## audit_sccs_intervals

### Purpose

Audit continuity, case-only eligibility, and baseline support.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_sccs_intervals( intervals: pd.DataFrame, *, patient_col: str = "patient_id", start_col: str = "interval_start", end_col: str = "interval_end", days_col: str = "interval_days", period_col: str = "period", event_count_col: str = "event_count", baseline_label: str = "baseline", ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `intervals` | `intervals: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'interval_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'interval_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `days_col` | `days_col: str = 'interval_days'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `period_col` | `period_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_count_col` | `event_count_col: str = 'event_count'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `baseline_label` | `baseline_label: str = 'baseline'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `intervals`.
- Referenced columns must exist in the input table: `patient_col`, `start_col`, `end_col`, `days_col`, `period_col`, `event_count_col`.

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

from thomaslab.self_controlled import audit_sccs_intervals

result = audit_sccs_intervals(
    intervals=sample_df
)

print(result)
~~~

### Related functions

- `validate_observation_periods`
- `build_sccs_intervals`
- `summarize_sccs_periods`
- `fit_sccs_conditional_poisson`
- `audit_event_dependent_exposure`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/self_controlled.py#L246`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L246)
- Repository search: [audit_sccs_intervals](https://github.com/appsplorer/thomaslab-core/search?q=audit_sccs_intervals&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Audit continuity, case-only eligibility, and baseline support.

### API inspection

~~~python
import inspect
from thomaslab.self_controlled import audit_sccs_intervals

print(inspect.signature(audit_sccs_intervals))
print(audit_sccs_intervals.__doc__)
~~~

### Source

[`src/thomaslab/self_controlled.py#L246`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L246)

---

<!-- callable:thomaslab.self_controlled.summarize_sccs_periods -->
## summarize_sccs_periods

### Purpose

Summarize SCCS events and person-time descriptively by period.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_sccs_periods( intervals: pd.DataFrame, *, period_col: str = "period", days_col: str = "interval_days", event_count_col: str = "event_count", rate_per_person_years: float = 100.0, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `intervals` | `intervals: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `period_col` | `period_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `days_col` | `days_col: str = 'interval_days'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_count_col` | `event_count_col: str = 'event_count'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `rate_per_person_years` | `rate_per_person_years: float = 100.0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `intervals`.
- Referenced columns must exist in the input table: `period_col`, `days_col`, `event_count_col`.

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

from thomaslab.self_controlled import summarize_sccs_periods

result = summarize_sccs_periods(
    intervals=sample_df
)

print(result)
~~~

### Related functions

- `validate_observation_periods`
- `build_sccs_intervals`
- `audit_sccs_intervals`
- `fit_sccs_conditional_poisson`
- `audit_event_dependent_exposure`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/self_controlled.py#L330`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L330)
- Repository search: [summarize_sccs_periods](https://github.com/appsplorer/thomaslab-core/search?q=summarize_sccs_periods&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize SCCS events and person-time descriptively by period.

### API inspection

~~~python
import inspect
from thomaslab.self_controlled import summarize_sccs_periods

print(inspect.signature(summarize_sccs_periods))
print(summarize_sccs_periods.__doc__)
~~~

### Source

[`src/thomaslab/self_controlled.py#L330`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L330)

---

<!-- callable:thomaslab.self_controlled.fit_sccs_conditional_poisson -->
## fit_sccs_conditional_poisson

### Purpose

Estimate period rate ratios with a conditional Poisson model.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fit_sccs_conditional_poisson( intervals: pd.DataFrame, *, patient_col: str = "patient_id", period_col: str = "period", event_count_col: str = "event_count", days_col: str = "interval_days", baseline_label: str = "baseline", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `intervals` | `intervals: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `period_col` | `period_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_count_col` | `event_count_col: str = 'event_count'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `days_col` | `days_col: str = 'interval_days'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `baseline_label` | `baseline_label: str = 'baseline'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `intervals`.
- Referenced columns must exist in the input table: `patient_col`, `period_col`, `event_count_col`, `days_col`.

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

from thomaslab.self_controlled import fit_sccs_conditional_poisson

result = fit_sccs_conditional_poisson(
    intervals=sample_df
)

print(result)
~~~

### Related functions

- `validate_observation_periods`
- `build_sccs_intervals`
- `audit_sccs_intervals`
- `summarize_sccs_periods`
- `audit_event_dependent_exposure`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/self_controlled.py#L362`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L362)
- Repository search: [fit_sccs_conditional_poisson](https://github.com/appsplorer/thomaslab-core/search?q=fit_sccs_conditional_poisson&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate period rate ratios with a conditional Poisson model.

Patient-specific fixed effects are conditioned out by statsmodels
ConditionalPoisson. This does not address time-varying confounding,
event-dependent exposure/observation, or misspecified risk periods.

### API inspection

~~~python
import inspect
from thomaslab.self_controlled import fit_sccs_conditional_poisson

print(inspect.signature(fit_sccs_conditional_poisson))
print(fit_sccs_conditional_poisson.__doc__)
~~~

### Source

[`src/thomaslab/self_controlled.py#L362`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L362)

---

<!-- callable:thomaslab.self_controlled.audit_event_dependent_exposure -->
## audit_event_dependent_exposure

### Purpose

Compare exposure starts immediately before vs after observed events.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_event_dependent_exposure( exposures: pd.DataFrame, events: pd.DataFrame, *, patient_col: str = "patient_id", exposure_start_col: str = "episode_start", event_date_col: str = "event_date", window_days: int = 30, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `exposures` | `exposures: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `exposure_start_col` | `exposure_start_col: str = 'episode_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_date_col` | `event_date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `window_days` | `window_days: int = 30` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `exposures`, `events`.
- Referenced columns must exist in the input table: `patient_col`, `exposure_start_col`, `event_date_col`.

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

from thomaslab.self_controlled import audit_event_dependent_exposure

result = audit_event_dependent_exposure(
    exposures=sample_df,
    events=sample_df
)

print(result)
~~~

### Related functions

- `validate_observation_periods`
- `build_sccs_intervals`
- `audit_sccs_intervals`
- `summarize_sccs_periods`
- `fit_sccs_conditional_poisson`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/self_controlled.py#L439`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L439)
- Repository search: [audit_event_dependent_exposure](https://github.com/appsplorer/thomaslab-core/search?q=audit_event_dependent_exposure&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compare exposure starts immediately before vs after observed events.

This is a diagnostic for protocol review, not a formal test proving or excluding
event-dependent exposure.

### API inspection

~~~python
import inspect
from thomaslab.self_controlled import audit_event_dependent_exposure

print(inspect.signature(audit_event_dependent_exposure))
print(audit_event_dependent_exposure.__doc__)
~~~

### Source

[`src/thomaslab/self_controlled.py#L439`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L439)

---

<!-- callable:thomaslab.self_controlled.build_case_crossover_windows -->
## build_case_crossover_windows

### Purpose

Create hazard and control windows around each case event.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_case_crossover_windows( cases: pd.DataFrame, *, hazard_window: Sequence[int], control_windows: Mapping[str, Sequence[int]], patient_col: str = "patient_id", event_date_col: str = "event_date", case_id_col: str | None = None, allow_post_event: bool = False, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `cases` | `cases: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `hazard_window` | `hazard_window: Sequence[int]` | Yes | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `control_windows` | `control_windows: Mapping[str, Sequence[int]]` | Yes | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_date_col` | `event_date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `case_id_col` | `case_id_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `allow_post_event` | `allow_post_event: bool = False` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `cases`, `hazard_window`, `control_windows`.
- Referenced columns must exist in the input table: `patient_col`, `event_date_col`, `case_id_col`.

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

from thomaslab.self_controlled import build_case_crossover_windows

result = build_case_crossover_windows(
    cases=sample_df,
    hazard_window=2,
    control_windows={}
)

print(result)
~~~

### Related functions

- `validate_observation_periods`
- `build_sccs_intervals`
- `audit_sccs_intervals`
- `summarize_sccs_periods`
- `fit_sccs_conditional_poisson`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/self_controlled.py#L503`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L503)
- Repository search: [build_case_crossover_windows](https://github.com/appsplorer/thomaslab-core/search?q=build_case_crossover_windows&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create hazard and control windows around each case event.

Offsets are inclusive days relative to the event date. By default, windows
touching or following day 0 are rejected to prevent accidental post-outcome
exposure assessment.

### API inspection

~~~python
import inspect
from thomaslab.self_controlled import build_case_crossover_windows

print(inspect.signature(build_case_crossover_windows))
print(build_case_crossover_windows.__doc__)
~~~

### Source

[`src/thomaslab/self_controlled.py#L503`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L503)

---

<!-- callable:thomaslab.self_controlled.audit_case_crossover_windows -->
## audit_case_crossover_windows

### Purpose

Audit hazard/control count, overlap, and duration within each case.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_case_crossover_windows( windows: pd.DataFrame, *, case_id_col: str = "case_id", role_col: str = "window_role", start_col: str = "window_start", end_col: str = "window_end", days_col: str = "window_days", require_equal_duration: bool = True, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `windows` | `windows: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `case_id_col` | `case_id_col: str = 'case_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `role_col` | `role_col: str = 'window_role'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'window_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'window_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `days_col` | `days_col: str = 'window_days'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `require_equal_duration` | `require_equal_duration: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `windows`.
- Referenced columns must exist in the input table: `case_id_col`, `role_col`, `start_col`, `end_col`, `days_col`.

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

from thomaslab.self_controlled import audit_case_crossover_windows

result = audit_case_crossover_windows(
    windows=sample_df
)

print(result)
~~~

### Related functions

- `validate_observation_periods`
- `build_sccs_intervals`
- `audit_sccs_intervals`
- `summarize_sccs_periods`
- `fit_sccs_conditional_poisson`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/self_controlled.py#L575`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L575)
- Repository search: [audit_case_crossover_windows](https://github.com/appsplorer/thomaslab-core/search?q=audit_case_crossover_windows&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Audit hazard/control count, overlap, and duration within each case.

### API inspection

~~~python
import inspect
from thomaslab.self_controlled import audit_case_crossover_windows

print(inspect.signature(audit_case_crossover_windows))
print(audit_case_crossover_windows.__doc__)
~~~

### Source

[`src/thomaslab/self_controlled.py#L575`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L575)

---

<!-- callable:thomaslab.self_controlled.classify_case_crossover_exposure -->
## classify_case_crossover_exposure

### Purpose

Classify any exposure overlap and exposed days in each case-crossover window.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def classify_case_crossover_exposure( windows: pd.DataFrame, exposures: pd.DataFrame, *, patient_col: str = "patient_id", drug_col: str = "drug", exposure_start_col: str = "episode_start", exposure_end_col: str = "episode_end", window_start_col: str = "window_start", window_end_col: str = "window_end", target_drugs: Sequence[str] | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `windows` | `windows: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `exposures` | `exposures: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `exposure_start_col` | `exposure_start_col: str = 'episode_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `exposure_end_col` | `exposure_end_col: str = 'episode_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `window_start_col` | `window_start_col: str = 'window_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `window_end_col` | `window_end_col: str = 'window_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `target_drugs` | `target_drugs: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `windows`, `exposures`.
- Referenced columns must exist in the input table: `patient_col`, `drug_col`, `exposure_start_col`, `exposure_end_col`, `window_start_col`, `window_end_col`.

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

from thomaslab.self_controlled import classify_case_crossover_exposure

result = classify_case_crossover_exposure(
    windows=sample_df,
    exposures=sample_df
)

print(result)
~~~

### Related functions

- `validate_observation_periods`
- `build_sccs_intervals`
- `audit_sccs_intervals`
- `summarize_sccs_periods`
- `fit_sccs_conditional_poisson`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/self_controlled.py#L644`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L644)
- Repository search: [classify_case_crossover_exposure](https://github.com/appsplorer/thomaslab-core/search?q=classify_case_crossover_exposure&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Classify any exposure overlap and exposed days in each case-crossover window.

### API inspection

~~~python
import inspect
from thomaslab.self_controlled import classify_case_crossover_exposure

print(inspect.signature(classify_case_crossover_exposure))
print(classify_case_crossover_exposure.__doc__)
~~~

### Source

[`src/thomaslab/self_controlled.py#L644`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L644)

---

<!-- callable:thomaslab.self_controlled.matched_case_crossover_odds_ratio -->
## matched_case_crossover_odds_ratio

### Purpose

Calculate the matched-pair odds ratio for one hazard and one control window.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def matched_case_crossover_odds_ratio( classified_windows: pd.DataFrame, *, case_id_col: str = "case_id", role_col: str = "window_role", exposure_col: str = "exposed_any", ci: float = 0.95, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `classified_windows` | `classified_windows: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `case_id_col` | `case_id_col: str = 'case_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `role_col` | `role_col: str = 'window_role'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `exposure_col` | `exposure_col: str = 'exposed_any'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `classified_windows`.
- Referenced columns must exist in the input table: `case_id_col`, `role_col`, `exposure_col`.

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

from thomaslab.self_controlled import matched_case_crossover_odds_ratio

result = matched_case_crossover_odds_ratio(
    classified_windows=sample_df
)

print(result)
~~~

### Related functions

- `validate_observation_periods`
- `build_sccs_intervals`
- `audit_sccs_intervals`
- `summarize_sccs_periods`
- `fit_sccs_conditional_poisson`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/self_controlled.py#L704`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L704)
- Repository search: [matched_case_crossover_odds_ratio](https://github.com/appsplorer/thomaslab-core/search?q=matched_case_crossover_odds_ratio&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate the matched-pair odds ratio for one hazard and one control window.

### API inspection

~~~python
import inspect
from thomaslab.self_controlled import matched_case_crossover_odds_ratio

print(inspect.signature(matched_case_crossover_odds_ratio))
print(matched_case_crossover_odds_ratio.__doc__)
~~~

### Source

[`src/thomaslab/self_controlled.py#L704`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L704)

---

<!-- callable:thomaslab.self_controlled.fit_case_crossover_conditional_logit -->
## fit_case_crossover_conditional_logit

### Purpose

Fit conditional logistic regression for one hazard and one-or-more controls per case.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fit_case_crossover_conditional_logit( classified_windows: pd.DataFrame, *, case_id_col: str = "case_id", role_col: str = "window_role", exposure_col: str = "exposed_any", ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `classified_windows` | `classified_windows: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `case_id_col` | `case_id_col: str = 'case_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `role_col` | `role_col: str = 'window_role'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `exposure_col` | `exposure_col: str = 'exposed_any'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `classified_windows`.
- Referenced columns must exist in the input table: `case_id_col`, `role_col`, `exposure_col`.

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

from thomaslab.self_controlled import fit_case_crossover_conditional_logit

result = fit_case_crossover_conditional_logit(
    classified_windows=sample_df
)

print(result)
~~~

### Related functions

- `validate_observation_periods`
- `build_sccs_intervals`
- `audit_sccs_intervals`
- `summarize_sccs_periods`
- `fit_sccs_conditional_poisson`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/self_controlled.py#L756`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L756)
- Repository search: [fit_case_crossover_conditional_logit](https://github.com/appsplorer/thomaslab-core/search?q=fit_case_crossover_conditional_logit&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Fit conditional logistic regression for one hazard and one-or-more controls per case.

### API inspection

~~~python
import inspect
from thomaslab.self_controlled import fit_case_crossover_conditional_logit

print(inspect.signature(fit_case_crossover_conditional_logit))
print(fit_case_crossover_conditional_logit.__doc__)
~~~

### Source

[`src/thomaslab/self_controlled.py#L756`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/self_controlled.py#L756)

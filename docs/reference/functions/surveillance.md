# thomaslab.surveillance

Medication-surveillance summaries for research use.

This module keeps denominator-based EHR/claims safety analyses separate from
spontaneous-report disproportionality analyses. Neither design, by itself,
establishes adverse-drug-event causality.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 6

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.surveillance.compare_window_rates -->
## compare_window_rates

### Purpose

Compare crude event rates in explicit risk and background windows.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def compare_window_rates( *, risk_events: int, risk_person_days: float, background_events: int, background_person_days: float, rate_per_person_years: float = 100.0, ci: float = 0.95, ) -> dict[str, object]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `risk_events` | `risk_events: int` | Yes | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `risk_person_days` | `risk_person_days: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `background_events` | `background_events: int` | Yes | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `background_person_days` | `background_person_days: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `rate_per_person_years` | `rate_per_person_years: float = 100.0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `risk_events`, `risk_person_days`, `background_events`, `background_person_days`.

### Returns

`dict[str, object]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.surveillance import compare_window_rates

result = compare_window_rates(
    risk_events=2,
    risk_person_days=0.5,
    background_events=2,
    background_person_days=0.5
)

print(result)
~~~

### Related functions

- `summarize_window_person_time`
- `build_safety_signal_table`
- `audit_signal_evidence`
- `calculate_disproportionality`
- `build_disproportionality_table`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/surveillance.py#L23`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/surveillance.py#L23)
- Repository search: [compare_window_rates](https://github.com/appsplorer/thomaslab-core/search?q=compare_window_rates&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compare crude event rates in explicit risk and background windows.

### API inspection

~~~python
import inspect
from thomaslab.surveillance import compare_window_rates

print(inspect.signature(compare_window_rates))
print(compare_window_rates.__doc__)
~~~

### Source

[`src/thomaslab/surveillance.py#L23`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/surveillance.py#L23)

---

<!-- callable:thomaslab.surveillance.summarize_window_person_time -->
## summarize_window_person_time

### Purpose

Summarize study-defined safety-window counts and person-time.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_window_person_time( windows: pd.DataFrame, *, group_cols: Sequence[str] = ("drug", "window_role"), window_days_col: str = "window_days", window_id_col: str = "window_id", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `windows` | `windows: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `group_cols` | `group_cols: Sequence[str] = ('drug', 'window_role')` | No | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `window_days_col` | `window_days_col: str = 'window_days'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `window_id_col` | `window_id_col: str = 'window_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `windows`.
- Referenced columns must exist in the input table: `window_days_col`, `window_id_col`.

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

from thomaslab.surveillance import summarize_window_person_time

result = summarize_window_person_time(
    windows=sample_df
)

print(result)
~~~

### Related functions

- `compare_window_rates`
- `build_safety_signal_table`
- `audit_signal_evidence`
- `calculate_disproportionality`
- `build_disproportionality_table`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/surveillance.py#L69`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/surveillance.py#L69)
- Repository search: [summarize_window_person_time](https://github.com/appsplorer/thomaslab-core/search?q=summarize_window_person_time&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize study-defined safety-window counts and person-time.

### API inspection

~~~python
import inspect
from thomaslab.surveillance import summarize_window_person_time

print(inspect.signature(summarize_window_person_time))
print(summarize_window_person_time.__doc__)
~~~

### Source

[`src/thomaslab/surveillance.py#L69`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/surveillance.py#L69)

---

<!-- callable:thomaslab.surveillance.build_safety_signal_table -->
## build_safety_signal_table

### Purpose

Build descriptive drug/event risk-vs-background summaries.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_safety_signal_table( windows: pd.DataFrame, linked_events: pd.DataFrame, *, drug_col: str = "drug", role_col: str = "window_role", window_id_col: str = "window_id", window_days_col: str = "window_days", event_col: str = "event_term", risk_role: str = "risk", background_role: str = "background", rate_per_person_years: float = 100.0, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `windows` | `windows: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `linked_events` | `linked_events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `role_col` | `role_col: str = 'window_role'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `window_id_col` | `window_id_col: str = 'window_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `window_days_col` | `window_days_col: str = 'window_days'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str = 'event_term'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `risk_role` | `risk_role: str = 'risk'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `background_role` | `background_role: str = 'background'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `rate_per_person_years` | `rate_per_person_years: float = 100.0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `windows`, `linked_events`.
- Referenced columns must exist in the input table: `drug_col`, `role_col`, `window_id_col`, `window_days_col`, `event_col`.

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

from thomaslab.surveillance import build_safety_signal_table

result = build_safety_signal_table(
    windows=sample_df,
    linked_events=sample_df
)

print(result)
~~~

### Related functions

- `compare_window_rates`
- `summarize_window_person_time`
- `audit_signal_evidence`
- `calculate_disproportionality`
- `build_disproportionality_table`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/surveillance.py#L97`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/surveillance.py#L97)
- Repository search: [build_safety_signal_table](https://github.com/appsplorer/thomaslab-core/search?q=build_safety_signal_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build descriptive drug/event risk-vs-background summaries.

### API inspection

~~~python
import inspect
from thomaslab.surveillance import build_safety_signal_table

print(inspect.signature(build_safety_signal_table))
print(build_safety_signal_table.__doc__)
~~~

### Source

[`src/thomaslab/surveillance.py#L97`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/surveillance.py#L97)

---

<!-- callable:thomaslab.surveillance.audit_signal_evidence -->
## audit_signal_evidence

### Purpose

Apply an operational review threshold without declaring a clinical signal.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_signal_evidence( signal_table: pd.DataFrame, *, minimum_risk_events_for_review: int = 3, risk_event_col: str = "risk_events", background_event_col: str = "background_events", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `signal_table` | `signal_table: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `minimum_risk_events_for_review` | `minimum_risk_events_for_review: int = 3` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `risk_event_col` | `risk_event_col: str = 'risk_events'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `background_event_col` | `background_event_col: str = 'background_events'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `signal_table`.
- Referenced columns must exist in the input table: `risk_event_col`, `background_event_col`.

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

from thomaslab.surveillance import audit_signal_evidence

result = audit_signal_evidence(
    signal_table=sample_df
)

print(result)
~~~

### Related functions

- `compare_window_rates`
- `summarize_window_person_time`
- `build_safety_signal_table`
- `calculate_disproportionality`
- `build_disproportionality_table`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/surveillance.py#L162`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/surveillance.py#L162)
- Repository search: [audit_signal_evidence](https://github.com/appsplorer/thomaslab-core/search?q=audit_signal_evidence&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Apply an operational review threshold without declaring a clinical signal.

### API inspection

~~~python
import inspect
from thomaslab.surveillance import audit_signal_evidence

print(inspect.signature(audit_signal_evidence))
print(audit_signal_evidence.__doc__)
~~~

### Source

[`src/thomaslab/surveillance.py#L162`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/surveillance.py#L162)

---

<!-- callable:thomaslab.surveillance.calculate_disproportionality -->
## calculate_disproportionality

### Purpose

Calculate report-level reporting odds ratio and proportional reporting ratio.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_disproportionality( reports: pd.DataFrame, *, target_drug: str, target_event: str, report_id_col: str = "report_id", drug_col: str = "drug", event_col: str = "event_term", ) -> dict[str, object]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `reports` | `reports: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `target_drug` | `target_drug: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `target_event` | `target_event: str` | Yes | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `report_id_col` | `report_id_col: str = 'report_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str = 'event_term'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `reports`, `target_drug`, `target_event`.
- Referenced columns must exist in the input table: `report_id_col`, `drug_col`, `event_col`.

### Returns

`dict[str, object]`

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

from thomaslab.surveillance import calculate_disproportionality

result = calculate_disproportionality(
    reports=sample_df,
    target_drug="value",
    target_event="value"
)

print(result)
~~~

### Related functions

- `compare_window_rates`
- `summarize_window_person_time`
- `build_safety_signal_table`
- `audit_signal_evidence`
- `build_disproportionality_table`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/surveillance.py#L185`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/surveillance.py#L185)
- Repository search: [calculate_disproportionality](https://github.com/appsplorer/thomaslab-core/search?q=calculate_disproportionality&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate report-level reporting odds ratio and proportional reporting ratio.

### API inspection

~~~python
import inspect
from thomaslab.surveillance import calculate_disproportionality

print(inspect.signature(calculate_disproportionality))
print(calculate_disproportionality.__doc__)
~~~

### Source

[`src/thomaslab/surveillance.py#L185`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/surveillance.py#L185)

---

<!-- callable:thomaslab.surveillance.build_disproportionality_table -->
## build_disproportionality_table

### Purpose

Calculate disproportionality for observed pairs meeting a transparent case-count screen.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_disproportionality_table( reports: pd.DataFrame, *, report_id_col: str = "report_id", drug_col: str = "drug", event_col: str = "event_term", minimum_case_count: int = 3, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `reports` | `reports: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `report_id_col` | `report_id_col: str = 'report_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str = 'event_term'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `minimum_case_count` | `minimum_case_count: int = 3` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `reports`.
- Referenced columns must exist in the input table: `report_id_col`, `drug_col`, `event_col`.

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

from thomaslab.surveillance import build_disproportionality_table

result = build_disproportionality_table(
    reports=sample_df
)

print(result)
~~~

### Related functions

- `compare_window_rates`
- `summarize_window_person_time`
- `build_safety_signal_table`
- `audit_signal_evidence`
- `calculate_disproportionality`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/surveillance.py#L238`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/surveillance.py#L238)
- Repository search: [build_disproportionality_table](https://github.com/appsplorer/thomaslab-core/search?q=build_disproportionality_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate disproportionality for observed pairs meeting a transparent case-count screen.

### API inspection

~~~python
import inspect
from thomaslab.surveillance import build_disproportionality_table

print(inspect.signature(build_disproportionality_table))
print(build_disproportionality_table.__doc__)
~~~

### Source

[`src/thomaslab/surveillance.py#L238`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/surveillance.py#L238)

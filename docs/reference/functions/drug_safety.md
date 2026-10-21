# thomaslab.drug_safety

Drug-safety and adverse-event research utilities.

These helpers make exposure/event timing explicit for observational safety research.
Temporal association, co-exposure, seriousness evidence, or dechallenge/rechallenge
patterns are research signals to review; they do not establish drug-event causality
or support autonomous prescribing decisions.

## Research-use boundary

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

## Self-service orientation

- Related guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 8

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.drug_safety.validate_adverse_events -->
## validate_adverse_events

### Purpose

Validate a standardized adverse-event table and normalize dates.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_adverse_events( events: pd.DataFrame, *, patient_col: str = "patient_id", event_col: str = "event_term", event_date_col: str = "event_date", end_date_col: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str = 'event_term'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_date_col` | `event_date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_date_col` | `end_date_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`.
- Referenced columns must exist in the input table: `patient_col`, `event_col`, `event_date_col`, `end_date_col`.

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

from thomaslab.drug_safety import validate_adverse_events

result = validate_adverse_events(
    events=sample_df
)

print(result)
~~~

### Related functions

- `build_exposure_risk_windows`
- `audit_safety_windows`
- `link_exposure_events`
- `classify_seriousness_evidence`
- `map_severity`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drug_safety.py#L67`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drug_safety.py#L67)
- Repository search: [validate_adverse_events](https://github.com/appsplorer/thomaslab-core/search?q=validate_adverse_events&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate a standardized adverse-event table and normalize dates.

### API inspection

~~~python
import inspect
from thomaslab.drug_safety import validate_adverse_events

print(inspect.signature(validate_adverse_events))
print(validate_adverse_events.__doc__)
~~~

### Source

[`src/thomaslab/drug_safety.py#L67`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drug_safety.py#L67)

---

<!-- callable:thomaslab.drug_safety.build_exposure_risk_windows -->
## build_exposure_risk_windows

### Purpose

Expand each exposure episode into explicit study-defined time windows.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_exposure_risk_windows( exposures: pd.DataFrame, *, risk_windows: Mapping[str, Sequence[int]], background_windows: Mapping[str, Sequence[int]] | None = None, patient_col: str = "patient_id", drug_col: str = "drug", start_col: str = "episode_start", end_col: str = "episode_end", anchor: str = "start", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `exposures` | `exposures: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `risk_windows` | `risk_windows: Mapping[str, Sequence[int]]` | Yes | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `background_windows` | `background_windows: Mapping[str, Sequence[int]] \| None = None` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'episode_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'episode_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `anchor` | `anchor: str = 'start'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `exposures`, `risk_windows`.
- Referenced columns must exist in the input table: `patient_col`, `drug_col`, `start_col`, `end_col`.

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

from thomaslab.drug_safety import build_exposure_risk_windows

result = build_exposure_risk_windows(
    exposures=sample_df,
    risk_windows={}
)

print(result)
~~~

### Related functions

- `validate_adverse_events`
- `audit_safety_windows`
- `link_exposure_events`
- `classify_seriousness_evidence`
- `map_severity`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drug_safety.py#L110`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drug_safety.py#L110)
- Repository search: [build_exposure_risk_windows](https://github.com/appsplorer/thomaslab-core/search?q=build_exposure_risk_windows&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Expand each exposure episode into explicit study-defined time windows.

### API inspection

~~~python
import inspect
from thomaslab.drug_safety import build_exposure_risk_windows

print(inspect.signature(build_exposure_risk_windows))
print(build_exposure_risk_windows.__doc__)
~~~

### Source

[`src/thomaslab/drug_safety.py#L110`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drug_safety.py#L110)

---

<!-- callable:thomaslab.drug_safety.audit_safety_windows -->
## audit_safety_windows

### Purpose

Report overlapping safety windows without resolving them automatically.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_safety_windows( windows: pd.DataFrame, *, patient_col: str = "patient_id", drug_col: str = "drug", window_id_col: str = "window_id", start_col: str = "window_start", end_col: str = "window_end", role_col: str = "window_role", ) -> dict[str, object]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `windows` | `windows: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `window_id_col` | `window_id_col: str = 'window_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'window_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'window_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `role_col` | `role_col: str = 'window_role'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `windows`.
- Referenced columns must exist in the input table: `patient_col`, `drug_col`, `window_id_col`, `start_col`, `end_col`, `role_col`.

### Returns

`dict[str, object]`

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

from thomaslab.drug_safety import audit_safety_windows

result = audit_safety_windows(
    windows=sample_df
)

print(result)
~~~

### Related functions

- `validate_adverse_events`
- `build_exposure_risk_windows`
- `link_exposure_events`
- `classify_seriousness_evidence`
- `map_severity`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drug_safety.py#L167`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drug_safety.py#L167)
- Repository search: [audit_safety_windows](https://github.com/appsplorer/thomaslab-core/search?q=audit_safety_windows&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Report overlapping safety windows without resolving them automatically.

### API inspection

~~~python
import inspect
from thomaslab.drug_safety import audit_safety_windows

print(inspect.signature(audit_safety_windows))
print(audit_safety_windows.__doc__)
~~~

### Source

[`src/thomaslab/drug_safety.py#L167`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drug_safety.py#L167)

---

<!-- callable:thomaslab.drug_safety.link_exposure_events -->
## link_exposure_events

### Purpose

Link events to every explicit window in which they occur.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def link_exposure_events( windows: pd.DataFrame, events: pd.DataFrame, *, patient_col: str = "patient_id", event_col: str = "event_term", event_date_col: str = "event_date", window_id_col: str = "window_id", window_start_col: str = "window_start", window_end_col: str = "window_end", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `windows` | `windows: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str = 'event_term'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_date_col` | `event_date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `window_id_col` | `window_id_col: str = 'window_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `window_start_col` | `window_start_col: str = 'window_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `window_end_col` | `window_end_col: str = 'window_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `windows`, `events`.
- Referenced columns must exist in the input table: `patient_col`, `event_col`, `event_date_col`, `window_id_col`, `window_start_col`, `window_end_col`.

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

from thomaslab.drug_safety import link_exposure_events

result = link_exposure_events(
    windows=sample_df,
    events=sample_df
)

print(result)
~~~

### Related functions

- `validate_adverse_events`
- `build_exposure_risk_windows`
- `audit_safety_windows`
- `classify_seriousness_evidence`
- `map_severity`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drug_safety.py#L223`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drug_safety.py#L223)
- Repository search: [link_exposure_events](https://github.com/appsplorer/thomaslab-core/search?q=link_exposure_events&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Link events to every explicit window in which they occur.

### API inspection

~~~python
import inspect
from thomaslab.drug_safety import link_exposure_events

print(inspect.signature(link_exposure_events))
print(link_exposure_events.__doc__)
~~~

### Source

[`src/thomaslab/drug_safety.py#L223`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drug_safety.py#L223)

---

<!-- callable:thomaslab.drug_safety.classify_seriousness_evidence -->
## classify_seriousness_evidence

### Purpose

Aggregate explicit regulatory-style seriousness evidence.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def classify_seriousness_evidence( events: pd.DataFrame, *, evidence_columns: Mapping[str, str], ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `evidence_columns` | `evidence_columns: Mapping[str, str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`, `evidence_columns`.

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

from thomaslab.drug_safety import classify_seriousness_evidence

result = classify_seriousness_evidence(
    events=sample_df,
    evidence_columns=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `validate_adverse_events`
- `build_exposure_risk_windows`
- `audit_safety_windows`
- `link_exposure_events`
- `map_severity`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drug_safety.py#L277`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drug_safety.py#L277)
- Repository search: [classify_seriousness_evidence](https://github.com/appsplorer/thomaslab-core/search?q=classify_seriousness_evidence&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Aggregate explicit regulatory-style seriousness evidence.

Missing evidence remains unassessable. Seriousness is intentionally distinct from
clinical severity.

### API inspection

~~~python
import inspect
from thomaslab.drug_safety import classify_seriousness_evidence

print(inspect.signature(classify_seriousness_evidence))
print(classify_seriousness_evidence.__doc__)
~~~

### Source

[`src/thomaslab/drug_safety.py#L277`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drug_safety.py#L277)

---

<!-- callable:thomaslab.drug_safety.map_severity -->
## map_severity

### Purpose

Map source severity labels using a reviewed study mapping.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def map_severity( series: pd.Series, mapping: Mapping[str, str], *, allowed_levels: Sequence[str] = ("mild", "moderate", "severe"), strict: bool = False, ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `series` | `series: pd.Series` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `mapping` | `mapping: Mapping[str, str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `allowed_levels` | `allowed_levels: Sequence[str] = ('mild', 'moderate', 'severe')` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strict` | `strict: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `series`, `mapping`.

### Returns

`pd.Series`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.drug_safety import map_severity

result = map_severity(
    series=sample_series,
    mapping={}
)

print(result)
~~~

### Related functions

- `validate_adverse_events`
- `build_exposure_risk_windows`
- `audit_safety_windows`
- `link_exposure_events`
- `classify_seriousness_evidence`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drug_safety.py#L311`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drug_safety.py#L311)
- Repository search: [map_severity](https://github.com/appsplorer/thomaslab-core/search?q=map_severity&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Map source severity labels using a reviewed study mapping.

### API inspection

~~~python
import inspect
from thomaslab.drug_safety import map_severity

print(inspect.signature(map_severity))
print(map_severity.__doc__)
~~~

### Source

[`src/thomaslab/drug_safety.py#L311`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drug_safety.py#L311)

---

<!-- callable:thomaslab.drug_safety.build_drug_drug_interaction_table -->
## build_drug_drug_interaction_table

### Purpose

Build overlap intervals for an explicitly reviewed list of drug pairs.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_drug_drug_interaction_table( exposures: pd.DataFrame, interaction_definitions: pd.DataFrame, *, patient_col: str = "patient_id", drug_col: str = "drug", start_col: str = "episode_start", end_col: str = "episode_end", drug_a_col: str = "drug_a", drug_b_col: str = "drug_b", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `exposures` | `exposures: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `interaction_definitions` | `interaction_definitions: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'episode_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'episode_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_a_col` | `drug_a_col: str = 'drug_a'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_b_col` | `drug_b_col: str = 'drug_b'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `exposures`, `interaction_definitions`.
- Referenced columns must exist in the input table: `patient_col`, `drug_col`, `start_col`, `end_col`, `drug_a_col`, `drug_b_col`.

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

from thomaslab.drug_safety import build_drug_drug_interaction_table

result = build_drug_drug_interaction_table(
    exposures=sample_df,
    interaction_definitions=sample_df
)

print(result)
~~~

### Related functions

- `validate_adverse_events`
- `build_exposure_risk_windows`
- `audit_safety_windows`
- `link_exposure_events`
- `classify_seriousness_evidence`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drug_safety.py#L344`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drug_safety.py#L344)
- Repository search: [build_drug_drug_interaction_table](https://github.com/appsplorer/thomaslab-core/search?q=build_drug_drug_interaction_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build overlap intervals for an explicitly reviewed list of drug pairs.

### API inspection

~~~python
import inspect
from thomaslab.drug_safety import build_drug_drug_interaction_table

print(inspect.signature(build_drug_drug_interaction_table))
print(build_drug_drug_interaction_table.__doc__)
~~~

### Source

[`src/thomaslab/drug_safety.py#L344`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drug_safety.py#L344)

---

<!-- callable:thomaslab.drug_safety.build_dechallenge_rechallenge_timeline -->
## build_dechallenge_rechallenge_timeline

### Purpose

Build temporal dechallenge/rechallenge evidence without causal attribution.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_dechallenge_rechallenge_timeline( exposures: pd.DataFrame, events: pd.DataFrame, *, patient_col: str = "patient_id", drug_col: str = "drug", start_col: str = "episode_start", end_col: str = "episode_end", event_col: str = "event_term", event_date_col: str = "event_date", event_end_col: str | None = "event_end", max_link_days_after_exposure: int = 0, rechallenge_window_days: int = 30, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `exposures` | `exposures: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'episode_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'episode_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_col` | `event_col: str = 'event_term'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_date_col` | `event_date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_end_col` | `event_end_col: str \| None = 'event_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `max_link_days_after_exposure` | `max_link_days_after_exposure: int = 0` | No | Treatment/exposure definition supplied by the study specification; do not infer clinical meaning from labels alone. |
| `rechallenge_window_days` | `rechallenge_window_days: int = 30` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `exposures`, `events`.
- Referenced columns must exist in the input table: `patient_col`, `drug_col`, `start_col`, `end_col`, `event_col`, `event_date_col`, `event_end_col`.

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

from thomaslab.drug_safety import build_dechallenge_rechallenge_timeline

result = build_dechallenge_rechallenge_timeline(
    exposures=sample_df,
    events=sample_df
)

print(result)
~~~

### Related functions

- `validate_adverse_events`
- `build_exposure_risk_windows`
- `audit_safety_windows`
- `link_exposure_events`
- `classify_seriousness_evidence`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drug_safety.py#L418`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drug_safety.py#L418)
- Repository search: [build_dechallenge_rechallenge_timeline](https://github.com/appsplorer/thomaslab-core/search?q=build_dechallenge_rechallenge_timeline&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build temporal dechallenge/rechallenge evidence without causal attribution.

### API inspection

~~~python
import inspect
from thomaslab.drug_safety import build_dechallenge_rechallenge_timeline

print(inspect.signature(build_dechallenge_rechallenge_timeline))
print(build_dechallenge_rechallenge_timeline.__doc__)
~~~

### Source

[`src/thomaslab/drug_safety.py#L418`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drug_safety.py#L418)

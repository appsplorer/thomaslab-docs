# thomaslab.claims

Claims-oriented enrollment, index-event, pharmacy-initiation, and new-user cohort utilities.

## Research-use boundary

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

## Self-service orientation

- Related guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 8

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.claims.merge_enrollment_intervals -->
## merge_enrollment_intervals

### Purpose

Merge overlapping/near-contiguous insurance/enrollment intervals.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def merge_enrollment_intervals( enrollment: pd.DataFrame, *, patient_col: str = "patient_id", start_col: str = "enrollment_start", end_col: str = "enrollment_end", allowed_gap_days: int = 0, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `enrollment` | `enrollment: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'enrollment_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'enrollment_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `allowed_gap_days` | `allowed_gap_days: int = 0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `enrollment`.
- Referenced columns must exist in the input table: `patient_col`, `start_col`, `end_col`.

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

from thomaslab.claims import merge_enrollment_intervals

result = merge_enrollment_intervals(
    enrollment=sample_df
)

print(result)
~~~

### Related functions

- `identify_continuous_enrollment`
- `identify_index_events`
- `identify_prior_exposure`
- `identify_post_index_initiation`
- `build_new_user_cohort`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/claims.py#L17`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/claims.py#L17)
- Repository search: [merge_enrollment_intervals](https://github.com/appsplorer/thomaslab-core/search?q=merge_enrollment_intervals&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Merge overlapping/near-contiguous insurance/enrollment intervals.

### API inspection

~~~python
import inspect
from thomaslab.claims import merge_enrollment_intervals

print(inspect.signature(merge_enrollment_intervals))
print(merge_enrollment_intervals.__doc__)
~~~

### Source

[`src/thomaslab/claims.py#L17`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/claims.py#L17)

---

<!-- callable:thomaslab.claims.identify_continuous_enrollment -->
## identify_continuous_enrollment

### Purpose

Assess whether merged enrollment covers the full requested index-centered window.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def identify_continuous_enrollment( index: pd.DataFrame, enrollment: pd.DataFrame, *, patient_col: str = "patient_id", index_date_col: str = "index_date", lookback_days: int = 365, followup_days: int = 0, allowed_gap_days: int = 0, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `index` | `index: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `enrollment` | `enrollment: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `lookback_days` | `lookback_days: int = 365` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `followup_days` | `followup_days: int = 0` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `allowed_gap_days` | `allowed_gap_days: int = 0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `index`, `enrollment`.
- Referenced columns must exist in the input table: `patient_col`, `index_date_col`.

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

from thomaslab.claims import identify_continuous_enrollment

result = identify_continuous_enrollment(
    index=sample_df,
    enrollment=sample_df
)

print(result)
~~~

### Related functions

- `merge_enrollment_intervals`
- `identify_index_events`
- `identify_prior_exposure`
- `identify_post_index_initiation`
- `build_new_user_cohort`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/claims.py#L56`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/claims.py#L56)
- Repository search: [identify_continuous_enrollment](https://github.com/appsplorer/thomaslab-core/search?q=identify_continuous_enrollment&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Assess whether merged enrollment covers the full requested index-centered window.

### API inspection

~~~python
import inspect
from thomaslab.claims import identify_continuous_enrollment

print(inspect.signature(identify_continuous_enrollment))
print(identify_continuous_enrollment.__doc__)
~~~

### Source

[`src/thomaslab/claims.py#L56`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/claims.py#L56)

---

<!-- callable:thomaslab.claims.identify_index_events -->
## identify_index_events

### Purpose

Identify first qualifying coded event per patient using an explicit code list.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def identify_index_events( claims: pd.DataFrame, *, patient_col: str = "patient_id", date_col: str = "service_date", code_col: str = "code", index_codes: Sequence[str], match: str = "exact", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `claims` | `claims: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str = 'service_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `code_col` | `code_col: str = 'code'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_codes` | `index_codes: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `match` | `match: str = 'exact'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `claims`, `index_codes`.
- Referenced columns must exist in the input table: `patient_col`, `date_col`, `code_col`.

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

from thomaslab.claims import identify_index_events

result = identify_index_events(
    claims=sample_df,
    index_codes=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `merge_enrollment_intervals`
- `identify_continuous_enrollment`
- `identify_prior_exposure`
- `identify_post_index_initiation`
- `build_new_user_cohort`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/claims.py#L95`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/claims.py#L95)
- Repository search: [identify_index_events](https://github.com/appsplorer/thomaslab-core/search?q=identify_index_events&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Identify first qualifying coded event per patient using an explicit code list.

### API inspection

~~~python
import inspect
from thomaslab.claims import identify_index_events

print(inspect.signature(identify_index_events))
print(identify_index_events.__doc__)
~~~

### Source

[`src/thomaslab/claims.py#L95`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/claims.py#L95)

---

<!-- callable:thomaslab.claims.identify_prior_exposure -->
## identify_prior_exposure

### Purpose

Flag exposure during the pre-index washout window.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def identify_prior_exposure( pharmacy: pd.DataFrame, index: pd.DataFrame, *, patient_col: str = "patient_id", fill_date_col: str = "fill_date", index_date_col: str = "index_date", washout_days: int = 365, drug_col: str = "drug", target_drugs: Sequence[str] | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `pharmacy` | `pharmacy: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `index` | `index: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `fill_date_col` | `fill_date_col: str = 'fill_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `washout_days` | `washout_days: int = 365` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `target_drugs` | `target_drugs: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `pharmacy`, `index`.
- Referenced columns must exist in the input table: `patient_col`, `fill_date_col`, `index_date_col`, `drug_col`.

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

from thomaslab.claims import identify_prior_exposure

result = identify_prior_exposure(
    pharmacy=sample_df,
    index=sample_df
)

print(result)
~~~

### Related functions

- `merge_enrollment_intervals`
- `identify_continuous_enrollment`
- `identify_index_events`
- `identify_post_index_initiation`
- `build_new_user_cohort`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/claims.py#L132`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/claims.py#L132)
- Repository search: [identify_prior_exposure](https://github.com/appsplorer/thomaslab-core/search?q=identify_prior_exposure&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Flag exposure during the pre-index washout window.

### API inspection

~~~python
import inspect
from thomaslab.claims import identify_prior_exposure

print(inspect.signature(identify_prior_exposure))
print(identify_prior_exposure.__doc__)
~~~

### Source

[`src/thomaslab/claims.py#L132`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/claims.py#L132)

---

<!-- callable:thomaslab.claims.identify_post_index_initiation -->
## identify_post_index_initiation

### Purpose

Find the first target-drug fill from index through the configured initiation window.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def identify_post_index_initiation( pharmacy: pd.DataFrame, index: pd.DataFrame, *, patient_col: str = "patient_id", fill_date_col: str = "fill_date", index_date_col: str = "index_date", drug_col: str = "drug", target_drugs: Sequence[str] | None = None, initiation_window_days: int = 30, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `pharmacy` | `pharmacy: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `index` | `index: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `fill_date_col` | `fill_date_col: str = 'fill_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `target_drugs` | `target_drugs: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `initiation_window_days` | `initiation_window_days: int = 30` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `pharmacy`, `index`.
- Referenced columns must exist in the input table: `patient_col`, `fill_date_col`, `index_date_col`, `drug_col`.

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

from thomaslab.claims import identify_post_index_initiation

result = identify_post_index_initiation(
    pharmacy=sample_df,
    index=sample_df
)

print(result)
~~~

### Related functions

- `merge_enrollment_intervals`
- `identify_continuous_enrollment`
- `identify_index_events`
- `identify_prior_exposure`
- `build_new_user_cohort`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/claims.py#L174`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/claims.py#L174)
- Repository search: [identify_post_index_initiation](https://github.com/appsplorer/thomaslab-core/search?q=identify_post_index_initiation&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Find the first target-drug fill from index through the configured initiation window.

### API inspection

~~~python
import inspect
from thomaslab.claims import identify_post_index_initiation

print(inspect.signature(identify_post_index_initiation))
print(identify_post_index_initiation.__doc__)
~~~

### Source

[`src/thomaslab/claims.py#L174`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/claims.py#L174)

---

<!-- callable:thomaslab.claims.build_new_user_cohort -->
## build_new_user_cohort

### Purpose

Build a transparent claims-style new-user cohort without inventing index codes.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_new_user_cohort( index: pd.DataFrame, pharmacy: pd.DataFrame, enrollment: pd.DataFrame | None = None, *, patient_col: str = "patient_id", index_date_col: str = "index_date", fill_date_col: str = "fill_date", drug_col: str = "drug", target_drugs: Sequence[str] | None = None, washout_days: int = 365, initiation_window_days: int = 30, require_continuous_enrollment: bool = True, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `index` | `index: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `pharmacy` | `pharmacy: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `enrollment` | `enrollment: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `fill_date_col` | `fill_date_col: str = 'fill_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `target_drugs` | `target_drugs: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `washout_days` | `washout_days: int = 365` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `initiation_window_days` | `initiation_window_days: int = 30` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `require_continuous_enrollment` | `require_continuous_enrollment: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `index`, `pharmacy`.
- Referenced columns must exist in the input table: `patient_col`, `index_date_col`, `fill_date_col`, `drug_col`.

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

from thomaslab.claims import build_new_user_cohort

result = build_new_user_cohort(
    index=sample_df,
    pharmacy=sample_df
)

print(result)
~~~

### Related functions

- `merge_enrollment_intervals`
- `identify_continuous_enrollment`
- `identify_index_events`
- `identify_prior_exposure`
- `identify_post_index_initiation`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/claims.py#L230`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/claims.py#L230)
- Repository search: [build_new_user_cohort](https://github.com/appsplorer/thomaslab-core/search?q=build_new_user_cohort&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build a transparent claims-style new-user cohort without inventing index codes.

``index`` must already contain the study-defined index event. Eligibility requires no target
exposure during washout, target initiation during the post-index window, and optionally
continuous lookback enrollment.

### API inspection

~~~python
import inspect
from thomaslab.claims import build_new_user_cohort

print(inspect.signature(build_new_user_cohort))
print(build_new_user_cohort.__doc__)
~~~

### Source

[`src/thomaslab/claims.py#L230`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/claims.py#L230)

---

<!-- callable:thomaslab.claims.summarize_pharmacy_claims -->
## summarize_pharmacy_claims

### Purpose

Summarize pharmacy fills by patient/drug; monetary fields are optional and descriptive.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_pharmacy_claims( pharmacy: pd.DataFrame, *, patient_col: str = "patient_id", drug_col: str = "drug", fill_date_col: str = "fill_date", days_supply_col: str = "days_supply", paid_col: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `pharmacy` | `pharmacy: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `fill_date_col` | `fill_date_col: str = 'fill_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `days_supply_col` | `days_supply_col: str = 'days_supply'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `paid_col` | `paid_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `pharmacy`.
- Referenced columns must exist in the input table: `patient_col`, `drug_col`, `fill_date_col`, `days_supply_col`, `paid_col`.

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

from thomaslab.claims import summarize_pharmacy_claims

result = summarize_pharmacy_claims(
    pharmacy=sample_df
)

print(result)
~~~

### Related functions

- `merge_enrollment_intervals`
- `identify_continuous_enrollment`
- `identify_index_events`
- `identify_prior_exposure`
- `identify_post_index_initiation`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/claims.py#L319`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/claims.py#L319)
- Repository search: [summarize_pharmacy_claims](https://github.com/appsplorer/thomaslab-core/search?q=summarize_pharmacy_claims&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize pharmacy fills by patient/drug; monetary fields are optional and descriptive.

### API inspection

~~~python
import inspect
from thomaslab.claims import summarize_pharmacy_claims

print(inspect.signature(summarize_pharmacy_claims))
print(summarize_pharmacy_claims.__doc__)
~~~

### Source

[`src/thomaslab/claims.py#L319`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/claims.py#L319)

---

<!-- callable:thomaslab.claims.build_claims_study_dataset -->
## build_claims_study_dataset

### Purpose

Return one analysis row per eligible new user with index and initiation metadata.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_claims_study_dataset( index: pd.DataFrame, new_users: pd.DataFrame, *, patient_col: str = "patient_id", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `index` | `index: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `new_users` | `new_users: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `index`, `new_users`.
- Referenced columns must exist in the input table: `patient_col`.

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

from thomaslab.claims import build_claims_study_dataset

result = build_claims_study_dataset(
    index=sample_df,
    new_users=sample_df
)

print(result)
~~~

### Related functions

- `merge_enrollment_intervals`
- `identify_continuous_enrollment`
- `identify_index_events`
- `identify_prior_exposure`
- `identify_post_index_initiation`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/claims.py#L346`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/claims.py#L346)
- Repository search: [build_claims_study_dataset](https://github.com/appsplorer/thomaslab-core/search?q=build_claims_study_dataset&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return one analysis row per eligible new user with index and initiation metadata.

### API inspection

~~~python
import inspect
from thomaslab.claims import build_claims_study_dataset

print(inspect.signature(build_claims_study_dataset))
print(build_claims_study_dataset.__doc__)
~~~

### Source

[`src/thomaslab/claims.py#L346`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/claims.py#L346)

# thomaslab.pkpd

Pharmacokinetic and pharmacodynamic research utilities.

## Research-use boundary

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

## Self-service orientation

- Related guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 9

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.pkpd.validate_pk_samples -->
## validate_pk_samples

### Purpose

Validate PK samples and return a cleaned, sorted copy.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_pk_samples( df: pd.DataFrame, *, patient_col: str, time_col: str, concentration_col: str, dose_col: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `concentration_col` | `concentration_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `dose_col` | `dose_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `patient_col`, `time_col`, `concentration_col`.
- Referenced columns must exist in the input table: `patient_col`, `time_col`, `concentration_col`, `dose_col`.

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

from thomaslab.pkpd import validate_pk_samples

result = validate_pk_samples(
    df=sample_df,
    patient_col='patient_id',
    time_col='event_date',
    concentration_col='concentration'
)

print(result)
~~~

### Related functions

- `calculate_auc`
- `calculate_cmax_tmax`
- `estimate_terminal_half_life`
- `calculate_apparent_clearance`
- `dose_normalize_exposure`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pkpd.py#L17`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pkpd.py#L17)
- Repository search: [validate_pk_samples](https://github.com/appsplorer/thomaslab-core/search?q=validate_pk_samples&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate PK samples and return a cleaned, sorted copy.

Duplicate patient/time rows are rejected because averaging replicate assay
measurements is a study decision and should not happen silently.

### API inspection

~~~python
import inspect
from thomaslab.pkpd import validate_pk_samples

print(inspect.signature(validate_pk_samples))
print(validate_pk_samples.__doc__)
~~~

### Source

[`src/thomaslab/pkpd.py#L17`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pkpd.py#L17)

---

<!-- callable:thomaslab.pkpd.calculate_auc -->
## calculate_auc

### Purpose

Calculate observed concentration-time AUC over the supplied interval.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_auc( time: Iterable[float], concentration: Iterable[float], *, method: str = "linear_trapezoidal", ) -> float
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `time` | `time: Iterable[float]` | Yes | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `concentration` | `concentration: Iterable[float]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `method` | `method: str = 'linear_trapezoidal'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `time`, `concentration`.

### Returns

`float`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.pkpd import calculate_auc

result = calculate_auc(
    time=0.5,
    concentration=0.5
)

print(result)
~~~

### Related functions

- `validate_pk_samples`
- `calculate_cmax_tmax`
- `estimate_terminal_half_life`
- `calculate_apparent_clearance`
- `dose_normalize_exposure`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pkpd.py#L54`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pkpd.py#L54)
- Repository search: [calculate_auc](https://github.com/appsplorer/thomaslab-core/search?q=calculate_auc&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate observed concentration-time AUC over the supplied interval.

### API inspection

~~~python
import inspect
from thomaslab.pkpd import calculate_auc

print(inspect.signature(calculate_auc))
print(calculate_auc.__doc__)
~~~

### Source

[`src/thomaslab/pkpd.py#L54`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pkpd.py#L54)

---

<!-- callable:thomaslab.pkpd.calculate_cmax_tmax -->
## calculate_cmax_tmax

### Purpose

Return observed Cmax and earliest Tmax.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_cmax_tmax( time: Iterable[float], concentration: Iterable[float], ) -> dict[str, float]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `time` | `time: Iterable[float]` | Yes | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `concentration` | `concentration: Iterable[float]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `time`, `concentration`.

### Returns

`dict[str, float]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.pkpd import calculate_cmax_tmax

result = calculate_cmax_tmax(
    time=0.5,
    concentration=0.5
)

print(result)
~~~

### Related functions

- `validate_pk_samples`
- `calculate_auc`
- `estimate_terminal_half_life`
- `calculate_apparent_clearance`
- `dose_normalize_exposure`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pkpd.py#L78`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pkpd.py#L78)
- Repository search: [calculate_cmax_tmax](https://github.com/appsplorer/thomaslab-core/search?q=calculate_cmax_tmax&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return observed Cmax and earliest Tmax.

### API inspection

~~~python
import inspect
from thomaslab.pkpd import calculate_cmax_tmax

print(inspect.signature(calculate_cmax_tmax))
print(calculate_cmax_tmax.__doc__)
~~~

### Source

[`src/thomaslab/pkpd.py#L78`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pkpd.py#L78)

---

<!-- callable:thomaslab.pkpd.estimate_terminal_half_life -->
## estimate_terminal_half_life

### Purpose

Estimate terminal half-life from the last positive concentrations.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def estimate_terminal_half_life( time: Iterable[float], concentration: Iterable[float], *, terminal_n_points: int = 3, min_r_squared: float | None = None, ) -> dict[str, float]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `time` | `time: Iterable[float]` | Yes | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `concentration` | `concentration: Iterable[float]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `terminal_n_points` | `terminal_n_points: int = 3` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `min_r_squared` | `min_r_squared: float \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `time`, `concentration`.

### Returns

`dict[str, float]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.pkpd import estimate_terminal_half_life

result = estimate_terminal_half_life(
    time=0.5,
    concentration=0.5
)

print(result)
~~~

### Related functions

- `validate_pk_samples`
- `calculate_auc`
- `calculate_cmax_tmax`
- `calculate_apparent_clearance`
- `dose_normalize_exposure`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pkpd.py#L96`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pkpd.py#L96)
- Repository search: [estimate_terminal_half_life](https://github.com/appsplorer/thomaslab-core/search?q=estimate_terminal_half_life&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate terminal half-life from the last positive concentrations.

### API inspection

~~~python
import inspect
from thomaslab.pkpd import estimate_terminal_half_life

print(inspect.signature(estimate_terminal_half_life))
print(estimate_terminal_half_life.__doc__)
~~~

### Source

[`src/thomaslab/pkpd.py#L96`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pkpd.py#L96)

---

<!-- callable:thomaslab.pkpd.calculate_apparent_clearance -->
## calculate_apparent_clearance

### Purpose

Calculate dose/AUC apparent clearance (CL/F unless F is known).

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_apparent_clearance( dose: float, auc: float, *, bioavailability: float | None = None, ) -> float
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `dose` | `dose: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `auc` | `auc: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `bioavailability` | `bioavailability: float \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `dose`, `auc`.

### Returns

`float`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.pkpd import calculate_apparent_clearance

result = calculate_apparent_clearance(
    dose=0.5,
    auc=0.5
)

print(result)
~~~

### Related functions

- `validate_pk_samples`
- `calculate_auc`
- `calculate_cmax_tmax`
- `estimate_terminal_half_life`
- `dose_normalize_exposure`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pkpd.py#L136`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pkpd.py#L136)
- Repository search: [calculate_apparent_clearance](https://github.com/appsplorer/thomaslab-core/search?q=calculate_apparent_clearance&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate dose/AUC apparent clearance (CL/F unless F is known).

### API inspection

~~~python
import inspect
from thomaslab.pkpd import calculate_apparent_clearance

print(inspect.signature(calculate_apparent_clearance))
print(calculate_apparent_clearance.__doc__)
~~~

### Source

[`src/thomaslab/pkpd.py#L136`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pkpd.py#L136)

---

<!-- callable:thomaslab.pkpd.dose_normalize_exposure -->
## dose_normalize_exposure

### Purpose

Return exposure per unit dose.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def dose_normalize_exposure(exposure: float, dose: float) -> float
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `exposure` | `exposure: float` | Yes | Treatment/exposure definition supplied by the study specification; do not infer clinical meaning from labels alone. |
| `dose` | `dose: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `exposure`, `dose`.

### Returns

`float`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.pkpd import dose_normalize_exposure

result = dose_normalize_exposure(
    exposure=0.5,
    dose=0.5
)

print(result)
~~~

### Related functions

- `validate_pk_samples`
- `calculate_auc`
- `calculate_cmax_tmax`
- `estimate_terminal_half_life`
- `calculate_apparent_clearance`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pkpd.py#L155`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pkpd.py#L155)
- Repository search: [dose_normalize_exposure](https://github.com/appsplorer/thomaslab-core/search?q=dose_normalize_exposure&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return exposure per unit dose.

### API inspection

~~~python
import inspect
from thomaslab.pkpd import dose_normalize_exposure

print(inspect.signature(dose_normalize_exposure))
print(dose_normalize_exposure.__doc__)
~~~

### Source

[`src/thomaslab/pkpd.py#L155`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pkpd.py#L155)

---

<!-- callable:thomaslab.pkpd.build_pk_profile -->
## build_pk_profile

### Purpose

Build one-row-per-patient observed PK summaries.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_pk_profile( samples: pd.DataFrame, *, patient_col: str, time_col: str, concentration_col: str, dose_col: str | None = None, terminal_n_points: int | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `samples` | `samples: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `concentration_col` | `concentration_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `dose_col` | `dose_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `terminal_n_points` | `terminal_n_points: int \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `samples`, `patient_col`, `time_col`, `concentration_col`.
- Referenced columns must exist in the input table: `patient_col`, `time_col`, `concentration_col`, `dose_col`.

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

from thomaslab.pkpd import build_pk_profile

result = build_pk_profile(
    samples=sample_df,
    patient_col='patient_id',
    time_col='event_date',
    concentration_col='concentration'
)

print(result)
~~~

### Related functions

- `validate_pk_samples`
- `calculate_auc`
- `calculate_cmax_tmax`
- `estimate_terminal_half_life`
- `calculate_apparent_clearance`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pkpd.py#L163`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pkpd.py#L163)
- Repository search: [build_pk_profile](https://github.com/appsplorer/thomaslab-core/search?q=build_pk_profile&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build one-row-per-patient observed PK summaries.

### API inspection

~~~python
import inspect
from thomaslab.pkpd import build_pk_profile

print(inspect.signature(build_pk_profile))
print(build_pk_profile.__doc__)
~~~

### Source

[`src/thomaslab/pkpd.py#L163`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pkpd.py#L163)

---

<!-- callable:thomaslab.pkpd.calculate_baseline_adjusted_pd_change -->
## calculate_baseline_adjusted_pd_change

### Purpose

Calculate within-patient PD change from an explicit baseline time.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_baseline_adjusted_pd_change( df: pd.DataFrame, *, patient_col: str, value_col: str, time_col: str, baseline_time: float = 0.0, followup_time: float | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `value_col` | `value_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `baseline_time` | `baseline_time: float = 0.0` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `followup_time` | `followup_time: float \| None = None` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `patient_col`, `value_col`, `time_col`.
- Referenced columns must exist in the input table: `patient_col`, `value_col`, `time_col`.

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

from thomaslab.pkpd import calculate_baseline_adjusted_pd_change

result = calculate_baseline_adjusted_pd_change(
    df=sample_df,
    patient_col='patient_id',
    value_col='value',
    time_col='event_date'
)

print(result)
~~~

### Related functions

- `validate_pk_samples`
- `calculate_auc`
- `calculate_cmax_tmax`
- `estimate_terminal_half_life`
- `calculate_apparent_clearance`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pkpd.py#L217`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pkpd.py#L217)
- Repository search: [calculate_baseline_adjusted_pd_change](https://github.com/appsplorer/thomaslab-core/search?q=calculate_baseline_adjusted_pd_change&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate within-patient PD change from an explicit baseline time.

### API inspection

~~~python
import inspect
from thomaslab.pkpd import calculate_baseline_adjusted_pd_change

print(inspect.signature(calculate_baseline_adjusted_pd_change))
print(calculate_baseline_adjusted_pd_change.__doc__)
~~~

### Source

[`src/thomaslab/pkpd.py#L217`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pkpd.py#L217)

---

<!-- callable:thomaslab.pkpd.build_pgx_pkpd_dataset -->
## build_pgx_pkpd_dataset

### Purpose

Join one-row-per-patient PK, PGx, PD, and drug summaries.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_pgx_pkpd_dataset( pk_profile: pd.DataFrame, *, pgx: pd.DataFrame | None = None, pd_summary: pd.DataFrame | None = None, drug_exposure: pd.DataFrame | None = None, patient_col: str = "patient_id", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `pk_profile` | `pk_profile: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `pgx` | `pgx: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `pd_summary` | `pd_summary: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `drug_exposure` | `drug_exposure: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `pk_profile`.
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

from thomaslab.pkpd import build_pgx_pkpd_dataset

result = build_pgx_pkpd_dataset(
    pk_profile=sample_df
)

print(result)
~~~

### Related functions

- `validate_pk_samples`
- `calculate_auc`
- `calculate_cmax_tmax`
- `estimate_terminal_half_life`
- `calculate_apparent_clearance`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pkpd.py#L261`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pkpd.py#L261)
- Repository search: [build_pgx_pkpd_dataset](https://github.com/appsplorer/thomaslab-core/search?q=build_pgx_pkpd_dataset&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Join one-row-per-patient PK, PGx, PD, and drug summaries.

### API inspection

~~~python
import inspect
from thomaslab.pkpd import build_pgx_pkpd_dataset

print(inspect.signature(build_pgx_pkpd_dataset))
print(build_pgx_pkpd_dataset.__doc__)
~~~

### Source

[`src/thomaslab/pkpd.py#L261`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pkpd.py#L261)

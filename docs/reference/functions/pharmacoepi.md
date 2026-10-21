# thomaslab.pharmacoepi

Pharmacoepidemiology design diagnostics and negative-control scaffolding.

## Research-use boundary

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

## Self-service orientation

- Related guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 6

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.pharmacoepi.summarize_new_user_design -->
## summarize_new_user_design

### Purpose

Summarize active-comparator new-user eligibility and exclusion reasons.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_new_user_design( cohort: pd.DataFrame, *, arm_col: str = "treatment_arm", eligibility_col: str = "eligible_active_comparator_new_user", status_col: str = "eligibility_status", ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `cohort` | `cohort: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `arm_col` | `arm_col: str = 'treatment_arm'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `eligibility_col` | `eligibility_col: str = 'eligible_active_comparator_new_user'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `status_col` | `status_col: str = 'eligibility_status'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `cohort`.
- Referenced columns must exist in the input table: `arm_col`, `eligibility_col`, `status_col`.

### Returns

`dict[str, Any]`

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

from thomaslab.pharmacoepi import summarize_new_user_design

result = summarize_new_user_design(
    cohort=sample_df
)

print(result)
~~~

### Related functions

- `calculate_treatment_switching`
- `negative_control_outcome_table`
- `negative_control_exposure_table`
- `audit_negative_control_spec`
- `build_protocol_deviation_table`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pharmacoepi.py#L18`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pharmacoepi.py#L18)
- Repository search: [summarize_new_user_design](https://github.com/appsplorer/thomaslab-core/search?q=summarize_new_user_design&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize active-comparator new-user eligibility and exclusion reasons.

### API inspection

~~~python
import inspect
from thomaslab.pharmacoepi import summarize_new_user_design

print(inspect.signature(summarize_new_user_design))
print(summarize_new_user_design.__doc__)
~~~

### Source

[`src/thomaslab/pharmacoepi.py#L18`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pharmacoepi.py#L18)

---

<!-- callable:thomaslab.pharmacoepi.calculate_treatment_switching -->
## calculate_treatment_switching

### Purpose

Summarize observed switching/discontinuation dates descriptively.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_treatment_switching( deviations: pd.DataFrame, *, switch_date_col: str = "switch_date", discontinuation_date_col: str = "discontinuation_date", ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `deviations` | `deviations: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `switch_date_col` | `switch_date_col: str = 'switch_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `discontinuation_date_col` | `discontinuation_date_col: str = 'discontinuation_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `deviations`.
- Referenced columns must exist in the input table: `switch_date_col`, `discontinuation_date_col`.

### Returns

`dict[str, Any]`

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

from thomaslab.pharmacoepi import calculate_treatment_switching

result = calculate_treatment_switching(
    deviations=sample_df
)

print(result)
~~~

### Related functions

- `summarize_new_user_design`
- `negative_control_outcome_table`
- `negative_control_exposure_table`
- `audit_negative_control_spec`
- `build_protocol_deviation_table`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pharmacoepi.py#L47`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pharmacoepi.py#L47)
- Repository search: [calculate_treatment_switching](https://github.com/appsplorer/thomaslab-core/search?q=calculate_treatment_switching&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize observed switching/discontinuation dates descriptively.

### API inspection

~~~python
import inspect
from thomaslab.pharmacoepi import calculate_treatment_switching

print(inspect.signature(calculate_treatment_switching))
print(calculate_treatment_switching.__doc__)
~~~

### Source

[`src/thomaslab/pharmacoepi.py#L47`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pharmacoepi.py#L47)

---

<!-- callable:thomaslab.pharmacoepi.negative_control_outcome_table -->
## negative_control_outcome_table

### Purpose

Compute crude binary risks by treatment for study-specified negative controls.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def negative_control_outcome_table( df: pd.DataFrame, *, treatment_col: str, negative_control_outcomes: Sequence[str], ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `negative_control_outcomes` | `negative_control_outcomes: Sequence[str]` | Yes | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `negative_control_outcomes`.
- Referenced columns must exist in the input table: `treatment_col`.

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

from thomaslab.pharmacoepi import negative_control_outcome_table

result = negative_control_outcome_table(
    df=sample_df,
    treatment_col='treatment',
    negative_control_outcomes=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `summarize_new_user_design`
- `calculate_treatment_switching`
- `negative_control_exposure_table`
- `audit_negative_control_spec`
- `build_protocol_deviation_table`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pharmacoepi.py#L66`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pharmacoepi.py#L66)
- Repository search: [negative_control_outcome_table](https://github.com/appsplorer/thomaslab-core/search?q=negative_control_outcome_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compute crude binary risks by treatment for study-specified negative controls.

### API inspection

~~~python
import inspect
from thomaslab.pharmacoepi import negative_control_outcome_table

print(inspect.signature(negative_control_outcome_table))
print(negative_control_outcome_table.__doc__)
~~~

### Source

[`src/thomaslab/pharmacoepi.py#L66`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pharmacoepi.py#L66)

---

<!-- callable:thomaslab.pharmacoepi.negative_control_exposure_table -->
## negative_control_exposure_table

### Purpose

Compute crude outcome risks across study-specified binary negative-control exposures.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def negative_control_exposure_table( df: pd.DataFrame, *, outcome_col: str, negative_control_exposures: Sequence[str], ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `negative_control_exposures` | `negative_control_exposures: Sequence[str]` | Yes | Treatment/exposure definition supplied by the study specification; do not infer clinical meaning from labels alone. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `outcome_col`, `negative_control_exposures`.
- Referenced columns must exist in the input table: `outcome_col`.

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

from thomaslab.pharmacoepi import negative_control_exposure_table

result = negative_control_exposure_table(
    df=sample_df,
    outcome_col='outcome',
    negative_control_exposures=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `summarize_new_user_design`
- `calculate_treatment_switching`
- `negative_control_outcome_table`
- `audit_negative_control_spec`
- `build_protocol_deviation_table`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pharmacoepi.py#L96`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pharmacoepi.py#L96)
- Repository search: [negative_control_exposure_table](https://github.com/appsplorer/thomaslab-core/search?q=negative_control_exposure_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compute crude outcome risks across study-specified binary negative-control exposures.

### API inspection

~~~python
import inspect
from thomaslab.pharmacoepi import negative_control_exposure_table

print(inspect.signature(negative_control_exposure_table))
print(negative_control_exposure_table.__doc__)
~~~

### Source

[`src/thomaslab/pharmacoepi.py#L96`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pharmacoepi.py#L96)

---

<!-- callable:thomaslab.pharmacoepi.audit_negative_control_spec -->
## audit_negative_control_spec

### Purpose

Audit whether negative controls have explicit rationale strings.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_negative_control_spec( *, outcome_controls: Mapping[str, str] | None = None, exposure_controls: Mapping[str, str] | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `outcome_controls` | `outcome_controls: Mapping[str, str] \| None = None` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `exposure_controls` | `exposure_controls: Mapping[str, str] \| None = None` | No | Treatment/exposure definition supplied by the study specification; do not infer clinical meaning from labels alone. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- This callable has no required public arguments beyond instance/class construction.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.pharmacoepi import audit_negative_control_spec

result = audit_negative_control_spec()

print(result)
~~~

### Related functions

- `summarize_new_user_design`
- `calculate_treatment_switching`
- `negative_control_outcome_table`
- `negative_control_exposure_table`
- `build_protocol_deviation_table`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pharmacoepi.py#L126`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pharmacoepi.py#L126)
- Repository search: [audit_negative_control_spec](https://github.com/appsplorer/thomaslab-core/search?q=audit_negative_control_spec&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Audit whether negative controls have explicit rationale strings.

### API inspection

~~~python
import inspect
from thomaslab.pharmacoepi import audit_negative_control_spec

print(inspect.signature(audit_negative_control_spec))
print(audit_negative_control_spec.__doc__)
~~~

### Source

[`src/thomaslab/pharmacoepi.py#L126`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pharmacoepi.py#L126)

---

<!-- callable:thomaslab.pharmacoepi.build_protocol_deviation_table -->
## build_protocol_deviation_table

### Purpose

Create one review table containing treatment assignment and deviation dates.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_protocol_deviation_table( cohort: pd.DataFrame, deviations: pd.DataFrame, *, patient_col: str = "patient_id", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `cohort` | `cohort: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `deviations` | `deviations: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `cohort`, `deviations`.
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

from thomaslab.pharmacoepi import build_protocol_deviation_table

result = build_protocol_deviation_table(
    cohort=sample_df,
    deviations=sample_df
)

print(result)
~~~

### Related functions

- `summarize_new_user_design`
- `calculate_treatment_switching`
- `negative_control_outcome_table`
- `negative_control_exposure_table`
- `audit_negative_control_spec`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pharmacoepi.py#L145`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pharmacoepi.py#L145)
- Repository search: [build_protocol_deviation_table](https://github.com/appsplorer/thomaslab-core/search?q=build_protocol_deviation_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create one review table containing treatment assignment and deviation dates.

### API inspection

~~~python
import inspect
from thomaslab.pharmacoepi import build_protocol_deviation_table

print(inspect.signature(build_protocol_deviation_table))
print(build_protocol_deviation_table.__doc__)
~~~

### Source

[`src/thomaslab/pharmacoepi.py#L145`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pharmacoepi.py#L145)

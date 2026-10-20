# thomaslab.target_trial

Target-trial-style pharmacoepidemiology study-design utilities.

These helpers encode protocol structure and follow-up mechanics for observational
research. They do not establish exchangeability, randomization, or causal validity.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 11

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.target_trial.TargetTrialSpec.to_dict -->
## TargetTrialSpec.to_dict

### Purpose

Serialize the protocol skeleton to a plain dictionary.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def to_dict(self) -> dict[str, Any]
~~~

### Parameters

This callable has no public parameters beyond instance/class binding.

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

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.target_trial import TargetTrialSpec

# Construct TargetTrialSpec with its documented constructor first.
# instance = TargetTrialSpec(...)
result = instance.to_dict()

print(result)
~~~

### Related functions

- `validate_target_trial_spec`
- `load_target_trial_spec`
- `build_active_comparator_new_user_cohort`
- `build_itt_followup`
- `identify_treatment_deviation`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/target_trial.py#L40`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L40)
- Repository search: [TargetTrialSpec.to_dict](https://github.com/appsplorer/thomaslab-core/search?q=TargetTrialSpec.to_dict&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Serialize the protocol skeleton to a plain dictionary.

### API inspection

~~~python
import inspect
from thomaslab.target_trial import TargetTrialSpec

print(inspect.signature(TargetTrialSpec.to_dict))
print(TargetTrialSpec.to_dict.__doc__)
~~~

### Source

[`src/thomaslab/target_trial.py#L40`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L40)

---

<!-- callable:thomaslab.target_trial.validate_target_trial_spec -->
## validate_target_trial_spec

### Purpose

Validate required target-trial protocol sections without inventing semantics.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_target_trial_spec(spec: Mapping[str, Any]) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `spec` | `spec: Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `spec`.

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
from thomaslab.target_trial import validate_target_trial_spec

result = validate_target_trial_spec(
    spec={}
)

print(result)
~~~

### Related functions

- `TargetTrialSpec.to_dict`
- `load_target_trial_spec`
- `build_active_comparator_new_user_cohort`
- `build_itt_followup`
- `identify_treatment_deviation`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/target_trial.py#L45`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L45)
- Repository search: [validate_target_trial_spec](https://github.com/appsplorer/thomaslab-core/search?q=validate_target_trial_spec&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate required target-trial protocol sections without inventing semantics.

### API inspection

~~~python
import inspect
from thomaslab.target_trial import validate_target_trial_spec

print(inspect.signature(validate_target_trial_spec))
print(validate_target_trial_spec.__doc__)
~~~

### Source

[`src/thomaslab/target_trial.py#L45`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L45)

---

<!-- callable:thomaslab.target_trial.load_target_trial_spec -->
## load_target_trial_spec

### Purpose

Load a YAML/JSON target-trial specification and validate its structure.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def load_target_trial_spec(spec: str | Path | Mapping[str, Any]) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `spec` | `spec: str \| Path \| Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `spec`.

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
from thomaslab.target_trial import load_target_trial_spec

result = load_target_trial_spec(
    spec={}
)

print(result)
~~~

### Related functions

- `TargetTrialSpec.to_dict`
- `validate_target_trial_spec`
- `build_active_comparator_new_user_cohort`
- `build_itt_followup`
- `identify_treatment_deviation`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/target_trial.py#L71`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L71)
- Repository search: [load_target_trial_spec](https://github.com/appsplorer/thomaslab-core/search?q=load_target_trial_spec&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Load a YAML/JSON target-trial specification and validate its structure.

### API inspection

~~~python
import inspect
from thomaslab.target_trial import load_target_trial_spec

print(inspect.signature(load_target_trial_spec))
print(load_target_trial_spec.__doc__)
~~~

### Source

[`src/thomaslab/target_trial.py#L71`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L71)

---

<!-- callable:thomaslab.target_trial.build_active_comparator_new_user_cohort -->
## build_active_comparator_new_user_cohort

### Purpose

Build a mutually exclusive active-comparator new-user cohort.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_active_comparator_new_user_cohort( index: pd.DataFrame, pharmacy: pd.DataFrame, *, patient_col: str = "patient_id", index_date_col: str = "index_date", fill_date_col: str = "fill_date", drug_col: str = "drug", target_drugs: Sequence[str], comparator_drugs: Sequence[str], washout_days: int = 365, initiation_window_days: int = 0, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `index` | `index: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `pharmacy` | `pharmacy: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `fill_date_col` | `fill_date_col: str = 'fill_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `target_drugs` | `target_drugs: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `comparator_drugs` | `comparator_drugs: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `washout_days` | `washout_days: int = 365` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `initiation_window_days` | `initiation_window_days: int = 0` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `index`, `pharmacy`, `target_drugs`, `comparator_drugs`.
- Referenced columns must exist in the input table: `patient_col`, `index_date_col`, `fill_date_col`, `drug_col`.

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

from thomaslab.target_trial import build_active_comparator_new_user_cohort

result = build_active_comparator_new_user_cohort(
    index=sample_df,
    pharmacy=sample_df,
    target_drugs=["feature_a", "feature_b"],
    comparator_drugs=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `TargetTrialSpec.to_dict`
- `validate_target_trial_spec`
- `load_target_trial_spec`
- `build_itt_followup`
- `identify_treatment_deviation`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/target_trial.py#L91`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L91)
- Repository search: [build_active_comparator_new_user_cohort](https://github.com/appsplorer/thomaslab-core/search?q=build_active_comparator_new_user_cohort&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build a mutually exclusive active-comparator new-user cohort.

Patients with prior exposure to either study arm during washout are excluded.
Initiation is determined from the first qualifying fill inside the explicit
post-index initiation window. Ties/multiple-arm initiations on the first date
are labelled ambiguous and excluded rather than resolved heuristically.

### API inspection

~~~python
import inspect
from thomaslab.target_trial import build_active_comparator_new_user_cohort

print(inspect.signature(build_active_comparator_new_user_cohort))
print(build_active_comparator_new_user_cohort.__doc__)
~~~

### Source

[`src/thomaslab/target_trial.py#L91`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L91)

---

<!-- callable:thomaslab.target_trial.build_itt_followup -->
## build_itt_followup

### Purpose

Construct an ITT-like observational follow-up window.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_itt_followup( cohort: pd.DataFrame, *, patient_col: str = "patient_id", time_zero_col: str = "initiation_date", administrative_end: str | pd.Timestamp, outcome_date_col: str | None = None, death_date_col: str | None = None, disenrollment_date_col: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `cohort` | `cohort: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_zero_col` | `time_zero_col: str = 'initiation_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `administrative_end` | `administrative_end: str \| pd.Timestamp` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `outcome_date_col` | `outcome_date_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `death_date_col` | `death_date_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `disenrollment_date_col` | `disenrollment_date_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `cohort`, `administrative_end`.
- Referenced columns must exist in the input table: `patient_col`, `time_zero_col`, `outcome_date_col`, `death_date_col`, `disenrollment_date_col`.

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

from thomaslab.target_trial import build_itt_followup

result = build_itt_followup(
    cohort=sample_df,
    administrative_end="value"
)

print(result)
~~~

### Related functions

- `TargetTrialSpec.to_dict`
- `validate_target_trial_spec`
- `load_target_trial_spec`
- `build_active_comparator_new_user_cohort`
- `identify_treatment_deviation`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/target_trial.py#L183`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L183)
- Repository search: [build_itt_followup](https://github.com/appsplorer/thomaslab-core/search?q=build_itt_followup&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Construct an ITT-like observational follow-up window.

### API inspection

~~~python
import inspect
from thomaslab.target_trial import build_itt_followup

print(inspect.signature(build_itt_followup))
print(build_itt_followup.__doc__)
~~~

### Source

[`src/thomaslab/target_trial.py#L183`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L183)

---

<!-- callable:thomaslab.target_trial.identify_treatment_deviation -->
## identify_treatment_deviation

### Purpose

Identify first post-initiation switch or discontinuation.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def identify_treatment_deviation( cohort: pd.DataFrame, exposures: pd.DataFrame, *, patient_col: str = "patient_id", arm_col: str = "treatment_arm", start_col: str = "episode_start", end_col: str = "episode_end", drug_col: str = "drug", target_drugs: Sequence[str], comparator_drugs: Sequence[str], grace_days: int = 0, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `cohort` | `cohort: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `exposures` | `exposures: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `arm_col` | `arm_col: str = 'treatment_arm'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'episode_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'episode_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `target_drugs` | `target_drugs: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `comparator_drugs` | `comparator_drugs: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `grace_days` | `grace_days: int = 0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `cohort`, `exposures`, `target_drugs`, `comparator_drugs`.
- Referenced columns must exist in the input table: `patient_col`, `arm_col`, `start_col`, `end_col`, `drug_col`.

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

from thomaslab.target_trial import identify_treatment_deviation

result = identify_treatment_deviation(
    cohort=sample_df,
    exposures=sample_df,
    target_drugs=["feature_a", "feature_b"],
    comparator_drugs=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `TargetTrialSpec.to_dict`
- `validate_target_trial_spec`
- `load_target_trial_spec`
- `build_active_comparator_new_user_cohort`
- `build_itt_followup`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/target_trial.py#L235`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L235)
- Repository search: [identify_treatment_deviation](https://github.com/appsplorer/thomaslab-core/search?q=identify_treatment_deviation&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Identify first post-initiation switch or discontinuation.

Exposure rows are expected to represent already-built coverage episodes. A
discontinuation is placed after the first own-arm episode that contains or
follows treatment initiation, plus the explicit grace period. Later restarts
do not erase that first deviation. Cross-arm episodes that begin before time
zero are ignored rather than treated as post-initiation switches.

### API inspection

~~~python
import inspect
from thomaslab.target_trial import identify_treatment_deviation

print(inspect.signature(identify_treatment_deviation))
print(identify_treatment_deviation.__doc__)
~~~

### Source

[`src/thomaslab/target_trial.py#L235`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L235)

---

<!-- callable:thomaslab.target_trial.build_as_treated_followup -->
## build_as_treated_followup

### Purpose

Construct as-treated follow-up censored at the first supplied treatment deviation.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_as_treated_followup( cohort: pd.DataFrame, deviations: pd.DataFrame, *, patient_col: str = "patient_id", time_zero_col: str = "initiation_date", administrative_end: str | pd.Timestamp, outcome_date_col: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `cohort` | `cohort: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `deviations` | `deviations: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_zero_col` | `time_zero_col: str = 'initiation_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `administrative_end` | `administrative_end: str \| pd.Timestamp` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `outcome_date_col` | `outcome_date_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `cohort`, `deviations`, `administrative_end`.
- Referenced columns must exist in the input table: `patient_col`, `time_zero_col`, `outcome_date_col`.

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

from thomaslab.target_trial import build_as_treated_followup

result = build_as_treated_followup(
    cohort=sample_df,
    deviations=sample_df,
    administrative_end="value"
)

print(result)
~~~

### Related functions

- `TargetTrialSpec.to_dict`
- `validate_target_trial_spec`
- `load_target_trial_spec`
- `build_active_comparator_new_user_cohort`
- `build_itt_followup`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/target_trial.py#L325`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L325)
- Repository search: [build_as_treated_followup](https://github.com/appsplorer/thomaslab-core/search?q=build_as_treated_followup&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Construct as-treated follow-up censored at the first supplied treatment deviation.

### API inspection

~~~python
import inspect
from thomaslab.target_trial import build_as_treated_followup

print(inspect.signature(build_as_treated_followup))
print(build_as_treated_followup.__doc__)
~~~

### Source

[`src/thomaslab/target_trial.py#L325`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L325)

---

<!-- callable:thomaslab.target_trial.generate_censoring_table -->
## generate_censoring_table

### Purpose

Summarize follow-up termination reasons without causal interpretation.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def generate_censoring_table( followup: pd.DataFrame, *, reason_col: str = "censor_or_event_reason", arm_col: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `followup` | `followup: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `reason_col` | `reason_col: str = 'censor_or_event_reason'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `arm_col` | `arm_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `followup`.
- Referenced columns must exist in the input table: `reason_col`, `arm_col`.

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

from thomaslab.target_trial import generate_censoring_table

result = generate_censoring_table(
    followup=sample_df
)

print(result)
~~~

### Related functions

- `TargetTrialSpec.to_dict`
- `validate_target_trial_spec`
- `load_target_trial_spec`
- `build_active_comparator_new_user_cohort`
- `build_itt_followup`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/target_trial.py#L382`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L382)
- Repository search: [generate_censoring_table](https://github.com/appsplorer/thomaslab-core/search?q=generate_censoring_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize follow-up termination reasons without causal interpretation.

### API inspection

~~~python
import inspect
from thomaslab.target_trial import generate_censoring_table

print(inspect.signature(generate_censoring_table))
print(generate_censoring_table.__doc__)
~~~

### Source

[`src/thomaslab/target_trial.py#L382`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L382)

---

<!-- callable:thomaslab.target_trial.audit_target_trial_alignment -->
## audit_target_trial_alignment

### Purpose

Audit structural alignment of eligibility, assignment and time zero.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_target_trial_alignment( cohort: pd.DataFrame, *, patient_col: str = "patient_id", index_date_col: str = "index_date", initiation_date_col: str = "initiation_date", arm_col: str = "treatment_arm", allowed_time_zero_gap_days: int = 0, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `cohort` | `cohort: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str = 'index_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `initiation_date_col` | `initiation_date_col: str = 'initiation_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `arm_col` | `arm_col: str = 'treatment_arm'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `allowed_time_zero_gap_days` | `allowed_time_zero_gap_days: int = 0` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `cohort`.
- Referenced columns must exist in the input table: `patient_col`, `index_date_col`, `initiation_date_col`, `arm_col`.

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

from thomaslab.target_trial import audit_target_trial_alignment

result = audit_target_trial_alignment(
    cohort=sample_df
)

print(result)
~~~

### Related functions

- `TargetTrialSpec.to_dict`
- `validate_target_trial_spec`
- `load_target_trial_spec`
- `build_active_comparator_new_user_cohort`
- `build_itt_followup`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/target_trial.py#L405`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L405)
- Repository search: [audit_target_trial_alignment](https://github.com/appsplorer/thomaslab-core/search?q=audit_target_trial_alignment&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Audit structural alignment of eligibility, assignment and time zero.

### API inspection

~~~python
import inspect
from thomaslab.target_trial import audit_target_trial_alignment

print(inspect.signature(audit_target_trial_alignment))
print(audit_target_trial_alignment.__doc__)
~~~

### Source

[`src/thomaslab/target_trial.py#L405`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L405)

---

<!-- callable:thomaslab.target_trial.build_target_trial_dataset -->
## build_target_trial_dataset

### Purpose

Merge one-row-per-patient cohort assignment and follow-up metadata.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_target_trial_dataset( cohort: pd.DataFrame, followup: pd.DataFrame, *, patient_col: str = "patient_id", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `cohort` | `cohort: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `followup` | `followup: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `cohort`, `followup`.
- Referenced columns must exist in the input table: `patient_col`.

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

from thomaslab.target_trial import build_target_trial_dataset

result = build_target_trial_dataset(
    cohort=sample_df,
    followup=sample_df
)

print(result)
~~~

### Related functions

- `TargetTrialSpec.to_dict`
- `validate_target_trial_spec`
- `load_target_trial_spec`
- `build_active_comparator_new_user_cohort`
- `build_itt_followup`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/target_trial.py#L436`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L436)
- Repository search: [build_target_trial_dataset](https://github.com/appsplorer/thomaslab-core/search?q=build_target_trial_dataset&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Merge one-row-per-patient cohort assignment and follow-up metadata.

### API inspection

~~~python
import inspect
from thomaslab.target_trial import build_target_trial_dataset

print(inspect.signature(build_target_trial_dataset))
print(build_target_trial_dataset.__doc__)
~~~

### Source

[`src/thomaslab/target_trial.py#L436`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L436)

---

<!-- callable:thomaslab.target_trial.summarize_target_trial_emulation -->
## summarize_target_trial_emulation

### Purpose

Return descriptive target-trial-emulation counts and follow-up summaries.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_target_trial_emulation( dataset: pd.DataFrame, *, arm_col: str = "treatment_arm", followup_days_col: str = "followup_days", reason_col: str = "censor_or_event_reason", ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `dataset` | `dataset: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `arm_col` | `arm_col: str = 'treatment_arm'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `followup_days_col` | `followup_days_col: str = 'followup_days'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `reason_col` | `reason_col: str = 'censor_or_event_reason'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `dataset`.
- Referenced columns must exist in the input table: `arm_col`, `followup_days_col`, `reason_col`.

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

from thomaslab.target_trial import summarize_target_trial_emulation

result = summarize_target_trial_emulation(
    dataset=sample_df
)

print(result)
~~~

### Related functions

- `TargetTrialSpec.to_dict`
- `validate_target_trial_spec`
- `load_target_trial_spec`
- `build_active_comparator_new_user_cohort`
- `build_itt_followup`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/target_trial.py#L450`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L450)
- Repository search: [summarize_target_trial_emulation](https://github.com/appsplorer/thomaslab-core/search?q=summarize_target_trial_emulation&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return descriptive target-trial-emulation counts and follow-up summaries.

### API inspection

~~~python
import inspect
from thomaslab.target_trial import summarize_target_trial_emulation

print(inspect.signature(summarize_target_trial_emulation))
print(summarize_target_trial_emulation.__doc__)
~~~

### Source

[`src/thomaslab/target_trial.py#L450`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/target_trial.py#L450)

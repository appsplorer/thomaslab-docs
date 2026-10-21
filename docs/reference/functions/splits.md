# thomaslab.splits

Leakage-aware patient/group/site/temporal dataset splitting utilities.

## Research-use boundary

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

## Self-service orientation

- Related guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 8

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.splits.patient_level_split -->
## patient_level_split

### Purpose

Assign whole patients to train/test; repeated rows for a patient stay together.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def patient_level_split( df: pd.DataFrame, *, patient_col: str = "patient_id", test_size: float = 0.2, random_state: int = 42, split_col: str = "split", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `test_size` | `test_size: float = 0.2` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |
| `split_col` | `split_col: str = 'split'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.
- Referenced columns must exist in the input table: `patient_col`, `split_col`.

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

from thomaslab.splits import patient_level_split

result = patient_level_split(
    df=sample_df
)

print(result)
~~~

### Related functions

- `grouped_split`
- `temporal_split`
- `site_holdout_split`
- `external_validation_split`
- `stratified_group_split`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/splits.py#L27`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/splits.py#L27)
- Repository search: [patient_level_split](https://github.com/appsplorer/thomaslab-core/search?q=patient_level_split&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Assign whole patients to train/test; repeated rows for a patient stay together.

### API inspection

~~~python
import inspect
from thomaslab.splits import patient_level_split

print(inspect.signature(patient_level_split))
print(patient_level_split.__doc__)
~~~

### Source

[`src/thomaslab/splits.py#L27`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/splits.py#L27)

---

<!-- callable:thomaslab.splits.grouped_split -->
## grouped_split

### Purpose

Assign entire groups (household/provider/site/etc.) to train/test.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def grouped_split( df: pd.DataFrame, *, group_col: str, test_size: float = 0.2, random_state: int = 42, split_col: str = "split", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `group_col` | `group_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `test_size` | `test_size: float = 0.2` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |
| `split_col` | `split_col: str = 'split'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `group_col`.
- Referenced columns must exist in the input table: `group_col`, `split_col`.

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

from thomaslab.splits import grouped_split

result = grouped_split(
    df=sample_df,
    group_col='group'
)

print(result)
~~~

### Related functions

- `patient_level_split`
- `temporal_split`
- `site_holdout_split`
- `external_validation_split`
- `stratified_group_split`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/splits.py#L50`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/splits.py#L50)
- Repository search: [grouped_split](https://github.com/appsplorer/thomaslab-core/search?q=grouped_split&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Assign entire groups (household/provider/site/etc.) to train/test.

### API inspection

~~~python
import inspect
from thomaslab.splits import grouped_split

print(inspect.signature(grouped_split))
print(grouped_split.__doc__)
~~~

### Source

[`src/thomaslab/splits.py#L50`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/splits.py#L50)

---

<!-- callable:thomaslab.splits.temporal_split -->
## temporal_split

### Purpose

Split earlier vs later observations, with explicit cross-boundary patient policy.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def temporal_split( df: pd.DataFrame, *, date_col: str, cutoff: str | pd.Timestamp, patient_col: str | None = "patient_id", patient_policy: str = "later", split_col: str = "split", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `date_col` | `date_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `cutoff` | `cutoff: str \| pd.Timestamp` | Yes | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |
| `patient_col` | `patient_col: str \| None = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `patient_policy` | `patient_policy: str = 'later'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `split_col` | `split_col: str = 'split'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `date_col`, `cutoff`.
- Referenced columns must exist in the input table: `date_col`, `patient_col`, `split_col`.

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

from thomaslab.splits import temporal_split

result = temporal_split(
    df=sample_df,
    date_col='event_date',
    cutoff="value"
)

print(result)
~~~

### Related functions

- `patient_level_split`
- `grouped_split`
- `site_holdout_split`
- `external_validation_split`
- `stratified_group_split`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/splits.py#L72`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/splits.py#L72)
- Repository search: [temporal_split](https://github.com/appsplorer/thomaslab-core/search?q=temporal_split&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Split earlier vs later observations, with explicit cross-boundary patient policy.

``patient_policy='later'`` assigns all rows for patients spanning the cutoff to
test, preventing the same patient from appearing in both sets.
``patient_policy='error'`` fails if any patient spans the cutoff.

### API inspection

~~~python
import inspect
from thomaslab.splits import temporal_split

print(inspect.signature(temporal_split))
print(temporal_split.__doc__)
~~~

### Source

[`src/thomaslab/splits.py#L72`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/splits.py#L72)

---

<!-- callable:thomaslab.splits.site_holdout_split -->
## site_holdout_split

### Purpose

Hold out explicit sites for transport/external-style validation.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def site_holdout_split( df: pd.DataFrame, *, site_col: str = "site_id", holdout_sites: Sequence[object], split_col: str = "split", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `site_col` | `site_col: str = 'site_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `holdout_sites` | `holdout_sites: Sequence[object]` | Yes | Site/domain identifier used for grouping, validation, or transportability analysis. |
| `split_col` | `split_col: str = 'split'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `holdout_sites`.
- Referenced columns must exist in the input table: `site_col`, `split_col`.

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

sample_value = "replace_with_validated_value"

from thomaslab.splits import site_holdout_split

result = site_holdout_split(
    df=sample_df,
    holdout_sites=sample_value
)

print(result)
~~~

### Related functions

- `patient_level_split`
- `grouped_split`
- `temporal_split`
- `external_validation_split`
- `stratified_group_split`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/splits.py#L106`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/splits.py#L106)
- Repository search: [site_holdout_split](https://github.com/appsplorer/thomaslab-core/search?q=site_holdout_split&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Hold out explicit sites for transport/external-style validation.

### API inspection

~~~python
import inspect
from thomaslab.splits import site_holdout_split

print(inspect.signature(site_holdout_split))
print(site_holdout_split.__doc__)
~~~

### Source

[`src/thomaslab/splits.py#L106`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/splits.py#L106)

---

<!-- callable:thomaslab.splits.external_validation_split -->
## external_validation_split

### Purpose

Concatenate derivation and independent external data with explicit provenance.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def external_validation_split( derivation: pd.DataFrame, external: pd.DataFrame, *, dataset_col: str = "dataset_role", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `derivation` | `derivation: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `external` | `external: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `dataset_col` | `dataset_col: str = 'dataset_role'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `derivation`, `external`.
- Referenced columns must exist in the input table: `dataset_col`.

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

from thomaslab.splits import external_validation_split

result = external_validation_split(
    derivation=sample_df,
    external=sample_df
)

print(result)
~~~

### Related functions

- `patient_level_split`
- `grouped_split`
- `temporal_split`
- `site_holdout_split`
- `stratified_group_split`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/splits.py#L124`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/splits.py#L124)
- Repository search: [external_validation_split](https://github.com/appsplorer/thomaslab-core/search?q=external_validation_split&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Concatenate derivation and independent external data with explicit provenance.

This function labels provenance only; it does not assert that the external source
is clinically independent or qualifies as regulatory/clinical external validation.

### API inspection

~~~python
import inspect
from thomaslab.splits import external_validation_split

print(inspect.signature(external_validation_split))
print(external_validation_split.__doc__)
~~~

### Source

[`src/thomaslab/splits.py#L124`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/splits.py#L124)

---

<!-- callable:thomaslab.splits.stratified_group_split -->
## stratified_group_split

### Purpose

One stratified group-aware train/test fold for classification.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def stratified_group_split( df: pd.DataFrame, *, target_col: str, group_col: str, n_splits: int = 5, fold: int = 0, random_state: int = 42, split_col: str = "split", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `target_col` | `target_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `group_col` | `group_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `n_splits` | `n_splits: int = 5` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `fold` | `fold: int = 0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |
| `split_col` | `split_col: str = 'split'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `target_col`, `group_col`.
- Referenced columns must exist in the input table: `target_col`, `group_col`, `split_col`.

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

from thomaslab.splits import stratified_group_split

result = stratified_group_split(
    df=sample_df,
    target_col='target',
    group_col='group'
)

print(result)
~~~

### Related functions

- `patient_level_split`
- `grouped_split`
- `temporal_split`
- `site_holdout_split`
- `external_validation_split`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/splits.py#L143`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/splits.py#L143)
- Repository search: [stratified_group_split](https://github.com/appsplorer/thomaslab-core/search?q=stratified_group_split&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

One stratified group-aware train/test fold for classification.

### API inspection

~~~python
import inspect
from thomaslab.splits import stratified_group_split

print(inspect.signature(stratified_group_split))
print(stratified_group_split.__doc__)
~~~

### Source

[`src/thomaslab/splits.py#L143`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/splits.py#L143)

---

<!-- callable:thomaslab.splits.grouped_cv_folds -->
## grouped_cv_folds

### Purpose

Assign deterministic non-overlapping group CV folds.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def grouped_cv_folds( df: pd.DataFrame, *, group_col: str, n_splits: int = 5, fold_col: str = "cv_fold", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `group_col` | `group_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `n_splits` | `n_splits: int = 5` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `fold_col` | `fold_col: str = 'cv_fold'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `group_col`.
- Referenced columns must exist in the input table: `group_col`, `fold_col`.

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

from thomaslab.splits import grouped_cv_folds

result = grouped_cv_folds(
    df=sample_df,
    group_col='group'
)

print(result)
~~~

### Related functions

- `patient_level_split`
- `grouped_split`
- `temporal_split`
- `site_holdout_split`
- `external_validation_split`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/splits.py#L169`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/splits.py#L169)
- Repository search: [grouped_cv_folds](https://github.com/appsplorer/thomaslab-core/search?q=grouped_cv_folds&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Assign deterministic non-overlapping group CV folds.

### API inspection

~~~python
import inspect
from thomaslab.splits import grouped_cv_folds

print(inspect.signature(grouped_cv_folds))
print(grouped_cv_folds.__doc__)
~~~

### Source

[`src/thomaslab/splits.py#L169`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/splits.py#L169)

---

<!-- callable:thomaslab.splits.audit_split -->
## audit_split

### Purpose

Audit overlap, class distribution, site distribution and temporal ordering.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_split( df: pd.DataFrame, *, split_col: str = "split", patient_col: str | None = "patient_id", site_col: str | None = "site_id", target_col: str | None = None, date_col: str | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `split_col` | `split_col: str = 'split'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `patient_col` | `patient_col: str \| None = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `site_col` | `site_col: str \| None = 'site_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `target_col` | `target_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.
- Referenced columns must exist in the input table: `split_col`, `patient_col`, `site_col`, `target_col`, `date_col`.

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

from thomaslab.splits import audit_split

result = audit_split(
    df=sample_df
)

print(result)
~~~

### Related functions

- `patient_level_split`
- `grouped_split`
- `temporal_split`
- `site_holdout_split`
- `external_validation_split`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/splits.py#L189`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/splits.py#L189)
- Repository search: [audit_split](https://github.com/appsplorer/thomaslab-core/search?q=audit_split&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Audit overlap, class distribution, site distribution and temporal ordering.

### API inspection

~~~python
import inspect
from thomaslab.splits import audit_split

print(inspect.signature(audit_split))
print(audit_split.__doc__)
~~~

### Source

[`src/thomaslab/splits.py#L189`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/splits.py#L189)

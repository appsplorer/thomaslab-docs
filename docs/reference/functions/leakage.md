# thomaslab.leakage

Pre-model leakage and feature-window auditing utilities.

## Research-use boundary

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

## Self-service orientation

- Related guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 11

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.leakage.detect_identifier_leakage -->
## detect_identifier_leakage

### Purpose

Flag likely identifiers that should generally not be model features.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_identifier_leakage( columns: Iterable[str], *, allowlist: Iterable[str] | None = None, patterns: Sequence[str] = _DEFAULT_IDENTIFIER_PATTERNS, ) -> list[str]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `columns` | `columns: Iterable[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `allowlist` | `allowlist: Iterable[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `patterns` | `patterns: Sequence[str] = _DEFAULT_IDENTIFIER_PATTERNS` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `columns`.

### Returns

`list[str]`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.leakage import detect_identifier_leakage

result = detect_identifier_leakage(
    columns="value"
)

print(result)
~~~

### Related functions

- `detect_target_leakage`
- `detect_outcome_proxy_features`
- `detect_post_index_features`
- `audit_feature_windows`
- `detect_train_test_patient_overlap`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/leakage.py#L25`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L25)
- Repository search: [detect_identifier_leakage](https://github.com/appsplorer/thomaslab-core/search?q=detect_identifier_leakage&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Flag likely identifiers that should generally not be model features.

### API inspection

~~~python
import inspect
from thomaslab.leakage import detect_identifier_leakage

print(inspect.signature(detect_identifier_leakage))
print(detect_identifier_leakage.__doc__)
~~~

### Source

[`src/thomaslab/leakage.py#L25`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L25)

---

<!-- callable:thomaslab.leakage.detect_target_leakage -->
## detect_target_leakage

### Purpose

Flag the target itself and explicitly forbidden derivative columns.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_target_leakage( columns: Iterable[str], target_col: str, *, additional_forbidden: Iterable[str] | None = None, ) -> list[str]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `columns` | `columns: Iterable[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `target_col` | `target_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `additional_forbidden` | `additional_forbidden: Iterable[str] \| None = None` | No | Identifier or identifier column. Confirm uniqueness/grouping semantics before analysis. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `columns`, `target_col`.
- Referenced columns must exist in the input table: `target_col`.

### Returns

`list[str]`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.leakage import detect_target_leakage

result = detect_target_leakage(
    columns="value",
    target_col='target'
)

print(result)
~~~

### Related functions

- `detect_identifier_leakage`
- `detect_outcome_proxy_features`
- `detect_post_index_features`
- `audit_feature_windows`
- `detect_train_test_patient_overlap`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/leakage.py#L43`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L43)
- Repository search: [detect_target_leakage](https://github.com/appsplorer/thomaslab-core/search?q=detect_target_leakage&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Flag the target itself and explicitly forbidden derivative columns.

### API inspection

~~~python
import inspect
from thomaslab.leakage import detect_target_leakage

print(inspect.signature(detect_target_leakage))
print(detect_target_leakage.__doc__)
~~~

### Source

[`src/thomaslab/leakage.py#L43`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L43)

---

<!-- callable:thomaslab.leakage.detect_outcome_proxy_features -->
## detect_outcome_proxy_features

### Purpose

Flag suspicious feature names that may encode future outcome information.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_outcome_proxy_features( columns: Iterable[str], *, patterns: Sequence[str] = _DEFAULT_PROXY_PATTERNS, allowlist: Iterable[str] | None = None, ) -> list[str]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `columns` | `columns: Iterable[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `patterns` | `patterns: Sequence[str] = _DEFAULT_PROXY_PATTERNS` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `allowlist` | `allowlist: Iterable[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `columns`.

### Returns

`list[str]`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.leakage import detect_outcome_proxy_features

result = detect_outcome_proxy_features(
    columns="value"
)

print(result)
~~~

### Related functions

- `detect_identifier_leakage`
- `detect_target_leakage`
- `detect_post_index_features`
- `audit_feature_windows`
- `detect_train_test_patient_overlap`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/leakage.py#L54`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L54)
- Repository search: [detect_outcome_proxy_features](https://github.com/appsplorer/thomaslab-core/search?q=detect_outcome_proxy_features&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Flag suspicious feature names that may encode future outcome information.

### API inspection

~~~python
import inspect
from thomaslab.leakage import detect_outcome_proxy_features

print(inspect.signature(detect_outcome_proxy_features))
print(detect_outcome_proxy_features.__doc__)
~~~

### Source

[`src/thomaslab/leakage.py#L54`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L54)

---

<!-- callable:thomaslab.leakage.detect_post_index_features -->
## detect_post_index_features

### Purpose

Return features whose documented extraction window ends after the allowed boundary.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_post_index_features( feature_metadata: pd.DataFrame, *, feature_col: str = "feature", window_end_col: str = "window_end_days", allowed_max_day: float = 0.0, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `feature_metadata` | `feature_metadata: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `feature_col` | `feature_col: str = 'feature'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `window_end_col` | `window_end_col: str = 'window_end_days'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `allowed_max_day` | `allowed_max_day: float = 0.0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `feature_metadata`.
- Referenced columns must exist in the input table: `feature_col`, `window_end_col`.

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

from thomaslab.leakage import detect_post_index_features

result = detect_post_index_features(
    feature_metadata=sample_df
)

print(result)
~~~

### Related functions

- `detect_identifier_leakage`
- `detect_target_leakage`
- `detect_outcome_proxy_features`
- `audit_feature_windows`
- `detect_train_test_patient_overlap`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/leakage.py#L72`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L72)
- Repository search: [detect_post_index_features](https://github.com/appsplorer/thomaslab-core/search?q=detect_post_index_features&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return features whose documented extraction window ends after the allowed boundary.

### API inspection

~~~python
import inspect
from thomaslab.leakage import detect_post_index_features

print(inspect.signature(detect_post_index_features))
print(detect_post_index_features.__doc__)
~~~

### Source

[`src/thomaslab/leakage.py#L72`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L72)

---

<!-- callable:thomaslab.leakage.audit_feature_windows -->
## audit_feature_windows

### Purpose

Validate documented feature windows and classify leakage risk.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_feature_windows( feature_metadata: pd.DataFrame, *, feature_col: str = "feature", window_start_col: str = "window_start_days", window_end_col: str = "window_end_days", allowed_max_day: float = 0.0, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `feature_metadata` | `feature_metadata: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `feature_col` | `feature_col: str = 'feature'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `window_start_col` | `window_start_col: str = 'window_start_days'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `window_end_col` | `window_end_col: str = 'window_end_days'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `allowed_max_day` | `allowed_max_day: float = 0.0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `feature_metadata`.
- Referenced columns must exist in the input table: `feature_col`, `window_start_col`, `window_end_col`.

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

from thomaslab.leakage import audit_feature_windows

result = audit_feature_windows(
    feature_metadata=sample_df
)

print(result)
~~~

### Related functions

- `detect_identifier_leakage`
- `detect_target_leakage`
- `detect_outcome_proxy_features`
- `detect_post_index_features`
- `detect_train_test_patient_overlap`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/leakage.py#L91`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L91)
- Repository search: [audit_feature_windows](https://github.com/appsplorer/thomaslab-core/search?q=audit_feature_windows&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate documented feature windows and classify leakage risk.

### API inspection

~~~python
import inspect
from thomaslab.leakage import audit_feature_windows

print(inspect.signature(audit_feature_windows))
print(audit_feature_windows.__doc__)
~~~

### Source

[`src/thomaslab/leakage.py#L91`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L91)

---

<!-- callable:thomaslab.leakage.detect_train_test_patient_overlap -->
## detect_train_test_patient_overlap

### Purpose

Return patient IDs present in both train and test data.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_train_test_patient_overlap( train: pd.DataFrame, test: pd.DataFrame, *, patient_col: str = "patient_id", ) -> list[object]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `train` | `train: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `test` | `test: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `train`, `test`.
- Referenced columns must exist in the input table: `patient_col`.

### Returns

`list[object]`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

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

from thomaslab.leakage import detect_train_test_patient_overlap

result = detect_train_test_patient_overlap(
    train=sample_df,
    test=sample_df
)

print(result)
~~~

### Related functions

- `detect_identifier_leakage`
- `detect_target_leakage`
- `detect_outcome_proxy_features`
- `detect_post_index_features`
- `audit_feature_windows`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/leakage.py#L118`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L118)
- Repository search: [detect_train_test_patient_overlap](https://github.com/appsplorer/thomaslab-core/search?q=detect_train_test_patient_overlap&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return patient IDs present in both train and test data.

### API inspection

~~~python
import inspect
from thomaslab.leakage import detect_train_test_patient_overlap

print(inspect.signature(detect_train_test_patient_overlap))
print(detect_train_test_patient_overlap.__doc__)
~~~

### Source

[`src/thomaslab/leakage.py#L118`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L118)

---

<!-- callable:thomaslab.leakage.detect_duplicate_patient_split -->
## detect_duplicate_patient_split

### Purpose

Return patients assigned to more than one split.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_duplicate_patient_split( assigned: pd.DataFrame, *, patient_col: str = "patient_id", split_col: str = "split", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `assigned` | `assigned: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `split_col` | `split_col: str = 'split'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `assigned`.
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

from thomaslab.leakage import detect_duplicate_patient_split

result = detect_duplicate_patient_split(
    assigned=sample_df
)

print(result)
~~~

### Related functions

- `detect_identifier_leakage`
- `detect_target_leakage`
- `detect_outcome_proxy_features`
- `detect_post_index_features`
- `audit_feature_windows`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/leakage.py#L130`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L130)
- Repository search: [detect_duplicate_patient_split](https://github.com/appsplorer/thomaslab-core/search?q=detect_duplicate_patient_split&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return patients assigned to more than one split.

### API inspection

~~~python
import inspect
from thomaslab.leakage import detect_duplicate_patient_split

print(inspect.signature(detect_duplicate_patient_split))
print(detect_duplicate_patient_split.__doc__)
~~~

### Source

[`src/thomaslab/leakage.py#L130`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L130)

---

<!-- callable:thomaslab.leakage.detect_site_leakage -->
## detect_site_leakage

### Purpose

Summarize site overlap across splits.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_site_leakage( assigned: pd.DataFrame, *, site_col: str = "site_id", split_col: str = "split", require_disjoint_sites: bool = False, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `assigned` | `assigned: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `site_col` | `site_col: str = 'site_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `split_col` | `split_col: str = 'split'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `require_disjoint_sites` | `require_disjoint_sites: bool = False` | No | Site/domain identifier used for grouping, validation, or transportability analysis. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `assigned`.
- Referenced columns must exist in the input table: `site_col`, `split_col`.

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

from thomaslab.leakage import detect_site_leakage

result = detect_site_leakage(
    assigned=sample_df
)

print(result)
~~~

### Related functions

- `detect_identifier_leakage`
- `detect_target_leakage`
- `detect_outcome_proxy_features`
- `detect_post_index_features`
- `audit_feature_windows`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/leakage.py#L145`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L145)
- Repository search: [detect_site_leakage](https://github.com/appsplorer/thomaslab-core/search?q=detect_site_leakage&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize site overlap across splits.

Site overlap is not inherently leakage for ordinary patient-level validation. It is
a violation only when ``require_disjoint_sites=True`` (for site-holdout designs).

### API inspection

~~~python
import inspect
from thomaslab.leakage import detect_site_leakage

print(inspect.signature(detect_site_leakage))
print(detect_site_leakage.__doc__)
~~~

### Source

[`src/thomaslab/leakage.py#L145`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L145)

---

<!-- callable:thomaslab.leakage.detect_temporal_split_violation -->
## detect_temporal_split_violation

### Purpose

Check whether any test observation predates/equal the latest train observation.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_temporal_split_violation( assigned: pd.DataFrame, *, date_col: str, split_col: str = "split", train_label: str = "train", test_label: str = "test", ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `assigned` | `assigned: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `date_col` | `date_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `split_col` | `split_col: str = 'split'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `train_label` | `train_label: str = 'train'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `test_label` | `test_label: str = 'test'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `assigned`, `date_col`.
- Referenced columns must exist in the input table: `date_col`, `split_col`.

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

from thomaslab.leakage import detect_temporal_split_violation

result = detect_temporal_split_violation(
    assigned=sample_df,
    date_col='event_date'
)

print(result)
~~~

### Related functions

- `detect_identifier_leakage`
- `detect_target_leakage`
- `detect_outcome_proxy_features`
- `detect_post_index_features`
- `audit_feature_windows`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/leakage.py#L177`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L177)
- Repository search: [detect_temporal_split_violation](https://github.com/appsplorer/thomaslab-core/search?q=detect_temporal_split_violation&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Check whether any test observation predates/equal the latest train observation.

### API inspection

~~~python
import inspect
from thomaslab.leakage import detect_temporal_split_violation

print(inspect.signature(detect_temporal_split_violation))
print(detect_temporal_split_violation.__doc__)
~~~

### Source

[`src/thomaslab/leakage.py#L177`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L177)

---

<!-- callable:thomaslab.leakage.detect_future_information -->
## detect_future_information

### Purpose

Return event rows occurring after the allowed feature boundary relative to index.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_future_information( events: pd.DataFrame, *, feature_date_col: str, index_date_col: str, allowed_max_day: float = 0.0, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `feature_date_col` | `feature_date_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `index_date_col` | `index_date_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `allowed_max_day` | `allowed_max_day: float = 0.0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`, `feature_date_col`, `index_date_col`.
- Referenced columns must exist in the input table: `feature_date_col`, `index_date_col`.

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

from thomaslab.leakage import detect_future_information

result = detect_future_information(
    events=sample_df,
    feature_date_col='feature_date',
    index_date_col='index_date'
)

print(result)
~~~

### Related functions

- `detect_identifier_leakage`
- `detect_target_leakage`
- `detect_outcome_proxy_features`
- `detect_post_index_features`
- `audit_feature_windows`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/leakage.py#L206`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L206)
- Repository search: [detect_future_information](https://github.com/appsplorer/thomaslab-core/search?q=detect_future_information&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return event rows occurring after the allowed feature boundary relative to index.

### API inspection

~~~python
import inspect
from thomaslab.leakage import detect_future_information

print(inspect.signature(detect_future_information))
print(detect_future_information.__doc__)
~~~

### Source

[`src/thomaslab/leakage.py#L206`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L206)

---

<!-- callable:thomaslab.leakage.audit_dataset_leakage -->
## audit_dataset_leakage

### Purpose

Run a pre-model leakage audit and optionally fail when blocking risks exist.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_dataset_leakage( dataset: pd.DataFrame, *, target_col: str, feature_cols: Sequence[str] | None = None, patient_col: str = "patient_id", split_col: str | None = None, site_col: str | None = None, require_disjoint_sites: bool = False, feature_metadata: pd.DataFrame | None = None, additional_forbidden: Iterable[str] | None = None, proxy_allowlist: Iterable[str] | None = None, strict: bool = False, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `dataset` | `dataset: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `target_col` | `target_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `feature_cols` | `feature_cols: Sequence[str] \| None = None` | No | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `split_col` | `split_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `site_col` | `site_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `require_disjoint_sites` | `require_disjoint_sites: bool = False` | No | Site/domain identifier used for grouping, validation, or transportability analysis. |
| `feature_metadata` | `feature_metadata: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `additional_forbidden` | `additional_forbidden: Iterable[str] \| None = None` | No | Identifier or identifier column. Confirm uniqueness/grouping semantics before analysis. |
| `proxy_allowlist` | `proxy_allowlist: Iterable[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strict` | `strict: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `dataset`, `target_col`.
- Referenced columns must exist in the input table: `target_col`, `patient_col`, `split_col`, `site_col`.

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

from thomaslab.leakage import audit_dataset_leakage

result = audit_dataset_leakage(
    dataset=sample_df,
    target_col='target'
)

print(result)
~~~

### Related functions

- `detect_identifier_leakage`
- `detect_target_leakage`
- `detect_outcome_proxy_features`
- `detect_post_index_features`
- `audit_feature_windows`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/leakage.py#L228`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L228)
- Repository search: [audit_dataset_leakage](https://github.com/appsplorer/thomaslab-core/search?q=audit_dataset_leakage&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Run a pre-model leakage audit and optionally fail when blocking risks exist.

### API inspection

~~~python
import inspect
from thomaslab.leakage import audit_dataset_leakage

print(inspect.signature(audit_dataset_leakage))
print(audit_dataset_leakage.__doc__)
~~~

### Source

[`src/thomaslab/leakage.py#L228`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/leakage.py#L228)

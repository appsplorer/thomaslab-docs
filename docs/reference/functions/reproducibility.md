# thomaslab.reproducibility

Reproducibility manifests, fingerprints, deterministic seeds, and contract audits.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 13

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.reproducibility.canonical_json -->
## canonical_json

### Purpose

Serialize supported metadata deterministically for hashing and manifests.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def canonical_json(value: Any) -> str
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `value` | `value: Any` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `value`.

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
from thomaslab.reproducibility import canonical_json

result = canonical_json(
    value={"key": "value"}
)

print(result)
~~~

### Related functions

- `sha256_bytes`
- `fingerprint_mapping`
- `fingerprint_file`
- `fingerprint_dataframe`
- `fingerprint_object`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/reproducibility.py#L53`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L53)
- Repository search: [canonical_json](https://github.com/appsplorer/thomaslab-core/search?q=canonical_json&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Serialize supported metadata deterministically for hashing and manifests.

### API inspection

~~~python
import inspect
from thomaslab.reproducibility import canonical_json

print(inspect.signature(canonical_json))
print(canonical_json.__doc__)
~~~

### Source

[`src/thomaslab/reproducibility.py#L53`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L53)

---

<!-- callable:thomaslab.reproducibility.sha256_bytes -->
## sha256_bytes

### Purpose

Return a lowercase SHA-256 digest.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def sha256_bytes(payload: bytes) -> str
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `payload` | `payload: bytes` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `payload`.

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
from thomaslab.reproducibility import sha256_bytes

result = sha256_bytes(
    payload=b"example"
)

print(result)
~~~

### Related functions

- `canonical_json`
- `fingerprint_mapping`
- `fingerprint_file`
- `fingerprint_dataframe`
- `fingerprint_object`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/reproducibility.py#L64`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L64)
- Repository search: [sha256_bytes](https://github.com/appsplorer/thomaslab-core/search?q=sha256_bytes&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return a lowercase SHA-256 digest.

### API inspection

~~~python
import inspect
from thomaslab.reproducibility import sha256_bytes

print(inspect.signature(sha256_bytes))
print(sha256_bytes.__doc__)
~~~

### Source

[`src/thomaslab/reproducibility.py#L64`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L64)

---

<!-- callable:thomaslab.reproducibility.fingerprint_mapping -->
## fingerprint_mapping

### Purpose

Fingerprint a JSON-compatible mapping with stable key ordering.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fingerprint_mapping(value: Mapping[str, Any]) -> str
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `value` | `value: Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `value`.

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
from thomaslab.reproducibility import fingerprint_mapping

result = fingerprint_mapping(
    value={}
)

print(result)
~~~

### Related functions

- `canonical_json`
- `sha256_bytes`
- `fingerprint_file`
- `fingerprint_dataframe`
- `fingerprint_object`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/reproducibility.py#L69`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L69)
- Repository search: [fingerprint_mapping](https://github.com/appsplorer/thomaslab-core/search?q=fingerprint_mapping&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Fingerprint a JSON-compatible mapping with stable key ordering.

### API inspection

~~~python
import inspect
from thomaslab.reproducibility import fingerprint_mapping

print(inspect.signature(fingerprint_mapping))
print(fingerprint_mapping.__doc__)
~~~

### Source

[`src/thomaslab/reproducibility.py#L69`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L69)

---

<!-- callable:thomaslab.reproducibility.fingerprint_file -->
## fingerprint_file

### Purpose

Fingerprint a file without loading the entire object into memory.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fingerprint_file(path: str | Path, *, chunk_size: int = 1024 * 1024) -> str
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `path` | `path: str \| Path` | Yes | Input source/path accepted by this callable. Keep raw-source provenance and do not overwrite the source. |
| `chunk_size` | `chunk_size: int = 1024 * 1024` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `path`.

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
from thomaslab.reproducibility import fingerprint_file

result = fingerprint_file(
    path="path/to/input.csv"
)

print(result)
~~~

### Related functions

- `canonical_json`
- `sha256_bytes`
- `fingerprint_mapping`
- `fingerprint_dataframe`
- `fingerprint_object`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/reproducibility.py#L74`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L74)
- Repository search: [fingerprint_file](https://github.com/appsplorer/thomaslab-core/search?q=fingerprint_file&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Fingerprint a file without loading the entire object into memory.

### API inspection

~~~python
import inspect
from thomaslab.reproducibility import fingerprint_file

print(inspect.signature(fingerprint_file))
print(fingerprint_file.__doc__)
~~~

### Source

[`src/thomaslab/reproducibility.py#L74`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L74)

---

<!-- callable:thomaslab.reproducibility.fingerprint_dataframe -->
## fingerprint_dataframe

### Purpose

Fingerprint a dataframe including schema, row order, values, and optionally index.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fingerprint_dataframe( df: pd.DataFrame, *, include_index: bool = True, ) -> str
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `include_index` | `include_index: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.

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

from thomaslab.reproducibility import fingerprint_dataframe

result = fingerprint_dataframe(
    df=sample_df
)

print(result)
~~~

### Related functions

- `canonical_json`
- `sha256_bytes`
- `fingerprint_mapping`
- `fingerprint_file`
- `fingerprint_object`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/reproducibility.py#L89`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L89)
- Repository search: [fingerprint_dataframe](https://github.com/appsplorer/thomaslab-core/search?q=fingerprint_dataframe&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Fingerprint a dataframe including schema, row order, values, and optionally index.

### API inspection

~~~python
import inspect
from thomaslab.reproducibility import fingerprint_dataframe

print(inspect.signature(fingerprint_dataframe))
print(fingerprint_dataframe.__doc__)
~~~

### Source

[`src/thomaslab/reproducibility.py#L89`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L89)

---

<!-- callable:thomaslab.reproducibility.fingerprint_object -->
## fingerprint_object

### Purpose

Return a typed fingerprint record for common research inputs.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fingerprint_object(value: Any) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `value` | `value: Any` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `value`.

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
from thomaslab.reproducibility import fingerprint_object

result = fingerprint_object(
    value={"key": "value"}
)

print(result)
~~~

### Related functions

- `canonical_json`
- `sha256_bytes`
- `fingerprint_mapping`
- `fingerprint_file`
- `fingerprint_dataframe`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/reproducibility.py#L109`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L109)
- Repository search: [fingerprint_object](https://github.com/appsplorer/thomaslab-core/search?q=fingerprint_object&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return a typed fingerprint record for common research inputs.

### API inspection

~~~python
import inspect
from thomaslab.reproducibility import fingerprint_object

print(inspect.signature(fingerprint_object))
print(fingerprint_object.__doc__)
~~~

### Source

[`src/thomaslab/reproducibility.py#L109`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L109)

---

<!-- callable:thomaslab.reproducibility.capture_environment -->
## capture_environment

### Purpose

Capture portable runtime facts without collecting environment variables or secrets.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def capture_environment( *, package_names: Sequence[str] = _DEFAULT_PACKAGES, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `package_names` | `package_names: Sequence[str] = _DEFAULT_PACKAGES` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

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
from thomaslab.reproducibility import capture_environment

result = capture_environment()

print(result)
~~~

### Related functions

- `canonical_json`
- `sha256_bytes`
- `fingerprint_mapping`
- `fingerprint_file`
- `fingerprint_dataframe`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/reproducibility.py#L136`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L136)
- Repository search: [capture_environment](https://github.com/appsplorer/thomaslab-core/search?q=capture_environment&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Capture portable runtime facts without collecting environment variables or secrets.

### API inspection

~~~python
import inspect
from thomaslab.reproducibility import capture_environment

print(inspect.signature(capture_environment))
print(capture_environment.__doc__)
~~~

### Source

[`src/thomaslab/reproducibility.py#L136`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L136)

---

<!-- callable:thomaslab.reproducibility.set_deterministic_seed -->
## set_deterministic_seed

### Purpose

Seed Python, NumPy, and optionally PyTorch for repeatable stochastic workflows.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def set_deterministic_seed( seed: int, *, seed_torch: bool = True, torch_deterministic_algorithms: bool = False, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `seed` | `seed: int` | Yes | Reproducibility seed. Record it in the study bundle. |
| `seed_torch` | `seed_torch: bool = True` | No | Reproducibility seed. Record it in the study bundle. |
| `torch_deterministic_algorithms` | `torch_deterministic_algorithms: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `seed`.

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
from thomaslab.reproducibility import set_deterministic_seed

result = set_deterministic_seed(
    seed=2
)

print(result)
~~~

### Related functions

- `canonical_json`
- `sha256_bytes`
- `fingerprint_mapping`
- `fingerprint_file`
- `fingerprint_dataframe`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/reproducibility.py#L156`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L156)
- Repository search: [set_deterministic_seed](https://github.com/appsplorer/thomaslab-core/search?q=set_deterministic_seed&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Seed Python, NumPy, and optionally PyTorch for repeatable stochastic workflows.

### API inspection

~~~python
import inspect
from thomaslab.reproducibility import set_deterministic_seed

print(inspect.signature(set_deterministic_seed))
print(set_deterministic_seed.__doc__)
~~~

### Source

[`src/thomaslab/reproducibility.py#L156`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L156)

---

<!-- callable:thomaslab.reproducibility.build_run_manifest -->
## build_run_manifest

### Purpose

Build an auditable run manifest with stable study/input fingerprints.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_run_manifest( *, study_spec: Mapping[str, Any] | str | Path, inputs: Mapping[str, Any], seed: int, parameters: Mapping[str, Any] | None = None, git_commit: str | None = None, package_names: Sequence[str] = _DEFAULT_PACKAGES, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `study_spec` | `study_spec: Mapping[str, Any] \| str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `inputs` | `inputs: Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `seed` | `seed: int` | Yes | Reproducibility seed. Record it in the study bundle. |
| `parameters` | `parameters: Mapping[str, Any] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `git_commit` | `git_commit: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `package_names` | `package_names: Sequence[str] = _DEFAULT_PACKAGES` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `study_spec`, `inputs`, `seed`.

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
from thomaslab.reproducibility import build_run_manifest

result = build_run_manifest(
    study_spec={},
    inputs={},
    seed=2
)

print(result)
~~~

### Related functions

- `canonical_json`
- `sha256_bytes`
- `fingerprint_mapping`
- `fingerprint_file`
- `fingerprint_dataframe`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/reproducibility.py#L199`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L199)
- Repository search: [build_run_manifest](https://github.com/appsplorer/thomaslab-core/search?q=build_run_manifest&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build an auditable run manifest with stable study/input fingerprints.

### API inspection

~~~python
import inspect
from thomaslab.reproducibility import build_run_manifest

print(inspect.signature(build_run_manifest))
print(build_run_manifest.__doc__)
~~~

### Source

[`src/thomaslab/reproducibility.py#L199`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L199)

---

<!-- callable:thomaslab.reproducibility.validate_run_manifest -->
## validate_run_manifest

### Purpose

Validate manifest structure and its stable run fingerprint.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_run_manifest( manifest: Mapping[str, Any], *, strict: bool = False, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `manifest` | `manifest: Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strict` | `strict: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `manifest`.

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
from thomaslab.reproducibility import validate_run_manifest

result = validate_run_manifest(
    manifest={}
)

print(result)
~~~

### Related functions

- `canonical_json`
- `sha256_bytes`
- `fingerprint_mapping`
- `fingerprint_file`
- `fingerprint_dataframe`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/reproducibility.py#L233`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L233)
- Repository search: [validate_run_manifest](https://github.com/appsplorer/thomaslab-core/search?q=validate_run_manifest&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate manifest structure and its stable run fingerprint.

### API inspection

~~~python
import inspect
from thomaslab.reproducibility import validate_run_manifest

print(inspect.signature(validate_run_manifest))
print(validate_run_manifest.__doc__)
~~~

### Source

[`src/thomaslab/reproducibility.py#L233`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L233)

---

<!-- callable:thomaslab.reproducibility.write_run_manifest -->
## write_run_manifest

### Purpose

Validate and write a run manifest as deterministic, human-readable JSON.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def write_run_manifest( manifest: Mapping[str, Any], output_path: str | Path, *, overwrite: bool = False, ) -> Path
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `manifest` | `manifest: Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `output_path` | `output_path: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `overwrite` | `overwrite: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `manifest`, `output_path`.

### Returns

`Path`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.reproducibility import write_run_manifest

result = write_run_manifest(
    manifest={},
    output_path="path/to/input.csv"
)

print(result)
~~~

### Related functions

- `canonical_json`
- `sha256_bytes`
- `fingerprint_mapping`
- `fingerprint_file`
- `fingerprint_dataframe`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/reproducibility.py#L279`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L279)
- Repository search: [write_run_manifest](https://github.com/appsplorer/thomaslab-core/search?q=write_run_manifest&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate and write a run manifest as deterministic, human-readable JSON.

### API inspection

~~~python
import inspect
from thomaslab.reproducibility import write_run_manifest

print(inspect.signature(write_run_manifest))
print(write_run_manifest.__doc__)
~~~

### Source

[`src/thomaslab/reproducibility.py#L279`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L279)

---

<!-- callable:thomaslab.reproducibility.verify_input_fingerprints -->
## verify_input_fingerprints

### Purpose

Compare current inputs against fingerprints captured in a run manifest.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def verify_input_fingerprints( manifest: Mapping[str, Any], inputs: Mapping[str, Any], ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `manifest` | `manifest: Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `inputs` | `inputs: Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `manifest`, `inputs`.

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
from thomaslab.reproducibility import verify_input_fingerprints

result = verify_input_fingerprints(
    manifest={},
    inputs={}
)

print(result)
~~~

### Related functions

- `canonical_json`
- `sha256_bytes`
- `fingerprint_mapping`
- `fingerprint_file`
- `fingerprint_dataframe`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/reproducibility.py#L300`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L300)
- Repository search: [verify_input_fingerprints](https://github.com/appsplorer/thomaslab-core/search?q=verify_input_fingerprints&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compare current inputs against fingerprints captured in a run manifest.

### API inspection

~~~python
import inspect
from thomaslab.reproducibility import verify_input_fingerprints

print(inspect.signature(verify_input_fingerprints))
print(verify_input_fingerprints.__doc__)
~~~

### Source

[`src/thomaslab/reproducibility.py#L300`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L300)

---

<!-- callable:thomaslab.reproducibility.validate_table_contracts -->
## validate_table_contracts

### Purpose

Validate several tables/contracts and retain every table's audit result.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_table_contracts( tables: Mapping[str, pd.DataFrame], contracts: Mapping[str, Mapping[str, Any] | str | Path], *, strict: bool = False, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `tables` | `tables: Mapping[str, pd.DataFrame]` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `contracts` | `contracts: Mapping[str, Mapping[str, Any] \| str \| Path]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strict` | `strict: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `tables`, `contracts`.

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

from thomaslab.reproducibility import validate_table_contracts

result = validate_table_contracts(
    tables=sample_df,
    contracts={}
)

print(result)
~~~

### Related functions

- `canonical_json`
- `sha256_bytes`
- `fingerprint_mapping`
- `fingerprint_file`
- `fingerprint_dataframe`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/reproducibility.py#L379`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L379)
- Repository search: [validate_table_contracts](https://github.com/appsplorer/thomaslab-core/search?q=validate_table_contracts&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate several tables/contracts and retain every table's audit result.

### API inspection

~~~python
import inspect
from thomaslab.reproducibility import validate_table_contracts

print(inspect.signature(validate_table_contracts))
print(validate_table_contracts.__doc__)
~~~

### Source

[`src/thomaslab/reproducibility.py#L379`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/reproducibility.py#L379)

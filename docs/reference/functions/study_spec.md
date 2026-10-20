# thomaslab.study_spec

Unified study specifications for reproducible thomaslab-core workflows.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 6

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.study_spec.load_study_spec -->
## load_study_spec

### Purpose

Load a study specification from YAML, JSON, or an in-memory mapping.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def load_study_spec(spec: str | Path | Mapping[str, Any]) -> dict[str, Any]
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
from thomaslab.study_spec import load_study_spec

result = load_study_spec(
    spec={}
)

print(result)
~~~

### Related functions

- `validate_study_spec`
- `canonicalize_study_spec`
- `study_fingerprint`
- `derive_seed`
- `freeze_study_spec`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/study_spec.py#L44`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/study_spec.py#L44)
- Repository search: [load_study_spec](https://github.com/appsplorer/thomaslab-core/search?q=load_study_spec&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Load a study specification from YAML, JSON, or an in-memory mapping.

### API inspection

~~~python
import inspect
from thomaslab.study_spec import load_study_spec

print(inspect.signature(load_study_spec))
print(load_study_spec.__doc__)
~~~

### Source

[`src/thomaslab/study_spec.py#L44`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/study_spec.py#L44)

---

<!-- callable:thomaslab.study_spec.validate_study_spec -->
## validate_study_spec

### Purpose

Validate structural requirements without inventing study-specific semantics.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_study_spec( spec: str | Path | Mapping[str, Any], *, strict: bool = False, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `spec` | `spec: str \| Path \| Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strict` | `strict: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

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
from thomaslab.study_spec import validate_study_spec

result = validate_study_spec(
    spec={}
)

print(result)
~~~

### Related functions

- `load_study_spec`
- `canonicalize_study_spec`
- `study_fingerprint`
- `derive_seed`
- `freeze_study_spec`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/study_spec.py#L67`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/study_spec.py#L67)
- Repository search: [validate_study_spec](https://github.com/appsplorer/thomaslab-core/search?q=validate_study_spec&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate structural requirements without inventing study-specific semantics.

### API inspection

~~~python
import inspect
from thomaslab.study_spec import validate_study_spec

print(inspect.signature(validate_study_spec))
print(validate_study_spec.__doc__)
~~~

### Source

[`src/thomaslab/study_spec.py#L67`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/study_spec.py#L67)

---

<!-- callable:thomaslab.study_spec.canonicalize_study_spec -->
## canonicalize_study_spec

### Purpose

Return stable study content after removing thomaslab freeze metadata.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def canonicalize_study_spec(spec: str | Path | Mapping[str, Any]) -> dict[str, Any]
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
from thomaslab.study_spec import canonicalize_study_spec

result = canonicalize_study_spec(
    spec={}
)

print(result)
~~~

### Related functions

- `load_study_spec`
- `validate_study_spec`
- `study_fingerprint`
- `derive_seed`
- `freeze_study_spec`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/study_spec.py#L133`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/study_spec.py#L133)
- Repository search: [canonicalize_study_spec](https://github.com/appsplorer/thomaslab-core/search?q=canonicalize_study_spec&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return stable study content after removing thomaslab freeze metadata.

### API inspection

~~~python
import inspect
from thomaslab.study_spec import canonicalize_study_spec

print(inspect.signature(canonicalize_study_spec))
print(canonicalize_study_spec.__doc__)
~~~

### Source

[`src/thomaslab/study_spec.py#L133`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/study_spec.py#L133)

---

<!-- callable:thomaslab.study_spec.study_fingerprint -->
## study_fingerprint

### Purpose

Return a stable SHA-256 fingerprint of the canonical study specification.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def study_fingerprint(spec: str | Path | Mapping[str, Any]) -> str
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
from thomaslab.study_spec import study_fingerprint

result = study_fingerprint(
    spec={}
)

print(result)
~~~

### Related functions

- `load_study_spec`
- `validate_study_spec`
- `canonicalize_study_spec`
- `derive_seed`
- `freeze_study_spec`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/study_spec.py#L144`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/study_spec.py#L144)
- Repository search: [study_fingerprint](https://github.com/appsplorer/thomaslab-core/search?q=study_fingerprint&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return a stable SHA-256 fingerprint of the canonical study specification.

### API inspection

~~~python
import inspect
from thomaslab.study_spec import study_fingerprint

print(inspect.signature(study_fingerprint))
print(study_fingerprint.__doc__)
~~~

### Source

[`src/thomaslab/study_spec.py#L144`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/study_spec.py#L144)

---

<!-- callable:thomaslab.study_spec.derive_seed -->
## derive_seed

### Purpose

Derive deterministic child seeds from a declared study seed and named tokens.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def derive_seed(base_seed: int, *tokens: object, modulus: int = 2**32 - 1) -> int
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `base_seed` | `base_seed: int` | Yes | Reproducibility seed. Record it in the study bundle. |
| `tokens` | `*tokens: object` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `modulus` | `modulus: int = 2 ** 32 - 1` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `base_seed`.

### Returns

`int`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.study_spec import derive_seed

result = derive_seed(
    base_seed=2
)

print(result)
~~~

### Related functions

- `load_study_spec`
- `validate_study_spec`
- `canonicalize_study_spec`
- `study_fingerprint`
- `freeze_study_spec`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/study_spec.py#L157`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/study_spec.py#L157)
- Repository search: [derive_seed](https://github.com/appsplorer/thomaslab-core/search?q=derive_seed&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Derive deterministic child seeds from a declared study seed and named tokens.

### API inspection

~~~python
import inspect
from thomaslab.study_spec import derive_seed

print(inspect.signature(derive_seed))
print(derive_seed.__doc__)
~~~

### Source

[`src/thomaslab/study_spec.py#L157`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/study_spec.py#L157)

---

<!-- callable:thomaslab.study_spec.freeze_study_spec -->
## freeze_study_spec

### Purpose

Write a frozen YAML study specification with a content fingerprint.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def freeze_study_spec( spec: str | Path | Mapping[str, Any], output_path: str | Path, *, overwrite: bool = False, ) -> Path
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `spec` | `spec: str \| Path \| Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `output_path` | `output_path: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `overwrite` | `overwrite: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `spec`, `output_path`.

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
from thomaslab.study_spec import freeze_study_spec

result = freeze_study_spec(
    spec={},
    output_path="path/to/input.csv"
)

print(result)
~~~

### Related functions

- `load_study_spec`
- `validate_study_spec`
- `canonicalize_study_spec`
- `study_fingerprint`
- `derive_seed`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/study_spec.py#L168`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/study_spec.py#L168)
- Repository search: [freeze_study_spec](https://github.com/appsplorer/thomaslab-core/search?q=freeze_study_spec&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Write a frozen YAML study specification with a content fingerprint.

### API inspection

~~~python
import inspect
from thomaslab.study_spec import freeze_study_spec

print(inspect.signature(freeze_study_spec))
print(freeze_study_spec.__doc__)
~~~

### Source

[`src/thomaslab/study_spec.py#L168`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/study_spec.py#L168)

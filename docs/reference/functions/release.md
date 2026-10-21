# thomaslab.release

Release-quality checks for the stable thomaslab-core release line.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 8

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.release.validate_version_consistency -->
## validate_version_consistency

### Purpose

Check pyproject, package __version__, and README release heading.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_version_consistency(repo_root: str | Path) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `repo_root` | `repo_root: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `repo_root`.

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
from thomaslab.release import validate_version_consistency

result = validate_version_consistency(
    repo_root="value"
)

print(result)
~~~

### Related functions

- `validate_public_module_exports`
- `validate_yaml_json_assets`
- `validate_notebook_numbering`
- `validate_deprecation_registry`
- `validate_api_compatibility`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/release.py#L29`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/release.py#L29)
- Repository search: [validate_version_consistency](https://github.com/appsplorer/thomaslab-core/search?q=validate_version_consistency&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Check pyproject, package __version__, and README release heading.

### API inspection

~~~python
import inspect
from thomaslab.release import validate_version_consistency

print(inspect.signature(validate_version_consistency))
print(validate_version_consistency.__doc__)
~~~

### Source

[`src/thomaslab/release.py#L29`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/release.py#L29)

---

<!-- callable:thomaslab.release.validate_public_module_exports -->
## validate_public_module_exports

### Purpose

Ensure each name in thomaslab.__all__ corresponds to one package module.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_public_module_exports(repo_root: str | Path) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `repo_root` | `repo_root: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `repo_root`.

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
from thomaslab.release import validate_public_module_exports

result = validate_public_module_exports(
    repo_root="value"
)

print(result)
~~~

### Related functions

- `validate_version_consistency`
- `validate_yaml_json_assets`
- `validate_notebook_numbering`
- `validate_deprecation_registry`
- `validate_api_compatibility`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/release.py#L55`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/release.py#L55)
- Repository search: [validate_public_module_exports](https://github.com/appsplorer/thomaslab-core/search?q=validate_public_module_exports&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Ensure each name in thomaslab.__all__ corresponds to one package module.

### API inspection

~~~python
import inspect
from thomaslab.release import validate_public_module_exports

print(inspect.signature(validate_public_module_exports))
print(validate_public_module_exports.__doc__)
~~~

### Source

[`src/thomaslab/release.py#L55`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/release.py#L55)

---

<!-- callable:thomaslab.release.validate_yaml_json_assets -->
## validate_yaml_json_assets

### Purpose

Parse repository contracts/configs and JSON schemas used by research workflows.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_yaml_json_assets(repo_root: str | Path) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `repo_root` | `repo_root: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `repo_root`.

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
from thomaslab.release import validate_yaml_json_assets

result = validate_yaml_json_assets(
    repo_root="value"
)

print(result)
~~~

### Related functions

- `validate_version_consistency`
- `validate_public_module_exports`
- `validate_notebook_numbering`
- `validate_deprecation_registry`
- `validate_api_compatibility`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/release.py#L80`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/release.py#L80)
- Repository search: [validate_yaml_json_assets](https://github.com/appsplorer/thomaslab-core/search?q=validate_yaml_json_assets&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Parse repository contracts/configs and JSON schemas used by research workflows.

### API inspection

~~~python
import inspect
from thomaslab.release import validate_yaml_json_assets

print(inspect.signature(validate_yaml_json_assets))
print(validate_yaml_json_assets.__doc__)
~~~

### Source

[`src/thomaslab/release.py#L80`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/release.py#L80)

---

<!-- callable:thomaslab.release.validate_notebook_numbering -->
## validate_notebook_numbering

### Purpose

Detect duplicate numbered guided notebooks while allowing unnumbered demos.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_notebook_numbering(repo_root: str | Path) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `repo_root` | `repo_root: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `repo_root`.

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
from thomaslab.release import validate_notebook_numbering

result = validate_notebook_numbering(
    repo_root="value"
)

print(result)
~~~

### Related functions

- `validate_version_consistency`
- `validate_public_module_exports`
- `validate_yaml_json_assets`
- `validate_deprecation_registry`
- `validate_api_compatibility`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/release.py#L123`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/release.py#L123)
- Repository search: [validate_notebook_numbering](https://github.com/appsplorer/thomaslab-core/search?q=validate_notebook_numbering&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Detect duplicate numbered guided notebooks while allowing unnumbered demos.

### API inspection

~~~python
import inspect
from thomaslab.release import validate_notebook_numbering

print(inspect.signature(validate_notebook_numbering))
print(validate_notebook_numbering.__doc__)
~~~

### Source

[`src/thomaslab/release.py#L123`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/release.py#L123)

---

<!-- callable:thomaslab.release.validate_deprecation_registry -->
## validate_deprecation_registry

### Purpose

Validate the structured deprecation policy/registry.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_deprecation_registry(repo_root: str | Path) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `repo_root` | `repo_root: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `repo_root`.

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
from thomaslab.release import validate_deprecation_registry

result = validate_deprecation_registry(
    repo_root="value"
)

print(result)
~~~

### Related functions

- `validate_version_consistency`
- `validate_public_module_exports`
- `validate_yaml_json_assets`
- `validate_notebook_numbering`
- `validate_api_compatibility`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/release.py#L144`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/release.py#L144)
- Repository search: [validate_deprecation_registry](https://github.com/appsplorer/thomaslab-core/search?q=validate_deprecation_registry&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate the structured deprecation policy/registry.

### API inspection

~~~python
import inspect
from thomaslab.release import validate_deprecation_registry

print(inspect.signature(validate_deprecation_registry))
print(validate_deprecation_registry.__doc__)
~~~

### Source

[`src/thomaslab/release.py#L144`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/release.py#L144)

---

<!-- callable:thomaslab.release.validate_api_compatibility -->
## validate_api_compatibility

### Purpose

Validate the v1 public-module compatibility manifest against the package.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_api_compatibility(repo_root: str | Path) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `repo_root` | `repo_root: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `repo_root`.

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
from thomaslab.release import validate_api_compatibility

result = validate_api_compatibility(
    repo_root="value"
)

print(result)
~~~

### Related functions

- `validate_version_consistency`
- `validate_public_module_exports`
- `validate_yaml_json_assets`
- `validate_notebook_numbering`
- `validate_deprecation_registry`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/release.py#L209`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/release.py#L209)
- Repository search: [validate_api_compatibility](https://github.com/appsplorer/thomaslab-core/search?q=validate_api_compatibility&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate the v1 public-module compatibility manifest against the package.

### API inspection

~~~python
import inspect
from thomaslab.release import validate_api_compatibility

print(inspect.signature(validate_api_compatibility))
print(validate_api_compatibility.__doc__)
~~~

### Source

[`src/thomaslab/release.py#L209`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/release.py#L209)

---

<!-- callable:thomaslab.release.validate_release_files -->
## validate_release_files

### Purpose

Check the stable-release governance and user-facing files expected for v1.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_release_files(repo_root: str | Path) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `repo_root` | `repo_root: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `repo_root`.

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
from thomaslab.release import validate_release_files

result = validate_release_files(
    repo_root="value"
)

print(result)
~~~

### Related functions

- `validate_version_consistency`
- `validate_public_module_exports`
- `validate_yaml_json_assets`
- `validate_notebook_numbering`
- `validate_deprecation_registry`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/release.py#L266`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/release.py#L266)
- Repository search: [validate_release_files](https://github.com/appsplorer/thomaslab-core/search?q=validate_release_files&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Check the stable-release governance and user-facing files expected for v1.

### API inspection

~~~python
import inspect
from thomaslab.release import validate_release_files

print(inspect.signature(validate_release_files))
print(validate_release_files.__doc__)
~~~

### Source

[`src/thomaslab/release.py#L266`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/release.py#L266)

---

<!-- callable:thomaslab.release.run_release_qa -->
## run_release_qa

### Purpose

Run all lightweight repository-level release checks.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def run_release_qa(repo_root: str | Path) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `repo_root` | `repo_root: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `repo_root`.

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
from thomaslab.release import run_release_qa

result = run_release_qa(
    repo_root="value"
)

print(result)
~~~

### Related functions

- `validate_version_consistency`
- `validate_public_module_exports`
- `validate_yaml_json_assets`
- `validate_notebook_numbering`
- `validate_deprecation_registry`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/release.py#L325`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/release.py#L325)
- Repository search: [run_release_qa](https://github.com/appsplorer/thomaslab-core/search?q=run_release_qa&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Run all lightweight repository-level release checks.

### API inspection

~~~python
import inspect
from thomaslab.release import run_release_qa

print(inspect.signature(run_release_qa))
print(run_release_qa.__doc__)
~~~

### Source

[`src/thomaslab/release.py#L325`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/release.py#L325)

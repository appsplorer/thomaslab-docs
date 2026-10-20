# thomaslab.interop

Lightweight FHIR Bundle interoperability helpers for research extraction.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 4

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.interop.validate_fhir_bundle -->
## validate_fhir_bundle

### Purpose

Validate the minimum structure required to safely iterate a FHIR Bundle.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_fhir_bundle(bundle: dict[str, Any]) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `bundle` | `bundle: dict[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `bundle`.

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
from thomaslab.interop import validate_fhir_bundle

result = validate_fhir_bundle(
    bundle={}
)

print(result)
~~~

### Related functions

- `flatten_fhir_bundle`
- `extract_fhir_observations`
- `extract_fhir_medication_requests`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/interop.py#L10`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/interop.py#L10)
- Repository search: [validate_fhir_bundle](https://github.com/appsplorer/thomaslab-core/search?q=validate_fhir_bundle&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate the minimum structure required to safely iterate a FHIR Bundle.

This is a structural validator, not full profile/conformance validation. Use an official FHIR
validator for implementation-guide or profile conformance testing.

### API inspection

~~~python
import inspect
from thomaslab.interop import validate_fhir_bundle

print(inspect.signature(validate_fhir_bundle))
print(validate_fhir_bundle.__doc__)
~~~

### Source

[`src/thomaslab/interop.py#L10`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/interop.py#L10)

---

<!-- callable:thomaslab.interop.flatten_fhir_bundle -->
## flatten_fhir_bundle

### Purpose

Flatten FHIR Bundle entries into one row per resource with raw-resource preservation.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def flatten_fhir_bundle( bundle: dict[str, Any], resource_types: list[str] | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `bundle` | `bundle: dict[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `resource_types` | `resource_types: list[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `bundle`.

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
from thomaslab.interop import flatten_fhir_bundle

result = flatten_fhir_bundle(
    bundle={}
)

print(result)
~~~

### Related functions

- `validate_fhir_bundle`
- `extract_fhir_observations`
- `extract_fhir_medication_requests`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/interop.py#L50`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/interop.py#L50)
- Repository search: [flatten_fhir_bundle](https://github.com/appsplorer/thomaslab-core/search?q=flatten_fhir_bundle&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Flatten FHIR Bundle entries into one row per resource with raw-resource preservation.

### API inspection

~~~python
import inspect
from thomaslab.interop import flatten_fhir_bundle

print(inspect.signature(flatten_fhir_bundle))
print(flatten_fhir_bundle.__doc__)
~~~

### Source

[`src/thomaslab/interop.py#L50`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/interop.py#L50)

---

<!-- callable:thomaslab.interop.extract_fhir_observations -->
## extract_fhir_observations

### Purpose

Extract common FHIR Observation fields into an analysis-friendly table.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def extract_fhir_observations(bundle: dict[str, Any]) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `bundle` | `bundle: dict[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `bundle`.

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
from thomaslab.interop import extract_fhir_observations

result = extract_fhir_observations(
    bundle={}
)

print(result)
~~~

### Related functions

- `validate_fhir_bundle`
- `flatten_fhir_bundle`
- `extract_fhir_medication_requests`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/interop.py#L109`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/interop.py#L109)
- Repository search: [extract_fhir_observations](https://github.com/appsplorer/thomaslab-core/search?q=extract_fhir_observations&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Extract common FHIR Observation fields into an analysis-friendly table.

### API inspection

~~~python
import inspect
from thomaslab.interop import extract_fhir_observations

print(inspect.signature(extract_fhir_observations))
print(extract_fhir_observations.__doc__)
~~~

### Source

[`src/thomaslab/interop.py#L109`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/interop.py#L109)

---

<!-- callable:thomaslab.interop.extract_fhir_medication_requests -->
## extract_fhir_medication_requests

### Purpose

Extract common FHIR MedicationRequest fields for research medication timelines.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def extract_fhir_medication_requests(bundle: dict[str, Any]) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `bundle` | `bundle: dict[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `bundle`.

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
from thomaslab.interop import extract_fhir_medication_requests

result = extract_fhir_medication_requests(
    bundle={}
)

print(result)
~~~

### Related functions

- `validate_fhir_bundle`
- `flatten_fhir_bundle`
- `extract_fhir_observations`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/interop.py#L148`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/interop.py#L148)
- Repository search: [extract_fhir_medication_requests](https://github.com/appsplorer/thomaslab-core/search?q=extract_fhir_medication_requests&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Extract common FHIR MedicationRequest fields for research medication timelines.

### API inspection

~~~python
import inspect
from thomaslab.interop import extract_fhir_medication_requests

print(inspect.signature(extract_fhir_medication_requests))
print(extract_fhir_medication_requests.__doc__)
~~~

### Source

[`src/thomaslab/interop.py#L148`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/interop.py#L148)

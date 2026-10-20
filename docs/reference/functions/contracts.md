# thomaslab.contracts

Canonical domain contracts for robust clinical dataset onboarding.

The contract layer defines *structure*, not clinical truth. A contract can assert that a
column is required, numeric, datetime-like, or unique, but it cannot establish that a
site-specific code has the clinical meaning claimed by a study protocol.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 7

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.contracts.get_domain_contract -->
## get_domain_contract

### Purpose

Return a defensive copy of a built-in canonical domain contract.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def get_domain_contract(domain: str) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `domain` | `domain: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `domain`.

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
from thomaslab.contracts import get_domain_contract

result = get_domain_contract(
    domain="value"
)

print(result)
~~~

### Related functions

- `infer_domain_from_columns`
- `build_data_contract`
- `load_data_contract`
- `validate_domain_contract`
- `validate_cross_domain_keys`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/contracts.py#L990`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/contracts.py#L990)
- Repository search: [get_domain_contract](https://github.com/appsplorer/thomaslab-core/search?q=get_domain_contract&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return a defensive copy of a built-in canonical domain contract.

### API inspection

~~~python
import inspect
from thomaslab.contracts import get_domain_contract

print(inspect.signature(get_domain_contract))
print(get_domain_contract.__doc__)
~~~

### Source

[`src/thomaslab/contracts.py#L990`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/contracts.py#L990)

---

<!-- callable:thomaslab.contracts.infer_domain_from_columns -->
## infer_domain_from_columns

### Purpose

Rank canonical domains from the columns available in ``data``.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def infer_domain_from_columns(data: Any) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `data` | `data: Any` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `data`.

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

from thomaslab.contracts import infer_domain_from_columns

result = infer_domain_from_columns(
    data=sample_df
)

print(result)
~~~

### Related functions

- `get_domain_contract`
- `build_data_contract`
- `load_data_contract`
- `validate_domain_contract`
- `validate_cross_domain_keys`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/contracts.py#L998`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/contracts.py#L998)
- Repository search: [infer_domain_from_columns](https://github.com/appsplorer/thomaslab-core/search?q=infer_domain_from_columns&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Rank canonical domains from the columns available in ``data``.

The score is structural only. It is useful for onboarding, but a high score does
not prove that the source table has the corresponding clinical semantics.

### API inspection

~~~python
import inspect
from thomaslab.contracts import infer_domain_from_columns

print(inspect.signature(infer_domain_from_columns))
print(infer_domain_from_columns.__doc__)
~~~

### Source

[`src/thomaslab/contracts.py#L998`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/contracts.py#L998)

---

<!-- callable:thomaslab.contracts.build_data_contract -->
## build_data_contract

### Purpose

Create a YAML-serializable contract from a canonicalized table.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_data_contract( data: Any, *, domain: str | None = None, dataset_name: str = "dataset", required_columns: list[str] | None = None, column_roles: Mapping[str, str] | None = None, units: Mapping[str, str] | None = None, vocabularies: Mapping[str, str] | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `data` | `data: Any` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `domain` | `domain: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `dataset_name` | `dataset_name: str = 'dataset'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `required_columns` | `required_columns: list[str] \| None = None` | No | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `column_roles` | `column_roles: Mapping[str, str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `units` | `units: Mapping[str, str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `vocabularies` | `vocabularies: Mapping[str, str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `data`.

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

from thomaslab.contracts import build_data_contract

result = build_data_contract(
    data=sample_df
)

print(result)
~~~

### Related functions

- `get_domain_contract`
- `infer_domain_from_columns`
- `load_data_contract`
- `validate_domain_contract`
- `validate_cross_domain_keys`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/contracts.py#L1036`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/contracts.py#L1036)
- Repository search: [build_data_contract](https://github.com/appsplorer/thomaslab-core/search?q=build_data_contract&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create a YAML-serializable contract from a canonicalized table.

### API inspection

~~~python
import inspect
from thomaslab.contracts import build_data_contract

print(inspect.signature(build_data_contract))
print(build_data_contract.__doc__)
~~~

### Source

[`src/thomaslab/contracts.py#L1036`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/contracts.py#L1036)

---

<!-- callable:thomaslab.contracts.load_data_contract -->
## load_data_contract

### Purpose

Load a data contract from YAML or a mapping and perform basic validation.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def load_data_contract(contract: str | Path | Mapping[str, Any]) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `contract` | `contract: str \| Path \| Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `contract`.

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
from thomaslab.contracts import load_data_contract

result = load_data_contract(
    contract={}
)

print(result)
~~~

### Related functions

- `get_domain_contract`
- `infer_domain_from_columns`
- `build_data_contract`
- `validate_domain_contract`
- `validate_cross_domain_keys`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/contracts.py#L1085`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/contracts.py#L1085)
- Repository search: [load_data_contract](https://github.com/appsplorer/thomaslab-core/search?q=load_data_contract&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Load a data contract from YAML or a mapping and perform basic validation.

### API inspection

~~~python
import inspect
from thomaslab.contracts import load_data_contract

print(inspect.signature(load_data_contract))
print(load_data_contract.__doc__)
~~~

### Source

[`src/thomaslab/contracts.py#L1085`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/contracts.py#L1085)

---

<!-- callable:thomaslab.contracts.validate_domain_contract -->
## validate_domain_contract

### Purpose

Validate a table against a structural data contract.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_domain_contract( data: Any, contract: str | Path | Mapping[str, Any], *, strict: bool = False, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `data` | `data: Any` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `contract` | `contract: str \| Path \| Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strict` | `strict: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `data`, `contract`.

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

from thomaslab.contracts import validate_domain_contract

result = validate_domain_contract(
    data=sample_df,
    contract={}
)

print(result)
~~~

### Related functions

- `get_domain_contract`
- `infer_domain_from_columns`
- `build_data_contract`
- `load_data_contract`
- `validate_cross_domain_keys`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/contracts.py#L1126`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/contracts.py#L1126)
- Repository search: [validate_domain_contract](https://github.com/appsplorer/thomaslab-core/search?q=validate_domain_contract&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate a table against a structural data contract.

Validation covers required columns, expected numeric/datetime parsability, and
configured uniqueness. It deliberately does not infer clinical correctness.

### API inspection

~~~python
import inspect
from thomaslab.contracts import validate_domain_contract

print(inspect.signature(validate_domain_contract))
print(validate_domain_contract.__doc__)
~~~

### Source

[`src/thomaslab/contracts.py#L1126`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/contracts.py#L1126)

---

<!-- callable:thomaslab.contracts.validate_cross_domain_keys -->
## validate_cross_domain_keys

### Purpose

Audit patient-key coverage across multiple canonical domain tables.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_cross_domain_keys( tables: Mapping[str, pd.DataFrame], *, patient_key: str = "patient_id", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `tables` | `tables: Mapping[str, pd.DataFrame]` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_key` | `patient_key: str = 'patient_id'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `tables`.

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

from thomaslab.contracts import validate_cross_domain_keys

result = validate_cross_domain_keys(
    tables=sample_df
)

print(result)
~~~

### Related functions

- `get_domain_contract`
- `infer_domain_from_columns`
- `build_data_contract`
- `load_data_contract`
- `validate_domain_contract`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/contracts.py#L1184`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/contracts.py#L1184)
- Repository search: [validate_cross_domain_keys](https://github.com/appsplorer/thomaslab-core/search?q=validate_cross_domain_keys&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Audit patient-key coverage across multiple canonical domain tables.

### API inspection

~~~python
import inspect
from thomaslab.contracts import validate_cross_domain_keys

print(inspect.signature(validate_cross_domain_keys))
print(validate_cross_domain_keys.__doc__)
~~~

### Source

[`src/thomaslab/contracts.py#L1184`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/contracts.py#L1184)

---

<!-- callable:thomaslab.contracts.generate_contract_yaml -->
## generate_contract_yaml

### Purpose

Write a contract to YAML with stable key ordering.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def generate_contract_yaml(contract: Mapping[str, Any], output_path: str | Path) -> Path
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `contract` | `contract: Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `output_path` | `output_path: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `contract`, `output_path`.

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
from thomaslab.contracts import generate_contract_yaml

result = generate_contract_yaml(
    contract={},
    output_path="path/to/input.csv"
)

print(result)
~~~

### Related functions

- `get_domain_contract`
- `infer_domain_from_columns`
- `build_data_contract`
- `load_data_contract`
- `validate_domain_contract`

### Related workflow

- Guide: [Readme](../../new-dataset/README.md)
- Guided notebooks: Notebooks 01–09
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/contracts.py#L1211`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/contracts.py#L1211)
- Repository search: [generate_contract_yaml](https://github.com/appsplorer/thomaslab-core/search?q=generate_contract_yaml&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Write a contract to YAML with stable key ordering.

### API inspection

~~~python
import inspect
from thomaslab.contracts import generate_contract_yaml

print(inspect.signature(generate_contract_yaml))
print(generate_contract_yaml.__doc__)
~~~

### Source

[`src/thomaslab/contracts.py#L1211`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/contracts.py#L1211)

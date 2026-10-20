# thomaslab.research_bundle

Low-level research-bundle export; tables are NOT deidentified or access-controlled.

For collaborator notebooks with patient-level data use the policy-gated
``thomaslab.adaptive.safe_bundle.export_governed_bundle`` instead.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 4

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.research_bundle.export_research_bundle -->
## export_research_bundle

### Purpose

Expert-only ungoverned export of supplied tables, including any PHI.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def export_research_bundle( output_dir: str | Path, *, tables: Mapping[str, pd.DataFrame], study_spec: Mapping[str, Any] | str | Path, run_manifest: Mapping[str, Any], metadata: Mapping[str, Any] | None = None, overwrite: bool = False, include_index: bool = False, ) -> Path
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `output_dir` | `output_dir: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `tables` | `tables: Mapping[str, pd.DataFrame]` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `study_spec` | `study_spec: Mapping[str, Any] \| str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `run_manifest` | `run_manifest: Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `metadata` | `metadata: Mapping[str, Any] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `overwrite` | `overwrite: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `include_index` | `include_index: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `output_dir`, `tables`, `study_spec`, `run_manifest`.

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

from thomaslab.research_bundle import export_research_bundle

result = export_research_bundle(
    output_dir="value",
    tables=sample_df,
    study_spec={},
    run_manifest={}
)

print(result)
~~~

### Related functions

- `bundle_inventory`
- `verify_research_bundle`
- `load_bundle_table`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/research_bundle.py#L53`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/research_bundle.py#L53)
- Repository search: [export_research_bundle](https://github.com/appsplorer/thomaslab-core/search?q=export_research_bundle&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Expert-only ungoverned export of supplied tables, including any PHI.

Checksums verify byte integrity only. This routine does **not** deidentify,
suppress small cells, check permissions, or grant a publication approval.
For clinical collaborators use the governed session/export instead.

### API inspection

~~~python
import inspect
from thomaslab.research_bundle import export_research_bundle

print(inspect.signature(export_research_bundle))
print(export_research_bundle.__doc__)
~~~

### Source

[`src/thomaslab/research_bundle.py#L53`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/research_bundle.py#L53)

---

<!-- callable:thomaslab.research_bundle.bundle_inventory -->
## bundle_inventory

### Purpose

Return the payload inventory declared by a research bundle.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def bundle_inventory(bundle_dir: str | Path) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `bundle_dir` | `bundle_dir: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `bundle_dir`.

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
from thomaslab.research_bundle import bundle_inventory

result = bundle_inventory(
    bundle_dir="value"
)

print(result)
~~~

### Related functions

- `export_research_bundle`
- `verify_research_bundle`
- `load_bundle_table`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/research_bundle.py#L166`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/research_bundle.py#L166)
- Repository search: [bundle_inventory](https://github.com/appsplorer/thomaslab-core/search?q=bundle_inventory&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return the payload inventory declared by a research bundle.

### API inspection

~~~python
import inspect
from thomaslab.research_bundle import bundle_inventory

print(inspect.signature(bundle_inventory))
print(bundle_inventory.__doc__)
~~~

### Source

[`src/thomaslab/research_bundle.py#L166`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/research_bundle.py#L166)

---

<!-- callable:thomaslab.research_bundle.verify_research_bundle -->
## verify_research_bundle

### Purpose

Verify payload presence and SHA-256 checksums without interpreting scientific validity.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def verify_research_bundle( bundle_dir: str | Path, *, strict_unexpected: bool = False, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `bundle_dir` | `bundle_dir: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strict_unexpected` | `strict_unexpected: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `bundle_dir`.

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
from thomaslab.research_bundle import verify_research_bundle

result = verify_research_bundle(
    bundle_dir="value"
)

print(result)
~~~

### Related functions

- `export_research_bundle`
- `bundle_inventory`
- `load_bundle_table`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/research_bundle.py#L176`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/research_bundle.py#L176)
- Repository search: [verify_research_bundle](https://github.com/appsplorer/thomaslab-core/search?q=verify_research_bundle&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Verify payload presence and SHA-256 checksums without interpreting scientific validity.

### API inspection

~~~python
import inspect
from thomaslab.research_bundle import verify_research_bundle

print(inspect.signature(verify_research_bundle))
print(verify_research_bundle.__doc__)
~~~

### Source

[`src/thomaslab/research_bundle.py#L176`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/research_bundle.py#L176)

---

<!-- callable:thomaslab.research_bundle.load_bundle_table -->
## load_bundle_table

### Purpose

Load one CSV table from a verified bundle path.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def load_bundle_table(bundle_dir: str | Path, table_name: str) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `bundle_dir` | `bundle_dir: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `table_name` | `table_name: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `bundle_dir`, `table_name`.

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
from thomaslab.research_bundle import load_bundle_table

result = load_bundle_table(
    bundle_dir="value",
    table_name="value"
)

print(result)
~~~

### Related functions

- `export_research_bundle`
- `bundle_inventory`
- `verify_research_bundle`

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/research_bundle.py#L235`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/research_bundle.py#L235)
- Repository search: [load_bundle_table](https://github.com/appsplorer/thomaslab-core/search?q=load_bundle_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Load one CSV table from a verified bundle path.

### API inspection

~~~python
import inspect
from thomaslab.research_bundle import load_bundle_table

print(inspect.signature(load_bundle_table))
print(load_bundle_table.__doc__)
~~~

### Source

[`src/thomaslab/research_bundle.py#L235`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/research_bundle.py#L235)

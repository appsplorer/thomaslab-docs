# thomaslab.integrated_workflow

Expert dataset-to-bundle workflow with structural checks only.

This legacy integration exports the complete analysis dataset unchanged,
potentially including patient identifiers. It is not safe to use on institutional
patient data without a separate reviewed output policy; use GovernedNotebookSession.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 1

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.integrated_workflow.run_integrated_research_workflow -->
## run_integrated_research_workflow

### Purpose

Prepare data, check contracts, capture provenance, and export raw tables.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def run_integrated_research_workflow( data: pd.DataFrame, output_dir: str | Path, *, study_spec: Mapping[str, Any] | str | Path, dataset_name: str, schema: Mapping[str, Any] | str | Path | None = None, contract: Mapping[str, Any] | str | Path | None = None, domain: str | None = None, required_columns: Sequence[str] | None = None, result_tables: Mapping[str, pd.DataFrame] | None = None, result_contracts: Mapping[str, Mapping[str, Any] | str | Path] | None = None, seed: int | None = None, git_commit: str | None = None, strict: bool = True, overwrite: bool = False, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `data` | `data: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `output_dir` | `output_dir: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `study_spec` | `study_spec: Mapping[str, Any] \| str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `dataset_name` | `dataset_name: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `schema` | `schema: Mapping[str, Any] \| str \| Path \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `contract` | `contract: Mapping[str, Any] \| str \| Path \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `domain` | `domain: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `required_columns` | `required_columns: Sequence[str] \| None = None` | No | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `result_tables` | `result_tables: Mapping[str, pd.DataFrame] \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `result_contracts` | `result_contracts: Mapping[str, Mapping[str, Any] \| str \| Path] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `seed` | `seed: int \| None = None` | No | Reproducibility seed. Record it in the study bundle. |
| `git_commit` | `git_commit: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strict` | `strict: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `overwrite` | `overwrite: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `data`, `output_dir`, `study_spec`, `dataset_name`.

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

from thomaslab.integrated_workflow import run_integrated_research_workflow

result = run_integrated_research_workflow(
    data=sample_df,
    output_dir="value",
    study_spec={},
    dataset_name="value"
)

print(result)
~~~

### Related functions

- No additional public callable is defined in this module.

### Related workflow

- Guide: [Reproducible Research Workflow](../../guides/reproducible-research-workflow.md)
- Guided notebooks: Notebooks 56–58
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/integrated_workflow.py#L36`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/integrated_workflow.py#L36)
- Repository search: [run_integrated_research_workflow](https://github.com/appsplorer/thomaslab-core/search?q=run_integrated_research_workflow&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Prepare data, check contracts, capture provenance, and export raw tables.

The workflow deliberately does not auto-approve inferred mappings or clinical
semantics. A schema is applied only when the caller supplies one. Without a schema,
source columns are preserved and contract validation occurs against those columns.

**Sensitive-data warning:** this trusted expert API serializes the entire
standardized dataset and result tables. It has no deidentification guarantee.
Guided collaborator workflows must use ``GovernedNotebookSession`` and its
restricted exporter instead.

### API inspection

~~~python
import inspect
from thomaslab.integrated_workflow import run_integrated_research_workflow

print(inspect.signature(run_integrated_research_workflow))
print(run_integrated_research_workflow.__doc__)
~~~

### Source

[`src/thomaslab/integrated_workflow.py#L36`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/integrated_workflow.py#L36)

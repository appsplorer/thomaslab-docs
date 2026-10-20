# v1 self-service reference workflow

Version 1.0.0 is the stable self-service release of thomaslab-core. The recommended path for a new analysis is intentionally reviewable rather than fully automatic.

## Workflow

1. Inspect the unfamiliar source and define or review its schema mapping.
2. Validate the canonical data contract before modeling.
3. Freeze the study specification and declare the reproducibility seed.
4. Run study-specific analysis modules with explicit assumptions.
5. Validate downstream result tables against their contracts.
6. Capture environment and input fingerprints in the run manifest.
7. Export the final research bundle.
8. Verify bundle checksums before manuscript handoff or archival.
9. Re-run external/site validation and scientific sensitivity analyses required by the protocol.

The integration layer can orchestrate the contract/provenance/export stages, but it does not auto-approve clinical semantics.

## Minimal stable path

```python
from pathlib import Path

import pandas as pd

from thomaslab.integrated_workflow import run_integrated_research_workflow

patients = pd.DataFrame(
    {
        "patient_id": [1, 2, 3],
        "age": [55, 61, 70],
        "sex": ["F", "M", "F"],
    }
)

study = {
    "study_id": "example-v1-study",
    "title": "Example v1 study",
    "version": "1.0",
    "design": {"type": "observational"},
    "data": {"datasets": [{"name": "patients", "domain": "person"}]},
    "analysis": {"primary": {"name": "descriptive"}},
    "reproducibility": {"seed": 2026},
}

contract = {
    "dataset_name": "patients",
    "domain": "person",
    "required_columns": ["patient_id"],
    "columns": ["patient_id", "age", "sex"],
    "dtypes": {},
    "datetime_columns": [],
    "numeric_columns": ["age"],
    "unique_keys": ["patient_id"],
    "column_roles": {},
    "units": {},
    "vocabularies": {},
}

result = run_integrated_research_workflow(
    patients,
    Path("research_bundle"),
    study_spec=study,
    dataset_name="patients",
    contract=contract,
    strict=True,
)
assert result["contract_report"]["valid"]
assert result["bundle_verification"]["valid"]
```

For real data, replace the demonstration contract with a reviewed study-specific mapping/contract and keep protected health information inside an institutionally approved environment.

## What v1 stability means

The v1 release freezes the documented public-module baseline and strengthens packaging, import, notebook, documentation, and compatibility checks. It does not freeze every numerical result across different dependency/hardware stacks, and it does not convert reproducibility metadata into evidence of scientific validity.

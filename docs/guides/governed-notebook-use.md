# Using Thomas Lab notebooks with governed research data

The interactive notebook framework is intended for Jupyter, PyCharm notebooks,
and Kaggle **synthetic-only** demonstrations. It does **not** provision user
accounts, approve datasets, enforce institution-wide storage ACLs, anonymize
patient records, or confer HIPAA/IRB approval.

## Lab deployment checklist

1. The institution approves the data-use agreement, study personnel, storage
   volume, compute environment, notebook host, and safe artifact directories.
2. A named lab data steward classifies each source as `PUBLIC`, `SYNTHETIC`,
   `INTERNAL_APPROVED`, or `RESTRICTED`. Unclassified is denied. Kaggle notebook execution accepts
   only SYNTHETIC inputs, even if a user edits the local host name. Licensed
   public research data belong on independently approved local/HPC compute.
3. The steward registers and independently approves a site/grain-specific
   dataset adapter following full-source validation. Inferred mapping
   suggestions remain drafts until reviewed.
4. A notebook session uses an `ExecutionPolicy` listing narrow **absolute**
   approved input/output locations, an actor and an audit destination. Required
   host authorization must also exist outside Python.
5. `GovernedNotebookSession.open_source` validates the policy before reading;
   `run` requires a matching `FullValidationReport` checksum, full row count,
   and approved adapter. Every run reports separate SOFTWARE, DATA and METHOD
   statuses. All runs remain `REVIEW_REQUIRED` for scientific interpretation.
6. `session.export` uses the governed bundle exporter, never the older raw
   bundle exporter. By default, a supplied table must be an explicitly reviewed
   aggregate with per-group denominators of at least 11 and no direct-identifier
   columns. The threshold is a conservative default, **not** an institutional
   disclosure assessment. Free-text identifiers or rare combinations need
   separate expert review.

## Synthetic notebook example

```python
from pathlib import Path
from thomaslab.adaptive.governance import ExecutionPolicy
from thomaslab.adaptive.governed_session import GovernedNotebookSession

workspace = Path("/absolute/path/to/approved/synthetic_workspace")
policy = ExecutionPolicy(
    environment="local",
    approved_input_roots=(workspace,),
    approved_output_roots=(workspace,),
    actor="authorized_researcher_01",
    audit_path=workspace / "audit.jsonl",
)
session = GovernedNotebookSession(policy, actor="authorized_researcher_01")
frame = session.open_source({
    "path": workspace / "synthetic_cohort.csv", "classification": "SYNTHETIC"
})
# Obtain a real complete FullValidationReport and an APPROVED AdapterRevision
# before session.run(...). Example never constructs a fake approval.
```

The traditional `thomaslab.research_bundle.export_research_bundle`,
`thomaslab.easy.export_analysis_bundle`, and
`thomaslab.integrated_workflow.run_integrated_research_workflow` are
**expert-only ungoverned** routines: they write supplied rows without removing
PHI. Never confuse checksum correctness with scientific validation, disclosure
review, or a patient's consent. Audit hash chains reveal some accidental local
edits but are not centrally immutable institutional audit services.

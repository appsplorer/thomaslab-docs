# S08 — Role-separated, auditable EHR mapping review queue

**Status:** focused synthetic development candidate. Not a hospital identity provider, cryptographic signature service, approved clinical mapping, or an authorization to process/export patient rows. A separate institution-managed IAM/role-verification service, filesystem controls, source DUA/IRB permissions, full-source validation and final AdapterRegistry review remain required.

The private module is `thomaslab.adaptive.review_queue.MappingReviewQueue`. It takes the existing S07 metadata-only `rank_reviewable_field_destinations` output; it does **not** open EHR source files, inspect patient values, perform OMOP transformations, run model inference or download external vocabularies.

## Review states

| Stage | Required reviewer role | Permitted decisions | Next state |
|---|---|---|---|
| `PENDING_INTERN` | `intern` | `TRIAGE_ACCEPT` with one source-field/domain/target candidate, or `TRIAGE_REJECT` | Clinical review or rejected |
| `PENDING_CLINICAL` | `clinical_expert` | `CLINICAL_ACCEPT` with a reference to supporting evidence, or `CLINICAL_REJECT` | Steward review or rejected |
| `PENDING_STEWARD` | `data_steward` | `STEWARD_CLEAR` with policy-evidence reference, or `STEWARD_REJECT` | Reviewed for validation or rejected |
| `REVIEWED_FOR_VALIDATION` | None | Terminal; no additional decisions | **Not approved for clinical ETL/export** |
| `REJECTED` | None | Terminal; create a new task with revised evidence | No automatic retry |

**Every accepting stage requires a different actor**, independently checked against an external role verifier. An intern cannot approve their own source mapping as a clinician or steward. Candidates in an S07 `ABSTAIN_...` state cannot be triaged as accepted. Source release and S01 structural fingerprint are retained with the task.

Review records are scoped to a private, precreated **institutionally approved** output directory. Each task has one immutable-by-normal-API proposal JSON and a sequence of write-once JSON event files. Permissions use 0700 task folders, 0600 records, exclusive event creation, bounded read/write sizes and an exclusive per-task lock. Each event refers to the previous SHA-256 record.

**Important limitation:** a local hash chain detects ordinary modifications, reorderings and missing intermediate records; it is not digitally signed and cannot prove authenticity, resist an administrator rewriting a complete chain or detect removal of the final event(s) without an external witness. Institutional append-only storage, trusted timestamps, remote audit anchoring, RBAC and backup/recovery remain future work.

## Example using invented synthetic metadata

```python
from pathlib import Path
import pandas as pd

from thomaslab.adaptive.governance import ExecutionPolicy
from thomaslab.adaptive.schema_discovery import discover_source_schema
from thomaslab.adaptive.field_suggestions import rank_reviewable_field_destinations
from thomaslab.adaptive.review_queue import MappingReviewQueue

# Only synthetic data in this example; create this private directory in
# an institution-approved location before constructing the queue.
root = Path("/your-approved-workspace/review")
policy = ExecutionPolicy(
    environment="local",  # only synthetic fixtures in local development
    approved_input_roots=(root.parent,),
    approved_output_roots=(root.parent,),
    actor="synthetic_operator", reviewer="synthetic_supervisor",
)
manifest = {
    "source_system": "synthetic_hospital",
    "source_release": "v1",
    "table_name": "lab_results",
    "classification": "SYNTHETIC",
}
profile = discover_source_schema(
    [pd.DataFrame({
        "subject_id": ["SYNTH-001"],
        "test_name": ["Invented assay"],
        "result_value": ["1"],
    })],
    source_system="synthetic_hospital",
    source_release="v1", table_name="lab_results",
)
suggestions = rank_reviewable_field_destinations(
    profile, domains=("measurement",),
)
queue = MappingReviewQueue(root, policy=policy, source_manifest=manifest)
task_id = queue.create(suggestions, source_column="result_value")

# Synthetic demo verifier ONLY. Real datasets require an independent IAM
# backend which validates source-specific roles and revocation.
def synthetic_demo_role_verifier(actor, role):
    return {
        ("synthetic.intern", "intern"),
        ("synthetic.clinician", "clinical_expert"),
        ("synthetic.steward", "data_steward"),
    }.__contains__((actor, role))

queue.decide(
    task_id, actor="synthetic.intern", role="intern",
    action="TRIAGE_ACCEPT", selected=("measurement", "lab_value"),
    rationale="Checked the synthetic source column against the staging contract.",
    verify_role=synthetic_demo_role_verifier,
)
queue.decide(
    task_id, actor="synthetic.clinician", role="clinical_expert",
    action="CLINICAL_ACCEPT",
    evidence_reference="SYNTH-ASSAY-EVIDENCE-01",
    rationale="Compared the fictional assay definition to the proposed staging field.",
    verify_role=synthetic_demo_role_verifier,
)
queue.decide(
    task_id, actor="synthetic.steward", role="data_steward",
    action="STEWARD_CLEAR",
    evidence_reference="SYNTH-POLICY-REVIEW-01",
    rationale="Checked the synthetic source scope and local storage policy.",
    verify_role=synthetic_demo_role_verifier,
)
status = queue.read(
    task_id, actor="synthetic.steward", role="data_steward",
    verify_role=synthetic_demo_role_verifier,
)
assert status["state"] == "REVIEWED_FOR_VALIDATION"
assert status["mapping_approved"] is False
assert status["full_source_validation_passed"] is False
assert status["authorized_for_export"] is False
```

`queue.list_pending(actor=..., role=..., verify_role=...)` returns up to 200 bounded, source-scoped task IDs pending at that role's stage; no original source values are displayed.

## Security, governance and review boundaries

- `verify_role(actor, role)` is a **required integration point**, not independently secured by the package. A notebook-provided `lambda _: True` or synthetic demo verifier **must never** authorize real hospital data. Provision trusted role checks outside the researcher's editable environment.
- The S08 queue explicitly refuses generic local All of Us CDR review. Restricted institutional EHR requires the existing `ExecutionPolicy` classifications/attestation and an approved output root, but these declarations do not themselves prove actual IRB/DUA/credential rights.
- Do not include patient names, medical record numbers, secrets or free-text PHI in the rationale, evidence tracking ID, field labels or repository/CI artifacts. **This module does not automatically detect/redact PHI entered into a rationale.** Review history is restricted metadata.
- `REVIEWED_FOR_VALIDATION` is a **workflow milestone only**. This implementation deliberately does not modify or bypass existing `MappingWorkbench`, `ReviewedMapping`, `FullValidationReport` or `AdapterRegistry` approval checks.
- A new source-release/structural-fingerprint report requires a fresh review task; existing tasks do not automatically transfer to drifted data. S01 fingerprints test structural metadata integrity, not original EHR extract authenticity.
- Task listing is bounded to 200 and intended for small, approved local work queues. Distributed scheduling, identity federation, per-hospital assignment queues, externally signed audit logs and tamper-proof archive are not yet delivered.

## Technical testing and acceptance

```bash
python -m pytest -q tests/test_adaptive_review_queue.py
python scripts/ehr_platform_status.py
# Run the full exact-head Core and supported Python/HPC gate separately:
bash scripts/verify_hardening_candidate.sh
```

**48/48 focused synthetic tests passed locally** on Python 3.13.5, pandas 2.2.3, pytest 9.0.2. Python 3.9–3.13 grammar checks passed, and Git blobs matched the exact tested files. The local test environment included the real S03 and S07 algorithms with test-compatible S01/legacy canonical definition and governance surrogates. These results do **not** establish full private Core integration, real IAM, authorized storage deployment, institutional authentication, Python 3.9 runtime, hospital/All of Us/MIMIC-IV acceptance or independent clinical review.

P1-07 is marked `LOCAL_TEST_PASS` only, not independently accepted. The next source/schema-drift approval-memory milestone is P1-08; P1-03 authorized SQL/FHIR and full Core/HPC release gates remain open.

See the [EHR platform engineering plan](../../guides/ehr-platform-build-plan.md) and [S07 field proposals](field_suggestions.md).

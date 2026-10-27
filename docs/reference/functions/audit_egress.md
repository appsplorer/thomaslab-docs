# S14 — Restricted audit journal, disclosure screening and egress denial

**Status: local synthetic governance candidate; P0-06 remains OPEN.** The implementation does not provide hospital SSO/IAM, immutable/WORM auditing, central signing, certified disclosure controls or an authorized data-export channel. It is deliberately **deny-only**.

Private API: `thomaslab.adaptive.audit_egress`.

## Implemented components

**`AuditLedger(directory, policy=...)`** uses a pre-existing, private 0700 directory within approved Core output roots and a nonexporting `ExecutionPolicy`. `append(...)` requires an authenticated-role verifier callback, an opaque actor ID, a bounded action type and a SHA-256 scope reference. It writes 0600 metadata records with O_EXCL/NOFOLLOW and exclusive local write locks. Each record links to the preceding digest and is verified on journal read. The default journal capacity is 1,000 events.

The explicit roles are `INTERN_METADATA`, `CLINICAL_REVIEW`, and `STEWARD_METADATA`. The event types include `SOURCE_PREFLIGHT`, `SCHEMA_REVIEW`, `MAPPING_REVIEW`, `DISCLOSURE_REVIEW` and `EGRESS_DENIED`.

This is a **local consistency chain, not a cryptographic signature or a managed institutional audit trail**. An administrator with filesystem access can rewrite/truncate the chain or remove its final records; no external witnessed head, timestamp authority, disaster recovery or WORM attestations are implemented. Never store patient names, clinical note bodies or credentials in actor IDs, event fields, file paths, notebook outputs or issue logs.

**`preview_disclosure(counts, minimum_cell_count=11)`** screens only bounded integer cell counts. It blocks below-threshold cells; even if every cell is at least 11, it requires a separate complementary-suppression and differencing/linkage review. Its output does **not** reveal original counts, values or row data. Eleven is a conservative development default, **not a universally valid hospital, NIH or publication policy threshold**.

**`assess_egress(...)`** requires the role verifier, a source-scope digest, explicit destination/classification/payload type, and nonexporting Core policy. It always returns `EGRESS_BLOCKED_PENDING_INSTITUTIONAL_AUTHORIZATION`, for external, public, internal metadata and row-level requests alike. There is **no path that changes `authorized_for_export` to true**.

## Synthetic code example

```python
from thomaslab.adaptive.audit_egress import (
    AuditLedger, preview_disclosure, assess_egress,
)

# root: a pre-existing private directory inside the authorized output root
# policy: a valid nonexporting ExecutionPolicy; synthetic tests only
audit = AuditLedger(root, policy=policy)

def synthetic_demo_role_verifier(actor, tier):
    return actor == "synthetic_reviewer" and tier == "INTERN_METADATA"

event = audit.append(
    actor="synthetic_reviewer",
    tier="INTERN_METADATA",
    event="SCHEMA_REVIEW",
    scope_sha256="a" * 64,
    verify_role=synthetic_demo_role_verifier,  # TESTS ONLY, never for patient data
)
assert event["authorized_for_export"] is False

screen = preview_disclosure([5, 17, 24])
assert screen["status"] == "BLOCK_SMALL_CELL_OR_COMPLEMENTARY_RISK"

denied = assess_egress(
    actor="synthetic_reviewer",
    tier="INTERN_METADATA",
    destination="PUBLIC_RELEASE",
    data_classification="SYNTHETIC",
    payload_kind="AGGREGATE",
    scope_sha256="a" * 64,
    verify_role=synthetic_demo_role_verifier,
    policy=policy,
)
assert denied["authorized_for_export"] is False
```

The demonstration verifier is fake; the true deployment must call a hospital-controlled identity and role service. Merely passing a `True` callback is not independent authentication.

## S14 acceptance boundaries

The combined S13+S14 local regression suite passed **66/66 synthetic tests**, using a local compatible Core-governance substitute. It exercises role denials, audit append and restart, tampering, missing journal entries, symlink/path rejection, exclusive-lock conflicts, small-cell and malformed count rejection, attempted policy relaxation and denied egress. New source/test files match their executed Git blobs; Python 3.9–3.13 grammar passes. Actual private-Core full pytest/Ruff, Python 3.9 HPC, operational IAM, object store WORM anchoring, central audit/witness/restore, disclosure experts and external release controls have **not** been tested or approved.

For real hospital EHR, institutional audit retention, staff identity, egress control at network/storage boundaries, disclosure risk assessments (including repeated query differencing and complementary cells), and official export authorizations must be enforced **outside** this local metadata code. Therefore **P0-06 stays OPEN**.

```bash
python -m pytest -q tests/test_adaptive_audit_egress.py
python scripts/ehr_platform_status.py
bash scripts/verify_hardening_candidate.sh  # exact Core SHA on permitted HPC
```

Related: [S13 source-use contract](source_use_contract.md), [S12 archival release identity](release_manifest.md), [EHR development plan](../../guides/ehr-platform-build-plan.md).

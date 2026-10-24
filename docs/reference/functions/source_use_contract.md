# S13 — Institution-issued source-use and retention preflight

**Status: local synthetic contract candidate; P0-01 remains OPEN.** This module does not issue institutional data-use grants, independently authenticate a hospital, certify IRB/DUA consent, delete source records, authorize row access or approve a clinical dataset release.

Private API: `thomaslab.adaptive.source_use_contract.validate_source_use_contract`. It extends, rather than replaces, the existing `adaptive.governance.ExecutionPolicy` and `validate_environment` safety checks.

## What the contract requires

A source-use manifest must carry the exact `thomaslab-source-use-v1` version, source system and release, classification, opaque institution/agreement/ethics references, an explicitly bounded list of research purposes, allowed execution environments, an expiry and retention-until timestamp, a legal-hold boolean, one S01 SHA-256 structural fingerprint, and a data-use approval declaration. Values are strictly bounded so patient names, source connection strings, file paths and arbitrary comments cannot be stored in the review result.

Allowed purpose codes: `SCHEMA_REVIEW`, `MAPPING_REVIEW`, `METHODS_RESEARCH`, `CLINICAL_RESEARCH` and `QUALITY_VALIDATION`. Hospital-restricted and internally approved sources cannot request local compute. The general-purpose API rejects All of Us, which requires separate controlled Workbench authorization.

The gate checks expiry, retention coverage of the active permission, source classification, minimum compute environment, matching purpose and nonexporting policy. It then calls a required `verify_institutional_grant(actor, institution_reference, agreement_reference, purpose, contract_sha256)` function.

**The verifier must be implemented and operated by the institution**, separately from researcher-editable notebook code, using its real grants and revocation logic. A synthetic lambda returning `True` proves only that the integration interface is callable. The schema's `data_use_approved` boolean and contract hash are not signed permission or evidence of an actual hospital agreement. This library does not validate a signed institutional grant by itself.

### Test-only example

```python
from datetime import datetime, timedelta, timezone
from thomaslab.adaptive.governance import ExecutionPolicy
from thomaslab.adaptive.source_use_contract import validate_source_use_contract

now = datetime.now(timezone.utc)
contract = {
    "version": "thomaslab-source-use-v1",
    "source_system": "synthetic_hospital",
    "source_release": "v1",
    "classification": "SYNTHETIC",
    "institution_reference": "SYNTH-INSTITUTION-01",
    "agreement_reference": "SYNTH-DUA-01",
    "ethics_reference": "SYNTH-RESEARCH-01",
    "approved_purposes": ["SCHEMA_REVIEW"],
    "allowed_environments": ["local"],
    "expires_at": (now + timedelta(days=30)).isoformat(),
    "retain_until": (now + timedelta(days=365)).isoformat(),
    "legal_hold": False,
    "source_schema_fingerprint": "1" * 64,
    "data_use_approved": True,
}
# policy must have institution-approved input/output roots; use a synthetic
# local development policy only with invented datasets.
result = validate_source_use_contract(
    contract,
    purpose="SCHEMA_REVIEW",
    policy=policy,
    verify_institutional_grant=lambda *args: True,  # TESTS ONLY
)
assert result["actual_data_access_authorized"] is False
assert result["authorized_for_export"] is False
```

The output is a metadata-only structural preflight with `POLICY_PREFLIGHT_PASS_NO_ACCESS_GRANTED`, a deterministic contract hash and denial flags. A legal hold never authorizes automatic deletion; expiration and retention periods need rechecking against actual institutional policy. The gate never echoes agreement IDs, patient data or source records.

## S13 verification and limitations

The S13 tests cover bounded scopes, purpose mismatch, expired grants and retention, legal holds, unsafe classifications/environments, verifier denial/errors, All of Us exclusion, forged export policy and malformed Core policy objects. Focused S13/S14 combined offline suite: **66/66 synthetic tests passed** on local Python 3.13.5/pytest 9.0.2, with Python 3.9–3.13 syntax parsing. Both modules and tests match committed Git blob hashes. The isolated test environment uses a Core-`ExecutionPolicy` compatible local stub for the existing governance dependency; **full actual private-Core integration has not passed**.

Real hospital IAM and authorized research-purpose grants, ethics agreements, retention schedule/hold enforcement, approval provenance and revocation remain independent institutional responsibilities. **P0-01 stays OPEN**, even after the locally implemented code contract.

Related: [S14 audit and disclosure preflight](audit_egress.md), [S12 release manifest](release_manifest.md), [EHR development plan](../../guides/ehr-platform-build-plan.md).

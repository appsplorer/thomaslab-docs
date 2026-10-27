# S12 — Content-addressed research release manifests and archive preflight

**Engineering state:** candidate contract only. S12 does **not** create immutable archives, store real patient rows, transfer files, sign manifests, authorize clinical use, or publish OMOP datasets. P0-05 stays **OPEN** until independently configured storage, identity, retention and release gates are demonstrated.

Private module: `thomaslab.adaptive.release_manifest`. This extends the S01 source-fingerprint, S10 staging and S11 OHDSI 5.4.3 target contracts; it neither replaces nor approves their clinical transformations.

## Implemented scope

| Function | Evidence and boundaries |
|---|---|
| `build_release_manifest` | Generates a deterministic SHA-256 `release_id` from tightly restricted metadata and declared content hashes. No data files are opened |
| `validate_release_manifest` | Checks exact identity integrity and a complete, noncyclic **source → staging → OMOP** DAG; returns release-blocked diagnostics |
| `verify_synthetic_archive_files` | Opens only **local synthetic** files in a precreated private directory, hashes them with bounded streaming reads and refuses mismatches, symlinks or unexpected file sizes. It never writes an archive |
| `inspect_worm_receipt_claims` | Checks that *declared* immutable-storage object-version metadata refer to the right artifacts, SHA-256 digests, future retention times and compliance lock mode. It cannot verify those receipts with the storage provider or validate cryptographic signatures |

The complete release manifest is bound to the following controlled metadata:

- `manifest_version=thomaslab-release-manifest-v1`, `staging_version=thomaslab-ehr-staging-v1`, `omop_version=5.4`, `ohdsi_tag=v5.4.3`
- Source system and source release, source classification, and explicit S01 fingerprints for person, encounter and clinical-event tables
- Between 3 and 64 artifacts, with opaque IDs, stage, declared content SHA-256, byte length, schema fingerprint, transformation revision, and direct parent artifacts
- Exactly supported three-stage topology: source objects have no parent, staging depends only on source, and OMOP depends only on staging. Orphan sources/staging products, missing parents, duplicates and cross-stage links block

The release ID changes with source-release, structural fingerprint, artifact hash, mapping revision or lineage changes. It is a **content-addressed metadata identity**, not proof that declared hashes match any real source or that the archive is immutable.

## Synthetic usage example

```python
import hashlib
from pathlib import Path
from thomaslab.adaptive.release_manifest import (
    build_release_manifest,
    validate_release_manifest,
    verify_synthetic_archive_files,
)

sha = lambda raw: hashlib.sha256(raw).hexdigest()
source_bytes = b"SYNTHETIC SOURCE\n"
staging_bytes = b"SYNTHETIC STAGING\n"
omop_bytes = b"SYNTHETIC OMOP\n"
fingerprints = {"person": "1"*64, "encounter": "2"*64, "clinical_event": "3"*64}

stages = [
    ("source_a", "source", [], None, source_bytes),
    ("staging_a", "staging", ["source_a"], "map_v1", staging_bytes),
    ("omop_a", "omop", ["staging_a"], "map_v1", omop_bytes),
]
artifacts = [
    {
        "artifact_id": name, "stage": stage, "parents": parents,
        "sha256": sha(raw), "size_bytes": len(raw),
        "schema_fingerprint_sha256": fingerprints["person"],
        "mapping_revision": revision,
    }
    for name, stage, parents, revision, raw in stages
]
manifest = build_release_manifest(
    source_system="synthetic_hospital",
    source_release="v1",
    classification="SYNTHETIC",
    source_schema_fingerprints=fingerprints,
    artifacts=artifacts,
)
assert validate_release_manifest(manifest)["status"] == (
    "STRUCTURAL_DRY_RUN_PASS_RELEASE_BLOCKED"
)
assert manifest["authorized_for_export"] is False

# Optional ONLY in a precreated, 0700 private synthetic directory:
# Put each invented payload in root / "<artifact_id>.bin" and run:
# result = verify_synthetic_archive_files(manifest, root)
# assert result["authorized_for_export"] is False
```

No real hospital, MIMIC-IV, All of Us or restricted-source file is opened by the byte-hashing function; non-synthetic classifications are rejected there. All of Us generic manifest construction is expressly blocked pending its Workbench-specific governance. Restricted-source *metadata-only* dry runs can be described, but never infer DUA/IRB access or authorize file reads.

## WORM evidence is declarative, never self-authorizing

A receipt declaration needs a matching artifact ID and SHA-256, a restricted object version reference, a future retention timestamp, `COMPLIANCE` lock mode and an opaque evidence reference. Even if all receipt fields agree, the result is always:

```text
DECLARED_WORM_RECEIPTS_CONSISTENT_RELEASE_BLOCKED
storage_object_lock_independently_verified = False
receipt_signatures_verified = False
retention_policy_institutionally_approved = False
authorized_for_export = False
```

Actual institutional deployment requires approved storage tenancy and IAM roles, enforced object-lock/WORM storage and **provider-verified** retention, independent authorization, source-to-target artifact byte verification inside the governed enclave, tamper-evident/signature-backed evidence, backup and recovery, source/licensing/IRB/DUA retention policies, controlled egress and clinical/OMOP quality validation. This implementation has no release/publish endpoint.

## Testing and release decision

**45/45 S12 focused synthetic tests passed locally** (Python 3.13.5, pytest 9.0.2). Python 3.9–3.13 AST grammar parsing passed. The committed implementation and test Git blob SHAs match the exact locally executed files; no older Core packages are mocked because this module uses only Python's standard library.

Run the focused test in your approved checkout:

```bash
python -m pytest -q tests/test_adaptive_release_manifest.py
python scripts/ehr_platform_status.py
# Full current-commit Core Python 3.9/Slurm/quality remains a separate gate.
bash scripts/verify_hardening_candidate.sh
```

**Unverified:** exact-head complete Core QA/CI, actual Python 3.9 runtime, Herts HPC, signed release identities, object-store WORM integration, patient-source approval, independently verified hash receipts, immutable retention, disclosure review, actual dataset creation or clinical/OMOP quality acceptance.

**P0-05 remains OPEN.** S12 provides a tested foundation contract, not a finished immutable archive or production-grade dataset release service.

See [S10 canonical staging](canonical_dataset.md), [S11 OMOP target contract](omop54_contract.md), and [the staged EHR platform plan](../../guides/ehr-platform-build-plan.md).

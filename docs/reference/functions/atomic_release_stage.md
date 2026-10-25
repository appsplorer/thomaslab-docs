# S24 — Atomic synthetic release candidate staging

**Candidate only; P3-07 remains OPEN.** Private API: `thomaslab.adaptive.atomic_release_stage`. It does not publish hospital data, enforce WORM retention, verify cryptographic signatures or authorize patient-data exports.

## Implemented

`stage_synthetic_release(manifest, source_directory, output_root, *, policy)` validates the complete S12 release manifest and requires classification `SYNTHETIC`, a nonexporting Core ExecutionPolicy, approved source/output paths and private 0700 directory permissions. Source artifacts are existing `<artifact_id>.bin` files in the explicitly approved source directory. Never use patient records; a caller-supplied `SYNTHETIC` label is not an independent PHI/privacy guarantee.

It enforces strict finite limits (default 32 MiB per file and 128 MiB total), uses exclusive process-level lock creation, refuses symlinks, opens ordinary files without following links, streams copies in bounded 1 MiB chunks, checks SHA-256 and inode/size/mtime consistency, writes a bounded nonauthorizing `candidate_metadata.json`, fsyncs content and directory, then atomically renames a private temporary directory to `candidate_<release_id>`. Failed pre-rename attempts clean up temporary files; existing candidates cannot be overwritten by cooperating writers. The returned object reports counts and the relative candidate directory name, never source bytes.

**Limits:** A local atomic rename is not immutable storage, signed institutional evidence, backup, retention or release approval. Privileged administrators can still change the candidate, and unexpected termination may leave a stale lock or temporary directory requiring controlled administrator recovery. Filesystem and policy integrations must be security-reviewed before any regulated use.

`inspect_release_signoff_claims(manifest, claims)` requires exactly two separate opaque reviewer IDs asserting `DATA_STEWARD` and `PRIVACY_OFFICER` roles, release-ID match and UTC nonfuture review times. It validates claims' *format*, not the claimed identities or signatures. It **always** returns `independent_signatures_verified=False`, `institutional_review_approved=False`, `immutable_storage_verified=False`, `authorized_for_export=False`.

## Invented fixture example

~~~python
from thomaslab.adaptive.atomic_release_stage import stage_synthetic_release

candidate = stage_synthetic_release(
    synthetic_s12_manifest,
    synthetic_0700_source_directory,
    synthetic_0700_candidate_directory,
    policy=nonexporting_execution_policy,
)
assert candidate["authorized_for_export"] is False
assert candidate["storage_worm_verified"] is False
~~~

## Verification and remaining P3-07 requirements

Combined S24/S25 **45/45 focused synthetic tests passed locally** on Python 3.13.5, with Python 3.9–3.13 AST syntax checks. Exact new source/test Git blobs match the executed local files. S24/S25 production modules were exercised, but existing S12 validator and governance used compatible local substitutes; full original private Core, Python 3.9 runtime and approved HPC acceptance are not yet verified.

Institution-owned signer authentication, revocation, approved IRB/DUA source access, immutable/WORM archive, external signed receipt, independent disclosure review, encrypted retention and clinical release control remain missing. **P3-07 stays OPEN.**

~~~bash
python -m pytest -q tests/test_adaptive_atomic_incremental.py
bash scripts/verify_hardening_candidate.sh
~~~

Related: [S12 manifests](release_manifest.md), [S13 data-use policy](source_use_contract.md), [S25 incremental plans](incremental_rebuild.md), [EHR platform plan](../../guides/ehr-platform-build-plan.md).

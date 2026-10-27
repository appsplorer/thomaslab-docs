# S25 — Version-bound incremental rebuild planning and resumable checkpoints

**Status: local synthetic candidate; P3-08 remains OPEN.** Private Core module: `thomaslab.adaptive.incremental_rebuild`. This is a *metadata* planner and local progress journal, not real clinical ETL execution, source CDC/HL7/FHIR feed, distributed DAG scheduler or approved patient-record cache.

## Deterministic change and dependency planning

`plan_incremental_rebuild(previous, current)` validates two exact S12 SHA-256-bound release manifests. Both must be synthetic releases from the same source system and classification. The planner compares artifact IDs, declared content SHA-256 digests, byte sizes, mapping revisions, parent dependencies and source release/fingerprints. It identifies added, changed and removed artifacts and **invalidates all downstream descendants** across the source → staging → OMOP dependency chain.

Changes in source release or source schema fingerprint invalidate the complete current plan. Unchanged artifacts are labelled `unchanged_declared_only`, not independently byte-verified. Removals are surfaced explicitly; no script deletes source files or patient records.

The returned bounded, content-addressed plan includes ordered tasks, SHA-256 plan identity, artifact stage, declared content digest and affected upstream dependencies. This is not an instruction to execute unreviewed code and cannot make actual transformations run. The output always has `work_authorized=False` and `authorized_for_export=False`.

## Crash-resumable progress journal

`update_rebuild_checkpoint(plan, root, *, complete_artifact=None, expected_revision=None)` uses a preexisting, private owner-only (0700) metadata directory. It writes a small digest-sealed 0600 JSON checkpoint with exclusive lock creation, fsync and atomic replacement. It enforces original plan digest, monotonic revision, bounded task set, dependency-order completion, stale-revision rejection, no symlinks and idempotent replay of previously declared completions.

Important: **completion entries are caller-supplied declarations, not independently authenticated job completion or content verification.** A user able to edit the checkpoint directory can rewrite its records; a local SHA-256 seal is not a signature. A clean resume requires source/target content revalidation under external governed execution and actor permission checks. Stale locks after crashes require controlled inspection; no automated destructive lock cleanup.

~~~python
from thomaslab.adaptive.incremental_rebuild import (
    plan_incremental_rebuild,
    update_rebuild_checkpoint,
)

plan = plan_incremental_rebuild(previous_synthetic_s12_manifest,
                                updated_synthetic_s12_manifest)
assert plan["work_authorized"] is False

# Existing 0700 metadata-only directory, NEVER a hospital patient dataset root.
checkpoint = update_rebuild_checkpoint(plan, private_checkpoint_root)
assert checkpoint["resume_allowed_for_clinical_execution"] is False

# After *independent* testing, a synthetic orchestration harness may record
# a declaration; this does NOT attest that the ETL result matches the source.
# update_rebuild_checkpoint(
#    plan, private_checkpoint_root,
#    complete_artifact="synthetic_source_artifact",
#    expected_revision=checkpoint["revision"],
# )
~~~

## Verification and production blockers

**S24+S25 combined 45/45 synthetic tests passed locally** on Python 3.13.5; Python 3.9–3.13 syntax parsing passed. Tests cover exact S12 identity expectations, source-release/fingerprint drift, source/staging/OMOP downstream invalidation, empty-delta idempotence, checkpoint restart and revisions, completion-order rejection, stale locks, symlinks, tampered content and empty/change plans. The GitHub source/test file blobs match the locally executed versions. The tests use locally compatible S12/governance stand-ins and are not a full actual-Core integration or Python 3.9/HPC acceptance.

**P3-08 stays OPEN** pending institution-managed CDC/incremental source extraction, actual target row/build byte verification, robust multiworker recovery, independently witnessed checkpoints, stable patient identity/time rechecks, source access revocation, permissioned cache, performance at real dataset scale, source-system retention policy, and complete Core/HPC quality gates.

~~~bash
python -m pytest -q tests/test_adaptive_atomic_incremental.py
python scripts/ehr_platform_status.py
bash scripts/verify_hardening_candidate.sh
~~~

Related: [S12 manifest identities](release_manifest.md), [S18 ETL graph](etl_graph.md), [S24 atomic synthetic candidates](atomic_release_stage.md), [EHR platform plan](../../guides/ehr-platform-build-plan.md).

# Verified synthetic rebuild artifact before S25 checkpoint (P3-08)

**Status:** development candidate only. This is additional P3-08 software hardening; **P3-08 remains OPEN** for real-data CDC, independently verified output lineage, controlled resume, institutional storage, HPC and clinical acceptance.

Private API: `thomaslab.adaptive.rebuild_verification.record_verified_synthetic_rebuild_progress`.

### Purpose

Original S25 `update_rebuild_checkpoint` records a caller's *declaration* that a task was completed, without opening the result file. This opt-in path verifies actual synthetic output bytes **at the time of the check** against an S25 task's SHA-256 from an exact, validated rebuild plan, then invokes the normal optimistic-revision checkpoint API. It does not alter that legacy API.

The checker enforces:

- S25 exact plan and planned artifact ID; no arbitrary paths or source names;
- separate, existing, absolute, private 0700 artifact and checkpoint roots;
- owner-only private regular `<artifact_id>.bin` files, without symlinks;
- bounded streaming SHA-256 (maximum 128 MiB by default);
- inode, size, mtime and ctime stability during the read;
- expected digest and optimistic checkpoint revision before declaring task progress;
- explicit `authorized_for_export=False`, `artifact_storage_immutable_verified=False`, and `checkpoint_signed_or_independently_attested=False` in results.

Example (invented synthetic artifacts ONLY, inside an approved local environment):

~~~python
from thomaslab.adaptive.incremental_rebuild import (
    plan_incremental_rebuild, update_rebuild_checkpoint,
)
from thomaslab.adaptive.rebuild_verification import (
    record_verified_synthetic_rebuild_progress,
)

plan = plan_incremental_rebuild(previous_synthetic_manifest, current_synthetic_manifest)
progress = update_rebuild_checkpoint(plan, existing_private_checkpoint_root)
verified = record_verified_synthetic_rebuild_progress(
    plan,
    checkpoint_root=existing_private_checkpoint_root,
    artifact_root=existing_private_artifact_root,
    artifact_id="omop",
    expected_revision=progress["revision"],
)
assert not verified["authorized_for_export"]
~~~

All task output files are synthetic and must match the declared digest. A SHA-256 match does **not** establish that the bytes correspond to authorized clinical records, that source rights are valid, that a race cannot happen after verification, or that the filesystem is WORM. A compromised operator who can change plan, local files and checkpoint is not independently attested.

### Verification

- **16/16** isolated synthetic regression tests passed on Python 3.13.5 (bad digest, symlink, permissions, size cap, revision, unplanned IDs).
- **14/14** partial22 audit regressions passed in the same local run (**30/30 combined**).
- Python 3.9–3.13 AST grammar parse passed for new files.
- A no-surrogate original-Core integration test for S12 manifest → S25 incremental plan → verified file → checkpoint is committed but **not yet run**.
- Exact current-head full Core CI/HPC, production storage, independent audit and actual patient datasets **not accepted**.

~~~bash
python -m pytest -q tests/test_adaptive_rebuild_verification.py tests/test_ehr_partial_acceptance.py
python -m pytest -q tests/test_ehr_partial_core_integration.py
~~~

See [incremental rebuild metadata plans](incremental_rebuild.md) and [the 22-gate EHR acceptance backlog](../../guides/ehr-partial22-acceptance.md).

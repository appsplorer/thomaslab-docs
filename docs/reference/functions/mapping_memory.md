# S09 — Schema-fingerprint-bound, reviewer-approved mapping memory

**Software state:** local synthetic contract candidate, not independently accepted for hospital deployment or patient-level export. The private implementation is `thomaslab.adaptive.mapping_memory` in <Link title="Core PR #34" url="https://github.com/appsplorer/thomaslab-core/pull/34"/>. Never use an archived mapping as permission to handle protected data.

## Role in the Thomas Lab EHR pipeline

S09 builds on the **same** S01 structural metadata fingerprint, S07 ranked field proposals, S08 role-separated review queue and existing `AdapterRegistry` used by the notebook workbench. It introduces:

- `FingerprintMappingMemory.remember(...)`: persist a metadata-only, write-once mapping hint after a completed three-person S08 review **and** a separate approved registry revision with passing full-source-validation metadata
- `FingerprintMappingMemory.lookup(...)`: search a bounded, approved local memory folder and return a *review-only* hint only for an exact source/release/table/structural fingerprint/ruleset/domain/source-column match
- `evaluate_unseen_schema_holdouts(...)`: compare the system's exact-match versus abstention result against synthetic or independently annotated held-out case labels, reporting aggregate false reuse, correct abstention, missed reuse and true reuse

S09 does not replace or weaken the existing `MappingWorkbench`, `FullValidationReport`, `AdapterRegistry` or source access requirements. It does not run SQL, materialize OMOP, infer a patient crosswalk, validate clinical concepts, invoke an LLM or export clinical data.

## Exact approval contract

Before a mapping enters memory, S09 requires:

1. **S08:** a verified three-role journal with `TRIAGE_ACCEPT`, `CLINICAL_ACCEPT` and `STEWARD_CLEAR`, with different actors and a fourth independently verified data-steward memory custodian
2. **AdapterRegistry:** an existing adapter revision in `APPROVED` state, with named reviewer and timestamp, named mapping reviews, and complete, passing `FULL_SOURCE` validation evidence with a SHA-256 checksum and no skipped or blocking rows
3. **Cross-module equivalence:** identical source system, source release, source table, ordered source field list, S01 schema fingerprint, reviewed canonical target and source field
4. **Storage:** a precreated private `mapping_memory` folder immediately under the existing S08 approved review root, exclusive writes, 0600 records, no symbolic links and content-hash integrity checks

To support S09, new `AdapterRegistry.create_draft` inputs may carry `source_release`, `table_name` and `source_schema_fingerprint_sha256` **as a complete group**. Partial bindings are rejected; legacy adapter revisions remain readable but cannot seed an S09 exact-approval hint without all three. `MappingWorkbench.request_approval` now forwards these fields when present in its manifest. The existing independent approval workflow remains necessary.

**Important:** S08 hash chains and registry metadata hashes detect ordinary modification but are not externally signed, do not independently authenticate IAM/IRB/DUA, and cannot resist an authorized administrator's coordinated record replacement. The package does not independently attest a real hospital's adapter approval from synthetic tests.

## Exact-match lookup statuses

| Status | Meaning |
|---|---|
| `EXACT_MATCH_REVIEW_HINT_ONLY` | Previously approved revision metadata found for this *exact* schema/version/context; researcher must validate and reauthorize current data |
| `BLOCK_SCHEMA_OR_RELEASE_DRIFT` | Field exists, but source fingerprint or source release no longer matches |
| `ABSTAIN_SOURCE_FIELD_NOT_PRESENT` | Previously considered source field absent from current S01 report |
| `ABSTAIN_NO_EXACT_MEMORY` | No usable exact-source memory; suggest fresh S07/S08 review |
| Exception | Tampered records, conflicting versions, invalid fingerprint, unauthorized role or unbounded inventory fail closed |

Even on an exact match, the result always has `source_data_revalidated=False`, `external_entitlement_rechecked=False`, `clinical_mapping_reapproved=False`, `automatic_etl_allowed=False` and `authorized_for_export=False`. No returned mapping can be silently plugged into a clinical ETL.

## Usage sketch (invented synthetic data only)

```python
from pathlib import Path
from thomaslab.adaptive.mapping_memory import (
    FingerprintMappingMemory, evaluate_unseen_schema_holdouts,
)

# queue: the already authorized S08 MappingReviewQueue instance
# schema_report: the completed, fingerprint-valid S01 profile
# registry: the existing approved AdapterRegistry instance
# task_id: the S08 three-role accepted task ID, tied to the exact schema
# trusted_verify_role: institution-owned IAM callback; synthetic tests can
# use a fixed fake verifier, never appropriate for actual patient sources
memory = FingerprintMappingMemory(
    queue.root / "mapping_memory", queue=queue
)

memory_id = memory.remember(
    task_id, schema_report,
    registry=registry,
    approved_revision_id="synthetic_ehr@v1",
    actor="separate_memory_steward",
    role="data_steward",
    verify_role=trusted_verify_role,
)
hint = memory.lookup(
    schema_report, source_column="result_value", domain="measurement",
    actor="authorized_researcher", role="intern",
    verify_role=trusted_verify_role,
)
assert hint["automatic_etl_allowed"] is False
```

Create the memory directory explicitly with private institutional permissions *before* constructing the class. This is an API sketch—not a ready-to-run hospital integration. The exact adapter ID, source data, authorized users and evidence must already exist.

For synthetic holdouts, pass 1–64 distinct cases with `report`, `source_column`, `domain` and explicit boolean `should_reuse` annotations. The evaluator exposes only aggregate counts and a `BLOCK_FALSE_REUSE` safety status if any labeled example was wrongly reused. A four-case synthetic illustration yielded one correct exact reuse and three correct abstentions. **These hand-built labels are not clinical ground truth and do not establish generalization to MIMIC-IV, All of Us or unseen hospital EHR schemas.**

## Boundaries, evidence and next work

- Memory inventory is capped at 300 metadata records; write-once by content identity. Repeated attempts to store an identical revision reject overwrites; it is not a distributed, production-scale data catalog.
- Only source metadata and restricted reviewer/approval IDs are persisted. Source field labels may still be sensitive. No patient-level sample values, credentials or medical record contents are persisted by S09.
- This module reuses internal, digest-checking S08 and AdapterRegistry readers. Cross-package release compatibility and full actual Core regression/HPC tests remain **unverified**.
- Stored hints are not checked for current approval revocation or up-to-date hospital data-use entitlement at lookup time. Thus exact reuse is **never automatic**. Real deployment requires institution-controlled revocation/authorization and current source validation.
- The new registry provenance fields and mapping-workbench propagation have not undergone the complete original Core test suite in this session. Source data permission, Python 3.9 runtime, clinical mapping precision, blinded clinical gold-standard datasets and larger-scale HPC benchmark remain pending.

**Focused local verification:** 37/37 synthetic memory and holdout tests pass on Python 3.13.5 / pandas 2.2.3 / pytest 9.0.2, with actual S03/S07/S08 algorithm implementations and contract-compatible surrogates for the legacy Core aliases/S01 adapter registry. Python 3.9/3.11/3.13 grammar parsing passes. Exact new source and test Git blobs match the locally tested files.

```bash
python -m pytest -q tests/test_adaptive_mapping_memory.py
python scripts/ehr_platform_status.py
# In an approved exact-commit Core checkout, with configured report root:
bash scripts/verify_hardening_candidate.sh
```

**Release decision:** P1-08 has focused local evidence only. P1-03 authorized enterprise source integration, Python 3.9 HPC, full Core quality gates, governance/clinical acceptance and independent unseen-schema benchmarking remain blocking before production use.

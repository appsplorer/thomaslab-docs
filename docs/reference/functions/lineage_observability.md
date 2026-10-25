# S28/S29 — Synthetic record lineage and clinical quality observability

**Checkpoint: 25 October 2026. Status: candidate only; P4-03/P4-04 remain OPEN.** These APIs are private Core prototypes for **invented synthetic events only**. They do not permit real patient identifiers, protected hospital extracts, MIMIC-IV clinical rows, All of Us participant data or publication. No research dataset is produced. A caller-provided SYNTHETIC declaration is not independent proof that PHI is absent.

## S28: row-to-source/mapping/vocabulary lineage

Private module: `thomaslab.adaptive.record_lineage`.

- `initialize_synthetic_lineage(root, manifest, site_scope=..., hmac_key=..., key_id=...)` creates an exclusive 0600 SQLite journal inside a pre-existing 0700 non-symlinked directory, bound to a structurally validated S12 synthetic release manifest, the source system, site and an externally provided 32+-byte HMAC key. **Never hard-code secrets, put them into example notebooks, or confuse HMAC with patient de-identification.**
- `append_synthetic_lineage(root, manifest, edges, site_scope=..., hmac_key=..., key_id=...)` accepts strictly bounded SOURCE → STAGING and STAGING → OMOP row edges. Each edge binds a declared upstream/downstream artifact and row reference, the approved-plan mapping revision, an opaque review reference and an exact terminology SHA-256. The module stores HMAC references rather than source identifiers, uses SQL parameters, requires an incoming source edge before a staging row can lead to OMOP, rejects conflicting retries and rolls back a failed batch.
- `audit_synthetic_lineage(...)` returns aggregate-only edge/target counts and identifies structurally orphaned staging relationships, with an explicit hard cap on inspected edges.
- `trace_synthetic_target(..., omop_artifact=..., omop_row=...)` inspects a bounded two-edge synthetic ancestry for an OMOP target and returns counts and a nonauthoritative digest of provenance labels. No source ID, target ID or row HMAC is returned.

**Limitations:** S12 artifact SHA-256 values remain declarations unless separately byte-verified. The source identity, review actor and terminology entitlement are not independently authenticated; SQLite journalling is not WORM evidence, an external HSM, a trusted signature or an institutional audit service. Metadata-level row lineage does not prove a clinically correct mapping or an approved multi-site join.

## S29: site/month clinical data-quality observability

Private module: `thomaslab.adaptive.clinical_observability`.

- `SyntheticQualityMonitor(manifest, site_scope=..., period="2026-09", code_catalog=..., units_by_code=...)` requires a complete validated synthetic release identity and exact versioned code-system / code-qualified unit allowlists. It does not infer diagnosis codes, UCUM equivalences, assay compatibility, clinical norms or treatment state.
- `ingest_batch(records)` atomically validates a bounded batch of **metadata-only invented** event records with exact keys: `site_scope`, `period`, `event_type`, `code_system`, `code`, `unit` and `value_present`. No patient identifiers, notes or numeric lab values can enter this API. Counters cover missing/unmapped codes, measurement-unit conflicts, missing results and event domain volumes. Code strings retain leading zeros.
- `snapshot()` builds a digest-sealed aggregate review report, suppressing **all** domain breakouts when a small domain group could be inferred. These guards are not source-specific disclosure clearance.
- `compare_synthetic_quality_windows(old, new)` detects month gaps, raised quality-error rates, large event-volume falls, source-release changes and incompatible site/vocabulary contexts. It is a **preflight**, not a causal trend test, false-alarm calibration or automated clinical alert.
- `persist_synthetic_quality_snapshot(root, snapshot)` and `load_synthetic_quality_snapshot(root, release_id=..., site_scope=..., period=...)` use private owner-only metadata storage, refuse overwrites and validate the source context and snapshot digest. Local SHA-256 integrity is **not a signature**; continuous scheduling and independent storage attestations are outside this prototype.

## Focused tests and remaining acceptance

- S28/S29: **46/46 synthetic regression cases passed locally** on Python 3.13.5, with Python 3.9–3.13 AST syntax parsing. Scope: path/symlink and classification denials, source/stage/OMOP ancestry, SQLite rollback, conflicting replay, wrong HMAC/site, code/unit/date checks, atomic invalid batches, small-group suppression, drift and tampered snapshots.
- Tests used a **contract-compatible local stand-in** for the existing S12 release-manifest implementation. The real current Core import/pytest suite, repository-wide Ruff/mypy/build QA, Python 3.9 runtime and HPC were **not run** for the S28/S29 additions at this checkpoint.
- Exact tested source/test Git blobs were verified on the Core candidate branch. The two Core milestone tasks remain **OPEN**, rather than counting these synthetic prototypes as full record-to-source institutional lineage or operational monitoring.

To run focused checks after an approved pull:

~~~bash
python -m pytest -q tests/test_adaptive_record_lineage.py tests/test_adaptive_clinical_observability.py
python scripts/ehr_platform_status.py
~~~

Further requirements: licensed vocabulary and mapping-review authority, approved site identity and clinical event-time semantics, patient-level linkage within a certified enclave, trusted key management, signed independent audit/WORM retention, time-series observability jobs, verified real-data source adapters, 15–20 unseen gold datasets, validated outcomes and specialist review, plus full exact-SHA Core/HPC acceptance.

**No code in this checkpoint may approve or export patient-level data.**

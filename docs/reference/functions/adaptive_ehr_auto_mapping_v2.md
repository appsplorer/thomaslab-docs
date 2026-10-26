# Adaptive EHR Mapping and ETL Workbench — S45 verified synthetic integration

**Status: engineering candidate. Not a production hospital ETL system. No real patient data, validated clinical code mapping, external authorization, or approved research release.**

The workbench must reuse Core's existing modules, not introduce a parallel clinical ETL system:

- `schema_discovery`, `clinical_domain_inference`, `field_suggestions`: S01 metadata and unreviewed canonical role ranking; never treat structural/name similarity as a clinical concept approval.
- `terminology_registry`, `athena_import`, `thomaslab.terminology`, `terminology_adapter`: pinned licensed terminology release and reviewer-only code candidates. **Vocabulary pack bytes, mapping suitability and source entitlements are not included or independently verified.**
- `mapping_memory`, `adapter_registry`, `review_queue`, `review_prioritization`: governed mapping history and intern → clinician → steward review, with independent institutional reviewer authentication still required.
- `etl_graph` (S18), `etl_compiler` (S19): exact graph/IR, approved-style adapter evidence, multiple source/target dependencies. The compiler's output remains non-executable by design.

## S45 engineering additions

### 1. `synthetic_etl_materializer.execute_synthetic_etl`

- Accepts S18 and S19 envelopes with exact SHA-256 digests and review-only flags; **rejects** code/SQL snippets or altered field/join instructions.
- Supports deterministic `COPY_COLUMNS_ONLY` transformations on **invented records**, one source → stage, explicit two-source site-scoped **inner joins**, source fan-out into multiple target tables, and multiple staging sources contributing to the same target through union.
- Requires all selected source fields and an explicit `site_id` matching the graph's site scope. Multi-source joins require explicit reviewed, projected `site_id` **plus one other identity key**, exact key-set equality, unique non-null join keys, equal membership and nonconflicting overlapping fields. Any incomplete/duplicated join blocks. There is **no silent row dropping**.
- Writes new tables to an owner-only SQLite file under an existing absolute private 0700 folder. No overwrite, no arbitrary SQL execution, and the response contains only aggregate source/stage/target counts and a nonrelease digest.
- Does **not** produce a complete clinically valid OMOP 5.4 CDM database: required fields/types, concept IDs, real identity resolution, time precision, joins, data meaning, PK/FK and overall conformance still need approved real execution. It also cannot prove that caller-supplied objects contain no PHI. Never supply actual patient rows.

### 2. `mapping_drift.compare_mapping_drift`

- Validates exact S01 schema fingerprint and explicit declared context for **every** column (domain, code system, vocabulary release, unit, specimen, route, timing semantics and precision, row grain, site).
- Reports new/removed fields, physical dtype shifts, declared semantic shifts, changed adapter SHA or release and which previously reviewed fields are affected.
- Keeps mapping reuse blocked until the original adapter registry and institutional data steward independently recheck permissions. It does not automatically certify clinical semantics.

### 3. `mapping_handoff.build_review_handoff`

- Validates S18/S19 graph and IR hashes, S44 risk triage hash, S45 drift digest, bound source schema and dictionary versions, reviewer queue reference and fail-closed nonapproval flags.
- Returns a metadata-only immutable-by-hash handoff with intern/expert review workload counts; **never executes ETL or grants release permissions**.

## Candidate demonstration workflow

1. Use the existing governed source readers for **authorized** metadata profiling (or separate invented fixtures for synthetic tests). Produce S01 schema metadata.
2. Obtain a version-pinned private terminology source, or create invented test concepts. Generate candidate mappings and prioritise ambiguous codes (S42–S44).
3. Compare release, code-system, unit and timing context against previously reviewed S01 metadata; do not reuse if drifted.
4. Obtain actual institution-authenticated intern/expert/steward review and full-source adapter validation, then independently construct S18 graph and S19 IR. **S45 does not replace these sign-offs**.
5. On invented data only, exercise `execute_synthetic_etl` to inspect restricted staging tables and count reconciliation. Review the resulting tables against OHDSI OMOP 5.4; never label the demo a release.
6. Run expert validation, approved ETL, source/target reconciliation, provenance, full DQD checks, independent privacy approval, 15–20 held-out data tests and HPC runtime/performance gates before considering clinical use.

### Focused local test evidence

```bash
python -m pytest -q tests/test_synthetic_etl_materializer.py tests/test_mapping_drift.py tests/test_mapping_handoff.py
```

The focused S45 suite ran **51/51 PASS on local Python 3.13** with Python 3.9–3.13 AST syntax checks. These are isolated contract tests. Full original-Core imports, the old regression suite, Python 3.9 **runtime**, Core CI, HPC, real hospitals and publication-level scientific review remain **NOT ACCEPTED**.

### Machine-readable acceptance

`configs/ehr_auto_mapping_acceptance.json` lists 13 engineering capabilities with exact code paths, implementation state and outstanding blockers. The JSON is an **inventory**, not a credential, a real clinical source, a clinician signature or an approval certificate. Never promote `production_accepted` or `authorized_for_patient_data` without independently verified evidence and full technical validation.

### Official reference

- [OHDSI WhiteRabbit/Rabbit-In-a-Hat](https://www.ohdsi.org/analytic-tools/whiterabbit-for-etl-design/) — ETL documentation/design is separate from executable ETL.
- [OMOP CDM 5.4](https://ohdsi.github.io/CommonDataModel/cdm54.html) — detailed field-level constraints, date/time precision and clinically correct concept mappings.

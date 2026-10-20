# Reproducible study specifications and validated research bundles

Version 0.30 is the final pre-v1 integration and production-hardening release. It connects dataset onboarding, contract validation, reproducibility metadata, deterministic seeds, result tables, and export verification into a single auditable workflow.

## Unified study specifications

A study specification records the stable research intent independently of one analysis script. The required top-level sections are:

- study_id, title and version;
- design;
- data.datasets;
- analysis.primary; and
- reproducibility.seed.

validate_study_spec() checks structure without inventing clinical semantics. study_fingerprint() hashes the canonicalized specification, and freeze_study_spec() writes a reviewable YAML copy with its fingerprint.

derive_seed() creates deterministic child seeds for named operations such as folds, bootstrap replicates, or model families while retaining one declared study seed.

## Input and environment provenance

reproducibility.py provides:

- deterministic mappings/file/dataframe fingerprints;
- Python/NumPy/PyTorch seed setup;
- selected package/runtime capture without collecting environment variables or secrets;
- stable run fingerprints;
- JSON run-manifest export;
- input-fingerprint verification; and
- multi-table contract auditing.

Dataframe fingerprints include schema, row order, values, and index by default. Reordering rows is therefore treated as a different input state.

set_deterministic_seed() seeds Python and NumPy and can seed PyTorch when available. Setting PYTHONHASHSEED inside an already-running interpreter cannot retroactively change that interpreter's hash randomization, so the seed report states that limitation explicitly.

## Standardized research bundles

export_research_bundle() writes an atomic directory containing:

- tables/*.csv;
- metadata/study_spec.yaml;
- metadata/run_manifest.json;
- metadata/bundle_metadata.json;
- bundle_manifest.json; and
- checksums.sha256.

Every declared payload receives a SHA-256 checksum. verify_research_bundle() detects missing or modified files and can optionally fail on unexpected files.

The bundle metadata explicitly states that the export is for research use and does not provide a de-identification guarantee. PHI governance remains the responsibility of the approved research environment and study protocol.

## Integrated workflow

run_integrated_research_workflow() provides the v0.30 end-to-end path:

1. validate the study specification;
2. establish the declared deterministic seed;
3. apply a caller-supplied schema adapter when provided;
4. validate the source/standardized table contract;
5. validate configured result-table contracts;
6. profile the analysis dataset;
7. fingerprint the input and build a run manifest;
8. export the standardized bundle; and
9. verify all exported checksums before returning success.

The workflow never auto-approves an inferred schema mapping. If no schema is supplied, source columns are preserved. Domain inference may help choose a structural contract, but it does not establish clinical meaning.

## Release-quality safeguards

Version 0.30 also adds a structured deprecation registry and lightweight release checks for:

- package/README version consistency;
- public module export integrity;
- YAML/JSON asset parsing;
- numbered notebook continuity; and
- deprecation-registry validity.

CI executes these checks, compiles source/tests, validates notebook JSON, executes smoke notebooks, and runs the complete test suite.

## Recommended pre-v1 workflow

1. Freeze the study specification before primary analysis.
2. Review all source-to-canonical mappings manually where clinical meaning is uncertain.
3. Validate contracts before modeling.
4. Use one declared study seed and derive named child seeds.
5. Record the exact Git commit when running a manuscript analysis.
6. Fingerprint every analysis input.
7. Export final tables through the research-bundle layer.
8. Verify checksums before manuscript handoff or archival.
9. Treat reproducibility metadata as provenance, not proof of scientific validity.
10. Keep all clinical interpretation, causal-identification assumptions, privacy review, and external validation under explicit study governance.

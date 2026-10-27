# S36 — Source-bound synthetic study-mart plan, timeline and methods report (P5-03)

**Status: local synthetic engineering candidate only. P5-03 remains OPEN.** Private implementation: `thomaslab.adaptive.synthetic_study_mart`.

- `plan_synthetic_study_mart(manifest, candidate, ...)` pins one exact S12 source release, site, OMOP-stage artifact digest, immutable S35 phenotype SHA-256, prespecified time-zero/observation windows, an explicit UTC clock and bounded synthetic event count. It rejects stale site/release definitions, non-OMOP targets, unapproved source classifications and forged approvals.
- `summarize_synthetic_study_timeline(plan, rows)` accepts at most 5,000 invented, ephemeral typed event records, requires UTC `Z` timestamps and one consistent index time per synthetic participant, and flags post-index baseline labs, delayed results, conflicting availability, nonpostindex outcomes/treatments, bad censor dates and out-of-window events. No row or person identifiers are returned. Fewer than 11 participants suppresses all aggregate counts.
- `validate_study_timeline(summary, plan)` validates structure, digest, population/count bounds and nonapproval flags.
- `build_synthetic_methods_report(plan, summary)` creates a deterministic, digest-bound **methods review checklist** referencing source, phenotype, artifact and timeline provenance. It does **not** materialize an OMOP table or validate treatment effects, cohort ascertainment, censoring independence, endpoint validity, clinical safety, publication eligibility or study results.

Clinical data mart materialization, secure storage, full longitudinal target construction, independent phenotype review, real data harmonization, quality/lineage checks, source authorization, and reproducible statistical execution all remain OPEN.

**Evidence:** S34–S36 combined locally isolated synthetic tests **70/70 PASS**, Python 3.9–3.13 AST PASS; S12 surrogate used. Full private Core test suite, CI, Python 3.9 runtime, HPC and real-source scientific validation **NOT RUN / NOT PASSED**.

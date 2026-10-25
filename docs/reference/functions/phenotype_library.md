# S35 — Immutable synthetic phenotype candidate library (P5-02)

**Status: local synthetic engineering candidate only. P5-02 remains OPEN.** Private implementation: `thomaslab.adaptive.phenotype_library`.

- `build_phenotype_candidate(...)` builds an exact, content-addressed versioned procedure, diagnosis, medication, measurement or observation definition using explicit code system + release, lossless include/exclude codes, site/source/release identity, time-zero event, lookback/follow-up periods and `UNKNOWN_NOT_NEGATIVE` missingness policy.
- `validate_phenotype_candidate(candidate)` round-trips the immutable specification and rejects altered code lists, version mismatch, unknown fields, unapproved missingness interpretations and forged expert-approval flags.
- `inspect_phenotype_review_claims(candidate, claims)` checks the format of **two distinct stated** clinical expert and data-steward roles. **The claim is not proof** of those identities, expert approval or hospital rights.
- `register_synthetic_phenotype(root, candidate)` and `load_synthetic_phenotype(root, sha)` use a preexisting private 0700 directory, O_EXCL 0600 files, SHA verification, size limits and refusal to overwrite, follow symlinks or accept changed content. The registry is **not** institutional WORM storage or a signed approvals service.

This module stores invented/review-only *definitions*, not clinical data or validated phenotype labels. True adoption requires licensed vocabularies, medical expert adjudication, authorized source compatibility and real evaluation of phenotype precision/recall.

**Evidence:** joint S34–S36 isolated synthetic tests **70/70 PASS** Python 3.13.5; Python 3.9–3.13 AST PASS. S12 surrogate used for cross-module tests. Full existing Core, approved Python 3.9 runtime, HPC, certified expert review and independent study validity remain **NOT VERIFIED**.

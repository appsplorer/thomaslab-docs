# 22 partially implemented EHR requirements — exact acceptance and remediation

**Status: WORK IN PROGRESS.** This page describes the 22 requirements with pre-existing local candidate implementations. It does not claim that any requirement has passed production, real-source, Python 3.9 runtime, HPC or clinical acceptance. No patient records are used.

## Technical checkpoint

The private Core candidate adds two complementary checks:

1. scripts/ehr_partial_acceptance.py — a deterministic 22-requirement audit against the exact 46-task ledger. Maps the partial requirements to **20 unique focused test files** and records their outstanding independent acceptance conditions. The default is an inventory check; it does not run tests or authorize a release.
2. tests/test_ehr_partial_core_integration.py — imports **21 actual Core modules** from the editable checkout, without surrogate modules, and checks that a synthetic S12 manifest works with S25 incremental planning, S28 lineage and S29 observability. This must be executed in the full repository environment.

The first utility also has 14 synthetic local regression cases in tests/test_ehr_partial_acceptance.py: **14/14 PASS on Python 3.13.5** with Python 3.9–3.13 AST parsing. The real-Core integration suite is committed but **has not passed execution in the complete Core environment**. The GitHub-hosted Core workflows currently fail and returned no usable execution-step logs during the audit.

### 22 existing partial requirements

| Group | IDs | Outstanding technical or external evidence |
| --- | --- | --- |
| Source governance and identifiers | P0-01, P0-02, P0-05, P0-06 | Institutional source authorization, KMS/HSM, immutable archival evidence, IAM and disclosure controls |
| Terminology source registry | P2-01, P2-02 | Licensed source bytes, archive integrity, live entitlements, verified Athena import and expert review |
| OMOP ETL and reproducible releases | P3-03, P3-04, P3-06, P3-07, P3-08 | Reviewed identity/temporal joins, full OMOP conformance, row reconciliation, signed release, real CDC/resume |
| Scalability and source lineage | P4-01, P4-02, P4-03, P4-04 | Real Parquet/DuckDB run, 1m/10m/100m memory benchmarks, governed lineage and live quality feeds |
| Scientific and federated validity | P4-05, P4-06, P4-07, P4-08 | Clinical time-zero/censoring adjudication, held-out hospitals, actual CPU/GPU/Python 3.9 HPC and site permissions |
| Researcher workflow | P5-01, P5-02, P5-03 | Real-role metadata permissions, signed clinical phenotype review and validated materialized longitudinal study marts |

**These 22 are not an exhaustive list of all remaining requirements.** The engineering ledger also has 12 requirements with no partial implementation evidence. As of this checkpoint the ledger contains 46 requirements, 12 locally evidenced and 34 formally open. No milestone is independently approved for real patient-data production.

## Run the inventory now, without HPC

~~~bash
python scripts/ehr_partial_acceptance.py
python -m pytest -q tests/test_ehr_partial_acceptance.py
~~~

To test the original-Core imports without submitting HPC work:

~~~bash
python -m pytest -q tests/test_ehr_partial_core_integration.py
~~~

For a *complete focused retest* of the 20 mapped regression files, using an exact clean checkout and approved local Python installation (this may take substantially longer):

~~~bash
export THOMASLAB_EXPECTED_SHA="$(git rev-parse HEAD)"
python scripts/ehr_partial_acceptance.py --run-local --expected-sha "$THOMASLAB_EXPECTED_SHA"
~~~

The latter executes fixed pytest commands but **does not** run the full Core quality suite, check GPU or HPC availability, validate restricted source access, authenticate clinician signatures or authorize any release. A reported PASS only establishes successful local regression execution on that checkout. Report fields deliberately retain all clinical and institutional gates as unmet even if tests pass.

## Do not misclassify milestones

- **Locally implemented:** independently executable source with successful focused tests (if actually run at the specified commit).
- **Technically integrated:** complete exact-head source/pytest/coverage/static/notebook/package checks and relevant CPU/GPU HPC acceptance pass.
- **Scientifically and institutionally accepted:** documented approvals, site contracts, licensed terminology, expert gold-standard mapping, real datasets, independent privacy/security review and reproducible clinical validity have been independently verified.

An approved institutional operator, steward and clinical expert must provide their own evidence. Local JSON, synthetic pass counts, a Git SHA, unsigned acknowledgements or CI labels cannot replace those authorities. All code must remain synthetic-only or otherwise governed until the proper rights and controls are in place.

**Development order:** resolve these 22 partial acceptance gaps before treating P5-04–P5-08 as finished. Actual human usability trials, clinician-reviewed data and signed hospital approvals cannot be manufactured from synthetic fixtures.

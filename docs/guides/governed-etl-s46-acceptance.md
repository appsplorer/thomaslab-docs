# S46 — Governed EHR staging and original-Core contract acceptance

**Status: candidate, NOT real hospital/clinical approval.** No hospital records have been received, processed or validated. No claim of fully passing GitHub CI or actual Python 3.9/HPC execution.

## Exact source contract

The existing S18 reviewed ETL graph and S19 allowlisted COPY-only IR are reused. S45 processes invented rows into private candidate SQLite and does **not** authorize real hospital data. S46 adds a *separate* `governed_etl_staging` executor for the deliberately restricted case of **one institutional SQLite source → one canonical staging node → up to four OMOP-shaped candidate tables**. It:

- rereads the existing Core AdapterRegistry through `mapping_memory._approval` (full-source validation, current approval and schema fingerprint), compares exact S18/S19 hashes and field mappings, checks the pinned OMOP 5.4 target-field catalogue;
- requires private input/output roots, a nonexporting institutional/HPC `ExecutionPolicy`, an external institution-operated authorization decision that is rechecked before committing, an approval expiry and SHA-256 of the exact source bytes;
- reads a physical, previously approved SQLite table in read-only mode; demands exact physical columns matching the approved revision, preserves lexical identifier strings, rejects BLOB/nonfinite values, nonreviewed timestamps and all cross-site rows;
- executes only safe, bounded parameterized COPY-column insertion, with a 5,000-row maximum cursor chunk and a 1,000,000-row hard limit; creates private 0600 staged SQLite with exclusive no-overwrite installation and metadata-only counts/hashes;
- rejects joins, free-form transformations, arbitrary SQL, direct provider APIs, generic All of Us exports, unsupported sources and automatic concept assignment. Any such case enters a clinical/ETL review queue and needs a separately built and accepted adapter.

The returned record explicitly states **`institutional_authority_independently_verified_by_library=false`**, **`clinical_mapping_approved=false`**, **`omop_54_conformance_passed=false`**, **`authorized_for_export=false`**. An external verifier *callback* is a technical integration point, not independently issued authorization; a test lambda never proves real hospital access.

## Unfamiliar hospital synthetic validation

`synthetic_hospital_variability` builds **five independently invented source-shaped families × sixteen adverse schema or semantics variants** (80 scenarios): hospital EHR, MIMIC-IV `hosp`, MIMIC-IV `icu`, All of Us OMOP-shaped and FHIR Observation-shaped. Each generates distinct invented codes and IDs and a private SQLite source, metadata SHA-256 and review flag. None has real patient or restricted vocabulary values. Variations include date-only temporal data, ambiguous `MS`, changed specimen/assay, unknown code, missing UCUM unit, medication order vs administration, encounter grain, cross-site key reuse and duplicate identifiers. Examples are not guaranteed valid OMOP datasets; their purpose is to force uncertainty into review.

Official structural documentation and caveats:

- [MIMIC-IV v3.1](https://physionet.org/content/mimiciv/3.1/) describes hospital and ICU `subject_id`/`hadm_id`/`stay_id` joins, date shifting per patient and controlled credentialed access. Do not assume dates are comparable across distinct patients.
- [All of Us](https://support.researchallofus.org/hc/en-us) requires study work in its approved Workbench; this tool only mimics generic OMOP field shapes and never copies participant-level data out of the Workbench.
- [FHIR R4 Observation](https://hl7.org/fhir/R4/observation-definitions.html) distinguishes `effective[x]` event timing from `issued` result availability and `specimen`/`subject` context. The generator deliberately does not infer clinical equivalence from field names.
- [OMOP CDM 5.4](https://ohdsi.github.io/CommonDataModel/cdm54.html) requires independently reviewed `measurement_concept_id` and appropriate `measurement_date`, source-value preservation and type/provenance concepts. S46 COPY-only staging does **not** assert these obligations are met.

## CI blocker and exact-head acceptance

Current Core GitHub Actions (at prior S45 head) show all major workflows failing approximately nine seconds after run start; the GitHub jobs API yielded `steps=[]` and fetching logs returned a BlobNotFound error. Therefore **code/test failure has not been demonstrated by these hosted runs**, and **runner/account/workflow provisioning must be investigated by the GitHub account administrator**. `scripts/ci_runner_diagnostics.py` parses supplied metadata and never fabricates a failing source line. The previously failing Python39/quality workflow suites must be rerun successfully and their actual logs read before any CI-resolution claim.

On a clean, full private Core checkout, run **without surrogate dependencies**:

```bash
python -m pytest -q tests/test_s18_s19_s45_s46_real_core.py
python -m pytest -q tests/test_governed_etl_staging.py tests/test_synthetic_hospital_variability.py tests/test_ci_runner_diagnostics.py
python scripts/local_quality_gate.py
```

Then separately run the existing complete Core pytest/build/quality suite and approved HPC Python 3.9 CPU benchmark at the **same SHA**. This does not authorize PHI; actual hospital extract onboarding additionally requires institution-supplied IAM, DUA/IRB approval, secure key storage, independent expert field/concept review, leakage/coverage validation, signed data releases and privacy review.

**Scope limit:** This is not a generic production ETL engine for unknown hospital CSV, Parquet, SQL, FHIR or HL7 sources; those require their connector-specific approved readers, approved clinical semantics and the full multi-source reconciliation engine. Unknown formats/fields must be quarantined for review, not guessed.

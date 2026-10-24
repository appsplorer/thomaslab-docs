# Cross-dataset clinical quality contracts and conservative baselines

**Status:** Experimental Python research utilities in private
`thomaslab-core` PR #34. This page is shared byte-identically with the
public handbook; no actual All of Us, MIMIC-IV or hospital records have
been supplied for independent verification.

## Scope and authoritative source context

The official [All of Us CDR v9 dictionary](https://support.researchallofus.org/hc/en-us/articles/360033200232-Data-Dictionaries)
identifies standard OMOP tables and non-OMOP surveys, wearables and genomic
data. Individual-level records are restricted to the Researcher Workbench;
**do not transfer them to UGA HPC**.
The [MIMIC-IV v3.1 PhysioNet reference](https://physionet.org/content/mimiciv/3.1/)
separates hospital from ICU event tables, describes release-specific lab and
patient-link corrections, and places independent restrictions on credentialed
usage. Hospital EHR sources require a local data steward's dictionary,
authorized compute and reviewed code/units/time mapping.

Every clinical dataset needs some common validation even after
source-specific adapters. This module handles structural, prespecified
contracts only. It does not establish source permissions, correct coding
crosswalks, phenotype truth, causal identification, model transportability,
medication adherence or disclosure permission.

## `thomaslab.healthcare_quality`

| Function | Contract / safeguards | What it cannot prove |
|---|---|---|
| `code_set_manifest` | Verify explicit ICD-9/ICD-10/SNOMED/LOINC/RxNorm/NDC/CPT/HCPCS/OMOP/local system, version, study protocol, effective date and unique text codes; return stable SHA-256 | That an unverified code set is clinically accurate or approved |
| `clinical_code_coverage` | Count missing/out-of-prespecified codes in authorized memory without printing actual unfamiliar codes | Terminology equivalence, mapping correctness or phenotype PPV |
| `medication_state_summary` | Keep `ORDER`, `DISPENSE`, `ADMINISTRATION` separate, reject unknown statuses and ambiguous timestamps | Medication adherence, exposure episode or treatment effect |
| `site_temporal_holdout_preflight` | Check patient non-overlap, wholly external site and strictly later held-out dates | Generalizability/calibration/fairness; a random split is **not** an external test |
| `site_missingness_preflight` | Block any site smaller than minimum 11 before computing aggregate missingness range | Full disclosure protection, complementary suppression or publication authorization |

All outputs and metrics are **research-only and restricted pending source
disclosure review**, including count-based reports. Even a site with 11
records does not automatically satisfy its DUA, HIPAA determination or
statistical disclosure-control protocol.

## Synthetic example: register coding provenance

~~~python
from datetime import date
import pandas as pd
from thomaslab.healthcare_quality import (
    code_set_manifest, clinical_code_coverage,
    site_temporal_holdout_preflight,
)

codes = code_set_manifest(
    system="ICD-10-CM",
    version="FY2026",
    protocol_id="SYNTHETIC-EXAMPLE",
    effective_date=date(2026, 10, 1),
    codes=("I21.9", "I25.10"),
)
assert codes["named_clinical_reviewer_verified"] is False

observed = pd.DataFrame({"diagnosis": ["I21.9", "LOCAL-UNKNOWN", None]})
report = clinical_code_coverage(
    observed, code_column="diagnosis",
    allowed_codes=frozenset(("I21.9", "I25.10")),
)
assert report["source_code_values_returned"] is False

train = pd.DataFrame({
    "patient": ["P1", "P2"], "site": ["A", "A"],
    "date": ["2025-01-01", "2025-02-01"],
})
test = pd.DataFrame({
    "patient": ["P3"], "site": ["B"], "date": ["2026-01-01"],
})
split = site_temporal_holdout_preflight(
    train, test, patient_col="patient", site_col="site", time_col="date"
)
assert split["status"] == "PASS_STRUCTURAL_ONLY"
assert split["externally_validated"] is False
~~~

These are invented records only. No live Workbench or PhysioNet data,
network access, credentials or hospital PHI are required.

## How common methods interact with source-specific methods

1. **All of Us:** Workbench access + v9 dictionary verified first; then
   OMOP concept/version checks, PPI code handling, wearable/omics provenance,
   prespecified coding fingerprint, population eligibility and approved
   per-patient model design inside Workbench.
2. **MIMIC-IV:** PhysioNet authorization and permissible local storage first;
   validate 3.1 `patients`/`admissions`/`icustays`, `d_labitems`
   and eMAR; never equate prescriptions with administrations; apply
   patient-specific shifted-time rules and ICU code/units checks.
3. **Hospital EHR:** Hospital-specific code system/version, MRN and
   encounter mapping, timezone, unit dictionary and source access must
   precede any patient linkage, shared holdout preflight or lab QA.
   Unrecognized local codes require signed mapping review.

## Synthetic acceptance commands

~~~bash
python -m pytest -q tests/test_healthcare_quality.py \
  tests/test_healthcare_omop.py tests/test_healthcare_mimic.py \
  tests/test_healthcare_hospital.py tests/test_healthcare_aou_domains.py
python scripts/synthetic_three_source_smoke.py --synthetic-only
~~~

Add the new suite to `scripts/verify_hardening_candidate.sh` before
requesting exact-commit acceptance on approved Slurm CPU compute.
The 21 October 2026 Herts HPC PASS applies to a **different Git SHA**;
this candidate's full suite remains unverified until new results are
produced and independently reviewed.

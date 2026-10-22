# Source-specific healthcare dataset onboarding: All of Us, MIMIC-IV and hospitals

**Status (22 October 2026): CODE CANDIDATE / SYNTHETIC TESTS ONLY.**
The private Core implementation is `thomaslab.healthcare_sources`. It adds
**structural** in-memory checks for three source families. It has **not** been
tested against actual All of Us, PhysioNet, or university hospital EHR records.
It does not access cloud accounts, call APIs, download patient data, infer
clinical semantics, certify HIPAA compliance, or authorize exports.

## Choose the permitted execution environment first

| Dataset | Native structure | Authorized execution | Never assume |
|---|---|---|---|
| **All of Us CDR v9** Registered/Controlled | OMOP person, visit_occurrence, condition_occurrence, drug_exposure, measurement; program-specific tables | Individual-level analyses stay **inside the All of Us Researcher Workbench** and its terms | Registered/Controlled records can be copied to UGA HPC, Kaggle or GitHub |
| **MIMIC-IV v3.1** | PhysioNet `hosp` and `icu` tables; `subject_id`/`hadm_id`/`stay_id` | PhysioNet-credentialed users, required training and DUA; UGA HPC only where the license and institution explicitly permit | Public GitHub access implies dataset access, or shifted dates are real calendar dates |
| **Hospital EHR** | Institution-specific encounters, observations, medication orders/administrations and clinical notes | UGA/hospital-approved enclave/HPC after PI, IRB/HRPP, DUA, IT, security and retention review | Any fixed schema, coding, dates, identifiers, field names or patient linkage |

**All of Us public aggregate exception:** Public Tier Data Browser summaries are distinct from Registered/Controlled participant-level records. The central governance policy permits an explicitly declared `PUBLIC_AGGREGATE` source in an approved local environment, still subject to small-cell and release terms. Kaggle notebook execution remains synthetic-only. The new individual-level source adapter intentionally does not accept public summaries as OMOP patient tables.

**All of Us:** The NIH program's [data-access tiers](https://researchallofus.org/data-tools/data-access/),
[Workbench](https://www.researchallofus.org/data-tools/workbench/), and
[current CDR data dictionaries](https://support.researchallofus.org/hc/en-us/articles/360033200232-Data-Dictionaries)
govern access. Check the exact Workbench CDR release; this candidate explicitly
recognizes only `registered_v9` / `controlled_v9` schema-review labels.
Genomic, survey and wearable data require domain-specific extensions and
authorization. Do not export participant-level results or attempt copying
controlled data into a UGA Slurm allocation. Workbench release/disclosure rules
are independent of local Python checks.

**MIMIC:** Use the official [PhysioNet MIMIC-IV v3.1 release](https://physionet.org/content/mimiciv/3.1/)
and [module documentation](https://mimic.mit.edu/docs/iv/).
Current structural adapters cover a **subset** of `hosp`/`icu` tables,
not MIMIC-IV-ED, -Note or -CXR. Its shifted/anchored dates need
MIMIC-specific design, including careful per-patient age/time calculations,
rather than pooling shifted calendar years or assuming cross-patient true dates.
Do not reconstruct identities or merge external record sources without approved
linkage and explicit permissions.

**Hospital EHR:** Obtain a written, site-specific data dictionary, permitted
patient/visit linkage, standardized codes and versions, date/time conventions,
outcome adjudication and a steward-approved mapping. The API **requires**
explicit `hospital_mapping` and does not silently use column-name guesses.

## Exact boundaries of the new implementation

The pure, in-memory helpers are:

- `SourceContext` and `assess_source_access`: reject incompatible
  declared environments, missing authorizations and off-platform export.
  All non-synthetic access evidence is an **attestation**, not verification.
- `inspect_source_table`: check *selected* required columns, missing or
  duplicate declared keys, and label all results `source_validated=False`.
  It caps in-memory work at 250,000 rows by default; larger sources require
  permissioned streaming/SQL validation.
- `relationship_integrity`: count unmatched links, without returning IDs.
- `visit_window_integrity`: flag missing, invalid or reversed time intervals.
  Timezone policy, clinical plausibility, shifted dates and censoring remain
  independent reviews.

These functions are neither a generalized ETL/OMOP conversion engine nor
publication-level validation. They do not provide automatic clinical
phenotypes, medications, units or PGx star-allele interpretation.

## Synthetic-only examples — no Workbench/PhysioNet data

~~~python
import pandas as pd
from thomaslab.healthcare_sources import (
    SourceContext, assess_source_access, inspect_source_table,
    relationship_integrity, visit_window_integrity,
)

aou = SourceContext(
    family="all_of_us", release="mock", environment="local",
    classification="SYNTHETIC", synthetic=True,
)
person = pd.DataFrame({
    "person_id": [1, 2], "gender_concept_id": [8507, 8532],
    "year_of_birth": [1980, 1971],
})
print(inspect_source_table(person, context=aou, table="person"))

mimic = SourceContext(
    family="mimic_iv", release="3.1", environment="local",
    classification="SYNTHETIC", synthetic=True,
)
admissions = pd.DataFrame({
    "subject_id": [1], "hadm_id": [100],
    "admittime": ["2026-01-01"], "dischtime": ["2026-01-03"],
})
print(inspect_source_table(admissions, context=mimic, table="admissions"))
print(visit_window_integrity(admissions, start="admittime", end="dischtime"))

hospital = SourceContext(
    family="hospital_ehr", release="mock-hospital-v1",
    environment="local", classification="SYNTHETIC", synthetic=True,
)
local = pd.DataFrame({"MRN_TEXT": ["00001"], "ENCOUNTER": ["A"]})
print(inspect_source_table(
    local, context=hospital, table="encounters",
    hospital_mapping={"patient_id": "MRN_TEXT", "encounter_id": "ENCOUNTER"},
))
~~~

No examples should be copied into an unauthorized environment using real
records. Do not mistake a `STRUCTURAL_REVIEW_REQUIRED` result for PASS.
Real-source contexts return `ATTESTATION_ONLY` where declarations look
consistent; the code **cannot verify program admission, DUA/IRB letters,
identity, workspace enrollment or storage ACLs**.

## Before the supervisor supplies a sample dataset

The private repository provides `configs/clinical_source_intake_template.yaml` as a **blank example**. Complete the actual intake only within institution-approved records; never commit signed approvals, confidential paths or patient metadata to a public or personal repository.

Request, in writing, the intended dataset family and source release;
whether the PI is legally authorized to share **this specific sample**;
the permitted secure compute location; IRB/HRPP determination and DUA;
row grain, identifiers, mapping dictionary, coding systems/versions,
date shift/time zones, restrictions on logs/results, retention and expiry.
Prefer fabricated or steward-provided synthetic schemas initially.
Never ask a supervisor to email protected patient files as ordinary attachments.

## Minimum verification and acceptance

~~~bash
python -m pytest -q tests/test_healthcare_sources.py tests/test_adaptive_governance.py
# Inside an authorized CPU Slurm job, at the exact pinned hardening-branch SHA:
bash scripts/verify_hardening_candidate.sh
~~~

Preserve the source SHA and tests. The original 21 October Herts technical
PASS was for an earlier commit; it does not certify these new adapters.
A clinical dataset moves beyond synthetic demonstration **only** after:
named source-specific review, full-source integrity/schema checks,
license/IRB/DUA, independently reviewed gold mappings, specialist model
validation, applicable privacy checks and secure-environment sign-off.

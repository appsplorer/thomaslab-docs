# Adaptive EHR relationship inference — S04 API reference

**Private module:** `thomaslab.adaptive.relationships`

**Development evidence:** S04 candidate, 34/34 focused synthetic tests passed on local Python 3.13.5/pandas 2.2.3/pytest 9.0.2. Combined with S03, 64/64 focused tests passed. The exact source and test Git blob hashes match the tested local files. Python 3.9–3.13 grammar parsing passed; actual Python 3.9 HPC runtime, full Core pytest/quality/coverage, authorized-source data validation and expert sign-off **have not passed**.

## Purpose and scope

S04 follows S01 complete metadata profiling and S03 review-required table-domain inference. It builds **possible** relationships between patient, admission/encounter, ICU-stay and downstream event tables using exact name/type evidence **within a single source system and source release**. It does not guess whether two hospitals share patients, infer a clinically valid admission, approve a mapping, execute a SQL join, or publish any data.

This is intentionally a small, testable milestone within the 46-deliverable hospital EHR project. It reuses `schema_discovery` and `clinical_domain_inference`, rather than introducing a second ETL system.

### Entry point 1 — propose metadata-only relationships

~~~python
from thomaslab.adaptive.relationships import propose_table_relationships

proposal = propose_table_relationships([
    complete_s01_patient_profile,
    complete_s01_admission_profile,
    complete_s01_icu_profile,
    complete_s01_lab_profile,
])
assert proposal["automatic_join_approved"] is False
~~~

Inputs are 2–64 *complete* S01 schema metadata reports from the same declared source system and release. Source-name, version, duplicate-table, column-physical-type and schema-status mismatches stop processing. The candidate parent must have an independently suggested `person`, `encounter` or `icu_stay` role.

Potential joins are proposed only for **matching exact lexical identifier fields**. No fuzzy matching or automatic `patient_id`-`subject_id` crosswalk is attempted. `site_id` is included in the proposed composite key when **both** tables carry it; one-sided site scoping results in abstention. Cross-hospital/cross-release matching requires a separately authorized identity-resolution process.

Parent keys are unverified structural candidates. A source containing multiple plausible parent-key aliases is explicitly blocked from automatic key selection. Child references containing missing values, such as `labevents.hadm_id`, are labelled for review rather than silently discarded.

For encounter-to-ICU joins, common patient identifiers are proposed as *additional consistency checks*. For ICU-stay-to-event links, available admission and patient identities are similarly checked. These are safeguards against a superficially valid but wrong encounter link.

Each candidate includes source-release identity, source schema hashes, source/target table labels, tentative join columns, consistency columns and `REVIEW_REQUIRED_NOT_AN_APPROVED_JOIN`. The output cannot authorize dataset export.

### Entry point 2 — bounded actual-key diagnostics

~~~python
from thomaslab.adaptive.relationships import validate_relationship_frames

diagnostics = validate_relationship_frames(
    reviewed_queue_candidate,
    authorized_parent_frame,
    authorized_child_frame,
    allow_missing_child_foreign_key=False,
    max_rows_per_table=100_000,
)
assert diagnostics["join_approved"] is False
~~~

This function only uses already-authorized **in-memory** DataFrames; it **does not open or access** new hospital files. The caller must establish permissions, storage and source completeness independently. Its default limit is 100,000 rows per table. This is deliberately a **bounded diagnostic**, not a full-source or billion-row validation engine.

It detects:
- Duplicate or missing parent composite identifiers.
- Orphan child references.
- Conflicting patient/admission identifiers across valid-looking links.
- Unknown or blank foreign keys; missing keys are blocked unless the reviewer *explicitly* supplies `allow_missing_child_foreign_key=True`.
- Numeric or otherwise nonlexical identifiers that might have lost leading zeros.
- Undeclared/untrusted candidate shapes, missing columns and exceeded memory limits.

The returned report contains counts and review statuses but no patient key values or row examples. It **still requires disclosure review** because even summary counts may be sensitive. A diagnostic without detected errors returns `BOUNDED_DIAGNOSTIC_REVIEW_REQUIRED`; a problem returns `BLOCK_STRUCTURAL_RELATIONSHIP`. Neither means a clinically approved join. Internal key maps remain in transient memory; this is not a hardened storage/egress control.

## MIMIC-IV-style synthetic illustration

~~~python
import pandas as pd
from thomaslab.adaptive.schema_discovery import discover_source_schema
from thomaslab.adaptive.relationships import (
    propose_table_relationships,
    validate_relationship_frames,
)

patient = pd.DataFrame({"subject_id": ["SYNTH001", "SYNTH002"]})
admissions = pd.DataFrame({
    "subject_id": ["SYNTH001", "SYNTH002"],
    "hadm_id": ["H01", "H02"],
    "admittime": ["2020-01-01", "2020-02-01"],
})
profiles = [
    discover_source_schema([frame], source_system="synthetic_hospital",
                           source_release="v1", table_name=name)
    for name, frame in (("patients", patient), ("admissions", admissions))
]
result = propose_table_relationships(profiles)
edge = next(x for x in result["candidates"]
            if x["parent_table"] == "patients"
            and x["child_table"] == "admissions")
diagnostic = validate_relationship_frames(edge, patient, admissions)
assert diagnostic["orphan_child_reference_rows"] == 0
assert diagnostic["join_approved"] is False
~~~

This example contains only invented identifiers; it makes no claim about the authorized MIMIC-IV dataset or an actual hospital's schema. It cannot determine whether source timestamps are shifted, population linkage is legal, or a drug-order record represents administration.

## Quality gates and limits

**Focused verification** on a development checkout:

~~~bash
python -m pytest -q tests/test_adaptive_relationships.py \
    tests/test_clinical_domain_inference.py
python scripts/ehr_platform_status.py
# Separately run full exact-current-commit Core quality and accepted CPU Slurm QA:
bash scripts/verify_hardening_candidate.sh
~~~

Remaining independent work includes complete approved CSV/Parquet/SQL/FHIR intake (P1-03), full-source streaming/cardinality validation on realistic data, signed source-specific clinical and data-steward approvals, multi-table ETL, terminology matching, robust patient identity crosswalks and accepted institutional compute. **No current S04 result is a release authorization or patient linkage approval.**

The next build items are P1-03's approved ingress gates, P1-06 multi-target mapping candidates with abstention, P1-07 intern/expert review workflow, and P2 controlled vocabulary import. Refer to the [EHR platform build plan](../../guides/ehr-platform-build-plan.md).

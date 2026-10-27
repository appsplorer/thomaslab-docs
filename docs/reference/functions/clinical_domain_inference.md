# `thomaslab.adaptive.clinical_domain_inference` — S03 API reference

**Engineering state:** Focused local synthetic tests passed at this source SHA.
Full private Core/HPC quality acceptance, clinical-domain accuracy on unseen
hospitals and institutional approval are **not established**.

## Purpose and contract

The S03 function consumes **only** a completed structural metadata report from
`thomaslab.adaptive.schema_discovery.discover_source_schema`. It proposes a
clinical table domain and possible source row grain, rather than classifying
patient records or assigning OMOP concepts. It does **not** open source files,
inspect patient values, download vocabularies, perform joins, approve mappings,
certify record uniqueness, or authorize any data export.

~~~python
from thomaslab.adaptive.clinical_domain_inference import (
    RULESET_VERSION,
    suggest_clinical_table_context,
)

result = suggest_clinical_table_context(completed_s01_metadata)
assert result["review_required"] is True
assert result["mapping_approved"] is False
assert result["source_grain_verified"] is False
assert result["authorized_for_export"] is False
~~~

`completed_s01_metadata` is a dictionary returned by the existing S01
`discover_source_schema(...)` function on an already authorized input.
This does **not** accept raw patient rows or an arbitrary source filename.

## Domains and safety semantics

| Candidate | Examples of structural hints | Important restriction |
|---|---|---|
| `person` | `patients`, `person`, `birth_date` | Patient identifier presence does not prove one row per person |
| `encounter` | `admissions`, `admittime`, `hadm_id` | Encounter keys and visit chronology still need review |
| `icu_stay` | `icustays`, `stay_id` | ICU stay-to-admission relationships are not validated |
| `condition` | `diagnoses_icd`, `icd_code` | Code-set system/version and actual diagnosis status not validated |
| `procedure` | `procedures_icd`, `procedure_code` | A procedure record is not proof of performed care without source semantics |
| `measurement` | `labevents`, `test_unit` | Assay, timestamp, measurement value and units not validated |
| `medication_order` | `prescriptions`, `prescription_id` | Orders must never become proven administrations |
| `medication_dispense` | `dispenses`, `dispense_id` | Dispensing is not proof of ingestion |
| `medication_administration` | `emar`, `not_given_reason` | Actual given/not-given state requires source-specific adjudication |
| `note` | `discharge`, `radiology`, `note_id` | No note text is parsed or made available to external services |
| `pgx` | `pgx_results`, `diplotype` | Genotype, assay, allele and CPIC/PharmVar interpretation unverified |
| `imaging` | `imaging_studies`, `study_instance_uid` | No image bytes or DICOM data processed |
| `claims` | `claim_lines`, `claim_line_id` | Claims do not independently prove care or outcome |

`domain_candidates` are ordered by a **deterministic heuristic ranking
score**, not a calibrated probability. Domain labels are candidate
**source-table categories**, not canonical OMOP target-table mappings.

Ambiguity, contradictory medication signals or too little evidence produces
`ABSTAIN_AMBIGUOUS_DOMAIN` or `ABSTAIN_INSUFFICIENT_EVIDENCE`.
An incomplete/unaccepted structural scan produces an error or
`BLOCK_SOURCE_SCHEMA`. Even an unambiguous candidate is
`CANDIDATE_REVIEW_REQUIRED`, never `AUTO_APPROVED`.

`row_grain_candidate` may be `PERSON_RECORD`, `ENCOUNTER_RECORD`,
`ICU_STAY_RECORD` or `CLINICAL_EVENT_RECORD`, but it remains explicitly
`CANDIDATE_UNVERIFIED_UNIQUENESS`. Subsequent P1-05 must check candidate keys,
repeated encounters, nullable links, and cross-table cardinality.

## Fully synthetic example

~~~python
import pandas as pd
from thomaslab.adaptive.schema_discovery import discover_source_schema
from thomaslab.adaptive.clinical_domain_inference import suggest_clinical_table_context

frame = pd.DataFrame({
    "subject_id": ["SYNTH01", "SYNTH02"],
    "hadm_id": ["A01", "A02"],
    "test_unit": ["mg/dL", "mg/dL"],
    "test_result": ["1.0", "2.0"],
})
profile = discover_source_schema(
    [frame], source_system="synthetic_hospital",
    source_release="v1", table_name="labevents",
)
context = suggest_clinical_table_context(profile)
assert context["suggested_domain"] == "measurement"
assert context["row_grain_candidate"] == "CLINICAL_EVENT_RECORD"
assert context["mapping_approved"] is False
~~~

Use this example only with invented synthetic records. Schema labels and
metadata counts can themselves be sensitive and should not leave approved
storage unless disclosure-reviewed.

## Test evidence and limitations

The exact source and synthetic test files were run locally and matched their
GitHub blob SHA values. **30/30 isolated tests passed** on local Python
3.13.5 and pytest 9.0.2. Python 3.9 and 3.11 grammar parses passed, but
runtime tests on those interpreters and full Core package tests were not
executed. Test cases cover 13 source domain families, contradictory
medication semantics, ambiguous clinical signals, incomplete scans,
unrecognized schemas, missing fingerprints, malformed normalized columns,
false approval flags, immutable inputs and no raw-value echo.

The ruleset is deliberately limited and synthetic. P1-05 multi-table
candidate-key/relationship testing, P1-06 reviewer-facing field ranking,
P1-07 human review routing, controlled vocabulary import and independent
held-out EHR validation are separate open work. A heuristic suggestion alone
must never be used to publish an OMOP clinical research dataset.

~~~bash
python -m pytest -q tests/test_clinical_domain_inference.py
python scripts/ehr_platform_status.py
bash scripts/verify_hardening_candidate.sh
~~~

See [staged hospital EHR build plan](../../guides/ehr-platform-build-plan.md)
and the [S01 schema discovery API](schema_discovery.md).

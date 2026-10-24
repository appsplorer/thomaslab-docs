# S10 — Canonical patient, encounter and event staging contract

**Engineering state:** local synthetic-test candidate. This is a **Thomas Lab
research staging contract**, not an OHDSI OMOP CDM 5.4 implementation, approved
patient identity transformation, certified temporal truth or finished
hospital research dataset. It does not ingest, transform, persist, export or
de-identify patient records.

Private API: `thomaslab.adaptive.canonical_dataset`. This builds on the
existing Core hospital EHR quality and OMOP diagnostic functions; it does not
replace `thomaslab.healthcare_omop`, `thomaslab.healthcare_hospital`,
the S01–S09 adapter and reviewer workflow or institutional policies.

## Versioned core table contracts

The current `thomaslab-ehr-staging-v1` contract has exactly three
structural table families:

| Family | Required fields | Grain and semantics |
|---|---|---|
| `person` | `site_id`, `person_id`, `source_system`, `source_release`, `source_record_id` | Unique **within site**. Original patient-ID pseudonymization is **not** verified |
| `encounter` | `site_id`, `person_id`, `encounter_id`, `admit_datetime`, `discharge_datetime`, `source_system`, `source_release`, `source_record_id` | Each visit links to a person at the same site; discharge may be null |
| `clinical_event` | `site_id`, `person_id`, `encounter_id`, `event_id`, `event_kind`, `event_datetime`, `recorded_datetime`, `available_datetime`, `source_system`, `source_release`, `source_table`, `source_record_id`, `mapping_revision` | Unique event within a site; visits may be null, but nonnull visits must belong to the same person/site |

Source and target identity strings remain lexical, so leading zeros are
preserved. A repeated `person_id`, `encounter_id` or `event_id` in
*different* sites is allowed; duplicate composite keys **within a site**
are blocked. A hospital's authorization to create pseudonymous IDs and
resolve cross-site patients is an independent P0-02 requirement.

Allowed distinct event kinds include condition, procedure, measurement,
observation, medication order, medication dispense, medication
administration, note metadata, PGx result, imaging and encounter event.
An order **never** becomes a documented administration simply because it
appears in the same event table.

## Three different event timestamps

- `event_datetime` — when the clinical event is said to have occurred
- `recorded_datetime` — when the event was recorded in its source system
- `available_datetime` — when the information first became available
  for research-feature purposes, subject to source review

All three are mandatory for S10 event rows. Timestamps must be
timezone-aware Python datetimes or ISO 8601 strings with an explicit
UTC offset (including `Z`). Numeric epoch assumptions and timezone-naive
values are blocked. Every event has a distinct source provenance ID
and mapping revision. Dates shifted by MIMIC-IV, retrospective corrections,
local timestamps, late entries and cross-hospital timezone reconciliation
**must** be reviewed before asserting point-in-time clinical semantics.

The conservative initial temporal contract refuses
`available_datetime` earlier than either event or recorded time.
Some legitimate EHR resources may not follow this chronology; those
cases require a source-specific, clinician-reviewed exception design.
Recorded timestamps preceding event times and events falling outside
their encounter interval are *counted for review* rather than silently
discarded. A null event encounter link is also counted, never fabricated.

This prevents one simple category of temporal leakage **only** and does
not establish causal/target-trial validity, true source availability or
point-in-time feature correctness.

## API and a synthetic usage sketch

```python
import pandas as pd
from thomaslab.adaptive.canonical_dataset import validate_staging_dataset

person = pd.DataFrame([{
    "site_id": "SITE-A", "person_id": "SYNTH-001",
    "source_system": "synthetic_ehr", "source_release": "v1",
    "source_record_id": "SYNTH-RAW-P1",
}])
encounter = pd.DataFrame([{
    "site_id": "SITE-A", "person_id": "SYNTH-001",
    "encounter_id": "SYNTH-H01",
    "admit_datetime": "2026-01-01T08:00:00Z",
    "discharge_datetime": "2026-01-03T08:00:00Z",
    "source_system": "synthetic_ehr", "source_release": "v1",
    "source_record_id": "SYNTH-RAW-E1",
}])
clinical_event = pd.DataFrame([{
    "site_id": "SITE-A", "person_id": "SYNTH-001",
    "encounter_id": "SYNTH-H01",
    "event_id": "SYNTH-M01", "event_kind": "measurement",
    "event_datetime": "2026-01-01T10:00:00Z",
    "recorded_datetime": "2026-01-01T10:05:00Z",
    "available_datetime": "2026-01-01T11:00:00Z",
    "source_system": "synthetic_ehr", "source_release": "v1",
    "source_table": "labs", "source_record_id": "SYNTH-RAW-L1",
    "mapping_revision": "v1",
}])
# Fake S01 hash values for synthetic contract illustration ONLY.
source_manifest = {
    "source_system": "synthetic_ehr",
    "source_release": "v1",
    "source_schema_fingerprints": {
        "person": "1" * 64,
        "encounter": "2" * 64,
        "clinical_event": "3" * 64,
    },
}
report = validate_staging_dataset(
    person, encounter, clinical_event, source_manifest=source_manifest
)
assert report["status"] == "STRUCTURAL_REVIEW_REQUIRED"
assert report["dataset_release_authorized"] is False
```

This function scans at most 100,000 in-memory rows per table and
128 columns per table (callers can set a *smaller* `max_rows_per_table`).
It only operates on already-authorized frames held within appropriately
governed compute. No files or networks are opened. It emits only restricted
aggregate row/exception counts and a structural manifest SHA-256 digest,
never the original person/encounter/event identifiers or rows.

**A structural manifest digest is not the dataset content checksum.**
S01 fingerprints are caller-supplied and their original extraction,
authenticity, source completeness and signatures are **not independently
verified** here. P0-05 immutable archival, versioned source snapshots,
full content hashing, retention policy, approved release IDs and FAIR
metadata remain OPEN.

## Production and clinical acceptance boundaries

`dataset_release_authorized`, `omop_cdm_54_conformance_verified`,
`person_identifiers_pseudonymization_verified`,
`full_source_completeness_verified`,
`source_manifest_signature_verified`,
`institutional_access_reauthorized`, and
`clinical_mapping_approved` remain explicitly false in every report.
No user should infer that the tested staging tables constitute clinical
or scientific publication-ready data.

**Focused S10 local evidence:** 39/39 invented-data regression tests
passed on Python 3.13.5 / pandas 2.2.3 / pytest 9.0.2. Python 3.9–3.13
AST grammar checks passed and exact source and test files matched
committed Git blobs. These run the new production module directly with
pandas; no mock source/registry modules are needed, but the **full Core
test suite, actual Python 3.9 runtime, Herts HPC, real source validation
and clinical data steward sign-off have not passed**.

```bash
python -m pytest -q tests/test_adaptive_canonical_dataset.py
python scripts/ehr_platform_status.py
# The exact-SHA full Core and accepted HPC verification are separate gates:
bash scripts/verify_hardening_candidate.sh
```

**Roadmap:** S10 locally completes only the *bounded temporal event contract*
of P0-04. P0-01/02/03/05/06, source connector P1-03, and approved
release/ETL/scalability remain OPEN. See
[the staged EHR implementation plan](../../guides/ehr-platform-build-plan.md).

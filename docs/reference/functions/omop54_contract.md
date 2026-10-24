# S11 — OMOP CDM 5.4.3 target definition and Thomas Lab extensions

**Status:** A version-pinned, locally tested design-time specification. Not an installed OMOP CDM database, clinical ETL, approved terminology mapper, certified dataset, or permission to process/export hospital patient data.

**Official basis:** [OHDSI OMOP CDM v5.4](https://ohdsi.github.io/CommonDataModel/cdm54.html), pinned to [OHDSI/CommonDataModel release v5.4.3](https://github.com/OHDSI/CommonDataModel/releases/tag/v5.4.3), commit `746a15e0fb36a95ba6cc0993737f1273bbad92f2`. Although OHDSI has released v5.5, Thomas Lab's explicit S11 target is **v5.4**; switching versions later requires separate review.

## Files and coverage

| Private Core file | Function |
|---|---|
| `configs/omop54_target_contract.json` | **39 official OMOP tables and 432 fields**, taken from the pinned OHDSI field/table CSVs. Each field preserves datatype, required, PK/FK and referenced table/field metadata |
| `configs/thomaslab_omop54_extensions.json` | Three proposed, *nonstandard* provenance, temporal and PGx sidecar manifests |
| `src/thomaslab/adaptive/omop54_contract.py` | Validates the release-tag and exact Git-blob snapshot; checks official field completeness; produces only review-required target blueprints |
| `tests/test_adaptive_omop54_contract.py` | 34 passing local synthetic tests for missing/extra fields, version drift, invalid FKs, extension scopes, medication abstention and forbidden approvals |

The official catalog Git blob is pinned to `7d37aac301f5ddeecf079ec88f37ca5e12c109d1`. The validator requires exactly 39 tables/432 fields and valid declared FK destinations. This is a **structural definition**; clinical content, actual database DDL, vocabulary releases, access rights and source rows are not verified.

OHDSI specifies that all CDM tables and columns should exist in a CDM installation, even if optional columns contain nulls. S11 rejects missing *optional as well as required* official columns when evaluating a completed table structure. Adding Thomas Lab-only fields to an official OMOP table also fails structural checks.

## Proposed sidecars — outside official OMOP

| Separate namespace | Proposed use | Additional release gates |
|---|---|---|
| `thomaslab.event_provenance` | Link a mapped target row to source system/release/table/record, S01 schema fingerprint and mapping revision | Data-use rights, identity linkage, provenance and disclosure review |
| `thomaslab.event_temporal_availability` | Keep event, recorded and available datetimes separate with timezone and exception reviews | Source time semantics, time-zone reconciliation and leakage review |
| `thomaslab.pgx_assay_provenance` | Reference assay, genotype-call method, gene/allele nomenclature, reference genome and guideline version | Genetic-data rights, lab assay and qualified PGx review |

All three are marked `not_for_export_by_default=true`, `PROPOSED_NOT_OHDSI_STANDARD` and independently reviewable. No standard OMOP table or vocabulary is modified.

## Controlled candidate mapping

`propose_omop54_targets()` returns unapproved possible destinations (e.g. condition → `condition_occurrence`, measurement → `measurement`). PGx has two candidate domains (`measurement` and `observation`) requiring expert disambiguation.

**Medication orders, dispensings, and administrations abstain**: none is automatically declared `drug_exposure`, nor are start/end dates, drug codes, routes or dose inferred. Imaging abstains too. No OMOP `concept_id` is assigned—not even the unmapped-concept convention of zero. Licensed, version-pinned terminology and a qualified clinician or pharmacist must validate clinical mappings.

## Usage — structural and synthetic

```python
from thomaslab.adaptive.omop54_contract import (
    load_omop54_catalog,
    inspect_omop_table_columns,
    propose_omop54_targets,
    assemble_omop54_target_blueprint,
)

catalog = load_omop54_catalog()
assert len(catalog["tables"]) == 39

candidate = propose_omop54_targets("measurement")
assert candidate["selected_target"] is None

blueprint = assemble_omop54_target_blueprint(
    staging_version="thomaslab-ehr-staging-v1",
    requested_tables=("person", "visit_occurrence", "measurement"),
    extension_names=("thomaslab.event_provenance",),
    vocabulary_release_reference="SYNTHETIC-UNVERIFIED-REF",
)
assert blueprint["staging_to_omop_etl_compiled"] is False
assert blueprint["dataset_release_authorized"] is False

measurement_fields = [
    field["name"] for field in catalog["tables"]["measurement"]["fields"]
]
report = inspect_omop_table_columns("measurement", measurement_fields)
assert report["status"] == "STRUCTURE_REVIEW_REQUIRED"
assert report["data_values_validated"] is False
```

This code opens **only bundled schema metadata**, never patient records, source databases, API endpoints or terminology providers.

## Testing and outstanding gates

**34/34 focused offline synthetic tests passed locally** on Python 3.13.5/pytest 9.0.2. The S11 source and test Git blobs match locally executed files. The official catalog was separately validated at commit time against OHDSI v5.4.3 field/table files: 39 tables, 432 fields, no invalid FK table or field references. The test fixture synthesizes equivalent table/field cardinalities and is **not** a full Core production-source integration test.

```bash
python -m pytest -q tests/test_adaptive_omop54_contract.py
python scripts/ehr_platform_status.py
bash scripts/verify_hardening_candidate.sh  # approved exact-SHA HPC only
```

Remaining independent requirements include verified database DDL/null/type/PK/FK compliance, vocabulary import licensing and standard concept mapping, site identity protection, source-to-target lineage and validation, OMOP Data Quality Dashboard, population/observation-period decisions, immutable release manifests, full private Core/Python 3.9/HPC testing, institutional IAM/IRB/DUA and clinical sign-off.

`P0-03 LOCAL_TEST_PASS` (if recorded) refers **only to the design-time version and proposed extension contracts**, not a clinically validated or publishable dataset.

See [S10 temporal staging](canonical_dataset.md) and [the EHR build plan](../../guides/ehr-platform-build-plan.md).

# S22 — Versioned research sidecars for OMOP 5.4

**Scope: version-pinned nonstandard extension schemas and synthetic in-memory SQLite instantiation.** The four research sidecars remain **outside** all 39 standard OMOP 5.4 tables. They are **not official OHDSI extensions**, not licensed clinical vocabularies, and not yet approved for patient data.

Pinned Core manifest: `configs/thomaslab_extension_tables_v1.json`, Git blob `ca76c04c74f7f3c12713161c5c49ffbec7307ef0`. Private module: `thomaslab.adaptive.extension_tables`.

| Separately versioned table | Review-only proposed purpose | Restricted-content boundary |
|---|---|---|
| `thomaslab_admin_event_v1` | Medication *administration* event time, source dose/route, approved target reference and order-link provenance | **Administration must not silently become OMOP drug exposure**; requires pharmacist-approved mapping |
| `thomaslab_note_provenance_v1` | Note digest, language/type reference, source event and first-available time | **No note body or note title column**; an ordinary SHA-256 of low-entropy note text is not a de-identification guarantee |
| `thomaslab_pgx_assay_v1` | Assay, gene, allele nomenclature and reference genome versions with phenotype source value | Genetic authorization, assay validity, CPIC/other guideline-version review required |
| `thomaslab_imaging_provenance_v1` | Modality/source image-study pseudonym, metadata digest and report first-availability | **No DICOM pixels, reports or original patient identifiers**; independent de-identification/metadata review required |

Each sidecar has a site reference, source release, opaque event and target-row references, source schema digest, mapping revision and human review reference. The v1 schema has a site-scoped composite primary key. Importantly, these sidecar references are *not* validated foreign-key links to real OMOP tables.

`load_sidecar_v1_spec()` loads the exact Git-blob-pinned v1 manifest and refuses changed schemas or altered default-deny/namespace declarations. `create_synthetic_sidecar_database()` creates the four tables in an ephemeral `:memory:` SQLite connection **only for invented data**, without modifying the official OMOP catalog. `insert_synthetic_sidecar_batch(...)` checks exact columns, site isolation, bounded batch size, digest/reference shapes, timezone-aware event times, finite dose values and duplicate keys. It rejects a file-backed/attached database and performs SQLite-transactional batch insertion.

## Invented test-only usage

~~~python
from thomaslab.adaptive.extension_tables import (
    create_synthetic_sidecar_database,
    load_sidecar_v1_spec,
)

definition = load_sidecar_v1_spec()
assert definition["export_default"] == "DENY"

connection, summary = create_synthetic_sidecar_database()
try:
    assert summary["official_omop_schema_modified"] is False
    assert summary["dataset_release_authorized"] is False
    # Test-only: insert_synthetic_sidecar_batch(...) with invented records.
finally:
    connection.close()
~~~

**Important:** Memory-only does not independently prove input data are synthetic. Never feed real clinical records into these functions. The caller can inspect the in-memory connection, so an externally approved governed storage/data execution environment must be implemented before any clinical use.

## Verification, delivery scope and remaining gates

The S21+S22 combined synthetic regression suite passed **51/51** on Python 3.13.5, and Python 3.9–3.13 syntax/compileall PASS. The config/module/test Git blobs match the exact tested files. Additional S23 tests passed **23/23**, for a three-milestone total **74/74**. Full original Core CI, supported Python 3.9 runtime, HPC, hospital-adopted physical extension storage, real source links, note/image privacy/security clearance and PGx clinical approvals remain unverified.

**P3-05 LOCAL_TEST_PASS only for versioned sidecar schema, in-memory synthetic instantiation and local safety checks.** This is not an authorized research data product or durable extension database.

Related: [S11 proposed extensions](omop54_contract.md), [S21 core builder](omop_core_builder.md), [S23 reconciliation](quarantine_reconcile.md), [EHR platform plan](../../guides/ehr-platform-build-plan.md).

~~~bash
python -m pytest -q tests/test_adaptive_omop_builders_sidecars.py
~~~

# S21 — Strict synthetic OMOP CDM 5.4 core record builder

**Scope: local, synthetic-only record construction; P3-04 remains OPEN.** Private module: `thomaslab.adaptive.omop_core_builder`. This is *not* an institutional OMOP ETL service, certified clinical mapping engine, de-identification guarantee or data-release endpoint.

The builder accepts the S11 pinned OHDSI OMOP 5.4 field contract (pass the exact `load_omop54_catalog()` output), an explicitly invented source batch and versioned source metadata. It constructs **complete row field shapes** with official required and nullable fields, strict types for integer, finite numeric, date, timezone-aware datetime and bounded varchar. It denies missing required fields, unknown/nonstandard columns, duplicate primary keys and invalid types.

Supported *synthetic* core-table fixtures are `person`, `visit_occurrence`, `observation_period`, `measurement`, `observation`, `condition_occurrence` and `procedure_occurrence`. **Drug exposure, clinical notes, death and unsupported tables abstain** pending genuine source semantics and privacy review. Seven fixture builders are not all 39 CDM tables.

For each core table with an official source-value field, the caller must supply the **original lexical source value separately** and exactly match it to `*_source_value`. Leading zeros and source-code strings cannot be truncated, reformatted or silently discarded. `observation_period` has no corresponding source-value field, so source values are refused there.

For every provided `*_concept_id`—including zero—the caller must supply an explicit opaque review reference. These references are **not an independent confirmation** of vocabulary entitlement, licensed concept validity, clinical domain matching, lab result units, phenotype interpretation or physician sign-off. The builder never chooses concept IDs.

## Invented example

~~~python
from thomaslab.adaptive.omop54_contract import load_omop54_catalog
from thomaslab.adaptive.omop_core_builder import build_synthetic_omop_rows

report = build_synthetic_omop_rows(
    "measurement",
    records=[{
        "measurement_id": 1001, "person_id": 100,
        "measurement_concept_id": 300,
        "measurement_type_concept_id": 400,
        "measurement_date": "2026-01-01",
        "measurement_source_value": "003.10",
    }],
    catalog=load_omop54_catalog(),
    source_metadata={
        "classification": "SYNTHETIC",  # self-declaration; not independently verified
        "site_scope": "invented_site",
        "source_system": "synthetic_ehr",
        "source_release": "v1",
        "mapping_revision": "m1",
        "source_schema_sha256": "a" * 64,
    },
    source_values=["003.10"],
    concept_reviews=[{
        "measurement_concept_id": "SYNTHETIC-REVIEW-01",
        "measurement_type_concept_id": "SYNTHETIC-REVIEW-02",
    }],
)
assert report["records"][0]["measurement_source_value"] == "003.10"
assert report["clinical_concepts_independently_validated"] is False
assert report["dataset_release_authorized"] is False
~~~

**Safety:** This function returns in-memory synthetic rows, including lexical source values. A caller can mislabel actual patient information as synthetic; the code cannot independently detect or prevent that. Never pass real, pseudonymized, deidentified, MIMIC-IV, All of Us or hospital EHR rows into this helper. Real ETL requires external institutional IAM, approved storage, source data contracts, licensed clinical terminology, controlled execution and pseudonym review.

## Verification and open gates

Combined S21/S22 local synthetic suite **51/51 PASS** (Python 3.13.5), plus S23 **23/23 PASS**; **74/74 total**. Python 3.9–3.13 grammar and compileall passed. Exact committed new sources/config/tests match the locally exercised files by Git blob. The local test suite supplies a reduced invented three-table catalog; full real Core import, pinned 39-table integration, medical record validation and Herts HPC/Python 3.9 runtime remain untested.

**P3-04 OPEN:** only seven safe fixture builders, no full table domain ETL, hospital approvals, provider/visit identity linkage, terminology verification, row-level provenance reconciliation, DQD or immutable release.

Related: [S11 OMOP 5.4 contract](omop54_contract.md), [S22 sidecar tables](extension_tables.md), [S23 reconciliation](quarantine_reconcile.md) and [platform plan](../../guides/ehr-platform-build-plan.md).

~~~bash
python -m pytest -q tests/test_adaptive_omop_builders_sidecars.py
python scripts/ehr_platform_status.py
~~~

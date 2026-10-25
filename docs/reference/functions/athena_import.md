# S17 — Governed OHDSI Athena full-package importer

**Status: locally tested software candidate; P2-02 remains OPEN pending licensed-source and institutional acceptance.** Private API: `thomaslab.adaptive.athena_import.import_athena_full_package`.

## Scope

S17 accepts an institution-authorized **full** Athena ZIP containing exactly nine official vocabulary TSV files: `CONCEPT.csv`, `CONCEPT_RELATIONSHIP.csv`, `CONCEPT_SYNONYM.csv`, `CONCEPT_ANCESTOR.csv`, `CONCEPT_CLASS.csv`, `DOMAIN.csv`, `DRUG_STRENGTH.csv`, `RELATIONSHIP.csv` and `VOCABULARY.csv`. It does not handle Athena delta packages, `delta.sql`, CPT4 reconstruction extras, proprietary repackaging or any unapproved extraction.

Athena documents TAB-delimited CSVs with headers inside full ZIP archives:
[Official Athena distribution](https://github.com/OHDSI/Athena) and
[The Book of OHDSI vocabularies](https://ohdsi.github.io/BookOfOhdsi-2ndEdition/representation/vocabularies.html).
Bundle contents and licensing can vary by selection and edition; this deliberately narrow full-bundle profile **rejects** incompatible packages instead of misimporting them. Confirm source version and rights with the institution.

## Implementation

`import_athena_full_package(archive, output_root, *, registry, release, actor, verify_entitlement, policy, ...)`:

- Requires `ExecutionPolicy` with approved input/output roots, declared institutional attestation, environment `institutional` or `hpc`, and row exports disabled. Requires private pre-created output directory (0700), refuses symlinks and unsafe archive paths.
- Re-reads the S16 `TerminologyReleaseRegistry` record for the *exact* `OHDSI_ATHENA` release with `VOCABULARY_QA` purpose, invoking a required external entitlement callback for revocation checking.
- Streams and verifies SHA-256 of the full ZIP against the declared registered pack hash **before** import. This verifies bytes against that declaration, not that the issuer signed the original hash or that the caller has a valid license.
- Rejects extra/missing ZIP members, delta scripts, encrypted members, unsupported compression, extreme compression ratios, oversized archives, malformed headers, non-UTF-8/NUL records and bounded row/field violations.
- Uses the S11 pinned OHDSI CDM 5.4.3 catalog for the exact nine table headers. Creates all nine SQLite tables with lexical/text columns, preserving source identifiers and codes without integer coercion. Metadata-defined field types are **not** enforced as native SQL types, so this is a restricted review index, not OMOP DDL conformance.
- Inserts in configurable bounded batches (default 1,000 records), with user-bounded ZIP size, decompressed bytes, rows, physical line length and SQLite database growth. Performs on-disk unique `CONCEPT.concept_id` and non-dangling `CONCEPT_RELATIONSHIP` / `CONCEPT_SYNONYM` checks. **It does not validate every OMOP concept/domain/vocabulary rule.**
- Writes a private database at `<approved_output_root>/athena_<release>/athena.sqlite` and a local `receipt.json`. Any detected failure in the import phase removes the partial release folder. Existing releases cannot be overwritten through this API.

**Security boundary:** The SQLite store contains potentially licensed terminology text and must remain inside institutionally approved storage. It must never be committed or exposed through GitHub, notebook output, CSV export, shared logs, public demos or external assistants. Restricted vocabulary content is not automatically eligible for dissemination.

The result reports imported row counts and archive checksum, but always marks `license_independently_verified=False`, `clinical_mapping_approved=False` and `authorized_for_export=False`. The module does **not** produce clinical concept mappings or authorize researcher access based on a notebook-supplied callback.

## API sketch

~~~python
from pathlib import Path
from thomaslab.adaptive.athena_import import import_athena_full_package

# Institutional identity, S16 registry, licensing and source paths MUST
# already be established by independently approved administrators.
result = import_athena_full_package(
    Path("/approved-input/athena/full-vocabulary.zip"),
    Path("/approved-private/vocabulary-index"),
    registry=registry,
    release="INSTITUTION_VERIFIED_RELEASE",
    actor="authenticated_steward",
    verify_entitlement=institution_owned_entitlement_service,
    policy=nonexporting_institutional_policy,
    batch_rows=1000,
)
assert result["authorized_for_export"] is False
~~~

## Verification and outstanding acceptance

**Focused synthetic tests:** 36/36 combined S17/S18 test cases passed locally on Python 3.13.5. They exercise creation/query of an invented nine-table ZIP, checksum/entitlement denial, corrupt ZIP/headers, source foreign-key corruption, rollback, local-compute denial and resource bounds. The local harness uses contract-compatible substitutes for S11's catalog and S16's registry/governance. The actual private Core dependency graph, Python 3.9 runtime, real licensed ZIP, source licensing terms, multi-GB performance and Slurm/HPC have **not passed**. The committed source/test files match the exact locally executed versions by Git blob SHA.

**P2-02 is still OPEN**: production acceptance requires institutionally obtained and licensed Athena source release, verified issuer checksum and entitlement, real ZIP format/scale tests in an approved enclave, clinical/vocabulary QA and a storage/egress security review. Full current-head Core quality and HPC acceptance remain separate gates.

Related: [S16 release registry](terminology_registry.md), [S11 pinned OMOP target](omop54_contract.md), [S18 ETL graph](etl_graph.md), [EHR development tracker](../../guides/ehr-platform-build-plan.md).

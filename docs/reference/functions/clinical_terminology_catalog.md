# Offline JSON terminology catalogue and dictionary readiness (S43)

**Status:** software-only inventory/audit candidate. It does not install 25 sources, prove licensing, authorize clinical mappings, verify an authentic release or certify large-scale production performance.

## What the JSON includes

`configs/clinical_terminology_catalog.json` includes **25 source families**, **21 capability entries**, **12 intended logical data tables**, a prespecified matching sequence and outstanding clinical, licensing, privacy, release and HPC acceptance gates. Each source is marked `NOT_INSTALLED`; no controlled vocabulary, license credential, clinical event or patient record is bundled.

All entries have separate `installation_state`, `license_independently_verified`, `clinical_contents_validated`, and `redistribution_authorized` states. They are all false or uninstalled until properly evidenced. A JSON file with a source name and download link does **not** mean a dictionary is present or usable.

Run entirely **offline**, without external services:

```bash
python scripts/clinical_terminology_status.py --catalog configs/clinical_terminology_catalog.json --repo-root . > private_review.json
```

To verify **locally installed** synthetic or externally authorized **private** S42 dictionary indexes, create a strictly private directory (`0700`) and a `0600` `installation_manifest.json` inside it, with an exact schema:

```json
{
  "version": "thomaslab-private-installed-v1",
  "installations": [
    {
      "source_id": "OHDSI_ATHENA",
      "dictionary_system": "MY_REGISTERED_ATHENA_VOCABULARY_ID",
      "source_release": "RELEASE_ID_FROM_THE_ACTUAL_AUTHORIZED_IMPORT",
      "dictionary_sha256": "64-lowercase-hex-from-the-real-S42-receipt",
      "source_package_sha256": "64-lowercase-hex-from-the-authorized-pack"
    }
  ]
}
```

The example above uses **placeholders, not installed content**. Remove placeholder entries instead of asserting false installation. The accompanying `configs/private_installation_manifest.example.json` contains an empty array for safe initialization. Do not place real institutional licence documents, credentials or source names that could identify hospitals in this public tree.

```bash
python scripts/clinical_terminology_status.py \
  --catalog configs/clinical_terminology_catalog.json \
  --repo-root . --installed-root /absolute/private/0700/dictionary_root > private_review.json
```

The CLI checks the private catalogue and the S42 `receipt.json`/`index.sqlite` integrity. It does not contact websites or APIs. Its positive state is **`PRIVATE_INDEX_HASH_VERIFIED_REVIEW_ONLY`**, never `APPROVED`. External independent licensing authority and curator validation are **not** inferred from an operator-written manifest.

## Batch unique-code matching

Use `thomaslab.terminology.batch_match.lookup_unique_codes` for up to 5,000 distinct lexical queries in an in-memory batch of up to 200,000 source entries. It opens and verifies one private pinned dictionary per batch, deduplicates codes without coercing leading zeroes, and abstains on ambiguity and context mismatches. It never authorizes ETL or external code release. This avoids re-hashing the entire dictionary file for every individual lookup, but **has not established multi-million-code throughput**. Use exact `system`+`release`+`dictionary_sha256` on every request, and keep returned codes inside the approved enclave.

## Full-specification gaps (not yet complete)

- The S42 dictionary builder materializes at most 250,000 concept records, does not scale to multimillion licensed packs or merge arbitrary source vocabularies safely.
- The original Athena importer supports nine full-package tables. Other primary/specialist vocabulary native formats (UMLS RRF, SNOMED RF2, NLM RxNorm RRF, NCI OWL, HGNC/HPO, UK NHS TRUD, CPIC/ClinPGx, etc.) are **not** implemented as governed production parsers.
- SQLite FTS5/RapidFuzz/FAISS semantic search, clinically reviewed dosage/specimen/assay rules, temporal crosswalk traversal, clinically calibrated ranking, full UCUM algebra and independently approved site-specific reuse remain absent or incomplete.
- S42 `lookup_concepts` hashes the full database for each request. The new batch API hashes once per batch. This is still not continuous WORM, signed source provenance, or a universal patient-level data processor.
- Real hospital labels, source permissions, gold mapping benchmarks, 15–20 independent held-out datasets, actual Python 3.9 runtime, complete Core CI and HPC remain unverified.

## Why vocabularies cannot be embedded in one JSON file

JSON should contain immutable *metadata and manifests*, source-specific release and licence status, concept-index receipts, policy flags, mapping/provenance identities and result summaries. Millions of lexical codes, synonyms and relationships should be in **private indexed SQLite, DuckDB or Parquet stores** with streaming ingestion. Baked-in licensed terminology redistributions may breach source-specific rights. The software can run offline after an authorized source pack has been obtained and installed under approved institutional controls. The public GitHub repository should contain code, tests, documentation and invented fixtures only.

Primary references: [OHDSI Book 2nd Edition](https://ohdsi.github.io/BookOfOhdsi-2ndEdition/representation/vocabularies.html), [UMLS licensing](https://www.nlm.nih.gov/databases/umls.html), [RxNorm licensing and variants](https://www.nlm.nih.gov/research/umls/rxnorm/overview.html), [LOINC](https://loinc.org/downloads/), [NHS terminology](https://digital.nhs.uk/services/terminology-and-classifications/dm-d).

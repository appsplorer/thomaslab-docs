# Adaptive clinical terminology dictionary — candidate S42 (P2-03 to P2-08)

**Status: local synthetic prototype. Not an installed licensed dictionary, approved mapping engine, or production-ready EHR harmonizer.** Core code: `thomaslab.terminology.dictionary`, `thomaslab.terminology.schema_aliases`, `thomaslab.terminology.ingestion_matrix`, and `thomaslab.adaptive.terminology_adapter`.

## What can run now

- **Private indexed concepts:** Write-once synthetic SQLite index, versioned source-system/release/code key, exact lexical code and normalized synonym lookup, hash-bound receipt, read-only queries, private 0700 directories, 0600 files and tamper checks. No PHI should be supplied, even to a function labelled synthetic.
- **A source-schema dictionary:** Approved-style S01 fingerprints are recomputed from column names/dtype families before source-to-canonical *candidate* aliases are stored in a write-once private JSON document. Existing reviewed adapter registry approval is not bypassed.
- **Clinical context:** Candidate retrieval requires a pinned terminology system and release. Optional domain/specimen/route conflicts trigger abstention. Multiple matching concepts and unsupported matches abstain rather than auto-map. Inactive entries are excluded. Every single hit still requires expert review.
- **Unit conversions:** Only deliberately entered, analyte-qualified rational conversions can return a numeric result; an unmatched or differently labelled analyte abstains. Rule provenance is stored as unverified `review_ref` metadata; clinician/vocabulary authority has not yet verified the content. No automatic mg/dL↔mmol/L or cross-assay conversion.
- **Relationships:** Bounded, referentially checked `MAPS_TO`, `IS_A`, or `EQUIVALENT_REVIEW_ONLY` links can be stored but are never treated as clinical equivalence or automatically applied to patient data.
- **Optional vocabulary packs:** `describe_optional_packs` validates version/hash/license manifest declarations for Athena, UMLS, SNOMED CT, LOINC, RxNorm, NHS dm+d, UCUM, CPIC, HGNC, and MONDO. It **does not download, license, install or redistribute** the resources.
- **Existing Athena importer bridge:** `build_index_from_authorized_athena` rechecks the existing private S16 terminology-registry entitlement and S17 package receipt, then builds a bounded source-vocabulary slice, preserving `concept_code` (including leading zeroes) and `CONCEPT_SYNONYM` strings. It rejects a source larger than the bounded review prototype rather than truncating it. It does not import Athena relations as unreviewed authoritative mappings, does not independently establish licensing, and cannot yet index the full multi-million-concept universe.
- **Synthetic mapping benchmark:** Counts offered candidates, abstentions and unsafe proposals against invented test labels; it does not claim clinically adjudicated gold labels or calibrated clinical performance.
- **Adaptive bridge:** `propose_synthetic_mapping` joins an S01 metadata fingerprint, exact S01 alias candidates and a source/version/context-specific dictionary hit. Returns a no-PHI, nonauthorizing reviewer proposal—not row-level transformed data or confirmed mapping.

## Multi-format ingestion (P1-03)

`validate_synthetic_ingestion_matrix` requires four source/release/schema-bound test receipts (CSV, Parquet, SQL and FHIR NDJSON), checks bounded counts and rejects known corruption flags including truncated Parquet, invalid UTF-8, dangling FHIR references, lossy code types and SQL BLOB fields. This is a **test matrix**, not a replacement for the actual `adaptive.source`, `adaptive.structured_ingest` and `adaptive.remote_ingest` readers. Full cross-connector integration and corrupt-source execution remain pending.

## How to exercise invented concepts locally

```python
from pathlib import Path
from thomaslab.terminology.dictionary import build_synthetic_dictionary, lookup_concepts

root = Path('/absolute/precreated/private_0700_directory')
result = build_synthetic_dictionary(
    root, system='ToyVocab', release='v1',
    concepts=[dict(system='ToyVocab', release='v1', code='00123',
                   label='Invented laboratory A', domain='MEASUREMENT',
                   specimen='Serum', route=None, aliases=['Toy lab A'], active=True)],
)
report = lookup_concepts(root, result['dictionary_sha256'],
                         query='00123', system='ToyVocab', release='v1',
                         domain='MEASUREMENT', specimen='Serum')
assert report['clinical_mapping_approved'] is False
```

For local software tests (no HPC):

```bash
python -m pytest -q tests/test_terminology_dictionary.py tests/test_terminology_adaptive.py tests/test_adaptive_terminology_adapter.py
```

**No real-pack or real-patient data acceptance.** Current limits include in-memory canonicalization of up to 250k term entries, mandatory full-database byte checks for each lookup (expensive for very large packs), only exact term/code matching (not semantic retrieval), no clinical accuracy calibration, no production sharded index/update job, no licensed pack validation against official release distribution, no independent KMS/WORM verification, and no actual HPC run.

## Authoritative sources for licensing and vocabulary usage

- [OHDSI Standardized Vocabularies and Athena](https://ohdsi.github.io/BookOfOhdsi-2ndEdition/representation/vocabularies.html) — Athena package conventions, `VOCABULARY`, relationships and release-specific downloads; proprietary source terms require licences.
- [NLM UMLS access and licensing](https://www.nlm.nih.gov/databases/umls.html) — an individual licence and source-specific restrictions may apply; a generic declaration is not a grant.
- [UMLS 2026AA licence source appendix](https://sites.wip.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/release/license_agreement_appendix.html) — restrictions vary across embedded terminologies.

Keep restricted packs private, never in `thomaslab-docs` or a public container. Record source release and licence per site, patient-use purpose and clinician mapping version. **Do not release clinical data or claim a comprehensive, validated dictionary on the basis of these software tests.**

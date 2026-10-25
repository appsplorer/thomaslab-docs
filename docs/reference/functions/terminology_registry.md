# S16 — Clinical terminology release registry and entitlement metadata

**Status: locally tested registry candidate; P2-01 remains OPEN.** It does not download, import, redistribute, validate or infer licensed clinical terminology concepts, or certify an institution's license. It stores release *metadata only*.

Private Core API: `thomaslab.adaptive.terminology_registry.TerminologyReleaseRegistry`.

## Controlled source families and release metadata

The source list includes `OHDSI_ATHENA`, `SNOMED_CT`, `LOINC`, `RXNORM`, `UCUM`, `UMLS`, `ICD10_CM`, `CPIC` and `NHS_DMD`. Their licensing varies by edition, jurisdiction and permitted use; inclusion is **not** a license grant.

Each exact `thomaslab-terminology-registry-v1` record includes source system, release version, **declared** pack SHA-256, opaque institution/license references, license model, jurisdiction, UTC entitlement expiry and permitted purposes (`CONCEPT_CANDIDATES`, `VOCABULARY_QA` and `CLINICAL_REVIEW`).

## Storage and fail-closed behavior

The registry requires a pre-existing private 0700 metadata directory. Each release is written once as a 0600 JSON metadata file with exclusive O_EXCL creation, record SHA-256 integrity and deterministic identity derived from source system plus release. Replacing a release's hash/metadata under the same version is not silently allowed.

Both registration and lookup call an *independently operated* institution entitlement verifier for actor/system/release/license/purpose/pack digest. This is a required **integration interface**. Lookup rechecks entitlement to deny revoked grants. Unknown releases, unrecognized licenses, expired permissions, tampered files and symlinked records fail closed.

**Limitations:** The module does not authenticate the external callback, independently verify declared pack bytes, validate license terms, download clinical code lists, import OMOP CONCEPT/CONCEPT_RELATIONSHIP tables or approve clinical mappings. A notebook stub returning True proves nothing about real license rights. Privileged administrators can still rewrite a fully local unsigned record.

## Invented synthetic example

~~~python
from datetime import datetime, timedelta, timezone
from thomaslab.adaptive.terminology_registry import VERSION, TerminologyReleaseRegistry

# approved_registry_dir must already exist with private permissions.
registry = TerminologyReleaseRegistry(approved_registry_dir)
metadata = {
    "schema_version": VERSION,
    "terminology_system": "LOINC",
    "source_release": "2026Q4",
    "pack_sha256": "a" * 64,  # invented value, not a real pack checksum
    "license_reference": "SYNTHETIC-LICENSE-001",
    "license_type": "RESTRICTED_LICENSE",
    "institution_reference": "SYNTHETIC-HOSPITAL",
    "jurisdiction": "US",
    "expires_at": (datetime.now(timezone.utc) + timedelta(days=60)).isoformat(),
    "allowed_purposes": ["CONCEPT_CANDIDATES"],
}
registry.register(metadata, actor="synthetic_researcher",
                  purpose="CONCEPT_CANDIDATES",
                  verify_entitlement=lambda *args: True)  # synthetic tests ONLY
result = registry.lookup(system="LOINC", release="2026Q4",
                         actor="synthetic_researcher",
                         purpose="CONCEPT_CANDIDATES",
                         verify_entitlement=lambda *args: True)
assert result["concepts_loaded"] is False
assert result["terminology_import_authorized"] is False
assert result["clinical_mapping_approved"] is False
~~~

Never put downloaded restricted vocabulary packs, credentials, site identifiers or patient data into GitHub, logs or the registry directory. The OMOP v5.4.3 field contract in S11 is independent of the institution's actual Athena vocabulary release.

## Focused evidence and open gates

**30/30 synthetic tests passed locally** on Python 3.13.5 / pytest 9.0.2, with source/test Git-blob matches, compilation and Python 3.9–3.13 AST grammar checks. The tests cover release persistence, version conflicts, entitlement denial/revocation, expiry, unsafe license types, tamper detection, symlinks, missing packs and authorized-purpose constraints.

The actual private Core full QA, Python 3.9 runtime/HPC, approved institutional entitlement service, signed release evidence, source pack byte verification and real clinical code import remain **NOT PASSED**. P2-01 remains OPEN.

~~~bash
python -m pytest -q tests/test_adaptive_terminology_registry.py
python scripts/ehr_platform_status.py
bash scripts/verify_hardening_candidate.sh
~~~

Related: [S11 OMOP target](omop54_contract.md), [S13 source-use policy](source_use_contract.md), and [EHR platform plan](../../guides/ehr-platform-build-plan.md).

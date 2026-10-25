# S15 — Site-scoped keyed pseudonymization and cross-site separation

**Status: synthetic locally tested candidate; P0-02 remains OPEN.** This is a bounded, in-memory identity transformation contract, not an institutional KMS/HSM integration, determination of de-identification under HIPAA/GDPR, patient-consent check, permitted interhospital linkage or clinical data release.

The private Core API is \`thomaslab.adaptive.site_identity\`. It adds \`pseudonymize_site_id\`, \`pseudonymize_site_batch\` (1–10,000 IDs), and \`inspect_cross_site_linkage_request\`. The latter **always blocks** cross-site linkage and never creates a crosswalk.

## Design and privacy boundaries

An HMAC-SHA-256 token is derived from a **site-managed, 32–128-byte cryptographic key** plus length-prefixed and domain-separated source context: site, source system, identifier namespace, entity grain (\`person\`, \`encounter\`, \`event\`), key version, and the original lexical identifier. This avoids unkeyed SHA hashing of low-entropy medical record numbers. Leading zeros and case-sensitive source IDs are preserved. Unsafe control characters, non-NFC text, whitespace-padded IDs, unsupported grains, weak keys and missing key providers fail closed.

The function outputs a \`tlp1_<sha256-hex>\` scoped pseudonym and explicit denial flags, never a raw source ID, site key, or approved hospital mapping. Stable tokens are intentionally **site- and namespace-specific**. Identical source IDs at two sites yield different tokens; distinct grains cannot be conflated. A rotated key version changes tokens and requires a separately controlled migration process.

**Pseudonymized IDs can still be personal data** and must remain within the authorized enclave. Tokens are potentially linkable, especially if coupled with dates, rare conditions, genes or site labels. Key bytes enter the Python process and are not guaranteed to be zeroized from memory; the library cannot prove trusted KMS custody because the caller supplies the key-provider callback. A researcher-supplied constant key is **not** a production identity service. Do not put real IDs, keys or pseudonymized record extracts in GitHub, CI logs or ChatGPT.

## Synthetic example

~~~python
from thomaslab.adaptive.site_identity import pseudonymize_site_id

# Test fixture only; do not hardcode institutional keys in notebooks!
development_key = bytes(range(32))
result = pseudonymize_site_id(
    "SYNTH-00001",
    site_id="SITEA",
    source_system="synthetic_ehr",
    identifier_namespace="patient_id",
    entity_kind="person",
    key_version="demo_v1",
    get_site_key=lambda site, version: development_key,
)
assert result["pseudonym"].startswith("tlp1_")
assert result["source_identifier_disclosed"] is False
assert result["institutional_linkage_approved"] is False
assert result["protected_data_release_authorized"] is False
~~~

For approved institutional deployments, the separate key provider must be owned by a hospital/approved data custodian, enforce actor/purpose/role and key-rotation authorization, use approved cryptographic material and auditable protected storage, and be independently accepted by security and privacy officers. Real consent/IRB/DUA, protected source identity rules, cross-site linkage adjudication, deterministic key migration and controlled pseudonym lifecycle remain P0-02 gates.

## Focused evidence

**39/39 synthetic identity tests passed locally** (Python 3.13.5, pytest 9.0.2). Exact source/test Git blobs matched the tested files, and Python 3.9–3.13 grammar plus compilation checks passed. No real patient IDs were used. This module has only Python standard-library dependencies, but the complete current private Core import/quality suite, actual Python 3.9 runtime and approved HPC tests have not passed.

~~~bash
python -m pytest -q tests/test_adaptive_site_identity.py
python scripts/ehr_platform_status.py
bash scripts/verify_hardening_candidate.sh  # only on approved exact Core SHA
~~~

**P0-02 is still OPEN.** S15 adds a locally verified keyed identity component, not a secure multi-institution linkage service or approved research dataset.

See [S10 staging](canonical_dataset.md), [S13 use/retention](source_use_contract.md), and [platform plan](../../guides/ehr-platform-build-plan.md).

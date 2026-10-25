# S20 — Site-scoped protected join and point-in-time temporal specification

**Status: locally tested design component; full P3-03 remains OPEN.** Private API: `thomaslab.adaptive.protected_joins`. This module consumes only the SHA-256-bound nonexecuting S19 IR. It does not read EHR rows, derive patient identity links, query hospitals, execute SQL, or authorize release.

## Safety contract

`define_protected_joins(...)` demands exactly one specification for every S19 source-to-stage edge declaring join keys. Each approved site/identity specification must have an explicit matching site equality `site_id = site_id`, a person/encounter/event key pair matching the declared entity grain, an opaque pseudonymization key-version reference, and the original edge's review reference. Origin and destination sites must match the original S18 site scope; **cross-hospital linking is categorically denied**.

The caller must supply a protected identity-scope verifier callback. The callback is required and rechecked, but a local lambda returning `True` is NOT an identity provider or independent proof of KMS/IRB/DUA authorization. Keys and source patient IDs are never accepted by this module.

The temporal policy `AS_OF_THREE_CLOCKS` requires an explicit index-time reference and bounded positive lookback, with a required independent review of *event time, source recording time and first data-availability time*. `NO_TEMPORAL_JOIN` is allowed only as an explicit non-temporal design. Neither policy generates SQL; neither guarantees the source's timestamps reflect actual clinical availability.

`screen_synthetic_asof_clocks` screens strictly synthetic ISO-8601, timezone-aware, four-clock examples and returns **only aggregate counts** of cases with event/recorded/available values that could leak beyond a study index time. It never returns original timestamps or patient events.

## Example

~~~python
from thomaslab.adaptive.protected_joins import define_protected_joins

join_plan = define_protected_joins(
    s19_ir,
    joins=[{
        "edge_id": "link",
        "origin_site": "siteA",
        "destination_site": "siteA",
        "entity_grain": "PERSON",
        "site_key_version": "k1",
        "site_key_pair": ["site_id", "site_id"],
        "person_key_pair": ["person_id", "person_id"],
        "join_review_reference": "JOIN-REVIEW-001",
        "temporal_rule": "AS_OF_THREE_CLOCKS",
        "index_time_reference": "index_analysis",
        "max_lookback_days": 365,
    }],
    actor="synthetic_reviewer",
    verify_site_key_review=lambda *args: True,  # SYNTHETIC TEST ONLY
)
assert join_plan["patient_join_authorized"] is False
assert join_plan["sql_generated"] is False
~~~

Use site-specific HMAC tokens only under independent P0-02 identity-service permissions. Never insert raw patient IDs, source row samples, keys, credentials or restricted study dates into notebooks, ChatGPT, GitHub or public docs.

## Verification and remaining work

34/34 S19+S20 focused synthetic tests passed on Python 3.13.5, including invalid grain, source/site mismatch, missing review, tampered IR, future availability, timezone ambiguity and recorded-before-event cases. Exact new code/test Git blobs match local tests and Python 3.9–3.13 grammar checks passed.

**P3-03 stays OPEN.** The source hospital's time semantics, actual pseudonym/encounter key provenance, approved identity-service callback, longitudinal patient/visit linkage, independent clinical review, controlled execution, large-scale HPC join cardinality tests and full current-SHA Core regression remain unverified.

Related: [S15 keyed identity](site_identity.md), [S10 event clocks](canonical_dataset.md), [S19 ETL compiler](etl_compiler.md), [development plan](../../guides/ehr-platform-build-plan.md).

~~~bash
python -m pytest -q tests/test_adaptive_etl_compiler_joins.py
bash scripts/verify_hardening_candidate.sh  # approved exact-SHA Core/HPC only
~~~
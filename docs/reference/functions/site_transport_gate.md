# S31 — Synthetic cross-hospital schema drift and held-out-site transport preflight

**Development status: local synthetic candidate; P4-06 OPEN.** The implementation is a *preflight audit*, not model transportability validation. It cannot approve cross-hospital linkage, access, clinical equivalence, site participation, phenotype validity or protected-data release.

**Private module:** `thomaslab.adaptive.site_transport_gate`.

`audit_synthetic_site_transport(*, site_profiles, site_mapping_contracts, partitions, train_sites, holdout_site, required_canonical_fields, missingness_gap_threshold=0.15, minimum_site_participants=11, require_future_holdout=False)` verifies:

- Site metadata is a complete, internally consistent S01 `discover_source_schema` result with exact independently recomputed structural SHA-256 and no patient values; source schema remains unreviewed.
- Each source site has a version-bound, explicitly *declared* canonical field mapping with reviewer SHA-256 and mapping revision. Declared reviewer digests do not authenticate any reviewer or mapping semantics.
- Training sites and the holdout site are disjoint, all site/participant partitions are present, participant tokens are unique *within* site, and at least 11 invented participants per site exist.
- Canonical field presence and physical datatype compatibility, S01 physical-type conflicts, and weighted training versus held-out missingness differences. A configurable prespecified maximum absolute missingness-rate difference causes a block when exceeded.
- Potentially colliding patient tokens across training and holdout sites are flagged conservatively. Identical local hospital IDs do **not** establish shared human identity; actual linkage requires a trusted, authorized institutional service.
- When the study contract requires a later-period holdout, the earliest holdout index must strictly follow the latest training index. Ordinary *different-site* holdout does not automatically require later chronology.
- Every output is aggregate-only with no source column names, patient keys or site identifiers, and `authorized_for_export=False`. A positive *structural* report requires independent assessment of clinical semantics, observation capability, covariate shift, label ascertainment, protected-data access and model performance before publication.

Synthetic usage:

~~~python
from thomaslab.adaptive.site_transport_gate import audit_synthetic_site_transport

report = audit_synthetic_site_transport(
    site_profiles=site_specific_s01_synthetic_schema_reports,
    site_mapping_contracts=review_declared_synthetic_mapping_contracts,
    partitions=synthetic_participant_partitions,
    train_sites=["inventedHospitalA", "inventedHospitalB"],
    holdout_site="inventedHospitalC",
    required_canonical_fields={"person": "text_or_object", "measurement": "integer"},
    require_future_holdout=True,
)
assert report["authorized_for_export"] is False
assert report["transport_accuracy_or_calibration_established"] is False
~~~

## Validation gaps

S31 passed **32 local synthetic regression cases** (combined S30/S31 64/64) on Python 3.13.5. Python 3.9–3.13 grammar parsing passed. There is no real multi-hospital EHR, OMOP mapping approval, cross-site identity service, site-stratified clinical gold standard, transport discrimination/calibration evaluation, institutional disclosure clearance or exact-head Core/HPC acceptance. The module can inspect metadata but cannot determine whether a model was fit on held-out data. **P4-06 remains OPEN.**

~~~bash
python -m pytest -q tests/test_adaptive_site_transport_gate.py
~~~

See S01 `schema_discovery`, S09 `mapping_memory`, S29 `clinical_observability`, and the existing `thomaslab.healthcare_quality.site_temporal_holdout_preflight` (separate design assumptions).

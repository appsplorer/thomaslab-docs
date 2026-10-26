# S44 — Clinical graph traversal, conservative mapping triage and 12-capability audit

**Software-development candidate, synthetic data only. No automatic clinical mapping or release permission.**

This increment extends the existing S42 release-pinned SQLite dictionary and S43 batch code matcher instead of creating a second terminology service.

## API additions

- `thomaslab.terminology.clinical_graph.trace_concept_relationships(root, sha, system, release, start_code, ...)`: locally traverse the actual S42 `relationship` table for **one verified dictionary SHA-256 and terminology release**. Directional `MAPS_TO`, `IS_A` and `EQUIVALENT_REVIEW_ONLY` edges retain their separate meaning; bounded depth/node/edge budgets prevent unbounded expansion. No edge licenses automatic equivalence, concept assignment, publishing licensed codes or clinical decisions.
- `thomaslab.adaptive.review_prioritization.plan_synthetic_distinct_code_reviews(...)`: deduplicate up to 5,000 invented source-code observations using the S43 matcher, then assign review lanes based on *declared* clinical-impact category, code frequency, site novelty, candidate ambiguity and an **uncalibrated** uncertainty heuristic. High-impact or unresolved cases go to `CLINICAL_EXPERT_REQUIRED`; even easy cases require intern and expert review. A valid local hit never becomes a governed approved mapping or ETL authorization.
- `thomaslab.adaptive.capability_audit.audit_candidate_capabilities(catalog, root)`: offline inspect the controlled 12-capability JSON to check code-file presence, explicitly returning false for technical/HPC/clinical acceptance. The attached `configs/ehr_12_capability_matrix.json` names exactly 12 requested capability areas and lists their implementation modules and real-world blockers.

### Local synthetic example

```python
from thomaslab.terminology.clinical_graph import trace_concept_relationships
from thomaslab.adaptive.review_prioritization import plan_synthetic_distinct_code_reviews

# These require an already-created S42 private 0700 SYNTHETIC dictionary.
relationships = trace_concept_relationships(
    private_root, dictionary_sha256, system='Toy', release='v1', start_code='A01',
    max_depth=2, max_nodes=20, max_edges=50,
)
triage = plan_synthetic_distinct_code_reviews(
    private_root, dictionary_sha256, system='Toy', release='v1',
    requests=[{
        'source_code': 'A01', 'frequency': 250,
        'clinical_impact': 'HIGH', 'source_novelty': 'NEW_SOURCE_RELEASE',
        'uncertainty': 0.3,
    }],
    domain='MEASUREMENT', specimen='Serum',
)
assert triage['mapping_approved'] is False
assert triage['tasks'][0]['review_lane'] == 'CLINICAL_EXPERT_REQUIRED'
```

**Risk score caveat:** The numerical priority is a deterministic scheduling heuristic, not a calibrated probability, model-based uncertainty estimate, impact assessment or clinical risk decision. It must not be used to waive human review. Even a previously reviewed adapter needs the original S09 governed mapping-memory, independent role verifier and full-source validation.

## Mapping each of the 12 requested additions

| Capability | Present software | Critical gap before full acceptance |
|---|---|---|
| Clinical knowledge graph | S42 relationship table + S44 bounded traversal | Licensed, complete graph provenance, curator-approved semantics and scale |
| Risk-calibrated mapping | S43 candidate abstention + S44 triage | Gold-standard calibration, clinically measured unsafe-match rate |
| Active-learning review | S08 review queue + S44 reviewer priority | Actual human feedback loop, reviewer assignment/role authority, adaptive model validation |
| Incremental ingestion/cache | S25 dependency invalidation + S25 byte-verified checkpoint | Approved source CDC, durable result verification at actual scale |
| Quality observability | S29 synthetic site/period counters | Live feeds, OHDSI DQD-style tests, clinical anomaly thresholds |
| Temporal integrity | S30 timing/censoring/coverage + S36 synthetic mart | Clinical time-zero adjudication, true cohort/mart execution |
| Lineage | S28 private synthetic lineage | Institutional key management and independent record-level audit |
| Privacy/IAM | S13–S15 contract and audit candidates | Real institution-managed access, egress, disclosure and signed approvals |
| Cohort/phenotype library | S35 candidate registry | Actual validated definitions and signed clinical reviews |
| Multi-hospital federation | S33 synthetic count pooling | Data partner approvals and real site-local executor/disclosure budget |
| Performance | S26/S27 synthetic stream and S32 Slurm plan | Benchmarks on 1m/10m/100m/billion events, real PyArrow/DuckDB/HPC timings |
| FAIR releases | S41 release metadata draft | Institutional data custodian authority, access terms, legitimate DOI |

**No technical subsystem may set institutional data rights or independent clinical acceptance using its own JSON boolean**. The JSON is a trackable inventory; real rights, licenses and expert reviews come from independently verified external authorities. Store licensed terminology indexes privately; do not include vocabulary rows in public docs or source control. Actual MIMIC-IV, All of Us and institutional EHR records were **not used**.

### Development verification

- S44 focused tests: **32/32 passed** locally using the S42 dictionary engine and S43 batch matcher.
- Combined with existing S43 catalogue/batch regressions: **66/66 passed** in the local prototype environment.
- Python 3.9–3.13 grammar syntax parsing is required; actual Python 3.9 runtime, complete Core import/CI and HPC are separate gates not yet passed.
- The full original private Core acceptance and independent clinical validity remain **OPEN**.

```bash
python -m pytest -q tests/test_s44_graph_triage.py tests/test_s44_capability_audit.py
python -m pytest -q tests/test_terminology_catalog.py tests/test_terminology_batch_match.py
```

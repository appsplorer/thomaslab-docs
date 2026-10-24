# Method readiness: transparent evidence levels

**Updated:** 24 October 2026. This is a *status contract*, not a certification.

The private Core candidate maintains `configs/method_readiness.yaml` and a
fail-closed `scripts/check_method_readiness.py` guard. Neither repository may
self-certify external clinical validation through a documentation edit.

| Method family | Source features | Verified evidence | Current study-level gate |
|---|---|---|---|
| New hospital EHR schema discovery/drift candidate | adaptive.schema_discovery (2 methods) | 17 synthetic local tests passed; source SHA registered in candidate; exact-HEAD Core CI/HPC not accepted | Source-specific schema, roles, permissions, code/units and clinician review remain NOT_ASSESSED |
| Ranked canonical EHR source-field proposals (S07 candidate) | adaptive.field_suggestions | 37/37 synthetic local tests; S03 code reused, S01 and Core alias/contract dependencies exercised through compatible offline test surrogates | No exact Core/HPC QA, calibrated mapping probabilities, named clinical review or approved ETL |
| Remote PostgreSQL/FHIR connector contracts (S06 candidate) | adaptive.remote_ingest | 39 synthetic local tests pass; exact new code and tests matched Git blobs, with fake DB/HTTP and substitute Core dependencies | No independently checked IAM/OAuth/TLS/database role, no actual Core/HPC or real source acceptance |
| Local SQLite + FHIR NDJSON schema preflight (S05 candidate) | adaptive.structured_ingest | 41/41 isolated synthetic tests with existing dependencies represented by local surrogates; exact code/test Git hashes match | No full Core/HPC acceptance, no remote SQL/FHIR source authorization, no clinical mapping or valid patient-data release |
| Governed bounded file metadata intake (S02 candidate) | adaptive.schema_intake | 15 isolated wrapper smoke cases, one optional Parquet skip; real Core integration/HPC not accepted | Source paths, declared data-use rights and clinical mapping not independently approved |
| Clinical domain and row-grain inference (S03 candidate) | adaptive.clinical_domain_inference | 30/30 local synthetic tests; structural heuristic ranking and abstention | No calibrated mapping confidence, certified source grain or clinical validation |
| Patient/encounter/ICU relationship inference (S04 candidate) | adaptive.relationships | 34/34 local S04 synthetic tests; 64/64 S03+S04 combined | No approved joins, independently verified full-source cardinality or real-data validation |
| Structural source profiling and baseline metrics | healthcare_foundation (new, experimental) | New unit regression examples; branch integration pending | NOT_ASSESSED for real patients |
| All of Us CDR v9 (Registered/Controlled) | healthcare_sources source contract (candidate) | Synthetic OMOP-shaped tables only; no program records obtained | Workbench-only analysis and authorization, release-specific dictionary and independent review |
| MIMIC-IV v3.1 hosp/icu | healthcare_sources source contract (candidate) | Synthetic tables only; no PhysioNet records obtained | Credentialing/DUA, permitted environment, module-specific key, shifted-time and event reviews |
| Institution-specific hospital EHR | healthcare_sources source contract (candidate) | Synthetic explicit-mapping tests only; no UGA hospital sample obtained | PI/IRB/DUA, approved storage, signed mapping, clinical code/unit/date and clinical-validity review |
| Clinical ML time-zero and leakage preflight | clinical_leakage + existing splits/leakage (candidate) | 12 locally executed synthetic guards for result availability, feature timing, purged patient splits and train-only imputation; current full-Core SHA acceptance pending | Clinician-reviewed time zero, feature posting/availability, patient/site splitting, data rights and independent validation |
| Outcomes, censoring, target-trial time zero and claims continuity | clinical_followup (candidate) | 9 locally executed synthetic safeguards for event followup, post-index treatment and enrollment gaps | Real-data capture, negative-label adjudication, informative censoring, causal protocol and site/claims review |
| Common clinical code/medication/site QA | healthcare_quality (candidate) | Code-set SHA, text-code preservation, event-state and holdout/small-stratum tests authored; exact-commit execution pending | No self-attested vocabulary or disclosure approval; external source/method review required |
| EHR/claims/OMOP/FHIR | adapters, contracts, validation | Synthetic tests and previously observed full QA gate | Named, source-specific semantic approval |
| PGx and CYP2C19/CYP2D6 | pgx modules and knowledge YAML | Software contracts; convenient incomplete knowledge tables | Upstream CPIC/PharmVar release/version and clinical panel review |
| NLP and annotations | context/annotation modules | Synthetic tests; adjudication helpers | Held-out gold annotations, site-specific error and disclosure review |
| Prediction and site validation | models/eval/external validation | Software quality gates, synthetic fixtures | Patient/site/time splits, calibration, decision curves, clinical thresholds |
| Causal and target-trial methods | causal/target_trial/longitudinal | Structural preflights, positivity/E-value checks | Identification, controls, clinical comparators, independent replication |
| Survival and competing risks | survival/censoring/recurrent | Numerical regression and prior HPC QA evidence | Independent method and endpoint validation |
| Health economics and utilization | economics/hcru | Software modules and synthetic checks | Currency/year/price perspective, sensitivity and economic review |

No method is marked **real-data validated** or **production clinical use**
without an independently approved dataset, named expert review and evidence.
The reported 21-phase HPC PASS is a technical property of one prior Git SHA,
not validation of every model or any named institution's health record system.

Before a paper, map relevant results to TRIPOD+AI, PROBAST+AI, STROBE,
RECORD/RECORD-PE and TARGET, noting which guidelines apply. A guideline name
alone cannot establish checklist compliance.

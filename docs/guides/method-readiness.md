# Method readiness: transparent evidence levels

**Updated:** 22 October 2026. This is a *status contract*, not a certification.

The private Core candidate maintains `configs/method_readiness.yaml` and a
fail-closed `scripts/check_method_readiness.py` guard. Neither repository may
self-certify external clinical validation through a documentation edit.

| Method family | Source features | Verified evidence | Current study-level gate |
|---|---|---|---|
| Structural source profiling and baseline metrics | healthcare_foundation (new, experimental) | New unit regression examples; branch integration pending | NOT_ASSESSED for real patients |
| All of Us CDR v9 (Registered/Controlled) | healthcare_sources source contract (candidate) | Synthetic OMOP-shaped tables only; no program records obtained | Workbench-only analysis and authorization, release-specific dictionary and independent review |
| MIMIC-IV v3.1 hosp/icu | healthcare_sources source contract (candidate) | Synthetic tables only; no PhysioNet records obtained | Credentialing/DUA, permitted environment, module-specific key, shifted-time and event reviews |
| Institution-specific hospital EHR | healthcare_sources source contract (candidate) | Synthetic explicit-mapping tests only; no UGA hospital sample obtained | PI/IRB/DUA, approved storage, signed mapping, clinical code/unit/date and clinical-validity review |
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

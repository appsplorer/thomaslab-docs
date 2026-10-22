# Method readiness: transparent evidence levels

**Updated:** 22 October 2026. This is a *status contract*, not a certification.

| Method family | Source features | Verified evidence | Current study-level gate |
|---|---|---|---|
| Structural source profiling and baseline metrics | healthcare_foundation (new, experimental) | New unit regression examples; branch integration pending | NOT_ASSESSED for real patients |
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

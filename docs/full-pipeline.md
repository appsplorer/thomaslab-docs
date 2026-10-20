# Full research pipeline

This is the canonical end-to-end documentation for **thomaslab-core v1.x**. It connects the platform's data onboarding, clinical-domain construction, study design, leakage control, modeling, causal inference, validation, reporting, provenance, and research-bundle export into one reviewable workflow.

> **Research-use boundary:** thomaslab-core is research software. It is not a medical device and does not turn statistical associations, model predictions, pharmacogenomic mappings, safety signals, or causal estimators into autonomous clinical decisions. Study-specific clinical, causal, privacy, governance, and external-validation review remains required.

## 1. Pipeline at a glance

```text
source systems / files
        |
        v
inspect unknown source
        |
        v
review schema mapping + vocabulary + units
        |
        v
canonical contract validation
        |
        v
cleaning + missingness + temporal QA + harmonisation
        |
        +-------------------+--------------------+------------------+
        |                   |                    |                  |
        v                   v                    v                  v
 medication / claims     PGx / precision     NLP / phenotypes   FHIR / SDOH
        |                   |                    |                  |
        +-------------------+--------------------+------------------+
                            |
                            v
                 index date / eligibility / cohort
                            |
                            v
                baseline + follow-up windows
                            |
                            v
                  endpoint / outcome construction
                            |
                            v
                    analysis dataset
                            |
                            v
              patient/site/time-aware splitting
                            |
                            v
                    leakage safety gate
                            |
             +--------------+----------------+------------------+
             |              |                |                  |
             v              v                v                  v
         prediction      survival         causal            safety /
                                                         utilization /
                                                          economics
             |              |                |                  |
             +--------------+----------------+------------------+
                            |
                            v
                calibration / uncertainty /
                 subgroup / site validation
                            |
                            v
                 publication tables / figures
                            |
                            v
          study spec + fingerprints + run manifest
                            |
                            v
               checksummed research bundle
                            |
                            v
                  manuscript / archive handoff
```

The pipeline is intentionally **reviewable rather than fully automatic**. Automation handles structure, consistency, provenance, and repeatable computation. It does not silently approve clinical semantics.

---

## 2. Install and verify the platform

thomaslab-core requires Python **3.10 or newer**.

```bash
git clone https://github.com/appsplorer/thomaslab-core.git
cd thomaslab-core

python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows PowerShell
# .venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -e ".[dev,docs,notebooks]"
```

Verify the package:

```bash
python - <<'PY'
import thomaslab
print(thomaslab.__version__)
print(len(thomaslab.__all__), "public modules")
PY

pytest -q
mkdocs build --strict
```

Optional model stacks are installed separately when required:

```bash
python -m pip install -e ".[models]"
python -m pip install -e ".[llm]"
python -m pip install -e ".[gpu]"
```

Keep production credentials and protected health information outside the repository.

---

## 3. Recommended study workspace

A practical study can keep source-specific decisions separate from reusable package code:

```text
my-study/
├── configs/
│   ├── study.yaml
│   ├── model.yaml
│   └── analysis.yaml
├── adapters/
│   └── site_a/
│       ├── schema.yaml
│       └── contract.yaml
├── codesets/
│   ├── exposure.yaml
│   ├── outcomes.yaml
│   └── exclusions.yaml
├── notebooks/
│   └── exploratory/
├── scripts/
│   ├── 01_onboard.py
│   ├── 02_cohort.py
│   ├── 03_analysis.py
│   └── 04_report.py
├── outputs/
│   ├── tables/
│   ├── figures/
│   └── research_bundle/
└── README.md
```

Do not commit PHI, access tokens, private keys, database passwords, or identifiable genomic data.

---

## 4. Freeze the research intent first

Before primary analysis, create a study specification. The stable v1 structure requires:

- `study_id`
- `title`
- `version`
- `design`
- `data.datasets`
- `analysis.primary`
- `reproducibility.seed`

Example:

```yaml
study_id: cvd-example
title: Cardiovascular outcomes example
version: "1.0"

design:
  type: observational

data:
  datasets:
    - name: site_a
      domain: person

analysis:
  primary:
    name: descriptive

reproducibility:
  seed: 2026
```

Validate and freeze it:

```python
from thomaslab.study_spec import (
    freeze_study_spec,
    study_fingerprint,
    validate_study_spec,
)

report = validate_study_spec("configs/study.yaml", strict=True)
print(report)

print("study fingerprint:", study_fingerprint("configs/study.yaml"))

freeze_study_spec(
    "configs/study.yaml",
    "outputs/frozen_study.yaml",
    overwrite=True,
)
```

A fingerprint proves identity of the specification; it does **not** prove that the study design is scientifically valid.

See [Reproducible research workflow](guides/reproducible-research-workflow.md).

---

## 5. Onboard a completely new dataset

For an unfamiliar hospital, registry, claims, vendor, or collaborator dataset, use `thomaslab.onboard`.

```python
from thomaslab.onboard import DatasetOnboarder

ob = DatasetOnboarder("partner_hospital.csv")
inspection = ob.inspect()

print(inspection["profile"]["columns"])
print(inspection["semantics"])
print(inspection["domain_ranking"])
```

Generate a review bundle:

```python
bundle = ob.generate(
    "work/adapters/site_a",
    dataset_name="site_a_pci",
    required_columns=["patient_id", "age", "event_date"],
)
```

This produces reviewable schema and contract files. Resolve ambiguous mappings before strict validation:

```python
result = ob.validate(
    required_columns=["patient_id", "age", "event_date"],
    strict=True,
)
```

After review, freeze the adapter:

```python
ob.freeze(
    "adapters",
    dataset_name="site_a_pci",
    version="1",
)
```

Important boundaries:

- code-shape recognition is not authoritative vocabulary identification;
- unit occurrence is not permission to perform an automatic clinical conversion;
- fuzzy column matching is intentionally conservative;
- a changed source schema should receive a new adapter version.

See [New dataset onboarding](guides/new-dataset-onboarding.md) and [Schema adapters](guides/schema-adapters.md).

---

## 6. Standardize the source schema

When the mapping has already been reviewed:

```python
import pandas as pd

from thomaslab.data import standardize_schema

raw = pd.read_csv("partner_hospital.csv")

canonical, audit = standardize_schema(
    raw,
    mapping="adapters/site_a/schema.yaml",
    required_columns=["patient_id", "age", "event_date"],
    return_report=True,
)
```

Explicit YAML mappings override automatic matching.

Schema standardization changes names and structure. It does not establish:

- that a timestamp is the correct clinical index date;
- that units are comparable;
- that an ICD/NDC/RxNorm/LOINC field uses the claimed vocabulary;
- that variables were observed before time zero;
- that two sites measured the same construct equivalently.

---

## 7. Validate canonical data contracts

Use domain contracts before modeling.

```python
from thomaslab.contracts import validate_domain_contract

contract_report = validate_domain_contract(
    canonical,
    "contracts/person.yaml",
    strict=True,
)

assert contract_report["valid"]
```

Contract validation can check required columns, parseability, duplicate columns, and configured uniqueness constraints. Clinical correctness remains a separate review.

For multiple domain tables, use cross-domain key auditing to confirm patient coverage and key consistency.

See [Canonical contracts](api/contracts.md).

---

## 8. Clean, profile, and audit data quality

Run data-quality checks before feature engineering.

```python
from thomaslab.quality import generate_data_quality_report

quality = generate_data_quality_report(
    canonical,
    required_columns=["patient_id", "index_date", "age"],
    column_types={
        "patient_id": "string",
        "index_date": "datetime",
        "age": "numeric",
    },
    numeric_ranges={"age": (18, 120)},
    duplicate_key=["patient_id", "index_date"],
    index_date_col="index_date",
    feature_date_cols=["last_lab_date", "last_medication_date"],
)
```

Review separately:

| QA domain | What to inspect |
|---|---|
| Schema | missing required fields, duplicate columns, unexpected types |
| Missingness | overall and by site/time |
| Ranges | protocol-defined numeric plausibility |
| Duplicates | patient/event key duplication |
| Units | analyte-specific compatibility |
| Codes | vocabulary provenance and version |
| Temporal logic | feature dates relative to time zero |
| Site shift | distribution and missingness differences |

Do not use universal physiologic thresholds without checking units and study context.

See [Clinical data quality](guides/data-quality.md), [Missing data & temporal EHR](guides/missing-temporal.md), and [Multi-site harmonisation & code sets](guides/multisite-codes.md).

---

## 9. Make time zero explicit

The study timeline should be frozen before baseline feature engineering:

```text
eligibility lookback         baseline window       index                 follow-up
<--------------------------><-------------------->|-------------------------------->
                                                  t0
```

Typical order:

1. resolve patient identity using the approved strategy;
2. define `t0` from the protocol;
3. apply eligibility and exclusions with explicit temporal scope;
4. construct baseline covariates using allowed pre-index information;
5. define exposure/treatment assignment;
6. start outcome surveillance;
7. censor according to the protocol.

For baseline labs, aggregate only after the patient-specific index date is known.

See [End-to-end EHR workflow](guides/ehr-workflow.md).

---

## 10. Construct clinical domains

The platform has several domain-specific lanes. A study may use one or combine several.

### Medication and claims

Use the drug, claims, target-trial, and pharmacoepidemiology layers for exposure episodes, adherence, new-user cohorts, active comparators, switching, follow-up, and negative-control scaffolding.

Recommended path:

```text
reviewed drug mappings
→ exposure episodes
→ washout / eligibility
→ new-user index
→ treatment assignment
→ ITT-like and/or protocol-defined as-treated follow-up
→ switching/discontinuation audit
→ causal/safety analysis
```

See [Medication exposure & claims](guides/medication-claims.md) and [Target-trial pharmacoepidemiology](guides/target-trial.md).

### Pharmacogenomics and precision medicine

Use gene-specific PGx layers where available. Keep assay coverage, allele function, diplotype/phenotype interpretation, phenoconversion, and guideline-concordance as separate provenance-bearing steps.

Unsupported or ambiguous diplotypes should remain explicit rather than being guessed.

See [PGx foundation](guides/pgx-foundation.md), [Pharmacogenomics](guides/pgx.md), and [Precision medicine & registries](guides/precision-registry.md).

### Clinical NLP and phenotyping

For note-derived phenotypes:

```text
raw notes
→ cleaning
→ section/context processing
→ target entity / medication / phenotype extraction
→ negation / uncertainty / temporality
→ annotation sample
→ independent adjudication / validation
→ structured phenotype evidence
```

The text cleaner is **not** a de-identification engine. Validate production phenotypes against independently annotated data.

See [Clinical NLP](guides/clinical-nlp.md), [Advanced clinical NLP](guides/advanced-clinical-nlp.md), [Annotation & adjudication](guides/annotation-adjudication.md), and [Phenotype & endpoint registry](guides/phenotype-endpoints.md).

### FHIR and interoperability

Use the interoperability layer to validate/extract research data from supported FHIR Bundles. FHIR structural compatibility does not guarantee research-semantic equivalence.

See [FHIR interoperability](guides/fhir.md).

### Social determinants of health

Use governed area-level linkage with explicit provenance. Geographic enrichment can create privacy and fairness risks, so linkage and interpretation should remain protocol controlled.

See [Governed SDOH enrichment](guides/sdoh-enrichment.md).

---

## 11. Build endpoints and outcomes

Outcome construction should be versioned and separated from modeling.

Available research layers include cardiovascular composites, bleeding classification, structured/NLP phenotypes, medication safety events, survival endpoints, recurrent outcomes, resource utilization, and economic outcomes.

For a versioned phenotype:

```text
reviewed definition
→ structured event matching
→ contextual NLP evidence when appropriate
→ composite rule
→ first qualifying endpoint
→ adjudication / validation
→ frozen phenotype version
```

Do not optimize outcome definitions against model performance.

---

## 12. Build the analysis dataset

Use explicit windows and index alignment.

```python
from thomaslab.dataset import (
    apply_lookback_window,
    create_time_to_event_dataset,
)

baseline = apply_lookback_window(
    events,
    index,
    lookback_days=365,
)

survival = create_time_to_event_dataset(
    index,
    outcomes,
    fixed_followup_days=365,
)
```

Recommended structure:

```text
canonical domain tables
→ cohort/index
→ baseline window
→ follow-up window
→ outcome table
→ patient-level analysis table
→ split assignment
→ leakage audit
→ analysis
```

See [Study dataset & splitting](guides/dataset-splitting.md).

---

## 13. Split before model development

Repeated rows from one patient should not cross development and validation partitions.

Select the split that matches the study design:

| Goal | Typical helper |
|---|---|
| Patient-disjoint holdout | `patient_level_split` |
| Family/provider/group disjoint | `grouped_split` |
| Prospective-style temporal validation | `temporal_split` |
| Site transportability test | `site_holdout_split` |
| Stratified grouped split | `stratified_group_split` |
| Group-aware cross-validation | `grouped_cv_folds` |
| Independent evaluation source | `external_validation_split` |

A site holdout is a design feature, not automatic proof of external validity.

---

## 14. Run the leakage safety gate

Leakage control belongs before modeling.

Maintain feature-window metadata:

| feature | window_start_days | window_end_days |
|---|---:|---:|
| age | 0 | 0 |
| creatinine_latest | -30 | 0 |
| post_bleed_hgb | 1 | 7 |

Then audit:

```python
from thomaslab.leakage import audit_dataset_leakage

audit_dataset_leakage(
    dataset,
    target_col="outcome",
    feature_cols=features,
    split_col="split",
    feature_metadata=feature_metadata,
    strict=True,
)
```

Strict review should block documented post-index features, direct target leakage, patient overlap, and required site-disjoint violations.

See [Leakage protection](guides/leakage-protection.md).

---

## 15. Choose the analysis lane

The full pipeline branches after the analysis dataset is frozen.

### Prediction and machine learning

Use `thomaslab.models`, `thomaslab.eval`, and `thomaslab.validation`.

A minimum evaluation package should include:

```text
discrimination
+ calibration
+ uncertainty
+ subgroup audit
+ site/external validation when available
+ decision-curve analysis when clinically meaningful
+ explanation only as model-behavior analysis
```

SHAP describes model behavior; it does not establish causal effects.

See [Longitudinal & deep models](guides/deep-models.md), [Evaluation & fairness](guides/evaluation.md), and [Site & external validation](guides/external-validation.md).

### Survival and recurrent outcomes

Use survival, competing-risk, recurrent-event, and censoring/IPCW layers.

See [Advanced survival & competing risks](guides/advanced-survival.md) and [Recurrent events & censoring](guides/recurrent-censoring.md).

### Standard causal analysis

Use the causal and causal-workflow layers for propensity, overlap, balance, weighting, and doubly robust effect estimation when the study assumptions support those methods.

See [Causal inference](guides/causal-inference.md) and [Epidemiology & causal workflows](guides/causal-epi-workflow.md).

### Longitudinal causal inference

The platform provides three complementary longitudinal g-method families:

```text
IPTW / marginal structural models
parametric g-formula
longitudinal doubly robust / AIPW
```

Triangulation can be useful, but agreement between estimators is not proof of causal validity.

See [Longitudinal causal inference](guides/longitudinal-causal.md), [Parametric g-formula](guides/gformula.md), and [Longitudinal doubly robust inference](guides/longitudinal-dr.md).

### Robustness and falsification

Use quantitative bias analysis, E-values, negative controls, calibration, overlap sensitivity, and influence diagnostics as sensitivity evidence rather than as a causal-validity score.

See [Causal robustness and falsification](guides/causal-robustness.md).

### Transportability and multisite generalizability

Use source-to-target sampling models, target standardization, transport AIPW, site-specific effects, heterogeneity, and leave-one-site-out analysis.

A covariate-only external target can support transport modeling, but does not itself provide external outcome validation.

See [Causal transportability](guides/transportability.md).

### Heterogeneous treatment effects

Use cross-fitted T-/S-/DR-learners, held-out calibration, subgroup/site stability, bootstrap model variability, and research-policy evaluation.

Patient-level CATE estimates are not autonomous treatment recommendations.

See [Heterogeneous treatment effects](guides/heterogeneous-effects.md).

### Multiple treatments

For three or more mutually exclusive strategies, use multinomial propensity, generalized overlap, multi-arm AIPW, pairwise effects, reference-arm DR learning, and research-policy evaluation.

See [Multi-treatment comparative effectiveness](guides/multi-treatment.md).

### Quasi-experimental studies

Available guarded methods include instrumental variables/2SLS, canonical two-period DiD, local-linear regression discontinuity, and interrupted time series.

Identification arguments must come from the study design, not from the estimator name.

See [Quasi-experimental causal research](guides/quasi-experimental.md).

### Staggered treatment adoption

Use cohort-time effects, not-yet-treated/never-treated controls, event-time aggregation, pre-period placebo screens, bootstrap uncertainty, and timing sensitivity.

See [Staggered-adoption event studies](guides/staggered-did.md).

### Causal mediation

Use the mediation layer for guarded interventional direct/indirect/total effect analogues, temporal auditing, bootstrap uncertainty, and mediator sensitivity.

Temporal ordering and measured support do not prove sequential exchangeability.

See [Causal mediation](guides/causal-mediation.md).

### Drug safety and medication surveillance

Use exposure-event windows, background windows, dechallenge/rechallenge timelines, denominator-based safety summaries, and separate spontaneous-report disproportionality where appropriate.

A safety signal is not a causal conclusion.

See [Drug safety & medication surveillance](guides/drug-safety-surveillance.md) and [Self-controlled medication safety](guides/self-controlled-safety.md).

### Healthcare utilization and economics

Use the HCRU and economics layers for encounter episodes, readmission timing, utilization summaries, observed costs, utilities, and QALY-style research endpoints.

See [Healthcare utilization & economics](guides/hcru-economics.md).

---

## 16. Evaluate prediction performance

For binary prediction:

```python
from thomaslab.eval import (
    calculate_clinical_metrics,
    compute_calibration,
)

metrics = calculate_clinical_metrics(
    y_true,
    y_pred_prob,
    threshold=0.5,
)

calibration = compute_calibration(
    y_true,
    y_pred_prob,
    n_bins=10,
)
```

Report both discrimination and calibration.

For decision-curve analysis:

```python
from thomaslab.eval import decision_curve_analysis

dca = decision_curve_analysis(y_true, y_pred_prob)
```

For group auditing:

```python
from thomaslab.eval import audit_fairness

by_group = audit_fairness(
    predictions,
    y_true_col="outcome",
    y_pred_prob_col="risk",
    demographic_col="race",
)
```

Group comparisons are an audit, not a single fairness verdict.

---

## 17. Validate across sites and independent sources

Use site-level reporting before claiming generalizability.

`site_validation_report()` provides pooled and site-specific prediction metrics without ranking sites.

`external_validation_report()` labels an evaluation cohort as an external-source evaluation only when the caller explicitly records that design assertion.

Use bootstrap intervals where appropriate and interpret site differences alongside sample size, prevalence, case mix, measurement process, and data-generation differences.

See [Site & external validation](guides/external-validation.md).

---

## 18. Build publication outputs

Use the visualization layer after analysis is frozen.

Examples include:

- Table 1;
- ROC and precision-recall curves;
- calibration plots;
- Kaplan-Meier plots;
- competing-risk cumulative incidence;
- treatment pathway Sankey diagrams;
- subgroup forest plots.

Example Table 1:

```python
from thomaslab.viz import generate_table_one

text = generate_table_one(
    cohort,
    group_col="treatment",
    categorical_cols=["sex", "diabetes"],
    continuous_cols=["age", "egfr"],
)

print(text)
```

For propensity analyses, Table 1 p-values are not a substitute for covariate-balance diagnostics.

See [Publication reporting](guides/reporting.md).

---

## 19. Capture provenance and deterministic execution

The reproducibility layer supports:

- deterministic mapping/file/dataframe fingerprints;
- Python/NumPy/optional PyTorch seed setup;
- selected runtime/package capture;
- run manifests;
- input fingerprint verification;
- cross-table contract validation.

Use a single declared study seed, then derive named child seeds for folds, bootstrap runs, or model families.

A deterministic seed improves reproducibility but does not guarantee bitwise-identical results across every library, operating system, hardware, or accelerator stack.

See [Reproducibility API](api/reproducibility.md).

---

## 20. Export the final checksummed research bundle

The standard bundle contains:

```text
research_bundle/
├── tables/
│   └── *.csv
├── metadata/
│   ├── study_spec.yaml
│   ├── run_manifest.json
│   └── bundle_metadata.json
├── bundle_manifest.json
└── checksums.sha256
```

Every declared payload receives a SHA-256 checksum.

Verify before handoff or archival:

```python
from thomaslab.research_bundle import verify_research_bundle

verification = verify_research_bundle(
    "research_bundle",
    strict_unexpected=True,
)

assert verification["valid"]
```

The bundle records provenance and artifact identity. It does **not** provide a de-identification guarantee.

---

## 21. Stable integrated workflow

For the stable contract/provenance/export path, use `run_integrated_research_workflow()`.

```python
from pathlib import Path

import pandas as pd

from thomaslab.integrated_workflow import run_integrated_research_workflow

patients = pd.DataFrame(
    {
        "patient_id": [1, 2, 3],
        "age": [55, 61, 70],
        "sex": ["F", "M", "F"],
    }
)

study = {
    "study_id": "example-v1-study",
    "title": "Example v1 study",
    "version": "1.0",
    "design": {"type": "observational"},
    "data": {"datasets": [{"name": "patients", "domain": "person"}]},
    "analysis": {"primary": {"name": "descriptive"}},
    "reproducibility": {"seed": 2026},
}

contract = {
    "dataset_name": "patients",
    "domain": "person",
    "required_columns": ["patient_id"],
    "columns": ["patient_id", "age", "sex"],
    "dtypes": {},
    "datetime_columns": [],
    "numeric_columns": ["age"],
    "unique_keys": ["patient_id"],
    "column_roles": {},
    "units": {},
    "vocabularies": {},
}

result = run_integrated_research_workflow(
    patients,
    Path("research_bundle"),
    study_spec=study,
    dataset_name="patients",
    contract=contract,
    strict=True,
)

assert result["contract_report"]["valid"]
assert result["bundle_verification"]["valid"]
```

This integrated function covers the stable infrastructure path:

```text
study-spec validation
→ deterministic seed
→ optional caller-supplied schema mapping
→ source/canonical contract validation
→ optional result-table contract validation
→ dataset profiling
→ input fingerprinting
→ run-manifest creation
→ research-bundle export
→ checksum verification
```

It deliberately does **not** select a statistical model, infer a causal design, approve clinical semantics, or decide whether a result is publishable.

---

## 22. Full module map

| Research responsibility | Primary modules |
|---|---|
| Data loading / canonical schema | `data`, `onboard`, `contracts`, `cleaning` |
| Missingness / temporal QA | `missing`, `temporal`, `quality` |
| Harmonisation / terminology | `harmonize`, `codes` |
| Medication / claims | `drugs`, `claims`, `target_trial`, `pharmacoepi` |
| Drug safety | `drug_safety`, `surveillance`, `self_controlled` |
| Longitudinal causal | `longitudinal_causal`, `gformula`, `longitudinal_dr` |
| Causal robustness | `causal_robustness` |
| Transportability | `transportability` |
| Heterogeneous effects | `heterogeneous_effects` |
| Multi-treatment effects | `multi_treatment` |
| Quasi-experimental designs | `quasi_experimental` |
| Staggered adoption | `staggered_did` |
| Mediation | `causal_mediation` |
| PGx | `pgx`, `pgx_core`, `pgx_cyp2c19`, `pgx_cyp2d6`, `pgx_assay`, `pgx_phenoconversion`, `pgx_guidelines` |
| Precision medicine / registries | `precision`, `registry`, `implementation` |
| Phenotypes / endpoints | `phenotypes`, `cardiovascular`, `bleeding` |
| Clinical NLP | `nlp`, `nlp_context`, `nlp_medications`, `nlp_phenotypes`, `annotation` |
| Dataset construction / splitting | `dataset`, `splits`, `leakage` |
| Epidemiology / causal | `epi`, `causal`, `causal_workflows` |
| Prediction validation | `eval`, `validation` |
| Survival | `survival`, `recurrent`, `censoring` |
| PK/PD / platelet | `pkpd`, `platelet` |
| SDOH | `sdoh` |
| HCRU / economics | `hcru`, `economics` |
| Interoperability | `interop` |
| Visualization / reporting | `viz` |
| Study specifications | `study_spec` |
| Provenance | `reproducibility` |
| Research bundles | `research_bundle` |
| Integrated orchestration | `integrated_workflow` |
| Release validation | `release` |

The complete callable API is documented under [API reference](api/index.md).

---

## 23. Guided notebook route

For collaborators who prefer notebooks, the numbered notebooks form a progressive path.

A practical route for a new EHR project is:

```text
01 data check
→ 06 schema adapter
→ 07 new dataset onboarding
→ 08 missing/temporal QA
→ 09 multisite harmonisation
→ 20 study dataset builder
→ 21 split/leakage audit
→ study-specific analysis notebook(s)
→ 23 external validation
→ 56 reproducible study bundle
→ 57 integrated workflow
→ 58 v1 self-service reference
```

Specialized notebooks cover claims, PGx, phenotypes, NLP, target trials, drug safety, longitudinal causal inference, transportability, HTE, multi-treatment analysis, quasi-experimental methods, staggered DiD, and mediation.

See [Guided notebooks](guides/nontechnical-notebooks.md).

---

## 24. Quality gates before manuscript freeze

A manuscript analysis should not be frozen until the relevant gates pass.

| Gate | Required evidence |
|---|---|
| Source mapping | reviewed adapter / source dictionary |
| Structural validity | contract validation passes |
| Clinical semantics | units, vocabularies, time variables reviewed |
| Cohort design | eligibility, exclusions, time zero, follow-up frozen |
| Leakage | patient/site/time/feature-window audit passes |
| Missingness | strategy declared and sensitivity considered |
| Modeling | train/validation separation preserved |
| Calibration | reported when prediction probabilities are used |
| Uncertainty | confidence intervals / bootstrap design documented |
| Causal design | assumptions and diagnostics documented |
| External validation | independence/design assertion stated explicitly |
| Fairness / subgroup | sample sizes and uncertainty reported |
| Reproducibility | version, commit, seed, fingerprints recorded |
| Export integrity | research-bundle checksum verification passes |
| Privacy | no PHI or restricted data committed to Git |

---

## 25. CI and release pipeline

The stable repository CI checks more than unit tests.

```text
pull request
  |
  +--> install package
  +--> compile source/tests/scripts
  +--> validate notebook JSON
  +--> stable release QA
  +--> targeted correctness lint
  +--> execute stable workflow notebooks
  +--> build wheel + source distribution
  +--> install built wheel
  +--> import every declared public module
  +--> pip dependency check
  +--> complete pytest suite
  +--> Python 3.10 compatibility build/tests

main documentation change
  |
  +--> install documentation dependencies
  +--> mkdocs build --strict
  +--> upload built-site artifact
  +--> publish generated site to gh-pages
  +--> native GitHub Pages deployment when repository Pages is enabled
```

The v1 public-module baseline is recorded in `api_compatibility.yaml`. Planned removals must be recorded in `deprecations.yaml`.

See [API stability & versioning](reference/api-stability.md) and [v1 release checklist](reference/release-checklist.md).

---

## 26. Documentation deployment

Documentation is written in `docs/` and built with Material for MkDocs.

Local preview:

```bash
python -m pip install -e ".[docs]"
mkdocs serve
```

Strict build:

```bash
mkdocs build --strict
```

The GitHub documentation workflow publishes the generated site to the `gh-pages` branch whenever documentation changes are merged to `main`. The workflow also verifies that `site/full-pipeline/index.html` exists before publishing and confirms the remote `gh-pages` branch after deployment.

The configured documentation URL is:

```text
https://appsplorer.github.io/thomaslab-core/
```

The repository is private, so enabling browser-served GitHub Pages is a one-time repository setting: **Settings → Pages → Build and deployment → Deploy from a branch → `gh-pages` → `/(root)`**. Whether a private-repository Pages site can be exposed depends on the GitHub account/plan. The generated site itself is already versioned and deployed in the repository's `gh-pages` branch.

---

## 27. What the platform deliberately does not do

thomaslab-core does not:

- infer clinical meaning from a column name and silently treat it as truth;
- guarantee that source data are de-identified;
- choose a causal design automatically;
- make unsupported causal claims from association;
- convert safety signals into adverse-drug causal attribution;
- convert CATEs or model-selected treatments into autonomous patient recommendations;
- treat SHAP as causal explanation;
- treat non-significant pre-trends as proof of parallel trends;
- treat overlap diagnostics as proof of positivity;
- treat external-source labels as proof of transportability;
- silently guess unsupported PGx diplotypes;
- replace annotation/adjudication for clinical NLP validation;
- make manuscript-level scientific judgments automatically.

Those boundaries are part of the platform's research-quality design.

---

## 28. Recommended path for a new study

For most new studies, start with this sequence:

```text
1. write study.yaml
2. inspect source
3. review/freeze schema adapter
4. validate contracts
5. run data-quality + temporal QA
6. define time zero and cohort
7. build outcomes
8. build analysis dataset
9. assign patient/site/time-aware splits
10. run strict leakage audit
11. run the protocol-selected analysis
12. evaluate calibration/uncertainty/site performance
13. generate tables/figures
14. capture fingerprints + run manifest
15. export research bundle
16. verify checksums
17. archive exact commit + environment + study specification
```

If a step is scientifically inappropriate for the study, omit it explicitly rather than forcing the study into a generic template.

---

## 29. Where to go next

Use this page as the pipeline map, then move into the specialized guide for the study component you are implementing. The [API reference](api/index.md) provides callable-level documentation generated from source docstrings, while the [research-use reference](reference/research-use.md) and [clinical assumptions reference](reference/clinical-assumptions.md) define the interpretation boundaries that should remain visible throughout the project.

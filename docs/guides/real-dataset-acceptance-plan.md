# Healthcare dataset integration — saved feedback and acceptance plan

**Feedback captured:** 24 October 2026.  
**Decision:** CONDITIONAL GO for continued development; **NOT READY** for unrestricted researcher or clinical use.  
**Primary tracking issue:** [Core #35](https://github.com/appsplorer/thomaslab-core/issues/35).  
**Related:** draft Core PR #34, public handbook PR #31, scientific acceptance #33, Actions runner #28.  
**Original 283-line feedback:** preserved verbatim in the **private** Core hardening branch at `audits/2026-10-24-healthcare-research-platform-feedback-original.md`. The public site contains only this reviewed implementation plan, not restricted data or private code.

This is a **persistent backlog and test design**. A checkbox can be closed only with inspectable evidence from the **exact tested software SHA** and the relevant authorizing institution. A new function's presence, synthetic PASS, docs build, or an earlier unrelated HPC result does not establish scientific acceptance. Retain every failed/blocked result in the evidence trail.

## Status definitions and dependency gates

- **CODE CANDIDATE:** implementation or synthetic tests exist; no current exact-SHA acceptance recorded.
- **NEEDS IMPLEMENTATION:** material functionality remains to be designed or implemented.
- **AWAITING APPROVED DATA:** real-source tests cannot begin until appropriate study and data approvals exist.
- **AWAITING INDEPENDENT REVIEW:** results need named scientific, clinical, statistical or security sign-off.
- **ACCEPTED FOR A NAMED STUDY:** all five relevant gates below are evidenced for an explicitly identified source/release, cohort, research question and approved environment. Never extend this claim automatically to other sources.

| Acceptance gate | Objective completion evidence |
|---|---|
| **SOFTWARE_PASS** | Installation in a clean supported environment, current-source-SHA pytest/coverage/Ruff/mypy/package/notebooks; HPC/CPU and GPU when actually required, archived failure diagnostics, dependency provenance |
| **STRUCTURAL_PASS** | Steward-reviewed dictionary, release/version, unique-grain/nullable-key validation, tested joins, units, vocabulary mappings, timestamps, drift, real-source scale and error cases |
| **SCIENTIFIC_PASS** | Prespecified research question, target population and time zero, clinician-approved labels, leakage/censoring checks, independent gold standard, suitable baselines and honest holdouts |
| **GOVERNANCE_APPROVED** | PI/data-owner decisions, DUA/IRB/HRPP where required, named accounts, approved storage/compute/egress and complete applicable small-count/privacy review |
| **RESEARCHER_USABLE** | Independent researchers successfully complete the documented supported workflow and can recognize unsupported or unsafe scenarios |

**Never call the platform universally leakage-free or compatible with every dataset.** Each new site, source version, analysis or clinical use needs its own evidence. All metrics and reports must obey their originating data-use and disclosure policies.

## A. Work to implement or audit **before** restricted datasets are available

- [ ] **P0 · Exact-commit Core QA:** investigate current GitHub Actions failures, obtain useful diagnostic logs or run independent clean-environment/HPC acceptance; archive each stage and SHA; do not merge draft Core PR solely because docs pass.
- [ ] **P0 · Separate MIMIC-IV-Note adapter:** define version-pinned `discharge`, `discharge_detail`, `radiology`, `radiology_detail` contracts, optional encounter links, addenda, versioning and note provenance without assuming admission-time notes exist.
- [ ] **P0 · Note information-time safety:** distinguish event time, charting, storage/availability time, annotation date and baseline clinical decision time. Block discharge/retrospective note information from pre-treatment model features.
- [ ] **P0 · Note extraction/annotation tests:** invented negation, uncertainty, deidentification placeholders `___`, medication start/stop/restart and dose, allergies, historical/current status, evidence spans, contradictory sections and addenda; define expert adjudication protocol.
- [ ] **P0 · Governance and leakage contracts:** block off-platform All of Us participant-level exports/linkage, require explicit source provenance, reviewed code/units/time mappings, train-only preprocessing and appropriate outcome follow-up.
- [ ] **P1 · MIMIC-IV structural work:** improve approved CSV.gz/SQL streaming, schema drift, corrupt/large inputs, admission/ICU keys, dictionary and unit checks, shifted dates, age anchors, medication orders versus administrations and longitudinal cohort requirements.
- [ ] **P1 · All of Us Workbench packaging:** prepare *non-executing* version-aware, allowlisted and parameterized OMOP query plans, dependency compatibility checks, vocabulary/descendant plans and controlled/registered domain contracts, using synthetic fixtures outside the Workbench.
- [ ] **P1 · Hospital EHR mapping:** build explicit optional/required column contracts, alternate mappings, local code provenance, lab units, clinical timezone, site-specific linkage, source drift and a named clinical-review checkpoint.
- [ ] **P1 · Three complete synthetic reference workflows:** (1) MIMIC readmission and medication timeline; (2) All of Us PGx feasibility only, avoiding unsupported genotype/clinical inference; (3) unfamiliar hospital EHR onboarding. Each should produce safe cohort flow, study-spec, limitations and reproducibility report.
- [ ] **P1 · Independent usability protocol:** preregister tasks, stopping rules, user errors and acceptance thresholds for five researchers with differing technical backgrounds.
- [ ] **P1 · Source-independent research acceptance protocol:** preregister 15–20 truly unseen datasets with expert gold mappings, performance/accuracy thresholds and fail-closed unsupported-design behavior.
- [ ] **P1 · Publication and ownership:** agree with PI/institution on private software ownership, public study-code release when legally required, citation, maintainer responsibility, and contribution/authorship records; never include credentialed data in Git.

## B. Tests **after the relevant approved dataset/access becomes available**

### MIMIC-IV v3.1 structured hospital and ICU

**Dependency:** credentialed PhysioNet access, required agreements/training and locally approved compute/storage. Real data must not enter this chat or public repositories.

- [ ] Verify source files, release and manifest fingerprints, actual table/column names, null patterns, encoding and input scale against the documented schema.
- [ ] Independently test `subject_id`, `hadm_id`, `stay_id` relationships, repeated stay rows, optional FKs, transferred patients, ICU dictionary integrity and shifted-time comparisons.
- [ ] Review ICD version/leading zeros, labs/results/units, actual medication order/pharmacy/eMAR/detail semantics, `Not Given`, dose/timing uncertainties and missing documentation.
- [ ] Run readmission/cohort baseline with clinician-adjudicated eligibility and follow-up, patient/temporal/site split checks, missing outcome capture and a transparent methods report.

### MIMIC-IV-Note (independent credentialed notes dataset)

**Dependency:** permission covering this separate notes release and approved *local/no-egress* NLP processing; review third-party model restrictions independently.

- [ ] Verify `discharge`, `discharge_detail`, `radiology`, `radiology_detail` schemas, notes IDs, charting/storage timestamps, section/addenda behavior and nullable links against the actual authorized release.
- [ ] Establish a clinician-approved annotation sample for negation, temporality, medications, bleed/contraindication and evidence spans; preserve deidentification placeholders.
- [ ] Compare transparent rules, classical NLP and permitted compact/local LLMs on independent patient splits, extraction F1, calibration, temporal accuracy, runtime/cost and real downstream study impact.
- [ ] Demonstrate **no post-decision note leakage** using data availability, not just dates mentioned inside note text; explicitly report questions these notes cannot answer.

### All of Us Registered/Controlled CDR

**Dependency:** user's actual Workbench eligibility, completed required training, named workspace and permissions for the exact release/tier. The user reports this access process is underway, **not approved yet**.

- [ ] Confirm current Workbench CDR and table version rather than assuming `v9` forever; verify in-Workbench dependencies and identity-authorized parameterized SQL with cost/timeout and schema-drift checks.
- [ ] Clinician-review OMOP source/standard concepts and descendants, observation periods, drug-era uncertainty, encounter gaps and prespecified cohort inclusion/exclusion.
- [ ] Validate `PMI_SKIP`, survey response/selection effects, Fitbit device/daily missingness, duplication and available provenance.
- [ ] For permitted genomics only: inspect modality/QC/reference build, sample coverage, CYP2C19 allele/phase and provenance. **Missing genotype is not a verified normal-metabolizer phenotype.**
- [ ] Review complete aggregate report—including figures, complementary cells, percentages and derivable counts—against current All of Us rules. Generic bundle export and participant-level transfer outside Workbench remain prohibited absent the programme's explicit authorized route.

### Independent hospital EHR / claims

**Dependency:** site steward's approval, data dictionary, IRB/DUA/HRPP decisions and approved institution-managed environment.

- [ ] Review effective data grain, privacy tier, local MRN/site linkage, timestamps and time zones, vocabulary versions, drug order/dispense/administration, units, missing values and cross-institution follow-up.
- [ ] Conduct blinded gold mapping and phenotype/outcome adjudication; test drift, leakage, claims enrollment continuity, censoring, fairness and explicit unsupported-study blocking.
- [ ] Document each accepted site separately—never equate successful synthetics with validated unseen hospital systems.

## C. Evidence pack to retain per authorized run

The investigator/authorized compute environment should retain a restricted manifest containing:

`run_id`, `git_sha`, `package_version`, `environment_id`,
`approved_source_id`, `source_release`, `data_fingerprint`,
`approval_or_dua_reference`, `approved_storage`, `adapter_version`,
`mapping_reviewer`, `study_spec_sha256`, `time_zero_definition`,
`feature_availability_contract`, `heldout_design`, `cohort_attrition`,
`test_results`, `failed_checks`, `methods_reviewer`,
`disclosure_reviewer`, and the five gate decisions.

Store actual identifiers and sensitive evidentiary details **only in the authorized enclave**, never in public documentation or ChatGPT. Share externally only source-safe code, synthetic reproductions, public dictionaries and programme/institution-permitted, disclosure-reviewed aggregates. A reported PASS must be traceable to that exact commit and approved dataset context.

## D. Feedback delivery milestones — planning targets, not promises

| Target date in 24 Oct feedback | Intended deliverable | Dependency |
|---|---|---|
| **31 Oct 2026** | Diagnose Core PR #34 current-HEAD failures and full technical acceptance | Hosted runner restoration or approved independent QA |
| **15 Nov 2026** | Dedicated MIMIC-IV-Note source adapter and synthetic/negative tests | Official public documentation; code review |
| **30 Nov 2026** | Authorized MIMIC/Workbench integration evidence where available | Credentials, data agreements, actual permitted workspace |
| **15 Dec 2026** | Three end-to-end studies and reproducible methods/limitation reports | Source-specific studies may remain synthetic if permissions pending |
| **31 Dec 2026** | Researcher-ready beta decision with signed software/scientific/governance/usability gates | Independent reviewers, five user trials and representative permitted data |

These dates come from the submitted audit and should be **replanned when access, data availability or scientific verification makes a target infeasible**. The core safety and scientific gate criteria must not be weakened to meet a calendar deadline.

## E. What counts as finished?

- [ ] Supported dataset versions and workflows are declared accurately; unsupported uses stop with an actionable explanation.
- [ ] No critical software test failures or unapproved data transfers are hidden or waived.
- [ ] Clinically reviewed reference outputs are reproduced on approved source data without invalid linkage, hindsight features or inappropriate negative outcome labels.
- [ ] Independent researchers can install, execute, inspect and report a prespecified analysis within their permitted environments.
- [ ] Only source-specific, independently reviewed scientific claims are made; publication remains a separate investigator and institutional decision.

**All checkboxes intentionally remain open** until evidence is available. The existing candidate modules and prior tests are useful implementation progress, not final acceptance. Related findings remain tracked in Core issues #28, #33 and #35.

# S37–S41 — Synthetic research-readiness workflows (P5-04 to P5-08)

**Engineering status: synthetic candidate only; requirements P5-04–P5-08 remain OPEN pending external evidence.** No protected MIMIC-IV, All of Us or hospital records were opened. No real researchers were enrolled, 15–20 real unfamiliar datasets inspected, clinical outcomes verified, hospital approvals obtained, DOI minted or data published. A caller-provided `SYNTHETIC` flag does not prove de-identification.

## S37 · Three source-shaped end-to-end examples

`thomaslab.adaptive.synthetic_research_journeys` provides `run_all_invented_journeys()` plus `run_invented_research_journey(profile=...)` for `MIMIC_IV_SHAPED`, `ALL_OF_US_OMOP_SHAPED`, and `HOSPITAL_EHR_SHAPED`. These create **invented** identifiers, visit links and lab-event rows, reconcile source-like columns to a deliberately **OMOP-like** canonical target, check join completeness, unit allowlists and pre-index result availability, and return only a deterministic review report. Deliberate join, timing and unit errors must BLOCK. 

`run_invented_safety_gate(profile=...)` feeds generated cohort, lab and coverage intervals into the **actual pre-existing S30 study safety module**, validating time-zero, result availability and site-local continuity. This is original Core integration, not a substitute for actual OMOP 5.4 conformance or a clinically reviewed phenotype. Three ready-to-open notebooks are in `notebooks/ehr_readiness/`.

MIMIC-IV documentation identifies hospital (`hosp`) and ICU (`icu`) modules and their table grains; source-shaped labels are **not** legitimate source data or a licensed MIMIC fixture. PhysioNet's current credentialed terms and DUA must be followed before any actual access: https://mimic.mit.edu/docs/iv/ and https://physionet.org/content/mimiciv/3.1/.

All of Us uses OMOP-harmonized EHR within its **Researcher Workbench**; real person-level records must not be fetched/processed by this generic example. Actual published/distributed participant counts of **1–20 are prohibited**, including inferable complementary cells; this framework makes no claim that an ordinary `>=11` threshold suffices: https://researchallofus.org/data-tools/data-access/ and https://researchallofus.org/data-tools/workbench/.

## S38 · Five independent researcher usability trial protocol

`thomaslab.adaptive.researcher_usability.build_usability_trial_protocol()` creates five independent participant slots, each assigned five tasks: source selection, schema interpretation, mapping review, phenotype review, and safe-result interpretation. Use the blank protocol worksheet/template in the accompanying configs to obtain appropriate institutional review, recruit five **actual independent** researchers, record consent, tasks, timing and assistance in approved storage, and obtain independent observer attestation. `assess_synthetic_usability_rehearsal()` accepts exactly 5×5 **invented** task observations for a software rehearsal, produces only aggregate statistics, and **never** claims the human trial occurred. Identity/consent files do not belong in the repository.

## S39 · 15–20 unfamiliar dataset validation protocol

`thomaslab.adaptive.unseen_dataset_benchmark.generate_invented_holdout_families(size=20)` generates 15–20 bounded synthetic schema variations, including unknown vocabulary and alias ambiguity. `evaluate_invented_mapping_benchmark()` deterministically checks abstention/review behavior and schema fingerprinting. Its programmatically generated oracle is NOT a clinician-approved gold standard or an independent real-world held-out test. Actual P5-06 acceptance requires at least 15–20 **independently collected and permissioned** unfamiliar datasets, a preregistered sampling plan, clinicians independently annotating gold mappings blind to model predictions, per-source mapping precision/recall/calibration, adjudication disagreement, leakage checks, performance stratification and immutable evidence IDs. Never reclassify synthetic oracle scores as clinical accuracy.

## S40 · Governance, privacy and scientific source acceptance

`thomaslab.adaptive.research_acceptance` pins source type, project and release digest against ten required gates: rights, IRB/exemption, DUA/purpose, vocabulary license, independent privacy review, clinician-approved mappings, reproducibility, IAM/egress, retention/audit and release/disclosure. The API accepts only restricted metadata review refs, validates structure, and **always BLOCKS** actual access/release even when all ten refs are supplied. A separate institution-operated signature/verifier service is mandatory; no caller flags can self-approve. Source-specific All of Us, PhysioNet, hospital DUA and IRB policies remain primary.

## S41 · FAIR draft catalog and citation infrastructure

`thomaslab.adaptive.fair_release_catalog` builds a deterministic schema.org `Dataset` / `SoftwareSourceCode` **draft** with creator references, versioned source SHA, provenance, controlled license reference and citation text. It deliberately leaves persistent identifier, verified license and public access blank. Restricted metadata never inherits an open-content license. FAIR (Findable/Accessible/Interoperable/Reusable) does **not** mean publication of patient records. Institution-approved metadata release, actual source rights, DataCite DOI minting (if selected), long-term metadata hosting, retention/deletion, citation ownership, dataset versioning and a publication checklist still require human/governance workflows. See https://www.gofair.foundation/fair-principles.

## Local candidate tests and HPC boundary

```bash
python -m pytest -q tests/test_s37_s41_readiness.py
```

If running **outside the actual Core checkout**, four real S30 integration tests will fail import rather than silently use stubs. Only report the number of cases *actually executed*. In the same candidate checkout, no GPU/Slurm job should be submitted until all requirements are implemented and the organization approves the acceptance environment.

**Release boundary:** S37–S41 are synthetic software implementations and review frameworks. P5-05/06/07 cannot be fully completed until genuine external human, dataset and institutional evidence is obtained. All five requirement statuses remain OPEN. Neither proof of privacy nor clinical validity can be manufactured by JSON hashes or passing synthetic tests.

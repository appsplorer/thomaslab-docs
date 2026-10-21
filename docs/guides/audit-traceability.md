# Thomas Lab platform audit: requirements, evidence and limits

This checklist links the original lab-wide audit to the implemented interfaces
and the evidence still required before unrestricted deployment. The audit was
initially written against `main` at `d7b88c4`; assess the **current feature
commit and its tests** before applying an older finding. These are engineering
capabilities and acceptance gates, not a claim that external validation or
institutional authorization has already happened.

## Six original safety findings

| Finding | Current software route | Verification and qualification |
| --- | --- | --- |
| Sample-only checks could miss errors beyond row 5,000 | `thomaslab.adaptive.full_validation.validate_entire_source` and `DatasetOnboarder.validate(full_dataset=True)` | Regression fixtures place invalid data beyond the preview boundary. Approval requires zero skipped records; unsupported formats fail closed. |
| Adapter approval lacked successful full validation and named human review | `thomaslab.adaptive.adapter_registry.AdapterRegistry` and `DatasetOnboarder.freeze` | Approval tests deny sample-only, unreviewed and invalid sources. Independent clinical review still belongs to the lab. |
| CSV/TSV identifiers could lose leading zeros | `thomaslab.adaptive.source.load_source_raw`, `thomaslab.easy.load_clinical_table` | Leading-zero identifiers and medication-code regression tests. Numerically stored Excel identifiers **cannot be restored** from lost source formatting. |
| Schema regeneration could overwrite reviewed YAML | `thomaslab.data.generate_schema_template` and the draft bundle generator | Exclusive creation; choose a new version or revision rather than overwriting reviewed files. |
| Beginner binary prediction could leak patients between splits | `thomaslab.easy.quick_binary_model` and Notebook 03 | Explicit appropriate split; patient overlap checks; aggregate-only output; invalid numeric predictors block fitting. A defensible observational study still requires protocol review. |
| Notebook controls were inadequately exercised | `scripts/notebook_smoke.py`, `thomaslab.adaptive.notebook_acceptance`, notebook callback tests | Forty advanced/demo synthetic method callbacks and blocking paths are exercised. The original 19 legacy notebooks are registered; selected beginner and onboarding buttons have direct synthetic click tests. Notebook 07 now blocks unauthorized file inspection and stale source reuse. All 19 have **not** been certified through an independent live usability study. |

## Five architecture layers

| Layer | Implemented entry point | What is not automatically granted |
| --- | --- | --- |
| Visual mapping review | Notebook 07; `MappingWorkbench` with source names, ranked alternatives, redacted samples, units and review status | A suggestion is not a validated clinical mapping. |
| Versioned adapter registry | `AdapterRegistry`, reviewer and full-source records, drift checks | Approval at one institution does not authorize pooling at another. |
| Guided analysis templates | Notebook controllers and descriptive, binary, survival templates | Advanced specialist or causal modes are gated; synthetic demos are not arbitrary patient-dataset execution. |
| Scientific validation reports | Separate software/data/study-method assessments | Execution never means publication approval. A domain expert must review assumptions. |
| Governed execution and exports | `ExecutionPolicy`, `GovernedNotebookSession`, governed bundle exporter | Python policy checks cannot create institutional storage ACLs, accounts, an IRB decision or guaranteed de-identification. Legacy raw exporters remain expert-only. |

## Input families and acceptance evidence

| Family | Software capability | Independent source/semantic acceptance |
| --- | --- | --- |
| CSV/TSV/Parquet; single-sheet `.xlsx` | Bounded preview and full-source validation where supported | Requires independently reviewed mapping and data-integrity checks for each dataset. Older `.xls` and multi-sheet workflows need explicit approved conversion. |
| EHR and clinical registry | Adaptation contracts and reviewed cohort settings | Site-specific clinical definitions, units, dates, identifier grain and reference outcomes: **pending**. |
| Medication claims | Drug and cohort modules with review gates | Vocabulary, enrollment and exposure semantics: **pending**. |
| PGx | Assay/guideline checks and supported modules | Laboratory assay coverage and relevant dated guidelines: **pending**. |
| Multi-hospital | Site adapters and explicit pooled-use policy | Permissions and independent harmonization review: **pending**. |
| FHIR bundles and notes | Bounded extraction/annotation interfaces | Broader resources, reference integrity and external phenotype gold standard: **partial; do not imply general support**. |
| Advanced causal analysis | Specialist modules and guided preflight restrictions | Expert design, identification, time-zero and sensitivity review: **required for each study**. |
| Large files | Streaming/complete-source validation and portable synthetic scale benchmark | Multiple formats, realistic peak memory, HPC permissions and reproducible million-row performance: **not independently established**. |

## External rollout evidence that software cannot supply

1. **15–20 genuinely independent unseen datasets:** not completed; ten
   synthetic fixture families are software-test coverage, not 15–20 sources.
   Record data-use rights, golden mappings, source integrity and each failure
   in the versioned benchmark manifest, without placing patient rows in Git.
2. **Five independent non-technical researchers:** not completed; use the
   [usability protocol](researcher-usability-protocol.md) and record assistance,
   errors, completion time and decisions, not just registered widgets.
3. **Institutional patient data:** permission from the institution/PI,
   IRB/DUA as applicable, approved compute/storage, group-based access,
   auditing and disclosure policy must be checked independently. Kaggle is
   only for legitimately public/synthetic sources.
4. **Publication-quality methods:** named study-specific clinical/statistical
   reviewers must validate definitions and assumptions; no automatic label
   of `publication_ready` is authoritative.

## Local review checklist before GitBook sync

From the **same checkout and interpreter** that researchers will use:

```bash
python -m pip install -e ".[dev,docs,notebooks]"
python scripts/generate_gitbook_docs.py --check
python scripts/docs_coverage_audit.py
python scripts/local_quality_gate.py
python scripts/benchmark_validation_scale.py --rows 100000 --chunk-rows 5000 --output results/synthetic-scale-new-run.json
```

Run the benchmark with a fresh output filename, record the Git SHA and
actual command logs, and report any missing dependency or failing test.
`local_quality_gate.py` has a quick option for development but only the full
gate can support a candidate release. The [release criteria](lab-validation-release-criteria.md)
explain the separate software, dataset and scientific decisions.

GitBook uses the repository-root `gitbook-docs.yaml` to import `./docs`.
`SUMMARY.md` is the navigation source. The `docs/api` MkDocs directives are
not executable GitBook content; use the complete generated function reference
instead. Changes to the draft GitHub feature branch will not enter a GitBook
space configured to sync `main` until the pull request is merged.

# Complete function reference

This self-service reference is generated from the public Python source surface.

**Stable baseline:** 69 modules, 571 documented callables  
**Candidate additions:** 13 module references and 54 callable signatures (Core PR #34; not yet accepted)

Every callable includes purpose, use guidance, full signature, parameter meanings, input contract, output guidance, raises/fail-closed behavior, research guardrails, a synthetic implementation template, related functions/workflows, verification links, and source documentation.

For end-to-end implementations, use the [self-service cookbook](../../examples/self-service-cookbook.md).

## Modules

| Module | Public callables |
|---|---:|
| [`thomaslab.annotation`](annotation.md) | 11 |
| [`thomaslab.bleeding`](bleeding.md) | 6 |
| [`thomaslab.cardiovascular`](cardiovascular.md) | 4 |
| [`thomaslab.causal`](causal.md) | 10 |
| [`thomaslab.causal_mediation`](causal_mediation.md) | 8 |
| [`thomaslab.causal_robustness`](causal_robustness.md) | 10 |
| [`thomaslab.causal_workflows`](causal_workflows.md) | 10 |
| [`thomaslab.censoring`](censoring.md) | 6 |
| [`thomaslab.claims`](claims.md) | 8 |
| [`thomaslab.cleaning`](cleaning.md) | 18 |
| [`thomaslab.codes`](codes.md) | 10 |
| [`thomaslab.contracts`](contracts.md) | 7 |
| [`thomaslab.data`](data.md) | 19 |
| [`thomaslab.dataset`](dataset.md) | 14 |
| [`thomaslab.drug_safety`](drug_safety.md) | 8 |
| [`thomaslab.drugs`](drugs.md) | 15 |
| [`thomaslab.easy`](easy.md) | 9 |
| [`thomaslab.economics`](economics.md) | 10 |
| [`thomaslab.epi`](epi.md) | 9 |
| [`thomaslab.eval`](eval.md) | 8 |
| [`thomaslab.gformula`](gformula.md) | 8 |
| [`thomaslab.harmonize`](harmonize.md) | 9 |
| [`thomaslab.hcru`](hcru.md) | 7 |
| [`thomaslab.heterogeneous_effects`](heterogeneous_effects.md) | 13 |
| [`thomaslab.implementation`](implementation.md) | 13 |
| [`thomaslab.integrated_workflow`](integrated_workflow.md) | 1 |
| [`thomaslab.interop`](interop.md) | 4 |
| [`thomaslab.leakage`](leakage.md) | 11 |
| [`thomaslab.longitudinal_causal`](longitudinal_causal.md) | 12 |
| [`thomaslab.longitudinal_dr`](longitudinal_dr.md) | 5 |
| [`thomaslab.missing`](missing.md) | 11 |
| [`thomaslab.models`](models.md) | 3 |
| [`thomaslab.multi_treatment`](multi_treatment.md) | 12 |
| [`thomaslab.nlp`](nlp.md) | 7 |
| [`thomaslab.nlp_context`](nlp_context.md) | 6 |
| [`thomaslab.nlp_medications`](nlp_medications.md) | 4 |
| [`thomaslab.nlp_phenotypes`](nlp_phenotypes.md) | 8 |
| [`thomaslab.onboard`](onboard.md) | 13 |
| [`thomaslab.pgx`](pgx.md) | 7 |
| [`thomaslab.pgx_assay`](pgx_assay.md) | 5 |
| [`thomaslab.pgx_core`](pgx_core.md) | 6 |
| [`thomaslab.pgx_cyp2c19`](pgx_cyp2c19.md) | 5 |
| [`thomaslab.pgx_cyp2d6`](pgx_cyp2d6.md) | 5 |
| [`thomaslab.pgx_guidelines`](pgx_guidelines.md) | 3 |
| [`thomaslab.pgx_phenoconversion`](pgx_phenoconversion.md) | 5 |
| [`thomaslab.pharmacoepi`](pharmacoepi.md) | 6 |
| [`thomaslab.phenotypes`](phenotypes.md) | 10 |
| [`thomaslab.pkpd`](pkpd.md) | 9 |
| [`thomaslab.platelet`](platelet.md) | 6 |
| [`thomaslab.precision`](precision.md) | 8 |
| [`thomaslab.quality`](quality.md) | 7 |
| [`thomaslab.quasi_experimental`](quasi_experimental.md) | 9 |
| [`thomaslab.recurrent`](recurrent.md) | 6 |
| [`thomaslab.registry`](registry.md) | 9 |
| [`thomaslab.release`](release.md) | 8 |
| [`thomaslab.reproducibility`](reproducibility.md) | 13 |
| [`thomaslab.research_bundle`](research_bundle.md) | 4 |
| [`thomaslab.sdoh`](sdoh.md) | 7 |
| [`thomaslab.self_controlled`](self_controlled.md) | 11 |
| [`thomaslab.splits`](splits.md) | 8 |
| [`thomaslab.staggered_did`](staggered_did.md) | 8 |
| [`thomaslab.study_spec`](study_spec.md) | 6 |
| [`thomaslab.surveillance`](surveillance.md) | 6 |
| [`thomaslab.survival`](survival.md) | 7 |
| [`thomaslab.target_trial`](target_trial.md) | 11 |
| [`thomaslab.temporal`](temporal.md) | 8 |
| [`thomaslab.transportability`](transportability.md) | 9 |
| [`thomaslab.validation`](validation.md) | 5 |
| [`thomaslab.viz`](viz.md) | 7 |

## Candidate clinical dataset and disclosure modules

**Not an accepted v1 release:** The entries below document public signatures from the current private Core PR #34; all three source families remain synthetic-only candidates pending exact-SHA tests, authorizations and independent scientific validation.

| Source-aware module | Documented callables |
|---|---:|
| [`thomaslab.healthcare_sources`](healthcare_sources.md) | 5 |
| [`thomaslab.healthcare_foundation`](healthcare_foundation.md) | 8 |
| [`thomaslab.healthcare_omop`](healthcare_omop.md) | 4 |
| [`thomaslab.healthcare_aou_domains`](healthcare_aou_domains.md) | 3 |
| [`thomaslab.healthcare_aou_query`](healthcare_aou_query.md) | 1 |
| [`thomaslab.healthcare_mimic`](healthcare_mimic.md) | 9 |
| [`thomaslab.healthcare_hospital`](healthcare_hospital.md) | 5 |
| [`thomaslab.healthcare_cohorts`](healthcare_cohorts.md) | 3 |
| [`thomaslab.healthcare_quality`](healthcare_quality.md) | 5 |
| [`thomaslab.adaptive.aou_disclosure`](aou_disclosure.md) | 1 |
| [`thomaslab.clinical_leakage`](clinical_leakage.md) | 5 |
| [`thomaslab.clinical_followup`](clinical_followup.md) | 3 |
| [`thomaslab.adaptive.schema_discovery`](schema_discovery.md) | 2 |

See also [All of Us disclosure restrictions](../../guides/aou-disclosure.md) and [dataset methods](../../guides/clinical-dataset-methods.md).

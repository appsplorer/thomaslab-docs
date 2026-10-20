# Causal mediation and treatment-mechanism research

Version 0.29 adds a guarded causal-mediation layer for studies that ask whether a treatment or exposure may operate through an intermediate variable.

The implementation emphasizes transparent assumptions and standardized interventional analogues. It does not convert an observational association into a verified biological mechanism.

## Scope

The primary workflow uses a binary treatment, one mediator at a time, continuous or binary mediators, continuous or binary outcomes, and analyst-declared pre-treatment covariates.

validate_mediation_inputs() checks structural requirements, treatment-arm support, variable roles, finite numeric data, and binary coding where requested.

validate_mediation_temporality() audits the required exposure → mediator → outcome ordering from explicit timestamps. A clean temporal audit is necessary for many mediation designs but is not sufficient for causal identification.

## Parametric interventional mediation

fit_interventional_mediation() fits:

1. a mediator model conditional on treatment and baseline covariates; and
2. an outcome model conditional on treatment, mediator, baseline covariates, and optionally a treatment×mediator interaction.

It then standardizes over the observed baseline-covariate distribution using Monte Carlo g-computation.

For treatment A, mediator M, and outcome Y, the reported additive decomposition is:

- total effect: E[Y(1,M(1))] - E[Y(0,M(0))];
- interventional direct analogue: E[Y(1,M(0))] - E[Y(0,M(0))];
- interventional indirect analogue: E[Y(1,M(1))] - E[Y(1,M(0))].

For binary outcomes the scale is risk difference. For continuous outcomes the scale is mean difference.

The software intentionally labels these outputs as interventional mediation analogues. It does not silently claim natural direct/indirect-effect identification or cross-world assumptions that cannot be checked from the observed data.

## Identification diagnostics

mediation_design_diagnostics() reports measured treatment-support information and can embed the temporal audit.

It also explicitly records that the following cannot be verified from the observed table alone:

- sequential exchangeability;
- absence of unmeasured mediator-outcome confounding; and
- cross-world independence assumptions.

Support diagnostics are therefore diagnostics, not causal-validity scores.

## Bootstrap inference

bootstrap_mediation_effects() refits the complete mediation analysis after row-level or cluster-level resampling.

It returns percentile confidence intervals, bootstrap standard errors, requested/successful replicate counts, and the success fraction.

Cluster resampling should be used when the study sampling unit requires it. Bootstrap uncertainty remains conditional on the fitted models and identifying assumptions.

## Mediator sensitivity analysis

mediator_shift_sensitivity() perturbs the treated continuous-mediator distribution by analyst-specified residual-standard-deviation shifts and reruns the mediation standardization.

This is useful for examining sensitivity to mediator-model/distribution assumptions. It is explicitly not an adjustment for unmeasured mediator-outcome confounding and should not be described as one.

## Multiple mediators

analyze_multiple_mediators() produces a research table by applying the same guarded single-mediator analysis to several prespecified mediators.

The output is not a joint multiple-mediator decomposition, does not identify path-specific effects, and does not account for causal dependence among mediators. It is an auditable screening/comparison table for separately specified mediator analyses.

## Recommended workflow

1. Define treatment, mediator, outcome, time zero, and baseline covariates before fitting models.
2. Confirm covariates are pre-treatment and clinically/research justified.
3. Audit exposure→mediator→outcome timing with actual study timestamps.
4. Review treatment support and any structural positivity concerns.
5. Fit the primary mediation model with the treatment×mediator interaction choice prespecified.
6. Inspect the direct, indirect, and total effects on the declared scale.
7. Use cluster bootstrap when the design requires patient/site-level resampling.
8. Run mediator-model/distribution sensitivity analyses that correspond to plausible scientific uncertainty.
9. Treat separate multiple-mediator analyses as separate analyses, not a path decomposition.
10. Report untestable assumptions and avoid unsupported biological-mechanism or clinical-treatment claims.

The package supports reproducible mediation estimation and assumption auditing. Scientific mechanism claims require substantive study design, measurement validity, and identification arguments beyond the software output.

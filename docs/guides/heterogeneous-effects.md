# Heterogeneous treatment effects and research-policy evaluation

Version 0.25 adds a dedicated heterogeneous treatment-effect (HTE) layer for observational research.

The central estimand is the conditional average treatment effect (CATE) on the outcome-difference scale:

[
	au(x)=E[Y(1)-Y(0)mid X=x].
]

For a binary adverse outcome, a negative CATE means the modeled treatment strategy reduces event risk at that covariate profile. For an outcome where larger values are desirable, the direction reverses. The software therefore never assumes that a numerically larger CATE is clinically preferable.

## Required design assumptions

HTE estimation does not relax the assumptions needed for average causal effects. Causal interpretation still requires, among other conditions:

- a well-defined treatment intervention;
- consistency;
- treatment exchangeability conditional on the declared baseline covariates;
- adequate treatment positivity;
- correct temporal ordering;
- adequate nuisance and effect-model estimation; and
- no use of post-treatment variables as HTE covariates.

The package cannot establish these conditions from data alone.

## Input validation

validate_hte_inputs() requires one analysis row per unit, binary treatment, a supported outcome type, and an explicit list of pre-treatment covariates.

Treatment and outcome columns cannot be included as HTE covariates.

## Cross-fitted T-learner

fit_t_learner() fits separate source outcome regressions for treated and control observations inside each training fold.

For held-out observation i:

[
hat	au_i=hat m_1(X_i)-hat m_0(X_i).
]

The same held-out fold also receives:

- raw and clipped treatment propensity;
- treated outcome regression;
- control outcome regression; and
- a doubly robust pseudo-outcome.

This allows the CATE ranking to be evaluated without comparing predictions directly with the observed outcome, which is not an individual treatment effect.

## Cross-fitted S-learner

fit_s_learner() fits one outcome model using both baseline covariates and treatment as inputs.

For each held-out observation, the fitted outcome model is evaluated twice:

[
hat m(X_i,A=1),qquad hat m(X_i,A=0).
]

Their difference is the S-learner CATE estimate.

The default S-learner uses a random forest so treatment-covariate interactions can be represented without requiring the analyst to manually specify every interaction term. A linear option remains available for transparent sensitivity analyses.

## Nested cross-fitted DR-learner

fit_dr_learner() uses a stronger nested design.

Within each outer training sample, treatment propensity and treatment-arm outcome models are themselves cross-fitted to create doubly robust pseudo-outcomes:

[
phi_i =
hat m_1(X_i)-hat m_0(X_i)
+rac{A_i(Y_i-hat m_1(X_i))}{hat e(X_i)}
-rac{(1-A_i)(Y_i-hat m_0(X_i))}{1-hat e(X_i)}.
]

A second-stage regression then learns (E[phimid X]).

The resulting CATE prediction for each outer test row comes from an effect model that did not train on that row.

This nested structure is intentionally more conservative than fitting a second-stage effect model directly to in-sample nuisance pseudo-outcomes.

## Predicting CATEs in new populations

predict_cate() applies the final fitted T-, S-, or DR-learner bundle to a new covariate table.

For the T- and S-learners it also returns modeled treatment-specific outcomes.

For the DR-learner the final second-stage model directly predicts the CATE; treatment-specific outcome predictions are therefore left missing rather than fabricated.

## Treatment-effect calibration

treatment_effect_calibration() compares held-out CATE predictions with held-out doubly robust pseudo-outcomes.

It reports:

- calibration intercept;
- calibration slope;
- prediction/pseudo-outcome correlation; and
- quantile-bin summaries of mean predicted CATE versus mean DR pseudo-outcome.

The pseudo-outcome is noisy and estimated. A calibration slope near one does not prove that patient-level effects are correct, and a poor slope does not identify the specific source of misspecification.

## Prespecified subgroup stability

subgroup_cate_summary() summarizes HTE predictions and DR pseudo-outcomes within analyst-declared subgroups.

It deliberately does not rank subgroup levels.

Variables with excessive numbers of unique levels fail closed. Analysts should first define scientifically meaningful grouped variables rather than allowing arbitrary high-cardinality subgroup fishing.

## Qini-style doubly robust gain curve

dr_gain_curve() ranks rows by predicted treatment benefit and evaluates cumulative doubly robust benefit pseudo-outcomes.

Because outcome direction is study-specific, higher_outcome_better must be supplied explicitly.

The returned area is a Qini-style observational ranking diagnostic. It is not equivalent to randomized uplift validation.

## Research-policy construction

derive_research_policy() converts a held-out CATE prediction into an exploratory binary treatment rule using:

- explicit outcome-benefit direction; and
- an explicit minimum modeled benefit threshold.

The function is intended for methodological evaluation. It is not a prescribing engine.

## Doubly robust research-policy evaluation

evaluate_research_policy() estimates the outcome under an explicit binary research policy using held-out outcome and propensity nuisances.

It also compares the research policy with treat-all and treat-none strategies on the same modeled outcome scale.

When higher outcomes are desirable, utility equals the modeled outcome. When lower outcomes are desirable, utility is the negative modeled outcome.

The function records whether the analyst asserts that policy decisions were generated honestly or out of fold. If not, the result is labeled as potentially optimistically biased.

Even an out-of-fold policy value remains an observational causal estimate and must not be converted directly into patient care recommendations.

## Bootstrap CATE variability

bootstrap_cate_uncertainty() resamples the training data, refits the selected HTE learner, and predicts the target rows repeatedly.

It returns percentile intervals for each target row.

These intervals quantify model/data resampling variability. They are explicitly labeled:

bootstrap_model_variability_not_individual_causal_confidence_interval

They should not be described as definitive patient-specific causal confidence intervals.

## Site-specific CATE stability

site_cate_stability_report() reports, without ranking sites:

- site sample size;
- mean and SD of held-out predicted CATE;
- mean DR pseudo-outcome;
- pseudo-outcome standard error; and
- within-site prediction/pseudo calibration intercept and slope.

This helps reveal whether apparent treatment-effect heterogeneity is stable across data-generating environments.

Differences can arise from real effect modification, case mix, treatment policies, measurement, outcome definitions, support, or model misspecification.

## Transporting the modeled CATE distribution

transport_cate_distribution() integrates the v0.25 HTE layer with the v0.24 transportability layer.

It predicts CATEs in source and external target covariate populations, fits source-versus-target sampling weights, and compares:

- unweighted source mean CATE;
- sampling-weighted source mean CATE; and
- directly modeled target mean CATE.

The target may be covariate-only.

This is a transport diagnostic for the fitted CATE model. It is not external validation of the true patient-level causal effect when target treatment/outcomes are unavailable.

## Recommended workflow

A publication-oriented workflow is:

1. define the target trial or causal contrast before HTE modeling;
2. freeze baseline covariates and exclude all post-treatment features;
3. establish average-effect overlap and nuisance diagnostics;
4. fit cross-fitted T- and S-learners as transparent sensitivity models;
5. fit the nested DR-learner;
6. inspect treatment-effect calibration against held-out DR pseudo-outcomes;
7. inspect prespecified subgroup summaries;
8. inspect site stability;
9. bootstrap model variability;
10. evaluate any exploratory treatment rule honestly/out of fold;
11. inspect the doubly robust gain curve;
12. transport the CATE distribution to external covariate populations when scientifically justified;
13. report estimator disagreement and uncertainty rather than selecting the most favorable subgroup or learner.

The output is research evidence about effect heterogeneity, not autonomous clinical decision support.

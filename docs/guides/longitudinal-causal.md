# Longitudinal causal inference and dynamic strategies

Version 0.20 extends the target-trial and censoring layers to longitudinal treatment decisions, time-varying confounding, marginal structural models (MSMs), and cloning-censoring-weighting scaffolding.

## Why a separate longitudinal layer?

Ordinary baseline propensity-score methods are not sufficient when treatment can change over time and a time-varying covariate both predicts future treatment and is itself affected by earlier treatment. This module keeps the treatment process, censoring process, outcome process, and temporal ordering visible instead of hiding them in a single black-box model.

## Person-period construction

Use build_person_period_dataset() to divide follow-up into discrete intervals. The final interval is shortened at the first observed outcome or censoring date, and no later rows are created.

After merging time-varying covariates and treatment status, run validate_person_period_panel() before fitting any weight model. add_lagged_history() can create explicitly named prior-treatment/prior-covariate variables.

Only variables available before the treatment decision at period t should enter a treatment model for period t.

## Stabilized longitudinal weights

estimate_stabilized_treatment_weights() fits pooled logistic treatment models and returns both numerator and denominator probabilities for the observed treatment.

estimate_stabilized_censoring_weights() separately models remaining under observation. The two processes stay separate so reviewers can inspect each model before they are multiplied.

combine_longitudinal_weights() can multiply treatment and censoring weights and optionally truncate empirical tails. The untruncated value is always retained.

Weight truncation is not a repair for a broken design. Report the chosen thresholds and rerun defensible alternative truncation levels as sensitivity analyses.

## Positivity and weight diagnostics

longitudinal_positivity_diagnostics() reports treatment prevalence and fitted probability tails at every period. A period containing only one treatment level is explicitly flagged.

weight_diagnostics() reports the weight distribution and effective sample size overall and by time.

Large or highly unstable weights should trigger design/model review rather than automatic acceptance of a weighted estimate.

## Marginal structural model

fit_weighted_pooled_logistic_msm() fits a weighted pooled-logistic model with patient-clustered standard errors. The fitted parameters are MSM parameters under the supplied weights.

A causal interpretation still requires the study's assumptions: consistency, appropriate treatment versions, sequential exchangeability, positivity, adequate temporal measurement, and appropriate treatment/censoring models.

## Cloning-censoring-weighting

build_clone_censor_dataset() duplicates every patient into each prespecified strategy and artificially censors a clone at its first deviation.

Strategies may be:
- static, such as always treated or never treated;
- time-indexed mappings; or
- dynamic callables that use the current row.

Dynamic rules must use only information available at the current decision time. Future data must never enter a strategy rule.

audit_clone_censor_dataset() checks that each clone stops at its first artificial censoring event.

estimate_clone_censoring_weights() provides a reusable model for artificial-censoring weights, stratified by strategy.

## Required sensitivity work

For publication-quality longitudinal causal analyses, pre-specify and compare defensible alternatives for:
- treatment/censoring model specification;
- probability clipping;
- weight truncation;
- interval width;
- treatment grace periods;
- dynamic strategy definitions;
- baseline and time-varying covariate sets;
- missing-data handling; and
- outcome/censoring timing.

These utilities make the analysis auditable; they do not make observational data equivalent to randomization.

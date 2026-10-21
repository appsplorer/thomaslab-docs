# Causal transportability and multisite generalizability

Version 0.24 adds source-to-target causal-effect transport and multisite heterogeneity utilities.

## Source and target populations

The source population must contain baseline covariates, treatment, and outcome.

The target population only needs the baseline covariates used by the transport model. Treatment and outcomes are not required in the target table. This supports external target populations where only covariate information is available.

## Sampling / participation model

fit_sampling_odds_weights() estimates

[
P(S=1mid X)
]

where S=1 denotes the source cohort and S=0 denotes the target population.

For source observations, the default inverse-odds-of-sampling weight is

[
rac{1-P(S=1mid X)}{P(S=1mid X)}.
]

Optional stabilization changes only the overall scale.

The raw sampling probabilities are retained. Probability clipping is used only for numerical stability in weight construction.

## Transport positivity diagnostics

transport_positivity_diagnostics() reports:

- source-probability quantiles in source and target populations;
- fraction of target observations with low estimated source participation probability;
- sampling-weight range;
- 99th percentile weight;
- maximum weight; and
- Kish effective sample size.

Poor support is a transportability warning. It is not repaired merely by clipping a probability.

## Target standardization

estimate_target_standardization() fits treatment-arm-specific outcome models in the source and evaluates both potential-outcome predictions over the target covariate distribution.

For binary outcomes it reports:

- target standardized treated risk;
- target standardized control risk;
- risk difference; and
- risk ratio.

Target outcomes are not used.

## Cross-fitted transport AIPW

estimate_transport_aipw() performs fold-based nuisance estimation.

Within each fold:

1. the sampling model is fitted on pooled source and target training rows;
2. the treatment model is fitted only in source training rows;
3. treatment-arm outcome models are fitted only in source training rows;
4. nuisance predictions are produced on held-out source and target rows.

For treatment level a, the estimator combines the target mean of the source outcome regression with a source residual correction weighted by the target-to-source sampling odds and source treatment propensity.

The method therefore combines:

- target standardization;
- source treatment adjustment; and
- source-to-target sampling adjustment.

Successful estimation does not establish the identification assumptions. Causal transport requires, among other conditions, source treatment exchangeability, conditional exchangeability across populations given the chosen covariates, positivity in both treatment and sampling processes, consistency, and measurement comparability.

## Bootstrap uncertainty

bootstrap_transport_aipw() resamples source and target populations independently, refits all nuisance models, and reruns the transported estimator.

It returns the complete bootstrap draws and percentile intervals.

The bootstrap captures empirical sampling and nuisance refitting variation. It does not address unmeasured effect modifiers or violations of the transport assumptions.

## Site-specific causal contrasts

site_specific_causal_effects() fits the existing cross-fitted AIPW estimator separately within each site.

Sites without adequate treatment-arm support are retained with an explicit status rather than being silently dropped.

The output intentionally contains no site ranking.

## Heterogeneity and meta-analysis

meta_analyze_site_effects() supports fixed-effect or DerSimonian-Laird random-effects pooling.

It reports:

- pooled estimate;
- standard error and interval;
- Cochran Q;
- between-site variance tau-squared; and
- I-squared.

These statistics describe heterogeneity. They do not establish that site effects are exchangeable or that pooling is scientifically justified.

leave_one_site_out_meta_analysis() repeats the selected meta-analysis after excluding each site in turn.

This is a sensitivity analysis for pooled results, not a quality ranking of sites.

## Recommended workflow

For a transport study:

1. define the source and target populations before modeling;
2. justify the baseline covariates as treatment confounders and/or cross-population effect modifiers;
3. inspect source/target distributions and sampling positivity;
4. fit inverse-odds sampling weights;
5. run target standardization;
6. run transport AIPW;
7. bootstrap uncertainty;
8. compare source-only and transported estimands;
9. evaluate site-specific effects when multiple source sites exist;
10. inspect heterogeneity and leave-one-site-out sensitivity;
11. report explicitly that target outcomes were or were not available.

Transportability is an identification claim about populations and design, not a property created by successful software execution.

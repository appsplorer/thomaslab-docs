# Parametric g-formula and sequential g-computation

Version 0.21 adds a model-based longitudinal standardization layer that complements the v0.20 inverse-probability-weighting and marginal-structural-model workflows.

## Temporal contract

The g-formula engine uses the following row-level interpretation:

    L_t available at start of period t
        ↓
    assign or observe A_t
        ↓
    generate/model interval outcome Y_t
        ↓
    if event-free, generate L_(t+1)

This ordering is not inferred from column names. The study team must build the panel so the timing is scientifically correct.

A variable measured after treatment A_t must not be placed in L_t for the same treatment decision.

## Panel validation

validate_gformula_panel() checks:

- one row per patient-period;
- integer periods beginning at zero;
- contiguous observed follow-up;
- binary treatment and interval outcome;
- one absorbing event at most;
- no rows after the event;
- baseline covariates that remain constant within patient; and
- explicitly declared binary/continuous time-varying covariates.

Missing time-varying model inputs fail closed. The package does not silently impute them.

## Fitting the parametric g-formula

fit_parametric_gformula() fits two types of models.

The outcome model predicts the probability of Y_t from baseline covariates, current time-varying state L_t, current treatment A_t, and period.

For every declared time-varying covariate, a transition model predicts L_(t+1) from baseline history, current L_t, A_t, and period among event-free patients with an observed next period.

Binary state variables use logistic regression. Continuous state variables use linear regression with an empirical residual standard deviation for Monte Carlo draws.

This is a transparent default, not a claim that these parametric forms are correct for every study.

## Intervention simulation

simulate_gformula_regime() starts from the empirical baseline population and simulates trajectories under a prespecified strategy.

Strategies can be:

- static: always treat / never treat;
- period-indexed mappings; or
- dynamic callables based on the current simulated row.

Dynamic rules must use only information available at the current decision time.

The simulator generates the interval event first and only simulates the next covariate state among survivors. Once an event occurs, that simulated trajectory stops.

Simulation beyond the maximum observed follow-up period is blocked.

Optional continuous_bounds can constrain simulated continuous states when the study protocol provides scientifically justified limits. Bounds are not applied automatically because clipping itself is a modeling assumption.

## Regime risks and contrasts

summarize_regime_risk() calculates cumulative Monte Carlo risk over the chosen horizon.

simulate_regime_set() applies multiple prespecified regimes using common random-number seeds and compare_regime_risks() reports:

- regime-specific risk;
- reference risk;
- risk difference; and
- risk ratio when the reference risk is non-zero.

These estimates are identified causally only under the longitudinal g-formula assumptions.

## Bootstrap uncertainty

bootstrap_gformula_contrasts() resamples patients, refits every conditional model, reruns the intervention simulations, and returns the complete bootstrap draws plus percentile intervals.

The bootstrap addresses sampling and model-refitting variability. It does not account for unmeasured confounding, positivity violations, measurement error, incorrect temporal ordering, or structural model misspecification.

## Sensitivity analysis against v0.20 MSMs

The g-formula and IPTW/MSM approaches make different modeling choices. Agreement can therefore be informative as a sensitivity analysis.

compare_gformula_with_msm() deliberately refuses to treat different effect measures as numerically equivalent. For example, a g-formula cumulative risk ratio and a pooled-logistic MSM odds ratio are shown side by side with directly_comparable=False.

For a direct numerical estimator comparison, first standardize both analyses to the same population, horizon, treatment contrast, estimand, and effect scale.

## Required study-level sensitivity work

Publication-quality use should examine:

- alternate plausible outcome-model forms;
- alternate state-transition model forms;
- intervention definitions;
- follow-up horizon;
- Monte Carlo sample size;
- continuous-state bounds when scientifically justified;
- missing-data strategy;
- competing-event handling;
- positivity diagnostics from the observed treatment process;
- bootstrap size; and
- comparison with weighting-based estimates on a common estimand where possible.

The g-formula does not make observational data equivalent to randomization.

# Cross-fitted longitudinal doubly robust estimation

Version 0.22 adds a longitudinal augmented inverse-probability-weighted layer that complements the v0.20 weighting/MSM workflow and the v0.21 parametric g-formula.

## Temporal contract

The estimator assumes each row follows this order:

    pre-treatment history H_t
             |
             v
        treatment A_t
             |
             v
      interval event Y_t
             |
             v
    censoring / H_(t+1)

History variables supplied to the nuisance models must therefore be known before treatment in that period.

Dynamic strategy functions do not receive the observed current treatment, interval outcome, or censoring indicator. They receive only patient/time identifiers and the explicitly declared pre-treatment history variables.

## Panel validation

validate_sequential_dr_panel checks:

- one row per patient-period;
- integer, contiguous periods;
- entry at period zero;
- binary treatment and interval-event indicators;
- no rows after an absorbing event;
- no rows after explicit censoring;
- no simultaneous event and censoring on one row;
- complete declared pre-treatment history; and
- a requested horizon inside observed study support.

A patient ending before the requested horizon without an explicit censoring flag is treated as implicitly censored and is surfaced in the audit.

## Cross-fitting by patient

estimate_sequential_aipw_regime assigns folds at the patient level. All rows for one patient remain in the same fold.

Within each training fold, outcome regressions are fitted backwards through time. For event-free patients, the target at period t is the regime-specific Q prediction from period t+1. At an event row the target is one. At the completed horizon without an event the target is zero.

Held-out rows receive:

- a regime-specific Q prediction;
- a treatment propensity;
- a probability for the strategy-prescribed treatment;
- an uncensoring/continuation probability among event-free patients; and
- an out-of-fold sequential target when observed.

The analysis table preserves all of these quantities for review.

## Longitudinal AIPW influence contribution

For each patient, the estimator starts from the held-out baseline regime Q prediction and adds the longitudinal augmentation terms.

The augmentation weight accumulates:

- adherence to the prespecified treatment regime; and
- remaining observed when continued follow-up is required.

Raw treatment and censoring probabilities are retained for diagnostics. Only the probability used as an inverse-weight denominator is floored at the explicitly configured probability_clip threshold; probabilities near one are not reduced. Flooring does not relabel the underlying treatment or censoring process as having adequate positivity.

The final regime estimate is the average patient pseudo-outcome. The empirical variance of held-out influence contributions gives the reported standard error under the usual cross-fitting and regularity conditions.

Finite-sample AIPW estimates can fall outside the zero-to-one risk range. The software does not silently truncate the point estimate.

## Sequential outcome-regression component

Every regime result also reports sequential_regression_estimate.

This is the cross-fitted baseline mean of the backwards Q regressions before augmentation. It gives a transparent model-based component to compare with the doubly robust estimate.

It should not be interpreted as an independent confirmation because it shares the same outcome-regression specification.

## Censoring nuisance model

For event rows, the terminal outcome is already observed and no current-period censoring factor is required.

For event-free rows before the horizon, the censoring nuisance target indicates whether the next period is observed.

At the horizon, an event-free row is complete unless an explicit censoring indicator says otherwise.

This distinction prevents the event itself from being modeled as an uncensoring event.

## Diagnostics

audit_longitudinal_dr_nuisance reports, by period:

- treatment prevalence;
- held-out treatment Brier score;
- held-out sequential-Q target mean squared error;
- held-out event-free censoring Brier score;
- strategy-treatment probability tails;
- low-probability counts;
- censoring-probability support;
- maximum cumulative regime weight;
- effective sample size among positive-weight observations; and
- observed adherence to the regime.

A positivity warning is a design/model review signal, not an automatic correction.

## Multiple regimes and paired contrasts

estimate_regime_set_sequential_aipw uses identical patient folds across regimes.

This allows risk-difference uncertainty to use paired influence contributions.

For positive regime and reference risks, risk-ratio uncertainty is calculated on the log scale using paired influence values.

The output includes:

- regime risk;
- influence-curve standard error and interval;
- sequential-regression risk;
- reference risk;
- risk difference with paired standard error and interval; and
- risk ratio with log-scale standard error and interval.

## Triangulation with v0.20 and v0.21

triangulate_longitudinal_estimators can assemble results from:

- cross-fitted longitudinal AIPW;
- the parametric g-formula; and
- the weighted pooled-logistic MSM.

The function does not choose a winner or create a causal score.

Risk, risk difference, and risk ratio from AIPW and the g-formula are marked as comparable only when the analyst has also aligned population, horizon, intervention definition, and estimand.

The pooled-logistic MSM odds ratio remains explicitly marked as a different effect scale.

## Interpretation limits

Longitudinal double robustness is not protection against arbitrary design failure. In particular, it does not solve:

- unmeasured time-varying confounding;
- structural positivity violations;
- incorrect treatment timing;
- informative measurement processes not represented in history;
- exposure or outcome misclassification;
- inappropriate dynamic treatment rules;
- severe nuisance-model extrapolation; or
- violations of consistency.

Use v0.20 positivity/weight diagnostics, v0.21 g-formula sensitivity analyses, and v0.22 held-out nuisance diagnostics together rather than relying on one estimator alone.

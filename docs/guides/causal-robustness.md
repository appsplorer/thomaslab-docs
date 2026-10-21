# Causal robustness, falsification, and sensitivity analysis

Version 0.23 adds a dedicated robustness layer above the longitudinal estimators introduced in v0.20–v0.22.

The goal is not to generate a causal-validity score. The goal is to make specific sensitivity questions reproducible, reviewable, and difficult to hide.

## Risk-ratio sensitivity to unmeasured confounding

risk_ratio_bias_factor() implements the standard risk-ratio bounding factor

[
BF = rac{RR_{AU}RR_{UY}}{RR_{AU}+RR_{UY}-1}
]

for sensitivity parameters at or above one.

Here:

- (RR_{AU}) is the specified strength of association between an unmeasured confounder and treatment/exposure;
- (RR_{UY}) is the specified strength of association between that confounder and the outcome.

The function returns a worst-case bounding factor under this parameterization. It does not estimate the actual amount of confounding.

bound_risk_ratio_for_unmeasured_confounding() applies the factor in the direction that moves the observed association toward the null.

For an observed RR above one:

[
RR_{bounded} = RR_{observed}/BF
]

For a protective observed RR below one, the inverse association is bounded and transformed back.

Values are allowed to reach or cross the null. They are not clipped.

## Tipping-point grids

risk_ratio_tipping_grid() evaluates a prespecified grid of (RR_{AU}) and (RR_{UY}) values.

Every row retains:

- the observed risk ratio;
- both confounding-strength parameters;
- the implied bias factor;
- the bounded risk ratio; and
- whether that combination is sufficient to reach or cross the null.

This is intended for transparent quantitative bias analysis rather than a single hand-picked sensitivity parameter.

## E-values for longitudinal contrasts

longitudinal_e_value_table() applies the existing thomaslab E-value implementation to longitudinal risk-ratio contrasts.

If a confidence interval is available, the E-value for the interval bound closest to the null is also reported.

An E-value is a sensitivity metric. It is not evidence that unmeasured confounding is absent, and it should not replace design-based reasoning about plausible confounders.

## Negative controls as falsification analyses

v0.15 already provides study-specified negative-control scaffolding. Version 0.23 adds summarize_negative_control_estimates() for estimates produced by the actual primary-design pipeline.

Whenever feasible, a negative-control outcome or exposure should be analyzed with the same:

- eligibility rules;
- time zero;
- treatment strategy definition;
- censoring rules;
- covariate strategy;
- estimator; and
- uncertainty procedure

used for the primary analysis.

The summary reports whether each interval includes its prespecified null.

An interval excluding the null is labeled for review. It is not automatically translated into a statement that residual confounding definitely exists or that the primary result is invalid. Negative controls can fail for reasons including measurement differences, chance, selection, or a poor control choice.

## Nuisance-model calibration

longitudinal_nuisance_calibration() evaluates the held-out treatment and censoring probabilities produced by v0.22.

Treatment calibration includes:

- event/treatment prevalence;
- mean predicted probability;
- Brier score;
- calibration intercept;
- calibration slope;
- expected calibration error;
- maximum calibration error; and
- a calibration table based on probability bins.

Censoring calibration is calculated only among event-free rows because an observed event is a terminal outcome rather than a continuation target.

Calibration is reported overall and by period.

Poor calibration can indicate nuisance-model misspecification, but good calibration does not establish exchangeability or positivity.

## Explicit overlap-restricted sensitivity populations

identify_longitudinal_overlap_population() evaluates raw regime-treatment probabilities and raw event-free continuation probabilities.

Treatment support is evaluated only along the observed regime-relevant prefix: through the first treatment deviation, inclusive. Censoring support is evaluated while the observed path remains treatment-adherent. Later post-deviation probabilities are excluded because they carry zero regime weight for that strategy. A patient enters the overlap sensitivity population only when every relevant treatment-support probability and every relevant censoring-support probability meet the explicitly chosen thresholds.

restrict_panel_to_overlap_population() then creates the corresponding sensitivity dataset and reports the retained patient fraction.

This changes the population being studied. The overlap-restricted result therefore should be labeled as a sensitivity estimand rather than silently substituted for the primary target-population result.

## Influence and leave-one-out diagnostics

longitudinal_influence_diagnostics() operates on the patient-level influence table produced by v0.22.

For every patient it reports:

- signed influence;
- absolute influence;
- standardized influence;
- exact leave-one-out estimate for the mean pseudo-outcome estimator; and
- the leave-one-out shift from the full estimate.

The exact leave-one-out identity used is

[
hatpsi_{-i} = hatpsi - IF_i/(n-1)
]

when the stored influence value is the centered patient pseudo-outcome.

Large influence should trigger case/history/model review. It is not a license to delete observations solely because they move the estimate.

## Unified robustness report

build_longitudinal_robustness_report() can combine:

- the v0.22 longitudinal AIPW comparison;
- optional v0.21 g-formula and v0.20 MSM estimator triangulation;
- E-values;
- an unmeasured-confounding tipping grid;
- prespecified negative-control estimates;
- treatment/censoring nuisance calibration; and
- patient influence diagnostics.

The returned bundle explicitly states:

sensitivity_bundle_not_a_causal_validity_score

The function intentionally does not assign a robustness grade, traffic light, winner, or automated causal conclusion.

## Recommended analysis sequence

For a publication-quality longitudinal observational study:

1. Establish eligibility, time zero, intervention strategies, follow-up, and outcomes before estimation.
2. Run v0.20 positivity and longitudinal weighting diagnostics.
3. Fit the v0.21 parametric g-formula as a model-based sensitivity analysis.
4. Fit the v0.22 cross-fitted longitudinal AIPW estimator and inspect held-out nuisance diagnostics.
5. Prespecify scientifically plausible negative controls.
6. Calculate risk-ratio E-values where the estimand/effect scale supports them.
7. Run a range of explicit unmeasured-confounding strength combinations rather than reporting only one.
8. Examine nuisance calibration and patient influence.
9. Repeat the primary estimator in any overlap-restricted sensitivity population and label the changed target population.
10. Report disagreement across estimators and sensitivity analyses rather than averaging it away.

None of these steps makes observational data equivalent to randomization.

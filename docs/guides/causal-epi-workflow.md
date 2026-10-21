# Epidemiology and causal workflow layer

Version 0.13 adds reusable descriptive epidemiology and observational causal-workflow diagnostics.

## Recommended order

1. Freeze cohort/index/exposure/outcome definitions.
2. Run leakage checks before modeling.
3. Describe crude prevalence/incidence and effect measures.
4. Specify pre-treatment confounders from subject-matter knowledge.
5. Estimate propensity scores only after the estimand and treatment are defined.
6. Inspect overlap and near-positivity problems.
7. Inspect covariate balance before and after weighting/matching.
8. Estimate the prespecified effect.
9. Run sensitivity analyses and alternative specifications.
10. Report assumptions and diagnostics alongside the estimate.

## Positivity is empirical and conceptual

`assess_propensity_overlap()` describes empirical common support. `assess_positivity()` reports observations near prespecified propensity boundaries and optional weight instability. Neither proves the causal positivity assumption.

## AIPW

`estimate_aipw_ate()` implements cross-fitted augmented inverse-probability weighting for the average treatment effect. For binary outcomes the primary effect is an absolute risk difference. The influence-function confidence interval accounts for empirical influence-function variation under the fitted nuisance models.

A doubly robust estimator does **not** protect against unmeasured confounding, poorly defined interventions, selection bias, measurement error, or severe positivity violations.

## Effect tables

`standardize_effect_table()` provides a consistent reporting structure across crude, weighted, survival, and sensitivity analyses. It intentionally does not reinterpret one effect scale as another.

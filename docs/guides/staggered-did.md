# Staggered adoption and event-study research

Version 0.28 adds a dedicated staggered-adoption difference-in-differences layer for studies in which treatment starts at different times across units.

The module is intentionally built around visible cohort-time effects rather than silently compressing a heterogeneous staggered-adoption design into one conventional two-way fixed-effects coefficient.

## Design scope

The staggered-adoption layer expects long-format panel data with a stable unit identifier, an ordered period variable, a numeric outcome, and a binary treatment indicator. Treatment is required to remain on after adoption for this design.

validate_staggered_panel() detects duplicate unit-time rows, non-binary treatment, treatment reversals, units first observed after treatment has already begun, adoption cohorts, and never-treated units.

treatment_timing_diagnostics() reports not-yet-treated and never-treated control support for each estimable adoption-cohort and target-period combination.

These are structural diagnostics. They do not establish parallel trends, no anticipation, or causal validity.

## Cohort-time effects

For adoption cohort g, target period t, and reference period g-1, estimate_group_time_effects() computes a repeated-panel difference-in-changes contrast:

ATT(g,t) = mean(Y_t - Y_(g-1) | G=g) - mean(Y_t - Y_(g-1) | selected controls).

The control set is explicit:

- not_yet_treated: never-treated units plus units whose adoption occurs after both the reference and target periods;
- never_treated: only units that remain untreated throughout their observed panel.

Already-treated units are never reused as controls for later adoption cohorts.

The default reference event time is -1, the last observed period before adoption. It is represented as an explicit zero normalization row, not an estimated treatment effect.

## Event-time and cohort aggregation

aggregate_event_study() aggregates cohort-time effects by event time while preserving the underlying cohort-time table for auditability.

Two event-time weighting rules are supported:

- cohort_size: weight by the treated units contributing to each cohort-time cell;
- equal_cohort: give each contributing adoption cohort equal weight.

aggregate_cohort_effects() also produces cohort-specific post-adoption summaries across estimable target periods. This keeps adoption-cohort heterogeneity visible rather than forcing a single pooled coefficient.

The analytic event-time standard error is explicitly labelled a cell-independence approximation because the same units may contribute to multiple cells. For primary uncertainty, use bootstrap_event_study(), which resamples complete units and returns percentile intervals plus the successful-replicate fraction.

## Pre-period placebo diagnostics

preperiod_placebo_diagnostic() summarizes event times at or before -2 and reports the number of available pre-period estimates, maximum absolute estimate, root-mean-square estimate, and which intervals exclude zero.

This is a falsification screen only. A quiet pre-period pattern does not prove parallel trends, absence of anticipation, stable measurement, or correct treatment timing.

## Treatment-timing sensitivity

timing_shift_sensitivity() shifts recorded adoption earlier or later by analyst-supplied numbers of observed periods and reruns the event-study pipeline.

A positive shift delays adoption; a negative shift moves it earlier. The result is labelled adoption-timing or exposure-misclassification sensitivity. It is not interpreted as an estimate of a biological latency period or true exposure onset.

## Why this is separate from ordinary TWFE

The v0.27 two-period DiD helper remains appropriate for a genuine two-group/two-period design. Version 0.28 does not silently extend it into a conventional staggered-adoption TWFE regression.

When treatment timing varies and effects may differ by cohort or event time, already-treated comparison groups and implicit weighting can make a single TWFE coefficient difficult to interpret. This module therefore identifies adoption cohorts explicitly, keeps group-time estimates visible, excludes already-treated controls, aggregates only after cell estimation, exposes support failures, separates placebo periods from post-adoption effects, and provides unit-cluster bootstrap uncertainty.

The implementation is an auditable group-time difference-in-changes framework. It should not be described as reproducing every semiparametric or doubly robust estimator in the staggered-DiD literature.

## Recommended workflow

1. Freeze unit, outcome, treatment, and period definitions before inspecting post-treatment estimates.
2. Run validate_staggered_panel() and resolve duplicate rows or treatment reversals.
3. Review adoption-cohort sizes and units lacking observed pre-adoption periods.
4. Inspect treatment_timing_diagnostics() for control support.
5. Estimate the full cohort-time table before aggregation.
6. Inspect pre-period placebo estimates and substantive threats to parallel trends.
7. Aggregate by event time using a prespecified weighting rule.
8. Use the unit-cluster bootstrap for event-study uncertainty where feasible.
9. Rerun scientifically defensible control-group and timing-shift sensitivity analyses.
10. Report that causal interpretation still requires parallel trends for selected controls, no anticipation over the reference window, consistency, correct timing, and adequate support.

The software supports transparent estimation and diagnostics; it does not certify a policy change, treatment adoption, or natural experiment as causally identified.

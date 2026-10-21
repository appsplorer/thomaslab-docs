# Self-controlled medication-safety designs

Version 0.19 adds reusable self-controlled case-series (SCCS) and case-crossover infrastructure above the v0.18 drug-safety window engine.

These designs compare periods within the same person, which removes confounding by characteristics that do not vary over the observation period. That does not make the analysis automatically causal. Time-varying confounding, exposure timing, event-dependent exposure, event-dependent observation, outcome-dependent censoring, age/calendar-time effects, and poorly specified risk windows can still bias results.

## SCCS workflow

    case patients + observation periods
              +
    reviewed exposure episodes
              +
    reviewed outcome events
              ↓
    protocol-defined induction/risk/washout windows
              ↓
    repeated-exposure overlap audit
              ↓
    mutually exclusive observation intervals
              ↓
    baseline + exposed period event/person-time table
              ↓
    SCCS diagnostics
              ↓
    conditional Poisson estimate

build_sccs_intervals() partitions each case patient's complete observation period into mutually exclusive intervals. Uncovered time is labelled baseline. By default, overlapping risk periods from repeated exposures raise an error rather than being silently assigned.

If a protocol explicitly defines precedence, overlap_policy="latest_exposure" or "earliest_exposure" can be used. That setting is a design decision and should be reported.

audit_sccs_intervals() checks interval continuity, overlap, case-only event support, and the presence of baseline time. summarize_sccs_periods() provides descriptive event/person-time summaries.

fit_sccs_conditional_poisson() uses a conditional Poisson model that conditions out patient-specific effects. The estimator does not by itself correct time-varying confounding or violations of SCCS assumptions. Age groups, season/calendar time, and other time-varying adjustments should be planned explicitly when scientifically required.

## Event-dependent exposure diagnostic

audit_event_dependent_exposure() compares exposure starts in symmetric windows before and after observed events. It is intentionally labelled a diagnostic only. A before/after imbalance can motivate protocol review but does not prove event-dependent exposure, and an apparently balanced pattern does not prove the assumption is satisfied.

## Case-crossover workflow

    case event date
         ↓
    one hazard window
    +
    one or more control windows
         ↓
    window overlap/duration audit
         ↓
    exposure overlap classification
         ↓
    within-case comparison

build_case_crossover_windows() uses inclusive day offsets relative to each event date. Post-event exposure assessment is blocked by default.

audit_case_crossover_windows() checks that each case has one hazard window, at least one control window, no overlapping windows, and—by default—equal durations.

classify_case_crossover_exposure() calculates any overlap and the number of uniquely covered exposure days within each window.

For exactly one hazard and one control period, matched_case_crossover_odds_ratio() reports the discordant-pair odds ratio. For one-or-more controls, fit_case_crossover_conditional_logit() fits a conditional logistic model.

## Sensitivity analyses

Window definitions are study assumptions rather than software defaults. Re-run the same construction with alternate biologically defensible induction, hazard, washout, or control windows and compare the direction, magnitude, precision, exposed case counts, and diagnostic results.

Do not select the final window because it produces the most favorable association.

## Interpretation limits

Self-controlled designs are particularly useful when stable person-level confounding is a major concern, but they require assumptions that differ from active-comparator cohort designs. The package therefore keeps these workflows separate from target-trial, IPTW/AIPW, and external-validation modules.

No SCCS or case-crossover estimate produced by this package should be described as proving an adverse drug reaction without the broader clinical, methodological, and evidence review required by the study.

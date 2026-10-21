# Advanced survival, competing-risk, and longitudinal follow-up workflows

`thomaslab.survival` adds explicit preparation and estimation utilities for time-to-event research.

## Competing risks

Use `aalen_johansen_cif()` for nonparametric cumulative incidence in the presence of competing events. Use `fit_cause_specific_cox()` when the research question concerns a cause-specific hazard. These answer different questions: a cause-specific hazard ratio is not a Fine–Gray subdistribution hazard ratio and should not be presented as one.

## Time-varying exposure

`build_time_varying_intervals()` creates explicit start/stop records from covariate changes. This is preferable to labeling a patient "ever exposed" at baseline when exposure starts later.

`audit_immortal_time_assignment()` detects one common source of immortal-time bias: baseline assignment that depends on exposure occurring after time zero.

## Landmark analyses

`build_landmark_dataset()` retains only people still under follow-up beyond the landmark, resets follow-up time, and—when exposure onset is supplied—defines exposure using information available by the landmark.

## Modeling notes

`fit_time_varying_cox()` delegates estimation to lifelines' Cox time-varying fitter. Long-format interval semantics and proportional-hazards assumptions remain study responsibilities.

This module is research infrastructure, not automatic causal identification or clinical decision support.

## Numeric input checks and reference tests

The survival functions must reject unknown, fractional or nonfinite event/cause codes rather than silently censoring or truncating them. `aalen_johansen_cif` requires finite non-negative follow-up time, binary event indicators and positive integral causes for observed events (cause 0 or missing for censored cases). `fit_cause_specific_cox` requires **positive** finite duration, a positive integer requested cause and finite integral cause codes. It must not quietly classify malformed cause values as censored.

A synthetic Aalen–Johansen reference case with follow-up times 1, 2, 2 and 3 and event causes 1, 2, 1 and 0 produces final cause-1 cumulative incidence **0.50**, cause-2 cumulative incidence **0.25**, and all-cause event-free survival **0.25**. These values are independently computable from the risk sets and do not establish covariate adjustment or clinical validity.

The input-contract regression tests under development live in private `tests/test_scientific_input_contracts.py`. The fixes must pass local and hosted tests before being treated as software-release evidence.

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

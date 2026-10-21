# PK/PD and platelet-function workflows

`thomaslab.pkpd` provides transparent observed PK summaries from already-curated concentration/time data: observed trapezoidal AUC, Cmax/Tmax, simple terminal log-linear half-life, dose-normalized exposure, CL/F-style summaries, and baseline-adjusted pharmacodynamic changes.

`thomaslab.platelet` handles PRU parsing, study-specified high platelet-reactivity thresholds, PRU change, and linkage to patient-level PGx/drug summaries.

## Guardrails

- observed trapezoidal AUC is not automatically AUC0-inf;
- terminal half-life selection remains a PK-analysis decision;
- dose/AUC without known bioavailability is apparent clearance (CL/F);
- PRU thresholds must be protocol-defined or loaded from a reviewed study configuration;
- platelet tests are measurements, not treatment recommendations;
- PK/PD summaries do not replace population-PK or nonlinear mixed-effects modeling.

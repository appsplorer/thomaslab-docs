# Quasi-experimental causal research

Version 0.27 adds guarded implementations of instrumental variables, canonical two-period difference-in-differences, local-linear regression discontinuity, and segmented interrupted time series.

The module treats quasi-experimental identification as a design problem rather than a property created by a regression coefficient.

## Instrumental variables

For a single endogenous treatment (A), outcome (Y), instrument set (Z), and exogenous covariates (X), estimate_2sls() implements the linear two-stage least-squares estimator.

The structural coefficient vector is

[
hateta =
{W^	op P_Z W}^{-1}W^	op P_ZY,
]

where (W) contains the intercept, endogenous treatment, and exogenous covariates, and (P_Z) projects onto the instrument/exogenous design.

The default covariance is HC1 heteroskedasticity robust.

Binary outcomes are permitted, but the treatment coefficient remains a linear probability-scale effect. It is not converted into an odds ratio.

### First-stage diagnostics

iv_first_stage_diagnostics() compares unrestricted and restricted first-stage OLS models and reports:

- excluded-instrument partial F statistic;
- partial (R^2);
- analyst-selected weak-F screening threshold;
- whether the statistic falls below that threshold; and
- instrument coefficients from the unrestricted first stage.

The conventional threshold of 10 is available as a default screening value only.

A large first-stage F statistic establishes neither:

- instrument independence;
- the exclusion restriction;
- monotonicity;
- absence of direct instrument effects; nor
- scientific instrument validity.

Likewise, a weak-instrument screen should not be treated as a complete weak-identification analysis.

## Difference-in-differences

estimate_two_period_did() implements the canonical two-group, two-period model:

[
Y = eta_0 + eta_1 G + eta_2 Post
+ eta_3(G	imes Post)+Xgamma+epsilon.
]

The coefficient (eta_3) is returned as the DiD contrast.

HC1 covariance is used by default. An explicit cluster column can instead be supplied.

The function requires all four treated/control × pre/post cells.

### Scope restriction

This implementation intentionally does not reinterpret a staggered-adoption study as a standard two-way fixed-effects design.

Treatment-timing heterogeneity and staggered adoption require design-specific estimators and diagnostics rather than silently reusing the two-period model.

### Pretrend diagnostic

did_pretrend_diagnostic() estimates a treated-group × pre-intervention time interaction using observed pre-period data.

It tests only for a differential linear pretrend over the available pre-period.

A non-significant interaction does not prove parallel trends. Statistical power can be low, and post-intervention counterfactual trends remain unobserved.

## Regression discontinuity

estimate_regression_discontinuity() implements a sharp local-linear RD around an analyst-supplied cutoff (c).

Within bandwidth (h), it fits separate local slopes on either side of the cutoff:

[
Y =
eta_0
+	au I(Rge c)
+eta_1(R-c)
+eta_2 I(Rge c)(R-c)
+Xgamma+epsilon.
]

The discontinuity coefficient (	au) is the reported RD effect.

Available kernels:

- triangular;
- uniform.

The bandwidth is never chosen silently by the library.

rd_bandwidth_sensitivity() reruns the local-linear estimator across a user-specified bandwidth grid and keeps failed bandwidths visible.

Causal interpretation requires a credible continuity design around the cutoff and review of possible sorting, manipulation, co-interventions, and outcome/covariate discontinuities.

The module does not claim that estimation itself verifies those assumptions.

## Interrupted time series

estimate_interrupted_time_series() fits a segmented linear model with:

- baseline level at the intervention time;
- baseline linear trend;
- immediate post-intervention level change; and
- post-intervention slope change.

For intervention time (T_0),

[
Y_t=
eta_0+eta_1(t-T_0)
+eta_2I(tge T_0)
+eta_3(t-T_0)I(tge T_0)
+X_tgamma+epsilon_t.
]

HAC covariance is used with an explicit lag choice.

The time index must be unique and the implementation requires observations on both sides of the intervention.

An ITS coefficient does not distinguish the intervention from another event occurring at the same time. Analysts must examine concurrent policies, shocks, seasonality, changes in measurement, and functional-form sensitivity.

## Recommended workflow

For quasi-experimental clinical or pharmacoepidemiologic research:

1. articulate the identification argument before fitting a model;
2. define exposure, time zero, outcome and population using the existing cohort utilities;
3. freeze the quasi-experimental design choice before outcome-driven tuning;
4. report the instrument/cutoff/intervention mechanism explicitly;
5. run design-specific support and diagnostic checks;
6. perform sensitivity analyses over bandwidths, specifications or covariance choices where scientifically justified;
7. retain failed diagnostics in the research record;
8. avoid interpreting an identification diagnostic as proof of an assumption it cannot test;
9. triangulate with other credible designs where possible; and
10. report uncertainty and design limitations alongside the effect estimate.

quasi_experimental_effect_table() converts supported estimator result dictionaries into a consistent downstream effect table with method, estimand/effect name, estimate, uncertainty, covariance metadata, and interpretation fields. Interrupted time series produces separate rows for level and slope changes rather than collapsing them into one effect.

The ITS implementation requires equally spaced time points so the declared HAC lag has a clear observation-interval interpretation.

The software supports estimation and auditability. It does not certify a natural experiment as valid.

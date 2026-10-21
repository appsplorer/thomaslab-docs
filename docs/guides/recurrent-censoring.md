# Recurrent events and censoring diagnostics

## Recurrent events

`thomaslab.recurrent` prepares total-time counting-process rows for recurrent outcomes and PWP-style event-order strata. It deliberately separates **data construction** from inferential claims: robust recurrent-event inference requires a model/variance strategy appropriate to the protocol.

The library rejects multiple same-patient events at the identical time unless they are adjudicated upstream.

## Censoring

`thomaslab.censoring` provides:

- marginal Kaplan–Meier censoring survival;
- simple marginal IPCW at observed times;
- explicit IPCW truncation;
- effective-sample-size and extreme-weight diagnostics;
- censoring summaries and measured-covariate SMDs.

Marginal IPCW is not sufficient when censoring depends on measured time-varying or baseline covariates. A low measured-covariate SMD does not prove censoring is non-informative.

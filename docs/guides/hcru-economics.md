# Healthcare utilization and economic outcomes

`thomaslab.hcru` converts reviewed encounter records into auditable utilization endpoints such as encounter counts, length of stay, readmission timing, and person-time rates. Encounter categories are never guessed from local labels without an explicit mapping.

`thomaslab.economics` aggregates observed cost fields, supports caller-supplied price-index and FX adjustments, summarizes skewed costs, calculates observed QALYs from supplied utility trajectories, and provides transparent ICER/net-monetary-benefit arithmetic.

## Required study decisions

Before analysis, document the encounter mapping, observation window, cost perspective, included cost categories, currency and price year, index/FX sources, utility instrument and mapping, handling of negative adjustments, and any willingness-to-pay threshold.

## Guardrails

- Readmission timing does not determine whether a readmission was planned or preventable.
- Cost fields should preserve provenance (allowed/paid/billed/patient share are not interchangeable).
- Inflation and currency conversion require externally supplied, versioned indices/rates.
- QALYs here are observed trapezoidal summaries of supplied utilities; the package does not create utilities from diagnoses or clinical scores.
- ICERs are descriptive arithmetic and require an appropriate effectiveness/causal analysis before policy interpretation.

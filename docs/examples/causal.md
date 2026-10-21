# Example: weighted binary treatment effect

This example shows the mechanics of using a study-supplied weight column. It does not establish causal identification.

~~~python
import pandas as pd

from thomaslab.causal_workflows import estimate_iptw_binary_effects

analysis = pd.DataFrame(
    {
        "treatment": [1, 1, 0, 0, 1, 0],
        "outcome": [1, 0, 0, 1, 1, 0],
        "iptw": [0.9, 1.1, 1.0, 0.95, 1.05, 1.0],
    }
)

effects = estimate_iptw_binary_effects(
    analysis,
    treatment_col="treatment",
    outcome_col="outcome",
    weight_col="iptw",
)

print(effects)
~~~

## Required scientific review

Before interpreting any estimate, define the estimand and evaluate treatment assignment, exchangeability, positivity, weight stability, censoring, temporal alignment, measurement error, and sensitivity to unmeasured confounding.

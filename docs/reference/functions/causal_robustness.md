# thomaslab.causal_robustness

Causal robustness, falsification, and sensitivity-analysis utilities.

This module complements the design and estimation layers in thomaslab-core. It
does not decide whether an observational result is causal. Instead, it makes
specific robustness questions inspectable:

* how strong an unmeasured confounder would need to be on a risk-ratio scale;
* how risk-ratio results move under explicit confounding-strength assumptions;
* whether prespecified negative-control estimates are compatible with their null;
* whether treatment/censoring nuisance probabilities are calibrated;
* which patients fall outside an explicitly chosen longitudinal support region;
* how sensitive an estimate is to individual influence contributions; and
* whether MSM, g-formula, and longitudinal AIPW results tell a coherent or
  discrepant sensitivity-analysis story.

All thresholds are analysis choices and are returned in the outputs. None is a
universal causal-validity cutoff.

## Research-use boundary

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

## Self-service orientation

- Related guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 10

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.causal_robustness.risk_ratio_bias_factor -->
## risk_ratio_bias_factor

### Purpose

Return the standard risk-ratio bounding factor for an unmeasured confounder.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def risk_ratio_bias_factor( confounder_exposure_rr: float, confounder_outcome_rr: float, ) -> float
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `confounder_exposure_rr` | `confounder_exposure_rr: float` | Yes | Treatment/exposure definition supplied by the study specification; do not infer clinical meaning from labels alone. |
| `confounder_outcome_rr` | `confounder_outcome_rr: float` | Yes | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `confounder_exposure_rr`, `confounder_outcome_rr`.

### Returns

`float`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.causal_robustness import risk_ratio_bias_factor

result = risk_ratio_bias_factor(
    confounder_exposure_rr=0.5,
    confounder_outcome_rr=0.5
)

print(result)
~~~

### Related functions

- `bound_risk_ratio_for_unmeasured_confounding`
- `risk_ratio_tipping_grid`
- `longitudinal_e_value_table`
- `summarize_negative_control_estimates`
- `longitudinal_nuisance_calibration`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_robustness.py#L46`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L46)
- Repository search: [risk_ratio_bias_factor](https://github.com/appsplorer/thomaslab-core/search?q=risk_ratio_bias_factor&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return the standard risk-ratio bounding factor for an unmeasured confounder.

Both supplied strengths are interpreted on scales at or above one. The result
is a worst-case bounding factor under the usual risk-ratio sensitivity
parameterization; it is not an estimate of actual bias.

### API inspection

~~~python
import inspect
from thomaslab.causal_robustness import risk_ratio_bias_factor

print(inspect.signature(risk_ratio_bias_factor))
print(risk_ratio_bias_factor.__doc__)
~~~

### Source

[`src/thomaslab/causal_robustness.py#L46`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L46)

---

<!-- callable:thomaslab.causal_robustness.bound_risk_ratio_for_unmeasured_confounding -->
## bound_risk_ratio_for_unmeasured_confounding

### Purpose

Move an observed risk ratio toward the null using an explicit bias factor.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def bound_risk_ratio_for_unmeasured_confounding( observed_risk_ratio: float, *, confounder_exposure_rr: float, confounder_outcome_rr: float, ) -> dict[str, float | bool]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `observed_risk_ratio` | `observed_risk_ratio: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `confounder_exposure_rr` | `confounder_exposure_rr: float` | Yes | Treatment/exposure definition supplied by the study specification; do not infer clinical meaning from labels alone. |
| `confounder_outcome_rr` | `confounder_outcome_rr: float` | Yes | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `observed_risk_ratio`, `confounder_exposure_rr`, `confounder_outcome_rr`.

### Returns

`dict[str, float | bool]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.causal_robustness import bound_risk_ratio_for_unmeasured_confounding

result = bound_risk_ratio_for_unmeasured_confounding(
    observed_risk_ratio=0.5,
    confounder_exposure_rr=0.5,
    confounder_outcome_rr=0.5
)

print(result)
~~~

### Related functions

- `risk_ratio_bias_factor`
- `risk_ratio_tipping_grid`
- `longitudinal_e_value_table`
- `summarize_negative_control_estimates`
- `longitudinal_nuisance_calibration`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_robustness.py#L66`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L66)
- Repository search: [bound_risk_ratio_for_unmeasured_confounding](https://github.com/appsplorer/thomaslab-core/search?q=bound_risk_ratio_for_unmeasured_confounding&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Move an observed risk ratio toward the null using an explicit bias factor.

For an observed ratio above one, the bound is RR/BF. For an observed ratio
below one, the inverse association is bounded and transformed back, yielding
RR*BF. Values can cross one when the supplied confounding strength is large
enough; this is retained rather than clipped.

### API inspection

~~~python
import inspect
from thomaslab.causal_robustness import bound_risk_ratio_for_unmeasured_confounding

print(inspect.signature(bound_risk_ratio_for_unmeasured_confounding))
print(bound_risk_ratio_for_unmeasured_confounding.__doc__)
~~~

### Source

[`src/thomaslab/causal_robustness.py#L66`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L66)

---

<!-- callable:thomaslab.causal_robustness.risk_ratio_tipping_grid -->
## risk_ratio_tipping_grid

### Purpose

Evaluate a grid of unmeasured-confounding strengths on the RR scale.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def risk_ratio_tipping_grid( observed_risk_ratio: float, *, confounder_exposure_rr_values: Sequence[float], confounder_outcome_rr_values: Sequence[float], ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `observed_risk_ratio` | `observed_risk_ratio: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `confounder_exposure_rr_values` | `confounder_exposure_rr_values: Sequence[float]` | Yes | Treatment/exposure definition supplied by the study specification; do not infer clinical meaning from labels alone. |
| `confounder_outcome_rr_values` | `confounder_outcome_rr_values: Sequence[float]` | Yes | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `observed_risk_ratio`, `confounder_exposure_rr_values`, `confounder_outcome_rr_values`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.causal_robustness import risk_ratio_tipping_grid

result = risk_ratio_tipping_grid(
    observed_risk_ratio=0.5,
    confounder_exposure_rr_values=0.5,
    confounder_outcome_rr_values=0.5
)

print(result)
~~~

### Related functions

- `risk_ratio_bias_factor`
- `bound_risk_ratio_for_unmeasured_confounding`
- `longitudinal_e_value_table`
- `summarize_negative_control_estimates`
- `longitudinal_nuisance_calibration`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_robustness.py#L100`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L100)
- Repository search: [risk_ratio_tipping_grid](https://github.com/appsplorer/thomaslab-core/search?q=risk_ratio_tipping_grid&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Evaluate a grid of unmeasured-confounding strengths on the RR scale.

### API inspection

~~~python
import inspect
from thomaslab.causal_robustness import risk_ratio_tipping_grid

print(inspect.signature(risk_ratio_tipping_grid))
print(risk_ratio_tipping_grid.__doc__)
~~~

### Source

[`src/thomaslab/causal_robustness.py#L100`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L100)

---

<!-- callable:thomaslab.causal_robustness.longitudinal_e_value_table -->
## longitudinal_e_value_table

### Purpose

Calculate E-values for longitudinal risk-ratio contrasts.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def longitudinal_e_value_table( comparison: pd.DataFrame, *, strategy_col: str = "strategy", risk_ratio_col: str = "risk_ratio", ci_lower_col: str = "risk_ratio_ci_lower", ci_upper_col: str = "risk_ratio_ci_upper", exclude_reference: bool = True, reference_col: str = "reference_strategy", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `comparison` | `comparison: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `strategy_col` | `strategy_col: str = 'strategy'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `risk_ratio_col` | `risk_ratio_col: str = 'risk_ratio'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `ci_lower_col` | `ci_lower_col: str = 'risk_ratio_ci_lower'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `ci_upper_col` | `ci_upper_col: str = 'risk_ratio_ci_upper'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `exclude_reference` | `exclude_reference: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `reference_col` | `reference_col: str = 'reference_strategy'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `comparison`.
- Referenced columns must exist in the input table: `strategy_col`, `risk_ratio_col`, `ci_lower_col`, `ci_upper_col`, `reference_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_df = pd.DataFrame(
    {
        "patient_id": ["P001", "P001", "P002", "P002"],
        "event_date": pd.to_datetime(["2026-01-01", "2026-02-01", "2026-01-05", "2026-02-07"]),
        "treatment": [1, 1, 0, 0],
        "outcome": [0, 1, 0, 0],
        "event": [0, 1, 0, 0],
        "duration": [31.0, 62.0, 33.0, 66.0],
        "weight": [1.0, 0.9, 1.1, 1.0],
        "propensity": [0.70, 0.65, 0.35, 0.30],
        "site": ["A", "A", "B", "B"],
        "feature_a": [1.0, 1.4, 0.7, 0.9],
        "feature_b": [2.0, 2.2, 1.5, 1.7],
    }
)

from thomaslab.causal_robustness import longitudinal_e_value_table

result = longitudinal_e_value_table(
    comparison=sample_df
)

print(result)
~~~

### Related functions

- `risk_ratio_bias_factor`
- `bound_risk_ratio_for_unmeasured_confounding`
- `risk_ratio_tipping_grid`
- `summarize_negative_control_estimates`
- `longitudinal_nuisance_calibration`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_robustness.py#L122`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L122)
- Repository search: [longitudinal_e_value_table](https://github.com/appsplorer/thomaslab-core/search?q=longitudinal_e_value_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate E-values for longitudinal risk-ratio contrasts.

Rows without a finite positive risk ratio are retained with missing E-values.
The E-value is a sensitivity metric, not a test that unmeasured confounding is
absent.

### API inspection

~~~python
import inspect
from thomaslab.causal_robustness import longitudinal_e_value_table

print(inspect.signature(longitudinal_e_value_table))
print(longitudinal_e_value_table.__doc__)
~~~

### Source

[`src/thomaslab/causal_robustness.py#L122`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L122)

---

<!-- callable:thomaslab.causal_robustness.summarize_negative_control_estimates -->
## summarize_negative_control_estimates

### Purpose

Summarize prespecified negative-control effect estimates against their null.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_negative_control_estimates( estimates: pd.DataFrame, *, control_col: str = "negative_control", estimate_col: str = "estimate", ci_lower_col: str = "ci_lower", ci_upper_col: str = "ci_upper", null_value: float = 1.0, effect_measure: str = "risk_ratio", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `estimates` | `estimates: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `control_col` | `control_col: str = 'negative_control'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `estimate_col` | `estimate_col: str = 'estimate'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `ci_lower_col` | `ci_lower_col: str = 'ci_lower'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `ci_upper_col` | `ci_upper_col: str = 'ci_upper'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `null_value` | `null_value: float = 1.0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `effect_measure` | `effect_measure: str = 'risk_ratio'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `estimates`.
- Referenced columns must exist in the input table: `control_col`, `estimate_col`, `ci_lower_col`, `ci_upper_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_df = pd.DataFrame(
    {
        "patient_id": ["P001", "P001", "P002", "P002"],
        "event_date": pd.to_datetime(["2026-01-01", "2026-02-01", "2026-01-05", "2026-02-07"]),
        "treatment": [1, 1, 0, 0],
        "outcome": [0, 1, 0, 0],
        "event": [0, 1, 0, 0],
        "duration": [31.0, 62.0, 33.0, 66.0],
        "weight": [1.0, 0.9, 1.1, 1.0],
        "propensity": [0.70, 0.65, 0.35, 0.30],
        "site": ["A", "A", "B", "B"],
        "feature_a": [1.0, 1.4, 0.7, 0.9],
        "feature_b": [2.0, 2.2, 1.5, 1.7],
    }
)

from thomaslab.causal_robustness import summarize_negative_control_estimates

result = summarize_negative_control_estimates(
    estimates=sample_df
)

print(result)
~~~

### Related functions

- `risk_ratio_bias_factor`
- `bound_risk_ratio_for_unmeasured_confounding`
- `risk_ratio_tipping_grid`
- `longitudinal_e_value_table`
- `longitudinal_nuisance_calibration`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_robustness.py#L175`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L175)
- Repository search: [summarize_negative_control_estimates](https://github.com/appsplorer/thomaslab-core/search?q=summarize_negative_control_estimates&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize prespecified negative-control effect estimates against their null.

This function does not estimate the negative-control effects. It is intended to
receive estimates produced with the same design/estimator used for the primary
analysis whenever feasible.

### API inspection

~~~python
import inspect
from thomaslab.causal_robustness import summarize_negative_control_estimates

print(inspect.signature(summarize_negative_control_estimates))
print(summarize_negative_control_estimates.__doc__)
~~~

### Source

[`src/thomaslab/causal_robustness.py#L175`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L175)

---

<!-- callable:thomaslab.causal_robustness.longitudinal_nuisance_calibration -->
## longitudinal_nuisance_calibration

### Purpose

Evaluate held-out treatment and censoring nuisance calibration.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def longitudinal_nuisance_calibration( nuisance: pd.DataFrame, *, treatment_col: str = "treatment", outcome_col: str = "interval_event", time_col: str = "period", treatment_probability_col: str = "treatment_probability", censoring_probability_col: str = "censoring_probability_raw", continuation_col: str = "continuation_observed", n_bins: int = 10, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `nuisance` | `nuisance: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str = 'treatment'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str = 'interval_event'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_probability_col` | `treatment_probability_col: str = 'treatment_probability'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `censoring_probability_col` | `censoring_probability_col: str = 'censoring_probability_raw'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `continuation_col` | `continuation_col: str = 'continuation_observed'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `n_bins` | `n_bins: int = 10` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `nuisance`.
- Referenced columns must exist in the input table: `treatment_col`, `outcome_col`, `time_col`, `treatment_probability_col`, `censoring_probability_col`, `continuation_col`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_df = pd.DataFrame(
    {
        "patient_id": ["P001", "P001", "P002", "P002"],
        "event_date": pd.to_datetime(["2026-01-01", "2026-02-01", "2026-01-05", "2026-02-07"]),
        "treatment": [1, 1, 0, 0],
        "outcome": [0, 1, 0, 0],
        "event": [0, 1, 0, 0],
        "duration": [31.0, 62.0, 33.0, 66.0],
        "weight": [1.0, 0.9, 1.1, 1.0],
        "propensity": [0.70, 0.65, 0.35, 0.30],
        "site": ["A", "A", "B", "B"],
        "feature_a": [1.0, 1.4, 0.7, 0.9],
        "feature_b": [2.0, 2.2, 1.5, 1.7],
    }
)

from thomaslab.causal_robustness import longitudinal_nuisance_calibration

result = longitudinal_nuisance_calibration(
    nuisance=sample_df
)

print(result)
~~~

### Related functions

- `risk_ratio_bias_factor`
- `bound_risk_ratio_for_unmeasured_confounding`
- `risk_ratio_tipping_grid`
- `longitudinal_e_value_table`
- `summarize_negative_control_estimates`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_robustness.py#L297`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L297)
- Repository search: [longitudinal_nuisance_calibration](https://github.com/appsplorer/thomaslab-core/search?q=longitudinal_nuisance_calibration&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Evaluate held-out treatment and censoring nuisance calibration.

Censoring calibration is evaluated only among event-free rows because event
rows have a terminal observed outcome rather than a continuation target.

### API inspection

~~~python
import inspect
from thomaslab.causal_robustness import longitudinal_nuisance_calibration

print(inspect.signature(longitudinal_nuisance_calibration))
print(longitudinal_nuisance_calibration.__doc__)
~~~

### Source

[`src/thomaslab/causal_robustness.py#L297`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L297)

---

<!-- callable:thomaslab.causal_robustness.identify_longitudinal_overlap_population -->
## identify_longitudinal_overlap_population

### Purpose

Identify patients inside an explicit regime-relevant support region.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def identify_longitudinal_overlap_population( nuisance: pd.DataFrame, *, patient_col: str = "patient_id", time_col: str = "period", outcome_col: str = "interval_event", adherence_col: str | None = "strategy_adherent", regime_probability_col: str = "regime_treatment_probability_raw", censoring_probability_col: str = "censoring_probability_raw", min_regime_probability: float = 0.05, min_censoring_probability: float = 0.05, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `nuisance` | `nuisance: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'period'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str = 'interval_event'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `adherence_col` | `adherence_col: str \| None = 'strategy_adherent'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `regime_probability_col` | `regime_probability_col: str = 'regime_treatment_probability_raw'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `censoring_probability_col` | `censoring_probability_col: str = 'censoring_probability_raw'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `min_regime_probability` | `min_regime_probability: float = 0.05` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `min_censoring_probability` | `min_censoring_probability: float = 0.05` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `nuisance`.
- Referenced columns must exist in the input table: `patient_col`, `time_col`, `outcome_col`, `adherence_col`, `regime_probability_col`, `censoring_probability_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_df = pd.DataFrame(
    {
        "patient_id": ["P001", "P001", "P002", "P002"],
        "event_date": pd.to_datetime(["2026-01-01", "2026-02-01", "2026-01-05", "2026-02-07"]),
        "treatment": [1, 1, 0, 0],
        "outcome": [0, 1, 0, 0],
        "event": [0, 1, 0, 0],
        "duration": [31.0, 62.0, 33.0, 66.0],
        "weight": [1.0, 0.9, 1.1, 1.0],
        "propensity": [0.70, 0.65, 0.35, 0.30],
        "site": ["A", "A", "B", "B"],
        "feature_a": [1.0, 1.4, 0.7, 0.9],
        "feature_b": [2.0, 2.2, 1.5, 1.7],
    }
)

from thomaslab.causal_robustness import identify_longitudinal_overlap_population

result = identify_longitudinal_overlap_population(
    nuisance=sample_df
)

print(result)
~~~

### Related functions

- `risk_ratio_bias_factor`
- `bound_risk_ratio_for_unmeasured_confounding`
- `risk_ratio_tipping_grid`
- `longitudinal_e_value_table`
- `summarize_negative_control_estimates`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_robustness.py#L384`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L384)
- Repository search: [identify_longitudinal_overlap_population](https://github.com/appsplorer/thomaslab-core/search?q=identify_longitudinal_overlap_population&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Identify patients inside an explicit regime-relevant support region.

Treatment support is evaluated through the first observed treatment deviation,
inclusive, because the prescribed treatment probability at that history is
relevant. Censoring support is evaluated only while the observed trajectory
remains treatment-adherent, because later censoring factors carry zero regime
weight after treatment deviation.

If adherence_col is None, all observed rows are reviewed. This defines a
sensitivity population and does not automatically redefine the primary
estimand.

### API inspection

~~~python
import inspect
from thomaslab.causal_robustness import identify_longitudinal_overlap_population

print(inspect.signature(identify_longitudinal_overlap_population))
print(identify_longitudinal_overlap_population.__doc__)
~~~

### Source

[`src/thomaslab/causal_robustness.py#L384`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L384)

---

<!-- callable:thomaslab.causal_robustness.restrict_panel_to_overlap_population -->
## restrict_panel_to_overlap_population

### Purpose

Restrict a panel to patients selected by an explicit support audit.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def restrict_panel_to_overlap_population( panel: pd.DataFrame, overlap_population: pd.DataFrame, *, patient_col: str = "patient_id", include_col: str = "in_overlap_population", ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `panel` | `panel: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `overlap_population` | `overlap_population: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `include_col` | `include_col: str = 'in_overlap_population'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `panel`, `overlap_population`.
- Referenced columns must exist in the input table: `patient_col`, `include_col`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_df = pd.DataFrame(
    {
        "patient_id": ["P001", "P001", "P002", "P002"],
        "event_date": pd.to_datetime(["2026-01-01", "2026-02-01", "2026-01-05", "2026-02-07"]),
        "treatment": [1, 1, 0, 0],
        "outcome": [0, 1, 0, 0],
        "event": [0, 1, 0, 0],
        "duration": [31.0, 62.0, 33.0, 66.0],
        "weight": [1.0, 0.9, 1.1, 1.0],
        "propensity": [0.70, 0.65, 0.35, 0.30],
        "site": ["A", "A", "B", "B"],
        "feature_a": [1.0, 1.4, 0.7, 0.9],
        "feature_b": [2.0, 2.2, 1.5, 1.7],
    }
)

from thomaslab.causal_robustness import restrict_panel_to_overlap_population

result = restrict_panel_to_overlap_population(
    panel=sample_df,
    overlap_population=sample_df
)

print(result)
~~~

### Related functions

- `risk_ratio_bias_factor`
- `bound_risk_ratio_for_unmeasured_confounding`
- `risk_ratio_tipping_grid`
- `longitudinal_e_value_table`
- `summarize_negative_control_estimates`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_robustness.py#L473`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L473)
- Repository search: [restrict_panel_to_overlap_population](https://github.com/appsplorer/thomaslab-core/search?q=restrict_panel_to_overlap_population&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Restrict a panel to patients selected by an explicit support audit.

### API inspection

~~~python
import inspect
from thomaslab.causal_robustness import restrict_panel_to_overlap_population

print(inspect.signature(restrict_panel_to_overlap_population))
print(restrict_panel_to_overlap_population.__doc__)
~~~

### Source

[`src/thomaslab/causal_robustness.py#L473`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L473)

---

<!-- callable:thomaslab.causal_robustness.longitudinal_influence_diagnostics -->
## longitudinal_influence_diagnostics

### Purpose

Summarize patient influence and exact leave-one-out mean shifts.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def longitudinal_influence_diagnostics( influence_curve: pd.DataFrame, *, patient_col: str = "patient_id", influence_col: str = "influence_value", pseudo_outcome_col: str = "pseudo_outcome", estimate: float | None = None, top_fraction: float = 0.01, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `influence_curve` | `influence_curve: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `influence_col` | `influence_col: str = 'influence_value'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `pseudo_outcome_col` | `pseudo_outcome_col: str = 'pseudo_outcome'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `estimate` | `estimate: float \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `top_fraction` | `top_fraction: float = 0.01` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `influence_curve`.
- Referenced columns must exist in the input table: `patient_col`, `influence_col`, `pseudo_outcome_col`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_df = pd.DataFrame(
    {
        "patient_id": ["P001", "P001", "P002", "P002"],
        "event_date": pd.to_datetime(["2026-01-01", "2026-02-01", "2026-01-05", "2026-02-07"]),
        "treatment": [1, 1, 0, 0],
        "outcome": [0, 1, 0, 0],
        "event": [0, 1, 0, 0],
        "duration": [31.0, 62.0, 33.0, 66.0],
        "weight": [1.0, 0.9, 1.1, 1.0],
        "propensity": [0.70, 0.65, 0.35, 0.30],
        "site": ["A", "A", "B", "B"],
        "feature_a": [1.0, 1.4, 0.7, 0.9],
        "feature_b": [2.0, 2.2, 1.5, 1.7],
    }
)

from thomaslab.causal_robustness import longitudinal_influence_diagnostics

result = longitudinal_influence_diagnostics(
    influence_curve=sample_df
)

print(result)
~~~

### Related functions

- `risk_ratio_bias_factor`
- `bound_risk_ratio_for_unmeasured_confounding`
- `risk_ratio_tipping_grid`
- `longitudinal_e_value_table`
- `summarize_negative_control_estimates`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_robustness.py#L500`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L500)
- Repository search: [longitudinal_influence_diagnostics](https://github.com/appsplorer/thomaslab-core/search?q=longitudinal_influence_diagnostics&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize patient influence and exact leave-one-out mean shifts.

### API inspection

~~~python
import inspect
from thomaslab.causal_robustness import longitudinal_influence_diagnostics

print(inspect.signature(longitudinal_influence_diagnostics))
print(longitudinal_influence_diagnostics.__doc__)
~~~

### Source

[`src/thomaslab/causal_robustness.py#L500`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L500)

---

<!-- callable:thomaslab.causal_robustness.build_longitudinal_robustness_report -->
## build_longitudinal_robustness_report

### Purpose

Assemble a review bundle for longitudinal causal sensitivity analyses.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_longitudinal_robustness_report( dr_comparison: pd.DataFrame, *, regime_results: Mapping[str, Mapping[str, Any]] | None = None, gformula_comparison: pd.DataFrame | None = None, msm_estimates: pd.DataFrame | None = None, negative_control_estimates: pd.DataFrame | None = None, qba_strengths: Sequence[float] = (1.25, 1.5, 2.0, 3.0), ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `dr_comparison` | `dr_comparison: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `regime_results` | `regime_results: Mapping[str, Mapping[str, Any]] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `gformula_comparison` | `gformula_comparison: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `msm_estimates` | `msm_estimates: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `negative_control_estimates` | `negative_control_estimates: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `qba_strengths` | `qba_strengths: Sequence[float] = (1.25, 1.5, 2.0, 3.0)` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `dr_comparison`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_df = pd.DataFrame(
    {
        "patient_id": ["P001", "P001", "P002", "P002"],
        "event_date": pd.to_datetime(["2026-01-01", "2026-02-01", "2026-01-05", "2026-02-07"]),
        "treatment": [1, 1, 0, 0],
        "outcome": [0, 1, 0, 0],
        "event": [0, 1, 0, 0],
        "duration": [31.0, 62.0, 33.0, 66.0],
        "weight": [1.0, 0.9, 1.1, 1.0],
        "propensity": [0.70, 0.65, 0.35, 0.30],
        "site": ["A", "A", "B", "B"],
        "feature_a": [1.0, 1.4, 0.7, 0.9],
        "feature_b": [2.0, 2.2, 1.5, 1.7],
    }
)

from thomaslab.causal_robustness import build_longitudinal_robustness_report

result = build_longitudinal_robustness_report(
    dr_comparison=sample_df
)

print(result)
~~~

### Related functions

- `risk_ratio_bias_factor`
- `bound_risk_ratio_for_unmeasured_confounding`
- `risk_ratio_tipping_grid`
- `longitudinal_e_value_table`
- `summarize_negative_control_estimates`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/causal_robustness.py#L564`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L564)
- Repository search: [build_longitudinal_robustness_report](https://github.com/appsplorer/thomaslab-core/search?q=build_longitudinal_robustness_report&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Assemble a review bundle for longitudinal causal sensitivity analyses.

The report is intentionally descriptive. It does not score, rank, or certify
causal validity.

### API inspection

~~~python
import inspect
from thomaslab.causal_robustness import build_longitudinal_robustness_report

print(inspect.signature(build_longitudinal_robustness_report))
print(build_longitudinal_robustness_report.__doc__)
~~~

### Source

[`src/thomaslab/causal_robustness.py#L564`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/causal_robustness.py#L564)

# thomaslab.heterogeneous_effects

Heterogeneous treatment-effect research utilities.

This module estimates conditional treatment-effect structure for research analyses.
It does not generate clinical treatment recommendations. Patient-level conditional
average treatment effects (CATEs) remain model-based causal estimands whose
interpretation requires exchangeability, positivity, consistency, correct temporal
ordering, adequate nuisance models, and a well-defined treatment intervention.

The module provides cross-fitted T-, S-, and doubly robust learners, pseudo-outcome
calibration, prespecified subgroup summaries, bootstrap model-variability intervals,
doubly robust gain curves, research-policy evaluation, site stability summaries,
and source-to-target CATE distribution transport.

## Research-use boundary

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

## Self-service orientation

- Related guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 13

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.heterogeneous_effects.validate_hte_inputs -->
## validate_hte_inputs

### Purpose

Validate one-row-per-unit HTE input data and baseline feature declarations.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_hte_inputs( df: pd.DataFrame, *, treatment_col: str, outcome_col: str, covariates: Sequence[str], outcome_type: str = "binary", ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `outcome_type` | `outcome_type: str = 'binary'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `outcome_col`, `covariates`.
- Referenced columns must exist in the input table: `treatment_col`, `outcome_col`.

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

from thomaslab.heterogeneous_effects import validate_hte_inputs

result = validate_hte_inputs(
    df=sample_df,
    treatment_col='treatment',
    outcome_col='outcome',
    covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `fit_t_learner`
- `fit_s_learner`
- `fit_dr_learner`
- `predict_cate`
- `treatment_effect_calibration`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/heterogeneous_effects.py#L187`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L187)
- Repository search: [validate_hte_inputs](https://github.com/appsplorer/thomaslab-core/search?q=validate_hte_inputs&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate one-row-per-unit HTE input data and baseline feature declarations.

### API inspection

~~~python
import inspect
from thomaslab.heterogeneous_effects import validate_hte_inputs

print(inspect.signature(validate_hte_inputs))
print(validate_hte_inputs.__doc__)
~~~

### Source

[`src/thomaslab/heterogeneous_effects.py#L187`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L187)

---

<!-- callable:thomaslab.heterogeneous_effects.fit_t_learner -->
## fit_t_learner

### Purpose

Fit a cross-fitted T-learner with held-out DR pseudo-outcome diagnostics.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fit_t_learner( df: pd.DataFrame, *, treatment_col: str, outcome_col: str, covariates: Sequence[str], outcome_type: str = "binary", n_splits: int = 5, propensity_clip: float = 0.01, model_kind: str = "linear", random_state: int = 42, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `outcome_type` | `outcome_type: str = 'binary'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `n_splits` | `n_splits: int = 5` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `propensity_clip` | `propensity_clip: float = 0.01` | No | Analysis weight/propensity input. Inspect support, positivity, extremes, and effective sample size where applicable. |
| `model_kind` | `model_kind: str = 'linear'` | No | Model or model setting. Fit/tune only within the training design and preserve independent evaluation. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `outcome_col`, `covariates`.
- Referenced columns must exist in the input table: `treatment_col`, `outcome_col`.

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

from thomaslab.heterogeneous_effects import fit_t_learner

result = fit_t_learner(
    df=sample_df,
    treatment_col='treatment',
    outcome_col='outcome',
    covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `validate_hte_inputs`
- `fit_s_learner`
- `fit_dr_learner`
- `predict_cate`
- `treatment_effect_calibration`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/heterogeneous_effects.py#L310`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L310)
- Repository search: [fit_t_learner](https://github.com/appsplorer/thomaslab-core/search?q=fit_t_learner&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Fit a cross-fitted T-learner with held-out DR pseudo-outcome diagnostics.

### API inspection

~~~python
import inspect
from thomaslab.heterogeneous_effects import fit_t_learner

print(inspect.signature(fit_t_learner))
print(fit_t_learner.__doc__)
~~~

### Source

[`src/thomaslab/heterogeneous_effects.py#L310`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L310)

---

<!-- callable:thomaslab.heterogeneous_effects.fit_s_learner -->
## fit_s_learner

### Purpose

Fit a cross-fitted S-learner and retain held-out nuisance diagnostics.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fit_s_learner( df: pd.DataFrame, *, treatment_col: str, outcome_col: str, covariates: Sequence[str], outcome_type: str = "binary", n_splits: int = 5, propensity_clip: float = 0.01, model_kind: str = "forest", random_state: int = 42, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `outcome_type` | `outcome_type: str = 'binary'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `n_splits` | `n_splits: int = 5` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `propensity_clip` | `propensity_clip: float = 0.01` | No | Analysis weight/propensity input. Inspect support, positivity, extremes, and effective sample size where applicable. |
| `model_kind` | `model_kind: str = 'forest'` | No | Model or model setting. Fit/tune only within the training design and preserve independent evaluation. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `outcome_col`, `covariates`.
- Referenced columns must exist in the input table: `treatment_col`, `outcome_col`.

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

from thomaslab.heterogeneous_effects import fit_s_learner

result = fit_s_learner(
    df=sample_df,
    treatment_col='treatment',
    outcome_col='outcome',
    covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `validate_hte_inputs`
- `fit_t_learner`
- `fit_dr_learner`
- `predict_cate`
- `treatment_effect_calibration`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/heterogeneous_effects.py#L371`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L371)
- Repository search: [fit_s_learner](https://github.com/appsplorer/thomaslab-core/search?q=fit_s_learner&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Fit a cross-fitted S-learner and retain held-out nuisance diagnostics.

### API inspection

~~~python
import inspect
from thomaslab.heterogeneous_effects import fit_s_learner

print(inspect.signature(fit_s_learner))
print(fit_s_learner.__doc__)
~~~

### Source

[`src/thomaslab/heterogeneous_effects.py#L371`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L371)

---

<!-- callable:thomaslab.heterogeneous_effects.fit_dr_learner -->
## fit_dr_learner

### Purpose

Fit a nested cross-fitted doubly robust learner for CATE research.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fit_dr_learner( df: pd.DataFrame, *, treatment_col: str, outcome_col: str, covariates: Sequence[str], outcome_type: str = "binary", n_splits: int = 5, inner_splits: int = 3, propensity_clip: float = 0.01, nuisance_model_kind: str = "linear", effect_model_kind: str = "forest", random_state: int = 42, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `outcome_type` | `outcome_type: str = 'binary'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `n_splits` | `n_splits: int = 5` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `inner_splits` | `inner_splits: int = 3` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `propensity_clip` | `propensity_clip: float = 0.01` | No | Analysis weight/propensity input. Inspect support, positivity, extremes, and effective sample size where applicable. |
| `nuisance_model_kind` | `nuisance_model_kind: str = 'linear'` | No | Model or model setting. Fit/tune only within the training design and preserve independent evaluation. |
| `effect_model_kind` | `effect_model_kind: str = 'forest'` | No | Model or model setting. Fit/tune only within the training design and preserve independent evaluation. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `outcome_col`, `covariates`.
- Referenced columns must exist in the input table: `treatment_col`, `outcome_col`.

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

from thomaslab.heterogeneous_effects import fit_dr_learner

result = fit_dr_learner(
    df=sample_df,
    treatment_col='treatment',
    outcome_col='outcome',
    covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `validate_hte_inputs`
- `fit_t_learner`
- `fit_s_learner`
- `predict_cate`
- `treatment_effect_calibration`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/heterogeneous_effects.py#L474`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L474)
- Repository search: [fit_dr_learner](https://github.com/appsplorer/thomaslab-core/search?q=fit_dr_learner&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Fit a nested cross-fitted doubly robust learner for CATE research.

Outer folds generate held-out CATE predictions. Within each outer training
sample, nuisance functions are themselves cross-fitted before the second-stage
effect model is trained. This avoids directly training the effect model on
nuisance pseudo-outcomes obtained from models that fit the same observation.

### API inspection

~~~python
import inspect
from thomaslab.heterogeneous_effects import fit_dr_learner

print(inspect.signature(fit_dr_learner))
print(fit_dr_learner.__doc__)
~~~

### Source

[`src/thomaslab/heterogeneous_effects.py#L474`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L474)

---

<!-- callable:thomaslab.heterogeneous_effects.predict_cate -->
## predict_cate

### Purpose

Predict model-based CATEs for a covariate table using a fitted bundle.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def predict_cate( model_bundle: dict[str, Any], new_df: pd.DataFrame, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `model_bundle` | `model_bundle: dict[str, Any]` | Yes | Model or model setting. Fit/tune only within the training design and preserve independent evaluation. |
| `new_df` | `new_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `model_bundle`, `new_df`.

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

from thomaslab.heterogeneous_effects import predict_cate

result = predict_cate(
    model_bundle={},
    new_df=sample_df
)

print(result)
~~~

### Related functions

- `validate_hte_inputs`
- `fit_t_learner`
- `fit_s_learner`
- `fit_dr_learner`
- `treatment_effect_calibration`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/heterogeneous_effects.py#L628`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L628)
- Repository search: [predict_cate](https://github.com/appsplorer/thomaslab-core/search?q=predict_cate&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Predict model-based CATEs for a covariate table using a fitted bundle.

### API inspection

~~~python
import inspect
from thomaslab.heterogeneous_effects import predict_cate

print(inspect.signature(predict_cate))
print(predict_cate.__doc__)
~~~

### Source

[`src/thomaslab/heterogeneous_effects.py#L628`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L628)

---

<!-- callable:thomaslab.heterogeneous_effects.treatment_effect_calibration -->
## treatment_effect_calibration

### Purpose

Compare predicted CATEs with held-out doubly robust pseudo-outcomes.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def treatment_effect_calibration( predictions: pd.DataFrame, *, cate_col: str = "predicted_cate", pseudo_col: str = "dr_pseudo_outcome", n_bins: int = 5, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `predictions` | `predictions: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `cate_col` | `cate_col: str = 'predicted_cate'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `pseudo_col` | `pseudo_col: str = 'dr_pseudo_outcome'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `n_bins` | `n_bins: int = 5` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `predictions`.
- Referenced columns must exist in the input table: `cate_col`, `pseudo_col`.

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

from thomaslab.heterogeneous_effects import treatment_effect_calibration

result = treatment_effect_calibration(
    predictions=sample_df
)

print(result)
~~~

### Related functions

- `validate_hte_inputs`
- `fit_t_learner`
- `fit_s_learner`
- `fit_dr_learner`
- `predict_cate`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/heterogeneous_effects.py#L680`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L680)
- Repository search: [treatment_effect_calibration](https://github.com/appsplorer/thomaslab-core/search?q=treatment_effect_calibration&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compare predicted CATEs with held-out doubly robust pseudo-outcomes.

### API inspection

~~~python
import inspect
from thomaslab.heterogeneous_effects import treatment_effect_calibration

print(inspect.signature(treatment_effect_calibration))
print(treatment_effect_calibration.__doc__)
~~~

### Source

[`src/thomaslab/heterogeneous_effects.py#L680`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L680)

---

<!-- callable:thomaslab.heterogeneous_effects.subgroup_cate_summary -->
## subgroup_cate_summary

### Purpose

Summarize prespecified subgroup CATEs without ranking subgroup levels.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def subgroup_cate_summary( df: pd.DataFrame, predictions: pd.DataFrame, *, subgroup_cols: Sequence[str], cate_col: str = "predicted_cate", pseudo_col: str = "dr_pseudo_outcome", max_levels: int = 20, min_n: int = 10, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `predictions` | `predictions: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `subgroup_cols` | `subgroup_cols: Sequence[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `cate_col` | `cate_col: str = 'predicted_cate'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `pseudo_col` | `pseudo_col: str = 'dr_pseudo_outcome'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `max_levels` | `max_levels: int = 20` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `min_n` | `min_n: int = 10` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `predictions`, `subgroup_cols`.
- Referenced columns must exist in the input table: `cate_col`, `pseudo_col`.

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

from thomaslab.heterogeneous_effects import subgroup_cate_summary

result = subgroup_cate_summary(
    df=sample_df,
    predictions=sample_df,
    subgroup_cols=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `validate_hte_inputs`
- `fit_t_learner`
- `fit_s_learner`
- `fit_dr_learner`
- `predict_cate`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/heterogeneous_effects.py#L735`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L735)
- Repository search: [subgroup_cate_summary](https://github.com/appsplorer/thomaslab-core/search?q=subgroup_cate_summary&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize prespecified subgroup CATEs without ranking subgroup levels.

### API inspection

~~~python
import inspect
from thomaslab.heterogeneous_effects import subgroup_cate_summary

print(inspect.signature(subgroup_cate_summary))
print(subgroup_cate_summary.__doc__)
~~~

### Source

[`src/thomaslab/heterogeneous_effects.py#L735`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L735)

---

<!-- callable:thomaslab.heterogeneous_effects.dr_gain_curve -->
## dr_gain_curve

### Purpose

Build a doubly robust Qini-style gain curve for exploratory ranking QA.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def dr_gain_curve( predictions: pd.DataFrame, *, cate_col: str = "predicted_cate", pseudo_col: str = "dr_pseudo_outcome", higher_outcome_better: bool, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `predictions` | `predictions: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `cate_col` | `cate_col: str = 'predicted_cate'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `pseudo_col` | `pseudo_col: str = 'dr_pseudo_outcome'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `higher_outcome_better` | `higher_outcome_better: bool` | Yes | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `predictions`, `higher_outcome_better`.
- Referenced columns must exist in the input table: `cate_col`, `pseudo_col`.

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

from thomaslab.heterogeneous_effects import dr_gain_curve

result = dr_gain_curve(
    predictions=sample_df,
    higher_outcome_better=False
)

print(result)
~~~

### Related functions

- `validate_hte_inputs`
- `fit_t_learner`
- `fit_s_learner`
- `fit_dr_learner`
- `predict_cate`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/heterogeneous_effects.py#L792`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L792)
- Repository search: [dr_gain_curve](https://github.com/appsplorer/thomaslab-core/search?q=dr_gain_curve&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build a doubly robust Qini-style gain curve for exploratory ranking QA.

### API inspection

~~~python
import inspect
from thomaslab.heterogeneous_effects import dr_gain_curve

print(inspect.signature(dr_gain_curve))
print(dr_gain_curve.__doc__)
~~~

### Source

[`src/thomaslab/heterogeneous_effects.py#L792`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L792)

---

<!-- callable:thomaslab.heterogeneous_effects.derive_research_policy -->
## derive_research_policy

### Purpose

Create an exploratory binary treatment rule from held-out CATE predictions.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def derive_research_policy( predictions: pd.DataFrame, *, cate_col: str = "predicted_cate", minimum_benefit: float = 0.0, higher_outcome_better: bool, ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `predictions` | `predictions: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `cate_col` | `cate_col: str = 'predicted_cate'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `minimum_benefit` | `minimum_benefit: float = 0.0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `higher_outcome_better` | `higher_outcome_better: bool` | Yes | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `predictions`, `higher_outcome_better`.
- Referenced columns must exist in the input table: `cate_col`.

### Returns

`pd.Series`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

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

from thomaslab.heterogeneous_effects import derive_research_policy

result = derive_research_policy(
    predictions=sample_df,
    higher_outcome_better=False
)

print(result)
~~~

### Related functions

- `validate_hte_inputs`
- `fit_t_learner`
- `fit_s_learner`
- `fit_dr_learner`
- `predict_cate`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/heterogeneous_effects.py#L837`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L837)
- Repository search: [derive_research_policy](https://github.com/appsplorer/thomaslab-core/search?q=derive_research_policy&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create an exploratory binary treatment rule from held-out CATE predictions.

### API inspection

~~~python
import inspect
from thomaslab.heterogeneous_effects import derive_research_policy

print(inspect.signature(derive_research_policy))
print(derive_research_policy.__doc__)
~~~

### Source

[`src/thomaslab/heterogeneous_effects.py#L837`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L837)

---

<!-- callable:thomaslab.heterogeneous_effects.evaluate_research_policy -->
## evaluate_research_policy

### Purpose

Estimate the outcome under a binary research policy with a DR score.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def evaluate_research_policy( predictions: pd.DataFrame, *, policy: pd.Series | np.ndarray, higher_outcome_better: bool, out_of_fold_policy_predictions_asserted: bool = False, ci: float = 0.95, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `predictions` | `predictions: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `policy` | `policy: pd.Series \| np.ndarray` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `higher_outcome_better` | `higher_outcome_better: bool` | Yes | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `out_of_fold_policy_predictions_asserted` | `out_of_fold_policy_predictions_asserted: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `predictions`, `policy`, `higher_outcome_better`.

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

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.heterogeneous_effects import evaluate_research_policy

result = evaluate_research_policy(
    predictions=sample_df,
    policy=sample_series,
    higher_outcome_better=False
)

print(result)
~~~

### Related functions

- `validate_hte_inputs`
- `fit_t_learner`
- `fit_s_learner`
- `fit_dr_learner`
- `predict_cate`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/heterogeneous_effects.py#L856`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L856)
- Repository search: [evaluate_research_policy](https://github.com/appsplorer/thomaslab-core/search?q=evaluate_research_policy&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate the outcome under a binary research policy with a DR score.

The function expects held-out nuisance predictions. If the treatment policy was
learned using the same outcomes without honest/out-of-fold prediction, policy
value can be optimistically biased; that assertion is therefore recorded.

### API inspection

~~~python
import inspect
from thomaslab.heterogeneous_effects import evaluate_research_policy

print(inspect.signature(evaluate_research_policy))
print(evaluate_research_policy.__doc__)
~~~

### Source

[`src/thomaslab/heterogeneous_effects.py#L856`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L856)

---

<!-- callable:thomaslab.heterogeneous_effects.bootstrap_cate_uncertainty -->
## bootstrap_cate_uncertainty

### Purpose

Bootstrap CATE model predictions as model-variability intervals.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def bootstrap_cate_uncertainty( training_df: pd.DataFrame, target_df: pd.DataFrame, *, method: str, treatment_col: str, outcome_col: str, covariates: Sequence[str], outcome_type: str = "binary", n_bootstrap: int = 100, ci: float = 0.95, n_splits: int = 3, random_state: int = 42, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `training_df` | `training_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `target_df` | `target_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `method` | `method: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `outcome_type` | `outcome_type: str = 'binary'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `n_bootstrap` | `n_bootstrap: int = 100` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `n_splits` | `n_splits: int = 3` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `training_df`, `target_df`, `method`, `treatment_col`, `outcome_col`, `covariates`.
- Referenced columns must exist in the input table: `treatment_col`, `outcome_col`.

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

from thomaslab.heterogeneous_effects import bootstrap_cate_uncertainty

result = bootstrap_cate_uncertainty(
    training_df=sample_df,
    target_df=sample_df,
    method="value",
    treatment_col='treatment',
    outcome_col='outcome',
    covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `validate_hte_inputs`
- `fit_t_learner`
- `fit_s_learner`
- `fit_dr_learner`
- `predict_cate`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/heterogeneous_effects.py#L936`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L936)
- Repository search: [bootstrap_cate_uncertainty](https://github.com/appsplorer/thomaslab-core/search?q=bootstrap_cate_uncertainty&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Bootstrap CATE model predictions as model-variability intervals.

These intervals are not individual-level causal confidence intervals.

### API inspection

~~~python
import inspect
from thomaslab.heterogeneous_effects import bootstrap_cate_uncertainty

print(inspect.signature(bootstrap_cate_uncertainty))
print(bootstrap_cate_uncertainty.__doc__)
~~~

### Source

[`src/thomaslab/heterogeneous_effects.py#L936`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L936)

---

<!-- callable:thomaslab.heterogeneous_effects.site_cate_stability_report -->
## site_cate_stability_report

### Purpose

Summarize held-out CATE behavior across sites without ranking sites.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def site_cate_stability_report( df: pd.DataFrame, predictions: pd.DataFrame, *, site_col: str, cate_col: str = "predicted_cate", pseudo_col: str = "dr_pseudo_outcome", min_n: int = 20, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `predictions` | `predictions: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `site_col` | `site_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `cate_col` | `cate_col: str = 'predicted_cate'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `pseudo_col` | `pseudo_col: str = 'dr_pseudo_outcome'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `min_n` | `min_n: int = 20` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `predictions`, `site_col`.
- Referenced columns must exist in the input table: `site_col`, `cate_col`, `pseudo_col`.

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

from thomaslab.heterogeneous_effects import site_cate_stability_report

result = site_cate_stability_report(
    df=sample_df,
    predictions=sample_df,
    site_col='site'
)

print(result)
~~~

### Related functions

- `validate_hte_inputs`
- `fit_t_learner`
- `fit_s_learner`
- `fit_dr_learner`
- `predict_cate`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/heterogeneous_effects.py#L1032`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L1032)
- Repository search: [site_cate_stability_report](https://github.com/appsplorer/thomaslab-core/search?q=site_cate_stability_report&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize held-out CATE behavior across sites without ranking sites.

### API inspection

~~~python
import inspect
from thomaslab.heterogeneous_effects import site_cate_stability_report

print(inspect.signature(site_cate_stability_report))
print(site_cate_stability_report.__doc__)
~~~

### Source

[`src/thomaslab/heterogeneous_effects.py#L1032`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L1032)

---

<!-- callable:thomaslab.heterogeneous_effects.transport_cate_distribution -->
## transport_cate_distribution

### Purpose

Compare source and external-target CATE distributions with sampling weights.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def transport_cate_distribution( model_bundle: dict[str, Any], source_df: pd.DataFrame, target_df: pd.DataFrame, *, probability_clip: float = 0.01, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `model_bundle` | `model_bundle: dict[str, Any]` | Yes | Model or model setting. Fit/tune only within the training design and preserve independent evaluation. |
| `source_df` | `source_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `target_df` | `target_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `probability_clip` | `probability_clip: float = 0.01` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `model_bundle`, `source_df`, `target_df`.

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

from thomaslab.heterogeneous_effects import transport_cate_distribution

result = transport_cate_distribution(
    model_bundle={},
    source_df=sample_df,
    target_df=sample_df
)

print(result)
~~~

### Related functions

- `validate_hte_inputs`
- `fit_t_learner`
- `fit_s_learner`
- `fit_dr_learner`
- `predict_cate`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/heterogeneous_effects.py#L1078`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L1078)
- Repository search: [transport_cate_distribution](https://github.com/appsplorer/thomaslab-core/search?q=transport_cate_distribution&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compare source and external-target CATE distributions with sampling weights.

This transports the distribution of a fitted CATE model over covariates. It is
not independent validation of the patient-level causal effect.

### API inspection

~~~python
import inspect
from thomaslab.heterogeneous_effects import transport_cate_distribution

print(inspect.signature(transport_cate_distribution))
print(transport_cate_distribution.__doc__)
~~~

### Source

[`src/thomaslab/heterogeneous_effects.py#L1078`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/heterogeneous_effects.py#L1078)

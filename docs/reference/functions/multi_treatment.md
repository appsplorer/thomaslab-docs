# thomaslab.multi_treatment

Multi-treatment comparative-effectiveness research utilities.

This module extends the binary heterogeneous-treatment-effect layer to three or
more mutually exclusive treatment strategies. It provides multinomial propensity
models, generalized-overlap diagnostics, multi-arm AIPW estimation, nested
cross-fitted doubly robust effect learning, research-policy evaluation, bootstrap
model-order uncertainty, site-specific comparative effects, and source-to-target
comparative-effect transport.

The outputs are research estimands. They are not patient-specific prescribing
recommendations, and a model-selected arm must not be described as the clinically
"best treatment" without independent validation, clinical governance, and an
appropriate decision context.

## Research-use boundary

Estimator execution does not establish causal identification assumptions. Define the estimand and review exchangeability, positivity, censoring, transportability, interference, measurement, and design-specific assumptions.

## Self-service orientation

- Related guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 12

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.multi_treatment.validate_multi_treatment_inputs -->
## validate_multi_treatment_inputs

### Purpose

Validate one-row-per-unit comparative-effectiveness input data.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_multi_treatment_inputs( df: pd.DataFrame, *, treatment_col: str, outcome_col: str, covariates: Sequence[str], outcome_type: str = "binary", ) -> dict[str, Any]
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

from thomaslab.multi_treatment import validate_multi_treatment_inputs

result = validate_multi_treatment_inputs(
    df=sample_df,
    treatment_col='treatment',
    outcome_col='outcome',
    covariates=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `generalized_overlap_diagnostics`
- `estimate_multiarm_aipw`
- `fit_multiarm_dr_learner`
- `predict_multiarm_effects`
- `pairwise_cate_predictions`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/multi_treatment.py#L212`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L212)
- Repository search: [validate_multi_treatment_inputs](https://github.com/appsplorer/thomaslab-core/search?q=validate_multi_treatment_inputs&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate one-row-per-unit comparative-effectiveness input data.

### API inspection

~~~python
import inspect
from thomaslab.multi_treatment import validate_multi_treatment_inputs

print(inspect.signature(validate_multi_treatment_inputs))
print(validate_multi_treatment_inputs.__doc__)
~~~

### Source

[`src/thomaslab/multi_treatment.py#L212`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L212)

---

<!-- callable:thomaslab.multi_treatment.generalized_overlap_diagnostics -->
## generalized_overlap_diagnostics

### Purpose

Audit generalized treatment support and multi-arm overlap weights.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def generalized_overlap_diagnostics( predictions: pd.DataFrame, *, arms: Sequence[Any], arm_keys: dict[Any, str], treatment_col: str = "treatment", probability_threshold: float = 0.05, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `predictions` | `predictions: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `arms` | `arms: Sequence[Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `arm_keys` | `arm_keys: dict[Any, str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `treatment_col` | `treatment_col: str = 'treatment'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `probability_threshold` | `probability_threshold: float = 0.05` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `predictions`, `arms`, `arm_keys`.
- Referenced columns must exist in the input table: `treatment_col`.

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

sample_value = "replace_with_validated_value"

from thomaslab.multi_treatment import generalized_overlap_diagnostics

result = generalized_overlap_diagnostics(
    predictions=sample_df,
    arms=sample_value,
    arm_keys={}
)

print(result)
~~~

### Related functions

- `validate_multi_treatment_inputs`
- `estimate_multiarm_aipw`
- `fit_multiarm_dr_learner`
- `predict_multiarm_effects`
- `pairwise_cate_predictions`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/multi_treatment.py#L366`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L366)
- Repository search: [generalized_overlap_diagnostics](https://github.com/appsplorer/thomaslab-core/search?q=generalized_overlap_diagnostics&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Audit generalized treatment support and multi-arm overlap weights.

### API inspection

~~~python
import inspect
from thomaslab.multi_treatment import generalized_overlap_diagnostics

print(inspect.signature(generalized_overlap_diagnostics))
print(generalized_overlap_diagnostics.__doc__)
~~~

### Source

[`src/thomaslab/multi_treatment.py#L366`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L366)

---

<!-- callable:thomaslab.multi_treatment.estimate_multiarm_aipw -->
## estimate_multiarm_aipw

### Purpose

Estimate all arm means and pairwise contrasts with cross-fitted AIPW.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def estimate_multiarm_aipw( df: pd.DataFrame, *, treatment_col: str, outcome_col: str, covariates: Sequence[str], reference_arm: Any, outcome_type: str = "binary", n_splits: int = 5, propensity_clip: float = 0.01, model_kind: str = "linear", ci: float = 0.95, random_state: int = 42, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `reference_arm` | `reference_arm: Any` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `outcome_type` | `outcome_type: str = 'binary'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `n_splits` | `n_splits: int = 5` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `propensity_clip` | `propensity_clip: float = 0.01` | No | Analysis weight/propensity input. Inspect support, positivity, extremes, and effective sample size where applicable. |
| `model_kind` | `model_kind: str = 'linear'` | No | Model or model setting. Fit/tune only within the training design and preserve independent evaluation. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `treatment_col`, `outcome_col`, `covariates`, `reference_arm`.
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

sample_value = "replace_with_validated_value"

from thomaslab.multi_treatment import estimate_multiarm_aipw

result = estimate_multiarm_aipw(
    df=sample_df,
    treatment_col='treatment',
    outcome_col='outcome',
    covariates=["feature_a", "feature_b"],
    reference_arm=sample_value
)

print(result)
~~~

### Related functions

- `validate_multi_treatment_inputs`
- `generalized_overlap_diagnostics`
- `fit_multiarm_dr_learner`
- `predict_multiarm_effects`
- `pairwise_cate_predictions`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/multi_treatment.py#L462`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L462)
- Repository search: [estimate_multiarm_aipw](https://github.com/appsplorer/thomaslab-core/search?q=estimate_multiarm_aipw&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate all arm means and pairwise contrasts with cross-fitted AIPW.

### API inspection

~~~python
import inspect
from thomaslab.multi_treatment import estimate_multiarm_aipw

print(inspect.signature(estimate_multiarm_aipw))
print(estimate_multiarm_aipw.__doc__)
~~~

### Source

[`src/thomaslab/multi_treatment.py#L462`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L462)

---

<!-- callable:thomaslab.multi_treatment.fit_multiarm_dr_learner -->
## fit_multiarm_dr_learner

### Purpose

Fit nested cross-fitted multi-arm DR effect models versus a reference arm.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fit_multiarm_dr_learner( df: pd.DataFrame, *, treatment_col: str, outcome_col: str, covariates: Sequence[str], reference_arm: Any, outcome_type: str = "binary", n_splits: int = 5, inner_splits: int = 3, propensity_clip: float = 0.01, nuisance_model_kind: str = "linear", effect_model_kind: str = "forest", random_state: int = 42, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `reference_arm` | `reference_arm: Any` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
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
- Required arguments: `df`, `treatment_col`, `outcome_col`, `covariates`, `reference_arm`.
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

sample_value = "replace_with_validated_value"

from thomaslab.multi_treatment import fit_multiarm_dr_learner

result = fit_multiarm_dr_learner(
    df=sample_df,
    treatment_col='treatment',
    outcome_col='outcome',
    covariates=["feature_a", "feature_b"],
    reference_arm=sample_value
)

print(result)
~~~

### Related functions

- `validate_multi_treatment_inputs`
- `generalized_overlap_diagnostics`
- `estimate_multiarm_aipw`
- `predict_multiarm_effects`
- `pairwise_cate_predictions`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/multi_treatment.py#L575`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L575)
- Repository search: [fit_multiarm_dr_learner](https://github.com/appsplorer/thomaslab-core/search?q=fit_multiarm_dr_learner&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Fit nested cross-fitted multi-arm DR effect models versus a reference arm.

### API inspection

~~~python
import inspect
from thomaslab.multi_treatment import fit_multiarm_dr_learner

print(inspect.signature(fit_multiarm_dr_learner))
print(fit_multiarm_dr_learner.__doc__)
~~~

### Source

[`src/thomaslab/multi_treatment.py#L575`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L575)

---

<!-- callable:thomaslab.multi_treatment.predict_multiarm_effects -->
## predict_multiarm_effects

### Purpose

Predict reference-arm CATEs and model outcome scores for new covariates.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def predict_multiarm_effects( model_bundle: dict[str, Any], new_df: pd.DataFrame, ) -> pd.DataFrame
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

from thomaslab.multi_treatment import predict_multiarm_effects

result = predict_multiarm_effects(
    model_bundle={},
    new_df=sample_df
)

print(result)
~~~

### Related functions

- `validate_multi_treatment_inputs`
- `generalized_overlap_diagnostics`
- `estimate_multiarm_aipw`
- `fit_multiarm_dr_learner`
- `pairwise_cate_predictions`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/multi_treatment.py#L786`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L786)
- Repository search: [predict_multiarm_effects](https://github.com/appsplorer/thomaslab-core/search?q=predict_multiarm_effects&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Predict reference-arm CATEs and model outcome scores for new covariates.

### API inspection

~~~python
import inspect
from thomaslab.multi_treatment import predict_multiarm_effects

print(inspect.signature(predict_multiarm_effects))
print(predict_multiarm_effects.__doc__)
~~~

### Source

[`src/thomaslab/multi_treatment.py#L786`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L786)

---

<!-- callable:thomaslab.multi_treatment.pairwise_cate_predictions -->
## pairwise_cate_predictions

### Purpose

Derive every pairwise CATE from reference-arm CATE predictions.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def pairwise_cate_predictions( predictions: pd.DataFrame, *, arms: Sequence[Any], arm_keys: dict[Any, str], ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `predictions` | `predictions: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `arms` | `arms: Sequence[Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `arm_keys` | `arm_keys: dict[Any, str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `predictions`, `arms`, `arm_keys`.

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

sample_value = "replace_with_validated_value"

from thomaslab.multi_treatment import pairwise_cate_predictions

result = pairwise_cate_predictions(
    predictions=sample_df,
    arms=sample_value,
    arm_keys={}
)

print(result)
~~~

### Related functions

- `validate_multi_treatment_inputs`
- `generalized_overlap_diagnostics`
- `estimate_multiarm_aipw`
- `fit_multiarm_dr_learner`
- `predict_multiarm_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/multi_treatment.py#L823`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L823)
- Repository search: [pairwise_cate_predictions](https://github.com/appsplorer/thomaslab-core/search?q=pairwise_cate_predictions&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Derive every pairwise CATE from reference-arm CATE predictions.

If all arm-specific CATEs are expressed relative to the same reference arm,
then the CATE for arm a versus arm b is tau_a:ref - tau_b:ref. The function
returns all unordered pairwise comparisons without selecting a preferred arm.

### API inspection

~~~python
import inspect
from thomaslab.multi_treatment import pairwise_cate_predictions

print(inspect.signature(pairwise_cate_predictions))
print(pairwise_cate_predictions.__doc__)
~~~

### Source

[`src/thomaslab/multi_treatment.py#L823`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L823)

---

<!-- callable:thomaslab.multi_treatment.summarize_reference_cate -->
## summarize_reference_cate

### Purpose

Summarize reference-arm CATE predictions and DR pseudo contrasts.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_reference_cate( predictions: pd.DataFrame, *, arms: Sequence[Any], arm_keys: dict[Any, str], reference_arm: Any, ci: float = 0.95, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `predictions` | `predictions: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `arms` | `arms: Sequence[Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `arm_keys` | `arm_keys: dict[Any, str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `reference_arm` | `reference_arm: Any` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `predictions`, `arms`, `arm_keys`, `reference_arm`.

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

sample_value = "replace_with_validated_value"

from thomaslab.multi_treatment import summarize_reference_cate

result = summarize_reference_cate(
    predictions=sample_df,
    arms=sample_value,
    arm_keys={},
    reference_arm=sample_value
)

print(result)
~~~

### Related functions

- `validate_multi_treatment_inputs`
- `generalized_overlap_diagnostics`
- `estimate_multiarm_aipw`
- `fit_multiarm_dr_learner`
- `predict_multiarm_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/multi_treatment.py#L871`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L871)
- Repository search: [summarize_reference_cate](https://github.com/appsplorer/thomaslab-core/search?q=summarize_reference_cate&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize reference-arm CATE predictions and DR pseudo contrasts.

### API inspection

~~~python
import inspect
from thomaslab.multi_treatment import summarize_reference_cate

print(inspect.signature(summarize_reference_cate))
print(summarize_reference_cate.__doc__)
~~~

### Source

[`src/thomaslab/multi_treatment.py#L871`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L871)

---

<!-- callable:thomaslab.multi_treatment.derive_multiarm_research_policy -->
## derive_multiarm_research_policy

### Purpose

Construct an exploratory multi-arm model policy from held-out scores.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def derive_multiarm_research_policy( predictions: pd.DataFrame, *, arms: Sequence[Any], arm_keys: dict[Any, str], higher_outcome_better: bool, minimum_margin: float = 0.0, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `predictions` | `predictions: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `arms` | `arms: Sequence[Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `arm_keys` | `arm_keys: dict[Any, str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `higher_outcome_better` | `higher_outcome_better: bool` | Yes | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `minimum_margin` | `minimum_margin: float = 0.0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `predictions`, `arms`, `arm_keys`, `higher_outcome_better`.

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

sample_value = "replace_with_validated_value"

from thomaslab.multi_treatment import derive_multiarm_research_policy

result = derive_multiarm_research_policy(
    predictions=sample_df,
    arms=sample_value,
    arm_keys={},
    higher_outcome_better=False
)

print(result)
~~~

### Related functions

- `validate_multi_treatment_inputs`
- `generalized_overlap_diagnostics`
- `estimate_multiarm_aipw`
- `fit_multiarm_dr_learner`
- `predict_multiarm_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/multi_treatment.py#L931`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L931)
- Repository search: [derive_multiarm_research_policy](https://github.com/appsplorer/thomaslab-core/search?q=derive_multiarm_research_policy&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Construct an exploratory multi-arm model policy from held-out scores.

The returned arm is a model-selected research strategy, not a treatment
recommendation. Rows below the requested score margin are marked as abstained.

### API inspection

~~~python
import inspect
from thomaslab.multi_treatment import derive_multiarm_research_policy

print(inspect.signature(derive_multiarm_research_policy))
print(derive_multiarm_research_policy.__doc__)
~~~

### Source

[`src/thomaslab/multi_treatment.py#L931`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L931)

---

<!-- callable:thomaslab.multi_treatment.evaluate_multiarm_research_policy -->
## evaluate_multiarm_research_policy

### Purpose

Estimate a multi-arm research policy value using held-out DR nuisances.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def evaluate_multiarm_research_policy( predictions: pd.DataFrame, *, policy: Sequence[Any] | pd.Series, arms: Sequence[Any], arm_keys: dict[Any, str], higher_outcome_better: bool, out_of_fold_policy_predictions_asserted: bool = False, ci: float = 0.95, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `predictions` | `predictions: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `policy` | `policy: Sequence[Any] \| pd.Series` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `arms` | `arms: Sequence[Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `arm_keys` | `arm_keys: dict[Any, str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `higher_outcome_better` | `higher_outcome_better: bool` | Yes | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `out_of_fold_policy_predictions_asserted` | `out_of_fold_policy_predictions_asserted: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `predictions`, `policy`, `arms`, `arm_keys`, `higher_outcome_better`.

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

sample_value = "replace_with_validated_value"

from thomaslab.multi_treatment import evaluate_multiarm_research_policy

result = evaluate_multiarm_research_policy(
    predictions=sample_df,
    policy=sample_series,
    arms=sample_value,
    arm_keys={},
    higher_outcome_better=False
)

print(result)
~~~

### Related functions

- `validate_multi_treatment_inputs`
- `generalized_overlap_diagnostics`
- `estimate_multiarm_aipw`
- `fit_multiarm_dr_learner`
- `predict_multiarm_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/multi_treatment.py#L973`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L973)
- Repository search: [evaluate_multiarm_research_policy](https://github.com/appsplorer/thomaslab-core/search?q=evaluate_multiarm_research_policy&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate a multi-arm research policy value using held-out DR nuisances.

### API inspection

~~~python
import inspect
from thomaslab.multi_treatment import evaluate_multiarm_research_policy

print(inspect.signature(evaluate_multiarm_research_policy))
print(evaluate_multiarm_research_policy.__doc__)
~~~

### Source

[`src/thomaslab/multi_treatment.py#L973`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L973)

---

<!-- callable:thomaslab.multi_treatment.bootstrap_multiarm_model_order_uncertainty -->
## bootstrap_multiarm_model_order_uncertainty

### Purpose

Bootstrap model-order uncertainty without creating a treatment recommendation.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def bootstrap_multiarm_model_order_uncertainty( training_df: pd.DataFrame, target_df: pd.DataFrame, *, treatment_col: str, outcome_col: str, covariates: Sequence[str], reference_arm: Any, higher_outcome_better: bool, outcome_type: str = "binary", n_bootstrap: int = 100, n_splits: int = 3, inner_splits: int = 2, nuisance_model_kind: str = "linear", effect_model_kind: str = "linear", random_state: int = 42, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `training_df` | `training_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `target_df` | `target_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `reference_arm` | `reference_arm: Any` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `higher_outcome_better` | `higher_outcome_better: bool` | Yes | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `outcome_type` | `outcome_type: str = 'binary'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `n_bootstrap` | `n_bootstrap: int = 100` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `n_splits` | `n_splits: int = 3` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `inner_splits` | `inner_splits: int = 2` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `nuisance_model_kind` | `nuisance_model_kind: str = 'linear'` | No | Model or model setting. Fit/tune only within the training design and preserve independent evaluation. |
| `effect_model_kind` | `effect_model_kind: str = 'linear'` | No | Model or model setting. Fit/tune only within the training design and preserve independent evaluation. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `training_df`, `target_df`, `treatment_col`, `outcome_col`, `covariates`, `reference_arm`, `higher_outcome_better`.
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

sample_value = "replace_with_validated_value"

from thomaslab.multi_treatment import bootstrap_multiarm_model_order_uncertainty

result = bootstrap_multiarm_model_order_uncertainty(
    training_df=sample_df,
    target_df=sample_df,
    treatment_col='treatment',
    outcome_col='outcome',
    covariates=["feature_a", "feature_b"],
    reference_arm=sample_value,
    higher_outcome_better=False
)

print(result)
~~~

### Related functions

- `validate_multi_treatment_inputs`
- `generalized_overlap_diagnostics`
- `estimate_multiarm_aipw`
- `fit_multiarm_dr_learner`
- `predict_multiarm_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/multi_treatment.py#L1055`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L1055)
- Repository search: [bootstrap_multiarm_model_order_uncertainty](https://github.com/appsplorer/thomaslab-core/search?q=bootstrap_multiarm_model_order_uncertainty&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Bootstrap model-order uncertainty without creating a treatment recommendation.

### API inspection

~~~python
import inspect
from thomaslab.multi_treatment import bootstrap_multiarm_model_order_uncertainty

print(inspect.signature(bootstrap_multiarm_model_order_uncertainty))
print(bootstrap_multiarm_model_order_uncertainty.__doc__)
~~~

### Source

[`src/thomaslab/multi_treatment.py#L1055`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L1055)

---

<!-- callable:thomaslab.multi_treatment.site_multiarm_effects -->
## site_multiarm_effects

### Purpose

Estimate site-specific multi-arm AIPW contrasts without ranking sites.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def site_multiarm_effects( df: pd.DataFrame, *, site_col: str, treatment_col: str, outcome_col: str, covariates: Sequence[str], reference_arm: Any, outcome_type: str = "binary", n_splits: int = 3, random_state: int = 42, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `site_col` | `site_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treatment_col` | `treatment_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `covariates` | `covariates: Sequence[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `reference_arm` | `reference_arm: Any` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `outcome_type` | `outcome_type: str = 'binary'` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `n_splits` | `n_splits: int = 3` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `site_col`, `treatment_col`, `outcome_col`, `covariates`, `reference_arm`.
- Referenced columns must exist in the input table: `site_col`, `treatment_col`, `outcome_col`.

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

sample_value = "replace_with_validated_value"

from thomaslab.multi_treatment import site_multiarm_effects

result = site_multiarm_effects(
    df=sample_df,
    site_col='site',
    treatment_col='treatment',
    outcome_col='outcome',
    covariates=["feature_a", "feature_b"],
    reference_arm=sample_value
)

print(result)
~~~

### Related functions

- `validate_multi_treatment_inputs`
- `generalized_overlap_diagnostics`
- `estimate_multiarm_aipw`
- `fit_multiarm_dr_learner`
- `predict_multiarm_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/multi_treatment.py#L1162`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L1162)
- Repository search: [site_multiarm_effects](https://github.com/appsplorer/thomaslab-core/search?q=site_multiarm_effects&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Estimate site-specific multi-arm AIPW contrasts without ranking sites.

### API inspection

~~~python
import inspect
from thomaslab.multi_treatment import site_multiarm_effects

print(inspect.signature(site_multiarm_effects))
print(site_multiarm_effects.__doc__)
~~~

### Source

[`src/thomaslab/multi_treatment.py#L1162`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L1162)

---

<!-- callable:thomaslab.multi_treatment.transport_multiarm_effect_distribution -->
## transport_multiarm_effect_distribution

### Purpose

Transport fitted multi-arm comparative-effect distributions to a target.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def transport_multiarm_effect_distribution( model_bundle: dict[str, Any], source_df: pd.DataFrame, target_df: pd.DataFrame, *, probability_clip: float = 0.01, ) -> dict[str, Any]
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

from thomaslab.multi_treatment import transport_multiarm_effect_distribution

result = transport_multiarm_effect_distribution(
    model_bundle={},
    source_df=sample_df,
    target_df=sample_df
)

print(result)
~~~

### Related functions

- `validate_multi_treatment_inputs`
- `generalized_overlap_diagnostics`
- `estimate_multiarm_aipw`
- `fit_multiarm_dr_learner`
- `predict_multiarm_effects`

### Related workflow

- Guide: [Causal Inference](../../guides/causal-inference.md)
- Guided notebooks: Notebooks 22 and 36–55
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/multi_treatment.py#L1227`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L1227)
- Repository search: [transport_multiarm_effect_distribution](https://github.com/appsplorer/thomaslab-core/search?q=transport_multiarm_effect_distribution&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Transport fitted multi-arm comparative-effect distributions to a target.

### API inspection

~~~python
import inspect
from thomaslab.multi_treatment import transport_multiarm_effect_distribution

print(inspect.signature(transport_multiarm_effect_distribution))
print(transport_multiarm_effect_distribution.__doc__)
~~~

### Source

[`src/thomaslab/multi_treatment.py#L1227`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/multi_treatment.py#L1227)

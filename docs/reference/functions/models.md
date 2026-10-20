# thomaslab.models

Deep-learning, trajectory, and time-series utilities for clinical research.

## Research-use boundary

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

## Self-service orientation

- Related guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 3

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.models.format_time_series_tensor -->
## format_time_series_tensor

### Purpose

Convert longitudinal rows into padded 3D PyTorch tensors.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def format_time_series_tensor( df: Any, id_col: str, time_col: str, feature_cols: list[str], max_seq_len: int = 100, *, fill_value: float = 0.0, standardize: bool = False, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: Any` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `id_col` | `id_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `feature_cols` | `feature_cols: list[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `max_seq_len` | `max_seq_len: int = 100` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `fill_value` | `fill_value: float = 0.0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `standardize` | `standardize: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `id_col`, `time_col`, `feature_cols`.
- Referenced columns must exist in the input table: `id_col`, `time_col`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

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

from thomaslab.models import format_time_series_tensor

result = format_time_series_tensor(
    df=sample_df,
    id_col='patient_id',
    time_col='event_date',
    feature_cols=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `fit_deep_survival_model`
- `extract_phenotype_clusters`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/models.py#L266`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/models.py#L266)
- Repository search: [format_time_series_tensor](https://github.com/appsplorer/thomaslab-core/search?q=format_time_series_tensor&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Convert longitudinal rows into padded 3D PyTorch tensors.

Sequences are ordered by ``time_col`` and truncated to the most recent
``max_seq_len`` observations. A boolean mask and original patient identifiers
are returned so padding is never mistaken for observed clinical data.

### API inspection

~~~python
import inspect
from thomaslab.models import format_time_series_tensor

print(inspect.signature(format_time_series_tensor))
print(format_time_series_tensor.__doc__)
~~~

### Source

[`src/thomaslab/models.py#L266`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/models.py#L266)

---

<!-- callable:thomaslab.models.fit_deep_survival_model -->
## fit_deep_survival_model

### Purpose

Fit a DeepHit-style discrete-time competing-risk neural network.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def fit_deep_survival_model( tensor_data: Any, event_times: Any, event_indicators: Any, model_type: str = "DeepHit", *, n_time_bins: int = 20, hidden_dims: tuple[int, ...] = (64, 32), dropout: float = 0.1, learning_rate: float = 1e-3, epochs: int = 100, batch_size: int = 256, ranking_weight: float = 0.1, ranking_pairs_per_batch: int = 512, random_state: int = 42, device: str | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `tensor_data` | `tensor_data: Any` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `event_times` | `event_times: Any` | Yes | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `event_indicators` | `event_indicators: Any` | Yes | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `model_type` | `model_type: str = 'DeepHit'` | No | Model or model setting. Fit/tune only within the training design and preserve independent evaluation. |
| `n_time_bins` | `n_time_bins: int = 20` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `hidden_dims` | `hidden_dims: tuple[int, ...] = (64, 32)` | No | Identifier or identifier column. Confirm uniqueness/grouping semantics before analysis. |
| `dropout` | `dropout: float = 0.1` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `learning_rate` | `learning_rate: float = 0.001` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `epochs` | `epochs: int = 100` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `batch_size` | `batch_size: int = 256` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `ranking_weight` | `ranking_weight: float = 0.1` | No | Analysis weight/propensity input. Inspect support, positivity, extremes, and effective sample size where applicable. |
| `ranking_pairs_per_batch` | `ranking_pairs_per_batch: int = 512` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |
| `device` | `device: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `tensor_data`, `event_times`, `event_indicators`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import numpy as np
import torch

sample_event_times = np.array([10.0, 20.0, 15.0, 25.0])

sample_event_indicators = np.array([1, 0, 2, 1])

sample_tensor_data = torch.tensor(
    [[[1.0, 2.0], [1.2, 2.1]], [[0.7, 1.4], [0.9, 1.6]]],
    dtype=torch.float32,
)

from thomaslab.models import fit_deep_survival_model

result = fit_deep_survival_model(
    tensor_data=sample_tensor_data,
    event_times=sample_event_times,
    event_indicators=sample_event_indicators
)

print(result)
~~~

### Related functions

- `format_time_series_tensor`
- `extract_phenotype_clusters`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/models.py#L375`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/models.py#L375)
- Repository search: [fit_deep_survival_model](https://github.com/appsplorer/thomaslab-core/search?q=fit_deep_survival_model&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Fit a DeepHit-style discrete-time competing-risk neural network.

Event indicators use ``0`` for censoring and ``1..K`` for competing causes.
The network directly models probability mass over cause/time cells plus survival
beyond the modeled horizon. The loss combines censoring-aware likelihood with a
sampled cause-specific ranking term, following the core DeepHit design idea.

Notes
-----
This implementation is intended for reproducible research and method prototyping.
It is not a drop-in reproduction of every architectural detail in the original
DeepHit paper; hyperparameters and external validation remain study-specific.

### API inspection

~~~python
import inspect
from thomaslab.models import fit_deep_survival_model

print(inspect.signature(fit_deep_survival_model))
print(fit_deep_survival_model.__doc__)
~~~

### Source

[`src/thomaslab/models.py#L375`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/models.py#L375)

---

<!-- callable:thomaslab.models.extract_phenotype_clusters -->
## extract_phenotype_clusters

### Purpose

Discover unsupervised patient phenotypes with autoencoder + K-Means.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def extract_phenotype_clusters( df: Any, feature_cols: list[str], n_clusters: int = 4, method: str = "autoencoder_kmeans", *, latent_dim: int | None = None, epochs: int = 100, random_state: int = 42, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: Any` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `feature_cols` | `feature_cols: list[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `n_clusters` | `n_clusters: int = 4` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `method` | `method: str = 'autoencoder_kmeans'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `latent_dim` | `latent_dim: int \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `epochs` | `epochs: int = 100` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `feature_cols`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Protect patient/site/time separation, leakage controls, calibration, uncertainty, subgroup behavior, and external-validation provenance.

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

from thomaslab.models import extract_phenotype_clusters

result = extract_phenotype_clusters(
    df=sample_df,
    feature_cols=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `format_time_series_tensor`
- `fit_deep_survival_model`

### Related workflow

- Guide: [Evaluation](../../guides/evaluation.md)
- Guided notebooks: Notebooks 21–23 and 29–30
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/models.py#L554`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/models.py#L554)
- Repository search: [extract_phenotype_clusters](https://github.com/appsplorer/thomaslab-core/search?q=extract_phenotype_clusters&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Discover unsupervised patient phenotypes with autoencoder + K-Means.

``method='kmeans'`` provides a deterministic non-neural baseline. The default
trains a compact PyTorch autoencoder on standardized complete numeric features
and clusters its latent representation.

### API inspection

~~~python
import inspect
from thomaslab.models import extract_phenotype_clusters

print(inspect.signature(extract_phenotype_clusters))
print(extract_phenotype_clusters.__doc__)
~~~

### Source

[`src/thomaslab/models.py#L554`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/models.py#L554)

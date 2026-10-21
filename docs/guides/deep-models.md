# Longitudinal and deep survival models

`thomaslab.models` provides research-oriented building blocks for longitudinal neural modeling.

## Padded longitudinal tensors

```python
from thomaslab.models import format_time_series_tensor

batch = format_time_series_tensor(
    events,
    id_col="patient_id",
    time_col="event_time",
    feature_cols=["creatinine", "hemoglobin", "heart_rate"],
    max_seq_len=100,
)
```

The returned dictionary includes the 3D tensor, a padding mask, sequence lengths, patient IDs, and time metadata.

## DeepHit-style competing risks

```python
from thomaslab.models import fit_deep_survival_model

result = fit_deep_survival_model(
    batch,
    event_times=followup_days,
    event_indicators=event_codes,  # 0=censored; 1..K=causes
    model_type="DeepHit",
)
```

The implementation models discrete cause/time probability mass and uses a censoring-aware likelihood plus a sampled ranking component. It is intended for research prototyping; architecture, discretization, hyperparameters, calibration, and external validation remain study-specific.

## Phenotype discovery

```python
from thomaslab.models import extract_phenotype_clusters

clusters = extract_phenotype_clusters(
    baseline_matrix,
    feature_cols=features,
    n_clusters=4,
    method="autoencoder_kmeans",
)
```

Unsupervised clusters are hypotheses, not clinical diagnoses. Assess stability, site transportability, and clinical interpretability before assigning phenotype meaning.

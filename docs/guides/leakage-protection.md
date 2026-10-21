# Leakage protection

Leakage controls are a pre-model safety gate, not a post-hoc explanation for unexpectedly high performance.

## Feature windows

Maintain a feature metadata table:

| feature | window_start_days | window_end_days |
|---|---:|---:|
| age | 0 | 0 |
| creatinine_latest | -30 | 0 |
| post_bleed_hgb | 1 | 7 |

```python
from thomaslab.leakage import audit_feature_windows

audit = audit_feature_windows(feature_metadata)
```

Any feature whose window ends after the allowed boundary is blocked by default.

## Split leakage

Use `detect_duplicate_patient_split`, `detect_site_leakage`, and `detect_temporal_split_violation` to verify the intended validation design.

Site overlap is not inherently leakage for ordinary patient-level validation. It becomes a violation only when the protocol explicitly requires disjoint sites.

## Target proxies

`detect_outcome_proxy_features` uses conservative column-name heuristics to surface suspicious features such as `days_to_bleeding` or `post_event_hb`. These are review candidates, not definitive causal judgments.

## Strict audit

```python
from thomaslab.leakage import audit_dataset_leakage

audit_dataset_leakage(
    dataset,
    target_col="outcome",
    feature_cols=features,
    split_col="split",
    feature_metadata=feature_metadata,
    strict=True,
)
```

Strict mode blocks direct target leakage, documented post-index features, patient split overlap, and required site-disjoint violations.

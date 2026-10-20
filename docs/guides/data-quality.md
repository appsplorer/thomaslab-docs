# Clinical data quality

`thomaslab.quality` provides explicit checks for the problems that commonly invalidate EHR/RWE analyses before modeling begins.

## Recommended sequence

```python
from thomaslab.quality import generate_data_quality_report

report = generate_data_quality_report(
    cohort,
    required_columns=["patient_id", "index_date", "age"],
    column_types={"patient_id": "string", "index_date": "datetime", "age": "numeric"},
    numeric_ranges={"age": (18, 120)},
    duplicate_key=["patient_id", "index_date"],
    index_date_col="index_date",
    feature_date_cols=["last_lab_date", "last_medication_date"],
)
```

The report separates schema problems, missingness, out-of-range values, duplicates, and temporal leakage.

## Range checks are protocol-defined

`check_numeric_ranges` deliberately requires caller-supplied limits. A universal hard-coded physiologic range can be wrong when units, assay type, age, pregnancy status, or study context differ.

## Temporal leakage

`detect_temporal_leakage` compares feature timestamps with the patient-specific index date. Any feature measured after the permitted prediction boundary should be reviewed before modeling.

## Multi-site transportability

`compare_site_distributions` quantifies numeric shifts with standardized mean difference and Wasserstein distance, and categorical shifts with total variation distance. These diagnostics help identify heterogeneity; they do not prove that two sites are transportable.

# High-performance EHR processing

The v0.2 data layer adds DuckDB, Polars, PyArrow-compatible workflows, Numba matching, and optional GPU acceleration.

## Out-of-core Parquet SQL

```python
from thomaslab.data import connect_duckdb_parquet

con = connect_duckdb_parquet("/data/mimiciv/**/labevents*.parquet")
cohort = con.execute("""
    SELECT subject_id, itemid, charttime, valuenum
    FROM ehr_parquet
    WHERE valuenum IS NOT NULL
""").df()
```

DuckDB queries the files directly; the complete dataset does not need to be materialized in Pandas.

## Structural source-schema adaptation

```python
from thomaslab.data import convert_schema_to_omop

measurement = convert_schema_to_omop(
    mimic_labs,
    source_schema="MIMIC-IV",
    source_table="labevents",
    concept_mapping=verified_mapping,
)
```

!!! warning
    Schema translation and vocabulary mapping are separate tasks. When no verified source-to-standard concept map is supplied, standard OMOP concept IDs remain `0` rather than being guessed.

## Polars lookback features

```python
from thomaslab.data import extract_longitudinal_features_polars

features = extract_longitudinal_features_polars(
    labs,
    patient_id_col="patient_id",
    lab_col="lab",
    window_days_list=[7, 30, 90, 365],
    value_col="value",
    date_col="date",
    index_date_col="index_date",
)
```

The result is a long-form feature table containing mean, minimum, maximum, observation count, and least-squares slope per day for each patient/lab/window.

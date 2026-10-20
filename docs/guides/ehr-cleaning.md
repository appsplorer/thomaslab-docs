# EHR cleaning and canonical contracts

Version 0.5 introduces a guarded cleaning layer between schema adaptation and downstream research analysis.

## Why a separate cleaning layer?

Changing a column name from `RESULT_NUM` to `lab_value` does not make the value valid. A robust pipeline must separately evaluate:

- missing-value sentinels;
- date parsing;
- units;
- duplicates;
- numeric plausibility;
- statistical outliers;
- coding normalization;
- structural contract requirements.

## Generic cleaning

```python
from thomaslab.cleaning import clean_ehr_dataset

clean, report = clean_ehr_dataset(
    raw,
    schema="schemas/site_a.yaml",
    config="configs/cleaning/default.yaml",
    required_columns=["patient_id", "event_date"],
)
```

The report records schema mappings, missing-token replacements, date parse failures, range violations and deduplication counts.

## Do not use universal clinical ranges blindly

`detect_impossible_values()` accepts caller-defined ranges rather than embedding universal thresholds. Plausible limits depend on population, units, instruments and protocol.

```python
from thomaslab.cleaning import detect_impossible_values

violations = detect_impossible_values(
    df,
    {
        "age": {"min": 18, "max": 110},
        "baseline_bmi": {"min": 10, "max": 80},
    },
)
```

## Unit normalization is fail-closed

```python
from thomaslab.cleaning import standardize_units

creatinine = standardize_units(
    labs,
    value_col="lab_value",
    unit_col="lab_unit",
    target_unit="mg/dL",
    analyte="creatinine",
)
```

Molecular conversions such as creatinine µmol/L to mg/dL or glucose mmol/L to mg/dL require the analyte to be named explicitly. Unknown conversions raise in strict mode.

## Raw clinical codes are retained

Domain cleaners preserve raw diagnosis/medication codes before normalization. This is essential for auditing, reconciliation and reproducibility.

## Contracts after cleaning

```python
from thomaslab.contracts import build_data_contract, validate_domain_contract

contract = build_data_contract(
    clean,
    domain="measurement",
    dataset_name="site_a_labs",
)

validation = validate_domain_contract(clean, contract)
```

Contracts are structural. They do not replace clinical phenotype validation, terminology mapping, leakage checks or protocol review.

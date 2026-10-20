# Schema adapters for unfamiliar datasets

The schema-adapter layer lets the research code operate on a stable internal vocabulary even when partner sites use different column names.

## Architecture

```text
Incoming dataset
      |
      v
Explicit YAML mapping
      |
      v
Exact alias / regex / conservative fuzzy matching
      |
      v
Mapping audit + required-column validation
      |
      v
Canonical thomaslab schema
      |
      v
EHR / PGx / causal / NLP / evaluation workflows
```

## Recommended workflow

1. Load the raw table without manually renaming it.
2. Run `generate_schema_template(raw.columns, "schemas/site.yaml")`.
3. Review the generated YAML with a domain expert.
4. Correct any semantically wrong suggestions.
5. Call `standardize_schema(..., mapping="schemas/site.yaml", required_columns=[...])`.
6. Save the mapping file with the study code so the transformation is reproducible.

## Two-line use

```python
import pandas as pd
from thomaslab.data import standardize_schema

raw = pd.read_csv("partner_hospital.csv")
clean, audit = standardize_schema(
    raw,
    mapping="schemas/partner_hospital.yaml",
    required_columns=["patient_id", "age", "event_date"],
    return_report=True,
)
```

The same function preserves the input table type for Pandas, Polars, and DuckDB relations.

## Why fuzzy matching is intentionally conservative

A column named `result` could be a lab value, an outcome label, or text. A column named `date` could represent specimen collection, admission, dispensing, procedure, or follow-up. Therefore fuzzy matching only proposes a rename when the best candidate clears the similarity threshold and is sufficiently separated from the next candidate.

Ambiguous columns remain unresolved. Required ambiguous fields cause a strict-mode error.

## YAML format

```yaml
dataset_name: emory_cardiovascular_cohort
required_columns:
  - patient_id
  - age
  - event_date
columns:
  patient_id: MRN_NUM
  age: AGE_AT_PCI
  sex: GENDER_DESC
  event_date: PROC_DATETIME
  icd_code: DX_ICD10
  rx_code: MED_NDC_CODE
```

Explicit mappings always override automatic matching.

## Clinical validation remains necessary

Schema adaptation standardizes **names**, not clinical meaning. It does not prove that:

- a timestamp is the correct index date;
- a numeric value has the expected unit;
- an ICD/NDC/RxNorm field uses the claimed vocabulary;
- a race/ethnicity field has the intended semantics;
- a variable was observed before time zero;
- two sites encoded the same construct identically.

Use the adapter with the data-quality and leakage checks, not instead of them.

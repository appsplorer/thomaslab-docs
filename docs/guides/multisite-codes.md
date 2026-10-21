# Multi-site harmonisation and terminology

Multi-institution studies need more than column alignment. Sites can differ in variable availability, units, category labels, code coverage, assay panels, and documentation workflows.

## Harmonisation audit

```python
from thomaslab.harmonize import generate_harmonization_report

report = generate_harmonization_report(
    {"site_a": site_a, "site_b": site_b},
    site_col="site_id",
    shift_columns=["age", "sex", "creatinine"],
)
```

Use `compare_site_schemas`, `compare_site_units`, `compare_site_missingness`, and `compare_site_code_coverage` before pooling data. `detect_site_shift` reports standardized mean differences for numeric variables and total-variation distance for categorical variables; these are diagnostics, not automatic reasons to exclude a site.

## Unit harmonisation

`harmonize_measurement_units` routes each analyte through the guarded unit converter. Molecular conversion requires an analyte-specific verified conversion; unknown units fail in strict mode.

## Code-set infrastructure

`thomaslab.codes` provides:

- format-level validators for ICD-9/10, CPT, HCPCS, LOINC, RxNorm and NDC11;
- conservative normalizers;
- explicit mapping-table application;
- wildcard/prefix expansion against an explicit reference universe;
- code-set diffs and SHA-256 provenance manifests.

It intentionally does **not** invent ICD↔SNOMED, NDC↔RxNorm, or local-code↔standard-code crosswalks. Those require reviewed terminology resources and release/version provenance.

Example code-set files live under `codesets/`.

# Versioned phenotypes and cardiovascular endpoints

`thomaslab-core` keeps clinical phenotype definitions outside core Python whenever possible. This makes changes reviewable and prevents a code-list change from being hidden inside an analysis function.

## Recommended workflow

1. Create or select a versioned phenotype YAML.
2. Record terminology/system version and source/protocol.
3. Apply the phenotype to canonical event data.
4. Validate against chart review or another reference standard when required.
5. Build composite endpoints from named component events.
6. Run sensitivity analyses with alternative reasonable definitions.
7. Freeze the phenotype files with the manuscript code and provenance bundle.

```python
from thomaslab.phenotypes import apply_structured_phenotype

mi = apply_structured_phenotype(
    diagnosis_events,
    "phenotypes/study/mi.yaml",
    code_col="icd_code",
)
```

## MAE and MACE

`build_mae_endpoint()` contains a convenience default for the **component labels** used in Thomas et al. JAHA 2022: all-cause death, MI, ischemic stroke, stent thrombosis, and hospitalization for unstable angina. It does **not** provide hidden diagnosis/procedure code lists for those events.

`build_mace_endpoint()` intentionally requires the caller to provide components because MACE definitions vary across studies.

## NLP + structured evidence

`combine_structured_nlp_phenotype()` supports explicit `or`, `and`, and `structured_preferred` logic. It does not assume that NLP evidence is equivalent to adjudication.

## Validation

Use `validate_against_gold_standard()` for sensitivity, specificity, PPV, NPV and F1 against adjudicated binary labels. Use `phenotype_sensitivity_analysis()` to quantify prevalence changes across alternative definitions.

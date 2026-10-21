# Clinical assumptions

This page documents assumptions that are important enough to make explicit.

## CKD-EPI 2021

`calculate_ckd_epi_2021` implements the race-free 2021 creatinine equation using sex-specific \(\kappa\) and \(\alpha\) parameters. Input serum creatinine must be in **mg/dL**.

## ABCD-GENE

The implementation uses:

- age >75: +4
- BMI >30 kg/m²: +4
- eGFR <60 mL/min/1.73m²: +3
- diabetes: +3
- one CYP2C19 LOF allele: +6
- two LOF alleles: +24
- high-risk threshold: ≥10

The function intentionally does not replace missing diabetes status with `False`.

## CYP2C19

The common diplotype mapper covers a limited, explicit allele set. Unsupported or ambiguous combinations return `Unknown`.

## CPIC recommendations

Any recommendation text emitted by the package is a **research abstraction**. Clinical guideline recommendations can depend on phenotype, indication, age, contraindications, bleeding risk, comedications, and guideline version.

## Charlson index

Different published ICD coding algorithms exist for Charlson comorbidity. Before publication, verify that the exact mapping, weights and lookback period match the intended reference implementation.

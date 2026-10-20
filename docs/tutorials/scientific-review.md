# Tutorial: scientific validation and method selection

The platform assesses three independent dimensions: **SOFTWARE execution**, **DATA validity**, and **METHOD validity**. None is automatically **publication-ready**.

## 1. Choose a question before choosing a tool

| Research question | Initial analysis | Required scientific checks |
|---|---|---|
| How frequent are events? | Descriptive summary or incidence rate | Denominator, follow-up, ascertainment, disclosure |
| Can baseline measurements predict an outcome? | Binary prediction | Time-zero features, group/site/time splitting, calibration |
| What happens over time? | Right-censored survival | Entry time, censoring, competing events, proportional hazards |
| What is the effect of treatment? | Target trial / causal inference | Exchangeability, positivity, timing, target estimand |
| Is a PGx treatment strategy appropriate? | Genotype/phenotype concordance | Assay coverage, knowledge version, clinical context |

!!! danger "Unsupported design is not an invitation to approximate"
    Advanced designs (time-varying treatment, competing risks, repeated-patient correlation, unmeasured confounding) require method-specific review. A guided template should stop with a documented explanation rather than silently substituting another method.

## 2. A synthetic cohort-flow check

```python
from thomaslab.easy import make_cohort_flow

flow = make_cohort_flow([
    {"label": "Screened (synthetic)", "n": 100},
    {"label": "Eligible", "n": 80},
    {"label": "With follow-up", "n": 73},
])
print(flow[["label", "remaining_n"]].to_string(index=False))
```

**Expected:** 100 screened, 80 eligible, 73 with follow-up. This establishes only correct arithmetic, not correct cohort definitions or clinical eligibility.

## 3. Researcher review checklist

1. **Population** — Who is represented? Are inclusion and exclusion windows aligned to time zero?
2. **Semantics** — Are lab units, diagnosis codes, PGx assay limits, and outcome definitions reviewed?
3. **Temporal leakage** — Are any predictors measured after the clinical decision or shared across train/test groups?
4. **Identification** — Are causal assumptions or survival censoring mechanisms plausible and prespecified?
5. **Uncertainty** — Are confidence intervals, calibration, sensitivity analysis and subgroup checks reported?
6. **Governance** — Does the output meet approval and disclosure requirements?

## 4. Record a scientific review

Keep `study_id`, the source and adapter revisions, a named reviewer, review date, selected method and version, unresolved findings, and explicit SOFTWARE/DATA/METHOD decisions. Use `REVIEW_REQUIRED` when independent scientific review has not taken place.

**Further reading:** [Leakage protection](../guides/leakage-protection.md) · [Target-trial guide](../guides/target-trial.md) · [Release and science gates](../guides/lab-validation-release-criteria.md).
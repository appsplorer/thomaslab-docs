# Site and external-validation reporting

Use `thomaslab.validation` for transparent binary prediction evaluation across sites or independent datasets.

## Site reporting

`site_validation_report()` returns pooled and site-specific discrimination, Brier score, calibration intercept/slope, sensitivity, specificity, PPV and NPV. It does not rank sites or recommend excluding a site.

## External-source language

`external_validation_report()` only labels an evaluation cohort `external_source_evaluation` when the caller explicitly sets `independent_source=True`. That flag records a study-design assertion; the software cannot prove independence, transportability, or adequate external validation.

## Bootstrap intervals

`bootstrap_metric_interval()` resamples the evaluation cohort and can provide percentile intervals for AUROC, AUPRC or Brier score. The procedure does not include upstream model-development uncertainty unless the entire development process is separately repeated.

## Generalizability gaps

`summarize_validation_gaps()` reports descriptive metric differences against a named reference. Differences should be interpreted with their sampling uncertainty, population mix, prevalence, measurement process, case mix and site-specific data generation in mind.

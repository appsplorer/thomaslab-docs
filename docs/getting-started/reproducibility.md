# Reproducibility checklist

Use this checklist before freezing a manuscript analysis.

- [ ] Record the exact `thomaslab-core` commit SHA and package version.
- [ ] Record Python and dependency versions.
- [ ] Freeze the cohort extraction timestamp and source-system release.
- [ ] Version all ICD/RxNorm/NDC/LOINC/OMOP mapping tables used in the study.
- [ ] Version CPIC/PGx rule sources and allele-definition tables.
- [ ] Store index-date, lookback, washout, and follow-up definitions as code/configuration.
- [ ] Preserve exclusion counts for a CONSORT/STROBE-style cohort flow diagram.
- [ ] Define missing-data handling before outcome analysis.
- [ ] Record propensity-model covariates, estimand, trimming/truncation rules, and balance diagnostics.
- [ ] Test proportional-hazards assumptions when using Cox models.
- [ ] Report confidence intervals and the exact method used to construct them.
- [ ] Distinguish derivation, validation, and external-validation cohorts.
- [ ] Archive figure/table-generation scripts, not only exported PNG/PDF files.
- [ ] Confirm no protected health information (PHI) is committed to Git.

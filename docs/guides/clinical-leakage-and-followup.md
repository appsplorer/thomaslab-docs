# Clinical ML leakage prevention and follow-up integrity

**Research software status: CANDIDATE.** Core PR #34 contains the
`thomaslab.clinical_leakage` and `thomaslab.clinical_followup` modules.
Their independently executed synthetic unit tests do not prove clinical or
statistical correctness on real EHR, claims, All of Us, or MIMIC-IV data.

The new code detects specific leakage mechanisms. **No generic software can
guarantee a study is leakage-free.** Investigators must prespecify prediction
time, clinical feature availability, outcomes, censoring, patient identity,
site structure, study splits and permitted data access.

## Risk-to-function matrix

| Leakage or validity risk | Function | Default safeguard |
|---|---|---|
| Lab collected before index but resulted afterward | `audit_feature_availability` | Block information available after the exact prediction cutoff |
| Feature schema contains target/ID/post-outcome proxies | `audit_feature_contract` | Block unsafe or late feature metadata; return no raw feature names |
| Repeated patients appear in both past/future partitions | `purged_patient_time_split` | Purge all rows of patients spanning the temporal boundary; optional embargo |
| Test/held-out information influences imputation | `fit_train_only_imputer` and `transform_with_train_imputer` | Fit medians using TRAIN only; transform using frozen statistics |
| Outcome becomes a negative label despite incomplete observation | `audit_outcome_ascertainment` | Count incomplete horizon, late outcomes, wrong-person outcomes; never create negative labels |
| Therapy starts after baseline (immortal-time bias risk) | `audit_treatment_time_zero` | Block assignments after a prespecified grace period; never assert causal validity |
| Medical claims or pharmacy enrollment has observation gaps | `audit_enrollment_windows` | Block insufficient or discontinuous observation around index |
| Legacy splitters silently train on missing IDs | `patient_level_split`, `temporal_split`, `site_holdout_split`, `grouped_cv_folds` | Explicit rejection of missing/lossy grouping keys and unsafe holdouts |

**Important:** these utilities are not substitutes for prespecified study
design, clinical code-set/units review, target-trial emulation, independent
gold-standard validation, transportability analysis, and data-release review.

## Source-specific rules

**All of Us Registered/Controlled CDR v9:** perform person-level operations
inside the authorized All of Us Researcher Workbench. Never move participant
records to personal machines, generic UGA HPC, Kaggle or public GitHub. A
matching OMOP `person_id` value from another dataset does not authorize
participant-level linkage; the source-aware linkage helper denies mixed
origins. Counts and candidate outputs remain subject to the programme's
[dissemination policy](aou-disclosure.md).

**MIMIC-IV v3.1:** preserve `subject_id`, `hadm_id`, `stay_id`, patient
date shifts, laboratory result posting times and the difference between
prescriptions, eMAR documentation and actual exposure. A clinical feature
must be available by *decision time*, not merely drawn before it.
Actual MIMIC access and PhysioNet authorization remain prerequisites.

**Hospital EHR/claims:** resolve local timezone and daylight-saving
ambiguities, merged/split MRNs, off-network outcome capture, facility/site
identity, medication order versus administration, and continuous enrollment.
Local non-UTC naïve timestamps need an explicitly declared timezone, not an
assumed conversion. Real records require an institutionally approved enclave.

## Synthetic point-in-time features

~~~python
import pandas as pd
from thomaslab.clinical_leakage import (
    audit_feature_availability, audit_feature_contract,
)

index = pd.DataFrame({
    "person": ["SYNTHETIC001"],
    "decision": ["2026-01-10T10:00:00Z"],
})
labs = pd.DataFrame({
    "person": ["SYNTHETIC001"],
    "specimen_time": ["2026-01-10T08:00:00Z"],
    "result_posted": ["2026-01-10T12:00:00Z"],
})
report = audit_feature_availability(
    labs, index, person_col="person", feature_time_col="specimen_time",
    available_time_col="result_posted", index_time_col="decision",
)
assert report["status"] == "BLOCK"  # Post-decision result leakage
assert report["information_available_after_cutoff"] == 1

metadata = pd.DataFrame({
    "feature": ["lab_baseline"],
    "window_end_hours": [-24.0],
    "availability_delay_hours": [2.0],
    "source_table": ["synthetic_labs"],
})
assert audit_feature_contract(metadata, target_col="outcome")["status"] == "REVIEW_REQUIRED"
~~~

## Purged time splitting and training-only transformation

~~~python
from thomaslab.clinical_leakage import (
    purged_patient_time_split,
    fit_train_only_imputer,
    transform_with_train_imputer,
)

# Use only with separately authorized in-memory patient-level data.
# Exact patient-level outputs are RESTRICTED; this example is invented.
events = pd.DataFrame({
    "pid": ["A", "B", "C"],
    "when": ["2025-10-01T00:00:00Z", "2025-11-01T00:00:00Z",
             "2026-02-01T00:00:00Z"],
    "lab": [1.0, None, 5.0],
})
labels = purged_patient_time_split(
    events, patient_col="pid", time_col="when",
    cutoff="2026-01-01T00:00:00Z", embargo_hours=48,
    allow_patient_level=True,
)
events["split"] = labels
frozen = fit_train_only_imputer(events, columns=("lab",), role_col="split")
test_features = transform_with_train_imputer(
    events.loc[events["split"].eq("TEST")],
    frozen=frozen, allow_patient_level=True,
)
assert test_features.attrs["export_approved"] is False
~~~

Train-only fitting deliberately does **not** use held-out values; statistics
can themselves reveal information about small research groups and must remain
inside approved compute. This code does not automatically approve exporting
fitted medians, model parameters or intermediate features.

## Outcome and claims windows

~~~python
from thomaslab.clinical_followup import (
    audit_outcome_ascertainment,
    audit_treatment_time_zero,
    audit_enrollment_windows,
)
# These diagnostics return restricted aggregate counts, not patient labels.
# Explicit observation_end and prespecified horizon are required.
# Missing outcome events must NEVER automatically mean a complete follow-up.
~~~

No function in this module estimates a treatment effect or proves the
absence of immortal-time, confounding, informative censoring or label error.

## Validation and HPC acceptance

~~~bash
# Entirely synthetic test fixtures:
python -m pytest -q tests/test_clinical_leakage.py \
    tests/test_clinical_followup.py tests/test_splits.py

# Run exact-SHA end-to-end acceptance on an approved CPU Slurm allocation:
sbatch --partition=batch --cpus-per-task=16 --mem=48G \
    --time=08:00:00 --export=ALL slurm/portable_acceptance.sbatch
~~~

The existing HPC runner additionally requires
`THOMASLAB_EXPECTED_SHA`, `THOMASLAB_PYTHON`,
`THOMASLAB_QA_REPORT_ROOT` and `THOMASLAB_CODE_ROOT` to be configured
as described in [HPC A–Z](hpc-a-to-z.md). **These tests must pass at the
same Git commit** before the Core candidate can be considered for merging.

### Release limitations

A technical test pass does not grant All of Us, PhysioNet, UGA or hospital
access, nor permission to release small counts, metadata, patient-level
records or model artifacts. The modules have not been evaluated against
approved real cohorts or independent gold-standard phenotypes. Their
scientific readiness remains `NOT_ASSESSED`, clinical deployment
`NOT_AUTHORIZED`.

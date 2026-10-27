# S30 — Synthetic clinical time-zero, censoring, observation coverage and leakage preflight

**Development status: S30 local synthetic QA only; P4-05 OPEN.** No real All of Us, MIMIC-IV, hospital or patient-level clinical data are supported by this prototype. Caller-supplied `classification="SYNTHETIC"` is not de-identification proof, data-use authorization or PHI detection. Work only with invented test inputs.

**Private module:** `thomaslab.adaptive.study_safety_gate`.

## Public function

`evaluate_synthetic_study_gate(*, contract, cohort, features, outcomes, treatments, capture_intervals)` checks an *entire bounded synthetic cohort* (max 50,000 records per input collection) against an explicit versioned study contract. The contract pins a source release SHA-256, protocol SHA-256, single site scope, horizon, lookback, information embargo, treatment grace and required capture domains. These SHA-256 values are declarations, not independently signed authorization.

Data format: cohort rows have `patient_ref`, `site_scope`, `index_at`, `observed_until`. Feature rows have `patient_ref`, `site_scope`, `domain`, `event_at`, `available_at`. Outcome rows have `patient_ref`, `site_scope`, `outcome_at`; treatment rows have `patient_ref`, `site_scope`, `assigned_at`. Capture metadata have `site_scope`, `domain`, `from_at`, `until_at`.

- Rejects unreviewed cross-site joins, duplicate time-zero rows, invalid timezones, numeric/date-only timestamps, unknown fields, malformed tokens and oversized batches.
- Blocks features measured **or available** after the index-minus-embargo cutoff, and recordings whose result availability precedes occurrence.
- Blocks unlinked outcomes or treatments, events at/before index, events after censoring, post-index assignments (even within an unanalysed grace period), and impossible observation intervals.
- Requires continuous declared clinical-domain capture across every participant's lookback and outcome horizon. Observation gaps are **never** assumed to be disease-free intervals.
- Counts those with inadequate actual follow-up separately from full-site capture. A censored participant is never assigned an event-negative label; outcome counts are events, not necessarily unique people.
- Returns only aggregate QA counters and SHA-256 evidence; no patient identifiers, times, individual labels, or row-level data. Every result has `authorized_for_export=False`, independent clinical validation `False` and disclosure approval `False`. Even harmless-looking aggregate counts must remain in the authorized environment and be reviewed before disclosure.

Synthetic-only example:

~~~python
from thomaslab.adaptive.study_safety_gate import evaluate_synthetic_study_gate

# Use only hand-invented fixtures satisfying the exact field contracts.
report = evaluate_synthetic_study_gate(
    contract=synthetic_study_contract,
    cohort=synthetic_cohort,
    features=synthetic_features,
    outcomes=synthetic_outcomes,
    treatments=synthetic_treatments,
    capture_intervals=synthetic_site_domain_capture,
)
assert report["authorized_for_export"] is False
assert report["missing_outcome_treated_as_negative"] is False
~~~

## Local evidence and missing acceptance

S30 was tested with **32 local synthetic regressions** (combined S30/S31: 64/64 PASS) using Python 3.13.5. Syntax parsing for Python 3.9–3.13 passed. No external or private clinical source used; no institutional data access, timing semantics, phenotype adjudication, censoring assumptions, causal identification, privacy review or trial-emulation scientific acceptance claimed. Current-head Core full CI, Python 3.9 runtime and HPC not accepted. **P4-05 remains OPEN.**

~~~bash
python -m pytest -q tests/test_adaptive_study_safety_gate.py
~~~

See the existing `thomaslab.clinical_leakage`, `thomaslab.clinical_followup`, S01 schema discovery and S29 observability packages for related preflights. This S30 gate does not replace their source-specific authorizations and does not automatically execute them.

# `thomaslab.clinical_followup` — API reference

**Status:** experimental source methods in Core PR #34; locally tested on
invented data only, pending full exact-commit Core CI/HPC and independent
clinical/statistical review. No actual EHR, MIMIC-IV or All of Us records
were used to produce these methods.

All outputs are in-memory research diagnostics or explicitly restricted
patient-level artifacts. A `BLOCK` status denotes a detected contract
violation. A non-blocked outcome does **not** certify freedom from data
leakage, data-use rights, scientific correctness or release approval.

For examples and per-dataset restrictions see
[Clinical ML leakage and follow-up guide](../../guides/clinical-leakage-and-followup.md).

## `audit_outcome_ascertainment`

Flag incomplete follow-up, impossible events and mismatched patient IDs.

~~~python
def audit_outcome_ascertainment( cohort: pd.DataFrame, outcomes: pd.DataFrame, *, patient_col: str, index_col: str, observation_end_col: str, outcome_time_col: str, horizon_days: float, assumed_timezone: str | None = None, max_rows: int = 250_000, ) -> dict[str, Any]:
~~~

The source input requires the study's approved dataset, correct column
mapping and explicitly documented time-zero, timezone, feature or outcome
semantics. Numerical results and fitted preprocessing statistics remain
restricted. Scientific validity and clinical authorization are **not assessed**.

## `audit_treatment_time_zero`

Identify treatment assignment after time-zero (immortal-time risk).

~~~python
def audit_treatment_time_zero( assignments: pd.DataFrame, *, index_col: str, assignment_col: str, allowed_lag_hours: float = 0.0, assumed_timezone: str | None = None, max_rows: int = 250_000, ) -> dict[str, Any]:
~~~

The source input requires the study's approved dataset, correct column
mapping and explicitly documented time-zero, timezone, feature or outcome
semantics. Numerical results and fitted preprocessing statistics remain
restricted. Scientific validity and clinical authorization are **not assessed**.

## `audit_enrollment_windows`

Check continuous insurance observation around index; no event-negative labels.

~~~python
def audit_enrollment_windows( cohort: pd.DataFrame, enrollment: pd.DataFrame, *, patient_col: str, index_col: str, coverage_start_col: str, coverage_end_col: str, lookback_days: float, followup_days: float, assumed_timezone: str | None = None, max_rows: int = 250_000, ) -> dict[str, Any]:
~~~

The source input requires the study's approved dataset, correct column
mapping and explicitly documented time-zero, timezone, feature or outcome
semantics. Numerical results and fitted preprocessing statistics remain
restricted. Scientific validity and clinical authorization are **not assessed**.


# `thomaslab.clinical_leakage` — API reference

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

## `FrozenNumericImputer`

Immutable candidate model of TRAIN-only medians, numeric feature names and
training row count, returned by `fit_train_only_imputer`.
Do not publish the stored statistics without disclosure review.

## `audit_feature_availability`

Count features known only after a clinical prediction cutoff.

~~~python
def audit_feature_availability( events: pd.DataFrame, index: pd.DataFrame, *, person_col: str, feature_time_col: str, available_time_col: str, index_time_col: str, embargo_hours: float = 0.0, assumed_timezone: str | None = None, max_rows: int = 250_000, ) -> dict[str, Any]:
~~~

The source input requires the study's approved dataset, correct column
mapping and explicitly documented time-zero, timezone, feature or outcome
semantics. Numerical results and fitted preprocessing statistics remain
restricted. Scientific validity and clinical authorization are **not assessed**.

## `audit_feature_contract`

Require a prespecified source/window/availability contract per feature.

~~~python
def audit_feature_contract( features: pd.DataFrame, *, feature_col: str = "feature", window_end_col: str = "window_end_hours", delay_col: str = "availability_delay_hours", source_col: str = "source_table", target_col: str, decision_offset_hours: float = 0.0, max_rows: int = 10_000, ) -> dict[str, Any]:
~~~

The source input requires the study's approved dataset, correct column
mapping and explicitly documented time-zero, timezone, feature or outcome
semantics. Numerical results and fitted preprocessing statistics remain
restricted. Scientific validity and clinical authorization are **not assessed**.

## `purged_patient_time_split`

Label train/test with embargo; purge all rows of boundary-spanning patients.

~~~python
def purged_patient_time_split( frame: pd.DataFrame, *, patient_col: str, time_col: str, cutoff: str, embargo_hours: float = 0.0, assumed_timezone: str | None = None, allow_patient_level: bool = False, max_rows: int = 250_000, ) -> pd.Series:
~~~

The source input requires the study's approved dataset, correct column
mapping and explicitly documented time-zero, timezone, feature or outcome
semantics. Numerical results and fitted preprocessing statistics remain
restricted. Scientific validity and clinical authorization are **not assessed**.

## `fit_train_only_imputer`

Calculate medians on TRAIN rows only, ignoring all held-out values.

~~~python
def fit_train_only_imputer( frame: pd.DataFrame, *, columns: Sequence[str], role_col: str, max_rows: int = 250_000, ) -> FrozenNumericImputer:
~~~

The source input requires the study's approved dataset, correct column
mapping and explicitly documented time-zero, timezone, feature or outcome
semantics. Numerical results and fitted preprocessing statistics remain
restricted. Scientific validity and clinical authorization are **not assessed**.

## `transform_with_train_imputer`

Apply prelearned train statistics without refitting on test patients.

~~~python
def transform_with_train_imputer( frame: pd.DataFrame, *, frozen: FrozenNumericImputer, allow_patient_level: bool = False, max_rows: int = 250_000, ) -> pd.DataFrame:
~~~

The source input requires the study's approved dataset, correct column
mapping and explicitly documented time-zero, timezone, feature or outcome
semantics. Numerical results and fitted preprocessing statistics remain
restricted. Scientific validity and clinical authorization are **not assessed**.


# `thomaslab.healthcare_foundation` — API reference

**Status:** candidate source methods, synthetic regression tests authored; full exact-SHA Core acceptance and clinical validation pending.

**Research-only:** execute in the source-authorized environment. This reference documents public Python signatures, not the private implementation or dataset entitlement. Returning an in-memory count does not authorize its publication.

See [source-specific methods](../../guides/clinical-dataset-methods.md) and [data rights](../../guides/dataset-access-and-adapters.md).

## `suggest_dataset_families`

**Purpose:** Suggest structural source families; every suggestion requires human review.

**Signature**

~~~python
def suggest_dataset_families(columns: Sequence[str]) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `profile_healthcare_table`

**Purpose:** Return aggregate shape, nulls and duplicate-row counts, never example values.

**Signature**

~~~python
def profile_healthcare_table(frame: pd.DataFrame) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `validate_column_contract`

**Purpose:** Fail closed on missing fields and unsafe basic types; no implicit recoding.

**Signature**

~~~python
def validate_column_contract(frame: pd.DataFrame, kinds: Mapping[str, str]) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `patient_split_overlap`

**Purpose:** Reject shared identifiers between partitions without returning raw IDs.

**Signature**

~~~python
def patient_split_overlap( train: pd.DataFrame, test: pd.DataFrame, *, id_column: str ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `baseline_leakage_check`

**Purpose:** Count rows with a feature timestamp after the clinical decision time.

**Signature**

~~~python
def baseline_leakage_check( frame: pd.DataFrame, *, feature_time: str, index_time: str, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `binary_baseline_report`

**Purpose:** Compute descriptive test-set metrics; callers must enforce honest splitting.

**Signature**

~~~python
def binary_baseline_report( truth: Sequence[int], probabilities: Sequence[float], *, threshold: float = 0.5 ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `regression_baseline_report`

**Purpose:** Provide MAE, RMSE and R² for held-out regression, without clinical claims.

**Signature**

~~~python
def regression_baseline_report( truth: Sequence[float], predictions: Sequence[float] ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `kaplan_meier_baseline_report`

**Purpose:** Unadjusted Kaplan-Meier benchmark with explicit horizon and right censoring.

**Signature**

~~~python
def kaplan_meier_baseline_report( followup_time: Sequence[float], event: Sequence[int], *, horizon: float ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.


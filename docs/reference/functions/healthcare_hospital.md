# `thomaslab.healthcare_hospital` — API reference

**Status:** candidate source methods, synthetic regression tests authored; full exact-SHA Core acceptance and clinical validation pending.

**Research-only:** execute in the source-authorized environment. This reference documents public Python signatures, not the private implementation or dataset entitlement. Returning an in-memory count does not authorize its publication.

See [source-specific methods](../../guides/clinical-dataset-methods.md) and [data rights](../../guides/dataset-access-and-adapters.md).

## `hospital_encounter_quality`

**Purpose:** Check duplicate admissions and impossible visit order, without patient IDs.

**Signature**

~~~python
def hospital_encounter_quality( encounters: pd.DataFrame, *, person_col: str, encounter_col: str, admit_col: str, discharge_col: str, max_rows: int = 250_000, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `hospital_lab_quality`

**Purpose:** Flag unit variation per analyte, not automatic UCUM/LOINC harmonization.

**Signature**

~~~python
def hospital_lab_quality( labs: pd.DataFrame, *, concept_col: str, result_col: str, unit_col: str, max_rows: int = 250_000, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `hospital_medication_quality`

**Purpose:** Require explicit separation of orders, dispensing and administration.

**Signature**

~~~python
def hospital_medication_quality( medications: pd.DataFrame, *, person_col: str, timestamp_col: str, code_col: str, event_kind_col: str, max_rows: int = 250_000, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `count_preindex_events`

**Purpose:** Create in-memory per-person pre-index feature counts, not exported data.

**Signature**

~~~python
def count_preindex_events( index: pd.DataFrame, events: pd.DataFrame, *, person_col: str, index_time_col: str, event_time_col: str, lookback_days: float, allow_patient_level: bool = False, max_rows: int = 250_000, ) -> pd.DataFrame:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `hospital_intervisit_gap_quality`

**Purpose:** Count consecutive stays within a chosen interval, NOT true readmission.

**Signature**

~~~python
def hospital_intervisit_gap_quality( encounters: pd.DataFrame, *, person_col: str, admit_col: str, discharge_col: str, days: float = 30.0, max_rows: int = 250_000, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.


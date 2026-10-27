# `thomaslab.healthcare_quality` — API reference

**Status:** candidate source methods, synthetic regression tests authored; full exact-SHA Core acceptance and clinical validation pending.

**Research-only:** execute in the source-authorized environment. This reference documents public Python signatures, not the private implementation or dataset entitlement. Returning an in-memory count does not authorize its publication.

See [source-specific methods](../../guides/clinical-dataset-methods.md) and [data rights](../../guides/dataset-access-and-adapters.md).

## `code_set_manifest`

**Purpose:** Create a deterministic versioned code-set fingerprint, not approval.

**Signature**

~~~python
def code_set_manifest( *, system: str, version: str, codes: Sequence[str], protocol_id: str, effective_date: date, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `clinical_code_coverage`

**Purpose:** Count null and outside-code-set rows without returning any source code.

**Signature**

~~~python
def clinical_code_coverage( events: pd.DataFrame, *, code_column: str, allowed_codes: frozenset[str], max_rows: int = 250000, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `medication_state_summary`

**Purpose:** Separate order, dispense and administration without inferring adherence.

**Signature**

~~~python
def medication_state_summary( events: pd.DataFrame, *, person_col: str, time_col: str, drug_col: str, state_col: str, max_rows: int = 250000, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `site_temporal_holdout_preflight`

**Purpose:** Fail when patient, site or chronological separation is violated.

**Signature**

~~~python
def site_temporal_holdout_preflight( train: pd.DataFrame, holdout: pd.DataFrame, *, patient_col: str, site_col: str, time_col: str, max_rows: int = 250000, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `site_missingness_preflight`

**Purpose:** Suppress site identifiers and block small-site release by default.

**Signature**

~~~python
def site_missingness_preflight( frame: pd.DataFrame, *, site_col: str, value_col: str, minimum_group_size: int = 11, max_rows: int = 250000, source_system: str = "generic", ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.


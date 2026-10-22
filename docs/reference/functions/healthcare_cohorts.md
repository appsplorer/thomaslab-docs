# `thomaslab.healthcare_cohorts` — API reference

**Status:** candidate source methods, synthetic regression tests authored; full exact-SHA Core acceptance and clinical validation pending.

**Research-only:** execute in the source-authorized environment. This reference documents public Python signatures, not the private implementation or dataset entitlement. Returning an in-memory count does not authorize its publication.

See [source-specific methods](../../guides/clinical-dataset-methods.md) and [data rights](../../guides/dataset-access-and-adapters.md).

## `cohort_attrition_summary`

**Purpose:** Count sequential investigator-prespecified masks; no clinical autoapproval.

**Signature**

~~~python
def cohort_attrition_summary( eligible: pd.Series, criteria: Mapping[str, pd.Series], ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `build_index_event_cohort`

**Purpose:** Choose each person's earliest reviewed code-defined index event.

**Signature**

~~~python
def build_index_event_cohort( events: pd.DataFrame, *, person_col: str, event_time_col: str, concept_col: str, prespecified_codes: frozenset[str], allow_patient_level: bool = False, max_rows: int = 250_000, ) -> pd.DataFrame:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `followup_event_quality`

**Purpose:** Check ascertainable followup and postindex events by person.

**Signature**

~~~python
def followup_event_quality( index: pd.DataFrame, outcomes: pd.DataFrame, *, person_col: str, index_col: str, end_col: str, event_time_col: str, horizon_days: float, max_rows: int = 250_000, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.


# `thomaslab.healthcare_omop` — API reference

**Status:** candidate source methods, synthetic regression tests authored; full exact-SHA Core acceptance and clinical validation pending.

**Research-only:** execute in the source-authorized environment. This reference documents public Python signatures, not the private implementation or dataset entitlement. Returning an in-memory count does not authorize its publication.

See [source-specific methods](../../guides/clinical-dataset-methods.md) and [data rights](../../guides/dataset-access-and-adapters.md).

## `omop_concept_integrity`

**Purpose:** Counts unmapped/zero, null and unknown concepts; never prints codes.

**Signature**

~~~python
def omop_concept_integrity( events: pd.DataFrame, concepts: pd.DataFrame, *, concept_column: str, max_rows: int = 250_000, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `omop_person_visit_integrity`

**Purpose:** Test event-person/visit relationship and mismatched visit ownership.

**Signature**

~~~python
def omop_person_visit_integrity( persons: pd.DataFrame, visits: pd.DataFrame, events: pd.DataFrame, *, visit_column: str = "visit_occurrence_id", max_rows: int = 250_000, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `omop_observation_period_integrity`

**Purpose:** Count impossible OMOP observation periods; never infer EHR completeness.

**Signature**

~~~python
def omop_observation_period_integrity( observations: pd.DataFrame, *, max_rows: int = 250_000 ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `omop_measurement_quality`

**Purpose:** Check recorded measurement value/unit fields without converting units.

**Signature**

~~~python
def omop_measurement_quality( measurements: pd.DataFrame, *, max_rows: int = 250_000 ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.


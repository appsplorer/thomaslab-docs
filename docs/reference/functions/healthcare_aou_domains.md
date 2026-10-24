# `thomaslab.healthcare_aou_domains` — API reference

**Status:** candidate source methods, synthetic regression tests authored; full exact-SHA Core acceptance and clinical validation pending.

**Research-only:** execute in the source-authorized environment. This reference documents public Python signatures, not the private implementation or dataset entitlement. Returning an in-memory count does not authorize its publication.

See [source-specific methods](../../guides/clinical-dataset-methods.md) and [data rights](../../guides/dataset-access-and-adapters.md).

## `aou_survey_response_quality`

**Purpose:** Differentiate PMI_SKIP (903096) from an answered survey response.

**Signature**

~~~python
def aou_survey_response_quality( observations: pd.DataFrame, *, max_rows: int = 250_000 ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `aou_wearable_daily_quality`

**Purpose:** Inspect consented daily wearable signals without interpolation.

**Signature**

~~~python
def aou_wearable_daily_quality( daily: pd.DataFrame, *, person_col: str, date_col: str, value_col: str, device_col: str | None = None, max_rows: int = 250_000, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `aou_omics_provenance_quality`

**Purpose:** Block omics claims without reference, modality and QC provenance.

**Signature**

~~~python
def aou_omics_provenance_quality( manifest: Mapping[str, object], ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.


# `thomaslab.healthcare_mimic` — API reference

**Status:** candidate source methods, synthetic regression tests authored; full exact-SHA Core acceptance and clinical validation pending.

**Research-only:** execute in the source-authorized environment. This reference documents public Python signatures, not the private implementation or dataset entitlement. Returning an in-memory count does not authorize its publication.

See [source-specific methods](../../guides/clinical-dataset-methods.md) and [data rights](../../guides/dataset-access-and-adapters.md).

## `mimic_anchor_age_quality`

**Purpose:** Respect age 91 as top-coded; never label 91 as an exact age.

**Signature**

~~~python
def mimic_anchor_age_quality( patients: pd.DataFrame, *, max_rows: int = 250_000 ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `mimic_stay_relationship_quality`

**Purpose:** Check subject/admission/ICU chains and shifted-within-patient intervals.

**Signature**

~~~python
def mimic_stay_relationship_quality( patients: pd.DataFrame, admissions: pd.DataFrame, icustays: pd.DataFrame, *, max_rows: int = 250_000, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `mimic_lab_event_quality`

**Purpose:** Inspect hosp.labevents, retaining legitimately null hadm_id.

**Signature**

~~~python
def mimic_lab_event_quality( labs: pd.DataFrame, *, max_rows: int = 250_000 ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `mimic_prescription_quality`

**Purpose:** Check MIMIC drug *orders*, not pharmacy dispensing or eMAR delivery.

**Signature**

~~~python
def mimic_prescription_quality( prescriptions: pd.DataFrame, *, max_rows: int = 250_000 ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `mimic_icd_version_quality`

**Purpose:** Preserve ICD-9 versus ICD-10; reject blank or invalid codes/versions.

**Signature**

~~~python
def mimic_icd_version_quality( diagnoses: pd.DataFrame, *, max_rows: int = 250_000 ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `mimic_emar_quality`

**Purpose:** Distinguish charted eMAR events from actual confirmed administration.

**Signature**

~~~python
def mimic_emar_quality( emar: pd.DataFrame, *, max_rows: int = 250_000, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `mimic_lab_dictionary_integrity`

**Purpose:** Count missing MIMIC d_labitems links; no automatic LOINC inference.

**Signature**

~~~python
def mimic_lab_dictionary_integrity( labs: pd.DataFrame, dictionary: pd.DataFrame, *, max_rows: int = 250_000, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `mimic_icu_chart_quality`

**Purpose:** Check ICU chart timing, measurement IDs and optional d_items coverage.

**Signature**

~~~python
def mimic_icu_chart_quality( chartevents: pd.DataFrame, *, item_dictionary: pd.DataFrame | None = None, max_rows: int = 250_000, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.



## `mimic_order_to_emar_linkage_quality`

**Purpose:** assess how documented MIMIC-IV `pharmacy_id` links associate
prescriptions with eMAR events without inferring that a prescription was
administered or dispensed.

**Signature**

~~~python
def mimic_order_to_emar_linkage_quality(
    prescriptions: pd.DataFrame,
    emar: pd.DataFrame,
    *,
    max_rows: int = 250_000,
) -> dict[str, Any]:
~~~

**Checks:** nonnull prescription pharmacy/subject/admission IDs,
potentially ambiguous pharmacy IDs used across patients, orphan eMAR pharmacy
links, patient and admission mismatches, cross-admission collisions, legitimately missing eMAR pharmacy/admission
references and incompatible identifier types.

**Output:** aggregate-only status `BLOCK` or
`MEDICATION_LINKAGE_REVIEW_REQUIRED`. No patient IDs or row-level tables
are returned.

**Important:** eMAR medication administration and eMAR-detail dose records
must be clinically reconciled separately; never infer medication adherence,
drug exposure, or dosage solely from matching order IDs.

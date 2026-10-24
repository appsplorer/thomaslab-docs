# `thomaslab.healthcare_aou_query` — API reference

**Status:** candidate source methods, synthetic regression tests authored; full exact-SHA Core acceptance and clinical validation pending.

**Research-only:** execute in the source-authorized environment. This reference documents public Python signatures, not the private implementation or dataset entitlement. Returning an in-memory count does not authorize its publication.

See [source-specific methods](../../guides/clinical-dataset-methods.md) and [data rights](../../guides/dataset-access-and-adapters.md).

## `plan_aou_omop_domain_query`

**Purpose:** Construct an allowlisted, parameterized participant-level cohort query.

**Signature**

~~~python
def plan_aou_omop_domain_query( *, context: SourceContext, approved_project_id: str, table: str, concept_ids: tuple[int, ...], start_date: date, end_date: date, max_concepts: int = 250, ) -> WorkbenchQueryPlan:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.


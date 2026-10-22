# `thomaslab.healthcare_sources` — API reference

**Status:** candidate source methods, synthetic regression tests authored; full exact-SHA Core acceptance and clinical validation pending.

**Research-only:** execute in the source-authorized environment. This reference documents public Python signatures, not the private implementation or dataset entitlement. Returning an in-memory count does not authorize its publication.

See [source-specific methods](../../guides/clinical-dataset-methods.md) and [data rights](../../guides/dataset-access-and-adapters.md).

## SourceContext

`SourceContext` declares `family`, `release`, `environment`, `classification`, `synthetic`, and optional authorization metadata. It is **declarative only** and never verifies Workbench/PhysioNet credentials.

## `assess_source_access`

**Purpose:** Fail closed for restricted data in unapproved compute environments.

**Signature**

~~~python
def assess_source_access(context: SourceContext) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `inspect_source_table`

**Purpose:** Aggregate-only schema diagnostics; no auto-approval, joins or file writes.

**Signature**

~~~python
def inspect_source_table( frame: pd.DataFrame, *, context: SourceContext, table: str, hospital_mapping: Mapping[str, str] | None = None, max_in_memory_rows: int = 250_000, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `relationship_integrity`

**Purpose:** Conservative referential diagnostic without copying identifier values.

**Signature**

~~~python
def relationship_integrity( child: pd.DataFrame, parent: pd.DataFrame, *, child_key: str, parent_key: str, max_rows: int = 250_000, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.

## `visit_window_integrity`

**Purpose:** Detect impossible temporal ordering; timezone conventions remain unverified.

**Signature**

~~~python
def visit_window_integrity( table: pd.DataFrame, *, start: str, end: str, ) -> dict[str, Any]:
~~~

**Input review:** verify source grain, data rights, column semantics, nulls, units, temporal origin and coding version before calling. **Output:** structural diagnostic or restricted in-memory research artifact. **Limit:** no patient-level external release, clinical inference, or independent validity is established.


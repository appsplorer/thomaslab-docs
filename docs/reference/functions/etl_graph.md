# S18 — Typed reviewed-source-to-OMOP ETL dependency graph

**Status:** design-time graph construction and validation only. It does not run ETL, compile SQL or Python, handle patient records, verify clinical time-zero or authorize patient-data release. The private API is `thomaslab.adaptive.etl_graph.build_reviewed_etl_graph`.

## Three types of graph nodes

1. `SOURCE` nodes refer to a specific hospital source table, source system, source release, S01 schema SHA-256 and **approved** existing `AdapterRegistry` revision.
2. `STAGING` nodes use one of the exact S10 canonical staging families: `person`, `encounter` or `clinical_event`.
3. `OMOP` nodes refer only to official tables in the pinned S11 OHDSI CDM v5.4.3 catalog.

Every node declares the same explicit site scope. Separate sites are never implicitly merged; an unauthorized cross-site join is denied. The source adapter is re-read through the S09 `_approval` gate, including full-source validation, mapping review and registry content integrity. Source release, table and fingerprint must match exactly.

## Graph edges, joins and fan-out

Edges connect only `SOURCE_TO_STAGE` or `STAGE_TO_OMOP`. They declare a bounded explicit `field_map` of source/target field pairs. Every field must exist in the applicable approved source, staging or official OMOP table. Source→staging mappings must match the reviewed adapter's exact mapping, not a user-written expression.

Edge multiplicities are `ONE_TO_ONE`, `ONE_TO_MANY` and `MANY_TO_ONE`. Anything other than one-to-one must carry an opaque external review reference. A branch from one node to several destinations requires review references on **each outgoing edge**.

A staging node with multiple source parents requires a reviewed join-key list on every incoming edge. Site isolation must explicitly include `("site_id", "site_id")`. Additional join keys must be present in approved source and target schemas. This is a *declaration of intended join semantics*, not proof that a hospital source identity link is correct. Neither time-windowed linkage nor actual join cardinality is executed or validated.

The graph is structurally acyclic because edges move strictly forward through its three node tiers. Unknown nodes, orphan source/staging nodes, cross-tier edges, duplicate node IDs, unapproved fields, conflicting target assignments, unsafe SQL snippets, schema drift and unreviewed fan-out fail closed.

## Returned data and security boundaries

The function returns an explicit ordered graph plus `graph_sha256`, node/edge counts and review flags, including:

~~~text
status = ETL_GRAPH_REVIEW_ONLY
source_adapters_indicated_approved = True
join_and_fanout_clinically_approved = False
compiled_sql = False
transformations_executed = False
concept_mapping_validated = False
site_linkage_authorized = False
dataset_release_authorized = False
~~~

The graph contains column names, table identities, adapter revision IDs and scope references. **These metadata may be sensitive** in an institutional research environment; keep them in approved storage. It contains no patient rows, credentials or generated executable SQL.

## Simplified synthetic invocation

~~~python
from thomaslab.adaptive.etl_graph import build_reviewed_etl_graph

# nodes and edges are explicit dictionaries with the documented schemas.
# registry is the real existing AdapterRegistry; source revisions must
# already have passing complete FULL_SOURCE and approved mapping evidence.
plan = build_reviewed_etl_graph(
    nodes=synthetic_nodes,
    edges=synthetic_edges,
    registry=approved_adapter_registry,
    source_system="synthetic_ehr",
    source_release="v1",
    site_scope="SITEA",
)
assert plan["status"] == "ETL_GRAPH_REVIEW_ONLY"
assert plan["compiled_sql"] is False
assert plan["dataset_release_authorized"] is False
~~~

The graph model deliberately does not represent SQL joins, arbitrary Python transforms, clinical concept mapping scripts or a UI automation that could run unreviewed source code. Those would require separate S19/P3-02 allowlisted compiler, S20/P3-03 protected identity and time-join contracts, full current-source QA and clinician/steward approval.

## Testing and acceptance

A **36/36-test combined synthetic S17/S18 suite** passed locally on Python 3.13.5. S18 tests covered exact graph fingerprints, source approval/fingerprint mismatch, cross-site denial, unknown official tables, unreviewed fan-out, multi-table joins requiring site keys and review IDs, and unsafe field name / SQL-snippet rejection. The 36 locally executed focused tests used an S09-compatible fake approval registry and the same staging/OMOP *interfaces*. A **37th test is now committed**, exercising an actual `AdapterRegistry` instance and rejection of a tampered approved-record content digest; that new integration case is **not yet runtime-verified** on the complete private Core checkout. The exact new S18 source and combined test file have Git blob matches to their locally tested counterparts.

The full private Core import graph, Python 3.9 runtime, HPC, independently clinician-approved joins, actual source cardinalities and OMOP value-level correctness are still unverified.

**P3-01 is locally tested at the bounded graph-design level only**, not clinically, institutionally or execution-level accepted. P3-02 (validated ETL compilation), P3-03 (secure identity/temporal joins) and P3-04 (record builders) remain separate OPEN tasks.

Related: [S10 staging](canonical_dataset.md), [S09 approved mapping memory](mapping_memory.md), [S11 official OMOP schema](omop54_contract.md), [S17 Athena importer](athena_import.md).

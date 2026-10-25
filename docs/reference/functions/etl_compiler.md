# S19 — Safe allowlisted ETL intermediate-representation compiler

**Development candidate; NOT an executable patient-data pipeline.** Private API: `thomaslab.adaptive.etl_compiler.compile_review_only_etl`. This extends the reviewed S18 dependency graph, S10 staging schema and S11 OMOP CDM 5.4 field catalog.

## Verified local scope

S19 accepts an S18 `ETL_GRAPH_REVIEW_ONLY` report. It verifies the graph's SHA-256 manifest identity, rejects any source claim of execution/clinical approval/release, requires an external review callback, and checks bounded typed SOURCE → STAGING → OMOP tiers and literal target columns against the supplied OMOP v5.4 catalog.

The compiler emits a deterministic, SHA-256-bound **intermediate representation (IR)** with only `COPY_COLUMNS_ONLY` operations. Each step explicitly lists source/target nodes, pairs of allowed source/target column names, multiplicity, reviewed join-key pairs and a review reference. Missing target columns, invalid identifiers, duplicate destination assignments, cross-site nodes, invalid tiers, unchecked fan-out and omitted join-review references fail closed.

The IR is **not SQL**, a Python transformation, a database query, or a runnable clinical ETL. No arbitrary script, SQL fragment, patient row, stored procedure or code string is accepted. S19 does **not** prove that a reviewer callback is genuinely tied to an institution, that source adapter approval is current in S08/S09, or that schema columns map to valid clinical concepts. A JSON SHA-256 proves integrity against the supplied digest, not independent digital signature or entitlement.

## Synthetic example

~~~python
from thomaslab.adaptive.etl_compiler import compile_review_only_etl
from thomaslab.adaptive.omop54_contract import load_omop54_catalog

plan = compile_review_only_etl(
    s18_graph_report,  # output of build_reviewed_etl_graph(...)
    actor="synthetic_reviewer",
    verify_graph_review=lambda actor, digest: True,  # DEMONSTRATION ONLY
    official_catalog=load_omop54_catalog(),
)
assert plan["status"] == "NON_EXECUTABLE_IR_REVIEW_ONLY"
assert plan["sql_generated"] is False
assert plan["transformations_executed"] is False
assert plan["dataset_release_authorized"] is False
~~~

The actual graph must already have originated from the original protected S18 registry workflow. The demonstration verifier cannot certify a hospital review. A real authority must validate the reviewer, graph revision, source access, source/schema drift and mapping approval on every use before clinical execution.

## Testing and next gates

34/34 S19+S20 synthetic focused tests passed locally using Python 3.13.5; the implementation and regression-test Git blobs match the tested source. Python 3.9–3.13 grammar parsing passed. This test setup uses invented graph/catalog metadata, **not** the entire private Core dependency graph, the additional pending S18 AdapterRegistry integration test, actual Python 3.9 runtime, or approved HPC.

**P3-02 `LOCAL_TEST_PASS` at its bounded, typed non-executing IR compiler scope only**, not executable ETL or scientific acceptance. Before patient-data processing, separately implement security-reviewed ETL execution/row builders, site/time joins, approval-and-revocation checks, OMOP vocabulary validation, row reconciliation, logging, clinical sign-off, and source licensing/IRB/DUA.

Related: [S18 dependency graph](etl_graph.md), [S20 protected join contract](protected_joins.md), [EHR platform roadmap](../../guides/ehr-platform-build-plan.md).

~~~bash
python -m pytest -q tests/test_adaptive_etl_compiler_joins.py
python scripts/ehr_platform_status.py
bash scripts/verify_hardening_candidate.sh  # approved exact-SHA Core/HPC only
~~~
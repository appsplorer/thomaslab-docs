# S06 — Governed remote SQL and FHIR metadata connector contracts

**State: PRIVATE DEVELOPMENT CANDIDATE.** This is not an institution-certified,
clinically validated or patient-data-authorized connector. It runs only inside
an institutionally approved environment with credentials, permissions, egress
rules and reviewer sign-off supplied independently.

The executable module is `thomaslab.adaptive.remote_ingest`, committed to
private Core PR #34. The corresponding tests are
`tests/test_adaptive_remote_ingest.py`. All demonstrations use synthetic
data and fake connectors. Do **not** paste server credentials, tokens, real
FHIR response bodies, patient identifiers or connection URLs into issues,
notebooks, public docs or CI artifacts.

## What this session adds

- `RemoteGrant`: an immutable requested scope identifying the source system,
  release, table, actor, connector type, destination resource and expiry.
  A grant object **cannot authorize itself**.
- `RemoteAuthorizationRequest`: a narrow, structured request passed to an
  independent institution-provided `verify_authorization` function.
- `discover_approved_postgres_schema`: bounded metadata scan through a
  preconfigured SQLAlchemy-compatible PostgreSQL engine. It executes
  `SET TRANSACTION READ ONLY`, sets a statement timeout, and issues a
  schema-qualified `SELECT` of *explicitly listed, identifier-validated*
  columns. It does **not** construct engines, hold credentials, accept
  user-written SQL, execute stored procedures, or return patient rows.
- `discover_approved_fhir_server_schema`: bounded same-origin HTTPS
  FHIR searchset scanning through a separately provisioned HTTP client.
  Redirects are forbidden; each page is restricted to the exact granted
  resource path and a short allowlist of paging query keys.
  The verifier is consulted before every page; a denial stops processing.

Both readers reuse `adaptive.governance.validate_environment` and the
existing S01 `adaptive.schema_discovery.discover_source_schema`. Outputs
include schema metadata, row/page counts and explicit flags stating that
mapping, source entitlement certification, clinical validation and export
authorization **have not** been established.

## Supported versus unsupported

| Path | Implemented candidate | Still missing |
|---|---|---|
| Hospital PostgreSQL | Read-only, bounded, explicit-schema/column metadata scans, delegated verification callback | Institution-owned read-only DB role/TLS certificate/driver, real PostgreSQL integration tests, source-specific audits |
| Hospital FHIR REST | Single-resource-type, bounded searchset Bundle metadata scanning with strict paging controls | Institution-provided OAuth/SMART authentication, verified network egress/TLS, complete FHIR resource/profile/reference validation |
| SQL Server | No remote execution in S06 | Institutional least-privilege read-only adapter and database-role proof |
| Bulk FHIR `$export` | No export in S06 | Approved asynchronous authorization, manifest/download integrity, permitted staging and dedicated privacy review |
| MIMIC-IV / All of Us | Generic S06 remote connector intentionally rejects these families | Their separate source-specific approved pathways |
| Hospital row export/OMOP ETL | Explicitly not supported | Signed ETL plan, clinical and data-steward review, disclosure and release gates |

### Strong prerequisites

The caller must provide an independently managed `ExecutionPolicy` with
restricted or internally-approved classification, nonexporting behavior,
institutional or approved HPC compute, an authenticated actor, reviewer and
attestation. The `RemoteGrant` and source manifest must agree exactly.
Expired/naive-time grants, unrecognized families and unverifiable authorization
fail before a network/database operation.

The verifier callback is only an **integration point**. A locally provided
`lambda _: True` is suitable solely for invented test doubles and must
never be installed for patient data. Actual production use needs a real
institution-owned verifier, separate from the researcher's editable notebook,
with replay-resistant scoped access decisions, expiry/revocation checking,
nonpublic audit evidence and independently enforced credentials/roles. A
client-side policy cannot substitute for network ACLs, database read-only
roles, DUA/IRB review or TLS certificate validation.

### Example: synthetically tested PostgreSQL interface

~~~python
from datetime import datetime, timezone
from thomaslab.adaptive.remote_ingest import (
    RemoteGrant,
    discover_approved_postgres_schema,
)

grant = RemoteGrant(
    grant_id="REPLACE_WITH_INSTITUTIONALLY_VERIFIED_GRANT",
    source_system="hospital_ehr",
    source_release="v1",
    table_name="patients",
    connector_kind="POSTGRESQL",
    resource="research",
    actor="approved_researcher",
    expires_at=datetime(2030, 1, 1, tzinfo=timezone.utc),
)
# Prepared externally, inside institution-approved compute:
# engine: a TLS-enforced, least-privilege SQLAlchemy PostgreSQL Engine
# policy: a verified ExecutionPolicy with matching actor and approved roots
# verify_authorization: a trusted institutional verifier (NOT a dummy lambda)
# manifest: a source-governance-approved, matching source manifest
report = discover_approved_postgres_schema(
    engine,
    grant=grant,
    policy=policy,
    source_manifest=manifest,
    verify_authorization=verify_authorization,
    columns=("patient_id", "gender"),
)
assert report["authorized_for_export"] is False
~~~

This illustrates an **interface**, not a runnable authorized hospital
connection. In S06 tests, the engine and verifier are synthetic stand-ins.
Numeric/clinical value types are converted to lexical strings *only for
metadata profiling*; their native physical types, code systems, exposure
semantics, source release and source rights are not independently validated.

### FHIR interface

~~~python
from thomaslab.adaptive.remote_ingest import (
    discover_approved_fhir_server_schema,
)

# client: institution-provisioned HTTP client with verified TLS/OAuth/network ACL
# grant.resource: exact HTTPS .../fhir/Observation collection path
# manifest.resource_type: "Observation"
report = discover_approved_fhir_server_schema(
    client,
    grant=fhir_grant,
    policy=policy,
    source_manifest=manifest,
    verify_authorization=verify_authorization,
    max_pages=4,
)
assert report["authorized_for_export"] is False
~~~

Only the top-level JSON attribute names and *types* of matching resources enter
transient DataFrames; nested clinical content is **not** mapped or approved.
Missing, inconsistent, nonfinite or malicious responses fail closed.
The two APIs never persist patient data or generate OMOP research tables.

## S06 test evidence and acceptance gates

Synthetic-only development suite: **39/39 passed**, using fake PostgreSQL
connections, fake HTTP responses and isolated contract-compatible stand-ins
for existing governance/S01 dependencies. Both exact source and test Git
blobs match the locally tested files. Python 3.9/3.10/3.11 syntax parsing
passed; these are **not** runtime certification on a Python 3.9 HPC node.

~~~bash
python -m pytest -q tests/test_adaptive_remote_ingest.py
python -m pytest -q tests/test_adaptive_structured_ingest.py \
    tests/test_adaptive_schema_intake.py
python scripts/ehr_platform_status.py
# The full exact-sha HPC release candidate gate remains separately required:
bash scripts/verify_hardening_candidate.sh
~~~

**P1-03 stays OPEN.** Remaining requirements include independently
authenticated and source-approved live PostgreSQL/FHIR tests, SQL Server
or other required hospital database family adapters, source-specific FHIR
Bulk Data controls, comprehensive malformed-input coverage, full actual-Core
pytest/typing/lint/runtime QA, secure audit/permissions evidence, and
independent hospital data-steward/clinical validation. The S06 milestone
completes the *bounded remote connector contract candidate* but not the
entire 46-task ingestion deliverable.

See the [full staged hospital dataset plan](../../guides/ehr-platform-build-plan.md)
and [S05 local structured-ingestion guide](structured_ingest.md).

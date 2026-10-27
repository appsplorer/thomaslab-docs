# Governed structured metadata intake: SQLite and FHIR NDJSON (S05)

**Engineering state:** Private Core PR #34 candidate. S05 added
`thomaslab.adaptive.structured_ingest` with two entry points and
`tests/test_adaptive_structured_ingest.py` (41 synthetic local tests).
**No exact-head full Core/Herts HPC or real patient-data authorization/validation is established.**

## Architecture and boundaries

This adds **metadata discovery**, not a general-purpose database adapter,
HL7 FHIR server client, Bulk FHIR exporter, clinical ETL or patient-data
distribution tool. It reuses the existing
`adaptive.governance.validate_environment`,
`ensure_approved_input` and `adaptive.schema_discovery.discover_source_schema`.
The source owner, IRB/DUA, institutional storage/credential controls and
source manifests must be independently approved; declarations in a local
manifest are not external proof of permission.

| Source | Entry point | Supported scope | Explicit exclusions |
|---|---|---|---|
| Approved local `.sqlite` | `discover_approved_sqlite_schema` | Read-only *ordinary named tables*, schema and null metadata | Arbitrary SQL, views, remote PostgreSQL/SQL Server, network/linked servers, automatic key or code interpretation |
| Approved local `.ndjson` | `discover_approved_fhir_ndjson_schema` | Single declared FHIR resource type per file, top-level field and JSON-type profiling | Remote FHIR endpoints, OAuth, Bulk Data API downloads, transaction bundles, clinically validated FHIR parsing |
| All of Us participant CDR | None in this module | **Not accepted** | Local/HPC CDR extraction or Workbench bypass |

Both APIs require an absolute file path, an `ExecutionPolicy` with approved
roots, and a source manifest containing `source_system`, `source_release`,
`table_name` and `classification`. Restricted hospital sources additionally
require the existing actor/reviewer/institutional attestations and source-use
declaration. These are policy checks, not proof of external access rights.
They never log rows, publish records, approve mappings or authorize exports.

## SQLite read-only metadata inspection

~~~python
from pathlib import Path
from thomaslab.adaptive.governance import ExecutionPolicy
from thomaslab.adaptive.structured_ingest import discover_approved_sqlite_schema

root = Path("/your-approved/synthetic-lab-workspace")
policy = ExecutionPolicy(
    environment="local",
    approved_input_roots=(root,),
    approved_output_roots=(root,),
)
report = discover_approved_sqlite_schema(
    root / "synthetic.sqlite",
    policy=policy,
    source_manifest={
        "source_system": "synthetic_hospital",
        "source_release": "v1",
        "table_name": "labs",
        "classification": "SYNTHETIC",
    },
)
assert report["authorized_for_export"] is False
~~~

This example assumes an **already created synthetic-only SQLite database**
containing a `labs` table. The function opens local SQLite in read-only
mode, with `PRAGMA query_only`, a fixed SELECT of an identifier-validated
ordinary table, a consistent read transaction, and no caller-supplied SQL.
Views/virtual tables, symlinks, ambiguous columns, SQLite BLOB values,
nontext clinical keys/codes and out-of-root files are rejected.

SQLite values are **lexically normalized to text for metadata inspection**:
the S01 physical type profile **does not represent native SQLite storage
types**, numerical validity, medical codes or medication exposure.
`physical_storage_dtype_validated=False` is always returned.

Default batches are at most 1,000 rows and 256 fields, using a 128 KiB
SQLite row-size constraint on drivers that support `setlimit`.
Python 3.9 drivers without `setlimit` are restricted to SQLite files
no larger than 32 MiB; large files must undergo additional approved
environmental/driver validation. These limits do not prove safe operation
for arbitrary untrusted databases, nor certify immutable source snapshots.

## Local FHIR NDJSON metadata inspection

~~~python
from thomaslab.adaptive.structured_ingest import discover_approved_fhir_ndjson_schema

report = discover_approved_fhir_ndjson_schema(
    root / "synthetic-observations.ndjson",
    policy=policy,
    source_manifest={
        "source_system": "synthetic_hospital",
        "source_release": "v1",
        "table_name": "observations",
        "classification": "SYNTHETIC",
        "resource_type": "Observation",
    },
)
assert report["authorized_for_export"] is False
~~~

For this metadata preflight, the reader accepts one FHIR resource per NDJSON
line and a declared resource type from its finite supported set (Patient,
Encounter, Observation, Condition, Procedure, MedicationRequest,
MedicationDispense, MedicationAdministration, DiagnosticReport,
DocumentReference, Specimen). It rejects malformed UTF-8/JSON, duplicate
JSON keys, nonfinite numeric constants, resource-type mismatch, ambiguous
top-level attributes, blank lines and exceeded line/row/column limits.

Two bounded passes over the **same opened file descriptor** identify the
union of top-level attributes while accommodating FHIR optional fields.
Only JSON *type markers* (e.g., string, number, object) enter the S01 scan,
never patient IDs, text or clinical values. The two passes are checked for
byte-hash agreement and ordinary file modification; the resulting
`fhir_shape_fingerprint_sha256` includes resource type and JSON value
type signatures. A non-null top-level JSON type conflict is marked
`BLOCK_FHIR_JSON_TYPE_DRIFT`.

FHIR top-level fields and types are **not** validated against full FHIR
profiles, cardinality, references, nested extensions, terminology or
institution-specific data quality rules. The metadata output and aggregate
counts still require appropriate disclosure review.

## Synthetic verification, evidence and remaining gaps

~~~bash
python -m pytest -q tests/test_adaptive_structured_ingest.py
python scripts/ehr_platform_status.py
# Then perform exact-current-sha full checks in an approved CPU Slurm job.
bash scripts/verify_hardening_candidate.sh
~~~

The 41 new synthetic tests passed locally on Python 3.13.5 with a faithful
stand-in for existing source/governance dependencies. The exact new source
and test Git blob hashes match these locally tested files; **full real Core
imports, Python 3.9 runtime, complete pytest/quality and Herts/UGA HPC
acceptance have NOT been executed in this session**.

**P1-03 remains OPEN.** Hospital-grade external SQL Server/PostgreSQL
connection controls, SQL/FHIR access authorization and audit integration,
FHIR-server authentication and Bulk Data download policy, richer source
semantics, comprehensive malformed-input tests across all supported
modalities and full current-head acceptance remain. Local SQLite/FHIR
metadata preflight must not be described as complete approved data
ingestion or an OMOP ETL. Other S01/S02/S03/S04 methods remain separately
review-required.

See the [hospital EHR engineering plan](../../guides/ehr-platform-build-plan.md).

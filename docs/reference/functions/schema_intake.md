# `thomaslab.adaptive.schema_intake` — API reference

**Status:** S02 *candidate*; implementation and synthetic regression tests
are committed. Exact-commit Core CI/HPC, authorized-source scientific review,
SQL/FHIR adapters and institutional permission evidence are **not accepted**.

## `discover_approved_file_schema`

~~~python
def discover_approved_file_schema(
    path: pathlib.Path,
    *,
    policy: ExecutionPolicy,
    source_manifest: dict[str, Any],
    chunk_rows: int = 10_000,
    max_batches: int = 100_000,
    max_columns: int = 1024,
) -> dict[str, Any]:
~~~

Uses the existing `adaptive.governance.validate_environment`,
`ensure_approved_input`, `adaptive.source.iter_source_chunks`, and
`adaptive.schema_discovery.discover_source_schema` components; it creates
**no duplicate ingest engine**. The manifest requires `source_system`,
`source_release`, `table_name` and `classification`. Restricted
sources additionally require the governance policy's institutional
actor/reviewer/attestation and source use declaration. These are declarations,
**not** external verification of IRB, DUA, credentials, institutional storage
controls or human-subjects authorization.

Supports local `.csv`, `.tsv`, `.csv.gz`, `.tsv.gz`, `.parquet`,
and single-sheet `.xlsx` paths through existing source readers.
For CSV/TSV, a strict header preflight rejects missing, duplicate and
case-colliding headers that Pandas could otherwise rename silently. Input
must be an absolute reviewed path under explicitly approved input roots;
path symlinks and unknown formats are denied. Rows remain in bounded
in-memory batches; file metadata is compared before and after the scan
to detect ordinary concurrent changes. This is **not** a complete
filesystem-race or immutable-snapshot guarantee.

A participant-level All of Us CDR file intake is blocked, even if an otherwise restricted source declares the PUBLIC_AGGREGATE tier: run
authorized Workbench-native source queries inside the Workbench instead.
No local file scan is permission to transfer, download or publish data.
SQL and FHIR ingestion need separate approved connection policies and
are **not** implemented by this file function.

The returned metadata includes the original discovery report,
`source_format`, `source_classification` and explicit
`source_permission_independently_verified=False`,
`clinical_mapping_approved=False` and
`authorized_for_export=False`. No row values or file paths are added to the
result. Schema names and aggregate counts may still be sensitive and must
remain inside authorized compute until disclosure review.

## Synthetic demonstration

~~~python
from pathlib import Path
from thomaslab.adaptive.governance import ExecutionPolicy
from thomaslab.adaptive.schema_intake import discover_approved_file_schema

root = Path("/approved/synthetic/demo")  # replace with your actual approved folder
policy = ExecutionPolicy(
    environment="local",
    approved_input_roots=(root,),
    approved_output_roots=(root,),
)
report = discover_approved_file_schema(
    root / "synthetic_labs.csv.gz",
    policy=policy,
    source_manifest={
        "source_system": "synthetic_hospital",
        "source_release": "v1",
        "table_name": "labs",
        "classification": "SYNTHETIC",
    },
    chunk_rows=10_000,
)
assert report["authorized_for_export"] is False
~~~

This documentation example assumes the explicitly synthetic file already
exists. Never replace that path with hospital/MIMIC/All of Us records outside
the source owner's approved environment.

## Testing and outstanding work

~~~bash
python -m pytest -q tests/test_adaptive_schema_intake.py
python -m pytest -q tests/test_adaptive_schema_discovery.py
bash scripts/verify_hardening_candidate.sh
~~~

New regression cases cover compressed CSV, ambiguous headers, corrupt gzip,
header-only sources, out-of-root paths, missing classification, restricted local
execution, declared institutional execution, All of Us Workbench barriers,
symlinks, unsupported formats and scan limits. Parquet needs `pyarrow`.
The standalone S02 wrapper was smoke-tested with stand-in dependencies, including a test rejecting a RESTRICTED All of Us source mislabelled as PUBLIC_AGGREGATE;
**the full actual Core implementation has not yet passed these new tests
or exact-commit release checks**. P1-03 stays OPEN until approved SQL/FHIR
ingestion, source-specific tests and release criteria are implemented.

See [hospital EHR build plan](../../guides/ehr-platform-build-plan.md)
and [schema discovery reference](schema_discovery.md).

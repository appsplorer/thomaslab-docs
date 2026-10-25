# S26/S27 — Synthetic streaming and columnar benchmark candidate

**Status:** partial engineering implementation only. P4-01 and P4-02 remain OPEN. No MIMIC-IV, All of Us, or hospital patient data are used. A benchmark cannot authorize access, clinical use, or research dataset release.

The private module **thomaslab.adaptive.synthetic_scale** supports:

- **iter_synthetic_event_batches**: stable invented integer events, with visit/person/site consistency and batches bounded to 100,000 rows. No row values originate from external files.
- **profile_synthetic_stream**: checksum and category reconciliation across invented records, with batch-invariant SHA-256 and elapsed time. Returns aggregate-only evidence and explicitly declares that peak resident memory, HPC performance and clinical correctness are NOT verified.
- **benchmark_synthetic_parquet**: optional, NOT locally runtime-verified PyArrow Zstd Parquet writer and fixed DuckDB read-only query of invented synthetic event counts. Requires already-installed institution-approved pyarrow and duckdb, an existing absolute private 0700 root, and an explicit output byte quota. Uses private temporary files, a fixed column schema, checks row/filter reconciliation, refuses overwrite and leaves authorized_for_export=False.

## Focused local evidence — 25 October 2026

- Python 3.13.5: **18/18 synthetic tests passed**, including batch invariance, deterministic site/person/visit linkage, parameter limits, private directory and symlink rejection.
- Python 3.9–3.13 AST grammar parsing passed.
- One-million-row synthetic streaming test: 1,000,000/1,000,000 events reconciled, four synthetic codes each with 250,000 rows, max batch 50,000. This is NOT a Parquet, DuckDB or HPC benchmark.
- PyArrow and DuckDB unavailable in the local runtime. The optional actual Parquet write/query branch DID NOT execute; missing-dependency failure was checked.

## On approved HPC / cluster

~~~bash
# Use an approved, exact-SHA checkout and Python environment first.
python -m pytest -q tests/test_adaptive_synthetic_scale.py
python - <<'PY'
from thomaslab.adaptive.synthetic_scale import profile_synthetic_stream
print(profile_synthetic_stream(1_000_000, batch_rows=50_000))
PY
# Install institution-approved Python 3.9-compatible pyarrow and duckdb builds.
# Use a private, existing 0700 synthetic-only directory:
mkdir -m 700 -p "$THOMASLAB_HPC_ROOT/benchmarks/synthetic_columnar"
python - <<'PY'
import os
from pathlib import Path
from thomaslab.adaptive.synthetic_scale import benchmark_synthetic_parquet
root=Path(os.environ["THOMASLAB_HPC_ROOT"]) / "benchmarks/synthetic_columnar"
print(benchmark_synthetic_parquet(root, rows=1_000_000, batch_rows=50_000))
PY
~~~

**P4-01 still open:** run and verify true Parquet/Zstd/DuckDB projection/filter/compression/query-plan comparisons against the exact head SHA, test version-pinned package compatibility and document disk/memory/elapsed performance.

**P4-02 still open:** measure credible peak RSS, disk I/O, timings and failure recovery at 1m, 10m and 100m synthetic events on approved CPU allocations. Confirm reproducibility, batching, environment provenance and actual memory ceilings. Neither the generated files nor the timing metrics constitute validation of clinical ETL, source authorization or any patient-record export.

Related: [EHR build plan](../../guides/ehr-platform-build-plan.md), [incremental rebuild](incremental_rebuild.md), [release staging](atomic_release_stage.md).

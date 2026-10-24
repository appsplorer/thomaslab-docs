# `thomaslab.adaptive.schema_discovery` — API reference

**Status:** locally tested synthetic candidate in private Core PR #34;
no current-commit full Core CI/HPC or clinical source acceptance.

The module is an **in-memory metadata profiler** for finite streams of
Pandas DataFrames. It reuses the existing
`thomaslab.adaptive.source.iter_source_chunks` and governed source-reader
contract; it does not read files, open a Workbench, run SQL, inspect notes,
export PHI or approve terminology mappings.

## `discover_source_schema`

~~~python
def discover_source_schema(
    batches: Iterable[pd.DataFrame],
    *,
    source_system: str,
    source_release: str,
    table_name: str,
    max_batches: int = 100_000,
    max_rows_per_batch: int = 200_000,
    max_columns: int = 1024,
) -> dict[str, Any]:
~~~

**Input:** finite iterator of already authorized, memory-bounded tabular
batches; validated source/system/release/table labels. Maximum rows are
enforced *per batch*, not as a universal RAM guarantee.

**Output:** metadata fields
`schema_fingerprint_sha256`, `rows_inspected`,
`batches_inspected`, `columns` (name, physical dtype families,
null count, unreviewed field-role hints), `dtype_conflict_count` and
`status`. The normal status is `REVIEW_REQUIRED`; physical type
changes within chunks return `BLOCK_DTYPE_DRIFT`. Schema metadata,
column names and aggregate counts must stay inside authorized compute
until the applicable institutional/programme disclosure review.

**Stop conditions:** duplicate or case-colliding headers; empty sources;
missing, reordered, ambiguous columns across chunks; malformed labels;
invalid bounds; chunk larger than configured limit. Raises before returning
an incomplete report. The schema fingerprint is **not** the patient/source
file fingerprint.

## `compare_source_schemas`

~~~python
def compare_source_schemas(
    previous: dict[str, Any],
    current: dict[str, Any],
) -> dict[str, Any]:
~~~

**Input:** two completed version-1 metadata profiles from the same source
system and source table.

**Output:** added/removed columns, changed physical dtype families,
release-change flags, structural hash-change flags and explicit
review-required status. Even an unchanged structural hash **does not**
verify clinical semantics, timestamp conventions, units, code sets,
patient linkage, vocabulary version validity or scientific suitability.

## Minimal synthetic test

~~~python
import pandas as pd
from thomaslab.adaptive.schema_discovery import (
    compare_source_schemas, discover_source_schema,
)

sample = pd.DataFrame({"patient_id": ["SYNTH001"], "lab": ["123"]})
v1 = discover_source_schema(
    iter([sample]), source_system="demo_site",
    source_release="v1", table_name="labs",
)
v2 = discover_source_schema(
    iter([sample.assign(new_unit="mg/dL")]), source_system="demo_site",
    source_release="v2", table_name="labs",
)
assert compare_source_schemas(v1, v2)["status"] == "REVIEW_REQUIRED"
assert v1["authorized_for_export"] is False
~~~

See the [full engineering plan](../../guides/ehr-platform-build-plan.md)
and [data access safeguards](../../guides/dataset-access-and-adapters.md).

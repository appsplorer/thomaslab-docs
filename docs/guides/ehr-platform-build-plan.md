# Building hospital EHR datasets: staged implementation and acceptance

**Development checkpoint:** 24 October 2026 · Session **S01**  
**Full private progress ledger:** `configs/ehr_platform_development_tracker.json`
in the private Core repository.  
**Input specification:** the four user-supplied briefs on OMOP/MIMIC-style
research data architecture, adaptive schema mapping, the clinical terminology
knowledge base, and MIMIC-scale research infrastructure.

## Scope and architectural decision

Thomas Lab Core is the executable **research data engineering software**.
The resulting **hospital EHR research resource** is a separately governed
dataset or federated network. Supporting a given hospital, model or study
requires an approved source adapter, lawful data access, quality evidence and
clinical validation; it is not implied by a successful software import.

Reuse existing Core components before adding new code:

| Existing component | Current responsibility | New extension relationship |
|---|---|---|
| `adaptive.source` | Lossless-first CSV/TSV/.gz, XLSX and Parquet import/chunk iteration | Feeds batches to new source metadata profiler |
| `adaptive.mappings` | Canonical mapping candidate + reviewer record | Preserve one-to-one compatibility; extend **typed ETL** separately |
| `adaptive.mapping_workbench` | Jupyter human review | Later: multi-table review, expert escalation and alternatives |
| `adaptive.adapter_registry` | Versioned, reviewed source adapters | Later: store reviewed fingerprints and approved schema-drift decisions |
| `harmonize`, `healthcare_quality` | Site/unit/structural diagnostics | Later: monitor source-specific quality contracts |
| `clinical_leakage`, `clinical_followup` | Time-zero, availability and follow-up preflights | Later: gate study-mart generation and external validation |

**Proposed standard representation:** OMOP CDM-compatible core with
MIMIC-style clinically meaningful source modules and separately versioned
extensions for medication administration, PGx, imaging and lineage. Preserve
original records in approved storage; never overwrite raw source evidence.
Use Parquet/DuckDB as a measured starting point; add distributed processing
only after actual site/HPC benchmarks justify it.

## Development stages and acceptance

| Stage | Acceptance deliverables |
|---|---|
| **P0** Architecture, access, provenance (6) | Governance contracts, site/person identity rules, OMOP, event timing, immutable raw archives and role-based restrictions |
| **P1** Ingestion/discovery/auto-mapping (8) | Memory-bounded source metadata, drift, relationships, inference, ranked proposals, intern/expert review and approved mapping memory |
| **P2** Terminology knowledge base (8) | Licensed source registry, Athena importer, versioned concept indexes, synonyms, contextual compatibility, UCUM and expert benchmark |
| **P3** Clinical ETL and tables (8) | Typed multi-table transform graph, safe compilation, identity joins, OMOP target tables, extension tables, reconciliation and immutable staged releases |
| **P4** Performance/lineage/scalability (8) | Parquet/DuckDB, 1m–100m synthetic tests, full lineage, observability, temporal/quality gates, federation and approved HPC |
| **P5** Researcher/independent acceptance (8) | Guided Jupyter workflows, versioned phenotypes, three examples, five independent usability trials, 15–20 unseen datasets, governance and FAIR documentation |

**Important:** a task with code but no passing full Core CI is **locally
implemented**, not accepted for production. For every session record a
specific tested SHA, local synthetic results, full CI/HPC status, newly
completed feature tasks, still-open tasks and restricted-source approvals.

## Session S01: bounded source schema discovery

Two new candidate functions in
`thomaslab.adaptive.schema_discovery`:

### `discover_source_schema(...)`

Safely scans in-memory Pandas batches supplied by an already authorized
source reader. Identifies all source column names, physical dtype families,
missing counts, conservative *unreviewed* identifier/code/unit/time hints,
total inspected rows, and a stable SHA-256 structural fingerprint. It **never
copies row values or provides automatic clinical mapping approval**.

The algorithm rejects duplicate/case-colliding columns, changing column
names or order between batches, empty streams, malformed source identifiers,
overly large batches and exceeded chunk limits. A physical dtype change
across batches returns `BLOCK_DTYPE_DRIFT`. A normal scan returns
`REVIEW_REQUIRED`—not `PASS_TO_RELEASE`.

**Security note:** field names, site/release labels and count statistics can
themselves be sensitive. Results may remain inside the institutionally
approved research enclave only and need independent disclosure review.
Fingerprints hash *schema metadata*, not patient records or the raw file.

### `compare_source_schemas(previous, current)`

Compares two completed source metadata reports and returns added, missing or
physical-type-changed columns and source-release changes. Identical
structural fingerprints **cannot establish identical clinical semantics**,
mapping validity or source-data equivalence. The output is never an
automatic ETL approval.

### Fully invented example

~~~python
import pandas as pd

from thomaslab.adaptive.schema_discovery import (
    compare_source_schemas,
    discover_source_schema,
)

a = pd.DataFrame({
    "patient_id": ["SYNTH-0001", "SYNTH-0002"],
    "test_unit": ["mg/dL", None],
    "result": [1.0, 2.0],
})
before = discover_source_schema(
    (batch for batch in (a.iloc[:1], a.iloc[1:])),
    source_system="demo_hospital",
    source_release="v1",
    table_name="labs",
)
assert before["status"] == "REVIEW_REQUIRED"
assert before["rows_inspected"] == 2

after_frame = a.drop(columns=["test_unit"]).copy()
after = discover_source_schema(
    iter([after_frame]),
    source_system="demo_hospital",
    source_release="v2",
    table_name="labs",
)
diff = compare_source_schemas(before, after)
assert diff["removed_columns"] == ("test_unit",)
assert diff["source_release_changed"]
assert diff["clinical_mapping_approved"] is False
~~~

For later **authorized** CSV/Parquet scans, source paths must be verified
by the existing `adaptive.governance.ensure_approved_input` and
`ExecutionPolicy` *before* passing the
`adaptive.source.iter_source_chunks` iterator to this function. The
metadata profiler does not itself authorize any file path or dataset.
Large-scale performance and restricted-source semantic tests remain open.

## Session test evidence

The 15 synthetic regression tests were actually run in an isolated local
environment with Pandas **2.2.3** and pytest **9.0.2** and passed. The
source module was compiled successfully. Cases include missing values,
chunk-invariant fingerprints, no raw values in reports, altered source
values, ambiguous headers, column-order changes, chunk memory limits,
empty iterators, invalid source identifiers, changing dtypes, changed
columns, changed release and unapproved status.

Run on approved developer/HPC checkout:

~~~bash
python -m pytest -q tests/test_adaptive_schema_discovery.py
# Full exact-Git-SHA acceptance in an approved CPU Slurm allocation:
bash scripts/verify_hardening_candidate.sh
~~~

The full acceptance script additionally requires the exact-source
`THOMASLAB_EXPECTED_SHA`, approved `THOMASLAB_PYTHON` and a protected
`THOMASLAB_QA_REPORT_ROOT`. See [HPC A–Z](hpc-a-to-z.md).

**S01 measured progress against these 46 newly scoped feature deliverables:**

- Locally implemented with focused synthetic tests: **2 / 46 (4.3%)**
- Open/unimplemented or not independently validated in this tracker: **44 / 46 (95.7%)**
- Accepted for institutional real patient datasets: **0 / 46**
- Full current-commit private Core QA: **NOT VERIFIED**
- Real MIMIC-IV, All of Us and new hospital EHR validation: **NOT STARTED**

Pre-existing Core functionality is **not counted as new implementation**.
An open tracker entry may overlap existing candidate code; it remains open
until integration and acceptance evidence support closure. This is not a
percentage of the entire pre-existing Thomas Lab platform.

## Reproducible progress and acceptance reporting

Run from the private Core checkout after each development session:

~~~bash
python scripts/ehr_platform_status.py
python -m pytest -q tests/test_adaptive_schema_discovery.py \
    tests/test_ehr_platform_status.py
~~~

The progress script validates the persistent
`configs/ehr_platform_development_tracker.json` ledger and reports,
for each phase, tracked deliverables, source-code implementation with
evidence, still-open tasks and separately approved real-data acceptance.
It refuses duplicate task identities and premature scientific approval.

**Session S01 test evidence:** 15 schema/drift tests plus 5 independent
status-ledger tests = **20 isolated tests PASS** on Python 3.13.5,
Pandas 2.2.3 and pytest 9.0.2. No Python 3.9, full Core CI/HPC,
Ruff/mypy or authorized patient-data acceptance was performed in this
session.

## Required order for next development sessions

**S02:** connect the schema scanner to approved source manifests/readers;
test CSV.gz/Parquet streaming, malformed inputs and site-specific schemas.
No patient data needed.

**S03:** add domain and table-relationship candidates with explicit
abstention for ambiguous keys; integrate with the existing Jupyter
mapping workbench. Preserve reviewer sign-off.

**S04:** establish the versioned **licence-gated clinical terminology
registry** and source-specific indexes. Do not embed licensed vocabulary
content or infer clinical equivalence from string resemblance.

**S05:** implement a typed, reviewed multi-table ETL graph and staging
table construction. Do not weaken the existing single-table one-to-one
mapping contract; retain backwards compatibility.

**Later sessions:** release lineage, incremental/resumable Parquet ETL,
observability, scalability benchmarks, held-out hospital mapping gold
standards, and independent researcher studies. The real-source tests
begin only inside the source-approved environment once access exists.

## Nonnegotiable release gates

A study-specific software release needs independently evidenced
**software, structural source-data, scientific/statistical, governance,
and researcher-usability** decisions. All of Us participant-level data
must stay inside its permitted Workbench; PhysioNet or hospital data must
remain under the applicable agreements and institutionally approved
compute. This public documentation contains no patient records, secret
paths, licence-restricted vocabulary dumps or unapproved export route.

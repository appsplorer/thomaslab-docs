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
names or order between batches, empty streams/header-only tables, malformed source identifiers,
overly large batches and exceeded chunk limits. Lexical blank strings and tokens such as `NA` are preserved, not automatically classified as missing; source-specific missingness review is required. A physical dtype change
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

The 17 synthetic regression tests were actually run in an isolated local
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

**Session S01 test evidence:** 17 schema/drift tests plus 5 independent
status-ledger tests = **22 isolated tests PASS** on Python 3.13.5,
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


## Session S02: governed local file intake (candidate; not yet accepted)

**24 October 2026.** A new private code module,
`thomaslab.adaptive.schema_intake`, connects the existing policy gate,
approved-path checker and chunked CSV/TSV/gzip/Parquet/XLSX reader with
the S01 metadata-only schema scanner. No parallel reader or mapping system
was created. The file intake adds a strict CSV header check that blocks
missing, repeated and case-colliding names that Pandas could mangle,
refuses unsupported formats and symlink paths, checks ordinary concurrent
file changes, and preserves explicit restrictions on publication/exports.

The API is documented in the [S02 governed file-intake reference](../reference/functions/schema_intake.md).
File classification declarations **are not proof** of data access rights;
all hospital/PhysioNet and source-owner authorizations still require
independent institutional verification. All of Us participant-level CDR
records are **not** accepted by this local file intake; its authorized
Workbench-specific connector remains a separate task.

**Isolated exercise evidence:** 15 S02 wrapper smoke cases passed using
local stand-in implementations of pre-existing source/governance/discovery
dependencies; one Parquet case was skipped because `pyarrow` was not
installed. This verifies the new wrapper's basic control flow, **not**
integration against the actual entire private Core package. The source and
regression tests are committed to draft Core PR #34; full exact-SHA Core
pytest, Ruff, mypy, Python 3.9/3.11, Parquet, HPC and independent acceptance
have **not** passed on this new commit.

**Tracker decision:** `P1-03` remains OPEN: approved SQL and FHIR ingress,
malformed-input handling across all authorized modalities and full-release
acceptance are still missing. The new 46-deliverable ledger therefore stays
at **2/46 with focused local implementation evidence, 44/46 open, 0/46
independently accepted for real data**. No source-specific PHI/clinical
rights or security certification is inferred.

Execute on an approved developer/HPC checkout with full package dependencies:

~~~bash
python -m pytest -q tests/test_adaptive_schema_intake.py \
    tests/test_adaptive_schema_discovery.py \
    tests/test_ehr_platform_status.py
bash scripts/verify_hardening_candidate.sh
~~~

Next: complete the still-open SQL/FHIR and approved-manifest contracts
before making new tracker completion claims; proceed to S03 domain/key
inference only with explicit abstention and human review.


## Session S03: contextual clinical-domain and source-grain candidates

**24 October 2026.** In private Core PR #34, the new
`thomaslab.adaptive.clinical_domain_inference` module consumes **completed
S01 schema metadata only**. It does not read patient records, transfer data,
infer code-set equivalence, approve mappings or write a dataset. It reuses the
previous scanner's source release and structural fingerprint.

The method proposes one of 13 reviewable domain families: person,
encounter, ICU stay, condition, procedure, measurement, medication order,
dispense, administration, clinical note, PGx, imaging or claims. It returns
ranked source-column/table-name evidence with heuristic ranking **scores that
are not calibrated probabilities**. It also proposes a source row grain only
where structural identifier hints and domain agree; uniqueness, valid keys
and patient/encounter linkage are *always unverified*. Contradictory medication
order/administration evidence requires abstention.

Statuses are `CANDIDATE_REVIEW_REQUIRED`,
`ABSTAIN_INSUFFICIENT_EVIDENCE`,
`ABSTAIN_AMBIGUOUS_DOMAIN`, or `BLOCK_SOURCE_SCHEMA`. The returned
`mapping_approved`, `source_grain_verified`,
`clinical_semantics_validated` and `authorized_for_export` are all
`False`. For source-specific approval, progress through separately reviewed
P1-05 through P1-08 and clinical governance gates; never treat these
structural suggestions as signed source semantics.

Documentation: [S03 clinical-domain inference reference](../reference/functions/clinical_domain_inference.md).

**Exact source/test file evidence:** local 30/30 synthetic tests PASS
(Python 3.13.5, pytest 9.0.2), source module compile PASS, Python 3.9/3.11
grammar parse PASS; byte-identical source/test Git blob SHA values checked
against Core PR #34. These are **isolated focused tests only**, not evidence
of a clean full Core runtime, supported Python 3.9/3.11 test execution,
HPC Slurm compatibility, clinical accuracy, or authorization for real data.

**Scope-adjusted 46-deliverable ledger after S03:**
- P1-01, P1-02, P1-04: **3/46 locally implemented and tested (6.5%)**
- **43/46 OPEN**; P1-03 remains open for SQL/FHIR authorization and ingestion.
- **0/46** independently source-/clinically accepted.
- Existing methods outside this new 46-item ledger are not counted here.

Focused verification on an approved development checkout:

~~~bash
python -m pytest -q tests/test_clinical_domain_inference.py \
    tests/test_adaptive_schema_discovery.py \
    tests/test_ehr_platform_status.py
python scripts/ehr_platform_status.py
# Full exact Git SHA acceptance on approved HPC:
bash scripts/verify_hardening_candidate.sh
~~~

**Next required milestones:** finish P1-03 approved SQL/FHIR source ingestion
and malformed-input integration, then P1-05 *multi-table relationship/key
candidates* with patient/encounter cardinality, nullable admissions, distinct
source row grain and explicit abstention. After that, build reviewable
multi-target mappings, signed expert review queue and fingerprint-bound
approved mapping reuse. Complete licensed vocabulary import and staged
OMOP/extension table materialization only after their own acceptance tests.


## Session S04: multi-table candidate keys and bounded relationship diagnostics

**24 October 2026.** Added `thomaslab.adaptive.relationships` with two
review-required functions that reuse completed S01 schema profiles and S03
domain candidates rather than introducing a disconnected mapping system.

- `propose_table_relationships` proposes exact-column, within-source,
  same-release person→encounter→ICU/event relationships, optionally
  site-scoped via composite `site_id` keys. Cross-hospital, different-release,
  mismatched source physical types, one-sided site scope and multiple
  ambiguous parent ID aliases block or abstain.
- `validate_relationship_frames` checks *authorized, already-loaded* bounded
  Pandas frames (maximum 100,000 rows per table by default), detecting
  duplicate parent keys, orphan child links, inconsistent patient/encounter
  identities, and missing or lossy numeric identifiers. MIMIC-IV-like
  `labevents.hadm_id` nulls are specifically marked and require an explicit
  `allow_missing_child_foreign_key` diagnostic choice. It never certifies
  full-source completeness, clinical semantics or an approved join.

**Evidence:** The exact new code/test files were independently matched to
their GitHub Git blob hashes. Local S04 synthetic suite **34/34 PASS**;
S03+S04 together **64/64 PASS** on Python 3.13.5, pandas 2.2.3 and
pytest 9.0.2. Local Python compilation and 3.9–3.13 grammar checks pass.
The tests use schema-version-1 **metadata contract fixtures** and the
real S03 candidate module; this does **not** verify an independently
executed full S01 source ingestion process, complete Core pytest/coverage,
Python 3.9 runtime, UGA/Herts Slurm or clinical source truth.

The [S04 API reference](../reference/functions/relationships.md) has
the complete input/output contracts, synthetic example and limits.

**Scope-adjusted engineering ledger:**
- **P1-01, P1-02, P1-04 and P1-05** have focused local evidence (**4/46, 8.7%**).
- **42/46 remain OPEN (91.3%)**, including **P1-03** (complete
  approved CSV/Parquet/SQL/FHIR ingest), P1-06 through P1-08, the clinical
  terminology dictionary, ETL, full-source scalability and usability.
- **0/46** independently accepted for institutionally governed patient data.

Next implement the remaining approved-ingress P1-03 connector and
failure-handling contracts before promoting automated reviewed
multi-target mapping. No patient dataset, PhysioNet record or All of Us
Workbench participant data was downloaded, accessed or certified in S04.
The full exact-SHA QA and independent reviewer approval remain blocking.


## Session S05: approved local SQLite/FHIR metadata ingress — candidate

**24 October 2026.** The new \`thomaslab.adaptive.structured_ingest\`
component implements *two narrow source readers*:

- \`discover_approved_sqlite_schema\`: local SQLite \`.sqlite\` file,
  specifically declared ordinary table, read-only SQL and no arbitrary
  commands. Identifier/code columns must retain text affinity; value
  representation is normalized to text for schema inspection and is not
  validated original clinical storage type. On Python 3.9 without SQLite
  \`setlimit\`, local database files exceeding 32 MiB are blocked.
- \`discover_approved_fhir_ndjson_schema\`: single-declared-resource FHIR
  \`.ndjson\` local extracts, two-pass top-level schema profiling, bounded
  line/row/column scanning, JSON type fingerprints, duplicate-key and
  malformed JSON/UTF-8 rejection, and explicit JSON type-drift blocking.
  No remote FHIR endpoints or Bulk FHIR download are implemented.

Both call the **existing** source governance checks and
\`adaptive.schema_discovery\`, carry forward review-only semantics, and
return no original clinical values, approved mappings, patient-level
exports, external credential assurances or clinical-validity claims.
All of Us participant CDR remains Workbench-only and is expressly refused
by these local readers. Even metadata/counts remain disclosure-sensitive.

**Local test evidence:** 41/41 synthetic SQLite+FHIR tests PASS on
Python 3.13.5, pandas 2.2.3, pytest 9.0.2, with *test surrogates for the
existing* governance and S01 scanner (not a full Core runtime test).
Exact tested source and regression-test files were compared with the
committed Git blobs. The full private Core CI, complete pytest/Ruff/mypy,
Python 3.9 runtime, Herts/UGA HPC, authorized hospital EHR and MIMIC/
All of Us source-scientific acceptance have **not** passed.

[See S05 function reference](../reference/functions/structured_ingest.md).

**Ledger decision: P1-03 stays OPEN.** S05 does not supply external
SQL Server/PostgreSQL network connector entitlement and query execution
contracts, a signed FHIR server/Bulk export pipeline, comprehensive
source-specific malformed-input tests, nor independently run full Core
CI/HPC acceptance. Do not label P1-03 as complete from synthetic local
SQLite and FHIR file profiling alone.

**Cumulative 46-deliverable tracker (S05):** 4/46 (8.7%) locally
implemented and tested *under their complete scoped task criteria*,
42/46 OPEN (91.3%); 0/46 accepted for real patients. S05 adds
documented implementation and focused evidence **within still-open
P1-03**, not another completed deliverable. The next session must
finish the source-governed integration and source-specific adapter
contracts before the tracker percentage changes. No new branch was
merged into \`main\`.

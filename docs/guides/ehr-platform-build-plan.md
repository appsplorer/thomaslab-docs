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

**24 October 2026.** The new `thomaslab.adaptive.structured_ingest`
component implements *two narrow source readers*:

- `discover_approved_sqlite_schema`: local SQLite `.sqlite` file,
  specifically declared ordinary table, read-only SQL and no arbitrary
  commands. Identifier/code columns must retain text affinity; value
  representation is normalized to text for schema inspection and is not
  validated original clinical storage type. On Python 3.9 without SQLite
  `setlimit`, local database files exceeding 32 MiB are blocked.
- `discover_approved_fhir_ndjson_schema`: single-declared-resource FHIR
  `.ndjson` local extracts, two-pass top-level schema profiling, bounded
  line/row/column scanning, JSON type fingerprints, duplicate-key and
  malformed JSON/UTF-8 rejection, and explicit JSON type-drift blocking.
  No remote FHIR endpoints or Bulk FHIR download are implemented.

Both call the **existing** source governance checks and
`adaptive.schema_discovery`, carry forward review-only semantics, and
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
merged into `main`.


## Session S06 — approved remote connector contract candidate (24 October 2026)

**Implementation:** `thomaslab.adaptive.remote_ingest` adds typed,
expiry-bound `RemoteGrant` and `RemoteAuthorizationRequest` objects,
an externally supplied authorization-verification callback,
`discover_approved_postgres_schema` and
`discover_approved_fhir_server_schema`. This extends prior S01–S05
components; it does not replace the existing governed source scanner
or researcher mapping workbench.

The PostgreSQL path uses a separately configured SQLAlchemy-compatible
connection, `SET TRANSACTION READ ONLY`, fixed schema-qualified
identifier-vetted columns, a 30-second statement timeout and bounded
cursor batches. It does not create credentials, permit arbitrary SQL,
export rows or infer clinical code/field semantics.

The FHIR path accepts an institutional HTTP client and a tightly scoped
HTTPS resource collection. It rejects redirects, cross-host/path next
links, malformed/oversize Bundles, resource-type mismatch and conflicting
top-level JSON value types. Authorization is checked before every page.
It inspects only top-level field names and type markers, not clinical
resource contents for automatic mapping.

Both connectors **require** institutional actor/reviewer attestation,
nonexporting execution policy, aligned source manifest, an unexpired grant
and an external verifier. A researcher-provided verifier returning
`True` is not independent authentication; real IAM, hospital role
permissions, OAuth/TLS/network controls, DUA/IRB and facility-controlled
audit remain external prerequisites. The generic remote APIs reject
All of Us and MIMIC-IV data rather than bypassing their established
source-specific access routes.

**Verification:** 39/39 focused synthetic connector tests PASS locally;
Python 3.9/3.10/3.11 grammar parsing PASS. Synthetic PostgreSQL and
HTTP clients and isolated contract-compatible stand-ins for existing
governance/S01 utilities were used; therefore these results do **not**
establish a clean full Core runtime, approved live PostgreSQL/FHIR
authentication, Python 3.9 HPC, clinically appropriate relationships or
a privacy-reviewed patient dataset. Exact new source/test files were
verified against committed Git blob hashes.

[Full S06 API, authorization and limitations](../reference/functions/remote_ingest.md).

**P1-03 remains OPEN** pending institution-owned PostgreSQL/other SQL
credentials and database-role verification, SQL Server (if applicable),
live FHIR/OAuth and Bulk Data source-specific acceptance, complete-source
and corruption integration, clinical governance, and full exact-current-
commit Core CI/HPC gates. The 46-task ledger accordingly remains
**4/46 locally implemented and tested against complete task definitions,
42/46 OPEN, 0/46 independently source-scientifically accepted.**
S06 is a partial P1-03 increment rather than a separately completed
deliverable.

**S07 priority:** implement a source-independent review queue for
P1-06/P1-07 using disclosure-safe metadata and existing adaptive
mapping/adapter registry, while separately clearing live P1-03
institutional and full Core acceptance gates. Do not silently merge
candidate code into `main` before those gates pass.


## Session S07 — ranked multi-target field suggestions (24 October 2026)

**Implementation:** `thomaslab.adaptive.field_suggestions` extends the S01
metadata → S03 source-domain proposal pipeline with
`rank_reviewable_field_destinations(...)`. It uses existing
`get_domain_contract` and `CANONICAL_SCHEMA` aliases, plus bounded,
deterministic lexical ranking (never calibrated probability estimates).

Unlike the earlier one-to-one `adaptive.mappings` preview, the new
**review-only** candidate model retains several domain-qualified targets
for one source field without selecting any for ETL. Competing source
columns, conflicting target fields, generic time labels, weak fuzzy matches
and unknown source schemas explicitly abstain. It refuses to interpret
prescribing, dispensing or eMAR as equivalent exposures and flags
unreviewed ICD/RxNorm vocabulary, protected identifier linkage, assay/unit
and timestamp/availability semantics.

The source metadata fingerprint is recalculated for consistency with
S01 physical column/type metadata, but **original source authenticity
and authorization are not independently verified**. Output contains
field names and risk metadata only, not patient values; even field names
can be sensitive and require approved institutional storage.

**Local verification:** **37/37** focused synthetic regression tests PASS
(Python 3.13.5, pandas 2.2.3, pytest 9.0.2);
Python 3.9–3.13 grammar PASS. Exact source and test blob SHAs were
compared with the locally tested files. The S03 module is the actual
earlier implementation; S01 producer and canonical contract/alias modules
were represented by contract-compatible local test surrogates. This is
**not** an exact-current-commit Core integration/HPC acceptance test
or a calibrated clinical mapping benchmark. A synthetic 253-column
eight-domain timing of approximately 0.15 seconds was exploratory only.

[Read the S07 function guide](../reference/functions/field_suggestions.md).

**Ledger scope:** P1-06 is **LOCAL_TEST_PASS** only (not independently
accepted). **5/46** deliverables have focused local implementation
evidence (~10.9%); **41/46** are OPEN (~89.1%); **0/46**
are independently source-scientifically accepted. P1-03 remains OPEN
for institutional SQL/FHIR access integration and exact-SHA QA.
P1-07 role-aware intern/clinical expert/steward review queue is the next
bounded development milestone. The existing `MappingWorkbench` and
`AdapterRegistry` were not silently modified; S07 candidates are
not legacy one-to-one reviewed mappings or approved executable OMOP ETL.


## Session S08 — role-separated, persistent mapping review queue (24 October 2026)

**Implementation:** New `thomaslab.adaptive.review_queue.MappingReviewQueue`
consumes bounded **S07 metadata-only** candidate records and attaches each
task to source system, release, S01 structural fingerprint, model ruleset,
source field and reviewed alternative destinations. It does not read hospital
rows, transform or export PHI, construct OMOP tables, certify a drug exposure
or bypass the existing `MappingWorkbench` / `AdapterRegistry` approval.

This milestone implements a staged queue with source-scoped task IDs and
bounded role-filtered pending lists. An `intern` triages a specific S07
candidate, a **different** `clinical_expert` records supporting clinical
evidence, and a third `data_steward` records source-governance review.
Rejection at any stage is terminal. The final accepted stage is explicitly
`REVIEWED_FOR_VALIDATION`, **not** a clinically authorized mapping,
full-source acceptance or patient-data release.

For reproducibility, per-task JSON records are exclusively created in
a pre-created, approved and private local folder, and reviewer decisions
are recorded in sequence-numbered SHA-256 hash-linked append-only-by-API
event records with private file permissions and per-task write locks.
Identity checks use a **mandatory external role verifier interface**.
This is a *hook for institutional IAM*, not actual cryptographically
verified employee login or dataset-grant entitlement. Review rationales
and field labels could still contain sensitive information and must stay
inside the approved enclave; automated PHI scrubbing of free-form
rationale is not provided. Hash linking is not externally signed and
cannot prevent privileged filesystem attackers from rewriting/truncating
journal history. Managed append-only audits and integration with actual
hospital IAM remain independent acceptance prerequisites.

**Local tests:** **48/48** S08 focused synthetic tests PASS on Python
3.13.5 / pandas 2.2.3 / pytest 9.0.2; Python 3.9–3.13 syntax/grammar
check PASS. The exact committed source and test Git blobs matched the
locally executed files. These tests used the S03 and S07 mapping logic,
with *local contract-compatible surrogates* for S01/legacy canonical
definitions and institutional governance. Neither actual full Core
integration, Linux Python 3.9/HPC run, hospital IAM, audited concurrent
cluster storage, clinical data, or real EHR acceptance were completed.

[Read S08 API and safe usage](../reference/functions/review_queue.md).

**46-deliverable ledger:** P1-07 is **LOCAL_TEST_PASS** only. Cumulative
**6/46** locally implemented/tested (~13.0%), **40/46 OPEN**
(~87.0%), **0/46** source-scientifically accepted. The prior P1-03
authorized SQL/FHIR institutional integration and full current-head
Core/HPC release gates remain OPEN. The next milestone is **S09:
P1-08 schema-fingerprint-bound reviewed mapping reuse, version/drift
invalidation and held-out unseen-schema evaluation**. Source-scoped
mapping memory must not bypass final full-source and clinician approvals.


## Session S09 — approved-adapter fingerprint memory and unseen-schema abstention (24 October 2026)

New `thomaslab.adaptive.mapping_memory` connects S01 structural metadata, the
S07 deterministic field ranking, S08 three-person review, and the existing
`AdapterRegistry`. The S09 `FingerprintMappingMemory` only stores a
**write-once, review-only hint** when a verified S08 chain ends in
`REVIEWED_FOR_VALIDATION` and the AdapterRegistry revision independently
shows `APPROVED` with named reviewer and passing, complete
`FULL_SOURCE` validation metadata. Both paths must agree on source system,
release, table, ordered source fields, S01 fingerprint and approved
source→canonical assignment. The memory-writing actor must be a fourth
separate verified data steward.

New registry drafts now optionally accept **all three** S09 provenance
fields (`source_release`, `table_name`,
`source_schema_fingerprint_sha256`) together; partial bindings are
rejected. `MappingWorkbench` forwards these fields when the source
manifest includes them. Older unbound registry revisions remain readable
but are **not eligible for S09 memory**.

Lookup requires an externally verified role and exact ruleset/fingerprint,
source/release/table/domain/field match. Different release or schema
produces `BLOCK_SCHEMA_OR_RELEASE_DRIFT`; missing or unfamiliar inputs
abstain. Even a successful lookup is only
`EXACT_MATCH_REVIEW_HINT_ONLY`, with
`automatic_etl_allowed=False`, `authorized_for_export=False`,
`clinical_mapping_reapproved=False`, and
`external_entitlement_rechecked=False`. No source rows, raw patient
values, credentials, or actual OMOP mappings are released.

`evaluate_unseen_schema_holdouts` accepts a bounded set of 1–64
explicitly labeled source-schema cases, reports aggregate exact-match/
abstention confusion counts, and blocks any labeled **false reuse**. The
local four-case synthetic illustration yielded one correct exact hint,
three correct abstentions, zero false reuse. These annotations are
**not** independent clinical gold-standard truth or held-out real
hospital evaluation. An intentionally false label triggered a
`BLOCK_FALSE_REUSE` safety result.

**Local evidence:** **37/37 synthetic S09 tests PASS** on Python
3.13.5/pandas 2.2.3/pytest 9.0.2, with Python 3.9–3.13
grammar parsing PASS. Exact tested new implementation/test Git blobs
matched Core candidate commits; the test environment uses actual S03,
S07 and S08 code plus compatible local surrogates for older S01,
canonical definitions and registry. Full, real Core import/integration,
new registry/provenance propagation regression testing, institutional IAM,
revocation checks, signed audit/WORM storage, Python 3.9 runtime and
HPC/clinical acceptance have **not passed**. A stored mapping hint cannot
be directly consumed by clinical ETL.

[Read the S09 API guide and limits](../reference/functions/mapping_memory.md).

**Ledger:** P1-08 has `LOCAL_TEST_PASS` synthetic evidence only.
**7/46** deliverables locally evidenced (15.2%), **39/46 OPEN**
(84.8%), **0/46** source-scientifically accepted for protected
hospital data. P1-03 enterprise-source authorization/integration and
full current-SHA private Core/HPC acceptance remain OPEN.

**Next milestone S10:** prioritize missing P0 dataset foundation
requirements—versioned canonical EHR tables, patient/encounter/event
semantics, source provenance, and approved release contracts—without
performing unsafe automatic mapping or real-data export.


## Session S10 — canonical patient/encounter/event temporal staging (24 October 2026)

**Implementation:** New `src/thomaslab/adaptive/canonical_dataset.py`
implements the first versioned *Thomas Lab research staging contract*
(`thomaslab-ehr-staging-v1`) for patient, encounter and clinical-event
tables. This is a **bounded, metadata-only diagnostic of
already-authorized in-memory data**, not a raw EHR importer,
pseudonymizer, published patient-level dataset, certified OMOP CDM 5.4
ETL, immutable archive or approved clinical data release.

The `validate_staging_dataset` function requires source system and
release provenance and the three S01 schema fingerprint declarations,
site-scoped lexical IDs with leading zeros, independent person/encounter/
clinical event uniqueness and joins, and distinct event, recorded and
available timestamps with explicit time zones. It does not collapse
orders, dispensings and administrations into one medication exposure.
Time-unavailable observations, numeric-epoch guesses, missing provenance,
cross-patient encounters and inconsistent IDs block. Events outside
encounter boundaries and recorded-before-event entries are retained
only as *aggregate source exception counts requiring reviewer attention*;
no event values or identities are returned. Null visit links are
counted, never imputed. A conservative rule blocks available time
earlier than event or recorded time pending source-specific exceptions.

The structural manifest hash is deterministic on declared contract,
schema columns and caller-supplied S01 fingerprints. It is **not a
cryptographic checksum of clinical record contents** nor proof of
real source schema identity, source completeness, certified
pseudonymization, controlled retention or release provenance.
Real source data and even restricted aggregate counts must remain
inside institutionally approved compute/storage.

**Evidence:** **39/39 focused synthetic local tests PASS** using the
actual new production module and pandas on Python 3.13.5, pandas
2.2.3 and pytest 9.0.2; Python 3.9–3.13 grammar parsing PASS.
Source/test Git blobs were checked against the exact locally
tested files. Full current-head Core test suite, actual Python 3.9
runtime, Slurm HPC, IRB/DUA and hospital staff approval, OMOP CDM 5.4
mapping and clinical dataset release are NOT PASSED.

[Read S10 staging API and temporal rules](../reference/functions/canonical_dataset.md).

**Ledger:** Mark **P0-04 `LOCAL_TEST_PASS` only** for the staged
three-timestamp contract; not independently source-scientifically
accepted. Cumulative **8/46** locally implemented/tested (~17.4%),
**38/46 OPEN** (~82.6%), **0/46** accepted for real patient data.
P0-01 approved use/retention, P0-02 pseudonymous identity/linkage,
P0-03 OMOP target/extension design, P0-05 immutable archive/release,
P0-06 access tiers/audit, and P1-03 enterprise SQL/FHIR IAM remain
OPEN. S10 does not generate files, claim official data availability,
or merge the Core draft PR into main.

**Next milestone S11:** P0-03 OMOP 5.4-aware canonical domain
specification and justified extension manifest, including
vocabulary/clinical concept review gates; in parallel, complete
P1-03 institutional source connector authorization and accepted
exact-SHA Core/HPC QA.


## Session S11 — pinned OHDSI OMOP 5.4.3 target specification and review-only extensions (24 October 2026)

**Version-pinned official scope:** In `configs/omop54_target_contract.json`,
Thomas Lab now contains all **39 official OMOP CDM 5.4.3 tables and 432
fields** from OHDSI's tagged field/table specification (v5.4.3, commit
`746a15e0fb36a95ba6cc0993737f1273bbad92f2`; bundled field catalog
Git blob `7d37aac301f5ddeecf079ec88f37ca5e12c109d1`).
The JSON preserves required fields, datatypes and primary/foreign-key
targets; the loader verifies expected version, completeness, FK
references and exact bundled Git blob, refusing altered snapshots.

**Thomas Lab extensions are *not* OMOP fields.**
`configs/thomaslab_omop54_extensions.json` proposes three *separately
governed sidecars*: `thomaslab.event_provenance`, `thomaslab.event_temporal_availability`
and `thomaslab.pgx_assay_provenance`. They keep source release and row
lineage, the three event/recording/availability clocks, and assay/gene/
allele/genome/guideline provenance without changing OHDSI's field
definition. All three are default-denied for export and require a
qualified reviewer, institutional rights and release policy.

New `thomaslab.adaptive.omop54_contract` provides pinned field-layout
checks, controlled candidate OMOP table suggestions and a
`assemble_omop54_target_blueprint` function which **does not** create a
database or authorize ETL. In particular, medication orders,
dispensing and administrations **abstain** instead of automatically
becoming drug exposures. PGx has explicit clinical measurement/observation
alternatives. No clinical concept or vocabulary release is asserted
as validated.

**Local evidence:** **34/34 focused synthetic Python tests PASS**
(Python 3.13.5, pytest 9.0.2) with exact tested module and test file
matched by Git blob. The official 5.4.3 source CSVs were separately
parsed and validated for **39 tables, 432 fields, zero missing FK table
or referenced field** when the snapshot was created. Local regression
fixtures intentionally synthesize the schema and do not establish
full Core integration. Actual Python 3.9 runtime, complete Core
pytest/quality, Slurm/HPC, official instantiated DDL, OHDSI
Data Quality Dashboard, licensed vocabulary content, source-to-concept
mapping precision, clinical review, approved IRB/DUA and hospital-source
permissions remain **NOT PASSED**. CDM v5.5 now exists; choosing 5.4 is
a documented S11 project scope, not a claim that it is the latest CDM.

[S11 OMOP target and extension API](../reference/functions/omop54_contract.md).

**Ledger:** P0-03 marked `LOCAL_TEST_PASS` **only for this full
version-pinned field-level target specification and proposed
clinical/provenance extension design**. Cumulative **9/46 local
deliverables (~19.6%), 37/46 OPEN (~80.4%), 0/46 independently
accepted** for patient datasets. The S10 temporal staging contract
(P0-04) remains locally tested. P0-01/02/05/06, enterprise-source
P1-03, production ETL and all full Core/HPC/clinical release gates
remain open. Core PR #34 stays a draft without merging to main.

**S12 recommendation:** implement a narrowly scoped P0-05 immutable
archive/release-identity *contract and dry-run validator* first. Require
institutionally approved storage, content hashes and reviewed source-
to-staging-to-OMOP lineage before any real protected-data release.


## Session S12 — deterministic release IDs and immutable-archive preflight (24 October 2026)

**Implementation:** Added `thomaslab.adaptive.release_manifest`, a
**metadata-only / synthetic-byte-only** module tied to the S01 fingerprint,
S10 temporal staging version and S11 OHDSI OMOP 5.4.3 target version.
`build_release_manifest` constructs deterministic SHA-256 release IDs
from source release, controlled classification, the three S01 schema
fingerprints and bounded source → staging → OMOP artifact descriptions.
Each artifact is identified by an opaque ID, declared SHA-256 and byte
length, required parent lineage, source schema and transformation
revision; stage-skipping, orphaned dependencies, duplicate IDs, version
drift and forged approval flags are rejected.

`validate_release_manifest` checks internal manifest identity and
three-stage dependencies. `verify_synthetic_archive_files` optionally
reads only **invented synthetic local** files from an existing private
directory, streaming SHA-256 checks and refusing corrupt, swapped,
oversized or symlinked sources. Protected-source byte inspections are
expressly refused. `inspect_worm_receipt_claims` checks **declared**
object-version/lock mode/digest/retention timestamp references without
claiming signed storage-provider verification. No archive is written,
WORM mode enabled, source data published, patient rows returned or
institutional release authorized. All outputs explicitly block export.

**Evidence:** **45/45 focused synthetic tests PASS** on Python 3.13.5
and pytest 9.0.2, Python 3.9–3.13 syntax/AST parsing PASS. Exact
committed new source/test Git blobs match the locally executed files.
These tests exercise the actual standalone standard-library module,
not mocked external data services. No real protected data, Herts HPC,
actual Python 3.9 runtime, full Core CI/Ruff/packaging, institutional
object-store immutability, signed audit, source use/retention policy,
dataset release or clinician OMOP validation have passed.

[Read S12 release manifest contract and limitations](../reference/functions/release_manifest.md).

**Ledger decision: P0-05 stays OPEN**. S12 is a bounded, locally tested
subcomponent of P0-05, *not the complete requirement*: no independently
enforced immutable archive, institutionally verified retention,
production archive/recovery process, authenticated WORM receipts or
approved release gate exists. Counts therefore remain **9/46 locally
complete against entire tracked task definitions, 37/46 OPEN, 0/46
independently accepted for real patient datasets**.

**Next development S13:** finish the independent P0-05 archive/storage
integration contract *where permitted by the institution*, or prioritize
P0-01 hospital-approved source classification/use/retention and P0-06
authenticated audit/egress controls before attempting any patient-data
workflow. Separately clear open P1-03 SQL/FHIR authorization and
full exact-SHA Core Python 3.9/HPC QA; Core PR #34 stays draft.


## Session S13 — source classification, purpose, retention and institutional grant contracts (24 October 2026)

New `thomaslab.adaptive.source_use_contract.validate_source_use_contract`
defines a strict, version-pinned, metadata-only contract for source
classification, institution/agreement/ethics references, explicit research
purposes, source release and S01 schema identity, allowed environments,
permission expiry, retention end and legal hold. It delegates the decision
to an **externally operated institutional grant verifier**, retains all
existing Core environment and All of Us restrictions, denies unverifiable
or expired scopes, and never grants source access, deletion or row export.
A caller-supplied synthetic `lambda: True` cannot attest a real hospital.
Hospital-issued agreements, independently checked IAM/DUA/IRB grants,
revocation services and retention enforcement remain prerequisites.

[S13 documented API and safety contract](../reference/functions/source_use_contract.md).

## Session S14 — metadata audit, cell-risk and deny-only egress controls (24 October 2026)

New `thomaslab.adaptive.audit_egress` adds a bounded private local
`AuditLedger` with role-verifier-gated event append, O_EXCL file creation,
owner-only record permissions, local SHA-256 hash chaining and exclusive
single-directory writes. This is **not** an institutionally signed,
externally anchored, protected WORM or centrally witnessed audit service.
`preview_disclosure` identifies cell counts below an explicitly
bounded threshold (default 11, **not an NIH/hospital universal rule**);
larger cells still require complementary suppression and repeated-query/
linkage review. `assess_egress` is *always deny-only*, including requests
from apparent stewards and for aggregates. No clinical export path,
network boundary control, institution IAM or independent DUA authorization
has been implemented.

[S14 documented API and limits](../reference/functions/audit_egress.md).

**Combined S13 and S14 evidence:** **66/66 synthetic local tests PASS**
on Python 3.13.5 / pytest 9.0.2, with Python 3.9–3.13 grammar parsing
PASS. The four new GitHub source/test files match the exact executed local
copies. Focused tests exercise the S13/S14 production functions with a
local contract-compatible substitute for Core `ExecutionPolicy` and
governance; this is *not* full exact-commit Core integration or approved
Herts HPC/Python 3.9 runtime.

**Tracker judgment: P0-01 and P0-06 both remain OPEN.** Passing software
preflights cannot establish that a real hospital has approved source use
and retention, independent staff role verification, external audit/WORM
storage, clinical disclosure governance or an egress gateway. P0-05
immutable archives and P1-03 approved SQL/FHIR source connectors remain
OPEN as well. Cumulative **9/46 scoped deliverables locally complete
(19.6%), 37/46 OPEN (80.4%), 0/46 independently accepted for real
patient data**. Core PR #34 remains draft, not merged into `main`.

**Next acceptance priorities:** provision *institution-owned* S13 IAM
verification and signed grant manifests, S14 central audit+egress
enforcement, P0-05 compliant archive receipts, P1-03 source IAM and
actual exact-SHA full Core/HPC acceptance before real hospital data is
used or a dataset is released.


## Session S15 — site-scoped pseudonymous identity safety (25 October 2026)

`thomaslab.adaptive.site_identity` implements bounded **HMAC-SHA-256**
source-identifier pseudonymization using explicit source site, source
system, original ID namespace, entity grain (person/encounter/event) and
site key version. Source IDs remain lexical (leading zeros preserved).
Separate sites, key versions and entity grains yield different derived
tokens even for the same source ID. Weak/nonbytes key material,
noncanonical IDs, unknown grain, missing key provider and oversized
batches fail closed. The batch API returns *only derived pseudonyms*.
Cross-site linkage requests are metadata-only and **always blocked**.

The cryptographic key must come from **institution-managed KMS/HSM or
enclave custody** with independent permissions, key rotation/retention
and full actor/purpose audit. This source-only module **does not**
authenticate the provider callback; outputs mark KMS and institutional
linkage approval as not verified. Pseudonyms remain sensitive patient
data, not an automatic de-identification guarantee. No real IDs were
used in development.

**Focused tests: 39/39 passed** locally on Python 3.13.5, pytest 9.0.2,
with source/test blob hashes matching the exact executed code,
Python 3.9–3.13 grammar and compileall PASS. Full current Core,
approved Herts HPC, institutional custody, IRB/DUA and clinical
reidentification-risk approvals were not tested.

[Read S15 keyed identity guide](../reference/functions/site_identity.md).

**Ledger: P0-02 remains OPEN** until independently approved
pseudonymization/key administration, site linkage design, controlled
data stewardship and hospital acceptance are demonstrated.

## Session S16 — clinical terminology registry, releases and entitlements (25 October 2026)

`thomaslab.adaptive.terminology_registry` implements **metadata-only**
source/release pinning for OHDSI Athena, SNOMED CT, LOINC, RxNorm,
UCUM, UMLS, ICD-10-CM, CPIC and NHS dm+d. A distinct source release
holds declared pack SHA-256, license model/reference, institution,
jurisdiction, allowed purposes and expiry. Registration persists
bounded 0600 JSON metadata records in an existing private 0700
directory, with identity/digest checks and write-once-by-API version
semantics. Lookup rechecks the **external institutional entitlement
verifier**, including a revocation denial path.

The supplied verifier callback is not automatically trusted, and
**declared** pack SHA-256 is not a byte-validated vocabulary source.
No licensed concepts are downloaded, shared, indexed, imported or
mapped to clinical source codes. The existing S11 5.4 target schema
does not imply entitlement to Athena vocabularies.

**Focused tests: 30/30 passed** locally on Python 3.13.5, pytest 9.0.2,
with exact source/test Git-blob matches and Python 3.9–3.13 syntax
and compilation PASS. Actual institutional licensing, original pack
byte checks, full Core/HPC compatibility and clinical mapping have
not passed.

[Read S16 terminology registry guide](../reference/functions/terminology_registry.md).

**Ledger: P2-01 remains OPEN** because source entitlement/legal
evidence and real vocabulary release checks still require independent
institutional service integration.

**Combined S15/S16:** **69/69 focused synthetic tests PASS**;
the two whole 46-item requirements are **not** independently fulfilled.
Cumulative completion stays **9/46 locally completed scoped tasks
(19.6%), 37/46 OPEN, 0/46** accepted for protected hospital data.
P0-01/P0-05/P0-06 and P1-03 institutional security/source gates
remain open; Core PR #34 remains draft.

**Next dependencies:** independent key custodian and permissioned
source crosswalk for P0-02, provider-signed license and SHA-verifiable
vocabulary import for P2-01/P2-02, and full Core/Python 3.9/Slurm
integration on an exact candidate SHA.


## Session S17 — governed full-package Athena terminology import (25 October 2026)

`thomaslab.adaptive.athena_import.import_athena_full_package` imports exactly the nine official Athena full-package TSV vocabulary files into a private, release-specific SQLite review store. It integrates with the **S16 `TerminologyReleaseRegistry`** for exact release/declared SHA-256 verification and rechecked external entitlement, with existing Core `ExecutionPolicy` governed input/output roots and nonexporting institutional/HPC mode. It rejects incompatible delta/CPT4 extra packages, corrupt/unapproved ZIPs, encrypted entries, high decompression ratios, bad UTF-8 and table headers, oversized rows and archives, and ambiguous/corrupt vocabulary concept references. Configurable row, ZIP, decompressed, physical-line, batch and SQLite byte ceilings bound resource use. Imports are staged inside private owner-only folders with no overwrite; failed attempts remove incomplete stores.

The SQLite schema preserves **lexical source vocabulary fields as TEXT**, not native official OMOP datatype constraints; no clinical concept mappings, signed license evidence, public export or DQD claims are made. The source must remain within separately licensed institutional storage. The entire Athena pack SHA is checked against the **declared S16 registry SHA**, which is not proof the publisher or institutional license authority signed that declaration. No actual Athena package was imported during synthetic testing.

[Read S17 full importer API and licensing restrictions](../reference/functions/athena_import.md).

**P2-02 remains OPEN:** production/clinical acceptance requires an actual permitted Athena release, verified issuer package/content hashes and licensing, retained restricted-source storage, large-scale quality testing and full Core/Python 3.9/HPC validation.

## Session S18 — typed source → canonical staging → OMOP dependency graph (25 October 2026)

`thomaslab.adaptive.etl_graph.build_reviewed_etl_graph` creates a deterministic SHA-256 identified **non-executable** graph spanning approved source adapters, the S10 person/encounter/clinical_event staging families, and only official tables from the S11 pinned OHDSI v5.4.3 catalog. It invokes S09's `_approval` to require a verified approved source adapter with complete full-source validation and fingerprint/source-release/table binding, checks each field map against the approved adapter and canonical/OMOP table, and disallows unapproved extra columns or arbitrary executable transform expressions.

Distinct site scopes cannot be mixed. Multi-source staging joins require explicit site-isolated key pairs and review references on each inbound edge. One-to-many and multi-target fan-out require separate review references; no join is actually run, no cross-hospital identity is reconciled and no approval is inferred from these reference strings. Outputs always set `compiled_sql=False`, `transformations_executed=False`, `concept_mapping_validated=False` and `dataset_release_authorized=False`.

[Read S18 typed graph and no-execution boundaries](../reference/functions/etl_graph.md).

**Combined local evidence:** **36/36 synthetic tests PASS**, Python 3.13.5, pytest; test source and both new production module Git blob SHA identities verified against exact executed copies. Tests include invented nine-table ZIP read/write and SQLite query, source entitlement denial, corrupt package rollback, unapproved graph revisions, multi-table source joins, cross-site block and review-only fan-out. The isolated test harness uses synthetic substitutes for **Core governance**, S11 full catalog and S16 registry (and S09's approval contract) rather than the full exact-head Core dependency graph. No official licensed vocabulary pack, real EHR, actual Python 3.9 interpreter, Slurm HPC, full CI/Ruff or scientific/clinical acceptance was tested.

**Tracker:** P3-01 `LOCAL_TEST_PASS` for the complete *bounded metadata-only typed graph* design; accepted remains false. P2-02 stays `OPEN` with S17 local subcomponent evidence. Totals **10/46 local scoped deliverables (21.7%), 36/46 OPEN (78.3%), 0/46 independently source-scientifically accepted**. The separate executable ETL compiler P3-02, join validity P3-03, OMOP record builders P3-04, licensed production sources and source security controls remain OPEN. Core PR #34 stays draft.

**Next gated milestones:** S19/P2-02 licensed full-package acceptance and bounded production vocab quality suite when institutional source access exists; S20/P3-02 allowlisted no-arbitrary-execution transformation compiler and S21/P3-03 protected site/time join contracts, plus exact-SHA Core/Python 3.9/Slurm QA.


## Session S19 — constrained allowlisted ETL intermediate-representation compiler (25 October 2026)

New `src/thomaslab/adaptive/etl_compiler.py` consumes a SHA-256-matching, typed S18 `ETL_GRAPH_REVIEW_ONLY` manifest and a supplied OHDSI CDM 5.4 field-level catalog. It rejects submitted ETL/execution/clinical release claims, requires an explicit external review-verification callback, independently screens node/edge tiers, schema allowlists, duplicate destination assignments, site-scoped join keys, graph completeness, mapping multiplicity and fanout-review references. It emits a deterministic, SHA-256-bound **`COPY_COLUMNS_ONLY` intermediate representation**. This is not SQL, a Python script, a database executor or clinically approved ETL. In particular, no rows are opened or exported, no scripts can be supplied, no OMOP concepts are selected, and callback approval is **not** proof of institutional access/clinical mapping authorization.

## Session S20 — protected site/identity key and point-in-time join specification (25 October 2026)

New `src/thomaslab/adaptive/protected_joins.py` consumes only the S19 nonexecuting IR, checks its exact SHA-256, demands a reviewed join specification for every join edge, enforces explicit same-site `site_id` equality plus a matching pseudonymous person/encounter/event key grain, preserves the key-version/reference and requires an external institutional site-key review callback. Cross-site linkage is denied. A bounded `AS_OF_THREE_CLOCKS` rule binds explicit study index time, event/recorded/available clocks and lookback. Synthetic-only helper `screen_synthetic_asof_clocks` counts chronology violations without releasing dates. No protected source identity is opened, and no join is executed or authorized.

**Evidence:** The combined `tests/test_adaptive_etl_compiler_joins.py` suite passed **34/34 focused synthetic tests** on Python 3.13.5/pytest 9.0.2, and Python 3.9–3.13 AST grammar checks passed. Production source modules and test file SHA-1 Git blobs exactly match committed versions. These are **standalone invented-data tests**, not full current-head Core/OMOP/registry integration, current hospital grant or approved Slurm HPC. Real-world pseudonymization/KMS, clinical time-zero semantics, join cardinality and complete ETL execution tests remain pending. The newly added S18 full AdapterRegistry integration test also remains separately pending an actual Core run.

[S19 compiler documentation](../reference/functions/etl_compiler.md) • [S20 protected join documentation](../reference/functions/protected_joins.md).

**Ledger:** P3-02 `LOCAL_TEST_PASS` only for bounded, allowlisted, non-executable IR compilation; does **not** certify production executable ETL. P3-03 remains `OPEN` with a locally tested **partial** protected-join design because independent site-key and clinical temporal validation are not implemented. New total **11/46 locally completed scoped technical deliverables (23.9%), 35/46 OPEN (76.1%), 0/46 independently accepted for protected hospital data**. No merge to `main`. Existing P0 source/IAM/WORM, P1-03 governed hospital connectors, P2-02 licensed source acceptance and P3-04 clinical record construction remain OPEN.

**Next recommended action:** Run exact-head Core pytest/Ruff and Python 3.9 Slurm/HPC on institution-approved compute, including the unexecuted S18 AdapterRegistry integration test. Then complete protected join service integration/temporal reference verification under P3-03 and standard OMOP core builders with source-to-target reconciliation under P3-04. Never enable real-data execution before identity/IRB/DUA and clinical review gates pass.

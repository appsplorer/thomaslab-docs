# S07 — Ranked, abstaining multi-target EHR field suggestions

**Development state:** implementation and synthetic tests are committed to private
`appsplorer/thomaslab-core` draft PR #34. The current work has **not** passed
full Core CI/HPC integration, expert mapping accuracy tests, or institution-
approved real-hospital source validation.

## Scope and position in the pipeline

`thomaslab.adaptive.field_suggestions.rank_reviewable_field_destinations`
consumes a **completed S01 schema metadata report**, calls the existing
S03 clinical-domain suggestion service, and retrieves field names and aliases
from the already defined `thomaslab.contracts.get_domain_contract` and
`thomaslab.data.CANONICAL_SCHEMA` interfaces.

It never reads raw EHR files, accesses patient rows, assigns OMOP concept IDs,
executes transformations, writes research tables, approves mappings, constructs
patient identity crosswalks or sends metadata to an LLM/remote API.

It provides ranked *possibilities* across more than one specified canonical
domain. A field that could contribute to both a clinical-event and an encounter
context retains **separate domain-qualified alternatives**, not a fabricated
unique one-to-one assignment. These are Thomas Lab canonical staging fields;
OMOP CDM transformations still require a separately reviewed ETL plan.

## API

```python
from thomaslab.adaptive.schema_discovery import discover_source_schema
from thomaslab.adaptive.field_suggestions import rank_reviewable_field_destinations

# Invented synthetic data, in a separately authorized development workspace:
import pandas as pd

metadata = discover_source_schema(
    [pd.DataFrame({
        "subject_id": ["SYNTH001", "SYNTH002"],
        "test_name": ["Synthetic assay", "Synthetic assay"],
        "result_value": ["1", "2"],
        "unit": ["mg/dL", "mg/dL"],
        "charttime": ["2026-01-01", "2026-01-02"],
    })],
    source_system="synthetic_hospital",
    source_release="v1",
    table_name="lab_results",
)

proposals = rank_reviewable_field_destinations(
    metadata,
    domains=("measurement",),
    max_options=5,
)
assert proposals["clinical_mapping_approved"] is False
assert proposals["authorized_for_export"] is False
```

A real caller must generate S01 metadata using the **governed** scanners in
the approved institutional enclave. A hand-built metadata dictionary is
not evidence of source authorization or a clinically trustworthy schema.

Output preserves the S01 structural fingerprint and checks that the declared
field/type metadata rehash consistently. This is an **integrity consistency
check**, not a signed checksum or independent verification of the hospital's
original extract. A false or malicious source may still fabricate internally
consistent metadata.

## Matching and safe abstention

The bounded algorithm uses exact canonical names, **existing curated aliases**
and finally weak lexical similarity for ranking **only**. It does not use
external terminology licenses or clinical embeddings. Heuristic scores of
100 (canonical), 90 (alias), or less than 60 (fuzzy evidence) are
**not probability estimates or calibrated clinical confidence**.

The full review queue contains the original field label, domain/target field,
ranking score, evidence type, risk flags, source-domain context, and an explicit
status. No original clinical value, example note, ID, code or unit measurement
is included.

| Status | Meaning |
|---|---|
| `REVIEW_REQUIRED` | At least one structural suggestion; requires a qualified reviewer |
| `REVIEW_MULTIPLE_DOMAIN_DESTINATIONS` | The same source field has credible domain-qualified alternatives |
| `ABSTAIN_COMPETING_SOURCE_COLUMNS` | Multiple source fields may populate one canonical field |
| `ABSTAIN_COMPETING_TARGET_FIELDS` | Several target fields plausibly compete |
| `ABSTAIN_WEAK_LEXICAL_EVIDENCE` | Only fuzzy string evidence supports a suggestion |
| `ABSTAIN_GENERIC_LABEL_REQUIRES_CONTEXT` | The source name is generic, e.g. `date` |
| `ABSTAIN_DOMAIN_SCOPE_CONFLICT` | Requested domains contradict the stronger structural table suggestion |
| `ABSTAIN_SOURCE_DOMAIN_UNRESOLVED` | S03 domain is uncertain or high-risk |
| `ABSTAIN_NO_SUPPORTED_MATCH` | No useful candidate from the bounded vocabulary |

For *medication orders versus dispensing versus administrations*, S03
distinguishes those source categories, but this canonical staging mapper
**does not conflate them into `medication` drug exposure**. These remain
abstentions until an explicit, reviewed source-specific transformation plan.

Special risk flags require review of protected patient identity crosswalks,
ICD vocabulary/version, drug coding and administration semantics, laboratory
assay and UCUM units, time-zero and event availability, sex versus gender,
and notes/NLP access. No source identifier is a validated OMOP
`person_id` merely because its column is named `patient_id`.

## Limits and interfaces

- At most 256 source fields, eight distinct explicitly requested canonical
  domains, and ten displayed candidates per source.
- **No data values are inspected.** Column labels and aggregate metadata
  may themselves be sensitive; retain outputs inside authorized compute.
- Internal mapping is deterministic, bounded, and caches repeated lexical
  comparisons **only for the duration of one call**.
- The existing legacy `mappings.py` / `MappingWorkbench` / `AdapterRegistry`
  remain unchanged and keep their separately reviewed simple one-to-one
  contracts. This candidate list is **not** directly accepted as an
  `AdapterRegistry` approval or executable many-to-many ETL plan.
- Full human role-aware review, corrections, immutable approvals and
  signed ETL staging are separate **P1-07/P1-08/P3** deliverables.

## Focused evidence

**37/37 synthetic-focused tests passed locally** on Python 3.13.5 with
pandas 2.2.3 and pytest 9.0.2; Python 3.9–3.13 grammar parsing passed.
The exact new implementation/test Git blobs match the locally tested files.

The S03 domain inference module in this isolated test environment matches
the prior GitHub implementation; the S01 metadata producer and legacy Core
contracts/aliases were represented by **test surrogates** based on the
documented contract. Therefore these are *not* complete private-Core
imports/quality tests. The local 253-column/eight-domain synthetic
timing (~0.15 seconds) is exploratory only and does not establish HPC
throughput, scaling or RAM limits on actual hospital data.

```bash
python -m pytest -q tests/test_adaptive_field_suggestions.py
python scripts/ehr_platform_status.py
# On an approved exact-current-sha HPC checkout:
bash scripts/verify_hardening_candidate.sh
```

The roadmap records **P1-06 as LOCALLY TESTED only**, pending full technical
acceptance and clinical/institutional evaluation. See
[staged EHR platform plan](../../guides/ehr-platform-build-plan.md).

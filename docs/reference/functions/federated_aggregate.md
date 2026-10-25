# S33 — Centralized/federated aggregate study design

**Status: synthetic-only research execution-design candidate; P4-08 remains OPEN.**
The module `thomaslab.adaptive.federated_aggregate` does not perform patient-
level harmonisation, cross-hospital identity linkage, hospital data transfer,
clinical study execution or actual dissemination.

## Contract

- `build_synthetic_federation_plan(mode, sites, cohort_sha256, vocabulary_sha256, phenotype_sha256, minimum_cell_count=11)`: creates a **nonexecuting**, SHA-256-bound plan for `CENTRALIZED` or `FEDERATED` architecture. The site list is explicitly bound to declared source-system, source-release and study-release digests. Only labelled `SYNTHETIC` source agreements are supported; All of Us is blocked (actual All of Us patient information must remain under its own Workbench controls). No source movement is authorized for either mode.
- `validate_synthetic_federation_plan(plan)`: rechecks exact canonical shape, plan hash and nonapproval flags.
- `validate_synthetic_site_report(plan, report)`: accepts **only** declared aggregate integer event counts with exact plan/site/release provenance. Rejects site duplicates, unknown fields, row identifiers, small event or nonevent categories, improper complements, shifted/reused source identities and forged suppression or source-classification fields.
- `pool_synthetic_site_reports(plan, reports)`: checks one complete report per declared site and produces pooled *synthetic* counters only, never per-site counters or row data. It does not prove that a person has not been counted at two hospitals.

The minimum cell threshold is at least 11; both the event and its complement
must clear the threshold for **each** site. This is intentionally more
restrictive than many research questions need. **It is not a disclosure
clearance**: overlapping queries, subtraction/differencing, repeated releases,
other published results, governance entitlements and policies for a particular
restricted source remain outside this module. In particular, All of Us
requires its own program-specific output review, not a generic threshold.

A pooled result always returns `safe_to_publish=False` and
`authorized_for_export=False`; external approval mechanisms must be
implemented and audited separately. Disallowed operations remain disallowed
even if the source data are called `synthetic` without verification.

## Example with completely invented counters

~~~python
from thomaslab.adaptive.federated_aggregate import (
    build_synthetic_federation_plan, pool_synthetic_site_reports
)
site_a = dict(site_scope="SyntheticA", source_system="GeneratedA",
              source_release="v1", release_id="1"*64,
              classification="SYNTHETIC")
site_b = dict(site_scope="SyntheticB", source_system="GeneratedB",
              source_release="v1", release_id="2"*64,
              classification="SYNTHETIC")
plan = build_synthetic_federation_plan(
    mode="FEDERATED", sites=[site_a, site_b],
    cohort_sha256="a"*64, vocabulary_sha256="b"*64,
    phenotype_sha256="c"*64,
)
def row(site, release):
    return dict(site_scope=site, release_id=release,
                plan_sha256=plan["plan_sha256"], classification="SYNTHETIC",
                total=30, events=15, nonevents=15, suppressed=False)
report = pool_synthetic_site_reports(plan,
    [row("SyntheticA", "1"*64), row("SyntheticB", "2"*64)])
assert report["events"] == 30
assert report["safe_to_publish"] is False
~~~

## Pending production integration

In an institutionally approved environment, a **different, reviewed** site-local
execution adapter would enforce source-specific IRB/DUA, IAM, network policy,
project authorization, permitted cohort queries and secure storage. The
federation coordinator must validate provenance from independently signed
receipts, correct clinical semantics, patient/site identity and time windows;
apply full disclosure review (including repeated-query accounting and
complementary suppression); audit authorization and site-specific errors;
validate aggregate correctness; and verify that raw data never leave a site in
federated mode. None of those approvals can be inferred from the synthetic
candidate or a structural test. **P4-08 remains OPEN.**

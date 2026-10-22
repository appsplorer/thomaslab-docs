# Engineering roadmap, accountable gates and maintenance

**Status:** living issue/decision log; institutional assignments pending.

| Gate | Proposed accountable role | Evidence expected | Status |
|---|---|---|---|
| IRB/DUA and data use | PI + UGA privacy/IRB | letters and data classifications | NOT_ASSESSED |
| Secure HPC and retention | GACRC/UGA IT + PI | approved ACLs, backups, logging and quotas | NOT_ASSESSED |
| Library governance and IP | PI + technology transfer | written license/ownership decision | NOT_ASSESSED |
| Python QA/CI | Two named maintainers | reproducible green exact-head CI, wheel, scans | PARTIAL |
| 15–20 unseen datasets | analyst + independent domain experts | preregistration, frozen gold, source SHA, results | NOT_RUN |
| Five-person notebooks | independent researchers | full task logs and errors, including 19 legacy | NOT_RUN |
| Clinical/statistical validation | domain specialists | per-method known answers, controls and review | NOT_RUN |
| Public research handover | maintainers | reviewed docs, roles, citation, release notes | PARTIAL |

## Decision log

- 2026-10-21: previous exact-SHA Herts Python 3.9 technical suite PASS; not
  evidence of patient-data approval or external scientific validity.
- 2026-10-22: private Core and public docs kept separate; only sanitized
  explanatory documentation is eligible for public publication.
- 2026-10-22: new safety/HPC/baseline implementation stays a candidate until
  exact-head test evidence and reviewers sign off. Do not silently backdate
  older HPC results to newly changed source.

## Sustainable ownership

The repositories are presently held under a personal account. An institution
must decide transfer, allowed license, stewardship and two named maintainers.
Do not state UGA endorsement or ownership before an authorized written
decision. Record response expectations, support channel, funded maintenance
time, incident contact, backup/restore and offboarding procedures.


## Clinical source audit addendum — 22 October 2026

This checklist records what source review and candidate code inspection
established, rather than treating passing syntax or older HPC tests as
evidence of clinical science validity.

| Audit subject | Evidence / corrective work | Disposition |
|---|---|---|
| All of Us CDR v9 | Official CDR dictionary reviewed; Workbench-only participant-level access retained; OMOP concepts, periods, PPI and wearable/omics metadata utilities | CODE CANDIDATE; real CDR NOT ACCESSED |
| MIMIC-IV v3.1 | Official PhysioNet and schema references; separate hosp/ICU keys, gzip input, shifted times, ICD, eMAR and lab dictionary QA | CODE CANDIDATE; credentialed data NOT ACCESSED |
| Site hospital EHR | Explicit local column/units/time mappings, encounter and longitudinal cohort preflights | CODE CANDIDATE; steward sample NOT PROVIDED |
| Shared data validation | Fixed pandas nullable numeric conversion; tightened mixed text/numeric diagnosis code checks; added versioned coding manifests and small-site holdout guards | TESTS AUTHORED; exact new SHA execution PENDING |
| Public documentation | Source-aware method catalogues, HPC A–Z and conservative method readiness mirrored between private Core and public docs branches | CI/site may pass independently of Core |
| Clinical privacy, governance and rights | All of Us Workbench, PhysioNet DUA and institution-approved hospital enclave are separate from software checks | EXTERNAL AUTHORIZATION NOT ESTABLISHED |
| Scientific verification | Novel cohorts, PGx, causal, NLP and baseline methods require prespecified independent real-source validation | NOT_ESTABLISHED |
| Maintainer workflows | GitHub Actions and branch protection require authorized repo administration | OPEN / NOT VERIFIED |

**Never merge or release this new Core candidate on the basis of the prior
Herts job 2499042.** Require an approved Python 3.11+ clean environment,
the new exact-commit `portable_acceptance.sbatch` report (including
`test_healthcare_quality.py`), and code review. UGA IRB/DUA, ownership,
security and data approval remain separately gated by the PI and institution.


## 22 October 2026 closure record — implementation versus acceptance

The P0 source-specific **code candidates** have been implemented in private
Core PR #34, with mirrored public guidance in docs PR #31:

| Audit finding | Software change | Evidence remaining |
|---|---|---|
| All of Us generic exporter bypass | Generic governed exporter denies every All of Us output; real sources require named source_system and fingerprint-bound adapter identity | Exact-SHA tests; institutional security review |
| All of Us counts 1–20 and derivable values | `adaptive.aou_disclosure` performs in-memory preliminary screening; generic site missingness refuses All of Us releases | Named Workbench-authorized disclosure review over all figures/tables/text, and programme exception where applicable |
| Missing clinical API reference | Nine healthcare module references plus one All of Us disclosure reference, linked on public navigation | Content review of each API contract and reproducible examples |
| Cross-repository documentation drift | Twenty-six publication-safe shared pages registered in Core `check_docs_sync.py`; pinned public commit compared in Core CI | Successful hosted Core gate, manual publishing/PR review |
| Outdated Core private Pages instructions | Both repos now describe public `thomaslab-docs` as sole Pages publisher | Merge approved docs PR and confirm deployed site |
| Source-dependent synthetic fixture restrictions | Synthetic MIMIC/hospital tables allowed locally; real patient records remain inside permitted institutional compute | Re-run synthetic tests at exact commit |

**NOT COMPLETE / not authorizable by a software contributor:**

- Core hosted Actions currently fail without usable job execution steps;
  the exact current PR SHA has **no accepted pytest/coverage/Ruff/mypy/HPC report**.
- No UGA approved enclave, accounts, dataset DUAs, IRB/HRPP determination,
  institutional owner/IP permission or central immutable audit storage has
  been attested.
- No independent real-source All of Us Workbench, MIMIC v3.1 or hospital EHR
  clinical/reference-map validity evaluation is reported.
- The 15–20 unseen-dataset gold-standard study and five independent research
  usability sessions have not been conducted.
- Release signing, lockfile/container digest, hosted runner allocation and
  repository branch protection remain separate open release/administrative gates.

**Release decision:** Do not merge the draft Core PR or describe the new
modules as clinically validated. Passing documentation CI only proves the
public MkDocs build, not the private Python release. The historical
Herts HPC result remains valid *only* for its original commit.


## 22 October 2026 — dataset-contract follow-up audit

The source-specific contract and documentation layer was checked again
against the official All of Us CDR v9 data dictionary and MIMIC-IV v3.1
hospital and ICU table documentation.

| Finding | Software remediation in Core PR #34 | Evidence/limits |
|---|---|---|
| All of Us tier reference ambiguity | Non-executing OMOP SQL planner now only accepts the documented `wb-affable-acorn-7941.R2025Q4R6` or `wb-silky-artichoke-2408.C2025Q4R6` pairing | Workbench IAM authorization, availability and real SQL execution still unverified |
| Participant-level cross-source linkage | Added `source_aware_relationship_integrity`: blocks mixed source family, release, host and approval/steward declaration | Declaration is not an authenticated proof; All of Us exceptions require explicit Programme approval |
| MIMIC lab admissions | Optional child `hadm_id` linkage can be counted with explicit review, without dropping or imputation | Source-specific clinical event timing, missingness and actual patient linkage remain unverified |
| MIMIC hosp and ICU coverage | Added structural candidates for `poe`, `emar_detail`, `services`, `procedureevents`, `datetimeevents`, `ingredientevents` | Not comprehensive data dictionaries; no real release sample tested |
| MIMIC medication workflow | Added `mimic_order_to_emar_linkage_quality` checking pharmacy/admission/patient conflicts and null associations | Orders do not establish administrations; dose, route and adherence NOT_ASSESSED |
| UGA and general HPC | Corrected A-to-Z acceptance documentation to five recorded QA exit statuses | UGA allocations, permitted storage, CPU/GPU/SBATCH runtime still not independently tested |
| Both documentation repos | Mirrored updated source-method references and clinical guide, bound by pinned 26-file synchronization | Draft PRs are not the public `main` release |

**No real-world research data was accessed in this software change.** The
code cannot promise compatibility with arbitrary unknown EHR layouts, label
definitions, vocabulary versions or clinical outcomes. Keep source contracts
at `CANDIDATE` until Dr Thomas supplies approved samples and gold-standard
mappings and a new exact-current-SHA test report passes.

Required acceptance evidence: clean Python 3.11/3.12 and supported HPC
software suite, full pytest/coverage/Ruff/mypy/package/notebook checks,
independent protocol/code review, licensed MIMIC access, All of Us Workbench
authorization, UGA hospital IRB/DUA/IT/storage controls and real external
data-validation cohorts.

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

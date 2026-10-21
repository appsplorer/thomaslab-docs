# Lab platform verification and scientific readiness gates

This repository has three distinct gates:

1. **Software execution:** tests, notebook callbacks, safe paths, packaging,
   documentation and reproducibility for a tested Git SHA.
2. **Dataset validity:** full record scan, schema/units/date semantics,
   approved human mapping, site provenance, drift, privacy and data-use rights.
3. **Scientific method validity:** design and cohort specification, time zero,
   censoring/competing risks, confounding and sensitivity assumptions,
   uncertainty, external validity and independent domain interpretation.

Passing gate 1 never automatically satisfies gates 2 or 3. Synthetic
fixtures demonstrate code integrity rather than clinical generalizability.

`scripts/benchmark_validation_scale.py` provides a reproducible synthetic CSV
throughput and Python-allocation measurement for comparing PyCharm, Kaggle and
HPC environments. The default 100,000-row run is deliberately bounded. It is
**not** evidence of large institutional EHR-scale capacity, external dataset
adaptation, clinical validity or approved patient-data execution.

## Software release decision

`verify_release_report(report, expected_sha=HEAD)` checks that the observed
report matches the exact checkout, records PASS for pytest/Ruff/mypy/docs/
notebooks/build, includes an executed ten-family synthetic adaptation suite,
confirms zero autoapprovals, and preserves clinical-method review as pending.
This verifier consumes evidence; it cannot independently authenticate a
claim of having run CI. Retain raw command logs and a remote GitHub Actions
run for the **remote PR head**, because local and connector-generated commit
SHAs can differ despite identical file blobs.

The verifier returns `SOFTWARE_RELEASE_CANDIDATE` only after all supplied
required suite statuses are PASS. Missing or skipped suites, a stale SHA,
misleading notebook counts, missing scientific axes or an asserted
`publication_ready=true` result in `BLOCK`.

The release report must be generated *after* the candidate Git commit: a
tracked JSON file cannot contain the SHA of the commit that contains that
very file. Store exact-head evidence as a run artifact and in the PR body,
not as self-referential text in the same source commit.

## Researcher deployment decision

| Condition | Software release | Lab pilot on synthetic/public | Institutional patient-level deployment |
| --- | --- | --- | --- |
| Full local checks and matching Git head | Required | Required | Required |
| Public Synthea structural failure | Must disclose | Review mapping | Independent site adapter required |
| 15–20 independent unseen dataset benchmark | Not required for software code | Pending evidence | Required for broad adaptation claims |
| Five researcher task study | Not required for code | Pending evidence | Required before describing self-service as independently usable |
| Approved real dataset mapping and full scan | Not applicable | Only if permitted | Required per dataset/version |
| Signed institution/IRB/DUA and output controls | Not applicable | Follow local terms | Required |
| Scientific publication review | Separate | Not established | Study-specific, never inferred |

**Release as research software** only if all current software gates really
pass at the tested SHA. **Conditional pilot** may use synthetic/public data
while mapping and independent usability evidence is gathered. **Stop** any
institutional rollout lacking the appropriate approvals, credentialed access,
PHI safeguards, or clinical semantics review. A FAILED public benchmark is
not upgraded to PASS to meet a release deadline.

This decision tree is intentionally conservative. The team should re-run
the complete tests and benchmark with its own Python environment in PyCharm
before the first lab-wide user trial.

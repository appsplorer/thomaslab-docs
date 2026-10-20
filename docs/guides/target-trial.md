# Active-comparator new-user and target-trial-style workflows

`thomaslab.target_trial` formalizes observational study design elements so eligibility,
treatment assignment, time zero, follow-up, censoring and outcomes can be reviewed
before estimation.

## Recommended sequence

1. define the target and active comparator using reviewed drug mappings;
2. require a study-defined washout period for both arms;
3. assign treatment from the first qualifying initiation event;
4. align eligibility, assignment and time zero;
5. build ITT-like and, when scientifically justified, as-treated sensitivity follow-up;
6. inspect switching/discontinuation and censoring reasons;
7. run overlap/balance diagnostics from `thomaslab.causal_workflows`;
8. report negative controls only when their rationale and measurement validity are documented.

## Guardrails

- This structure does not create randomization.
- ITT-like means treatment assignment is carried forward observationally; it is not a randomized-trial ITT estimand.
- Censoring at switching or discontinuation can induce selection bias.
- A simple as-treated analysis is not automatically a valid per-protocol effect.
- Grace periods, washout, eligibility, comparators and outcomes must be study-defined.
- Negative controls are not selected automatically and require substantive justification.

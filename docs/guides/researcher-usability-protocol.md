# Thomas Lab independent researcher usability protocol

Status: **NOT_RUN**. No volunteer testing has been represented as complete.

## Participants and environment

- Recruit five independent researchers who are not the implementation author;
  include those without Python/YAML experience.
- Obtain appropriate local training and data-use approvals **before** any
  private institutional dataset is used. Use a deliberately synthetic cohort
  for the first round, on an approved local Jupyter/PyCharm kernel.
- Record exact package Git SHA, Python/Jupyter/ipywidgets versions, OS,
  configuration, dataset fingerprint (not its records), and participant role.
  Do not publish identities or patient-level values in feedback logs.

## Exercises (each researcher, no editing Python or YAML)

1. Launch notebook 07, inspect a new unfamiliar synthetic CSV, review
   suggested and alternative mappings, and identify at least one ambiguous
   field that must not be autoapproved.
2. Review a mapping with named simulation credentials; run full-source
   validation on a dataset containing a bad value beyond row 5,000.
   Expected result: blocked until source or contract is corrected.
3. Record a new adapter version; verify same-version overwrites and
   unreviewed approval are rejected; compare a changed source schema.
4. Choose a guided descriptive or binary-analysis form, run only synthetic
   data and identify which of software/data/method evidence is incomplete.
5. Attempt unsupported analysis, unreviewed patient-level export and
   institutional data execution on Kaggle. Each must stop and explain why.
6. Export an approved synthetic aggregate via the governed workflow and
   inspect the redacted audit trail. Confirm patient-level values are absent.

## Measures and release decision

Record task completion, wrong decisions, number of researcher actions,
elapsed time, help requests, failed/puzzling messages and anonymous comments.
Target a high independent completion rate with no unapproved action,
no privacy exposure, no silent schema overwrite and no false publication-
readiness status. Any data loss or unauthorized exposure is a STOP.

The automated `notebook-acceptance.json` file is distinct from this study:
40 converted notebooks have synthetic callbacks that run automatically;
the first 19 legacy widgets are recorded as **LEGACY_WIDGET_REGISTERED_ONLY**
until individually exercised in an appropriate live user study. This is
interface evidence, not proof that all 59 scientific designs are validated.

| Participant | Start | Completed tasks | Unapproved-action count | Result |
| --- | --- | --- | --- | --- |
| R1 | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| R2 | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| R3 | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| R4 | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| R5 | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |

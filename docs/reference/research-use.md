# Research-use & validation

## Not clinical decision support

`thomaslab-core` is designed for reproducible research workflows. It has not undergone regulatory validation as a medical device and should not produce autonomous clinical decisions.

## Validation expectations

Before using a function in a manuscript or prospective study:

1. Confirm variable semantics and units.
2. Validate coding-system mappings against an authoritative vocabulary release.
3. Write unit tests against known clinical examples.
4. Perform chart review for computable phenotypes when feasible.
5. Quantify missingness and mapping failures.
6. Validate temporal logic on manually inspected patient timelines.
7. Reproduce key estimates independently before publication freeze.

## Privacy and security

Do not commit PHI, credentials, database extracts, free-text notes, genomic identifiers, or patient-level intermediate artifacts to the repository. Use institution-approved storage, secrets management, and access controls.

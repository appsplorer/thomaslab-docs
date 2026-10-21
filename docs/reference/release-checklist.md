# v1 release checklist

A stable thomaslab-core release is ready only when all of the following are true.

1. Package version, `thomaslab.__version__`, README release heading, and compatibility baseline agree.
2. `api_compatibility.yaml` exactly matches the intended public-module surface.
3. `deprecations.yaml` is valid and every planned removal has a migration path.
4. Contracts, configs, schemas, and notebooks parse successfully.
5. Public package modules import in the release CI environment.
6. Wheel and source distributions build successfully.
7. The v1 self-service reference notebook executes successfully.
8. Python 3.9 runtime and static compatibility checks pass for the exact tested SHA; Python 3.10/3.11 checks are separately verified where applicable.
9. The complete pytest suite and coverage/public-callable execution audits pass.
10. `python scripts/local_quality_gate.py` passes on a clean checkout bound to an exact Git commit.
11. Strict MkDocs documentation builds successfully.
12. The tested candidate tree is identical to the tree promoted to main; merge ancestry may differ, but file-tree content must not.
13. Research-use, privacy, causal-identification, and clinical-interpretation limitations remain explicit.

A green checklist establishes software-release readiness. It does not certify a study design, dataset, model, or clinical use.

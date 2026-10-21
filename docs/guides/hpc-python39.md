# Python 3.9 and Slurm: Thomas Lab HPC validation

**Current canonical procedure for Python 3.9 development validation.** This page supersedes the older `slurm/python39_validation.sbatch`, `THOMASLAB_INSTALL`, and shared-environment instructions. The unmerged private Core development branch declares **Python 3.9+** support, while `thomaslab-core/main` still requires **Python 3.10+**; the current *integrated Herts CPU runner* specifically requires **Python 3.9** in an isolated environment.

!!! warning "Not a clinical or release approval"
    Technical validation runs against synthetic/test fixtures and only separately authorized public source profiles. No data-use permissions, institutional accounts, validated external clinical mappings, independent researcher task trials or manuscript-level scientific validity follow from a Slurm PASS.

## 1. Prepare an authorized private checkout

The public handbook does not contain executable Core source. An authorized collaborator can use an approved SSH credential to access the private repository:

```bash
git clone git@github.com:appsplorer/thomaslab-core.git
cd thomaslab-core
git switch audit/kaggle-hpc-final-20261021
git pull --ff-only
git rev-parse HEAD
git status --short
```

This is an **unmerged development branch** in the October 2026 evidence snapshot. Do not interpret its documentation as a stable release from `main`. Existing collaborators should use their approved checkout; avoid multiple unaudited copies of clinical code.

## 2. Create a clean Python 3.9 environment

Do not install packages during Slurm compute jobs, and do **not** modify the shared institutional `research_env`. Use an institution-approved preparation/login environment with package-index access and adequate storage:

```bash
# Replace with your institution-approved, private research workspace.
export THOMASLAB_HPC_ROOT="/path/to/approved/thomaslab_hpc"
export THOMASLAB_PREP_FULL=1

# If the approved base Python 3.9 is not /usr/bin/python3.9:
# export THOMASLAB_BASE_PYTHON39="/path/to/python3.9"

bash scripts/hpc_prepare_python39_env.sh
```

The preparation script creates a private `thomaslab-core-cpu` virtual environment, installs constrained `dev`, `notebooks`, `docs` and model dependencies, and runs `pip check`. Its Python 3.9 constraints file is **not** an exact lockfile. Capturing the approved wheel source, Python ABI and dependency freeze remains necessary.

```bash
export THOMASLAB_VENV="$THOMASLAB_HPC_ROOT/environments/python39/thomaslab-core-cpu"
export THOMASLAB_PYTHON39="$THOMASLAB_VENV/bin/python"

unset PYTHONPATH PYTHONHOME
export PYTHONNOUSERSITE=1

"$THOMASLAB_PYTHON39" scripts/hpc_environment_gate.py \
  --expected-venv "$THOMASLAB_VENV" --full
"$THOMASLAB_PYTHON39" -m pip check
"$THOMASLAB_PYTHON39" scripts/python39_compat.py
"$THOMASLAB_PYTHON39" -m ruff check src/thomaslab tests scripts
"$THOMASLAB_PYTHON39" scripts/mypy_environment_safe.py \
  src/thomaslab --show-error-codes --no-error-summary
```

The environment gate fails closed if the interpreter is not 3.9, the environment inherits system packages, the resolved venv differs from the approved path, `lifelines`, `types-PyYAML` or other required distributions are missing, or `pip check` reports conflicts.

## 3. Run focused tests using an authorized CPU allocation

Use your site's actual account, partition and limits; `eng` and `core256` below are **examples from prior authorized Herts runs**, not guarantees of entitlement at another institution.

```bash
srun --account=eng --partition=core256 \
  --cpus-per-task=4 --mem=12G --time=00:45:00 \
  --export=ALL \
  "$THOMASLAB_PYTHON39" -m pytest -q \
  tests/test_adaptive_templates.py \
  tests/test_adaptive_full_validation.py \
  tests/test_adaptive_mapping_workbench.py \
  tests/test_adaptive_validation.py \
  tests/test_notebook_catalog.py \
  tests/test_adaptive_public_benchmark.py \
  tests/test_models.py \
  tests/test_expansion_data.py \
  tests/test_pgx.py \
  tests/test_transportability_v24.py
```

The focused suite covers synthetic governance, PGx, causal transport and notebook controls. A passing focused test run is **not** a full function-by-function acceptance report.

## 4. Run the integrated CPU technical gate

Only after local preflight and focused tests pass:

```bash
export THOMASLAB_EXPECTED_SHA="$(git rev-parse HEAD)"
export THOMASLAB_FULL=1
export THOMASLAB_REPAIR_MISLABELED=0

sbatch --account=eng --partition=core256 \
  --cpus-per-task=16 --mem=48G --time=08:00:00 \
  --export=ALL slurm/thomaslab_integrated_cpu.sbatch
```

The runner verifies a clean tracked checkout and exact source SHA, Python 3.9 compatibility, dependency health, source-package origin, targeted and full pytest, coverage, recursive import audit, synthetic adaptation and scale benchmarks, Ruff/mypy/packaging/notebook quality, and approval-aware public-source integrity/profiling.

It writes a **separate, restricted-access report per job** under:

```text
$THOMASLAB_HPC_ROOT/benchmarks/integrated_acceptance/<job-id>-<timestamp>/
```

Read `summary.txt`, `phases.tsv`, `module-import.json`, `coverage.json`, `per-function-coverage.json`, and failure logs. The strict callable ledger requires an executed body line for each declared named Python function or class method—including private and nested declarations. Coverage observation cannot prove every branch, mathematical model or clinical interpretation.

```bash
squeue -j "$JOB_ID"
sacct -j "$JOB_ID" -X \
  --format=JobID,JobName%25,State%18,ExitCode,Elapsed

REPORT=$(find "$THOMASLAB_HPC_ROOT/benchmarks/integrated_acceptance" \
  -mindepth 1 -maxdepth 1 -type d -name "${JOB_ID}-*" \
  -print | sort | tail -1)

if [ -n "$REPORT" ]; then
  cat "$REPORT/summary.txt"
  cat "$REPORT/phases.tsv"
fi
```

Set `JOB_ID` to the actual batch job number printed by `sbatch`. A job being submitted or allocated is **not** evidence it completed, and a Slurm `COMPLETED` state is not a substitute for inspecting each acceptance phase.

## 5. Last verified checkpoint and pending gates

At the recorded 21 October 2026 development checkpoint:

| Evidence | Observed outcome |
| --- | --- |
| Herts job `2498939` on Core SHA `1ff0a055c43db0c5023b03a953cb92b08fb847ad` | Full pytest, quality gates, and 106/106 module imports **PASS** |
| Same job, strict function-ledger phase | **FAIL:** 940/955 function/method bodies observed; 15 unobserved |
| Subsequent focused tests at Core SHA `469c120a81bdf5957911550dea4075fbf577ab61`, job `2499039` | **PASS** for executed targeted test modules |
| Subsequent integrated job `2499042` | **Submitted** in supplied evidence; its final status and callable ledger were not provided |
| Scientific reviewer-approved external mappings | **NOT_ASSESSED / NOT_RUN** |
| Independent broad unseen-source benchmarks and five-researcher usability evaluation | **Not established** |

**Do not merge or claim technical release acceptance from a previous SHA.** The public documents and MkDocs build are independent of the private Core PR stack; private Core CI and scientific validity still need separate evidence.

For details on Kaggle source identity, license reviews and historic individual tests, read [Kaggle/HPC acceptance evidence](kaggle-hpc-acceptance.md). For software-versus-science decisions, see [lab validation gates](lab-validation-release-criteria.md).

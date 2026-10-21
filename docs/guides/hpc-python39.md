# Python 3.9 on an institutional HPC cluster

!!! warning "Compatibility candidate, not yet an institutional deployment approval"
    The private `thomaslab-core` Python 3.9 work lives in the Python 3.9 compatibility feature branch. Packaging, dependency constraints and static checks are implemented, but runtime support remains **PENDING** until the exact commit passes a clean Python 3.9 HPC job, full scientific regression gate and packaging checks. No patient-level permissions are granted by these instructions.

This procedure runs a private, **CPU-only Slurm validation job** against synthetic tests and public-independent code contracts. It leaves the HPC system Python and global scientific modules unchanged. It does not require Streamlit or a web server.

## 1. Prepare a source checkout

Check which Python 3.9 environment the cluster actually provides. Module labels vary across institutions.

```bash
module avail python 2>&1 || true
command -v python3.9
python3.9 --version
```

If `python3.9` is unavailable, ask HPC support for an approved Python 3.9 module or isolated virtual environment. Do **not** replace system Python.

Use authorized credentials to clone the private code and switch to the Python 3.9 development branch:

```bash
git clone git@github.com:appsplorer/thomaslab-core.git
cd thomaslab-core
git fetch origin
git switch feature/hpc-python39-compat-20261021
git pull --ff-only
git status --short
git rev-parse HEAD
```

The public documentation repository is *not* a substitute for the private Python package.

## 2. Submit an isolated Slurm verification job

From the repository root:

```bash
export THOMASLAB_EXPECTED_SHA="$(git rev-parse HEAD)"
export THOMASLAB_INSTALL=1
export THOMASLAB_FULL=0

sbatch --partition=core32 --cpus-per-task=8 --mem=32G --time=06:00:00 \
  slurm/python39_validation.sbatch
```

Supply any required site account or QoS with the `sbatch` command. If `core32` is unavailable, choose a site-authorized CPU partition. Do not request GPUs for these checks. Jobs running on a restricted cluster may need a pre-provisioned wheelhouse because compute nodes often have no internet access. In that case, install compatible wheels on an authorized build/login environment and submit with `THOMASLAB_INSTALL=0` and `THOMASLAB_VENV` pointing to the approved prepared Python 3.9 environment.

The validation entry point enforces Python 3.9, a clean tracked Git checkout, optional exact SHA matching, compatible package constraints, a dependency check, a syntax/API scan, environment preflight, targeted PGx/survival/IPCW scientific regressions, and the existing quick quality gate. It also runs the ten-family fabricated adaptation matrix and a **100,000-row full-source synthetic validation benchmark**, with optional `THOMASLAB_SCALE_ROWS` between 1,000 and 1,000,000. These benchmarks do **not** establish performance or scientific validity for hospital datasets. It uses an isolated `.venv-python39` by default.

## 3. Review and preserve evidence

The Slurm stdout is written to `slurm-thomaslab-py39-<job-id>.out`. Per-run results are written under `hpc_validation/<job-id>-<UTC-time>/` with restrictive directory permissions. Review `summary.txt`, `pip-freeze.txt`, `pip-check.log`, `python39-static.json`, `targeted-junit.xml`, `targeted.log`, and `quick-gate.log`, plus `synthetic-ten-family.json` and `synthetic-scale.json`.

```bash
squeue -u "$USER"
ls -lt hpc_validation/
```

The evidence must record the exact SHA and Python/dependency versions. A structural `python39-static.json: PASS` is **not** the same as a passing installed-and-executed Python 3.9 test suite.

If the quick gate passes and a site-approved CPU PyTorch build is available, run a new job with `THOMASLAB_FULL=1`. The full gate additionally checks stable notebook replay, wheel/sdist installation, dependency consistency, and strict documentation build. **Do not lower the 84% coverage floor** to force success. A full run can be time/memory-intensive, so request suitable CPU resources.

## 4. Scientific and data-use boundaries

The HPC process checks only synthetic/public-safe tests until lab and institution approvals are documented. Patient EHR, claims, notes, pharmacogenomic and other restricted data require an approved HPC project area, authorization, institutional account/ACL controls, applicable IRB/DUA, defined data classifications, and independent scientific method review. `ExecutionPolicy(environment="hpc", ...)` does not provide any of those permissions itself.

The synthetic ten-family suite is not 15–20 independent unseen datasets. The older public Synthea adaptation result was a mapping recall of 0.75 against an 0.80 gate (**FAIL**). Five independent nontechnical researcher sessions and publication-level clinical validation remain **NOT_RUN / NOT_VERIFIED**.

## 5. Dependency limitations

Use `constraints/python39.txt` to bound numerical/ABI-sensitive dependencies when resolving the Python 3.9 environment. It is a compatibility constraint file, **not** an exact wheel lock or an assurance of HPC-specific binary compatibility. Record full `pip freeze`, `pip check`, Python ABI, SLURM allocation and package import errors.

Installing PyTorch, CUDA, and specialty NLP/LLM packages is optional for the initial source/numerical checks; the full historical release gate requires CPU PyTorch. GPU jobs should be tested separately on the institution's permitted GPU partitions, with verified drivers and CUDA runtime. Unsupported tasks must fail clearly, never silently substitute estimators.

Before merging the private feature branch, require real Python 3.9 **and** Python 3.10/3.11 checks, 84% coverage, a source/docs consistency review, and independent lab approvals. Never confuse a published MkDocs site with verified research software.

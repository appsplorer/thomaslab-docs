# S32 — Governed CPU/GPU HPC compatibility contract

**Status: local synthetic technical candidate; P4-07 remains OPEN.** This module
creates deterministic proposed acceptance matrices and checks bounded,
**caller-reported** runtime probes. It never submits Slurm jobs, approves
partitions, copies research datasets, runs real patient data, or attests
scientific validity.

## API

`thomaslab.adaptive.hpc_acceptance_contract` provides:

- `build_hpc_candidate_plan(commit_sha, profiles, approved_partitions, require_python39=True)`: SHA-1-formatted **Git commit identity** (40 lowercase hex; this does not mean SHA-1 content is a clinical integrity check), bounded CPU/GPU profile resource requests, exact partition allowlist and Python 3.9-compatible testing requirements. The supplied partition allowlist is *not* institutional approval.
- `validate_hpc_candidate_plan(plan)`: canonical SHA-256 plan identity and rejection of any mutated/forged acceptance flags.
- `audit_synthetic_runtime_probe(...)`: bounded metadata-only consistency checks for a selected profile; a returned `REPORTED_PROBE_REVIEW_REQUIRED` is not an independently verified job result.

The private source repository also contains:

- `slurm/ehr_candidate_acceptance.sbatch`: a noninteractive exact-Git-commit Slurm launcher. In CPU mode it invokes the existing **five-phase exact-commit quality runner**; in GPU mode it launches only the small CUDA preflight.
- `scripts/ehr_gpu_preflight.py`: checks that a GPU allocation and compatible torch/CUDA runtime are genuinely present and executes a tiny invented-matrix arithmetic check. It uses no model downloads or patient files. A result is only a *GPU environment smoke check*, never proof of healthcare/clinical method validity.

## Suggested future execution (not run during development)

Before submitting anything, verify institutional partition, QoS, job limit,
Python version, torch/CUDA compatibility, owned reporting directory, storage
restrictions and research data permissions independently. The following is an
**example only**, not an instruction to bypass cluster site policy.

~~~bash
# From the actual approved and clean Core candidate checkout:
export THOMASLAB_CODE_ROOT="$PWD"
export THOMASLAB_EXPECTED_SHA="$(git rev-parse HEAD)"
export THOMASLAB_PYTHON="$(command -v python)"
export THOMASLAB_QA_REPORT_ROOT="$THOMASLAB_HPC_ROOT/benchmarks/hardening_qa"
# Prepare an approved 0700 report root using normal institution permissions.
export THOMASLAB_HPC_MODE=CPU
sbatch --partition=core256 --cpus-per-task=8 --mem=32G --time=08:00:00 \
 --export=THOMASLAB_CODE_ROOT,THOMASLAB_EXPECTED_SHA,THOMASLAB_PYTHON,THOMASLAB_QA_REPORT_ROOT,THOMASLAB_HPC_MODE \
 slurm/ehr_candidate_acceptance.sbatch

# After separately confirming the GPU partition, CUDA toolkit and Python env:
export THOMASLAB_HPC_MODE=GPU
sbatch --partition=gpu-interactive --gres=gpu:1 --cpus-per-task=8 \
 --mem=32G --time=12:00:00 \
 --export=THOMASLAB_CODE_ROOT,THOMASLAB_EXPECTED_SHA,THOMASLAB_PYTHON,THOMASLAB_QA_REPORT_ROOT,THOMASLAB_HPC_MODE \
 slurm/ehr_candidate_acceptance.sbatch
~~~

Partition names above are examples from prior Herts HPC use; do not assume they
exist or are allowed at UGA or on another cluster. Slurm directives/CLI rules
are site-dependent and must be approved by administrators.

## Local acceptance evidence and explicit gaps

- Candidate source, focused negative tests, nonexecuting Slurm template and GPU
  preflight included on the development branch. Python 3.9–3.13 AST grammar
  parsing and Bash syntax checks are separate from actual Python 3.9 execution.
- Local focused tests only assess deterministic metadata validation. A GPU
  allocation was **not requested or tested**, and a complete exact-HEAD Core
  suite was **not run**.
- Independent QA must still verify commit provenance, package origin,
  python39 runtime, dependency resolution, full pytest/coverage, Ruff/mypy,
  notebooks, wheel, supply-chain checks, current Slurm partition entitlements,
  actual CPU/GPU results and private report retention. **P4-07 stays OPEN.**

This module does not accept All of Us, MIMIC, hospital source records or
institutional permissions as arguments. No patient data may be used to
validate a candidate simply by declaring it synthetic.

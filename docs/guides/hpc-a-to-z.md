# HPC from zero to first Thomas Lab analysis

**Audience:** new researchers, pharmacists, clinicians and data scientists.
**Status:** operational setup instructions; **not** institutional authorization or
proof of any particular account's access. The package is research software only.

## 0. Before you log in

Ask your PI and research computing administrator to confirm your **named**
account, group, CPU/GPU partitions, storage quota, software installation rules,
data classification, allowed destination, DUA/IRB as appropriate, audit storage
and approved transfer procedure. Never upload UGA patient data to Kaggle,
personal GitHub, public notebooks or unapproved cloud services. The governed
notebook interface treats Kaggle as **SYNTHETIC ONLY**. Public/licensed data may
be evaluated on approved institutional/local compute, with source terms checked.

Keep one code checkout, one private environment, one approved data root,
and one restricted results/audit root. No credentials, notebooks with outputs,
or patient rows in Git commits or job logs.

## 1. Connect to UGA's Sapelo2

UGA GACRC's published instructions identify **Sapelo2** at
`sapelo2.gacrc.uga.edu` and require MyID and Duo. Check the current campus
network/VPN instructions before connecting from off campus.

~~~powershell
# Windows PowerShell, once your UGA account is provisioned
ssh YOUR_MYID@sapelo2.gacrc.uga.edu
~~~

Transfer permitted files through the dedicated **xfer.gacrc.uga.edu** transfer
nodes, not job login nodes. For example, with an administrator-approved path:

~~~powershell
scp .\approved_synthetic_example.csv YOUR_MYID@xfer.gacrc.uga.edu:/project/APPROVED_GROUP/YOUR_MYID/
~~~

Do not assume the example path exists. On first access, confirm with GACRC
whether `/project`, `/work` or `/scratch` is appropriate and whether scratch
will be purged. Do not move restricted data until formal approval is complete.

Official references:
[Connecting](https://wiki.gacrc.uga.edu/wiki/Connecting),
[Transferring files](https://wiki.gacrc.uga.edu/wiki/Transferring_Files),
[Job submissions](https://wiki.gacrc.uga.edu/wiki/Job_Submission_partitions_on_Sapelo2).

## 2. Inspect resources without running scientific work on the login node

~~~bash
sinfo
squeue -u "$USER"
module avail python
~~~

The published examples use `batch` for CPU, `gpu_p` for GPU and
`inter_p` for interactive sessions. **Check live `sinfo` and local policy**,
not an old hard-coded partition name. Never run large analysis, build containers,
train models or install heavy dependencies on a login node.

## 3. Choose private code and environment locations

~~~bash
# Replace this with a real institutional allocation approved by your PI/IT.
export THOMASLAB_WORK_ROOT=/project/APPROVED_GROUP/YOUR_MYID/thomaslab
mkdir -p "$THOMASLAB_WORK_ROOT"/{code,envs,results,audit}
chmod 700 "$THOMASLAB_WORK_ROOT"/{envs,results,audit}

cd "$THOMASLAB_WORK_ROOT/code"
git clone git@github.com:appsplorer/thomaslab-core.git
cd thomaslab-core
git switch main
git pull --ff-only
git rev-parse HEAD
git status --short
~~~

Use an approved SSH key; private repository access is separate from your GACRC
account. The public docs repository does not contain runnable Core source.

## 4. Prepare an isolated Python environment

The historical exact-SHA Herts HPC acceptance used Python 3.9.25, **now EOL**.
New environments should prefer a GACRC-supported **Python 3.11 or newer**
and must validate the resolved scientific binaries. Current package metadata
temporarily permits 3.9 for legacy reproducibility; it is **not** a secure
long-term deployment target. Use a permitted prep/interactive compute session
rather than a busy login node for package builds.

~~~bash
module avail python
# Use a versioned Python module approved for this allocation.
# Example after selecting your actual module:
# module load Python/3.11.x
python3 --version

python3 -m venv "$THOMASLAB_WORK_ROOT/envs/core"
export THOMASLAB_PYTHON="$THOMASLAB_WORK_ROOT/envs/core/bin/python"
"$THOMASLAB_PYTHON" -m pip install --upgrade pip
"$THOMASLAB_PYTHON" -m pip install -e '.[dev,notebooks]'
"$THOMASLAB_PYTHON" -m pip check
~~~

This is a convenience **candidate** environment, not a hash-locked release.
Record `pip freeze`, the Python version, OS/CUDA/driver, wheel source and Git
SHA in restricted research evidence. Model/GPU dependencies must be provisioned
with administrator-approved binaries and CUDA compatibility; do not install
random wheel versions into the institution's shared Python environment.

## 5. CPU Slurm: first synthetic quality job

~~~bash
cd "$THOMASLAB_WORK_ROOT/code/thomaslab-core"
export THOMASLAB_CODE_ROOT="$PWD"
export THOMASLAB_PYTHON="$THOMASLAB_WORK_ROOT/envs/core/bin/python"

# No patient data: these are focused synthetic/unit checks.
sbatch --partition=batch --cpus-per-task=8 --mem=24G --time=02:00:00 \
  --export=ALL slurm/portable_cpu.sbatch

# Custom permitted Python workload, with explicit script and arguments:
# sbatch --partition=batch --export=ALL slurm/portable_cpu.sbatch \
#   scripts/benchmark_validation_scale.py --rows 100000
~~~

`slurm/portable_cpu.sbatch` verifies the Python interpreter, records safe
software metadata and executes synthetic tests by default. It does not download
datasets or install dependencies during compute allocations.

## 6. GPU Slurm: confirm allocation *before* any LLM job

~~~bash
# First install an approved CUDA-capable PyTorch in a private GPU environment.
# Use your GACRC-approved CUDA/PyTorch combination; CPU wheels are NOT enough.
export THOMASLAB_PYTHON=/approved/absolute/path/to/gpu-venv/bin/python
sbatch --partition=gpu_p --gres=gpu:1 --cpus-per-task=8 --mem=32G \
  --time=02:00:00 --export=ALL slurm/portable_gpu.sbatch

# Once the synthetic GPU preflight passes, pass a reviewed training script:
# sbatch ... slurm/portable_gpu.sbatch scripts/approved_gpu_experiment.py ...
~~~

The default GPU job runs a **two-by-two synthetic matrix calculation** and
checks `torch.cuda.is_available()`. It does not claim full Torch, CUDA, LLM,
PGx or scientific acceptance. On other clusters override `--partition`,
`--gres`, `--account`, resource/time limits and module loading as permitted.

## 7. Arrays, logs and job troubleshooting

~~~bash
# Default array just checks four synthetic execution environments.
sbatch --array=0-3%2 --partition=batch --export=ALL \
  slurm/portable_array.sbatch

squeue -u "$USER"
sacct -j JOB_ID -X --format=JobID,State,ExitCode,Elapsed,AllocCPUS
scancel JOB_ID
~~~

Inspect `thomaslab-cpu-JOB_ID.out`, `thomaslab-gpu-JOB_ID.out` or the
array's `%A_%a` output. A `COMPLETED` Slurm state is not a passing experiment:
review the recorded test evidence and exact source SHA. Do not emit records,
paths containing secrets, bearer tokens or raw clinical errors to shared logs.

Use `scontrol show job JOB_ID` and the institution's job accounting procedures
for pending reasons, memory/time failures, and allocation limits. Never simply
increase resource requests without first inspecting the failure.

## 8. Apptainer/Singularity candidate and locked-release discipline

`containers/THOMASLAB_CPU.def` is an **illustrative CPU candidate**, not
a validated or dependency-locked image. Build on authorized compute/CI
infrastructure from a **clean, sanitized Git archive**, never from a workspace
containing untracked clinical data. Obtain an approved base image digest,
frozen wheel hashes, vulnerability review and immutable image checksum.

~~~bash
# Only after admin approval; create a clean source-only build context.
# Do not use a working directory containing untracked datasets or secrets.
cd "$THOMASLAB_CODE_ROOT"
python scripts/check_repository_hygiene.py
mkdir -p "$THOMASLAB_WORK_ROOT/build-context"
git archive --format=tar HEAD | tar -xf - -C "$THOMASLAB_WORK_ROOT/build-context"
cd "$THOMASLAB_WORK_ROOT/build-context"

# Run on an institution-authorized build allocation, never a busy login node:
apptainer build thomaslab-cpu.sif containers/THOMASLAB_CPU.def
sha256sum thomaslab-cpu.sif
# In a permitted Slurm CPU allocation:
apptainer exec thomaslab-cpu.sif python scripts/hpc_environment_probe.py
~~~

UGA supports Apptainer/Singularity-style HPC containers; verify the actual
runtime and image-building policy first. A GPU container must be independently
validated and run with `--nv` where the site permits it.

## 9. Preparing for Dr Thomas's sample datasets

Request **only a lawful, approved dataset transfer** from the PI. For each
source, have an authorized steward document:
- source institution, dataset identifier/version, grain and row identity;
- classification and DUA/IRB/HRPP decision, permitted uses and retention;
- code systems, units, timestamps/time zone, de-identification determination;
- allowed storage, compute, readers, audit, egress and publishing policy;
- predefined mapping gold standard, analysis design, outcomes, baselines,
  leakage checks, thresholds and independent review;
- SHA-256 source fingerprint and approved adapter revision.

Start with **synthetic or suitably authorized de-identified** sources. The
software can validate structure and run approved controls but cannot grant
data rights, verify hidden clinical semantics or certify publications.

## 10. Handover evidence and stop conditions

Preserve exact Git SHA, package lock/constraint resolver, CPU/GPU description,
Slurm job IDs, raw redacted logs, tests, benchmark config, data fingerprint,
reviewer approvals and failure/stop decisions in institution-approved storage.
Do **not** begin real-data analysis when access/DUA/IRB, clinical semantics,
mapping review, identity permissions or export controls remain unknown.

This guide is a reusable template for other Slurm systems; **not** an assertion
that any named user already has UGA GACRC access.

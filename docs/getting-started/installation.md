# Installation

The **research code** is maintained in the private `appsplorer/thomaslab-core` repository. This public documentation site is a separate, static MkDocs project. Access to the core repository requires authorization; publishing or building this handbook does not provide source-code or patient-data access.

## Supported Python versions

The **unmerged Core development branch** declares **Python 3.9 or newer** (`requires-python = ">=3.9"`) and lists Python **3.9, 3.10 and 3.11**. The current private **`main` branch still declares Python 3.10+** (`requires-python = ">=3.10"`). Choose Python 3.9 **only after checking out the development branch** until those changes are merged. The examples here choose Python **3.9** to match the verified Herts HPC environment. Python 3.10 and 3.11 can be used in their own clean environments; future versions need their own compatibility checks.

For Python 3.9, apply the private repository's [conservative version constraints](https://github.com/appsplorer/thomaslab-core/blob/audit/kaggle-hpc-final-20261021/constraints/python39.txt). The constraints are **not** a fully pinned lockfile; record resolved versions for reproducibility.

See [Python compatibility](python-compatibility.md) and [HPC validation](../guides/hpc-python39.md).

## Install the private research package

These commands assume you are an **authorized collaborator** with access to the private GitHub repository. If Git requests authentication, use your institution-approved SSH key or GitHub credentials; never put tokens in public commands, notebooks or logs.

### Windows / PowerShell and PyCharm

```powershell
git clone git@github.com:appsplorer/thomaslab-core.git
cd thomaslab-core
git switch audit/kaggle-hpc-final-20261021
py -3.9 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -c constraints/python39.txt -e ".[dev,notebooks]"
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -c "import thomaslab; print('Thomas Lab imported')"
```

In PyCharm, select `.venv\Scripts\python.exe` as the project interpreter and use the same environment for its Jupyter kernel.

### Linux / macOS

```bash
git clone git@github.com:appsplorer/thomaslab-core.git
cd thomaslab-core
git switch audit/kaggle-hpc-final-20261021
python3.9 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -c constraints/python39.txt -e '.[dev,notebooks]'
.venv/bin/python -m pip check
.venv/bin/python -c "import thomaslab; print('Thomas Lab imported')"
```

The optional scientific extras include `models` (PyTorch), `llm`, and `gpu`. Use those only with supported wheels, licenses and approved compute resources. For the complete notebook/docs/model QA on Python 3.9, an isolated environment with the approved extras is required; see [local validation](local-validation.md). `lifelines` and `shap` are standard runtime dependencies.

## Validate the research package

Use the **same isolated interpreter** for every command (not the login or system Python):

```bash
# Linux/macOS, from the private Core checkout
.venv/bin/python scripts/environment_preflight.py
.venv/bin/python scripts/python39_compat.py
.venv/bin/python scripts/local_quality_gate.py --quick
```

```powershell
# Windows PowerShell, from the private Core checkout
.\.venv\Scripts\python.exe scripts/environment_preflight.py
.\.venv\Scripts\python.exe scripts/python39_compat.py
.\.venv\Scripts\python.exe scripts/local_quality_gate.py --quick
```

Static compatibility success, a passing import, and a quick test run do **not** replace full pytest, the complete module import audit, the strict per-function execution ledger, or scientific validation. On Slurm follow the [isolated HPC acceptance procedure](../guides/hpc-python39.md), not a shared research environment.

## Install this public documentation site separately

You do **not** need access to the private package to preview the published documentation.

```bash
git clone https://github.com/appsplorer/thomaslab-docs.git
cd thomaslab-docs
python3.9 -m venv .venv-docs
.venv-docs/bin/python -m pip install -r requirements-docs.txt
.venv-docs/bin/python scripts/check_public_docs.py
.venv-docs/bin/python -m mkdocs build --strict
.venv-docs/bin/python -m mkdocs serve
```

For Windows, replace `.venv-docs/bin/python` with `.venv-docs\Scripts\python.exe` and create the environment using `py -3.9 -m venv .venv-docs`. The public site CI also validates documentation on Python 3.11 separately; that is a build interpreter choice, **not** the minimum version for the research package.

!!! warning "Scientific and institutional approvals are separate"
    Software installation never grants EHR/claims/PGx access, patient-level analysis permission, IRB/DUA clearance, externally reviewed gold mappings or publication-ready scientific methods.

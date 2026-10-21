# Python compatibility and reproducible environments

**The private Core development branch supports Python 3.9 or newer** according to its `pyproject.toml` (`requires-python = ">=3.9"`). **The currently released private `main` branch still declares `requires-python = ">=3.10"`.** Do not install Python 3.9 against `main` before the validated development changes have been merged. Python 3.9, 3.10 and 3.11 appear in its package classifiers. This is a software **version-support claim**, not a claim that every future interpreter, wheel, method or dataset has been independently validated.

| Environment | Recommended Python | What this means |
| --- | --- | --- |
| Institutional Herts HPC research checkout | **3.9** | The current integrated CPU validation scripts specifically require Python 3.9, an isolated venv, resolved dependencies and an exact Git SHA |
| Windows/PyCharm and local JupyterLab | **3.9** for reproducing the HPC baseline; **3.10/3.11** with their own clean environments | Project compatibility does not imply that identical binary wheels or results are available on every computer |
| Kaggle and notebook services | An available compatible **3.9+** interpreter and approved package set | Synthetic/public sources only; never upload restricted datasets or private repository credentials |
| Public `thomaslab-docs` static site | **3.9 and 3.11** for standalone MkDocs build checks | This repository contains Markdown and public static assets, not the private research package or source datasets |

## Verified Python 3.9 evidence and its limits

Real October 2026 Herts HPC acceptance logs on the private development branch establish that:

- An isolated **Python 3.9.25** environment passed `pip check`, with `lifelines 0.29.0`, `numpy 1.26.4`, `pyarrow 18.1.0`, `torch 2.8.0`, and the development tools available.
- Source commit `1ff0a055c43db0c5023b03a953cb92b08fb847ad` passed full pytest, Ruff, mypy, the complete quality gate, and imports of **106/106** discovered source modules. The strict callable execution inventory found **940 of 955** function and method bodies observed, so its final CPU technical status remained **FAIL**.
- At source commit `469c120a81bdf5957911550dea4075fbf577ab61`, focused CPU regression job `2499039` completed **PASS** (`0:0`, 32 seconds); full integrated CPU job **`2499042` completed PASS** (`0:0`, 16 minutes 51 seconds). All **21 executed technical phases passed**, including full pytest, Ruff/mypy and full quality, **106/106 imported modules** and **955/955 declared named function/method bodies observed**, with **zero unobserved functions**. The separate `reviewed_gold_matrix` phase remains **`NOT_RUN_REQUIRES_NAMED_APPROVAL`**.
- A previously performed NVIDIA A100 smoke test passed synthetic tensor arithmetic and gradient checks. It does not establish universal GPU compatibility.

These statements document specific test runs. **Even 955/955 function bodies being observed is not 100% branch coverage, proven numerical correctness, or scientific validation.** They do not assert that the private branch has merged into `main` or that GitHub CI is green; the three-version GitHub Actions matrix still reports failures at the tested source SHA. Clinical outcomes have not been independently validated. The independent clinical and scientific validation status remains **`NOT_ASSESSED`** until approved data mappings, independent studies and named expert sign-off are available.

## Python 3.9 dependency resolution

For installation in an authorized private checkout of `audit/kaggle-hpc-final-20261021` (not `main`):

```bash
git switch audit/kaggle-hpc-final-20261021
python3.9 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -c constraints/python39.txt -e '.[dev,notebooks]'
.venv/bin/python -m pip check
.venv/bin/python scripts/python39_compat.py
```

The file `constraints/python39.txt` belongs to the **private Core repository**. It limits ABI-sensitive dependencies such as NumPy to 1.x, PyArrow to versions below 19, and `lifelines` to compatible versions. It is a **constraint set**, not an environment lockfile, and must not be used as a claim that untested dependency combinations work.

For a full scientific-development and notebook QA environment, approved extras may include `models` and `docs` as well. The Herts HPC full-mode gate additionally expects `types-PyYAML`. Use the [HPC-specific instructions](../guides/hpc-python39.md) to create and audit the fully isolated environment on an approved preparation node.

## Separate code execution from scientific authorization

A complete software pass requires matching source SHA, tests, coverage, source imports, notebooks, packaging and quality gates. Even 100% of named function bodies reached by tests would **not** prove 100% branch coverage, correct mathematical assumptions, externally validated EHR/PGx semantics, five-person usability acceptance, security compliance or institutional authorization.

The documentation build is independent of the private package. See [installation](installation.md), [local testing](local-validation.md), and [release readiness](../guides/lab-validation-release-criteria.md).

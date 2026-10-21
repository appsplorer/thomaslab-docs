# Local validation and PyCharm

Use the local quality gate when you want to validate the repository on your own workstation without depending on a GitHub-hosted runner.

## Recommended Windows / PyCharm setup

From PowerShell:

```powershell
git clone https://github.com/appsplorer/thomaslab-core.git
cd thomaslab-core
git switch main

py -3.9 -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -c constraints/python39.txt -e ".[dev,docs,notebooks]"
python -m pip install --no-cache-dir --index-url https://download.pytorch.org/whl/cpu "torch>=2.1.0"
```

In PyCharm, set the project interpreter to:

```text
<repository>\.venv\Scripts\python.exe
```

These example commands select **Python 3.9 on the current `main` branch**, which now includes the previously validated development history without squashing. The private package also declares 3.10 and 3.11 compatibility; choose a dedicated virtual environment for each interpreter rather than reusing a shared scientific environment. For 3.9, `constraints/python39.txt` supplies conservative resolution bounds, not a reproducible lockfile. See the [compatibility matrix](../getting-started/python-compatibility.md).

## One-command full quality gate

Run from the repository root:

```powershell
python scripts/local_quality_gate.py
```

The full gate performs:

1. dependency/environment preflight;
2. Python byte-code compilation;
3. structural public-API audit;
4. Ruff;
5. mypy;
6. complete pytest suite with the package coverage threshold;
7. public-callable executed-body coverage audit;
8. stable-release QA;
9. notebook JSON validation;
10. stable reference-notebook execution;
11. wheel and source-distribution build;
12. built-wheel/public-API smoke validation;
13. dependency consistency check;
14. strict MkDocs build.

A shorter developer loop is available with:

```powershell
python scripts/local_quality_gate.py --quick
```

## Portable synthetic streaming benchmark

Run the following on your PyCharm terminal, a Kaggle notebook kernel using
legitimately synthetic data, or a permitted HPC login/compute environment:

```bash
python scripts/benchmark_validation_scale.py --rows 100000 --chunk-rows 5000 --output results/synthetic-scale-100k.json
```

The tool creates a temporary fabricated CSV, scans **all** of its rows, and
writes an immutable JSON report of elapsed time, throughput and Python-traced
allocations. It cannot quantify all native-library RAM use or guarantee
performance on multi-million-row hospital EHR/Parquet/Excel workloads.
Use a new `--output` filename for each run; compare host environments rather
than treating one result as a universal benchmark. Larger than one-million-row
or institutional workloads require separately approved resources, controls
and observation. No real patient data are read by this benchmark.

This is software performance evidence only: a synthetic run does **not**
complete the independent 15–20 unseen-source study or a five-researcher
usability evaluation. Follow the separate human-review protocol and do not
claim clinical deployment approval from local quality checks.

Use the full gate before treating a checkout as release-ready.

## Environment preflight only

To inspect required and optional native dependencies without running the full suite:

```powershell
python scripts/environment_preflight.py
```

The preflight distinguishes package/import failures from operating-system native-extension blocks.

## Windows Application Control

Some managed or hardened Windows machines apply App Control/Code Integrity rules to native extensions loaded by Python packages. A typical failure looks like:

```text
ImportError: DLL load failed ... An Application Control policy has blocked this file.
```

That message is an operating-system policy decision rather than a failed Python assertion.

The modeling layer avoids eager loading of scikit-learn clustering binaries and provides NumPy fallbacks for its scaling/K-Means phenotype-clustering path. The active backend is recorded in returned metadata as `scaler_backend` and `kmeans_backend`.

This fallback is deliberately narrow. If Windows blocks a native extension required by a scientific dependency with no validated fallback, the package should fail visibly rather than silently substitute a different estimator. In an institution-managed environment, the correct remedy is to use an approved execution environment or have the relevant native package allowed by the administrator.

## GitHub Actions mode

The Tests, Documentation, and Infrastructure Audit workflows remain available through **Actions → Run workflow**, but automatic push/pull-request execution is disabled while the repository is using local-first validation. This prevents infrastructure-level hosted-runner allocation failures from being confused with code failures.

When hosted runners are available again, the automatic triggers can be restored without changing the local quality gate. Manual documentation runs on `main` can still publish the generated MkDocs site.

## Interpreting a pass

A complete local quality-gate pass establishes that the checked-out software tree satisfies the repository's automated software checks in that environment.

It does **not** establish that:

- an unseen dataset has valid clinical semantics;
- a source-to-canonical mapping is correct;
- a phenotype is clinically valid;
- causal assumptions hold;
- a model transports to another institution or population;
- a research bundle is de-identified;
- a result is suitable for patient-level clinical use.

For a new dataset, use the onboarding, contract, temporal, leakage, provenance, and external-validation workflow in the [Full research pipeline](../full-pipeline.md).

## Before analyzing a future dataset

For every new hospital, registry, claims source, survey, genomic source, or collaborator dataset:

1. inspect the raw source before mapping;
2. keep source-specific mappings in reviewed configuration;
3. validate required columns, units, code systems, cardinality, missingness, and timing;
4. fail closed on unresolved mappings or unsupported states;
5. build the cohort and outcomes from explicit study definitions;
6. split at the patient/site/time level appropriate to the design;
7. run leakage checks before model fitting;
8. retain source and transformation provenance;
9. quantify uncertainty and site/subgroup behavior;
10. perform genuinely independent external validation when the scientific claim requires it.

No generic software package can guarantee correctness on every future dataset without these study-level checks.

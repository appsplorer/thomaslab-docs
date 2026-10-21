# Thomas Lab: PyCharm, JupyterLab and Kaggle handoff

The library is notebook-native. There is no Streamlit server, public upload
endpoint or need to edit YAML to try the synthetic demonstration. Use a local
copy of the private `appsplorer/thomaslab-core` repository with Python **3.9 or newer**
and confirm you are on the tested commit before running real research.

## PyCharm on Windows

Open the cloned repository as a PyCharm project, then in its Terminal (PowerShell):

```powershell
py -3.9 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -c constraints/python39.txt -e ".[notebooks,dev]"
.\.venv\Scripts\python.exe -m ipykernel install --user --name thomaslab-pycharm --display-name "Thomas Lab (Python 3.9)"
```

These example commands deliberately use Python 3.9; 3.10 or 3.11 may be used in a separate compatible interpreter. See the [compatibility matrix](../getting-started/python-compatibility.md).

Select `.venv` as Project Interpreter and the **Thomas Lab (Python 3.12)**
kernel in the PyCharm notebook UI. If PyCharm offers Jupyter server options,
use the project's interpreter/local notebook server. Do not enter institutional
credentials in notebook source or commit `.ipynb` cell outputs containing data.

Open `notebooks/07_new_dataset_onboarding.ipynb` for interactive mapping or
`notebooks/36_longitudinal_msm.ipynb` for its bounded synthetic guided method
demo. Run its guided control cell and click **Validate & run**. Unsupported
institutional mode displays an explicit block. Advanced reference recipes in
notebooks 20–55 are preserved in Markdown, so **Run All** does not open
placeholder paths. Execute a recipe separately only after reviewing its
dataset input, method assumptions and permitted file locations.

Notebook 07 is a source-file onboarding workflow and has **different** buttons:
**Inspect**, **Generate adapter**, **Preview validation**, **Validate ALL rows**,
and **Open visual mapping workbench**. An administrator must configure the
approved `lab_execution_policy` before those buttons read or write files.
Select a correct source classification and absolute approved paths. A source
changed after preview is blocked. For a synthetic-only policy example see the
[notebook workbench instructions](notebook-workbench-quickstart.md).

## Basic verification from the same local interpreter

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_adaptive_release_gate.py tests/test_adaptive_researcher_journey.py -q
.\.venv\Scripts\python.exe scripts/notebook_smoke.py --all-guided --widgets
.\.venv\Scripts\python.exe scripts/notebook_smoke.py --acceptance-output results/notebooks-pycharm-check
.\.venv\Scripts\python.exe scripts/run_lab_adaptation_benchmark.py --synthetic --report results/synthetic-benchmark.json
.\.venv\Scripts\python.exe scripts/local_quality_gate.py --quick
```

Use **fresh** output directories/names for repeated runs; reports are
immutable. The full quality gate (remove `--quick`) additionally needs the
packaging, notebook and documentation toolchain from the repository dev/docs
environment. Local CPU memory and runtime results will differ by machine.

The synthetic suite covers ten representative table families; it does *not*
validate real EHR notes, claims, pharmacogenomics semantics or transportability.
The Synthea public sample has a recorded structural-mapping **FAIL**
(recall 0.75 at threshold 0.80) that requires human review.

## Kaggle: public/synthetic only

1. Use a **private notebook** with a legitimately public or fabricated
   input; do not attach UGA/EHR/claims, student records or restricted data.
2. Install `thomaslab-core` from an authorized source copy. Never make
   the private repository or tokens public through notebook output.
3. Disable network unless a particular approved public source is required.
   The public benchmark downloader has `allow_network=False` by default.
4. Set `ExecutionPolicy(environment="kaggle", ...)` only for public or
   synthetic sources. Internal/restricted classifications deliberately fail.
5. Keep notebook outputs free from direct identifiers, small-cell tables,
   PHI-like values, access tokens and unreviewed narratives.

Kaggle is not a substitute for hospital-approved compute, credentialed
PhysioNet data agreements, UGA IT accounts or IRB/data-use authorization.

## Institutional and supervisor review boundary

An `ExecutionPolicy` specifies narrow absolute input/output roots, actor,
approved environment and redacted audit path. An institution must *separately*
enforce account permissions, storage ACLs, reviewed contracts and source DUA.
Run `validate_entire_source` on the **full data**, then approve a versioned
adapter with independent named review. For analyses use
`GovernedNotebookSession`, verify source checksum, and export only a reviewed,
non-small aggregate to an approved directory. This software does not remove
PHI, provide de-identification certification or replace scientific/IRB review.

## What each evidence status means

| Evidence | Status | Meaning |
| --- | --- | --- |
| 40 guided notebook callbacks | `PASSED_SYNTHETIC_CALLBACK` | Method demo executed and unsupported mode blocked |
| 19 legacy notebooks | `LEGACY_WIDGET_REGISTERED_ONLY` | Widgets bind and code cells compile; no independent live-use claim |
| Full synthetic review-to-bundle journey | Automated integration | A *simulated* reviewer exercised software interfaces only |
| Synthea April 2020 public synthetic sample | `FAIL` | 1,171 rows, 3 of 4 reviewed mappings suggested |
| Dynamic FDA openFDA, MIMIC, Thomas 2024 cohort | `NOT_RUN` / reference-only | No patient-level validation evidence claimed |
| Five-researcher user study | `NOT_RUN` | Requires actual independent participants |

See [release criteria](lab-validation-release-criteria.md) and
[researcher protocol](researcher-usability-protocol.md).

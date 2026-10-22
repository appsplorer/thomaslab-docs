# Code versus documentation: verification and evidence

!!! warning "Read this before interpreting the handbook as lab deployment approval"
    The public **thomaslab-docs** site is a static teaching and API-reference publication. The software itself lives in private **thomaslab-core**, available only to authorized collaborators. Documentation coverage and a working website do not establish numerical correctness, data authorization, a validated clinical study, or publication readiness.

## What the two repositories contain

| Location | Source of truth | Evidence provided | Evidence NOT provided |
| --- | --- | --- | --- |
| Public `thomaslab-docs` | Approved Markdown, examples and static API snapshots | Guide usability, links, search, tutorial instructions, stable function reference | Software execution, patient-data access, institution-approved research |
| Private `thomaslab-core` | Implementation, notebooks, tests, data contracts, software-release gates | Source inspection, executable tests, package metadata, scientific safeguards | Automatic external validity, independent researcher usability, IRB/DUA approval |
| Local or hosted test artifacts | Exact Git commit and runner environment | Actual observed test output and release evidence | Universal correctness across unseen datasets |

**Source review performed:** private `thomaslab-core` development branches, including `audit/kaggle-hpc-final-20261021` (subsequently integrated into `main` with a two-parent non-squash merge and every original commit retained). The real Herts Python 3.9 CPU job `2498939`, at source commit `1ff0a055c43db0c5023b03a953cb92b08fb847ad`, passed full pytest, quick/full quality gates, and all 106 module imports. Its strict callable evidence gate reported **940/955 observed** and therefore the CPU technical status was **FAIL**. Later focused CPU regression job `2499039` passed and exact source-commit `469c120a81bdf5957911550dea4075fbf577ab61` integrated CPU job **`2499042`** completed `0:0` with **21 passing executed technical phases, zero failed phases, 106/106 module imports, and 955/955 named function/method bodies observed**. The single reviewer-approved gold-mapping phase remained `NOT_RUN`, and GitHub Actions CI remained failing independently. Separately, independent clinical dataset/method approval is `NOT_ASSESSED`.

## Traceability matrix: P0 / P1 engineering safeguards

| Scope | Source implementation | Executable evidence | Current limitation |
| --- | --- | --- | --- |
| Lossless CSV identifiers | `thomaslab.easy.load_clinical_table` | Existing identifier tests | Excel cells stored numerically may have irrecoverably lost leading zeros |
| Full validation, not 5,000-row preview | `thomaslab.adaptive.full_validation.validate_entire_source` | Full-row corruption and resource tests | Multi-sheet workbooks and other unsupported formats need reviewed conversion |
| Reviewed, immutable adapters | `thomaslab.adaptive.adapter_registry.AdapterRegistry` | Approval, drift and tamper tests | Mapping correctness requires named expert review |
| Researcher-safe beginner model | `thomaslab.easy.quick_binary_model`, Notebook 03 | Explicit split and leakage tests | A model fit does not establish transportability |
| Governed inputs/outputs | `thomaslab.adaptive.governance` | Policy, path and exporter tests | Python checks cannot provision OS accounts, ACLs, IRB/DUA approval or de-identify arbitrary data |
| Pharmacogenomics indication | `thomaslab.pgx_guidelines.lookup_pgx_rule` | `tests/test_scientific_input_contracts.py` | Exact-SHA Python 3.9 HPC software gate PASS (job 2499042); PGx assay, allele and guideline domain sign-off remains pending |
| Competing-risk numerical coding | `thomaslab.survival.aalen_johansen_cif` | Finite time, binary event, integral cause and known closed-form tests | Exact-SHA Python 3.9 HPC software gate PASS (job 2499042); method-specific clinical review pending; no Fine–Gray or causal claim |
| Notebook interface | 59 notebooks | 40 synthetic callbacks; 19 legacy registrations | Five independent nontechnical researchers and complete legacy user journeys remain outstanding |

## How to reproduce code-side checks (authorized collaborators)

Use the private repository and choose a clean, isolated interpreter. Do **not** upload source code or institutional records to the public documentation repository.

```powershell
git clone https://github.com/appsplorer/thomaslab-core.git
cd thomaslab-core
git switch main
py -3.9 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -c constraints/python39.txt -e ".[dev,notebooks,docs]"
.\.venv\Scripts\python.exe -m pytest -q tests/test_scientific_input_contracts.py tests/test_code_docs_audit.py tests/test_pgx_guidelines_v08.py tests/test_survival_v16.py
.\.venv\Scripts\python.exe scripts/audit_code_docs.py --output code-doc-audit-local.json
.\.venv\Scripts\python.exe scripts/local_quality_gate.py --quick
```

For a full packaging, reference-notebook and documentation gate, install the tested CPU PyTorch environment and run `python scripts/local_quality_gate.py` in a clean virtual environment. Keep the **exact Git SHA, dependency versions, machine details, raw logs and artifacts** with the test report. A report that only inventories source files explicitly labels tests `NOT_RUN`; it is not a passing numerical test.

## What should block a release

- Failing regression tests, inconsistent package metadata, missing license or security policy, broken builds, or unresolved high-severity numerical input defects.
- A source change without fresh test results at its exact commit; a GitHub workflow with no executed steps does **not** count as passing CI.
- A synthetic benchmark being presented as independent clinical validation.
- Publishing patient-level data, credentials or restricted lab data into code, notebook outputs or public documentation.

## What remains outside automated software verification

**15–20 genuinely independently sourced unseen datasets**, a **five-researcher task study**, UGA-approved storage and account permissions, applicable IRB/DUA decisions, and clinical or publication-level scientific review. Keep each explicitly `NOT_RUN`, `PENDING` or `NOT_VERIFIED` until actual evidence is attached.

## Publishing discipline

Public documentation is **not** automatically synchronized from the private research repository. When private code changes: review source/tests first, update sanitized Markdown and the public static function reference, run public `mkdocs build --strict`, then merge and publish the documentation. A published documentation update must not imply that the private research-code PR has already merged.

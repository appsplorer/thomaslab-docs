# Thomas Lab Research Handbook

**A practical, reproducible research manual for clinicians, pharmacists, research staff, and data scientists.**

This public website teaches the Thomas Lab notebook-based research workflows. The **source-code repository is private** and only available to authorized collaborators. Every tutorial here uses fabricated, non-patient data.

**Supported core interpreters:** Python **3.9+** (3.9, 3.10 and 3.11 documented and tested at specific development commits). Start with the [Python compatibility guide](getting-started/python-compatibility.md) and [installation instructions](getting-started/installation.md). This published documentation does not imply that the current private development PRs have merged.

!!! danger "Research software only"
    thomaslab-core is not an approved medical device or clinical decision support system. Successful calculations, unit tests, and synthetic experiments **do not** constitute clinical, scientific-publication, or institutional-data approval.

## Find the right workflow

| Your task | Start here | Outcome |
|---|---|---|
| I'm new to Python or Jupyter | [First research session](getting-started/first-session.md) | Install, run synthetic data and interpret a basic output |
| I received a new CSV, EHR extract or registry | [Unfamiliar dataset walkthrough](tutorials/dataset-onboarding.md) | Review schema, units, provenance and approval requirements |
| I need to choose a clinical analysis | [Scientific validation](tutorials/scientific-review.md) | Select an analysis lane and understand its assumptions |
| I want interactive notebooks without YAML editing | [Notebook workbench](guides/notebook-workbench-quickstart.md) | Use reviewed mapping and guided demonstrations |
| I use PyCharm, Jupyter, Kaggle or HPC | [Environment setup](guides/pycharm-lab-workbench.md) | Configure an appropriate environment and approved data source |
| I need PGx, claims, target trials or survival tools | [Research workflows](guides/pgx.md) | Find the relevant method and safety requirements |
| I need a function's signature | [API reference](api/index.md) | Find module documentation and Python examples |

## The eight-stage research journey

1. **Specify the question:** Population, treatment/exposure, comparison, outcome, time zero, and estimand.
2. **Confirm permission:** Dataset classification, authorized workspace, intended uses, and responsible reviewer.
3. **Inspect source:** Row grain, identifiers, data types, coding systems, missingness, dates, and units.
4. **Review mappings:** Candidate roles, alternatives, confidence, schema drift, and named reviewer sign-off.
5. **Validate completely:** Run full-source integrity checks, not just a 5,000-row preview.
6. **Choose analysis:** Select a valid method with patient/site/time-aware validation; block unsupported designs.
7. **Interpret scientifically:** Assess bias, uncertainty, censoring, transportability and clinical implications.
8. **Export with governance:** Use approved summary outputs, fingerprints, checksums and an audit trail.

## What is verified and what remains open?

The development branch has passed extensive synthetic software checks, including guided callbacks for 40 advanced/demo notebooks. The remaining 19 legacy notebook interfaces have not all undergone independent live human task testing. Evaluations on **15–20 independently sourced unseen datasets**, a **five-researcher usability study**, and institutional patient-data permissions remain outstanding. See [Release and science gates](guides/lab-validation-release-criteria.md) and [Audit traceability](guides/audit-traceability.md).

## About this website

The website is built with MkDocs Material and deployed as **static public documentation**; no patient data is required. [How publication works](publishing/github-pages.md).
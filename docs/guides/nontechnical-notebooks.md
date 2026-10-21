# Guided notebooks for non-technical collaborators

Version 0.3.0 includes a set of widget-driven Jupyter notebooks under `notebooks/`. They are designed for pharmacists, clinicians, students, and research staff who need to inspect data or run a baseline analysis without building a Python pipeline from scratch.

## Install

```bash
python -m pip install -e ".[notebooks]"
jupyter lab
```

## Available notebooks

| Notebook | Purpose |
|---|---|
| `01_nontechnical_data_check.ipynb` | Load CSV/Excel/Parquet data and inspect privacy-reduced structure, missingness, and quality summary |
| `02_cohort_flow_builder.ipynb` | Build a sequential cohort inclusion/exclusion table |
| `03_nontechnical_binary_model.ipynb` | Select patient/site/time validation and inspect aggregate AUROC/AUPRC/Brier score; no patient-level predictions |
| `04_fhir_bundle_explorer.ipynb` | Load FHIR Bundle JSON and extract Observation/MedicationRequest tables |
| `05_export_research_bundle.ipynb` | Blocks ungoverned table export and directs users to the governed bundle workflow |
| `06_schema_adapter.ipynb` | Create a non-overwriting draft mapping and inspect structural standardization; use Notebook 07 for named approval |
| `07_new_dataset_onboarding.ipynb` | Policy-gated source inspection, adapter draft, full-source validation, visual mapping review and approval request |

## Safe-use rules

- Do not use these notebooks as autonomous clinical decision support.
- Do not upload PHI to an unapproved notebook server.
- Keep outcome definitions, cohort logic, units, and terminology mappings under protocol control.
- Treat the baseline modeling notebook as an orientation tool; publication models still require prespecified validation, calibration, uncertainty, and external validation where appropriate.
- CSV/TSV values are preserved as text by default, including leading-zero IDs and codes. Explicitly review and parse quantitative/date columns for analysis. Numeric-formatted spreadsheet identifier cells are **not** automatically recoverable; save them as text before import.
- In Notebook 03, list clinically reviewed quantitative predictors in **Numeric features**. Any unparseable nonblank value blocks the run instead of silently becoming an analysis value. Leave clinical codes and patient identifiers as text and never use them as predictors.
- Workbook-wide structural verification supports a **single-sheet `.xlsx`** in streaming mode. Multi-sheet Excel and older `.xls` must be converted or reviewed as separately identified, approved sources; passing this scan does not establish clinical semantic validity.
- Existing schema YAML files are never replaced by the suggestion generator. Choose a new versioned name and complete the visual named-review workflow in Notebook 07 before using a mapping as approved.
- Notebook 07 requires the lab administrator to configure `lab_execution_policy` before a user clicks **Inspect**, **Generate**, **Preview**, **Validate ALL rows**, or opens the mapping workbench. Enter **absolute approved** dataset and output directories, select the correct classification, and do not treat a classification dropdown as a data-use authorization. An altered or unauthorized source is blocked even after an earlier successful preview. Restricted data additionally require administrator-provided `lab_data_use_approved=True` and the institutional policy attestations; they cannot be self-authorized by a researcher's notebook controls.

# Thomas Lab notebook-native research workbench

Thomas Lab offers 59 Jupyter notebooks: 01–58 and `demo_pipeline.ipynb`.
All 19 earlier notebooks retain their existing `ipywidgets` controls. Every
notebook 20–58 and the demo now has a guided launch cell with method-specific
controls, a **Validate & run** button, and an explicit scientific-review state.
This is a Python library and notebook interface, not a Streamlit service.

## Install and open locally (PyCharm or JupyterLab)

Use Python 3.10 or later in a dedicated virtual environment:

```bash
python -m pip install -e ".[notebooks]"
jupyter lab
```

In PyCharm, select the same project interpreter for its Jupyter notebook
kernel. Open, for example, `notebooks/36_longitudinal_msm.ipynb`, execute
the new **Guided synthetic research demonstration** cell, inspect the
parameter controls, and press **Validate & run**. The 148 advanced code recipes
in notebooks 20–55 remain below their widgets as fenced Markdown examples;
they require a reviewed local dataset and do not execute unexpectedly when
you select **Run All**. Technical researchers can copy a recipe into a new
code cell after supplying their own approved file paths.

For an advanced notebook form in a Python console:

```python
from IPython.display import display
from thomaslab.adaptive.notebook_actions import launch_notebook_panel

panel = launch_notebook_panel("36")
display(panel.widget)
```

Notebook 07 contains the interactive column-mapping workbench. Review its
suggestions, alternatives and units, validate the *entire source*, and submit
adapter mappings for human approval; a sample preview cannot grant approval.
Its older **Inspect**, **Generate**, **Preview** and **Validate ALL rows**
buttons are now subject to the same administrator-configured `ExecutionPolicy`.
Use narrow **absolute** approved source and output paths. A source or data
classification changed after inspection must pass policy validation again;
the notebook never silently continues on an older approved source.

For a locally fabricated CSV, the lab administrator can configure a bounded
synthetic-only policy in an earlier trusted setup cell or approved environment
bootstrap (the researcher does not edit the mapping YAML):

```python
from pathlib import Path
from thomaslab.adaptive.governance import ExecutionPolicy

synthetic_root = Path("/absolute/path/to/local/synthetic_workspace").resolve()
lab_execution_policy = ExecutionPolicy(
    environment="local",
    approved_input_roots=(synthetic_root,),
    approved_output_roots=(synthetic_root,),
)
```

The directory must already exist with suitable OS permissions. This example
does **not** authorize institutional datasets or let users assign themselves
hospital data-use rights. The reviewer separately approves source semantics
and each adapter revision; the workbench submits a review request, not an
automatic approval.

## Data safety and scientific interpretation

- The notebook convenience launcher uses **synthetic data only**. It does not
  accept arbitrary institutional DataFrames, infer EHR semantics, or authorize
  a clinical or causal study. In notebooks 20–25, role fields are prefilled
  solely for the bundled synthetic fixture.
- For restricted EHR, claims, PGx or multisite records, the institution must
  first approve the data use, user account, storage, compute host, dataset
  adapter, source-wide validation and safe output root. Use the
  `GovernedNotebookSession` API on the approved host for the reviewed source.
- Kaggle is suitable **only for synthetic or legitimately public data**.
  Never upload patient-level records, credentials or restricted exports.
- A runnable estimator is **not publication approval**. Study-design validity,
  causal assumptions, positivity, measurement semantics, assay coverage,
  terminology versions and clinical interpretation still require qualified
  independent review. Treat demonstrations as educational diagnostics.
- Notebook 05 now **blocks** its previous ungoverned export action. Its old
  path could include row-level previews. Use the governed workflow in
  notebooks 56/57 for an approved synthetic or institutional aggregate export.
- Notebooks 01–19 use a privacy-safe display wrapper that shows structural
  column/row/missingness diagnostics, not raw observations or note excerpts.
  This also means some existing legacy tables are intentionally summarized.
- Notebook 03 now refuses an unspecified or unsuitable validation split;
  researchers must select patient-, site- or time-aware validation with a
  patient identifier. The callback emits aggregate performance only. Notebook
  06 refuses to overwrite a previous schema suggestion, including one already
  reviewed by a researcher; revisions use new names and Notebook 07 approval.
- CSV/TSV loading preserves raw text (including `000123` and zero-padded NDC
  codes). Clinical numeric/date conversions remain a deliberate, reviewed step;
  spreadsheet cells stored as numbers cannot be made lossless after import.
- The underlying legacy `thomaslab.easy.export_analysis_bundle` library helper
  still copies caller-supplied tables; do not use it on restricted data. The
  governed export route uses `export_governed_bundle`, which
  defaults to reviewed non-small aggregate tables, but **does not guarantee
  de-identification** or replace institutional disclosure review.

## Local acceptance tests

```bash
python -m pytest tests/test_notebook_interactions.py tests/test_notebook_catalog.py -q
python -m pytest tests/test_legacy_notebook_safety_callbacks.py -q
python scripts/notebook_smoke.py --all-guided --widgets
python scripts/notebook_smoke.py notebooks/*.ipynb
python scripts/notebook_smoke.py --acceptance-output results/my-first-acceptance
python scripts/local_quality_gate.py --quick
```

The guided smoke executes every 20–58/demo method callback on a bounded
synthetic fixture and independently checks that institutional-mode requests
block. It also discovers the 19 existing widget notebooks. For PyCharm, run
these commands from the repository root using the same interpreter selected
as the Jupyter kernel. The acceptance JSON distinguishes **40 exercised
synthetic callbacks** from **19 registered legacy widgets**; the latter
are not falsely described as executed on real researcher inputs. Independent
five-researcher validation is still `NOT_RUN` (see
`researcher-usability-protocol.md`). None of these software tests replaces
clinical validation or institutional deployment authorization.

# First research session

**Audience:** clinicians, pharmacists, graduate students and research assistants. **All data below is synthetic.**

!!! warning "Keep research data in approved environments"
    Never upload patient-level EHR, claims, genetics or clinical notes to Kaggle, GitHub Pages, public notebook services or unapproved workspaces.

## 1. Install from your authorized private checkout

In **PyCharm Terminal / PowerShell**:

```powershell
py -3.9 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[notebooks]"
python -c "import thomaslab; print('Thomas Lab ready')"
```

For Linux/macOS/HPC, activate with `source .venv/bin/activate`. Python 3.9 or newer is supported; these steps choose 3.9 to match the institutional HPC baseline. Select the same interpreter for the Jupyter kernel. On Linux/macOS use `python3.9 -m venv .venv` to create that environment. The private checkout requires existing collaborator permission; do not put access tokens into notebooks.

## 2. Create an entirely fabricated cohort

Copy this into a **new Jupyter code cell**:

```python
from pathlib import Path
import pandas as pd

root = Path("demo_output")
root.mkdir(exist_ok=True)
cohort = pd.DataFrame({
    "patient_id": ["S001", "S002", "S003", "S004", "S005", "S006"],
    "site": ["A", "A", "B", "B", "A", "B"],
    "age": [59, 72, 64, 51, 68, 56],
    "event": [0, 1, 0, 0, 1, 0],
    "follow_up_days": [365, 60, 365, 365, 200, 365]
})
cohort.to_csv(root / "synthetic_cohort.csv", index=False)
print("Synthetic rows:", len(cohort))
```

**Expected:** `Synthetic rows: 6`. These are fabricated records, not study participants.

## 3. Run a transparent baseline analysis

```python
from thomaslab.easy import quick_cohort_summary, compute_incidence_rate

summary = quick_cohort_summary(cohort, outcome_col="event")
print(summary["n_rows"], summary["outcome"]["events"])
rate = compute_incidence_rate(cohort, "event", "follow_up_days")
print(round(rate["person_years"], 2))
print(round(rate["incidence_rate"], 2))
```

**Expected:** 6 rows and 2 events; approximately 4.71 person-years and 42.47 events per 100 person-years (a crude synthetic calculation, not a clinical estimate). No confounding adjustment, censoring model or causal interpretation is provided here.

## 4. Open a guided notebook

Start `jupyter lab` or open a notebook with the same interpreter in PyCharm. For example, an advanced notebook contains a **Guided synthetic research demonstration** cell with controls and a **Validate & run** button.

Use [Notebook 07's reviewed data-mapping workbench](../guides/notebook-workbench-quickstart.md) for unfamiliar sources. Its file controls require an administrator-supplied `ExecutionPolicy`, absolute approved paths and full-source validation. A column suggestion is *not* an approved clinical mapping.

## 5. Read the status before sharing results

A callback pass proves a software path executes. It does not establish correct outcomes, medical advice, causal validity or publication readiness. Record the data, method and software decisions separately.

**Next:** [Adapting unfamiliar data](../tutorials/dataset-onboarding.md) · [Scientific review](../tutorials/scientific-review.md) · [PyCharm/Kaggle/HPC](../guides/pycharm-lab-workbench.md).
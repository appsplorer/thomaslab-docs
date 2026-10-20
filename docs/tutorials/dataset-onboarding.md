# Tutorial: adapt an unfamiliar dataset

**Objective:** safely map a new registry, claims, EHR or CSV table without changing identifiers or guessing clinical meaning.

## 1. Inventory the source

Record **institution, owner, authorized purpose, row grain** (patient/encounter/claim), source timestamp, coding scheme, measurement units and follow-up window before opening patient-level files. Keep restricted files on approved institutional systems.

**Synthetic example:**

```python
from pathlib import Path
import pandas as pd

root = Path("demo_output")
root.mkdir(exist_ok=True)
path = root / "unseen_synthetic.csv"
pd.DataFrame({
    "patient_code": ["000123", "000124", "000125"],
    "visit_on": ["2026-01-02", "2026-01-05", "2026-01-07"],
    "creatinine_mg_dl": ["1.1", "0.9", "1.3"],
    "event_flag": ["0", "1", "0"],
}).to_csv(path, index=False)
raw = pd.read_csv(path, dtype=str, keep_default_na=False)
assert raw.loc[0, "patient_code"] == "000123"
print(raw.shape)
```

**Expected:** `(3, 4)`. Preserving raw text matters for leading-zero patient IDs and drug codes. Numeric-stored Excel identifiers may already be irreversibly altered.

## 2. Approve semantic mappings

| Source column | Candidate meaning | Human review required |
|---|---|---|
| `patient_code` | Person identifier | ID formatting, uniqueness, linkage across visits |
| `visit_on` | Visit date | Time zone, precision, and chronology |
| `creatinine_mg_dl` | Clinical laboratory result | Analyte, specimen, units, reference range |
| `event_flag` | Binary clinical endpoint | Exact phenotype, window, ascertainment |

The [visual notebook workbench](../guides/notebook-workbench-quickstart.md) shows suggested matches, alternatives, confidence, units, and review status. **Suggested mappings are never silently approved.**

## 3. Validate every row

A preview of 5,000 records is not sufficient for a large file. Before approval, run the full-source validator and review date parsing, missing values, identifiers, duplicate keys, unit mismatches, and schema drift. Single-sheet `.xlsx` full scanning is supported in the latest workbench; multi-sheet or legacy XLS needs explicit reviewed conversion.

## 4. Register an immutable adapter

Record the source checksum, approved column mapping, dataset grain, institution, reviewer's identity, decision date and adapter version. Do not overwrite existing YAML files or treat a successful schema suggestion as human sign-off. A subsequent data extract must undergo drift checks.

## 5. Select a defensible analysis

Write a protocol specifying population, eligibility, time zero, exposure, comparison, outcome, confounders, censoring and validation split. Structural consistency does **not** imply that a causal study design is identified.

## 6. Export an auditable handoff

A governed package should contain approved summary outputs, the method specification, source fingerprint, validation report, adapter revision, audit log and checksums. Never attach raw patient tables or identifiable notes to a public issue, tutorial or website.

**Next:** [Scientific review gates](scientific-review.md) · [Mapping guide](../guides/schema-adapters.md) · [Governed data use](../guides/governed-notebook-use.md).
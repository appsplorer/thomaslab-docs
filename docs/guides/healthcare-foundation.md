# Dataset-neutral healthcare foundation and standard baselines

**Status:** Implemented as new research code; independent HPC execution and
clinical validation pending. Code entry: `thomaslab.healthcare_foundation`
(experimental, intentionally outside the v1 frozen public-module list).

The helpers accept tabular frames from synthetic/reviewed exports of EHR,
OMOP/FHIR flattened records, claims, pharmacy, registries and PGx.
**They do not automatically understand all datasets.** Column patterns are
suggestions, not proof of clinical grain, code/units, consent or temporal
validity. Nested FHIR bundles, unstructured protected text, genomic variant
calling and image arrays require separate vetted adapters.

~~~python
import pandas as pd
from thomaslab.healthcare_foundation import (
    suggest_dataset_families, profile_healthcare_table,
    validate_column_contract, patient_split_overlap,
    baseline_leakage_check, binary_baseline_report,
    regression_baseline_report,
)

# Invented records only; no actual patient content.
example = pd.DataFrame({
    "patient_id": ["DEMO001", "DEMO002"],
    "encounter_id": ["E1", "E2"],
    "event_time": ["2026-01-01", "2026-01-02"],
    "outcome": [0, 1],
})
print(suggest_dataset_families(example.columns))
print(profile_healthcare_table(example))
print(validate_column_contract(example, {
    "patient_id": "id", "outcome": "binary", "event_time": "date"
}))
print(binary_baseline_report([0, 0, 1, 1], [0.1, 0.2, 0.8, 0.9]))
~~~

All reports contain aggregate diagnostics, not sample records or identifiers.
Baseline inputs must be held out independently by patient/site/time as
appropriate. Thresholds and estimands must be chosen *before* test evaluation.
Single-class ROC AUC is reported as `None` rather than fabricated.

The baseline reports are **descriptive software checks**, not clinical
prediction validity, correct calibration on new hospitals, causal
identification, medication-safety estimands or publication evidence.
Perform specialist data profiling, label adjudication, transportability,
clinical utility, uncertainty intervals and external validation separately.

## Test and release procedure

~~~bash
python -m pytest -q tests/test_healthcare_foundation.py
python scripts/local_quality_gate.py --quick
~~~

Keep the current exploratory module out of the frozen v1 API until a reviewed
compatibility expansion and multi-source scientific validation are available.

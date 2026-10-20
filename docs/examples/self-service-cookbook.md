# Self-service implementation cookbook

This cookbook is the practical bridge between the generated API reference and complete research workflows. It uses synthetic data only. Replace the examples with reviewed, governed, study-specific data only after validating schema, units, timing, code systems, and cohort definitions.

## 1. Unseen dataset onboarding

~~~python
import pandas as pd

from thomaslab.onboard import generate_adapter_bundle, inspect_source

data = pd.DataFrame(
    {
        "PATIENT": ["P001", "P002", "P003"],
        "EVENT_DATE": ["2026-01-10", "2026-01-11", "2026-01-12"],
        "AGE": [64, 71, 58],
    }
)

inspection = inspect_source(data)
print(inspection["profile"])
print(inspection["semantics"])

bundle = generate_adapter_bundle(
    data,
    "work/adapters/site_v1",
    dataset_name="site_v1",
    required_columns=["PATIENT", "EVENT_DATE"],
)
print(bundle)
~~~

Review all proposed mappings manually before freezing a source adapter.

## 2. Data quality, missingness, and temporal QA

Use the dedicated modules for:
- schema and type validation;
- missingness summaries and handling;
- duplicate and uniqueness checks;
- temporal ordering and observation windows;
- cross-site harmonisation;
- code-system normalization.

Start with the [new dataset wizard](../new-dataset/README.md), then use notebooks 01–09 for the complete sequence.

## 3. Medication exposure and claims

~~~python
import pandas as pd

from thomaslab.drugs import build_exposure_episodes

claims = pd.DataFrame(
    {
        "patient_id": ["P001", "P001", "P002"],
        "drug": ["clopidogrel", "clopidogrel", "ticagrelor"],
        "fill_date": pd.to_datetime(["2026-01-01", "2026-01-30", "2026-01-10"]),
        "days_supply": [30, 30, 30],
    }
)

episodes = build_exposure_episodes(
    claims,
    patient_col="patient_id",
    drug_col="drug",
    date_col="fill_date",
    days_supply_col="days_supply",
)

print(episodes)
~~~

Confirm medication identifiers, grace periods, stockpiling rules, switching, discontinuation, and follow-up definitions before analysis.

## 4. Pharmacogenomics

~~~python
from thomaslab.pgx_cyp2c19 import translate_cyp2c19_diplotype

result = translate_cyp2c19_diplotype("*1/*2")
print(result)
~~~

For production research, additionally record assay coverage, allele nomenclature version, guideline/knowledge-source version, unresolved calls, phenoconversion rules, indication, and medication context.

## 5. Clinical NLP

~~~python
from thomaslab.nlp_context import classify_clinical_mentions

text = """
Assessment:
No evidence of active bleeding.
History of gastrointestinal bleeding in 2024.
"""

mentions = classify_clinical_mentions(
    text,
    target_terms=["bleeding"],
    window_tokens=10,
)

print(mentions)
~~~

Validate negation, temporality, section handling, abbreviations, medication extraction, and phenotype performance on study-appropriate labeled notes.

## 6. Prediction and evaluation

~~~python
import numpy as np

from thomaslab.eval import calculate_clinical_metrics

y_true = np.array([0, 1, 0, 1, 1, 0])
y_probability = np.array([0.10, 0.82, 0.25, 0.74, 0.67, 0.31])

metrics = calculate_clinical_metrics(
    y_true,
    y_probability,
    threshold=0.5,
)

print(metrics)
~~~

Use patient/site/time-safe splits, preserve a genuinely untouched test set, assess calibration and uncertainty, and label external validation only when the source is genuinely independent.

## 7. Longitudinal tensors and deep models

~~~python
import pandas as pd

from thomaslab.models import format_time_series_tensor

longitudinal = pd.DataFrame(
    {
        "patient_id": ["P001", "P001", "P002", "P002"],
        "event_date": pd.to_datetime(
            ["2026-01-01", "2026-02-01", "2026-01-05", "2026-02-07"]
        ),
        "feature_a": [1.0, 1.4, 0.7, 0.9],
        "feature_b": [2.0, 2.2, 1.5, 1.7],
    }
)

batch = format_time_series_tensor(
    longitudinal,
    id_col="patient_id",
    time_col="event_date",
    feature_cols=["feature_a", "feature_b"],
    max_seq_len=10,
    standardize=True,
)

print(batch["tensor"].shape)
print(batch["mask"])
print(batch["ids"])
~~~

Do not allow post-outcome measurements or future information into baseline/prediction features.

## 8. Survival and recurrent-event analysis

Define time zero, censoring, event coding, competing risks, recurrent-event policy, and observation horizon before fitting. Use the survival/recurrent/censoring modules and notebooks 29–30.

## 9. Causal inference

~~~python
import pandas as pd

from thomaslab.causal_workflows import estimate_iptw_binary_effects

analysis = pd.DataFrame(
    {
        "treatment": [1, 1, 0, 0, 1, 0],
        "outcome": [1, 0, 0, 1, 1, 0],
        "iptw": [0.9, 1.1, 1.0, 0.95, 1.05, 1.0],
    }
)

effects = estimate_iptw_binary_effects(
    analysis,
    treatment_col="treatment",
    outcome_col="outcome",
    weight_col="iptw",
)

print(effects)
~~~

Successful execution does not establish exchangeability, positivity, consistency, non-interference, correct model specification, or absence of unmeasured confounding.

## 10. Target-trial emulation

Before calling target-trial utilities, explicitly specify:
- eligibility;
- time zero;
- treatment strategies;
- assignment procedure;
- follow-up;
- outcome;
- causal contrast;
- analysis plan;
- switching/discontinuation/grace rules;
- censoring and weighting.

Use notebooks 28 and the target-trial guide.

## 11. Longitudinal causal inference

Use the longitudinal causal, g-formula, and doubly robust modules only after defining the longitudinal data-generating order and time-indexed treatment/confounder/outcome histories. Use notebooks 36–43.

## 12. Transportability and multisite validation

Use site/domain identifiers, source/target definitions, support diagnostics, and explicit target-population assumptions. Do not call an evaluation "external validation" unless the source is genuinely independent.

## 13. Healthcare utilization and economics

Define the perspective, costing year, resource definitions, censoring, inflation/currency assumptions, and follow-up before interpreting HCRU/economic outputs. Use notebooks 30–31.

## 14. Reproducibility and release

~~~python
from thomaslab.study_spec import validate_study_spec
from thomaslab.reproducibility import fingerprint_file
~~~

Keep study specifications, seeds, source fingerprints, software versions, manifests, tables, figures, and checksums together. Use notebooks 56–58 for the stable self-service workflow.

## 15. How to use an individual API page

Every public callable page now contains:

1. Purpose.
2. When to use it.
3. Full signature.
4. Parameter meanings.
5. Input contract.
6. Return type and output guidance.
7. Raises/fail-closed behavior.
8. Scientific guardrails.
9. A synthetic implementation template.
10. Related functions.
11. Related guide/notebook range.
12. Verification/source links.
13. Original source documentation.

The implementation template is a starting point, not a substitute for study-specific validation. When a function requires clinically meaningful columns, codes, units, time windows, treatments, outcomes, or genotype semantics, replace the synthetic values only after those meanings are reviewed.

## 16. Before a collaborator runs a real study

Confirm all of the following:

- source governance and de-identification;
- patient and encounter identity semantics;
- date/time semantics and timezone assumptions;
- coding systems and versions;
- medication and laboratory units;
- cohort eligibility and index-date rules;
- exposure and outcome definitions;
- censoring/follow-up;
- missing-data policy;
- leakage controls;
- train/validation/test separation;
- calibration and uncertainty;
- subgroup/site evaluation;
- causal identification assumptions where relevant;
- external-validation provenance;
- reproducibility bundle and checksums.

If any required meaning is unresolved, stop and resolve it rather than allowing the package to guess.

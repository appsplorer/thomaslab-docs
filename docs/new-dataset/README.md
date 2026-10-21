# New dataset wizard

Use this path whenever a new hospital, registry, claims source, survey, PGx source, note corpus, partner extract, or unfamiliar research table arrives. Notebooks run locally in Jupyter or PyCharm; restricted or identifiable clinical datasets must never be uploaded to Kaggle.

## 1. Preserve the raw source

Do not rename columns or overwrite source values before inspection. Store the source under the institutionally approved governance boundary.

## 2. Inspect before mapping

~~~python
from thomaslab.onboard import inspect_source

report = inspect_source("partner_dataset.csv")
print(report["profile"])
print(report["semantics"])
~~~

Review row count, identifiers, date-like fields, categorical cardinality, missingness, candidate domains, and likely canonical constructs.

## 3. Generate a reviewable adapter bundle

~~~python
from thomaslab.adaptive.source import load_source_raw
from thomaslab.onboard import generate_adapter_bundle

data = load_source_raw("partner_dataset.csv", sample_rows=5000)  # Preview ONLY

paths = generate_adapter_bundle(
    data,
    "work/adapters/partner_v1",
    dataset_name="partner_v1",
    required_columns=["patient_id", "event_date"],
)
print(paths)
~~~

Treat proposed mappings as candidates, not truth.

The loader preserves zero-padded identifiers and NDC strings. `sample_rows` never qualifies an adapter for approval. Existing reviewed YAML files are protected against overwrite: create a new versioned directory to revise a mapping.

## 4. Resolve ambiguity explicitly

Review:

- patient identifiers;
- encounter and event dates;
- medication identifiers;
- diagnosis/procedure vocabularies;
- laboratory names and units;
- genotype/assay representation;
- site identifiers;
- outcome definitions;
- censoring/follow-up fields.

If a meaning cannot be established, leave it unresolved and fail closed.

## 5. Validate contracts and timing

Run a complete-source check before approval; it must validate every row and have zero skipped records:

~~~python
from thomaslab.onboard import DatasetOnboarder

ob = DatasetOnboarder("partner_dataset.csv")
ob.generate("work/adapters/partner_v2", dataset_name="partner_v2")
full_report = ob.validate(full_dataset=True)
assert full_report.passed, full_report.to_dict()
~~~

This is structural data validation only. Resolve date interpretations, unit conversions, vocabularies and clinical definitions separately. Use `propose_column_mappings` and `review_column_mapping` from `thomaslab.adaptive.mappings` to record a named review for every mapping. A second named review through `DatasetOnboarder.freeze(..., reviewer=..., rationale=..., full_validation=..., reviewed_mappings=..., owner=..., source_institution=..., dataset_grain=..., data_classification=...)` creates an immutable approved registry revision. The original `register_dataset_adapter` shortcut is disabled because it could freeze unreviewed artifacts.

## 6. Freeze the study specification

Write the study question, population, index date, eligibility, baseline, exposure, outcome, follow-up, censoring, analysis, and validation plan in a versioned study specification.

## 7. Construct the analysis dataset

Use explicit windows and auditable provenance. Never allow post-outcome or future information into baseline features.

## 8. Split safely

Choose patient-, site-, group-, or time-aware splitting according to the scientific design. Run leakage checks before model fitting.

## 9. Select the analysis lane

Use the appropriate workflow:

- prediction / calibration;
- survival / competing risks;
- causal inference;
- target trial;
- medication safety;
- PGx / precision medicine;
- clinical NLP;
- healthcare utilization / economics.

## 10. Validate and bundle

Quantify uncertainty, site/subgroup behavior, calibration, sensitivity analyses, and genuinely independent external validation where the claim requires it. Export fingerprints, provenance, manifests, tables, figures, and a checksummed research bundle.

## Stop conditions

Do not proceed automatically when:

- the patient identifier is ambiguous;
- units are unknown;
- temporal order is unclear;
- outcome semantics are unresolved;
- genotype/assay interpretation is unsupported;
- a local code system has no reviewed mapping;
- leakage cannot be excluded;
- the target population differs materially without a transportability assessment.

These are scientific review gates, not software errors.

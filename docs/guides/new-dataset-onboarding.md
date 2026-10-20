# Onboarding a completely new dataset

Use this workflow when a new hospital, registry, claims partner, research collaborator, or vendor delivers a dataset whose column names and conventions have not previously been seen by `thomaslab-core`.

The goal is **not** to guess everything automatically. The goal is to automate high-confidence work, surface ambiguity, record human decisions once, and freeze those decisions as a reusable adapter.

## Recommended workflow

```text
raw source
   ↓
inspect source
   ↓
suggest schema/domain/unit/vocabulary candidates
   ↓
review ambiguity
   ↓
generate schema.yaml + contract.yaml
   ↓
inspect every mapping with a named clinical reviewer
   ↓
validate ALL source rows (not sample only)
   ↓
freeze versioned adapter
   ↓
clean/phenotype/cohort/analyse
```

## 1. Inspect

```python
from thomaslab.onboard import DatasetOnboarder

ob = DatasetOnboarder("partner_hospital.csv")
inspection = ob.inspect()

inspection["profile"]["columns"]
inspection["semantics"]
inspection["domain_ranking"]
```

The inspection stage uses names, dtypes and redacted sample descriptors. CSV and TSV values are loaded text-first so leading zeros survive. It is a structural aid only; it does not establish clinical meaning. Restricted files belong in approved institutional storage, never Kaggle.

## 2. Generate an adapter bundle

```python
bundle = ob.generate(
    "work/adapters/site_a",
    dataset_name="site_a_pci",
    required_columns=["patient_id", "age", "event_date"],
)
```

This creates:

```text
schema.yaml
contract.yaml
```

Review `schema.yaml` before validating. Ambiguous or unresolved required variables must be resolved by someone who understands the source data. A second `generate()` call against the same path refuses to overwrite the original; request a new revision instead.

## 3. Validate

```python
result = ob.validate(
    required_columns=["patient_id", "age", "event_date"],
    strict=True,
)
```

Strict mode stops on unresolved required columns or contract failures. Do not weaken strict mode simply to make a dataset pass.

This preview is not sufficient to approve a source. Run the complete scan separately:

```python
full_report = ob.validate(full_dataset=True)
print(full_report.to_dict())  # Redacted validation summary
assert full_report.passed
```

The complete scan checks late rows, format errors, duplicate keys across chunks and resource limits. It returns `passed=False` when a scan is incomplete.

## 4. Freeze the reviewed adapter

```python
from thomaslab.adaptive.mappings import propose_column_mappings, review_column_mapping

suggestions = propose_column_mappings(ob.data, "person")  # Choose correct domain
# Inspect each candidate's confidence, alternatives, source documentation and units.
reviewed = [
    review_column_mapping(candidate, target=candidate.target, unit=None,
                          reviewer="Named clinical reviewer",
                          rationale="Reviewed against local data dictionary")
    for candidate in suggestions
    if candidate.source_column is not None and candidate.target is not None
]

ob.freeze(
    "adapters", dataset_name="site_a_pci", version="1.0.0",
    reviewer="Named PI", rationale="Verified study grain and variable semantics",
    full_validation=full_report, reviewed_mappings=reviewed,
    owner="Research lead", source_institution="Site A",
    dataset_grain="person", data_classification="restricted",
)
```

The resulting adapter is versioned and immutable. A changed source institution, grain or schema requires a new reviewed version. The example is a scaffold: only include mappings actually approved by the reviewer, and configure the site-approved storage and permissions before using restricted data.

## Code-vocabulary suggestions

`infer_code_vocabulary()` looks only at code shape. It can recognize patterns resembling ICD-10-CM, LOINC or NDC, but numeric identifiers are deliberately treated conservatively because RxNorm, SNOMED CT, local concepts and other systems overlap in representation.

Never convert a suggestion into an authoritative vocabulary assignment without source documentation or a verified terminology mapping.

## Unit suggestions

`suggest_unit_mapping()` reports which units occur for each measure. It does not guess a target unit or silently convert molecular measurements.

This is especially important for clinical laboratories, where the correct conversion depends on the analyte.

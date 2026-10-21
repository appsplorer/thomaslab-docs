# thomaslab.precision

Precision-medicine integration utilities.

The module combines already-cleaned canonical domains into auditable patient-level
research datasets. It does not infer clinical meaning or prescribing decisions.

## Research-use boundary

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

## Self-service orientation

- Related guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 8

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.precision.PrecisionPatient.to_dict -->
## PrecisionPatient.to_dict

### Purpose

Return a plain nested dictionary.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def to_dict(self) -> dict[str, Any]
~~~

### Parameters

This callable has no public parameters beyond instance/class binding.

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- This callable has no required public arguments beyond instance/class construction.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.precision import PrecisionPatient

# Construct PrecisionPatient with its documented constructor first.
# instance = PrecisionPatient(...)
result = instance.to_dict()

print(result)
~~~

### Related functions

- `build_precision_patient`
- `merge_patient_domains`
- `aggregate_patient_events`
- `build_precision_dataset`
- `evaluate_gene_drug_context`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/precision.py#L29`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/precision.py#L29)
- Repository search: [PrecisionPatient.to_dict](https://github.com/appsplorer/thomaslab-core/search?q=PrecisionPatient.to_dict&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return a plain nested dictionary.

### API inspection

~~~python
import inspect
from thomaslab.precision import PrecisionPatient

print(inspect.signature(PrecisionPatient.to_dict))
print(PrecisionPatient.to_dict.__doc__)
~~~

### Source

[`src/thomaslab/precision.py#L29`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/precision.py#L29)

---

<!-- callable:thomaslab.precision.build_precision_patient -->
## build_precision_patient

### Purpose

Build a patient-centric object without changing supplied clinical values.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_precision_patient( patient_id: Any, *, demographics: Mapping[str, Any] | None = None, clinical: Mapping[str, Any] | None = None, pgx: Mapping[str, Any] | None = None, medications: Mapping[str, Any] | None = None, outcomes: Mapping[str, Any] | None = None, metadata: Mapping[str, Any] | None = None, ) -> PrecisionPatient
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `patient_id` | `patient_id: Any` | Yes | Identifier or identifier column. Confirm uniqueness/grouping semantics before analysis. |
| `demographics` | `demographics: Mapping[str, Any] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `clinical` | `clinical: Mapping[str, Any] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `pgx` | `pgx: Mapping[str, Any] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `medications` | `medications: Mapping[str, Any] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `outcomes` | `outcomes: Mapping[str, Any] \| None = None` | No | Outcome/event definition supplied by the study specification; validate timing and endpoint semantics. |
| `metadata` | `metadata: Mapping[str, Any] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `patient_id`.

### Returns

`PrecisionPatient`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
sample_value = "replace_with_validated_value"

from thomaslab.precision import build_precision_patient

result = build_precision_patient(
    patient_id=sample_value
)

print(result)
~~~

### Related functions

- `PrecisionPatient.to_dict`
- `merge_patient_domains`
- `aggregate_patient_events`
- `build_precision_dataset`
- `evaluate_gene_drug_context`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/precision.py#L51`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/precision.py#L51)
- Repository search: [build_precision_patient](https://github.com/appsplorer/thomaslab-core/search?q=build_precision_patient&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build a patient-centric object without changing supplied clinical values.

### API inspection

~~~python
import inspect
from thomaslab.precision import build_precision_patient

print(inspect.signature(build_precision_patient))
print(build_precision_patient.__doc__)
~~~

### Source

[`src/thomaslab/precision.py#L51`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/precision.py#L51)

---

<!-- callable:thomaslab.precision.merge_patient_domains -->
## merge_patient_domains

### Purpose

Merge one-row-per-patient canonical domains with collision protection.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def merge_patient_domains( domains: Mapping[str, pd.DataFrame], *, patient_col: str = "patient_id", how: str = "outer", prefixes: bool = True, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `domains` | `domains: Mapping[str, pd.DataFrame]` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `how` | `how: str = 'outer'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `prefixes` | `prefixes: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `domains`.
- Referenced columns must exist in the input table: `patient_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_df = pd.DataFrame(
    {
        "patient_id": ["P001", "P001", "P002", "P002"],
        "event_date": pd.to_datetime(["2026-01-01", "2026-02-01", "2026-01-05", "2026-02-07"]),
        "treatment": [1, 1, 0, 0],
        "outcome": [0, 1, 0, 0],
        "event": [0, 1, 0, 0],
        "duration": [31.0, 62.0, 33.0, 66.0],
        "weight": [1.0, 0.9, 1.1, 1.0],
        "propensity": [0.70, 0.65, 0.35, 0.30],
        "site": ["A", "A", "B", "B"],
        "feature_a": [1.0, 1.4, 0.7, 0.9],
        "feature_b": [2.0, 2.2, 1.5, 1.7],
    }
)

from thomaslab.precision import merge_patient_domains

result = merge_patient_domains(
    domains=sample_df
)

print(result)
~~~

### Related functions

- `PrecisionPatient.to_dict`
- `build_precision_patient`
- `aggregate_patient_events`
- `build_precision_dataset`
- `evaluate_gene_drug_context`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/precision.py#L75`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/precision.py#L75)
- Repository search: [merge_patient_domains](https://github.com/appsplorer/thomaslab-core/search?q=merge_patient_domains&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Merge one-row-per-patient canonical domains with collision protection.

Parameters
----------
domains:
    Mapping from domain name to a patient-level DataFrame.
prefixes:
    Prefix non-key columns with ``<domain>__``. This is recommended because
    it prevents silent collisions such as multiple ``site_id`` variables.

### API inspection

~~~python
import inspect
from thomaslab.precision import merge_patient_domains

print(inspect.signature(merge_patient_domains))
print(merge_patient_domains.__doc__)
~~~

### Source

[`src/thomaslab/precision.py#L75`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/precision.py#L75)

---

<!-- callable:thomaslab.precision.aggregate_patient_events -->
## aggregate_patient_events

### Purpose

Aggregate repeated patient events to count/first/last summaries.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def aggregate_patient_events( events: pd.DataFrame, *, patient_col: str, value_col: str, date_col: str | None = None, prefix: str = "event", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `value_col` | `value_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `prefix` | `prefix: str = 'event'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`, `patient_col`, `value_col`.
- Referenced columns must exist in the input table: `patient_col`, `value_col`, `date_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_df = pd.DataFrame(
    {
        "patient_id": ["P001", "P001", "P002", "P002"],
        "event_date": pd.to_datetime(["2026-01-01", "2026-02-01", "2026-01-05", "2026-02-07"]),
        "treatment": [1, 1, 0, 0],
        "outcome": [0, 1, 0, 0],
        "event": [0, 1, 0, 0],
        "duration": [31.0, 62.0, 33.0, 66.0],
        "weight": [1.0, 0.9, 1.1, 1.0],
        "propensity": [0.70, 0.65, 0.35, 0.30],
        "site": ["A", "A", "B", "B"],
        "feature_a": [1.0, 1.4, 0.7, 0.9],
        "feature_b": [2.0, 2.2, 1.5, 1.7],
    }
)

from thomaslab.precision import aggregate_patient_events

result = aggregate_patient_events(
    events=sample_df,
    patient_col='patient_id',
    value_col='value'
)

print(result)
~~~

### Related functions

- `PrecisionPatient.to_dict`
- `build_precision_patient`
- `merge_patient_domains`
- `build_precision_dataset`
- `evaluate_gene_drug_context`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/precision.py#L118`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/precision.py#L118)
- Repository search: [aggregate_patient_events](https://github.com/appsplorer/thomaslab-core/search?q=aggregate_patient_events&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Aggregate repeated patient events to count/first/last summaries.

### API inspection

~~~python
import inspect
from thomaslab.precision import aggregate_patient_events

print(inspect.signature(aggregate_patient_events))
print(aggregate_patient_events.__doc__)
~~~

### Source

[`src/thomaslab/precision.py#L118`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/precision.py#L118)

---

<!-- callable:thomaslab.precision.build_precision_dataset -->
## build_precision_dataset

### Purpose

Build a prefixed one-row-per-patient precision-medicine analysis table.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_precision_dataset( person: pd.DataFrame, *, pgx_results: pd.DataFrame | None = None, clinical_features: pd.DataFrame | None = None, medication_summary: pd.DataFrame | None = None, outcome_summary: pd.DataFrame | None = None, patient_col: str = "patient_id", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `person` | `person: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `pgx_results` | `pgx_results: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `clinical_features` | `clinical_features: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `medication_summary` | `medication_summary: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `outcome_summary` | `outcome_summary: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `person`.
- Referenced columns must exist in the input table: `patient_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_df = pd.DataFrame(
    {
        "patient_id": ["P001", "P001", "P002", "P002"],
        "event_date": pd.to_datetime(["2026-01-01", "2026-02-01", "2026-01-05", "2026-02-07"]),
        "treatment": [1, 1, 0, 0],
        "outcome": [0, 1, 0, 0],
        "event": [0, 1, 0, 0],
        "duration": [31.0, 62.0, 33.0, 66.0],
        "weight": [1.0, 0.9, 1.1, 1.0],
        "propensity": [0.70, 0.65, 0.35, 0.30],
        "site": ["A", "A", "B", "B"],
        "feature_a": [1.0, 1.4, 0.7, 0.9],
        "feature_b": [2.0, 2.2, 1.5, 1.7],
    }
)

from thomaslab.precision import build_precision_dataset

result = build_precision_dataset(
    person=sample_df
)

print(result)
~~~

### Related functions

- `PrecisionPatient.to_dict`
- `build_precision_patient`
- `merge_patient_domains`
- `aggregate_patient_events`
- `evaluate_gene_drug_context`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/precision.py#L145`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/precision.py#L145)
- Repository search: [build_precision_dataset](https://github.com/appsplorer/thomaslab-core/search?q=build_precision_dataset&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build a prefixed one-row-per-patient precision-medicine analysis table.

### API inspection

~~~python
import inspect
from thomaslab.precision import build_precision_dataset

print(inspect.signature(build_precision_dataset))
print(build_precision_dataset.__doc__)
~~~

### Source

[`src/thomaslab/precision.py#L145`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/precision.py#L145)

---

<!-- callable:thomaslab.precision.evaluate_gene_drug_context -->
## evaluate_gene_drug_context

### Purpose

Attach the matching versioned PGx research rule to each row.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def evaluate_gene_drug_context( df: pd.DataFrame, knowledge: Mapping[str, Any] | str, *, gene: str, phenotype_col: str, drug_col: str, indication_col: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `knowledge` | `knowledge: Mapping[str, Any] \| str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `gene` | `gene: str` | Yes | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |
| `phenotype_col` | `phenotype_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `indication_col` | `indication_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `knowledge`, `gene`, `phenotype_col`, `drug_col`.
- Referenced columns must exist in the input table: `phenotype_col`, `drug_col`, `indication_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_df = pd.DataFrame(
    {
        "patient_id": ["P001", "P001", "P002", "P002"],
        "event_date": pd.to_datetime(["2026-01-01", "2026-02-01", "2026-01-05", "2026-02-07"]),
        "treatment": [1, 1, 0, 0],
        "outcome": [0, 1, 0, 0],
        "event": [0, 1, 0, 0],
        "duration": [31.0, 62.0, 33.0, 66.0],
        "weight": [1.0, 0.9, 1.1, 1.0],
        "propensity": [0.70, 0.65, 0.35, 0.30],
        "site": ["A", "A", "B", "B"],
        "feature_a": [1.0, 1.4, 0.7, 0.9],
        "feature_b": [2.0, 2.2, 1.5, 1.7],
    }
)

from thomaslab.precision import evaluate_gene_drug_context

result = evaluate_gene_drug_context(
    df=sample_df,
    knowledge={},
    gene="CYP2C19",
    phenotype_col='phenotype',
    drug_col='drug'
)

print(result)
~~~

### Related functions

- `PrecisionPatient.to_dict`
- `build_precision_patient`
- `merge_patient_domains`
- `aggregate_patient_events`
- `build_precision_dataset`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/precision.py#L169`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/precision.py#L169)
- Repository search: [evaluate_gene_drug_context](https://github.com/appsplorer/thomaslab-core/search?q=evaluate_gene_drug_context&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Attach the matching versioned PGx research rule to each row.

This is a research-annotation helper and does not make treatment decisions.

### API inspection

~~~python
import inspect
from thomaslab.precision import evaluate_gene_drug_context

print(inspect.signature(evaluate_gene_drug_context))
print(evaluate_gene_drug_context.__doc__)
~~~

### Source

[`src/thomaslab/precision.py#L169`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/precision.py#L169)

---

<!-- callable:thomaslab.precision.summarize_precision_cohort -->
## summarize_precision_cohort

### Purpose

Generate a compact auditable summary of a precision-medicine cohort.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_precision_cohort( df: pd.DataFrame, *, patient_col: str = "patient_id", gene_col: str | None = None, phenotype_col: str | None = None, drug_col: str | None = None, outcome_col: str | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `gene_col` | `gene_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `phenotype_col` | `phenotype_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.
- Referenced columns must exist in the input table: `patient_col`, `gene_col`, `phenotype_col`, `drug_col`, `outcome_col`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_df = pd.DataFrame(
    {
        "patient_id": ["P001", "P001", "P002", "P002"],
        "event_date": pd.to_datetime(["2026-01-01", "2026-02-01", "2026-01-05", "2026-02-07"]),
        "treatment": [1, 1, 0, 0],
        "outcome": [0, 1, 0, 0],
        "event": [0, 1, 0, 0],
        "duration": [31.0, 62.0, 33.0, 66.0],
        "weight": [1.0, 0.9, 1.1, 1.0],
        "propensity": [0.70, 0.65, 0.35, 0.30],
        "site": ["A", "A", "B", "B"],
        "feature_a": [1.0, 1.4, 0.7, 0.9],
        "feature_b": [2.0, 2.2, 1.5, 1.7],
    }
)

from thomaslab.precision import summarize_precision_cohort

result = summarize_precision_cohort(
    df=sample_df
)

print(result)
~~~

### Related functions

- `PrecisionPatient.to_dict`
- `build_precision_patient`
- `merge_patient_domains`
- `aggregate_patient_events`
- `build_precision_dataset`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/precision.py#L213`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/precision.py#L213)
- Repository search: [summarize_precision_cohort](https://github.com/appsplorer/thomaslab-core/search?q=summarize_precision_cohort&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Generate a compact auditable summary of a precision-medicine cohort.

### API inspection

~~~python
import inspect
from thomaslab.precision import summarize_precision_cohort

print(inspect.signature(summarize_precision_cohort))
print(summarize_precision_cohort.__doc__)
~~~

### Source

[`src/thomaslab/precision.py#L213`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/precision.py#L213)

---

<!-- callable:thomaslab.precision.generate_precision_report -->
## generate_precision_report

### Purpose

Return cohort summary plus missingness and duplicate-patient diagnostics.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def generate_precision_report( df: pd.DataFrame, *, patient_col: str = "patient_id", gene_col: str | None = None, phenotype_col: str | None = None, drug_col: str | None = None, outcome_col: str | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `gene_col` | `gene_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `phenotype_col` | `phenotype_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `outcome_col` | `outcome_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.
- Referenced columns must exist in the input table: `patient_col`, `gene_col`, `phenotype_col`, `drug_col`, `outcome_col`.

### Returns

`dict[str, Any]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_df = pd.DataFrame(
    {
        "patient_id": ["P001", "P001", "P002", "P002"],
        "event_date": pd.to_datetime(["2026-01-01", "2026-02-01", "2026-01-05", "2026-02-07"]),
        "treatment": [1, 1, 0, 0],
        "outcome": [0, 1, 0, 0],
        "event": [0, 1, 0, 0],
        "duration": [31.0, 62.0, 33.0, 66.0],
        "weight": [1.0, 0.9, 1.1, 1.0],
        "propensity": [0.70, 0.65, 0.35, 0.30],
        "site": ["A", "A", "B", "B"],
        "feature_a": [1.0, 1.4, 0.7, 0.9],
        "feature_b": [2.0, 2.2, 1.5, 1.7],
    }
)

from thomaslab.precision import generate_precision_report

result = generate_precision_report(
    df=sample_df
)

print(result)
~~~

### Related functions

- `PrecisionPatient.to_dict`
- `build_precision_patient`
- `merge_patient_domains`
- `aggregate_patient_events`
- `build_precision_dataset`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/precision.py#L247`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/precision.py#L247)
- Repository search: [generate_precision_report](https://github.com/appsplorer/thomaslab-core/search?q=generate_precision_report&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return cohort summary plus missingness and duplicate-patient diagnostics.

### API inspection

~~~python
import inspect
from thomaslab.precision import generate_precision_report

print(inspect.signature(generate_precision_report))
print(generate_precision_report.__doc__)
~~~

### Source

[`src/thomaslab/precision.py#L247`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/precision.py#L247)

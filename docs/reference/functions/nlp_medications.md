# thomaslab.nlp_medications

Medication and adverse-event extraction from clinical narrative.

These functions are target-driven and auditable. Medication vocabularies and reason
lexicons are expected to be study-reviewed; lexical matching is not a replacement for
RxNorm normalization, medication reconciliation, or chart adjudication.

## Research-use boundary

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

## Self-service orientation

- Related guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 4

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.nlp_medications.load_medication_reason_lexicon -->
## load_medication_reason_lexicon

### Purpose

Load a reviewed medication-change reason lexicon.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def load_medication_reason_lexicon(source: str | Path | Mapping[str, Any]) -> dict[str, list[str]]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `source` | `source: str \| Path \| Mapping[str, Any]` | Yes | Input source/path accepted by this callable. Keep raw-source provenance and do not overwrite the source. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `source`.

### Returns

`dict[str, list[str]]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

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

from thomaslab.nlp_medications import load_medication_reason_lexicon

result = load_medication_reason_lexicon(
    source=sample_df
)

print(result)
~~~

### Related functions

- `extract_medication_mentions`
- `extract_adverse_drug_events`
- `extract_medication_change_reasons`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp_medications.py#L30`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_medications.py#L30)
- Repository search: [load_medication_reason_lexicon](https://github.com/appsplorer/thomaslab-core/search?q=load_medication_reason_lexicon&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Load a reviewed medication-change reason lexicon.

### API inspection

~~~python
import inspect
from thomaslab.nlp_medications import load_medication_reason_lexicon

print(inspect.signature(load_medication_reason_lexicon))
print(load_medication_reason_lexicon.__doc__)
~~~

### Source

[`src/thomaslab/nlp_medications.py#L30`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_medications.py#L30)

---

<!-- callable:thomaslab.nlp_medications.extract_medication_mentions -->
## extract_medication_mentions

### Purpose

Extract target medication mentions with context, dose, and frequency snippets.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def extract_medication_mentions( notes: pd.DataFrame, medication_terms: Iterable[str], *, text_col: str = "note_text", note_id_col: str | None = "note_id", patient_col: str | None = "patient_id", date_col: str | None = "event_date", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `notes` | `notes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `medication_terms` | `medication_terms: Iterable[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `text_col` | `text_col: str = 'note_text'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `note_id_col` | `note_id_col: str \| None = 'note_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `patient_col` | `patient_col: str \| None = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str \| None = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `notes`, `medication_terms`.
- Referenced columns must exist in the input table: `text_col`, `note_id_col`, `patient_col`, `date_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

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

from thomaslab.nlp_medications import extract_medication_mentions

result = extract_medication_mentions(
    notes=sample_df,
    medication_terms="value"
)

print(result)
~~~

### Related functions

- `load_medication_reason_lexicon`
- `extract_adverse_drug_events`
- `extract_medication_change_reasons`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp_medications.py#L76`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_medications.py#L76)
- Repository search: [extract_medication_mentions](https://github.com/appsplorer/thomaslab-core/search?q=extract_medication_mentions&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Extract target medication mentions with context, dose, and frequency snippets.

### API inspection

~~~python
import inspect
from thomaslab.nlp_medications import extract_medication_mentions

print(inspect.signature(extract_medication_mentions))
print(extract_medication_mentions.__doc__)
~~~

### Source

[`src/thomaslab/nlp_medications.py#L76`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_medications.py#L76)

---

<!-- callable:thomaslab.nlp_medications.extract_adverse_drug_events -->
## extract_adverse_drug_events

### Purpose

Extract contextualized adverse-event mentions and nearest same-sentence medication.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def extract_adverse_drug_events( notes: pd.DataFrame, adverse_terms: Iterable[str], *, medication_terms: Iterable[str] | None = None, text_col: str = "note_text", patient_col: str | None = "patient_id", note_id_col: str | None = "note_id", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `notes` | `notes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `adverse_terms` | `adverse_terms: Iterable[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `medication_terms` | `medication_terms: Iterable[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `text_col` | `text_col: str = 'note_text'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `patient_col` | `patient_col: str \| None = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `note_id_col` | `note_id_col: str \| None = 'note_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `notes`, `adverse_terms`.
- Referenced columns must exist in the input table: `text_col`, `patient_col`, `note_id_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

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

from thomaslab.nlp_medications import extract_adverse_drug_events

result = extract_adverse_drug_events(
    notes=sample_df,
    adverse_terms="value"
)

print(result)
~~~

### Related functions

- `load_medication_reason_lexicon`
- `extract_medication_mentions`
- `extract_medication_change_reasons`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp_medications.py#L104`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_medications.py#L104)
- Repository search: [extract_adverse_drug_events](https://github.com/appsplorer/thomaslab-core/search?q=extract_adverse_drug_events&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Extract contextualized adverse-event mentions and nearest same-sentence medication.

### API inspection

~~~python
import inspect
from thomaslab.nlp_medications import extract_adverse_drug_events

print(inspect.signature(extract_adverse_drug_events))
print(extract_adverse_drug_events.__doc__)
~~~

### Source

[`src/thomaslab/nlp_medications.py#L104`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_medications.py#L104)

---

<!-- callable:thomaslab.nlp_medications.extract_medication_change_reasons -->
## extract_medication_change_reasons

### Purpose

Extract medication changes and study-reviewed reason categories from sentences.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def extract_medication_change_reasons( notes: pd.DataFrame, medication_terms: Iterable[str], *, reason_lexicon: str | Path | Mapping[str, Any] | None = None, action_cues: Mapping[str, Iterable[str]] | None = None, text_col: str = "note_text", patient_col: str | None = "patient_id", note_id_col: str | None = "note_id", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `notes` | `notes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `medication_terms` | `medication_terms: Iterable[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `reason_lexicon` | `reason_lexicon: str \| Path \| Mapping[str, Any] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `action_cues` | `action_cues: Mapping[str, Iterable[str]] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `text_col` | `text_col: str = 'note_text'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `patient_col` | `patient_col: str \| None = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `note_id_col` | `note_id_col: str \| None = 'note_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `notes`, `medication_terms`.
- Referenced columns must exist in the input table: `text_col`, `patient_col`, `note_id_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

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

from thomaslab.nlp_medications import extract_medication_change_reasons

result = extract_medication_change_reasons(
    notes=sample_df,
    medication_terms="value"
)

print(result)
~~~

### Related functions

- `load_medication_reason_lexicon`
- `extract_medication_mentions`
- `extract_adverse_drug_events`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp_medications.py#L145`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_medications.py#L145)
- Repository search: [extract_medication_change_reasons](https://github.com/appsplorer/thomaslab-core/search?q=extract_medication_change_reasons&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Extract medication changes and study-reviewed reason categories from sentences.

### API inspection

~~~python
import inspect
from thomaslab.nlp_medications import extract_medication_change_reasons

print(inspect.signature(extract_medication_change_reasons))
print(extract_medication_change_reasons.__doc__)
~~~

### Source

[`src/thomaslab/nlp_medications.py#L145`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_medications.py#L145)

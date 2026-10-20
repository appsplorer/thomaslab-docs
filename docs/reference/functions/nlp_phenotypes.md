# thomaslab.nlp_phenotypes

Configurable phenotype-oriented NLP extraction for clinical notes.

## Research-use boundary

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

## Self-service orientation

- Related guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 8

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.nlp_phenotypes.load_phenotype_lexicon -->
## load_phenotype_lexicon

### Purpose

Load a phenotype NLP lexicon from YAML or a mapping.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def load_phenotype_lexicon(source: str | Path | Mapping[str, Any]) -> dict[str, Any]
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

`dict[str, Any]`

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

from thomaslab.nlp_phenotypes import load_phenotype_lexicon

result = load_phenotype_lexicon(
    source=sample_df
)

print(result)
~~~

### Related functions

- `extract_contextual_phenotype_mentions`
- `aggregate_note_phenotype`
- `extract_bleeding_mentions`
- `extract_mi_mentions`
- `extract_stroke_mentions`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp_phenotypes.py#L15`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_phenotypes.py#L15)
- Repository search: [load_phenotype_lexicon](https://github.com/appsplorer/thomaslab-core/search?q=load_phenotype_lexicon&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Load a phenotype NLP lexicon from YAML or a mapping.

### API inspection

~~~python
import inspect
from thomaslab.nlp_phenotypes import load_phenotype_lexicon

print(inspect.signature(load_phenotype_lexicon))
print(load_phenotype_lexicon.__doc__)
~~~

### Source

[`src/thomaslab/nlp_phenotypes.py#L15`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_phenotypes.py#L15)

---

<!-- callable:thomaslab.nlp_phenotypes.extract_contextual_phenotype_mentions -->
## extract_contextual_phenotype_mentions

### Purpose

Extract phenotype mentions with contextual inclusion flags.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def extract_contextual_phenotype_mentions( notes: pd.DataFrame, lexicon: str | Path | Mapping[str, Any], *, text_col: str = "note_text", patient_col: str = "patient_id", note_id_col: str | None = "note_id", date_col: str | None = "event_date", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `notes` | `notes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `lexicon` | `lexicon: str \| Path \| Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `text_col` | `text_col: str = 'note_text'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `note_id_col` | `note_id_col: str \| None = 'note_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str \| None = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `notes`, `lexicon`.
- Referenced columns must exist in the input table: `text_col`, `patient_col`, `note_id_col`, `date_col`.

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

from thomaslab.nlp_phenotypes import extract_contextual_phenotype_mentions

result = extract_contextual_phenotype_mentions(
    notes=sample_df,
    lexicon={}
)

print(result)
~~~

### Related functions

- `load_phenotype_lexicon`
- `aggregate_note_phenotype`
- `extract_bleeding_mentions`
- `extract_mi_mentions`
- `extract_stroke_mentions`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp_phenotypes.py#L39`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_phenotypes.py#L39)
- Repository search: [extract_contextual_phenotype_mentions](https://github.com/appsplorer/thomaslab-core/search?q=extract_contextual_phenotype_mentions&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Extract phenotype mentions with contextual inclusion flags.

### API inspection

~~~python
import inspect
from thomaslab.nlp_phenotypes import extract_contextual_phenotype_mentions

print(inspect.signature(extract_contextual_phenotype_mentions))
print(extract_contextual_phenotype_mentions.__doc__)
~~~

### Source

[`src/thomaslab/nlp_phenotypes.py#L39`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_phenotypes.py#L39)

---

<!-- callable:thomaslab.nlp_phenotypes.aggregate_note_phenotype -->
## aggregate_note_phenotype

### Purpose

Aggregate contextual mention evidence to one phenotype row per patient.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def aggregate_note_phenotype( mentions: pd.DataFrame, *, patient_col: str = "patient_id", date_col: str | None = "event_date", require_included: bool = True, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `mentions` | `mentions: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str \| None = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `require_included` | `require_included: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `mentions`.
- Referenced columns must exist in the input table: `patient_col`, `date_col`.

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

from thomaslab.nlp_phenotypes import aggregate_note_phenotype

result = aggregate_note_phenotype(
    mentions=sample_df
)

print(result)
~~~

### Related functions

- `load_phenotype_lexicon`
- `extract_contextual_phenotype_mentions`
- `extract_bleeding_mentions`
- `extract_mi_mentions`
- `extract_stroke_mentions`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp_phenotypes.py#L83`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_phenotypes.py#L83)
- Repository search: [aggregate_note_phenotype](https://github.com/appsplorer/thomaslab-core/search?q=aggregate_note_phenotype&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Aggregate contextual mention evidence to one phenotype row per patient.

### API inspection

~~~python
import inspect
from thomaslab.nlp_phenotypes import aggregate_note_phenotype

print(inspect.signature(aggregate_note_phenotype))
print(aggregate_note_phenotype.__doc__)
~~~

### Source

[`src/thomaslab/nlp_phenotypes.py#L83`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_phenotypes.py#L83)

---

<!-- callable:thomaslab.nlp_phenotypes.extract_bleeding_mentions -->
## extract_bleeding_mentions

### Purpose

Extract bleeding mentions using a reviewed bleeding lexicon.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def extract_bleeding_mentions( notes: pd.DataFrame, lexicon: str | Path | Mapping[str, Any], **kwargs: Any ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `notes` | `notes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `lexicon` | `lexicon: str \| Path \| Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `kwargs` | `**kwargs: Any` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `notes`, `lexicon`.

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

from thomaslab.nlp_phenotypes import extract_bleeding_mentions

result = extract_bleeding_mentions(
    notes=sample_df,
    lexicon={}
)

print(result)
~~~

### Related functions

- `load_phenotype_lexicon`
- `extract_contextual_phenotype_mentions`
- `aggregate_note_phenotype`
- `extract_mi_mentions`
- `extract_stroke_mentions`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp_phenotypes.py#L125`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_phenotypes.py#L125)
- Repository search: [extract_bleeding_mentions](https://github.com/appsplorer/thomaslab-core/search?q=extract_bleeding_mentions&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Extract bleeding mentions using a reviewed bleeding lexicon.

### API inspection

~~~python
import inspect
from thomaslab.nlp_phenotypes import extract_bleeding_mentions

print(inspect.signature(extract_bleeding_mentions))
print(extract_bleeding_mentions.__doc__)
~~~

### Source

[`src/thomaslab/nlp_phenotypes.py#L125`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_phenotypes.py#L125)

---

<!-- callable:thomaslab.nlp_phenotypes.extract_mi_mentions -->
## extract_mi_mentions

### Purpose

Extract myocardial-infarction mentions using a reviewed lexicon.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def extract_mi_mentions( notes: pd.DataFrame, lexicon: str | Path | Mapping[str, Any], **kwargs: Any ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `notes` | `notes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `lexicon` | `lexicon: str \| Path \| Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `kwargs` | `**kwargs: Any` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `notes`, `lexicon`.

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

from thomaslab.nlp_phenotypes import extract_mi_mentions

result = extract_mi_mentions(
    notes=sample_df,
    lexicon={}
)

print(result)
~~~

### Related functions

- `load_phenotype_lexicon`
- `extract_contextual_phenotype_mentions`
- `aggregate_note_phenotype`
- `extract_bleeding_mentions`
- `extract_stroke_mentions`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp_phenotypes.py#L132`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_phenotypes.py#L132)
- Repository search: [extract_mi_mentions](https://github.com/appsplorer/thomaslab-core/search?q=extract_mi_mentions&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Extract myocardial-infarction mentions using a reviewed lexicon.

### API inspection

~~~python
import inspect
from thomaslab.nlp_phenotypes import extract_mi_mentions

print(inspect.signature(extract_mi_mentions))
print(extract_mi_mentions.__doc__)
~~~

### Source

[`src/thomaslab/nlp_phenotypes.py#L132`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_phenotypes.py#L132)

---

<!-- callable:thomaslab.nlp_phenotypes.extract_stroke_mentions -->
## extract_stroke_mentions

### Purpose

Extract stroke mentions using a reviewed lexicon.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def extract_stroke_mentions( notes: pd.DataFrame, lexicon: str | Path | Mapping[str, Any], **kwargs: Any ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `notes` | `notes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `lexicon` | `lexicon: str \| Path \| Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `kwargs` | `**kwargs: Any` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `notes`, `lexicon`.

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

from thomaslab.nlp_phenotypes import extract_stroke_mentions

result = extract_stroke_mentions(
    notes=sample_df,
    lexicon={}
)

print(result)
~~~

### Related functions

- `load_phenotype_lexicon`
- `extract_contextual_phenotype_mentions`
- `aggregate_note_phenotype`
- `extract_bleeding_mentions`
- `extract_mi_mentions`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp_phenotypes.py#L139`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_phenotypes.py#L139)
- Repository search: [extract_stroke_mentions](https://github.com/appsplorer/thomaslab-core/search?q=extract_stroke_mentions&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Extract stroke mentions using a reviewed lexicon.

### API inspection

~~~python
import inspect
from thomaslab.nlp_phenotypes import extract_stroke_mentions

print(inspect.signature(extract_stroke_mentions))
print(extract_stroke_mentions.__doc__)
~~~

### Source

[`src/thomaslab/nlp_phenotypes.py#L139`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_phenotypes.py#L139)

---

<!-- callable:thomaslab.nlp_phenotypes.extract_acs_mentions -->
## extract_acs_mentions

### Purpose

Extract ACS mentions using a reviewed lexicon.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def extract_acs_mentions( notes: pd.DataFrame, lexicon: str | Path | Mapping[str, Any], **kwargs: Any ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `notes` | `notes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `lexicon` | `lexicon: str \| Path \| Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `kwargs` | `**kwargs: Any` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `notes`, `lexicon`.

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

from thomaslab.nlp_phenotypes import extract_acs_mentions

result = extract_acs_mentions(
    notes=sample_df,
    lexicon={}
)

print(result)
~~~

### Related functions

- `load_phenotype_lexicon`
- `extract_contextual_phenotype_mentions`
- `aggregate_note_phenotype`
- `extract_bleeding_mentions`
- `extract_mi_mentions`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp_phenotypes.py#L146`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_phenotypes.py#L146)
- Repository search: [extract_acs_mentions](https://github.com/appsplorer/thomaslab-core/search?q=extract_acs_mentions&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Extract ACS mentions using a reviewed lexicon.

### API inspection

~~~python
import inspect
from thomaslab.nlp_phenotypes import extract_acs_mentions

print(inspect.signature(extract_acs_mentions))
print(extract_acs_mentions.__doc__)
~~~

### Source

[`src/thomaslab/nlp_phenotypes.py#L146`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_phenotypes.py#L146)

---

<!-- callable:thomaslab.nlp_phenotypes.build_nlp_adjudication_candidates -->
## build_nlp_adjudication_candidates

### Purpose

Return mention rows that merit manual review before phenotype use.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_nlp_adjudication_candidates( mentions: pd.DataFrame, *, include_uncertain: bool = True, include_context_conflicts: bool = True, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `mentions` | `mentions: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `include_uncertain` | `include_uncertain: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `include_context_conflicts` | `include_context_conflicts: bool = True` | No | Clinical text input. Apply governance/de-identification requirements and validate NLP behavior on labeled data. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `mentions`.

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

from thomaslab.nlp_phenotypes import build_nlp_adjudication_candidates

result = build_nlp_adjudication_candidates(
    mentions=sample_df
)

print(result)
~~~

### Related functions

- `load_phenotype_lexicon`
- `extract_contextual_phenotype_mentions`
- `aggregate_note_phenotype`
- `extract_bleeding_mentions`
- `extract_mi_mentions`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp_phenotypes.py#L153`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_phenotypes.py#L153)
- Repository search: [build_nlp_adjudication_candidates](https://github.com/appsplorer/thomaslab-core/search?q=build_nlp_adjudication_candidates&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return mention rows that merit manual review before phenotype use.

### API inspection

~~~python
import inspect
from thomaslab.nlp_phenotypes import build_nlp_adjudication_candidates

print(inspect.signature(build_nlp_adjudication_candidates))
print(build_nlp_adjudication_candidates.__doc__)
~~~

### Source

[`src/thomaslab/nlp_phenotypes.py#L153`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_phenotypes.py#L153)

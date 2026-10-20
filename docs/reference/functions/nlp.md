# thomaslab.nlp

Lightweight clinical NLP utilities with deterministic, auditable rules.

## Research-use boundary

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

## Self-service orientation

- Related guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 7

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.nlp.clean_clinical_text -->
## clean_clinical_text

### Purpose

Remove common note boilerplate/timestamps and normalize whitespace.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def clean_clinical_text(text_series: pd.Series) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `text_series` | `text_series: pd.Series` | Yes | Clinical text input. Apply governance/de-identification requirements and validate NLP behavior on labeled data. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `text_series`.

### Returns

`pd.Series`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.nlp import clean_clinical_text

result = clean_clinical_text(
    text_series=sample_series
)

print(result)
~~~

### Related functions

- `detect_negation`
- `extract_medical_entities`
- `extract_lab_values_from_notes`
- `extract_entities_llm_local`
- `embed_clinical_text_bge`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp.py#L34`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp.py#L34)
- Repository search: [clean_clinical_text](https://github.com/appsplorer/thomaslab-core/search?q=clean_clinical_text&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Remove common note boilerplate/timestamps and normalize whitespace.

### API inspection

~~~python
import inspect
from thomaslab.nlp import clean_clinical_text

print(inspect.signature(clean_clinical_text))
print(clean_clinical_text.__doc__)
~~~

### Source

[`src/thomaslab/nlp.py#L34`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp.py#L34)

---

<!-- callable:thomaslab.nlp.detect_negation -->
## detect_negation

### Purpose

Return True when a target term is negated by a nearby NegEx-style cue.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_negation(text_snippet: str, term: str) -> bool
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `text_snippet` | `text_snippet: str` | Yes | Clinical text input. Apply governance/de-identification requirements and validate NLP behavior on labeled data. |
| `term` | `term: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `text_snippet`, `term`.

### Returns

`bool`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.nlp import detect_negation

result = detect_negation(
    text_snippet="Patient denies active bleeding.",
    term="value"
)

print(result)
~~~

### Related functions

- `clean_clinical_text`
- `extract_medical_entities`
- `extract_lab_values_from_notes`
- `extract_entities_llm_local`
- `embed_clinical_text_bge`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp.py#L53`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp.py#L53)
- Repository search: [detect_negation](https://github.com/appsplorer/thomaslab-core/search?q=detect_negation&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return True when a target term is negated by a nearby NegEx-style cue.

A cue is considered active when it occurs within six tokens before the term and no
termination cue intervenes. This intentionally favors interpretability over opaque NLP.

### API inspection

~~~python
import inspect
from thomaslab.nlp import detect_negation

print(inspect.signature(detect_negation))
print(detect_negation.__doc__)
~~~

### Source

[`src/thomaslab/nlp.py#L53`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp.py#L53)

---

<!-- callable:thomaslab.nlp.extract_medical_entities -->
## extract_medical_entities

### Purpose

Extract non-negated target clinical terms from notes using auditable regex matching.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def extract_medical_entities(text_series: pd.Series, target_terms: list[str]) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `text_series` | `text_series: pd.Series` | Yes | Clinical text input. Apply governance/de-identification requirements and validate NLP behavior on labeled data. |
| `target_terms` | `target_terms: list[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `text_series`, `target_terms`.

### Returns

`pd.Series`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.nlp import extract_medical_entities

result = extract_medical_entities(
    text_series=sample_series,
    target_terms=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `clean_clinical_text`
- `detect_negation`
- `extract_lab_values_from_notes`
- `extract_entities_llm_local`
- `embed_clinical_text_bge`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp.py#L81`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp.py#L81)
- Repository search: [extract_medical_entities](https://github.com/appsplorer/thomaslab-core/search?q=extract_medical_entities&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Extract non-negated target clinical terms from notes using auditable regex matching.

The function is target-driven by design. scispaCy can be layered upstream for open-vocabulary
NER, but deterministic dictionary extraction is preferred when reproducing a published phenotype.

### API inspection

~~~python
import inspect
from thomaslab.nlp import extract_medical_entities

print(inspect.signature(extract_medical_entities))
print(extract_medical_entities.__doc__)
~~~

### Source

[`src/thomaslab/nlp.py#L81`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp.py#L81)

---

<!-- callable:thomaslab.nlp.extract_lab_values_from_notes -->
## extract_lab_values_from_notes

### Purpose

Extract numeric lab/vital values appearing adjacent to a requested label.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def extract_lab_values_from_notes(text_series: pd.Series, lab_name: str) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `text_series` | `text_series: pd.Series` | Yes | Clinical text input. Apply governance/de-identification requirements and validate NLP behavior on labeled data. |
| `lab_name` | `lab_name: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `text_series`, `lab_name`.

### Returns

`pd.Series`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.nlp import extract_lab_values_from_notes

result = extract_lab_values_from_notes(
    text_series=sample_series,
    lab_name="value"
)

print(result)
~~~

### Related functions

- `clean_clinical_text`
- `detect_negation`
- `extract_medical_entities`
- `extract_entities_llm_local`
- `embed_clinical_text_bge`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp.py#L112`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp.py#L112)
- Repository search: [extract_lab_values_from_notes](https://github.com/appsplorer/thomaslab-core/search?q=extract_lab_values_from_notes&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Extract numeric lab/vital values appearing adjacent to a requested label.

Supports scalar values and blood-pressure-like fractions. The return value is a float for
scalar measurements, a ``(systolic, diastolic)`` tuple for ``X/Y`` values, or NaN.

### API inspection

~~~python
import inspect
from thomaslab.nlp import extract_lab_values_from_notes

print(inspect.signature(extract_lab_values_from_notes))
print(extract_lab_values_from_notes.__doc__)
~~~

### Source

[`src/thomaslab/nlp.py#L112`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp.py#L112)

---

<!-- callable:thomaslab.nlp.extract_entities_llm_local -->
## extract_entities_llm_local

### Purpose

Extract structured clinical variables with a local Ollama or vLLM server.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def extract_entities_llm_local( text_series: pd.Series, prompt_template: str, model_name: str = "llama3-clinical", *, backend: str = "ollama", endpoint: str | None = None, timeout: float = 120.0, allow_remote: bool = False, errors: str = "raise", ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `text_series` | `text_series: pd.Series` | Yes | Clinical text input. Apply governance/de-identification requirements and validate NLP behavior on labeled data. |
| `prompt_template` | `prompt_template: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `model_name` | `model_name: str = 'llama3-clinical'` | No | Model or model setting. Fit/tune only within the training design and preserve independent evaluation. |
| `backend` | `backend: str = 'ollama'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `endpoint` | `endpoint: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `timeout` | `timeout: float = 120.0` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |
| `allow_remote` | `allow_remote: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `errors` | `errors: str = 'raise'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `text_series`, `prompt_template`.

### Returns

`pd.Series`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.nlp import extract_entities_llm_local

result = extract_entities_llm_local(
    text_series=sample_series,
    prompt_template="value"
)

print(result)
~~~

### Related functions

- `clean_clinical_text`
- `detect_negation`
- `extract_medical_entities`
- `extract_lab_values_from_notes`
- `embed_clinical_text_bge`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp.py#L154`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp.py#L154)
- Repository search: [extract_entities_llm_local](https://github.com/appsplorer/thomaslab-core/search?q=extract_entities_llm_local&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Extract structured clinical variables with a local Ollama or vLLM server.

``prompt_template`` should normally contain ``{text}``. The model is instructed
through the caller's template and the response must be valid JSON. Remote hosts
are rejected unless ``allow_remote=True`` to reduce accidental PHI disclosure.

### API inspection

~~~python
import inspect
from thomaslab.nlp import extract_entities_llm_local

print(inspect.signature(extract_entities_llm_local))
print(extract_entities_llm_local.__doc__)
~~~

### Source

[`src/thomaslab/nlp.py#L154`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp.py#L154)

---

<!-- callable:thomaslab.nlp.embed_clinical_text_bge -->
## embed_clinical_text_bge

### Purpose

Generate dense local embeddings for clinical notes.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def embed_clinical_text_bge( text_series: pd.Series, model_name: str = "BAAI/bge-m3", *, batch_size: int = 16, device: str | None = None, normalize_embeddings: bool = True, local_files_only: bool = True, ) -> np.ndarray
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `text_series` | `text_series: pd.Series` | Yes | Clinical text input. Apply governance/de-identification requirements and validate NLP behavior on labeled data. |
| `model_name` | `model_name: str = 'BAAI/bge-m3'` | No | Model or model setting. Fit/tune only within the training design and preserve independent evaluation. |
| `batch_size` | `batch_size: int = 16` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `device` | `device: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `normalize_embeddings` | `normalize_embeddings: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `local_files_only` | `local_files_only: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `text_series`.

### Returns

`np.ndarray`

### Output guidance

Returns an array/tensor-like artifact. Verify shape, row/order alignment, masking/padding semantics, dtype, and device where relevant.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.nlp import embed_clinical_text_bge

result = embed_clinical_text_bge(
    text_series=sample_series
)

print(result)
~~~

### Related functions

- `clean_clinical_text`
- `detect_negation`
- `extract_medical_entities`
- `extract_lab_values_from_notes`
- `extract_entities_llm_local`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp.py#L240`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp.py#L240)
- Repository search: [embed_clinical_text_bge](https://github.com/appsplorer/thomaslab-core/search?q=embed_clinical_text_bge&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Generate dense local embeddings for clinical notes.

Sentence-Transformers is used when available; otherwise the function falls back
to mean-pooled Hugging Face Transformers embeddings. ``local_files_only=True``
prevents an accidental model download from clinical compute environments.

### API inspection

~~~python
import inspect
from thomaslab.nlp import embed_clinical_text_bge

print(inspect.signature(embed_clinical_text_bge))
print(embed_clinical_text_bge.__doc__)
~~~

### Source

[`src/thomaslab/nlp.py#L240`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp.py#L240)

---

<!-- callable:thomaslab.nlp.extract_temporal_note_expressions -->
## extract_temporal_note_expressions

### Purpose

Extract relative/absolute temporal expressions from clinical narrative.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def extract_temporal_note_expressions( text_series: pd.Series, *, reference_dates: pd.Series | None = None, ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `text_series` | `text_series: pd.Series` | Yes | Clinical text input. Apply governance/de-identification requirements and validate NLP behavior on labeled data. |
| `reference_dates` | `reference_dates: pd.Series \| None = None` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `text_series`.

### Returns

`pd.Series`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.nlp import extract_temporal_note_expressions

result = extract_temporal_note_expressions(
    text_series=sample_series
)

print(result)
~~~

### Related functions

- `clean_clinical_text`
- `detect_negation`
- `extract_medical_entities`
- `extract_lab_values_from_notes`
- `extract_entities_llm_local`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp.py#L325`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp.py#L325)
- Repository search: [extract_temporal_note_expressions](https://github.com/appsplorer/thomaslab-core/search?q=extract_temporal_note_expressions&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Extract relative/absolute temporal expressions from clinical narrative.

Relative phrases are normalized to day offsets (for example, ``3 days prior``
becomes ``-3``). If ``reference_dates`` is provided, a resolved timestamp is
also returned. Month/year conversions use 30/365-day normalization and are
therefore explicit approximations rather than calendar arithmetic.

### API inspection

~~~python
import inspect
from thomaslab.nlp import extract_temporal_note_expressions

print(inspect.signature(extract_temporal_note_expressions))
print(extract_temporal_note_expressions.__doc__)
~~~

### Source

[`src/thomaslab/nlp.py#L325`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp.py#L325)

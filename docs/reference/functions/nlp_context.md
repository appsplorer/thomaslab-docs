# thomaslab.nlp_context

Auditable clinical-NLP context and note-section utilities.

The functions in this module are deliberately rule-based and configuration-driven.
They support research phenotyping and annotation workflows, but they do not replace
clinical adjudication or establish the truth of a clinical event.

## Research-use boundary

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

## Self-service orientation

- Related guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 6

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.nlp_context.load_nlp_lexicon -->
## load_nlp_lexicon

### Purpose

Load a YAML/dictionary NLP lexicon with minimal structural validation.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def load_nlp_lexicon(source: str | Path | Mapping[str, Any]) -> dict[str, Any]
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

from thomaslab.nlp_context import load_nlp_lexicon

result = load_nlp_lexicon(
    source=sample_df
)

print(result)
~~~

### Related functions

- `split_clinical_sentences`
- `segment_note_sections`
- `extract_note_section`
- `classify_clinical_mentions`
- `summarize_context_mentions`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp_context.py#L111`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_context.py#L111)
- Repository search: [load_nlp_lexicon](https://github.com/appsplorer/thomaslab-core/search?q=load_nlp_lexicon&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Load a YAML/dictionary NLP lexicon with minimal structural validation.

### API inspection

~~~python
import inspect
from thomaslab.nlp_context import load_nlp_lexicon

print(inspect.signature(load_nlp_lexicon))
print(load_nlp_lexicon.__doc__)
~~~

### Source

[`src/thomaslab/nlp_context.py#L111`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_context.py#L111)

---

<!-- callable:thomaslab.nlp_context.split_clinical_sentences -->
## split_clinical_sentences

### Purpose

Split clinical prose conservatively at sentence-like boundaries.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def split_clinical_sentences(text: object) -> list[str]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `text` | `text: object` | Yes | Clinical text input. Apply governance/de-identification requirements and validate NLP behavior on labeled data. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `text`.

### Returns

`list[str]`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.nlp_context import split_clinical_sentences

result = split_clinical_sentences(
    text="Patient denies active bleeding."
)

print(result)
~~~

### Related functions

- `load_nlp_lexicon`
- `segment_note_sections`
- `extract_note_section`
- `classify_clinical_mentions`
- `summarize_context_mentions`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp_context.py#L136`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_context.py#L136)
- Repository search: [split_clinical_sentences](https://github.com/appsplorer/thomaslab-core/search?q=split_clinical_sentences&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Split clinical prose conservatively at sentence-like boundaries.

### API inspection

~~~python
import inspect
from thomaslab.nlp_context import split_clinical_sentences

print(inspect.signature(split_clinical_sentences))
print(split_clinical_sentences.__doc__)
~~~

### Source

[`src/thomaslab/nlp_context.py#L136`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_context.py#L136)

---

<!-- callable:thomaslab.nlp_context.segment_note_sections -->
## segment_note_sections

### Purpose

Segment a clinical note by recognizable line-leading section headers.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def segment_note_sections( text: object, *, section_aliases: Mapping[str, Iterable[str]] | None = None, ) -> list[dict[str, Any]]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `text` | `text: object` | Yes | Clinical text input. Apply governance/de-identification requirements and validate NLP behavior on labeled data. |
| `section_aliases` | `section_aliases: Mapping[str, Iterable[str]] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `text`.

### Returns

`list[dict[str, Any]]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.nlp_context import segment_note_sections

result = segment_note_sections(
    text="Patient denies active bleeding."
)

print(result)
~~~

### Related functions

- `load_nlp_lexicon`
- `split_clinical_sentences`
- `extract_note_section`
- `classify_clinical_mentions`
- `summarize_context_mentions`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp_context.py#L148`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_context.py#L148)
- Repository search: [segment_note_sections](https://github.com/appsplorer/thomaslab-core/search?q=segment_note_sections&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Segment a clinical note by recognizable line-leading section headers.

Unknown text before the first header is assigned to ``preamble``. Header matching
is intentionally conservative; inline words such as "plan" are not treated as a
section unless they occur at a line boundary and resemble a heading.

### API inspection

~~~python
import inspect
from thomaslab.nlp_context import segment_note_sections

print(inspect.signature(segment_note_sections))
print(segment_note_sections.__doc__)
~~~

### Source

[`src/thomaslab/nlp_context.py#L148`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_context.py#L148)

---

<!-- callable:thomaslab.nlp_context.extract_note_section -->
## extract_note_section

### Purpose

Return concatenated text for a canonical note section.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def extract_note_section( text: object, section: str, *, section_aliases: Mapping[str, Iterable[str]] | None = None, ) -> str
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `text` | `text: object` | Yes | Clinical text input. Apply governance/de-identification requirements and validate NLP behavior on labeled data. |
| `section` | `section: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `section_aliases` | `section_aliases: Mapping[str, Iterable[str]] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `text`, `section`.

### Returns

`str`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.nlp_context import extract_note_section

result = extract_note_section(
    text="Patient denies active bleeding.",
    section="value"
)

print(result)
~~~

### Related functions

- `load_nlp_lexicon`
- `split_clinical_sentences`
- `segment_note_sections`
- `classify_clinical_mentions`
- `summarize_context_mentions`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp_context.py#L198`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_context.py#L198)
- Repository search: [extract_note_section](https://github.com/appsplorer/thomaslab-core/search?q=extract_note_section&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return concatenated text for a canonical note section.

### API inspection

~~~python
import inspect
from thomaslab.nlp_context import extract_note_section

print(inspect.signature(extract_note_section))
print(extract_note_section.__doc__)
~~~

### Source

[`src/thomaslab/nlp_context.py#L198`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_context.py#L198)

---

<!-- callable:thomaslab.nlp_context.classify_clinical_mentions -->
## classify_clinical_mentions

### Purpose

Classify contextual attributes for each target-term mention.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def classify_clinical_mentions( text: object, target_terms: Iterable[str], *, window_tokens: int = 10, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `text` | `text: object` | Yes | Clinical text input. Apply governance/de-identification requirements and validate NLP behavior on labeled data. |
| `target_terms` | `target_terms: Iterable[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `window_tokens` | `window_tokens: int = 10` | No | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `text`, `target_terms`.

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
from thomaslab.nlp_context import classify_clinical_mentions

result = classify_clinical_mentions(
    text="Patient denies active bleeding.",
    target_terms="value"
)

print(result)
~~~

### Related functions

- `load_nlp_lexicon`
- `split_clinical_sentences`
- `segment_note_sections`
- `extract_note_section`
- `summarize_context_mentions`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp_context.py#L245`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_context.py#L245)
- Repository search: [classify_clinical_mentions](https://github.com/appsplorer/thomaslab-core/search?q=classify_clinical_mentions&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Classify contextual attributes for each target-term mention.

Returned attributes include negation, uncertainty, hypothetical context,
experiencer, coarse temporality, severity, and a conservative ``affirmed`` flag.
The rules are intended for transparent research triage and require validation on
a representative annotated sample before use as a study phenotype.

### API inspection

~~~python
import inspect
from thomaslab.nlp_context import classify_clinical_mentions

print(inspect.signature(classify_clinical_mentions))
print(classify_clinical_mentions.__doc__)
~~~

### Source

[`src/thomaslab/nlp_context.py#L245`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_context.py#L245)

---

<!-- callable:thomaslab.nlp_context.summarize_context_mentions -->
## summarize_context_mentions

### Purpose

Summarize output from :func:`classify_clinical_mentions`.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_context_mentions(mentions: pd.DataFrame) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `mentions` | `mentions: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `mentions`.

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

from thomaslab.nlp_context import summarize_context_mentions

result = summarize_context_mentions(
    mentions=sample_df
)

print(result)
~~~

### Related functions

- `load_nlp_lexicon`
- `split_clinical_sentences`
- `segment_note_sections`
- `extract_note_section`
- `classify_clinical_mentions`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/nlp_context.py#L329`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_context.py#L329)
- Repository search: [summarize_context_mentions](https://github.com/appsplorer/thomaslab-core/search?q=summarize_context_mentions&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize output from :func:`classify_clinical_mentions`.

### API inspection

~~~python
import inspect
from thomaslab.nlp_context import summarize_context_mentions

print(inspect.signature(summarize_context_mentions))
print(summarize_context_mentions.__doc__)
~~~

### Source

[`src/thomaslab/nlp_context.py#L329`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/nlp_context.py#L329)

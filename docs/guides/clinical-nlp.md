# Clinical NLP

The NLP layer is deliberately deterministic and auditable for phenotype extraction.

## Clean notes

```python
from thomaslab.nlp import clean_clinical_text

notes["clean_text"] = clean_clinical_text(notes["note_text"])
```

The cleaner removes common header/signature patterns, timestamps, and excess whitespace. It is not a de-identification engine.

## Target-term extraction

```python
from thomaslab.nlp import extract_medical_entities

notes["entities"] = extract_medical_entities(
    notes["clean_text"],
    target_terms=["bleeding", "melena", "hematemesis"],
)
```

This target-driven approach is often preferable when reproducing a predefined computable phenotype because every lexical rule can be reviewed.

## Negation

`detect_negation` uses a NegEx-style rule window and stops negation scope at sentence/clause boundaries.

```python
from thomaslab.nlp import detect_negation

assert detect_negation("No evidence of bleeding.", "bleeding") is True
assert detect_negation("No bleeding. Patient has diabetes.", "diabetes") is False
```

## Extract values from notes

```python
from thomaslab.nlp import extract_lab_values_from_notes

lvef = extract_lab_values_from_notes(notes["clean_text"], "LVEF")
bp = extract_lab_values_from_notes(notes["clean_text"], "BP")
```

For production phenotyping, validate precision/recall against an independently annotated sample and document the annotation protocol.

## Local LLM extraction and embeddings

```python
from thomaslab.nlp import extract_entities_llm_local

structured = extract_entities_llm_local(
    notes["clean_text"],
    "Return JSON with bleeding_site and severity from: {text}",
    model_name="local-clinical-model",
    backend="ollama",
)
```

The default endpoint is localhost and non-local hosts are blocked unless the caller explicitly sets `allow_remote=True`. This guard is intended to reduce accidental PHI disclosure; institutional governance still applies.

`embed_clinical_text_bge` uses local Sentence-Transformers/Transformers models with `local_files_only=True` by default. `extract_temporal_note_expressions` normalizes relative phrases to day offsets and can resolve them against a supplied reference date.


## Advanced context and annotation

Version 0.11 adds note-section parsing, uncertainty/hypothetical/experiencer/temporality context, medication/adverse-event extraction, versioned phenotype lexicons, and annotation/adjudication utilities.

Continue with [Advanced clinical NLP](advanced-clinical-nlp.md) and [Annotation and adjudication](annotation-adjudication.md).

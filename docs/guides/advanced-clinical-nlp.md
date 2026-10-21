# Advanced clinical NLP

Version 0.11 extends the deterministic NLP layer with note sections, contextual mention classification, medication/adverse-event extraction, and phenotype-oriented lexicons.

## Context before classification

Clinical mentions are not automatically positive events. The context engine records:

- negation;
- uncertainty;
- hypothetical/risk language;
- patient versus family experiencer;
- historical/current/unspecified temporality;
- simple severity cues.

```python
from thomaslab.nlp_context import classify_clinical_mentions

mentions = classify_clinical_mentions(
    "Family history of stroke. No active bleeding. Possible NSTEMI.",
    ["stroke", "bleeding", "NSTEMI"],
)
```

These rules are designed for transparent research triage. Validate them against an independently annotated sample before treating them as phenotype labels.

## Note sections

```python
from thomaslab.nlp_context import segment_note_sections

sections = segment_note_sections(note_text)
```

Section aliases are configurable so partner sites can adapt to local templates without changing Python code.

## Medication extraction

```python
from thomaslab.nlp_medications import extract_medication_mentions

meds = extract_medication_mentions(
    notes,
    ["clopidogrel", "ticagrelor", "prasugrel"],
)
```

Dose/frequency snippets are lexical observations only. They do not replace medication reconciliation, RxNorm normalization, or exposure construction from structured medication data.

Medication-change reasons use a versioned reason lexicon:

```python
from thomaslab.nlp_medications import extract_medication_change_reasons

changes = extract_medication_change_reasons(
    notes,
    ["clopidogrel", "ticagrelor"],
    reason_lexicon="nlp_knowledge/medication_change_reasons.yaml",
)
```

## Phenotype-oriented NLP

Versioned YAML lexicons live under `nlp_knowledge/`.

```python
from thomaslab.nlp_phenotypes import (
    extract_contextual_phenotype_mentions,
    aggregate_note_phenotype,
)

mentions = extract_contextual_phenotype_mentions(
    notes,
    "nlp_knowledge/bleeding_example.yaml",
)
patient_level = aggregate_note_phenotype(mentions)
```

The supplied bleeding/MI/stroke lexicons are examples, not validated outcome definitions. Structured EHR evidence, NLP evidence, and chart adjudication should remain distinguishable.

## PHI and model governance

The existing local-LLM utilities remain localhost-only by default. Do not send clinical-note text to a remote model or notebook environment unless the institutional governance process explicitly permits it.

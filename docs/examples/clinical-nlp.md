# Example: contextual clinical mention classification

~~~python
from thomaslab.nlp_context import classify_clinical_mentions

text = """
Assessment:
No evidence of active bleeding.
History of prior gastrointestinal bleeding in 2024.
"""

mentions = classify_clinical_mentions(
    text,
    target_terms=["bleeding"],
    window_tokens=10,
)

print(mentions)
~~~

## Interpretation boundary

Context classification is a research preprocessing step. Validate negation, temporality, section handling, abbreviation behavior, and phenotype performance against study-appropriate labeled notes before scientific use.

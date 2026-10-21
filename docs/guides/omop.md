# OMOP mapping

Local EHR codes cannot be converted to OMOP standard concepts by string manipulation alone. `map_omop_codes` therefore requires an explicit mapping table.

```python
from thomaslab.data import map_omop_codes

mapped = map_omop_codes(
    diagnoses,
    source_col="local_code",
    vocabulary="ICD10CM",
    concept_mapping=concept_map,
)
```

## Recommended mapping workflow

1. Freeze the OMOP vocabulary release date.
2. Normalize source-system codes without changing semantic content.
3. Join source codes to valid source concepts.
4. Traverse `Maps to` relationships to standard concepts where appropriate.
5. Preserve source concept ID, standard concept ID, vocabulary, domain and concept name.
6. Quantify unmapped codes and manually review high-frequency/high-impact failures.
7. Store the mapping artifact under version control **without PHI**.

!!! warning
    Never invent OMOP concept IDs for unmapped local terms. A missing mapping should remain missing and be audited.

# Annotation and adjudication

Reliable clinical NLP requires an annotated validation set. Version 0.11 adds sampling, blinded batch construction, agreement metrics, disagreement queues, and export manifests.

## Sample notes

```python
from thomaslab.annotation import sample_notes_for_annotation

sample = sample_notes_for_annotation(notes, 200, strata="site_id", random_state=42)
```

## Create blinded batches

```python
from thomaslab.annotation import blind_annotation_batches

batches = blind_annotation_batches(
    sample,
    ["annotator_a", "annotator_b"],
    overlap_fraction=0.30,
)
```

The helper controls assignment but **does not de-identify note text**. Annotation must occur in an institutionally approved environment.

## Agreement

```python
from thomaslab.annotation import (
    merge_annotator_labels,
    calculate_interannotator_agreement,
)

long = merge_annotator_labels(batches)
agreement = calculate_interannotator_agreement(long)
```

Cohen's kappa is returned pairwise. Fleiss' kappa is calculated only on items with a common number of completed ratings. Report raw agreement alongside kappa rather than interpreting a single threshold mechanically.

## Adjudication

```python
from thomaslab.annotation import create_adjudication_queue

queue = create_adjudication_queue(long)
```

After adjudication, compare phenotype predictions against the gold labels using `calculate_phenotype_precision_recall`.

## Reproducibility

`export_annotation_dataset` writes CSV/Parquet plus a SHA-256 manifest. The manifest records the artifact identity; it does not make an unapproved storage location safe for PHI.

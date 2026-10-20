# thomaslab.annotation

Annotation, inter-annotator agreement, and adjudication utilities.

## Research-use boundary

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

## Self-service orientation

- Related guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 11

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.annotation.sample_notes_for_annotation -->
## sample_notes_for_annotation

### Purpose

Sample notes reproducibly, optionally approximately balanced by strata.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def sample_notes_for_annotation( notes: pd.DataFrame, n: int, *, strata: str | list[str] | None = None, random_state: int = 42, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `notes` | `notes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `n` | `n: int` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strata` | `strata: str \| list[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `notes`, `n`.

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

from thomaslab.annotation import sample_notes_for_annotation

result = sample_notes_for_annotation(
    notes=sample_df,
    n=2
)

print(result)
~~~

### Related functions

- `create_annotation_batch`
- `blind_annotation_batches`
- `merge_annotator_labels`
- `calculate_cohen_kappa`
- `calculate_fleiss_kappa`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/annotation.py#L16`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L16)
- Repository search: [sample_notes_for_annotation](https://github.com/appsplorer/thomaslab-core/search?q=sample_notes_for_annotation&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Sample notes reproducibly, optionally approximately balanced by strata.

### API inspection

~~~python
import inspect
from thomaslab.annotation import sample_notes_for_annotation

print(inspect.signature(sample_notes_for_annotation))
print(sample_notes_for_annotation.__doc__)
~~~

### Source

[`src/thomaslab/annotation.py#L16`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L16)

---

<!-- callable:thomaslab.annotation.create_annotation_batch -->
## create_annotation_batch

### Purpose

Create a blank annotation batch with stable opaque annotation IDs.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def create_annotation_batch( notes: pd.DataFrame, *, text_col: str = "note_text", id_col: str | None = "note_id", metadata_cols: Iterable[str] | None = None, annotator: str | None = None, batch_id: str = "batch", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `notes` | `notes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `text_col` | `text_col: str = 'note_text'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `id_col` | `id_col: str \| None = 'note_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `metadata_cols` | `metadata_cols: Iterable[str] \| None = None` | No | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `annotator` | `annotator: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `batch_id` | `batch_id: str = 'batch'` | No | Identifier or identifier column. Confirm uniqueness/grouping semantics before analysis. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `notes`.
- Referenced columns must exist in the input table: `text_col`, `id_col`.

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

from thomaslab.annotation import create_annotation_batch

result = create_annotation_batch(
    notes=sample_df
)

print(result)
~~~

### Related functions

- `sample_notes_for_annotation`
- `blind_annotation_batches`
- `merge_annotator_labels`
- `calculate_cohen_kappa`
- `calculate_fleiss_kappa`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/annotation.py#L53`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L53)
- Repository search: [create_annotation_batch](https://github.com/appsplorer/thomaslab-core/search?q=create_annotation_batch&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create a blank annotation batch with stable opaque annotation IDs.

### API inspection

~~~python
import inspect
from thomaslab.annotation import create_annotation_batch

print(inspect.signature(create_annotation_batch))
print(create_annotation_batch.__doc__)
~~~

### Source

[`src/thomaslab/annotation.py#L53`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L53)

---

<!-- callable:thomaslab.annotation.blind_annotation_batches -->
## blind_annotation_batches

### Purpose

Create blinded batches with a controlled shared-overlap subset.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def blind_annotation_batches( notes: pd.DataFrame, annotators: Iterable[str], *, text_col: str = "note_text", id_col: str | None = "note_id", n_per_annotator: int | None = None, overlap_fraction: float = 0.2, random_state: int = 42, ) -> dict[str, pd.DataFrame]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `notes` | `notes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `annotators` | `annotators: Iterable[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `text_col` | `text_col: str = 'note_text'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `id_col` | `id_col: str \| None = 'note_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `n_per_annotator` | `n_per_annotator: int \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `overlap_fraction` | `overlap_fraction: float = 0.2` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `notes`, `annotators`.
- Referenced columns must exist in the input table: `text_col`, `id_col`.

### Returns

`dict[str, pd.DataFrame]`

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

from thomaslab.annotation import blind_annotation_batches

result = blind_annotation_batches(
    notes=sample_df,
    annotators="value"
)

print(result)
~~~

### Related functions

- `sample_notes_for_annotation`
- `create_annotation_batch`
- `merge_annotator_labels`
- `calculate_cohen_kappa`
- `calculate_fleiss_kappa`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/annotation.py#L88`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L88)
- Repository search: [blind_annotation_batches](https://github.com/appsplorer/thomaslab-core/search?q=blind_annotation_batches&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create blinded batches with a controlled shared-overlap subset.

The function controls assignment only. It does not de-identify note text; PHI must
be handled through the institution's approved environment and annotation protocol.

### API inspection

~~~python
import inspect
from thomaslab.annotation import blind_annotation_batches

print(inspect.signature(blind_annotation_batches))
print(blind_annotation_batches.__doc__)
~~~

### Source

[`src/thomaslab/annotation.py#L88`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L88)

---

<!-- callable:thomaslab.annotation.merge_annotator_labels -->
## merge_annotator_labels

### Purpose

Merge annotated batches into long format with explicit annotator identity.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def merge_annotator_labels( annotations: Mapping[str, pd.DataFrame] | Iterable[pd.DataFrame], *, source_id_col: str = "source_id", label_col: str = "label", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `annotations` | `annotations: Mapping[str, pd.DataFrame] \| Iterable[pd.DataFrame]` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `source_id_col` | `source_id_col: str = 'source_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `label_col` | `label_col: str = 'label'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `annotations`.
- Referenced columns must exist in the input table: `source_id_col`, `label_col`.

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

from thomaslab.annotation import merge_annotator_labels

result = merge_annotator_labels(
    annotations=sample_df
)

print(result)
~~~

### Related functions

- `sample_notes_for_annotation`
- `create_annotation_batch`
- `blind_annotation_batches`
- `calculate_cohen_kappa`
- `calculate_fleiss_kappa`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/annotation.py#L139`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L139)
- Repository search: [merge_annotator_labels](https://github.com/appsplorer/thomaslab-core/search?q=merge_annotator_labels&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Merge annotated batches into long format with explicit annotator identity.

### API inspection

~~~python
import inspect
from thomaslab.annotation import merge_annotator_labels

print(inspect.signature(merge_annotator_labels))
print(merge_annotator_labels.__doc__)
~~~

### Source

[`src/thomaslab/annotation.py#L139`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L139)

---

<!-- callable:thomaslab.annotation.calculate_cohen_kappa -->
## calculate_cohen_kappa

### Purpose

Calculate Cohen's kappa and raw agreement for two annotators.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_cohen_kappa( annotations: pd.DataFrame, *, item_col: str = "source_id", annotator_col: str = "annotator", label_col: str = "label", annotators: tuple[str, str] | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `annotations` | `annotations: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `item_col` | `item_col: str = 'source_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `annotator_col` | `annotator_col: str = 'annotator'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `label_col` | `label_col: str = 'label'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `annotators` | `annotators: tuple[str, str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `annotations`.
- Referenced columns must exist in the input table: `item_col`, `annotator_col`, `label_col`.

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

from thomaslab.annotation import calculate_cohen_kappa

result = calculate_cohen_kappa(
    annotations=sample_df
)

print(result)
~~~

### Related functions

- `sample_notes_for_annotation`
- `create_annotation_batch`
- `blind_annotation_batches`
- `merge_annotator_labels`
- `calculate_fleiss_kappa`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/annotation.py#L164`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L164)
- Repository search: [calculate_cohen_kappa](https://github.com/appsplorer/thomaslab-core/search?q=calculate_cohen_kappa&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate Cohen's kappa and raw agreement for two annotators.

### API inspection

~~~python
import inspect
from thomaslab.annotation import calculate_cohen_kappa

print(inspect.signature(calculate_cohen_kappa))
print(calculate_cohen_kappa.__doc__)
~~~

### Source

[`src/thomaslab/annotation.py#L164`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L164)

---

<!-- callable:thomaslab.annotation.calculate_fleiss_kappa -->
## calculate_fleiss_kappa

### Purpose

Calculate Fleiss' kappa on items with the same number of completed ratings.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_fleiss_kappa( annotations: pd.DataFrame, *, item_col: str = "source_id", annotator_col: str = "annotator", label_col: str = "label", ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `annotations` | `annotations: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `item_col` | `item_col: str = 'source_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `annotator_col` | `annotator_col: str = 'annotator'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `label_col` | `label_col: str = 'label'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `annotations`.
- Referenced columns must exist in the input table: `item_col`, `annotator_col`, `label_col`.

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

from thomaslab.annotation import calculate_fleiss_kappa

result = calculate_fleiss_kappa(
    annotations=sample_df
)

print(result)
~~~

### Related functions

- `sample_notes_for_annotation`
- `create_annotation_batch`
- `blind_annotation_batches`
- `merge_annotator_labels`
- `calculate_cohen_kappa`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/annotation.py#L199`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L199)
- Repository search: [calculate_fleiss_kappa](https://github.com/appsplorer/thomaslab-core/search?q=calculate_fleiss_kappa&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate Fleiss' kappa on items with the same number of completed ratings.

### API inspection

~~~python
import inspect
from thomaslab.annotation import calculate_fleiss_kappa

print(inspect.signature(calculate_fleiss_kappa))
print(calculate_fleiss_kappa.__doc__)
~~~

### Source

[`src/thomaslab/annotation.py#L199`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L199)

---

<!-- callable:thomaslab.annotation.calculate_interannotator_agreement -->
## calculate_interannotator_agreement

### Purpose

Return pairwise Cohen metrics and Fleiss kappa when estimable.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_interannotator_agreement( annotations: pd.DataFrame, *, item_col: str = "source_id", annotator_col: str = "annotator", label_col: str = "label", ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `annotations` | `annotations: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `item_col` | `item_col: str = 'source_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `annotator_col` | `annotator_col: str = 'annotator'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `label_col` | `label_col: str = 'label'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `annotations`.
- Referenced columns must exist in the input table: `item_col`, `annotator_col`, `label_col`.

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

from thomaslab.annotation import calculate_interannotator_agreement

result = calculate_interannotator_agreement(
    annotations=sample_df
)

print(result)
~~~

### Related functions

- `sample_notes_for_annotation`
- `create_annotation_batch`
- `blind_annotation_batches`
- `merge_annotator_labels`
- `calculate_cohen_kappa`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/annotation.py#L236`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L236)
- Repository search: [calculate_interannotator_agreement](https://github.com/appsplorer/thomaslab-core/search?q=calculate_interannotator_agreement&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return pairwise Cohen metrics and Fleiss kappa when estimable.

### API inspection

~~~python
import inspect
from thomaslab.annotation import calculate_interannotator_agreement

print(inspect.signature(calculate_interannotator_agreement))
print(calculate_interannotator_agreement.__doc__)
~~~

### Source

[`src/thomaslab/annotation.py#L236`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L236)

---

<!-- callable:thomaslab.annotation.find_annotation_disagreements -->
## find_annotation_disagreements

### Purpose

Return labelled items with more than one distinct annotator label.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def find_annotation_disagreements( annotations: pd.DataFrame, *, item_col: str = "source_id", annotator_col: str = "annotator", label_col: str = "label", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `annotations` | `annotations: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `item_col` | `item_col: str = 'source_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `annotator_col` | `annotator_col: str = 'annotator'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `label_col` | `label_col: str = 'label'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `annotations`.
- Referenced columns must exist in the input table: `item_col`, `annotator_col`, `label_col`.

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

from thomaslab.annotation import find_annotation_disagreements

result = find_annotation_disagreements(
    annotations=sample_df
)

print(result)
~~~

### Related functions

- `sample_notes_for_annotation`
- `create_annotation_batch`
- `blind_annotation_batches`
- `merge_annotator_labels`
- `calculate_cohen_kappa`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/annotation.py#L269`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L269)
- Repository search: [find_annotation_disagreements](https://github.com/appsplorer/thomaslab-core/search?q=find_annotation_disagreements&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return labelled items with more than one distinct annotator label.

### API inspection

~~~python
import inspect
from thomaslab.annotation import find_annotation_disagreements

print(inspect.signature(find_annotation_disagreements))
print(find_annotation_disagreements.__doc__)
~~~

### Source

[`src/thomaslab/annotation.py#L269`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L269)

---

<!-- callable:thomaslab.annotation.create_adjudication_queue -->
## create_adjudication_queue

### Purpose

Create one row per disagreement with blank adjudication fields.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def create_adjudication_queue( annotations: pd.DataFrame, *, item_col: str = "source_id", annotator_col: str = "annotator", label_col: str = "label", text_col: str = "text", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `annotations` | `annotations: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `item_col` | `item_col: str = 'source_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `annotator_col` | `annotator_col: str = 'annotator'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `label_col` | `label_col: str = 'label'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `text_col` | `text_col: str = 'text'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `annotations`.
- Referenced columns must exist in the input table: `item_col`, `annotator_col`, `label_col`, `text_col`.

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

from thomaslab.annotation import create_adjudication_queue

result = create_adjudication_queue(
    annotations=sample_df
)

print(result)
~~~

### Related functions

- `sample_notes_for_annotation`
- `create_annotation_batch`
- `blind_annotation_batches`
- `merge_annotator_labels`
- `calculate_cohen_kappa`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/annotation.py#L294`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L294)
- Repository search: [create_adjudication_queue](https://github.com/appsplorer/thomaslab-core/search?q=create_adjudication_queue&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create one row per disagreement with blank adjudication fields.

### API inspection

~~~python
import inspect
from thomaslab.annotation import create_adjudication_queue

print(inspect.signature(create_adjudication_queue))
print(create_adjudication_queue.__doc__)
~~~

### Source

[`src/thomaslab/annotation.py#L294`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L294)

---

<!-- callable:thomaslab.annotation.calculate_phenotype_precision_recall -->
## calculate_phenotype_precision_recall

### Purpose

Calculate binary precision, recall, F1, and support from adjudicated labels.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_phenotype_precision_recall( gold: Iterable[Any], predicted: Iterable[Any], *, positive_label: Any = 1, ) -> dict[str, float]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `gold` | `gold: Iterable[Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `predicted` | `predicted: Iterable[Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `positive_label` | `positive_label: Any = 1` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `gold`, `predicted`.

### Returns

`dict[str, float]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
sample_value = "replace_with_validated_value"

from thomaslab.annotation import calculate_phenotype_precision_recall

result = calculate_phenotype_precision_recall(
    gold=sample_value,
    predicted={}
)

print(result)
~~~

### Related functions

- `sample_notes_for_annotation`
- `create_annotation_batch`
- `blind_annotation_batches`
- `merge_annotator_labels`
- `calculate_cohen_kappa`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/annotation.py#L319`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L319)
- Repository search: [calculate_phenotype_precision_recall](https://github.com/appsplorer/thomaslab-core/search?q=calculate_phenotype_precision_recall&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate binary precision, recall, F1, and support from adjudicated labels.

### API inspection

~~~python
import inspect
from thomaslab.annotation import calculate_phenotype_precision_recall

print(inspect.signature(calculate_phenotype_precision_recall))
print(calculate_phenotype_precision_recall.__doc__)
~~~

### Source

[`src/thomaslab/annotation.py#L319`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L319)

---

<!-- callable:thomaslab.annotation.export_annotation_dataset -->
## export_annotation_dataset

### Purpose

Export annotation rows plus a SHA-256 manifest.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def export_annotation_dataset( annotations: pd.DataFrame, output_path: str | Path, *, metadata: Mapping[str, Any] | None = None, ) -> dict[str, str]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `annotations` | `annotations: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `output_path` | `output_path: str \| Path` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `metadata` | `metadata: Mapping[str, Any] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `annotations`, `output_path`.

### Returns

`dict[str, str]`

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

from thomaslab.annotation import export_annotation_dataset

result = export_annotation_dataset(
    annotations=sample_df,
    output_path="path/to/input.csv"
)

print(result)
~~~

### Related functions

- `sample_notes_for_annotation`
- `create_annotation_batch`
- `blind_annotation_batches`
- `merge_annotator_labels`
- `calculate_cohen_kappa`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/annotation.py#L347`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L347)
- Repository search: [export_annotation_dataset](https://github.com/appsplorer/thomaslab-core/search?q=export_annotation_dataset&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Export annotation rows plus a SHA-256 manifest.

CSV and Parquet are supported. The manifest documents the exported artifact; it
does not make an ungoverned location suitable for PHI.

### API inspection

~~~python
import inspect
from thomaslab.annotation import export_annotation_dataset

print(inspect.signature(export_annotation_dataset))
print(export_annotation_dataset.__doc__)
~~~

### Source

[`src/thomaslab/annotation.py#L347`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/annotation.py#L347)

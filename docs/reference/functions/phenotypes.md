# thomaslab.phenotypes

Versioned clinical phenotype definitions and reusable endpoint utilities.

The phenotype layer is intentionally configuration-driven. It can standardize and
apply reviewed rules, but it does not invent clinical code sets or adjudication
criteria when those are absent from the study protocol.

## Research-use boundary

Validate extraction, context, annotation, and phenotype behavior against study-appropriate labeled data before scientific use.

## Self-service orientation

- Related guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 10

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.phenotypes.load_phenotype_definition -->
## load_phenotype_definition

### Purpose

Load and validate a phenotype definition from YAML or a mapping.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def load_phenotype_definition(source: str | Path | Mapping[str, Any]) -> dict[str, Any]
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

from thomaslab.phenotypes import load_phenotype_definition

result = load_phenotype_definition(
    source=sample_df
)

print(result)
~~~

### Related functions

- `validate_phenotype_definition`
- `match_structured_events`
- `apply_structured_phenotype`
- `first_endpoint_event`
- `build_composite_endpoint`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/phenotypes.py#L19`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L19)
- Repository search: [load_phenotype_definition](https://github.com/appsplorer/thomaslab-core/search?q=load_phenotype_definition&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Load and validate a phenotype definition from YAML or a mapping.

### API inspection

~~~python
import inspect
from thomaslab.phenotypes import load_phenotype_definition

print(inspect.signature(load_phenotype_definition))
print(load_phenotype_definition.__doc__)
~~~

### Source

[`src/thomaslab/phenotypes.py#L19`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L19)

---

<!-- callable:thomaslab.phenotypes.validate_phenotype_definition -->
## validate_phenotype_definition

### Purpose

Validate a versioned structured-event phenotype definition.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_phenotype_definition(definition: Mapping[str, Any]) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `definition` | `definition: Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `definition`.

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
from thomaslab.phenotypes import validate_phenotype_definition

result = validate_phenotype_definition(
    definition={}
)

print(result)
~~~

### Related functions

- `load_phenotype_definition`
- `match_structured_events`
- `apply_structured_phenotype`
- `first_endpoint_event`
- `build_composite_endpoint`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/phenotypes.py#L34`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L34)
- Repository search: [validate_phenotype_definition](https://github.com/appsplorer/thomaslab-core/search?q=validate_phenotype_definition&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Validate a versioned structured-event phenotype definition.

Supported structured rules are exact and prefix code matching. The definition
records the code-system/version used by the study; this function does not check
whether a code exists in a current external terminology release.

### API inspection

~~~python
import inspect
from thomaslab.phenotypes import validate_phenotype_definition

print(inspect.signature(validate_phenotype_definition))
print(validate_phenotype_definition.__doc__)
~~~

### Source

[`src/thomaslab/phenotypes.py#L34`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L34)

---

<!-- callable:thomaslab.phenotypes.match_structured_events -->
## match_structured_events

### Purpose

Return event rows matching a reviewed exact/prefix phenotype definition.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def match_structured_events( events: pd.DataFrame, definition: str | Path | Mapping[str, Any], *, code_col: str = "code", date_col: str = "event_date", patient_col: str = "patient_id", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `definition` | `definition: str \| Path \| Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `code_col` | `code_col: str = 'code'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`, `definition`.
- Referenced columns must exist in the input table: `code_col`, `date_col`, `patient_col`.

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

from thomaslab.phenotypes import match_structured_events

result = match_structured_events(
    events=sample_df,
    definition={}
)

print(result)
~~~

### Related functions

- `load_phenotype_definition`
- `validate_phenotype_definition`
- `apply_structured_phenotype`
- `first_endpoint_event`
- `build_composite_endpoint`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/phenotypes.py#L69`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L69)
- Repository search: [match_structured_events](https://github.com/appsplorer/thomaslab-core/search?q=match_structured_events&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return event rows matching a reviewed exact/prefix phenotype definition.

### API inspection

~~~python
import inspect
from thomaslab.phenotypes import match_structured_events

print(inspect.signature(match_structured_events))
print(match_structured_events.__doc__)
~~~

### Source

[`src/thomaslab/phenotypes.py#L69`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L69)

---

<!-- callable:thomaslab.phenotypes.apply_structured_phenotype -->
## apply_structured_phenotype

### Purpose

Apply a phenotype and return one row per patient with first-event metadata.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def apply_structured_phenotype( events: pd.DataFrame, definition: str | Path | Mapping[str, Any], *, code_col: str = "code", date_col: str = "event_date", patient_col: str = "patient_id", patient_universe: Iterable[Any] | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `definition` | `definition: str \| Path \| Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `code_col` | `code_col: str = 'code'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `patient_universe` | `patient_universe: Iterable[Any] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`, `definition`.
- Referenced columns must exist in the input table: `code_col`, `date_col`, `patient_col`.

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

from thomaslab.phenotypes import apply_structured_phenotype

result = apply_structured_phenotype(
    events=sample_df,
    definition={}
)

print(result)
~~~

### Related functions

- `load_phenotype_definition`
- `validate_phenotype_definition`
- `match_structured_events`
- `first_endpoint_event`
- `build_composite_endpoint`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/phenotypes.py#L107`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L107)
- Repository search: [apply_structured_phenotype](https://github.com/appsplorer/thomaslab-core/search?q=apply_structured_phenotype&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Apply a phenotype and return one row per patient with first-event metadata.

### API inspection

~~~python
import inspect
from thomaslab.phenotypes import apply_structured_phenotype

print(inspect.signature(apply_structured_phenotype))
print(apply_structured_phenotype.__doc__)
~~~

### Source

[`src/thomaslab/phenotypes.py#L107`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L107)

---

<!-- callable:thomaslab.phenotypes.first_endpoint_event -->
## first_endpoint_event

### Purpose

Return the earliest event per patient with deterministic component tie-breaking.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def first_endpoint_event( events: pd.DataFrame, *, patient_col: str = "patient_id", date_col: str = "event_date", component_col: str = "component", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `component_col` | `component_col: str = 'component'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`.
- Referenced columns must exist in the input table: `patient_col`, `date_col`, `component_col`.

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

from thomaslab.phenotypes import first_endpoint_event

result = first_endpoint_event(
    events=sample_df
)

print(result)
~~~

### Related functions

- `load_phenotype_definition`
- `validate_phenotype_definition`
- `match_structured_events`
- `apply_structured_phenotype`
- `build_composite_endpoint`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/phenotypes.py#L144`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L144)
- Repository search: [first_endpoint_event](https://github.com/appsplorer/thomaslab-core/search?q=first_endpoint_event&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return the earliest event per patient with deterministic component tie-breaking.

### API inspection

~~~python
import inspect
from thomaslab.phenotypes import first_endpoint_event

print(inspect.signature(first_endpoint_event))
print(first_endpoint_event.__doc__)
~~~

### Source

[`src/thomaslab/phenotypes.py#L144`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L144)

---

<!-- callable:thomaslab.phenotypes.build_composite_endpoint -->
## build_composite_endpoint

### Purpose

Build a first-event composite endpoint from explicit component names.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_composite_endpoint( events: pd.DataFrame, components: Iterable[str], *, endpoint_name: str, patient_col: str = "patient_id", date_col: str = "event_date", component_col: str = "component", patient_universe: Iterable[Any] | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `components` | `components: Iterable[str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `endpoint_name` | `endpoint_name: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `component_col` | `component_col: str = 'component'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `patient_universe` | `patient_universe: Iterable[Any] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`, `components`, `endpoint_name`.
- Referenced columns must exist in the input table: `patient_col`, `date_col`, `component_col`.

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

from thomaslab.phenotypes import build_composite_endpoint

result = build_composite_endpoint(
    events=sample_df,
    components="value",
    endpoint_name="value"
)

print(result)
~~~

### Related functions

- `load_phenotype_definition`
- `validate_phenotype_definition`
- `match_structured_events`
- `apply_structured_phenotype`
- `first_endpoint_event`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/phenotypes.py#L165`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L165)
- Repository search: [build_composite_endpoint](https://github.com/appsplorer/thomaslab-core/search?q=build_composite_endpoint&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build a first-event composite endpoint from explicit component names.

### API inspection

~~~python
import inspect
from thomaslab.phenotypes import build_composite_endpoint

print(inspect.signature(build_composite_endpoint))
print(build_composite_endpoint.__doc__)
~~~

### Source

[`src/thomaslab/phenotypes.py#L165`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L165)

---

<!-- callable:thomaslab.phenotypes.combine_structured_nlp_phenotype -->
## combine_structured_nlp_phenotype

### Purpose

Combine structured and NLP phenotype evidence with an explicit logic rule.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def combine_structured_nlp_phenotype( structured: pd.DataFrame, nlp: pd.DataFrame, *, patient_col: str = "patient_id", structured_positive_col: str = "phenotype_positive", nlp_positive_col: str = "phenotype_positive", logic: str = "or", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `structured` | `structured: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `nlp` | `nlp: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `structured_positive_col` | `structured_positive_col: str = 'phenotype_positive'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `nlp_positive_col` | `nlp_positive_col: str = 'phenotype_positive'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `logic` | `logic: str = 'or'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `structured`, `nlp`.
- Referenced columns must exist in the input table: `patient_col`, `structured_positive_col`, `nlp_positive_col`.

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

from thomaslab.phenotypes import combine_structured_nlp_phenotype

result = combine_structured_nlp_phenotype(
    structured=sample_df,
    nlp=sample_df
)

print(result)
~~~

### Related functions

- `load_phenotype_definition`
- `validate_phenotype_definition`
- `match_structured_events`
- `apply_structured_phenotype`
- `first_endpoint_event`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/phenotypes.py#L211`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L211)
- Repository search: [combine_structured_nlp_phenotype](https://github.com/appsplorer/thomaslab-core/search?q=combine_structured_nlp_phenotype&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Combine structured and NLP phenotype evidence with an explicit logic rule.

### API inspection

~~~python
import inspect
from thomaslab.phenotypes import combine_structured_nlp_phenotype

print(inspect.signature(combine_structured_nlp_phenotype))
print(combine_structured_nlp_phenotype.__doc__)
~~~

### Source

[`src/thomaslab/phenotypes.py#L211`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L211)

---

<!-- callable:thomaslab.phenotypes.validate_against_gold_standard -->
## validate_against_gold_standard

### Purpose

Calculate basic binary phenotype validation metrics against adjudicated gold labels.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def validate_against_gold_standard( predictions: pd.DataFrame, gold: pd.DataFrame, *, patient_col: str = "patient_id", prediction_col: str = "phenotype_positive", gold_col: str = "gold_positive", ) -> dict[str, float | int]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `predictions` | `predictions: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `gold` | `gold: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `prediction_col` | `prediction_col: str = 'phenotype_positive'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `gold_col` | `gold_col: str = 'gold_positive'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `predictions`, `gold`.
- Referenced columns must exist in the input table: `patient_col`, `prediction_col`, `gold_col`.

### Returns

`dict[str, float | int]`

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

from thomaslab.phenotypes import validate_against_gold_standard

result = validate_against_gold_standard(
    predictions=sample_df,
    gold=sample_df
)

print(result)
~~~

### Related functions

- `load_phenotype_definition`
- `validate_phenotype_definition`
- `match_structured_events`
- `apply_structured_phenotype`
- `first_endpoint_event`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/phenotypes.py#L256`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L256)
- Repository search: [validate_against_gold_standard](https://github.com/appsplorer/thomaslab-core/search?q=validate_against_gold_standard&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate basic binary phenotype validation metrics against adjudicated gold labels.

### API inspection

~~~python
import inspect
from thomaslab.phenotypes import validate_against_gold_standard

print(inspect.signature(validate_against_gold_standard))
print(validate_against_gold_standard.__doc__)
~~~

### Source

[`src/thomaslab/phenotypes.py#L256`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L256)

---

<!-- callable:thomaslab.phenotypes.phenotype_sensitivity_analysis -->
## phenotype_sensitivity_analysis

### Purpose

Compare prevalence and patient-level overlap across alternative phenotype definitions.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def phenotype_sensitivity_analysis( results: Mapping[str, pd.DataFrame], *, patient_col: str = "patient_id", positive_col: str = "phenotype_positive", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `results` | `results: Mapping[str, pd.DataFrame]` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `positive_col` | `positive_col: str = 'phenotype_positive'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `results`.
- Referenced columns must exist in the input table: `patient_col`, `positive_col`.

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

from thomaslab.phenotypes import phenotype_sensitivity_analysis

result = phenotype_sensitivity_analysis(
    results=sample_df
)

print(result)
~~~

### Related functions

- `load_phenotype_definition`
- `validate_phenotype_definition`
- `match_structured_events`
- `apply_structured_phenotype`
- `first_endpoint_event`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/phenotypes.py#L303`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L303)
- Repository search: [phenotype_sensitivity_analysis](https://github.com/appsplorer/thomaslab-core/search?q=phenotype_sensitivity_analysis&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compare prevalence and patient-level overlap across alternative phenotype definitions.

### API inspection

~~~python
import inspect
from thomaslab.phenotypes import phenotype_sensitivity_analysis

print(inspect.signature(phenotype_sensitivity_analysis))
print(phenotype_sensitivity_analysis.__doc__)
~~~

### Source

[`src/thomaslab/phenotypes.py#L303`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L303)

---

<!-- callable:thomaslab.phenotypes.create_adjudication_queue -->
## create_adjudication_queue

### Purpose

Return phenotype candidates requiring manual chart/annotation review.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def create_adjudication_queue( candidates: pd.DataFrame, *, status_col: str = "status", review_statuses: Iterable[str] = ("ambiguous", "uncertain", "needs_review"), priority_col: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `candidates` | `candidates: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `status_col` | `status_col: str = 'status'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `review_statuses` | `review_statuses: Iterable[str] = ('ambiguous', 'uncertain', 'needs_review')` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `priority_col` | `priority_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `candidates`.
- Referenced columns must exist in the input table: `status_col`, `priority_col`.

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

from thomaslab.phenotypes import create_adjudication_queue

result = create_adjudication_queue(
    candidates=sample_df
)

print(result)
~~~

### Related functions

- `load_phenotype_definition`
- `validate_phenotype_definition`
- `match_structured_events`
- `apply_structured_phenotype`
- `first_endpoint_event`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/phenotypes.py#L336`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L336)
- Repository search: [create_adjudication_queue](https://github.com/appsplorer/thomaslab-core/search?q=create_adjudication_queue&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return phenotype candidates requiring manual chart/annotation review.

### API inspection

~~~python
import inspect
from thomaslab.phenotypes import create_adjudication_queue

print(inspect.signature(create_adjudication_queue))
print(create_adjudication_queue.__doc__)
~~~

### Source

[`src/thomaslab/phenotypes.py#L336`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/phenotypes.py#L336)

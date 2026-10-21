# thomaslab.bleeding

Bleeding-event classification and high-bleeding-risk research utilities.

## Research-use boundary

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

## Self-service orientation

- Related guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 6

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.bleeding.classify_gusto_bleeding -->
## classify_gusto_bleeding

### Purpose

Classify GUSTO bleeding severity from standardized event indicators.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def classify_gusto_bleeding( events: pd.DataFrame, *, bleeding_col: str = "bleeding_present", intracerebral_col: str = "intracerebral_hemorrhage", hemodynamic_col: str = "hemodynamic_compromise_treated", transfusion_col: str = "blood_transfusion", ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `bleeding_col` | `bleeding_col: str = 'bleeding_present'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `intracerebral_col` | `intracerebral_col: str = 'intracerebral_hemorrhage'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `hemodynamic_col` | `hemodynamic_col: str = 'hemodynamic_compromise_treated'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `transfusion_col` | `transfusion_col: str = 'blood_transfusion'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`.
- Referenced columns must exist in the input table: `bleeding_col`, `intracerebral_col`, `hemodynamic_col`, `transfusion_col`.

### Returns

`pd.Series`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

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

from thomaslab.bleeding import classify_gusto_bleeding

result = classify_gusto_bleeding(
    events=sample_df
)

print(result)
~~~

### Related functions

- `classify_barc_bleeding`
- `calculate_arc_hbr`
- `summarize_bleeding_outcomes`
- `create_bleeding_adjudication_queue`
- `bleeding_classification_report`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/bleeding.py#L34`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/bleeding.py#L34)
- Repository search: [classify_gusto_bleeding](https://github.com/appsplorer/thomaslab-core/search?q=classify_gusto_bleeding&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Classify GUSTO bleeding severity from standardized event indicators.

Severe/life-threatening takes precedence over moderate, which takes precedence
over mild. Rows without bleeding are labelled ``none``.

### API inspection

~~~python
import inspect
from thomaslab.bleeding import classify_gusto_bleeding

print(inspect.signature(classify_gusto_bleeding))
print(classify_gusto_bleeding.__doc__)
~~~

### Source

[`src/thomaslab/bleeding.py#L34`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/bleeding.py#L34)

---

<!-- callable:thomaslab.bleeding.classify_barc_bleeding -->
## classify_barc_bleeding

### Purpose

Classify common BARC bleeding categories from standardized inputs.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def classify_barc_bleeding( events: pd.DataFrame, *, bleeding_col: str = "bleeding_present", fatal_col: str = "fatal_bleeding", cabg_type4_col: str = "barc_type4_criteria_met", intracranial_col: str = "intracranial_hemorrhage", intraocular_col: str = "intraocular_vision_compromising", hemoglobin_drop_col: str = "hemoglobin_drop_g_dl", transfusion_col: str = "blood_transfusion", tamponade_col: str = "cardiac_tamponade", surgery_col: str = "surgical_intervention_for_bleeding", vasoactive_col: str = "iv_vasoactive_for_bleeding", actionable_col: str = "medical_intervention_or_hospitalization", ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `bleeding_col` | `bleeding_col: str = 'bleeding_present'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `fatal_col` | `fatal_col: str = 'fatal_bleeding'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `cabg_type4_col` | `cabg_type4_col: str = 'barc_type4_criteria_met'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `intracranial_col` | `intracranial_col: str = 'intracranial_hemorrhage'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `intraocular_col` | `intraocular_col: str = 'intraocular_vision_compromising'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `hemoglobin_drop_col` | `hemoglobin_drop_col: str = 'hemoglobin_drop_g_dl'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `transfusion_col` | `transfusion_col: str = 'blood_transfusion'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `tamponade_col` | `tamponade_col: str = 'cardiac_tamponade'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `surgery_col` | `surgery_col: str = 'surgical_intervention_for_bleeding'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `vasoactive_col` | `vasoactive_col: str = 'iv_vasoactive_for_bleeding'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `actionable_col` | `actionable_col: str = 'medical_intervention_or_hospitalization'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`.
- Referenced columns must exist in the input table: `bleeding_col`, `fatal_col`, `cabg_type4_col`, `intracranial_col`, `intraocular_col`, `hemoglobin_drop_col`, `transfusion_col`, `tamponade_col`, `surgery_col`, `vasoactive_col`, `actionable_col`.

### Returns

`pd.Series`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

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

from thomaslab.bleeding import classify_barc_bleeding

result = classify_barc_bleeding(
    events=sample_df
)

print(result)
~~~

### Related functions

- `classify_gusto_bleeding`
- `calculate_arc_hbr`
- `summarize_bleeding_outcomes`
- `create_bleeding_adjudication_queue`
- `bleeding_classification_report`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/bleeding.py#L58`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/bleeding.py#L58)
- Repository search: [classify_barc_bleeding](https://github.com/appsplorer/thomaslab-core/search?q=classify_barc_bleeding&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Classify common BARC bleeding categories from standardized inputs.

CABG-related type 4 is accepted as a pre-adjudicated boolean because the full
type-4 definition contains procedure-specific details. The function implements
hierarchical precedence and does not infer missing clinical facts.

### API inspection

~~~python
import inspect
from thomaslab.bleeding import classify_barc_bleeding

print(inspect.signature(classify_barc_bleeding))
print(classify_barc_bleeding.__doc__)
~~~

### Source

[`src/thomaslab/bleeding.py#L58`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/bleeding.py#L58)

---

<!-- callable:thomaslab.bleeding.calculate_arc_hbr -->
## calculate_arc_hbr

### Purpose

Apply the ARC-HBR binary aggregation rule to precomputed criterion flags.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_arc_hbr( criteria: pd.DataFrame, *, major_columns: Iterable[str], minor_columns: Iterable[str], ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `criteria` | `criteria: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `major_columns` | `major_columns: Iterable[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `minor_columns` | `minor_columns: Iterable[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `criteria`, `major_columns`, `minor_columns`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

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

from thomaslab.bleeding import calculate_arc_hbr

result = calculate_arc_hbr(
    criteria=sample_df,
    major_columns=["feature_a", "feature_b"],
    minor_columns=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `classify_gusto_bleeding`
- `classify_barc_bleeding`
- `summarize_bleeding_outcomes`
- `create_bleeding_adjudication_queue`
- `bleeding_classification_report`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/bleeding.py#L109`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/bleeding.py#L109)
- Repository search: [calculate_arc_hbr](https://github.com/appsplorer/thomaslab-core/search?q=calculate_arc_hbr&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Apply the ARC-HBR binary aggregation rule to precomputed criterion flags.

Criterion derivation is intentionally external: the caller must construct each
reviewed major/minor boolean criterion from appropriately timed clinical data.
HBR is positive when at least one major or at least two minor criteria are met.

### API inspection

~~~python
import inspect
from thomaslab.bleeding import calculate_arc_hbr

print(inspect.signature(calculate_arc_hbr))
print(calculate_arc_hbr.__doc__)
~~~

### Source

[`src/thomaslab/bleeding.py#L109`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/bleeding.py#L109)

---

<!-- callable:thomaslab.bleeding.summarize_bleeding_outcomes -->
## summarize_bleeding_outcomes

### Purpose

Summarize bleeding-class counts and unique patient counts.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_bleeding_outcomes( events: pd.DataFrame, *, patient_col: str = "patient_id", class_col: str, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `class_col` | `class_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`, `class_col`.
- Referenced columns must exist in the input table: `patient_col`, `class_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

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

from thomaslab.bleeding import summarize_bleeding_outcomes

result = summarize_bleeding_outcomes(
    events=sample_df,
    class_col='class'
)

print(result)
~~~

### Related functions

- `classify_gusto_bleeding`
- `classify_barc_bleeding`
- `calculate_arc_hbr`
- `create_bleeding_adjudication_queue`
- `bleeding_classification_report`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/bleeding.py#L144`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/bleeding.py#L144)
- Repository search: [summarize_bleeding_outcomes](https://github.com/appsplorer/thomaslab-core/search?q=summarize_bleeding_outcomes&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize bleeding-class counts and unique patient counts.

### API inspection

~~~python
import inspect
from thomaslab.bleeding import summarize_bleeding_outcomes

print(inspect.signature(summarize_bleeding_outcomes))
print(summarize_bleeding_outcomes.__doc__)
~~~

### Source

[`src/thomaslab/bleeding.py#L144`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/bleeding.py#L144)

---

<!-- callable:thomaslab.bleeding.create_bleeding_adjudication_queue -->
## create_bleeding_adjudication_queue

### Purpose

Return bleeding candidates with missing fields needed for severity adjudication.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def create_bleeding_adjudication_queue( events: pd.DataFrame, *, patient_col: str = "patient_id", event_date_col: str = "event_date", required_fields: Iterable[str] = ( "bleeding_present", "blood_transfusion", "hemoglobin_drop_g_dl", ), ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `event_date_col` | `event_date_col: str = 'event_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `required_fields` | `required_fields: Iterable[str] = ('bleeding_present', 'blood_transfusion', 'hemoglobin_drop_g_dl')` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`.
- Referenced columns must exist in the input table: `patient_col`, `event_date_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

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

from thomaslab.bleeding import create_bleeding_adjudication_queue

result = create_bleeding_adjudication_queue(
    events=sample_df
)

print(result)
~~~

### Related functions

- `classify_gusto_bleeding`
- `classify_barc_bleeding`
- `calculate_arc_hbr`
- `summarize_bleeding_outcomes`
- `bleeding_classification_report`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/bleeding.py#L162`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/bleeding.py#L162)
- Repository search: [create_bleeding_adjudication_queue](https://github.com/appsplorer/thomaslab-core/search?q=create_bleeding_adjudication_queue&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return bleeding candidates with missing fields needed for severity adjudication.

### API inspection

~~~python
import inspect
from thomaslab.bleeding import create_bleeding_adjudication_queue

print(inspect.signature(create_bleeding_adjudication_queue))
print(create_bleeding_adjudication_queue.__doc__)
~~~

### Source

[`src/thomaslab/bleeding.py#L162`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/bleeding.py#L162)

---

<!-- callable:thomaslab.bleeding.bleeding_classification_report -->
## bleeding_classification_report

### Purpose

Generate GUSTO and BARC classifications plus an adjudication queue.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def bleeding_classification_report( events: pd.DataFrame, *, patient_col: str = "patient_id", ) -> dict[str, pd.DataFrame]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `events` | `events: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `events`.
- Referenced columns must exist in the input table: `patient_col`.

### Returns

`dict[str, pd.DataFrame]`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

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

from thomaslab.bleeding import bleeding_classification_report

result = bleeding_classification_report(
    events=sample_df
)

print(result)
~~~

### Related functions

- `classify_gusto_bleeding`
- `classify_barc_bleeding`
- `calculate_arc_hbr`
- `summarize_bleeding_outcomes`
- `create_bleeding_adjudication_queue`

### Related workflow

- Guide: [Clinical Nlp](../../guides/clinical-nlp.md)
- Guided notebooks: Notebooks 18–20
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/bleeding.py#L187`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/bleeding.py#L187)
- Repository search: [bleeding_classification_report](https://github.com/appsplorer/thomaslab-core/search?q=bleeding_classification_report&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Generate GUSTO and BARC classifications plus an adjudication queue.

### API inspection

~~~python
import inspect
from thomaslab.bleeding import bleeding_classification_report

print(inspect.signature(bleeding_classification_report))
print(bleeding_classification_report.__doc__)
~~~

### Source

[`src/thomaslab/bleeding.py#L187`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/bleeding.py#L187)

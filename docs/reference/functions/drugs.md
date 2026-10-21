# thomaslab.drugs

Longitudinal medication exposure, adherence, persistence, and treatment-pathway utilities.

The module is intentionally terminology-agnostic. Brand/generic normalization and treatment
intensity orderings must be supplied explicitly from reviewed study resources; the library does
not infer therapeutic equivalence or clinical superiority from drug names.

## Research-use boundary

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

## Self-service orientation

- Related guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 15

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.drugs.normalize_drug_name -->
## normalize_drug_name

### Purpose

Normalize medication names using an explicit reviewed synonym map.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def normalize_drug_name( series: pd.Series, *, synonym_map: Mapping[str, str] | None = None, preserve_unknown: bool = True, ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `series` | `series: pd.Series` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `synonym_map` | `synonym_map: Mapping[str, str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `preserve_unknown` | `preserve_unknown: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `series`.

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

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.drugs import normalize_drug_name

result = normalize_drug_name(
    series=sample_series
)

print(result)
~~~

### Related functions

- `map_brand_to_generic`
- `calculate_days_supply`
- `build_drug_exposure_episodes`
- `calculate_pdc`
- `calculate_mpr`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drugs.py#L31`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L31)
- Repository search: [normalize_drug_name](https://github.com/appsplorer/thomaslab-core/search?q=normalize_drug_name&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Normalize medication names using an explicit reviewed synonym map.

Only lexical cleanup is automatic. Brand-to-generic or local-formulary mappings are never
fabricated. ``synonym_map`` keys are normalized before matching.

### API inspection

~~~python
import inspect
from thomaslab.drugs import normalize_drug_name

print(inspect.signature(normalize_drug_name))
print(normalize_drug_name.__doc__)
~~~

### Source

[`src/thomaslab/drugs.py#L31`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L31)

---

<!-- callable:thomaslab.drugs.map_brand_to_generic -->
## map_brand_to_generic

### Purpose

Map brand/local names to generic names using only an explicit mapping table.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def map_brand_to_generic( series: pd.Series, mapping: Mapping[str, str], *, strict: bool = False, ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `series` | `series: pd.Series` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `mapping` | `mapping: Mapping[str, str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `strict` | `strict: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `series`, `mapping`.

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

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.drugs import map_brand_to_generic

result = map_brand_to_generic(
    series=sample_series,
    mapping={}
)

print(result)
~~~

### Related functions

- `normalize_drug_name`
- `calculate_days_supply`
- `build_drug_exposure_episodes`
- `calculate_pdc`
- `calculate_mpr`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drugs.py#L55`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L55)
- Repository search: [map_brand_to_generic](https://github.com/appsplorer/thomaslab-core/search?q=map_brand_to_generic&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Map brand/local names to generic names using only an explicit mapping table.

### API inspection

~~~python
import inspect
from thomaslab.drugs import map_brand_to_generic

print(inspect.signature(map_brand_to_generic))
print(map_brand_to_generic.__doc__)
~~~

### Source

[`src/thomaslab/drugs.py#L55`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L55)

---

<!-- callable:thomaslab.drugs.calculate_days_supply -->
## calculate_days_supply

### Purpose

Derive days supply as quantity / administrations-per-day when defensible.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_days_supply( df: pd.DataFrame, *, quantity_col: str, doses_per_day_col: str, output_col: str = "days_supply", strict: bool = True, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `quantity_col` | `quantity_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `doses_per_day_col` | `doses_per_day_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `output_col` | `output_col: str = 'days_supply'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `strict` | `strict: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `quantity_col`, `doses_per_day_col`.
- Referenced columns must exist in the input table: `quantity_col`, `doses_per_day_col`, `output_col`.

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

from thomaslab.drugs import calculate_days_supply

result = calculate_days_supply(
    df=sample_df,
    quantity_col='quantity',
    doses_per_day_col='doses_per_day'
)

print(result)
~~~

### Related functions

- `normalize_drug_name`
- `map_brand_to_generic`
- `build_drug_exposure_episodes`
- `calculate_pdc`
- `calculate_mpr`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drugs.py#L80`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L80)
- Repository search: [calculate_days_supply](https://github.com/appsplorer/thomaslab-core/search?q=calculate_days_supply&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Derive days supply as quantity / administrations-per-day when defensible.

Fractional derived values are retained. Real dispensing datasets should prefer the source
days-supply field when available because PRN instructions and dose titration can invalidate
this arithmetic approximation.

### API inspection

~~~python
import inspect
from thomaslab.drugs import calculate_days_supply

print(inspect.signature(calculate_days_supply))
print(calculate_days_supply.__doc__)
~~~

### Source

[`src/thomaslab/drugs.py#L80`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L80)

---

<!-- callable:thomaslab.drugs.build_drug_exposure_episodes -->
## build_drug_exposure_episodes

### Purpose

Build same-drug exposure episodes from dispensing/fill records.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_drug_exposure_episodes( fills: pd.DataFrame, *, patient_col: str = "patient_id", drug_col: str = "drug", date_col: str = "fill_date", days_supply_col: str = "days_supply", grace_days: int = 0, stockpile: bool = True, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `fills` | `fills: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str = 'fill_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `days_supply_col` | `days_supply_col: str = 'days_supply'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `grace_days` | `grace_days: int = 0` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `stockpile` | `stockpile: bool = True` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `fills`.
- Referenced columns must exist in the input table: `patient_col`, `drug_col`, `date_col`, `days_supply_col`.

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

from thomaslab.drugs import build_drug_exposure_episodes

result = build_drug_exposure_episodes(
    fills=sample_df
)

print(result)
~~~

### Related functions

- `normalize_drug_name`
- `map_brand_to_generic`
- `calculate_days_supply`
- `calculate_pdc`
- `calculate_mpr`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drugs.py#L107`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L107)
- Repository search: [build_drug_exposure_episodes](https://github.com/appsplorer/thomaslab-core/search?q=build_drug_exposure_episodes&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build same-drug exposure episodes from dispensing/fill records.

When ``stockpile=True``, an early refill extends coverage from the existing coverage end,
preventing overlapping supplies from double-counting calendar time. A new episode starts
when the next fill begins more than ``grace_days`` after coverage ends.

### API inspection

~~~python
import inspect
from thomaslab.drugs import build_drug_exposure_episodes

print(inspect.signature(build_drug_exposure_episodes))
print(build_drug_exposure_episodes.__doc__)
~~~

### Source

[`src/thomaslab/drugs.py#L107`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L107)

---

<!-- callable:thomaslab.drugs.calculate_pdc -->
## calculate_pdc

### Purpose

Calculate PDC from unique covered calendar days within the observation window.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_pdc( episodes: pd.DataFrame, observation: pd.DataFrame, *, patient_col: str = "patient_id", start_col: str = "episode_start", end_col: str = "episode_end", obs_start_col: str = "observation_start", obs_end_col: str = "observation_end", drug_col: str | None = None, target_drugs: Sequence[str] | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `episodes` | `episodes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `observation` | `observation: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'episode_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'episode_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `obs_start_col` | `obs_start_col: str = 'observation_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `obs_end_col` | `obs_end_col: str = 'observation_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `target_drugs` | `target_drugs: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `episodes`, `observation`.
- Referenced columns must exist in the input table: `patient_col`, `start_col`, `end_col`, `obs_start_col`, `obs_end_col`, `drug_col`.

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

from thomaslab.drugs import calculate_pdc

result = calculate_pdc(
    episodes=sample_df,
    observation=sample_df
)

print(result)
~~~

### Related functions

- `normalize_drug_name`
- `map_brand_to_generic`
- `calculate_days_supply`
- `build_drug_exposure_episodes`
- `calculate_mpr`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drugs.py#L230`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L230)
- Repository search: [calculate_pdc](https://github.com/appsplorer/thomaslab-core/search?q=calculate_pdc&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate PDC from unique covered calendar days within the observation window.

If ``target_drugs`` is supplied, ``drug_col`` is required and coverage is restricted to
those drugs. This avoids accidentally treating unrelated medications as adherence to the
exposure of interest.

### API inspection

~~~python
import inspect
from thomaslab.drugs import calculate_pdc

print(inspect.signature(calculate_pdc))
print(calculate_pdc.__doc__)
~~~

### Source

[`src/thomaslab/drugs.py#L230`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L230)

---

<!-- callable:thomaslab.drugs.calculate_mpr -->
## calculate_mpr

### Purpose

Calculate raw/capped MPR from fills occurring inside observation windows.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_mpr( fills: pd.DataFrame, observation: pd.DataFrame, *, patient_col: str = "patient_id", date_col: str = "fill_date", days_supply_col: str = "days_supply", drug_col: str | None = None, target_drugs: Sequence[str] | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `fills` | `fills: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `observation` | `observation: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str = 'fill_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `days_supply_col` | `days_supply_col: str = 'days_supply'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `target_drugs` | `target_drugs: Sequence[str] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `fills`, `observation`.
- Referenced columns must exist in the input table: `patient_col`, `date_col`, `days_supply_col`, `drug_col`.

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

from thomaslab.drugs import calculate_mpr

result = calculate_mpr(
    fills=sample_df,
    observation=sample_df
)

print(result)
~~~

### Related functions

- `normalize_drug_name`
- `map_brand_to_generic`
- `calculate_days_supply`
- `build_drug_exposure_episodes`
- `calculate_pdc`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drugs.py#L299`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L299)
- Repository search: [calculate_mpr](https://github.com/appsplorer/thomaslab-core/search?q=calculate_mpr&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate raw/capped MPR from fills occurring inside observation windows.

MPR sums supplied days and can exceed 1.0 because of stockpiling; both raw and capped values
are returned. Use ``target_drugs`` to scope the calculation to the intended therapy/class.

### API inspection

~~~python
import inspect
from thomaslab.drugs import calculate_mpr

print(inspect.signature(calculate_mpr))
print(calculate_mpr.__doc__)
~~~

### Source

[`src/thomaslab/drugs.py#L299`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L299)

---

<!-- callable:thomaslab.drugs.calculate_persistence -->
## calculate_persistence

### Purpose

Summarize first continuous exposure episode as persistence duration per patient/drug.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_persistence( episodes: pd.DataFrame, *, patient_col: str = "patient_id", drug_col: str = "drug", start_col: str = "episode_start", end_col: str = "episode_end", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `episodes` | `episodes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'episode_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'episode_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `episodes`.
- Referenced columns must exist in the input table: `patient_col`, `drug_col`, `start_col`, `end_col`.

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

from thomaslab.drugs import calculate_persistence

result = calculate_persistence(
    episodes=sample_df
)

print(result)
~~~

### Related functions

- `normalize_drug_name`
- `map_brand_to_generic`
- `calculate_days_supply`
- `build_drug_exposure_episodes`
- `calculate_pdc`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drugs.py#L359`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L359)
- Repository search: [calculate_persistence](https://github.com/appsplorer/thomaslab-core/search?q=calculate_persistence&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize first continuous exposure episode as persistence duration per patient/drug.

### API inspection

~~~python
import inspect
from thomaslab.drugs import calculate_persistence

print(inspect.signature(calculate_persistence))
print(calculate_persistence.__doc__)
~~~

### Source

[`src/thomaslab/drugs.py#L359`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L359)

---

<!-- callable:thomaslab.drugs.detect_drug_switches -->
## detect_drug_switches

### Purpose

Detect transitions between different drug episodes for the same patient.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_drug_switches( episodes: pd.DataFrame, *, patient_col: str = "patient_id", drug_col: str = "drug", start_col: str = "episode_start", end_col: str = "episode_end", max_transition_gap_days: int = 30, max_overlap_days: int = 1, intensity_order: Mapping[str, float] | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `episodes` | `episodes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'episode_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'episode_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `max_transition_gap_days` | `max_transition_gap_days: int = 30` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `max_overlap_days` | `max_overlap_days: int = 1` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `intensity_order` | `intensity_order: Mapping[str, float] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `episodes`.
- Referenced columns must exist in the input table: `patient_col`, `drug_col`, `start_col`, `end_col`.

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

from thomaslab.drugs import detect_drug_switches

result = detect_drug_switches(
    episodes=sample_df
)

print(result)
~~~

### Related functions

- `normalize_drug_name`
- `map_brand_to_generic`
- `calculate_days_supply`
- `build_drug_exposure_episodes`
- `calculate_pdc`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drugs.py#L383`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L383)
- Repository search: [detect_drug_switches](https://github.com/appsplorer/thomaslab-core/search?q=detect_drug_switches&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Detect transitions between different drug episodes for the same patient.

``intensity_order`` is optional and study-defined. Without it, transitions are labelled
``switch`` only; the library does not infer escalation/de-escalation from drug identity.

### API inspection

~~~python
import inspect
from thomaslab.drugs import detect_drug_switches

print(inspect.signature(detect_drug_switches))
print(detect_drug_switches.__doc__)
~~~

### Source

[`src/thomaslab/drugs.py#L383`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L383)

---

<!-- callable:thomaslab.drugs.detect_discontinuation -->
## detect_discontinuation

### Purpose

Flag apparent discontinuation when final coverage ends before censoring minus grace.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_discontinuation( episodes: pd.DataFrame, observation: pd.DataFrame, *, patient_col: str = "patient_id", drug_col: str = "drug", end_col: str = "episode_end", censor_col: str = "observation_end", grace_days: int = 30, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `episodes` | `episodes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `observation` | `observation: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'episode_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `censor_col` | `censor_col: str = 'observation_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `grace_days` | `grace_days: int = 30` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `episodes`, `observation`.
- Referenced columns must exist in the input table: `patient_col`, `drug_col`, `end_col`, `censor_col`.

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

from thomaslab.drugs import detect_discontinuation

result = detect_discontinuation(
    episodes=sample_df,
    observation=sample_df
)

print(result)
~~~

### Related functions

- `normalize_drug_name`
- `map_brand_to_generic`
- `calculate_days_supply`
- `build_drug_exposure_episodes`
- `calculate_pdc`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drugs.py#L459`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L459)
- Repository search: [detect_discontinuation](https://github.com/appsplorer/thomaslab-core/search?q=detect_discontinuation&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Flag apparent discontinuation when final coverage ends before censoring minus grace.

### API inspection

~~~python
import inspect
from thomaslab.drugs import detect_discontinuation

print(inspect.signature(detect_discontinuation))
print(detect_discontinuation.__doc__)
~~~

### Source

[`src/thomaslab/drugs.py#L459`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L459)

---

<!-- callable:thomaslab.drugs.detect_restarts -->
## detect_restarts

### Purpose

Identify later same-drug episodes after a coverage gap.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_restarts( episodes: pd.DataFrame, *, patient_col: str = "patient_id", drug_col: str = "drug", start_col: str = "episode_start", end_col: str = "episode_end", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `episodes` | `episodes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'episode_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'episode_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `episodes`.
- Referenced columns must exist in the input table: `patient_col`, `drug_col`, `start_col`, `end_col`.

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

from thomaslab.drugs import detect_restarts

result = detect_restarts(
    episodes=sample_df
)

print(result)
~~~

### Related functions

- `normalize_drug_name`
- `map_brand_to_generic`
- `calculate_days_supply`
- `build_drug_exposure_episodes`
- `calculate_pdc`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drugs.py#L491`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L491)
- Repository search: [detect_restarts](https://github.com/appsplorer/thomaslab-core/search?q=detect_restarts&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Identify later same-drug episodes after a coverage gap.

### API inspection

~~~python
import inspect
from thomaslab.drugs import detect_restarts

print(inspect.signature(detect_restarts))
print(detect_restarts.__doc__)
~~~

### Source

[`src/thomaslab/drugs.py#L491`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L491)

---

<!-- callable:thomaslab.drugs.detect_dose_changes -->
## detect_dose_changes

### Purpose

Detect numeric dose changes between consecutive same-drug records.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_dose_changes( fills: pd.DataFrame, *, patient_col: str = "patient_id", drug_col: str = "drug", date_col: str = "fill_date", dose_col: str = "dose", relative_change_threshold: float = 0.0, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `fills` | `fills: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str = 'fill_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `dose_col` | `dose_col: str = 'dose'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `relative_change_threshold` | `relative_change_threshold: float = 0.0` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `fills`.
- Referenced columns must exist in the input table: `patient_col`, `drug_col`, `date_col`, `dose_col`.

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

from thomaslab.drugs import detect_dose_changes

result = detect_dose_changes(
    fills=sample_df
)

print(result)
~~~

### Related functions

- `normalize_drug_name`
- `map_brand_to_generic`
- `calculate_days_supply`
- `build_drug_exposure_episodes`
- `calculate_pdc`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drugs.py#L513`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L513)
- Repository search: [detect_dose_changes](https://github.com/appsplorer/thomaslab-core/search?q=detect_dose_changes&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Detect numeric dose changes between consecutive same-drug records.

### API inspection

~~~python
import inspect
from thomaslab.drugs import detect_dose_changes

print(inspect.signature(detect_dose_changes))
print(detect_dose_changes.__doc__)
~~~

### Source

[`src/thomaslab/drugs.py#L513`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L513)

---

<!-- callable:thomaslab.drugs.detect_concomitant_medications -->
## detect_concomitant_medications

### Purpose

Find overlapping exposure episodes to different drugs within a patient.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def detect_concomitant_medications( episodes: pd.DataFrame, *, patient_col: str = "patient_id", drug_col: str = "drug", start_col: str = "episode_start", end_col: str = "episode_end", min_overlap_days: int = 1, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `episodes` | `episodes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'episode_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'episode_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `min_overlap_days` | `min_overlap_days: int = 1` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `episodes`.
- Referenced columns must exist in the input table: `patient_col`, `drug_col`, `start_col`, `end_col`.

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

from thomaslab.drugs import detect_concomitant_medications

result = detect_concomitant_medications(
    episodes=sample_df
)

print(result)
~~~

### Related functions

- `normalize_drug_name`
- `map_brand_to_generic`
- `calculate_days_supply`
- `build_drug_exposure_episodes`
- `calculate_pdc`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drugs.py#L544`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L544)
- Repository search: [detect_concomitant_medications](https://github.com/appsplorer/thomaslab-core/search?q=detect_concomitant_medications&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Find overlapping exposure episodes to different drugs within a patient.

### API inspection

~~~python
import inspect
from thomaslab.drugs import detect_concomitant_medications

print(inspect.signature(detect_concomitant_medications))
print(detect_concomitant_medications.__doc__)
~~~

### Source

[`src/thomaslab/drugs.py#L544`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L544)

---

<!-- callable:thomaslab.drugs.calculate_polypharmacy -->
## calculate_polypharmacy

### Purpose

Summarize maximum concurrently active distinct drugs per patient.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_polypharmacy( episodes: pd.DataFrame, *, patient_col: str = "patient_id", drug_col: str = "drug", start_col: str = "episode_start", end_col: str = "episode_end", threshold: int = 5, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `episodes` | `episodes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'episode_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `end_col` | `end_col: str = 'episode_end'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `threshold` | `threshold: int = 5` | No | Analysis threshold/cutoff. Pre-specify or justify it; do not tune on the final test set. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `episodes`.
- Referenced columns must exist in the input table: `patient_col`, `drug_col`, `start_col`, `end_col`.

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

from thomaslab.drugs import calculate_polypharmacy

result = calculate_polypharmacy(
    episodes=sample_df
)

print(result)
~~~

### Related functions

- `normalize_drug_name`
- `map_brand_to_generic`
- `calculate_days_supply`
- `build_drug_exposure_episodes`
- `calculate_pdc`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drugs.py#L589`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L589)
- Repository search: [calculate_polypharmacy](https://github.com/appsplorer/thomaslab-core/search?q=calculate_polypharmacy&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize maximum concurrently active distinct drugs per patient.

### API inspection

~~~python
import inspect
from thomaslab.drugs import calculate_polypharmacy

print(inspect.signature(calculate_polypharmacy))
print(calculate_polypharmacy.__doc__)
~~~

### Source

[`src/thomaslab/drugs.py#L589`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L589)

---

<!-- callable:thomaslab.drugs.build_treatment_sequence -->
## build_treatment_sequence

### Purpose

Create ordered drug-stage sequences from episode starts.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_treatment_sequence( episodes: pd.DataFrame, *, patient_col: str = "patient_id", drug_col: str = "drug", start_col: str = "episode_start", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `episodes` | `episodes: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `start_col` | `start_col: str = 'episode_start'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `episodes`.
- Referenced columns must exist in the input table: `patient_col`, `drug_col`, `start_col`.

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

from thomaslab.drugs import build_treatment_sequence

result = build_treatment_sequence(
    episodes=sample_df
)

print(result)
~~~

### Related functions

- `normalize_drug_name`
- `map_brand_to_generic`
- `calculate_days_supply`
- `build_drug_exposure_episodes`
- `calculate_pdc`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drugs.py#L629`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L629)
- Repository search: [build_treatment_sequence](https://github.com/appsplorer/thomaslab-core/search?q=build_treatment_sequence&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create ordered drug-stage sequences from episode starts.

### API inspection

~~~python
import inspect
from thomaslab.drugs import build_treatment_sequence

print(inspect.signature(build_treatment_sequence))
print(build_treatment_sequence.__doc__)
~~~

### Source

[`src/thomaslab/drugs.py#L629`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L629)

---

<!-- callable:thomaslab.drugs.summarize_medication_use -->
## summarize_medication_use

### Purpose

Return descriptive fill counts, first/last fill, and supplied days per patient/drug.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_medication_use( fills: pd.DataFrame, *, patient_col: str = "patient_id", drug_col: str = "drug", date_col: str = "fill_date", days_supply_col: str = "days_supply", ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `fills` | `fills: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str = 'drug'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `date_col` | `date_col: str = 'fill_date'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `days_supply_col` | `days_supply_col: str = 'days_supply'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `fills`.
- Referenced columns must exist in the input table: `patient_col`, `drug_col`, `date_col`, `days_supply_col`.

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

from thomaslab.drugs import summarize_medication_use

result = summarize_medication_use(
    fills=sample_df
)

print(result)
~~~

### Related functions

- `normalize_drug_name`
- `map_brand_to_generic`
- `calculate_days_supply`
- `build_drug_exposure_episodes`
- `calculate_pdc`

### Related workflow

- Guide: [Medication Claims](../../guides/medication-claims.md)
- Guided notebooks: Notebooks 10–12 and 28, 32–35
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/drugs.py#L645`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L645)
- Repository search: [summarize_medication_use](https://github.com/appsplorer/thomaslab-core/search?q=summarize_medication_use&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return descriptive fill counts, first/last fill, and supplied days per patient/drug.

### API inspection

~~~python
import inspect
from thomaslab.drugs import summarize_medication_use

print(inspect.signature(summarize_medication_use))
print(summarize_medication_use.__doc__)
~~~

### Source

[`src/thomaslab/drugs.py#L645`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/drugs.py#L645)

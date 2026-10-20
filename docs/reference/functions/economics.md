# thomaslab.economics

Health-economic research utilities with explicit cost-year/currency provenance.

The library does not provide unit costs, CPI values, exchange rates, willingness-to-pay thresholds,
or utility mappings. Those remain study inputs with source/version documentation.

## Research-use boundary

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

## Self-service orientation

- Related guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 10

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.economics.clean_cost_fields -->
## clean_cost_fields

### Purpose

Coerce named monetary fields to numeric and validate sign policy.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def clean_cost_fields( df: pd.DataFrame, *, cost_columns: Sequence[str], allow_negative_adjustments: bool = False, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `cost_columns` | `cost_columns: Sequence[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `allow_negative_adjustments` | `allow_negative_adjustments: bool = False` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `cost_columns`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

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

from thomaslab.economics import clean_cost_fields

result = clean_cost_fields(
    df=sample_df,
    cost_columns=["feature_a", "feature_b"]
)

print(result)
~~~

### Related functions

- `aggregate_costs`
- `adjust_cost_year`
- `convert_currency`
- `summarize_cost_distribution`
- `bootstrap_mean_cost_difference`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/economics.py#L21`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L21)
- Repository search: [clean_cost_fields](https://github.com/appsplorer/thomaslab-core/search?q=clean_cost_fields&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Coerce named monetary fields to numeric and validate sign policy.

### API inspection

~~~python
import inspect
from thomaslab.economics import clean_cost_fields

print(inspect.signature(clean_cost_fields))
print(clean_cost_fields.__doc__)
~~~

### Source

[`src/thomaslab/economics.py#L21`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L21)

---

<!-- callable:thomaslab.economics.aggregate_costs -->
## aggregate_costs

### Purpose

Aggregate observed costs per patient, optionally with wide category subtotals.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def aggregate_costs( df: pd.DataFrame, *, patient_col: str = "patient_id", amount_col: str = "cost", category_col: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `amount_col` | `amount_col: str = 'cost'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `category_col` | `category_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`.
- Referenced columns must exist in the input table: `patient_col`, `amount_col`, `category_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

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

from thomaslab.economics import aggregate_costs

result = aggregate_costs(
    df=sample_df
)

print(result)
~~~

### Related functions

- `clean_cost_fields`
- `adjust_cost_year`
- `convert_currency`
- `summarize_cost_distribution`
- `bootstrap_mean_cost_difference`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/economics.py#L39`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L39)
- Repository search: [aggregate_costs](https://github.com/appsplorer/thomaslab-core/search?q=aggregate_costs&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Aggregate observed costs per patient, optionally with wide category subtotals.

### API inspection

~~~python
import inspect
from thomaslab.economics import aggregate_costs

print(inspect.signature(aggregate_costs))
print(aggregate_costs.__doc__)
~~~

### Source

[`src/thomaslab/economics.py#L39`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L39)

---

<!-- callable:thomaslab.economics.adjust_cost_year -->
## adjust_cost_year

### Purpose

Adjust monetary amounts with a caller-supplied price index.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def adjust_cost_year( amount: pd.Series | Sequence[float], source_year: pd.Series | Sequence[int] | int, *, target_year: int, price_index: Mapping[int, float], ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `amount` | `amount: pd.Series \| Sequence[float]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `source_year` | `source_year: pd.Series \| Sequence[int] \| int` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `target_year` | `target_year: int` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `price_index` | `price_index: Mapping[int, float]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `amount`, `source_year`, `target_year`, `price_index`.

### Returns

`pd.Series`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.economics import adjust_cost_year

result = adjust_cost_year(
    amount=sample_series,
    source_year=sample_series,
    target_year=2,
    price_index={}
)

print(result)
~~~

### Related functions

- `clean_cost_fields`
- `aggregate_costs`
- `convert_currency`
- `summarize_cost_distribution`
- `bootstrap_mean_cost_difference`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/economics.py#L63`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L63)
- Repository search: [adjust_cost_year](https://github.com/appsplorer/thomaslab-core/search?q=adjust_cost_year&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Adjust monetary amounts with a caller-supplied price index.

Formula: amount * index[target_year] / index[source_year]. The index source/version is not
inferred and should be documented by the study team.

### API inspection

~~~python
import inspect
from thomaslab.economics import adjust_cost_year

print(inspect.signature(adjust_cost_year))
print(adjust_cost_year.__doc__)
~~~

### Source

[`src/thomaslab/economics.py#L63`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L63)

---

<!-- callable:thomaslab.economics.convert_currency -->
## convert_currency

### Purpose

Convert amounts using an explicit caller-supplied FX rate and retain provenance fields.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def convert_currency( amount: pd.Series | Sequence[float], *, fx_rate: float, from_currency: str, to_currency: str, rate_date_or_period: str, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `amount` | `amount: pd.Series \| Sequence[float]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `fx_rate` | `fx_rate: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `from_currency` | `from_currency: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `to_currency` | `to_currency: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `rate_date_or_period` | `rate_date_or_period: str` | Yes | Temporal value or setting. Confirm time zero, ordering, observation windows, and censoring semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `amount`, `fx_rate`, `from_currency`, `to_currency`, `rate_date_or_period`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
import pandas as pd

sample_series = pd.Series([0.2, 0.8, 0.4, 0.6])

from thomaslab.economics import convert_currency

result = convert_currency(
    amount=sample_series,
    fx_rate=0.5,
    from_currency="value",
    to_currency="value",
    rate_date_or_period="value"
)

print(result)
~~~

### Related functions

- `clean_cost_fields`
- `aggregate_costs`
- `adjust_cost_year`
- `summarize_cost_distribution`
- `bootstrap_mean_cost_difference`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/economics.py#L91`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L91)
- Repository search: [convert_currency](https://github.com/appsplorer/thomaslab-core/search?q=convert_currency&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Convert amounts using an explicit caller-supplied FX rate and retain provenance fields.

### API inspection

~~~python
import inspect
from thomaslab.economics import convert_currency

print(inspect.signature(convert_currency))
print(convert_currency.__doc__)
~~~

### Source

[`src/thomaslab/economics.py#L91`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L91)

---

<!-- callable:thomaslab.economics.summarize_cost_distribution -->
## summarize_cost_distribution

### Purpose

Summarize skewed cost distributions without assuming normality.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def summarize_cost_distribution( df: pd.DataFrame, *, cost_col: str, group_col: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `cost_col` | `cost_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `group_col` | `group_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `cost_col`.
- Referenced columns must exist in the input table: `cost_col`, `group_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

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

from thomaslab.economics import summarize_cost_distribution

result = summarize_cost_distribution(
    df=sample_df,
    cost_col='cost'
)

print(result)
~~~

### Related functions

- `clean_cost_fields`
- `aggregate_costs`
- `adjust_cost_year`
- `convert_currency`
- `bootstrap_mean_cost_difference`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/economics.py#L116`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L116)
- Repository search: [summarize_cost_distribution](https://github.com/appsplorer/thomaslab-core/search?q=summarize_cost_distribution&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Summarize skewed cost distributions without assuming normality.

### API inspection

~~~python
import inspect
from thomaslab.economics import summarize_cost_distribution

print(inspect.signature(summarize_cost_distribution))
print(summarize_cost_distribution.__doc__)
~~~

### Source

[`src/thomaslab/economics.py#L116`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L116)

---

<!-- callable:thomaslab.economics.bootstrap_mean_cost_difference -->
## bootstrap_mean_cost_difference

### Purpose

Bootstrap the unadjusted mean cost difference between two groups.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def bootstrap_mean_cost_difference( df: pd.DataFrame, *, cost_col: str, group_col: str, treated_value: object, comparator_value: object, n_boot: int = 1000, random_state: int = 42, ci: float = 0.95, ) -> dict[str, float]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `cost_col` | `cost_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `group_col` | `group_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `treated_value` | `treated_value: object` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `comparator_value` | `comparator_value: object` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `n_boot` | `n_boot: int = 1000` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `random_state` | `random_state: int = 42` | No | Reproducibility seed. Record it in the study bundle. |
| `ci` | `ci: float = 0.95` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `cost_col`, `group_col`, `treated_value`, `comparator_value`.
- Referenced columns must exist in the input table: `cost_col`, `group_col`.

### Returns

`dict[str, float]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

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

sample_value = "replace_with_validated_value"

from thomaslab.economics import bootstrap_mean_cost_difference

result = bootstrap_mean_cost_difference(
    df=sample_df,
    cost_col='cost',
    group_col='group',
    treated_value=sample_value,
    comparator_value=sample_value
)

print(result)
~~~

### Related functions

- `clean_cost_fields`
- `aggregate_costs`
- `adjust_cost_year`
- `convert_currency`
- `summarize_cost_distribution`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/economics.py#L144`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L144)
- Repository search: [bootstrap_mean_cost_difference](https://github.com/appsplorer/thomaslab-core/search?q=bootstrap_mean_cost_difference&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Bootstrap the unadjusted mean cost difference between two groups.

### API inspection

~~~python
import inspect
from thomaslab.economics import bootstrap_mean_cost_difference

print(inspect.signature(bootstrap_mean_cost_difference))
print(bootstrap_mean_cost_difference.__doc__)
~~~

### Source

[`src/thomaslab/economics.py#L144`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L144)

---

<!-- callable:thomaslab.economics.calculate_qalys -->
## calculate_qalys

### Purpose

Calculate observed QALYs as trapezoidal area under utility-time measurements.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_qalys( utility: pd.DataFrame, *, patient_col: str = "patient_id", time_col: str = "time_years", utility_col: str = "utility", clamp_utility: tuple[float, float] | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `utility` | `utility: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `time_col` | `time_col: str = 'time_years'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `utility_col` | `utility_col: str = 'utility'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `clamp_utility` | `clamp_utility: tuple[float, float] \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `utility`.
- Referenced columns must exist in the input table: `patient_col`, `time_col`, `utility_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

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

from thomaslab.economics import calculate_qalys

result = calculate_qalys(
    utility=sample_df
)

print(result)
~~~

### Related functions

- `clean_cost_fields`
- `aggregate_costs`
- `adjust_cost_year`
- `convert_currency`
- `summarize_cost_distribution`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/economics.py#L185`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L185)
- Repository search: [calculate_qalys](https://github.com/appsplorer/thomaslab-core/search?q=calculate_qalys&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate observed QALYs as trapezoidal area under utility-time measurements.

### API inspection

~~~python
import inspect
from thomaslab.economics import calculate_qalys

print(inspect.signature(calculate_qalys))
print(calculate_qalys.__doc__)
~~~

### Source

[`src/thomaslab/economics.py#L185`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L185)

---

<!-- callable:thomaslab.economics.calculate_icer -->
## calculate_icer

### Purpose

Calculate ICER and cost-effectiveness-plane quadrant from supplied increments.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_icer(*, incremental_cost: float, incremental_qaly: float) -> dict[str, object]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `incremental_cost` | `incremental_cost: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `incremental_qaly` | `incremental_qaly: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `incremental_cost`, `incremental_qaly`.

### Returns

`dict[str, object]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.economics import calculate_icer

result = calculate_icer(
    incremental_cost=0.5,
    incremental_qaly=0.5
)

print(result)
~~~

### Related functions

- `clean_cost_fields`
- `aggregate_costs`
- `adjust_cost_year`
- `convert_currency`
- `summarize_cost_distribution`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/economics.py#L230`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L230)
- Repository search: [calculate_icer](https://github.com/appsplorer/thomaslab-core/search?q=calculate_icer&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Calculate ICER and cost-effectiveness-plane quadrant from supplied increments.

### API inspection

~~~python
import inspect
from thomaslab.economics import calculate_icer

print(inspect.signature(calculate_icer))
print(calculate_icer.__doc__)
~~~

### Source

[`src/thomaslab/economics.py#L230`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L230)

---

<!-- callable:thomaslab.economics.calculate_net_monetary_benefit -->
## calculate_net_monetary_benefit

### Purpose

Return net monetary benefit using a caller-specified willingness-to-pay threshold.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_net_monetary_benefit( *, incremental_cost: float, incremental_qaly: float, willingness_to_pay: float ) -> float
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `incremental_cost` | `incremental_cost: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `incremental_qaly` | `incremental_qaly: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `willingness_to_pay` | `willingness_to_pay: float` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `incremental_cost`, `incremental_qaly`, `willingness_to_pay`.

### Returns

`float`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.economics import calculate_net_monetary_benefit

result = calculate_net_monetary_benefit(
    incremental_cost=0.5,
    incremental_qaly=0.5,
    willingness_to_pay=0.5
)

print(result)
~~~

### Related functions

- `clean_cost_fields`
- `aggregate_costs`
- `adjust_cost_year`
- `convert_currency`
- `summarize_cost_distribution`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/economics.py#L254`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L254)
- Repository search: [calculate_net_monetary_benefit](https://github.com/appsplorer/thomaslab-core/search?q=calculate_net_monetary_benefit&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return net monetary benefit using a caller-specified willingness-to-pay threshold.

### API inspection

~~~python
import inspect
from thomaslab.economics import calculate_net_monetary_benefit

print(inspect.signature(calculate_net_monetary_benefit))
print(calculate_net_monetary_benefit.__doc__)
~~~

### Source

[`src/thomaslab/economics.py#L254`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L254)

---

<!-- callable:thomaslab.economics.build_economic_endpoint_table -->
## build_economic_endpoint_table

### Purpose

Combine one-row-per-patient cost totals with optional observed QALY summaries.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_economic_endpoint_table( costs: pd.DataFrame, *, patient_col: str = "patient_id", qaly: pd.DataFrame | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `costs` | `costs: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `patient_col` | `patient_col: str = 'patient_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `qaly` | `qaly: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `costs`.
- Referenced columns must exist in the input table: `patient_col`.

### Returns

`pd.DataFrame`

### Output guidance

Returns a table-like research artifact. Inspect row count, column definitions, dtypes, missingness, and any attrs/provenance before downstream use.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Review source semantics, units, code systems, temporal definitions, missingness, and study assumptions before interpreting outputs.

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

from thomaslab.economics import build_economic_endpoint_table

result = build_economic_endpoint_table(
    costs=sample_df
)

print(result)
~~~

### Related functions

- `clean_cost_fields`
- `aggregate_costs`
- `adjust_cost_year`
- `convert_currency`
- `summarize_cost_distribution`

### Related workflow

- Guide: [Hcru Economics](../../guides/hcru-economics.md)
- Guided notebooks: Notebooks 30–31
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/economics.py#L264`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L264)
- Repository search: [build_economic_endpoint_table](https://github.com/appsplorer/thomaslab-core/search?q=build_economic_endpoint_table&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Combine one-row-per-patient cost totals with optional observed QALY summaries.

### API inspection

~~~python
import inspect
from thomaslab.economics import build_economic_endpoint_table

print(inspect.signature(build_economic_endpoint_table))
print(build_economic_endpoint_table.__doc__)
~~~

### Source

[`src/thomaslab/economics.py#L264`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/economics.py#L264)

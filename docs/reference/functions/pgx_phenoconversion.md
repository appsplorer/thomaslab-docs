# thomaslab.pgx_phenoconversion

Medication-mediated pharmacogenomic phenoconversion utilities.

## Research-use boundary

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

## Self-service orientation

- Related guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 5

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.pgx_phenoconversion.normalize_inhibitor_strength -->
## normalize_inhibitor_strength

### Purpose

Normalize inhibitor strength without inferring it from a drug name.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def normalize_inhibitor_strength(value: object) -> str
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `value` | `value: object` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `value`.

### Returns

`str`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.pgx_phenoconversion import normalize_inhibitor_strength

result = normalize_inhibitor_strength(
    value={"key": "value"}
)

print(result)
~~~

### Related functions

- `strongest_inhibitor_strength`
- `adjust_cyp2d6_activity_score`
- `classify_cyp2d6_inhibitors`
- `apply_cyp2d6_phenoconversion`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_phenoconversion.py#L14`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_phenoconversion.py#L14)
- Repository search: [normalize_inhibitor_strength](https://github.com/appsplorer/thomaslab-core/search?q=normalize_inhibitor_strength&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Normalize inhibitor strength without inferring it from a drug name.

### API inspection

~~~python
import inspect
from thomaslab.pgx_phenoconversion import normalize_inhibitor_strength

print(inspect.signature(normalize_inhibitor_strength))
print(normalize_inhibitor_strength.__doc__)
~~~

### Source

[`src/thomaslab/pgx_phenoconversion.py#L14`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_phenoconversion.py#L14)

---

<!-- callable:thomaslab.pgx_phenoconversion.strongest_inhibitor_strength -->
## strongest_inhibitor_strength

### Purpose

Return the strongest explicitly supplied inhibitor category.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def strongest_inhibitor_strength(values: Iterable[object]) -> str
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `values` | `values: Iterable[object]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `values`.

### Returns

`str`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
sample_value = "replace_with_validated_value"

from thomaslab.pgx_phenoconversion import strongest_inhibitor_strength

result = strongest_inhibitor_strength(
    values=sample_value
)

print(result)
~~~

### Related functions

- `normalize_inhibitor_strength`
- `adjust_cyp2d6_activity_score`
- `classify_cyp2d6_inhibitors`
- `apply_cyp2d6_phenoconversion`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_phenoconversion.py#L32`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_phenoconversion.py#L32)
- Repository search: [strongest_inhibitor_strength](https://github.com/appsplorer/thomaslab-core/search?q=strongest_inhibitor_strength&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return the strongest explicitly supplied inhibitor category.

### API inspection

~~~python
import inspect
from thomaslab.pgx_phenoconversion import strongest_inhibitor_strength

print(inspect.signature(strongest_inhibitor_strength))
print(strongest_inhibitor_strength.__doc__)
~~~

### Source

[`src/thomaslab/pgx_phenoconversion.py#L32`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_phenoconversion.py#L32)

---

<!-- callable:thomaslab.pgx_phenoconversion.adjust_cyp2d6_activity_score -->
## adjust_cyp2d6_activity_score

### Purpose

Adjust CYP2D6 activity score for inhibitor-mediated phenoconversion.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def adjust_cyp2d6_activity_score(activity_score: float | int, inhibitor_strength: object) -> float
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `activity_score` | `activity_score: float \| int` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `inhibitor_strength` | `inhibitor_strength: object` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `activity_score`, `inhibitor_strength`.

### Returns

`float`

### Output guidance

Returns a scalar/label. Interpret it only in the context of the documented inputs, assumptions, and study definition.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.pgx_phenoconversion import adjust_cyp2d6_activity_score

result = adjust_cyp2d6_activity_score(
    activity_score=2,
    inhibitor_strength="value"
)

print(result)
~~~

### Related functions

- `normalize_inhibitor_strength`
- `strongest_inhibitor_strength`
- `classify_cyp2d6_inhibitors`
- `apply_cyp2d6_phenoconversion`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_phenoconversion.py#L38`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_phenoconversion.py#L38)
- Repository search: [adjust_cyp2d6_activity_score](https://github.com/appsplorer/thomaslab-core/search?q=adjust_cyp2d6_activity_score&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Adjust CYP2D6 activity score for inhibitor-mediated phenoconversion.

Strong inhibitors set activity score to 0; moderate inhibitors multiply it by
0.5; weak/no inhibitor leaves it unchanged. Drug-to-strength classification
must be supplied by the study from a reviewed source.

### API inspection

~~~python
import inspect
from thomaslab.pgx_phenoconversion import adjust_cyp2d6_activity_score

print(inspect.signature(adjust_cyp2d6_activity_score))
print(adjust_cyp2d6_activity_score.__doc__)
~~~

### Source

[`src/thomaslab/pgx_phenoconversion.py#L38`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_phenoconversion.py#L38)

---

<!-- callable:thomaslab.pgx_phenoconversion.classify_cyp2d6_inhibitors -->
## classify_cyp2d6_inhibitors

### Purpose

Classify a medication list using an explicit drug-to-strength mapping.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def classify_cyp2d6_inhibitors( medications: Iterable[object], inhibitor_map: Mapping[str, str], ) -> dict[str, object]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `medications` | `medications: Iterable[object]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `inhibitor_map` | `inhibitor_map: Mapping[str, str]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `medications`, `inhibitor_map`.

### Returns

`dict[str, object]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
sample_value = "replace_with_validated_value"

from thomaslab.pgx_phenoconversion import classify_cyp2d6_inhibitors

result = classify_cyp2d6_inhibitors(
    medications=sample_value,
    inhibitor_map={}
)

print(result)
~~~

### Related functions

- `normalize_inhibitor_strength`
- `strongest_inhibitor_strength`
- `adjust_cyp2d6_activity_score`
- `apply_cyp2d6_phenoconversion`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_phenoconversion.py#L56`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_phenoconversion.py#L56)
- Repository search: [classify_cyp2d6_inhibitors](https://github.com/appsplorer/thomaslab-core/search?q=classify_cyp2d6_inhibitors&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Classify a medication list using an explicit drug-to-strength mapping.

### API inspection

~~~python
import inspect
from thomaslab.pgx_phenoconversion import classify_cyp2d6_inhibitors

print(inspect.signature(classify_cyp2d6_inhibitors))
print(classify_cyp2d6_inhibitors.__doc__)
~~~

### Source

[`src/thomaslab/pgx_phenoconversion.py#L56`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_phenoconversion.py#L56)

---

<!-- callable:thomaslab.pgx_phenoconversion.apply_cyp2d6_phenoconversion -->
## apply_cyp2d6_phenoconversion

### Purpose

Return genotype-based and inhibitor-adjusted CYP2D6 phenotypes.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def apply_cyp2d6_phenoconversion( activity_score: float | int, inhibitor_strength: object, ) -> dict[str, object]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `activity_score` | `activity_score: float \| int` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `inhibitor_strength` | `inhibitor_strength: object` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `activity_score`, `inhibitor_strength`.

### Returns

`dict[str, object]`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.pgx_phenoconversion import apply_cyp2d6_phenoconversion

result = apply_cyp2d6_phenoconversion(
    activity_score=2,
    inhibitor_strength="value"
)

print(result)
~~~

### Related functions

- `normalize_inhibitor_strength`
- `strongest_inhibitor_strength`
- `adjust_cyp2d6_activity_score`
- `classify_cyp2d6_inhibitors`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_phenoconversion.py#L73`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_phenoconversion.py#L73)
- Repository search: [apply_cyp2d6_phenoconversion](https://github.com/appsplorer/thomaslab-core/search?q=apply_cyp2d6_phenoconversion&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return genotype-based and inhibitor-adjusted CYP2D6 phenotypes.

### API inspection

~~~python
import inspect
from thomaslab.pgx_phenoconversion import apply_cyp2d6_phenoconversion

print(inspect.signature(apply_cyp2d6_phenoconversion))
print(apply_cyp2d6_phenoconversion.__doc__)
~~~

### Source

[`src/thomaslab/pgx_phenoconversion.py#L73`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_phenoconversion.py#L73)

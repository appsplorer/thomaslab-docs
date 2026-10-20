# thomaslab.pgx_guidelines

Versioned pharmacogenomic knowledge and research-concordance utilities.

## Research-use boundary

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

## Self-service orientation

- Related guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 3

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.pgx_guidelines.load_pgx_knowledge -->
## load_pgx_knowledge

### Purpose

Load and validate a local versioned PGx knowledge artifact.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def load_pgx_knowledge(source: str | Path | Mapping[str, Any]) -> dict[str, Any]
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

from thomaslab.pgx_guidelines import load_pgx_knowledge

result = load_pgx_knowledge(
    source=sample_df
)

print(result)
~~~

### Related functions

- `lookup_pgx_rule`
- `audit_pgx_concordance`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_guidelines.py#L13`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_guidelines.py#L13)
- Repository search: [load_pgx_knowledge](https://github.com/appsplorer/thomaslab-core/search?q=load_pgx_knowledge&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Load and validate a local versioned PGx knowledge artifact.

### API inspection

~~~python
import inspect
from thomaslab.pgx_guidelines import load_pgx_knowledge

print(inspect.signature(load_pgx_knowledge))
print(load_pgx_knowledge.__doc__)
~~~

### Source

[`src/thomaslab/pgx_guidelines.py#L13`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_guidelines.py#L13)

---

<!-- callable:thomaslab.pgx_guidelines.lookup_pgx_rule -->
## lookup_pgx_rule

### Purpose

Lookup one research rule by gene/drug/phenotype/optional indication.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def lookup_pgx_rule( knowledge: str | Path | Mapping[str, Any], *, gene: str, drug: str, phenotype: str, indication: str | None = None, ) -> dict[str, Any] | None
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `knowledge` | `knowledge: str \| Path \| Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `gene` | `gene: str` | Yes | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |
| `drug` | `drug: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `phenotype` | `phenotype: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `indication` | `indication: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `knowledge`, `gene`, `drug`, `phenotype`.

### Returns

`dict[str, Any] | None`

### Output guidance

Returns a mapping of results/diagnostics. Inspect documented keys and preserve diagnostics/provenance with the primary result.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.pgx_guidelines import lookup_pgx_rule

result = lookup_pgx_rule(
    knowledge={},
    gene="CYP2C19",
    drug="value",
    phenotype="value"
)

print(result)
~~~

### Related functions

- `load_pgx_knowledge`
- `audit_pgx_concordance`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_guidelines.py#L37`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_guidelines.py#L37)
- Repository search: [lookup_pgx_rule](https://github.com/appsplorer/thomaslab-core/search?q=lookup_pgx_rule&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Lookup one research rule by gene/drug/phenotype/optional indication.

### API inspection

~~~python
import inspect
from thomaslab.pgx_guidelines import lookup_pgx_rule

print(inspect.signature(lookup_pgx_rule))
print(lookup_pgx_rule.__doc__)
~~~

### Source

[`src/thomaslab/pgx_guidelines.py#L37`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_guidelines.py#L37)

---

<!-- callable:thomaslab.pgx_guidelines.audit_pgx_concordance -->
## audit_pgx_concordance

### Purpose

Audit research concordance against explicit, versioned rule categories.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_pgx_concordance( df: pd.DataFrame, knowledge: str | Path | Mapping[str, Any], *, phenotype_col: str, drug_col: str, actual_action_col: str, gene: str, indication_col: str | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `knowledge` | `knowledge: str \| Path \| Mapping[str, Any]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `phenotype_col` | `phenotype_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug_col` | `drug_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `actual_action_col` | `actual_action_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `gene` | `gene: str` | Yes | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |
| `indication_col` | `indication_col: str \| None = None` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `knowledge`, `phenotype_col`, `drug_col`, `actual_action_col`, `gene`.
- Referenced columns must exist in the input table: `phenotype_col`, `drug_col`, `actual_action_col`, `indication_col`.

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

from thomaslab.pgx_guidelines import audit_pgx_concordance

result = audit_pgx_concordance(
    df=sample_df,
    knowledge={},
    phenotype_col='phenotype',
    drug_col='drug',
    actual_action_col='actual_action',
    gene="CYP2C19"
)

print(result)
~~~

### Related functions

- `load_pgx_knowledge`
- `lookup_pgx_rule`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_guidelines.py#L72`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_guidelines.py#L72)
- Repository search: [audit_pgx_concordance](https://github.com/appsplorer/thomaslab-core/search?q=audit_pgx_concordance&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Audit research concordance against explicit, versioned rule categories.

Rules may specify ``concordant_actions`` as normalized study categories. This is
a retrospective/implementation-research audit and does not issue a prescription.

### API inspection

~~~python
import inspect
from thomaslab.pgx_guidelines import audit_pgx_concordance

print(inspect.signature(audit_pgx_concordance))
print(audit_pgx_concordance.__doc__)
~~~

### Source

[`src/thomaslab/pgx_guidelines.py#L72`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_guidelines.py#L72)

# thomaslab.pgx_assay

Multisite pharmacogenomic assay-panel quality-control utilities.

## Research-use boundary

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

## Self-service orientation

- Related guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 5

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.pgx_assay.build_assay_panel -->
## build_assay_panel

### Purpose

Create a serializable assay-panel definition.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def build_assay_panel( *, site_id: str, gene: str, tested_alleles: Iterable[object], assay_name: str, assay_version: str | None = None, method: str | None = None, ) -> dict[str, Any]
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `site_id` | `site_id: str` | Yes | Identifier or identifier column. Confirm uniqueness/grouping semantics before analysis. |
| `gene` | `gene: str` | Yes | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |
| `tested_alleles` | `tested_alleles: Iterable[object]` | Yes | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |
| `assay_name` | `assay_name: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `assay_version` | `assay_version: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `method` | `method: str \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `site_id`, `gene`, `tested_alleles`, `assay_name`.

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
from thomaslab.pgx_assay import build_assay_panel

result = build_assay_panel(
    site_id="value",
    gene="CYP2C19",
    tested_alleles="*1",
    assay_name="value"
)

print(result)
~~~

### Related functions

- `assay_panels_to_frame`
- `compare_assay_panels`
- `audit_required_allele_coverage`
- `audit_reported_alleles_against_panel`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_assay.py#L13`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_assay.py#L13)
- Repository search: [build_assay_panel](https://github.com/appsplorer/thomaslab-core/search?q=build_assay_panel&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Create a serializable assay-panel definition.

### API inspection

~~~python
import inspect
from thomaslab.pgx_assay import build_assay_panel

print(inspect.signature(build_assay_panel))
print(build_assay_panel.__doc__)
~~~

### Source

[`src/thomaslab/pgx_assay.py#L13`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_assay.py#L13)

---

<!-- callable:thomaslab.pgx_assay.assay_panels_to_frame -->
## assay_panels_to_frame

### Purpose

Normalize assay panel dictionaries into one row per site/gene/allele.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def assay_panels_to_frame(panels: Iterable[dict[str, Any]]) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `panels` | `panels: Iterable[dict[str, Any]]` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `panels`.

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
from thomaslab.pgx_assay import assay_panels_to_frame

result = assay_panels_to_frame(
    panels={}
)

print(result)
~~~

### Related functions

- `build_assay_panel`
- `compare_assay_panels`
- `audit_required_allele_coverage`
- `audit_reported_alleles_against_panel`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_assay.py#L36`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_assay.py#L36)
- Repository search: [assay_panels_to_frame](https://github.com/appsplorer/thomaslab-core/search?q=assay_panels_to_frame&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Normalize assay panel dictionaries into one row per site/gene/allele.

### API inspection

~~~python
import inspect
from thomaslab.pgx_assay import assay_panels_to_frame

print(inspect.signature(assay_panels_to_frame))
print(assay_panels_to_frame.__doc__)
~~~

### Source

[`src/thomaslab/pgx_assay.py#L36`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_assay.py#L36)

---

<!-- callable:thomaslab.pgx_assay.compare_assay_panels -->
## compare_assay_panels

### Purpose

Pairwise compare tested allele coverage across sites.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def compare_assay_panels(panel_frame: pd.DataFrame, gene: str | None = None) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `panel_frame` | `panel_frame: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `gene` | `gene: str \| None = None` | No | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `panel_frame`.

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

from thomaslab.pgx_assay import compare_assay_panels

result = compare_assay_panels(
    panel_frame=sample_df
)

print(result)
~~~

### Related functions

- `build_assay_panel`
- `assay_panels_to_frame`
- `audit_required_allele_coverage`
- `audit_reported_alleles_against_panel`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_assay.py#L61`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_assay.py#L61)
- Repository search: [compare_assay_panels](https://github.com/appsplorer/thomaslab-core/search?q=compare_assay_panels&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Pairwise compare tested allele coverage across sites.

### API inspection

~~~python
import inspect
from thomaslab.pgx_assay import compare_assay_panels

print(inspect.signature(compare_assay_panels))
print(compare_assay_panels.__doc__)
~~~

### Source

[`src/thomaslab/pgx_assay.py#L61`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_assay.py#L61)

---

<!-- callable:thomaslab.pgx_assay.audit_required_allele_coverage -->
## audit_required_allele_coverage

### Purpose

Report per-site coverage of a study-defined required allele set.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_required_allele_coverage( panel_frame: pd.DataFrame, required_alleles: Iterable[object], *, gene: str, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `panel_frame` | `panel_frame: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `required_alleles` | `required_alleles: Iterable[object]` | Yes | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |
| `gene` | `gene: str` | Yes | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `panel_frame`, `required_alleles`, `gene`.

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

from thomaslab.pgx_assay import audit_required_allele_coverage

result = audit_required_allele_coverage(
    panel_frame=sample_df,
    required_alleles="*1",
    gene="CYP2C19"
)

print(result)
~~~

### Related functions

- `build_assay_panel`
- `assay_panels_to_frame`
- `compare_assay_panels`
- `audit_reported_alleles_against_panel`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_assay.py#L91`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_assay.py#L91)
- Repository search: [audit_required_allele_coverage](https://github.com/appsplorer/thomaslab-core/search?q=audit_required_allele_coverage&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Report per-site coverage of a study-defined required allele set.

### API inspection

~~~python
import inspect
from thomaslab.pgx_assay import audit_required_allele_coverage

print(inspect.signature(audit_required_allele_coverage))
print(audit_required_allele_coverage.__doc__)
~~~

### Source

[`src/thomaslab/pgx_assay.py#L91`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_assay.py#L91)

---

<!-- callable:thomaslab.pgx_assay.audit_reported_alleles_against_panel -->
## audit_reported_alleles_against_panel

### Purpose

Flag reported non-reference alleles absent from that site's declared assay panel.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def audit_reported_alleles_against_panel( results: pd.DataFrame, panel_frame: pd.DataFrame, *, site_col: str = "site_id", gene_col: str = "gene", allele_cols: tuple[str, str] = ("allele_1", "allele_2"), ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `results` | `results: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `panel_frame` | `panel_frame: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `site_col` | `site_col: str = 'site_id'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `gene_col` | `gene_col: str = 'gene'` | No | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `allele_cols` | `allele_cols: tuple[str, str] = ('allele_1', 'allele_2')` | No | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `results`, `panel_frame`.
- Referenced columns must exist in the input table: `site_col`, `gene_col`.

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

from thomaslab.pgx_assay import audit_reported_alleles_against_panel

result = audit_reported_alleles_against_panel(
    results=sample_df,
    panel_frame=sample_df
)

print(result)
~~~

### Related functions

- `build_assay_panel`
- `assay_panels_to_frame`
- `compare_assay_panels`
- `audit_required_allele_coverage`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx_assay.py#L119`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_assay.py#L119)
- Repository search: [audit_reported_alleles_against_panel](https://github.com/appsplorer/thomaslab-core/search?q=audit_reported_alleles_against_panel&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Flag reported non-reference alleles absent from that site's declared assay panel.

Reference ``*1`` is not flagged because many assays infer it by absence of tested
variants; this function does not certify that such a reference call is complete.

### API inspection

~~~python
import inspect
from thomaslab.pgx_assay import audit_reported_alleles_against_panel

print(inspect.signature(audit_reported_alleles_against_panel))
print(audit_reported_alleles_against_panel.__doc__)
~~~

### Source

[`src/thomaslab/pgx_assay.py#L119`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx_assay.py#L119)

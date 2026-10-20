# thomaslab.pgx

Pharmacogenomics and clinical pharmacogenetic score utilities.

## Research-use boundary

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

## Self-service orientation

- Related guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Start unfamiliar data with the [new dataset wizard](../../new-dataset/README.md).

**Documented public callables:** 7

**Implementation source:** Private; available to authorized Thomas Lab collaborators.

---

<!-- callable:thomaslab.pgx.map_star_alleles_to_phenotype -->
## map_star_alleles_to_phenotype

### Purpose

Map common CYP2C19 star-allele pairs to CPIC metabolizer phenotypes.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def map_star_alleles_to_phenotype( df: pd.DataFrame, allele_1_col: str, allele_2_col: str, gene: str = "CYP2C19", ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `allele_1_col` | `allele_1_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `allele_2_col` | `allele_2_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `gene` | `gene: str = 'CYP2C19'` | No | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `allele_1_col`, `allele_2_col`.
- Referenced columns must exist in the input table: `allele_1_col`, `allele_2_col`.

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

from thomaslab.pgx import map_star_alleles_to_phenotype

result = map_star_alleles_to_phenotype(
    df=sample_df,
    allele_1_col='allele_1',
    allele_2_col='allele_2'
)

print(result)
~~~

### Related functions

- `compute_abcd_gene_score`
- `calculate_pgx_risk_score`
- `assign_cpic_guideline_recommendation`
- `parse_vcf_to_star_alleles`
- `compute_polygenic_risk_score_fast`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx.py#L33`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx.py#L33)
- Repository search: [map_star_alleles_to_phenotype](https://github.com/appsplorer/thomaslab-core/search?q=map_star_alleles_to_phenotype&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Map common CYP2C19 star-allele pairs to CPIC metabolizer phenotypes.

Unsupported or ambiguous diplotypes return ``'Unknown'`` rather than being inferred.

### API inspection

~~~python
import inspect
from thomaslab.pgx import map_star_alleles_to_phenotype

print(inspect.signature(map_star_alleles_to_phenotype))
print(map_star_alleles_to_phenotype.__doc__)
~~~

### Source

[`src/thomaslab/pgx.py#L33`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx.py#L33)

---

<!-- callable:thomaslab.pgx.compute_abcd_gene_score -->
## compute_abcd_gene_score

### Purpose

Compute the published ABCD-GENE score and <10/≥10 risk category.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def compute_abcd_gene_score( df: pd.DataFrame, age_col: str, bmi_col: str, egfr_col: str, diabetes_col: str, cyp2c19_lof_count_col: str, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `age_col` | `age_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `bmi_col` | `bmi_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `egfr_col` | `egfr_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `diabetes_col` | `diabetes_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `cyp2c19_lof_count_col` | `cyp2c19_lof_count_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `age_col`, `bmi_col`, `egfr_col`, `diabetes_col`, `cyp2c19_lof_count_col`.
- Referenced columns must exist in the input table: `age_col`, `bmi_col`, `egfr_col`, `diabetes_col`, `cyp2c19_lof_count_col`.

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

from thomaslab.pgx import compute_abcd_gene_score

result = compute_abcd_gene_score(
    df=sample_df,
    age_col='age',
    bmi_col='bmi',
    egfr_col='egfr',
    diabetes_col='diabetes',
    cyp2c19_lof_count_col='cyp2c19_lof_count'
)

print(result)
~~~

### Related functions

- `map_star_alleles_to_phenotype`
- `calculate_pgx_risk_score`
- `assign_cpic_guideline_recommendation`
- `parse_vcf_to_star_alleles`
- `compute_polygenic_risk_score_fast`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx.py#L85`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx.py#L85)
- Repository search: [compute_abcd_gene_score](https://github.com/appsplorer/thomaslab-core/search?q=compute_abcd_gene_score&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compute the published ABCD-GENE score and <10/≥10 risk category.

Published weights: age >75 (+4), BMI >30 (+4), eGFR <60 (+3), diabetes (+3),
one CYP2C19 loss-of-function allele (+6), two LOF alleles (+24).

### API inspection

~~~python
import inspect
from thomaslab.pgx import compute_abcd_gene_score

print(inspect.signature(compute_abcd_gene_score))
print(compute_abcd_gene_score.__doc__)
~~~

### Source

[`src/thomaslab/pgx.py#L85`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx.py#L85)

---

<!-- callable:thomaslab.pgx.calculate_pgx_risk_score -->
## calculate_pgx_risk_score

### Purpose

Compute an additive weighted genomic risk score from dosage-like variants.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def calculate_pgx_risk_score( df: pd.DataFrame, variant_cols: list[str], weights: list[float], ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `variant_cols` | `variant_cols: list[str]` | Yes | Names of validated input columns. Exclude leakage/proxy variables that violate the study design. |
| `weights` | `weights: list[float]` | Yes | Analysis weight/propensity input. Inspect support, positivity, extremes, and effective sample size where applicable. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `variant_cols`, `weights`.

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

from thomaslab.pgx import calculate_pgx_risk_score

result = calculate_pgx_risk_score(
    df=sample_df,
    variant_cols=["feature_a", "feature_b"],
    weights=0.5
)

print(result)
~~~

### Related functions

- `map_star_alleles_to_phenotype`
- `compute_abcd_gene_score`
- `assign_cpic_guideline_recommendation`
- `parse_vcf_to_star_alleles`
- `compute_polygenic_risk_score_fast`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx.py#L126`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx.py#L126)
- Repository search: [calculate_pgx_risk_score](https://github.com/appsplorer/thomaslab-core/search?q=calculate_pgx_risk_score&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compute an additive weighted genomic risk score from dosage-like variants.

### API inspection

~~~python
import inspect
from thomaslab.pgx import calculate_pgx_risk_score

print(inspect.signature(calculate_pgx_risk_score))
print(calculate_pgx_risk_score.__doc__)
~~~

### Source

[`src/thomaslab/pgx.py#L126`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx.py#L126)

---

<!-- callable:thomaslab.pgx.assign_cpic_guideline_recommendation -->
## assign_cpic_guideline_recommendation

### Purpose

Return a CPIC-2022 research-rule label for CYP2C19/clopidogrel.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def assign_cpic_guideline_recommendation( df: pd.DataFrame, phenotype_col: str, drug: str = "clopidogrel", indication: str = "acs_pci", ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `df` | `df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `phenotype_col` | `phenotype_col: str` | Yes | Name of the corresponding validated input column; the column must exist and have the expected study semantics. |
| `drug` | `drug: str = 'clopidogrel'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `indication` | `indication: str = 'acs_pci'` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `df`, `phenotype_col`.
- Referenced columns must exist in the input table: `phenotype_col`.

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

from thomaslab.pgx import assign_cpic_guideline_recommendation

result = assign_cpic_guideline_recommendation(
    df=sample_df,
    phenotype_col='phenotype'
)

print(result)
~~~

### Related functions

- `map_star_alleles_to_phenotype`
- `compute_abcd_gene_score`
- `calculate_pgx_risk_score`
- `parse_vcf_to_star_alleles`
- `compute_polygenic_risk_score_fast`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx.py#L145`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx.py#L145)
- Repository search: [assign_cpic_guideline_recommendation](https://github.com/appsplorer/thomaslab-core/search?q=assign_cpic_guideline_recommendation&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Return a CPIC-2022 research-rule label for CYP2C19/clopidogrel.

This function encodes guideline categories for research reproducibility, not patient-specific
prescribing. For ACS/PCI, normal/rapid/ultrarapid phenotypes map to standard-dose clopidogrel;
intermediate/poor phenotypes map to avoiding standard clopidogrel when possible and considering
an alternative P2Y12 inhibitor if clinically appropriate and not contraindicated.

### API inspection

~~~python
import inspect
from thomaslab.pgx import assign_cpic_guideline_recommendation

print(inspect.signature(assign_cpic_guideline_recommendation))
print(assign_cpic_guideline_recommendation.__doc__)
~~~

### Source

[`src/thomaslab/pgx.py#L145`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx.py#L145)

---

<!-- callable:thomaslab.pgx.parse_vcf_to_star_alleles -->
## parse_vcf_to_star_alleles

### Purpose

Parse a VCF into conservative star-allele calls for target genes.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def parse_vcf_to_star_alleles( vcf_file_path: str, target_genes: list[str] | None = None, *, allele_definitions: pd.DataFrame | None = None, ) -> pd.DataFrame
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `vcf_file_path` | `vcf_file_path: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `target_genes` | `target_genes: list[str] \| None = None` | No | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |
| `allele_definitions` | `allele_definitions: pd.DataFrame \| None = None` | No | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `vcf_file_path`.

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
from thomaslab.pgx import parse_vcf_to_star_alleles

result = parse_vcf_to_star_alleles(
    vcf_file_path="path/to/input.csv"
)

print(result)
~~~

### Related functions

- `map_star_alleles_to_phenotype`
- `compute_abcd_gene_score`
- `calculate_pgx_risk_score`
- `assign_cpic_guideline_recommendation`
- `compute_polygenic_risk_score_fast`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx.py#L228`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx.py#L228)
- Repository search: [parse_vcf_to_star_alleles](https://github.com/appsplorer/thomaslab-core/search?q=parse_vcf_to_star_alleles&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Parse a VCF into conservative star-allele calls for target genes.

Generic VCF data are not sufficient to infer complex pharmacogenes safely. In
particular, CYP2D6 commonly requires copy-number, structural-variant, and
phasing information. Therefore this function only makes a call when all marker
loci in a supplied *single-marker-per-star-allele* definition set are present.

When ``allele_definitions`` is omitted, the function provides a conservative
marker-based implementation for common CYP2C19 ``*2``, ``*3``, and ``*17``
loci identified by rsID. CYP2D6 and SLCO1B1 return ``definition_required``
rather than fabricated diplotypes.

Parameters
----------
vcf_file_path:
    Path to a diploid VCF/VCF-like text file. Compressed ``.vcf.gz`` is
    supported.
target_genes:
    Pharmacogenes to report.
allele_definitions:
    Optional DataFrame containing ``gene``, ``variant_id``, and ``star_allele``.
    Each star allele must be represented by exactly one defining marker in this
    lightweight parser. Complex haplotypes should be called by a dedicated
    PharmVar-aware caller upstream.

Returns
-------
pandas.DataFrame
    One row per sample/gene with allele calls, diplotype, status, and CYP2C19
    phenotype when available.

### API inspection

~~~python
import inspect
from thomaslab.pgx import parse_vcf_to_star_alleles

print(inspect.signature(parse_vcf_to_star_alleles))
print(parse_vcf_to_star_alleles.__doc__)
~~~

### Source

[`src/thomaslab/pgx.py#L228`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx.py#L228)

---

<!-- callable:thomaslab.pgx.compute_polygenic_risk_score_fast -->
## compute_polygenic_risk_score_fast

### Purpose

Compute additive polygenic risk scores from long-form genotype dosages.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def compute_polygenic_risk_score_fast( vcf_df: pd.DataFrame, weights_df: pd.DataFrame, ) -> pd.Series
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `vcf_df` | `vcf_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |
| `weights_df` | `weights_df: pd.DataFrame` | Yes | Input table. Validate required columns, units, timing, missingness, and provenance before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `vcf_df`, `weights_df`.

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

from thomaslab.pgx import compute_polygenic_risk_score_fast

result = compute_polygenic_risk_score_fast(
    vcf_df=sample_df,
    weights_df=sample_df
)

print(result)
~~~

### Related functions

- `map_star_alleles_to_phenotype`
- `compute_abcd_gene_score`
- `calculate_pgx_risk_score`
- `assign_cpic_guideline_recommendation`
- `parse_vcf_to_star_alleles`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx.py#L445`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx.py#L445)
- Repository search: [compute_polygenic_risk_score_fast](https://github.com/appsplorer/thomaslab-core/search?q=compute_polygenic_risk_score_fast&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Compute additive polygenic risk scores from long-form genotype dosages.

``vcf_df`` must contain ``variant_id`` and either ``dosage`` or ``gt``. A
``sample_id`` column is optional for a single-sample score. When ``ref``/``alt``
and ``effect_allele`` are available, REF-effect weights are automatically
oriented as ``2 - ALT dosage``.

### API inspection

~~~python
import inspect
from thomaslab.pgx import compute_polygenic_risk_score_fast

print(inspect.signature(compute_polygenic_risk_score_fast))
print(compute_polygenic_risk_score_fast.__doc__)
~~~

### Source

[`src/thomaslab/pgx.py#L445`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx.py#L445)

---

<!-- callable:thomaslab.pgx.map_drug_gene_phenotype_network -->
## map_drug_gene_phenotype_network

### Purpose

Build a drug-gene-phenotype interaction graph from local source tables.

### When to use

Use this callable when its purpose matches a pre-specified step in the study workflow and the required source semantics have been validated. It should not be used merely because similarly named columns are present.

### Signature

~~~python
def map_drug_gene_phenotype_network( drug_name: str, gene: str, *, pharmgkb_source: object | None = None, drugbank_source: object | None = None, ) -> object
~~~

### Parameters

| Parameter | Declaration | Required | Meaning |
|---|---|:---:|---|
| `drug_name` | `drug_name: str` | Yes | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `gene` | `gene: str` | Yes | PGx value. Confirm assay coverage, nomenclature, knowledge-source version, and unresolved states. |
| `pharmgkb_source` | `pharmgkb_source: object \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |
| `drugbank_source` | `drugbank_source: object \| None = None` | No | Study-specific argument. Follow the declared type/default and source documentation; validate semantics before use. |

### Input contract

- Use data that have passed the relevant schema, temporal, missingness, and provenance checks.
- Supply arguments using the meanings documented below; do not rely on column-name similarity alone.
- Required arguments: `drug_name`, `gene`.

### Returns

`object`

### Output guidance

Inspect the returned object and its documented metadata/diagnostics before passing it downstream.

### Raises

No separate `Raises` section is documented in the source docstring. Invalid, ambiguous, unsupported, or structurally inconsistent inputs may still fail closed; review the source tests and domain guide before study use.

### Guardrails

Clinical, medication, assay, genotype, endpoint, and coding semantics require source- and study-specific review. Outputs are research artifacts, not autonomous clinical guidance.

### Implementation example

The following is a synthetic implementation template. It is intentionally small and contains no patient data. Replace synthetic values only after validating the new dataset's schema, units, timing, code systems, and study definitions.

~~~python
from thomaslab.pgx import map_drug_gene_phenotype_network

result = map_drug_gene_phenotype_network(
    drug_name="value",
    gene="CYP2C19"
)

print(result)
~~~

### Related functions

- `map_star_alleles_to_phenotype`
- `compute_abcd_gene_score`
- `calculate_pgx_risk_score`
- `assign_cpic_guideline_recommendation`
- `parse_vcf_to_star_alleles`

### Related workflow

- Guide: [Pgx](../../guides/pgx.md)
- Guided notebooks: Notebooks 10–17 and 24–25
- Cookbook: [Self-service implementation cookbook](../../examples/self-service-cookbook.md)

### Verification

- Source: [`src/thomaslab/pgx.py#L518`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx.py#L518)
- Repository search: [map_drug_gene_phenotype_network](https://github.com/appsplorer/thomaslab-core/search?q=map_drug_gene_phenotype_network&type=code)
- Local software gate: `python scripts/local_quality_gate.py --quick`

### Source documentation

Build a drug-gene-phenotype interaction graph from local source tables.

DrugBank redistribution is licensed and PharmGKB exports are versioned, so this
function deliberately does not scrape or silently download either resource.
Supply DataFrames/CSV/TSV exports (or set ``THOMASLAB_PHARMGKB_PATH`` and/or
``THOMASLAB_DRUGBANK_PATH``) to produce a reproducible NetworkX graph.

### API inspection

~~~python
import inspect
from thomaslab.pgx import map_drug_gene_phenotype_network

print(inspect.signature(map_drug_gene_phenotype_network))
print(map_drug_gene_phenotype_network.__doc__)
~~~

### Source

[`src/thomaslab/pgx.py#L518`](https://github.com/appsplorer/thomaslab-core/blob/main/src/thomaslab/pgx.py#L518)

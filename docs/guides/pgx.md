# Pharmacogenomics

## CYP2C19 phenotype mapping

The package implements a conservative subset of common CYP2C19 diplotypes. It distinguishes:

- Normal metabolizer
- Rapid metabolizer
- Ultrarapid metabolizer
- Intermediate metabolizer
- Poor metabolizer
- `Unknown` for unsupported/ambiguous combinations

```python
from thomaslab.pgx import map_star_alleles_to_phenotype

cohort["phenotype"] = map_star_alleles_to_phenotype(
    cohort,
    allele_1_col="cyp2c19_a1",
    allele_2_col="cyp2c19_a2",
)
```

!!! warning
    Star-allele definitions and CPIC recommendations evolve. For a manuscript or clinical implementation study, document the allele-definition release and guideline version used. Do not infer rare diplotypes from this helper.

## ABCD-GENE score

`compute_abcd_gene_score` uses the published weighting used in clopidogrel/PCI literature:

| Component | Points |
|---|---:|
| Age > 75 years | 4 |
| BMI > 30 kg/m² | 4 |
| CKD / eGFR < 60 mL/min/1.73m² | 3 |
| Diabetes | 3 |
| One CYP2C19 loss-of-function allele | 6 |
| Two loss-of-function alleles | 24 |

The helper returns the numeric score and a binary high-risk classification based on a threshold of **10**.

```python
from thomaslab.pgx import compute_abcd_gene_score

score = compute_abcd_gene_score(
    cohort,
    age_col="age",
    bmi_col="bmi",
    egfr_col="egfr",
    diabetes_col="diabetes",
    cyp2c19_lof_count_col="lof_count",
)
```

## CPIC-oriented recommendation labels

`assign_cpic_guideline_recommendation` creates **research labels**, not prescribing orders. CPIC clopidogrel recommendations depend on phenotype and clinical indication, especially ACS/PCI. The function must therefore be treated as an analytic abstraction and validated against the protocol-specific CPIC version before use.

## VCF, PRS, and interaction networks

### Conservative VCF star-allele calling

```python
from thomaslab.pgx import parse_vcf_to_star_alleles

calls = parse_vcf_to_star_alleles(
    "cohort.vcf.gz",
    target_genes=["CYP2C19", "CYP2D6"],
    allele_definitions=validated_marker_definitions,
)
```

A generic VCF does **not** guarantee sufficient phasing, locus coverage, copy-number information, or structural-variant representation for complex pharmacogenes. The function returns explicit status codes such as `definition_required`, `insufficient_locus_coverage`, and `ambiguous_unphased` instead of inventing a diplotype.

### Polygenic risk scores

`compute_polygenic_risk_score_fast` joins long-form genotype dosages to a versioned weight table and orients dosage to the stated effect allele when REF/ALT are available.

### PharmGKB / DrugBank network inputs

`map_drug_gene_phenotype_network` reads local, versioned source exports. It intentionally does not scrape DrugBank or silently download licensed data.


## Version 0.8 foundation

For new studies, prefer the gene-specific v0.8 modules described in [PGx foundation](pgx-foundation.md). The original helpers remain available for backward compatibility.

The v0.8 design keeps assay coverage, allele function, CYP2D6 activity score, predicted phenotype, phenoconversion, and research guideline-concordance as separate provenance-bearing objects.

## Indication-specific PGx research rules — data-integrity boundary

The low-level `lookup_pgx_rule` concordance lookup only matches a rule with a named indication (such as `acs_pci`) when the calling study provides that indication explicitly. Missing indication, a different indication, or an unreviewed label must **not** be treated as an ACS/PCI recommendation. Generic `any` rules remain possible, subject to the reviewed knowledge version.

```python
from thomaslab.pgx_guidelines import lookup_pgx_rule

# Synthetic reviewed rule artifact; not a prescription or universal guidance.
kb = {"knowledge_id": "demonstration", "version": "test-1", "rules": [
    {"rule_id": "pci_example", "gene": "CYP2C19", "drug": "clopidogrel",
     "phenotypes": ["Intermediate"], "indication": "acs_pci",
     "concordant_actions": ["alternative_p2y12"]}
]}
assert lookup_pgx_rule(kb, gene="CYP2C19", drug="clopidogrel",
                       phenotype="Intermediate", indication=None) is None
assert lookup_pgx_rule(kb, gene="CYP2C19", drug="clopidogrel",
                       phenotype="Intermediate", indication="acs_pci") is not None
```

**Evidence status:** Dedicated tests are being introduced on the private audit branch; those changes are not considered released until exact-commit CI and the lab's local verification gate pass. The example only demonstrates conservative rule matching.

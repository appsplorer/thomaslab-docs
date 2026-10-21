# PGx foundation: CYP2C19, CYP2D6, assay QC, and phenoconversion

Version 0.8 separates PGx into auditable layers so a lab member can distinguish **laboratory result**, **allele function**, **activity score**, **predicted phenotype**, **assay coverage**, **drug-mediated phenoconversion**, and **research guideline-concordance**.

## CYP2C19 pipeline

```text
reported star alleles
      ↓
allele-function table
      ↓
diplotype function combination
      ↓
Normal / Rapid / Ultrarapid
Intermediate / Poor
Likely IM / Likely PM / Indeterminate
      ↓
research drug-gene concordance
```

```python
from thomaslab.pgx_cyp2c19 import translate_cyp2c19_diplotype

result = translate_cyp2c19_diplotype("*1/*2")
```

Unknown alleles return `Unknown`; they are not silently treated as `*1`.

## CYP2D6 pipeline

```text
validated diplotype/CNV result
      ↓
allele activity values × copy number
      ↓
genetic activity score
      ↓
predicted phenotype
      ↓
strong/moderate inhibitor adjustment
      ↓
clinical phenotype for research
```

The convenience subset uses the current standardized CYP2D6 phenotype thresholds:

| Activity score | Phenotype |
|---:|---|
| 0 | Poor |
| >0 and <1.25 | Intermediate |
| 1.25–2.25 | Normal |
| >2.25 | Ultrarapid |

Do not infer CYP2D6 structural variants from ordinary VCF SNVs. Pass a validated diplotype/CNV result from an appropriate upstream caller.

## Phenoconversion

`thomaslab.pgx_phenoconversion` deliberately does **not** classify drugs autonomously. Supply an inhibitor-strength mapping reviewed for the study.

```python
from thomaslab.pgx_phenoconversion import apply_cyp2d6_phenoconversion

result = apply_cyp2d6_phenoconversion(
    activity_score=2.0,
    inhibitor_strength="moderate",
)
```

Strong CYP2D6 inhibitors set activity score to 0; moderate inhibitors multiply by 0.5; weak inhibitors do not alter the score in this implementation.

## Multisite assay-panel QC

Different sites may interrogate different alleles. Before pooling PGx cohorts:

```python
from thomaslab.pgx_assay import audit_required_allele_coverage

coverage = audit_required_allele_coverage(
    panel_frame,
    required_alleles=["*2", "*3", "*4", "*17"],
    gene="CYP2C19",
)
```

A reported `*1` does not prove full locus interrogation. The library therefore separates **reported result** from **assay coverage**.

## Versioned PGx knowledge

Files under `pgx_knowledge/` are reviewable local artifacts. They record the research abstraction/version used for an analysis. Replace convenience subsets with comprehensive, version-pinned source exports when required by a manuscript or clinical implementation protocol.

## Research concordance, not prescribing

`audit_pgx_concordance` compares observed study categories against a versioned rule artifact. It does not issue patient-specific treatment instructions.

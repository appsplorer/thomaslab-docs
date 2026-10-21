# PGx implementation-science workflows

The implementation module quantifies whether pharmacogenomic testing reached the right population, returned in time, yielded a study-defined actionable result, and was incorporated into a study-defined action.

## Implementation funnel

```text
eligible
   ↓
ordered
   ↓
completed
   ↓
actionable
   ↓
acted on
```

```python
from thomaslab.implementation import build_pgx_implementation_funnel

funnel = build_pgx_implementation_funnel(
    cohort,
    eligible_col="eligible",
    ordered_col="ordered",
    completed_col="completed",
    actionable_col="actionable",
    acted_on_col="acted_on",
)
```

Every stage uses the preceding stage as its conversion denominator and also reports fraction of the initially eligible population.

## Turnaround time

```python
turnaround = calculate_genotype_turnaround_time(
    cohort,
    order_date_col="test_order_date",
    result_date_col="test_result_date",
)
```

Negative order-to-result intervals are flagged invalid rather than converted to absolute values.

## Result availability before prescribing

`calculate_result_before_prescribing_rate` evaluates whether a dated result was available on or before a dated prescribing event. It does not establish that the prescriber actually saw or used the result.

## Actionability

`calculate_actionable_genotype_rate` requires an explicit phenotype set supplied by the study. Actionability can depend on gene, drug, indication and guideline version, so it is intentionally not inferred globally.

## Concordance

Use `thomaslab.pgx_guidelines.audit_pgx_concordance` first with a versioned rule artifact. Then `calculate_guideline_concordance_rate` summarizes only evaluable rows.

These are implementation-research metrics, not clinical recommendations.

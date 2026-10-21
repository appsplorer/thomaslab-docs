# End-to-end EHR workflow

A robust real-world study should make the patient timeline explicit before feature engineering starts.

## Canonical timeline

```text
eligibility lookback            baseline window         index           follow-up
<-----------------------------><---------------------->|-------------------------------->
                                                      t0
```

Typical implementation order:

1. **Resolve patient identity** using the approved source-system identifier strategy.
2. **Define time zero (`t0`)** from the protocol: e.g., PCI date, first qualifying prescription, admission, or genotyping result.
3. **Apply eligibility criteria** using only information allowed by the study protocol.
4. **Apply exclusions** with explicit temporal scope (ever, prior year, prior 30 days, etc.).
5. **Construct baseline covariates** from data at or before `t0`.
6. **Assign treatment/exposure** using a prespecified window and avoid immortal-time bias.
7. **Start outcome surveillance** at the protocol-defined time.
8. **Censor** at outcome, death, loss of observability, treatment-switch rule, or administrative end as specified.

## Database connections

`connect_db` reads JSON/YAML configuration and returns a SQLAlchemy engine. Keep credentials outside the repository and use environment-secret injection in production.

```yaml
# local example only; do not commit real secrets
url: postgresql+psycopg://user:password@host:5432/clinical
```

## Cohort construction

`filter_cohort` is intentionally conservative. A manuscript-specific cohort should usually be encoded as project SQL plus tested Python transformations, rather than hidden inside a generic helper.

```python
from thomaslab.data import filter_cohort

eligible = filter_cohort(
    exposure_rows,
    drug_code="CLOPIDOGREL_CODE",
    min_age=18,
    start_date="2020-01-01",
)
```

## Baseline labs

Use `aggregate_lab_features` only after the index date is known. Check units and reference ranges before aggregation; mixing mg/dL and µmol/L, for example, is a data-engineering error, not a modeling problem.

## Charlson Comorbidity Index

`compute_charlson_index` implements an ICD-10-oriented weighted Charlson abstraction. For publication, freeze the exact diagnosis mapping and confirm that it matches the intended CCI implementation and lookback period.

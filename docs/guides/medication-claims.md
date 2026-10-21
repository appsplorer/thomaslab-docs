# Medication exposure and claims workflows

Version 0.7 adds a reusable longitudinal medication and claims layer for P2Y12 inhibitors, PPIs, opioids, beta-blockers, and future drug classes.

## Design principles

The library separates **what the data say** from **what the study assumes**:

- brand/local-formulary mappings must be supplied explicitly;
- therapeutic equivalence is not inferred from names;
- escalation/de-escalation labels require a reviewed study-specific ordering;
- NDC/RxNorm crosswalks are not fabricated;
- PDC counts unique covered days; MPR sums supplied days and may exceed 1.0;
- new-user designs require an explicit washout and index event;
- continuous enrollment is checked against the requested baseline window;
- days supply derived from quantity/frequency is an approximation and should not replace a trustworthy source field.

## Build exposure episodes

```python
import pandas as pd
from thomaslab.drugs import build_drug_exposure_episodes

fills = pd.read_csv("pharmacy_fills.csv")
episodes = build_drug_exposure_episodes(
    fills,
    patient_col="patient_id",
    drug_col="drug",
    date_col="fill_date",
    days_supply_col="days_supply",
    grace_days=14,
    stockpile=True,
)
```

With stockpiling enabled, an early refill extends existing coverage instead of double-counting calendar days.

## Adherence and persistence

```python
from thomaslab.drugs import calculate_pdc, calculate_mpr

pdc = calculate_pdc(
    episodes,
    observation,
    drug_col="drug",
    target_drugs=["clopidogrel"],
)

mpr = calculate_mpr(
    fills,
    observation,
    drug_col="drug",
    target_drugs=["clopidogrel"],
)
```

PDC and MPR answer different questions. The package returns both raw and capped MPR and never silently treats unrelated medications as adherence when a target list is supplied.

## Treatment switching

```python
from thomaslab.drugs import detect_drug_switches

switches = detect_drug_switches(episodes)
```

Without an explicit ordering, transitions are labelled simply `switch`. If a study protocol defines an analytical order, pass it explicitly:

```python
switches = detect_drug_switches(
    episodes,
    intensity_order={"clopidogrel": 1, "ticagrelor": 2, "prasugrel": 2},
)
```

This ordering is a study configuration, not a patient-level treatment recommendation.

## Claims-style new-user cohort

```python
from thomaslab.claims import build_new_user_cohort

cohort = build_new_user_cohort(
    index=index_events,
    pharmacy=pharmacy_claims,
    enrollment=enrollment,
    target_drugs=["clopidogrel", "ticagrelor", "prasugrel"],
    washout_days=365,
    initiation_window_days=30,
)
```

The output keeps explicit flags for prior exposure, post-index initiation, continuous enrollment, final eligibility, and exclusion reason.

## Recommended sequence for a new claims dataset

```text
onboard source
    ↓
validate pharmacy/enrollment contracts
    ↓
normalize codes/names using reviewed mappings
    ↓
identify index event from explicit code set
    ↓
check continuous enrollment
    ↓
apply washout/new-user rule
    ↓
identify treatment initiation
    ↓
build refill/exposure episodes
    ↓
PDC / MPR / persistence
    ↓
switching / overlap / discontinuation / restart
    ↓
analysis dataset + provenance
```

## Interpretation safeguards

A pharmacy fill is evidence of dispensing/claim activity, not proof that the patient ingested the medication. PDC/MPR are adherence proxies. A gap in claims can reflect discontinuation, insurance changes, cash payment, samples, inpatient supply, or missing data. These functions operationalize prespecified research definitions; they do not establish clinical truth.

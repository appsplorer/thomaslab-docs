# Drug safety and medication surveillance

Version 0.18 adds an auditable safety-research layer above the existing medication-exposure, claims, phenotype, NLP, and pharmacoepidemiology modules.

## Recommended EHR/claims workflow

~~~text
reviewed exposure episodes
        +
reviewed adverse-event phenotype
        ↓
explicit risk + background windows
        ↓
window-overlap audit
        ↓
exposure–event linkage
        ↓
seriousness / severity evidence
        ↓
descriptive event-rate comparison
        ↓
clinical/statistical review
~~~

Use build_exposure_risk_windows() to construct protocol-defined time windows. The package never selects a biologically correct risk window automatically. Run audit_safety_windows() before denominator-based summaries because overlapping windows can double-count person-time and link the same event more than once.

link_exposure_events() performs temporal linkage only. It does not classify an event as an adverse drug reaction. classify_seriousness_evidence() also keeps **seriousness** separate from **severity** and preserves rows where seriousness cannot be assessed from the available evidence.

## Dechallenge and rechallenge

build_dechallenge_rechallenge_timeline() records explicit dates for drug stop, event resolution, later re-exposure, and recurrence after re-exposure. The output deliberately labels causal interpretation as not_established. Temporal improvement after withdrawal or recurrence after re-exposure can support review, but it does not prove drug causality.

## Drug–drug interaction research

build_drug_drug_interaction_table() requires a reviewed drug-pair definition table and returns observed co-exposure intervals. Co-exposure does not prove that a pharmacokinetic, pharmacodynamic, or clinical interaction occurred.

## Denominator-based surveillance

thomaslab.surveillance summarizes explicit risk/background person-time and crude event rates. build_safety_signal_table() reports descriptive risk-window versus background-window incidence-rate ratios and records when a zero-cell continuity correction was used.

These summaries do not adjust for confounding, informative observation, competing events, event-dependent exposure, or repeated-event correlation. Use the appropriate causal, survival, or recurrent-event layers when the study question requires those methods.

## Spontaneous-report disproportionality

calculate_disproportionality() and build_disproportionality_table() calculate report-level reporting odds ratios (ROR) and proportional reporting ratios (PRR) after collapsing duplicate rows within a report. These are **reporting measures**, not incidence rates or causal effect estimates. They are sensitive to reporting practices, duplicate or linked reports, coding choices, stimulated reporting, and missing denominators.

## Operational review thresholds

audit_signal_evidence() can apply a study-configured minimum case count to decide whether a row is ready for human review. This is an operational workflow threshold only. It is not a clinical signal-detection rule and must not be presented as regulatory confirmation.

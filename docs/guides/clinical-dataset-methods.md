# All of Us, MIMIC-IV and hospital EHR methods — source-aware API

**Implementation:** private `thomaslab-core` [hardening PR #34](https://github.com/appsplorer/thomaslab-core/pull/34).
**Status:** candidate with synthetic regression cases; no actual credentialed
All of Us, MIMIC-IV or hospital records were accessed during development.
An independent HPC test pass at the *new exact commit* is still required.

## Documentation-backed distinctions

- [All of Us CDR v9 dictionaries](https://support.researchallofus.org/hc/en-us/articles/360033200232-Data-Dictionaries):
  CDR release **Registered R2025Q4R6** or **Controlled C2025Q4R6**
  (June 26, 2026); source structures include OMOP 5.3 and programme-specific
  survey, wearable, genomic and multi-omics data. Individual-level records
  remain in the authorized **Researcher Workbench**. The Controlled Tier
  includes genomics and sensitive additional fields. Query-builder execution
  and participant-level extracts are not implemented outside the Workbench.
- [All of Us survey transformation](https://support.researchallofus.org/hc/en-us/articles/6085114880148-Introduction-to-All-of-Us-Survey-Collection-and-Data-Transformation-Methods):
  OMOP `observation` stores coded PPI answers; **903096 = PMI_SKIP**,
  intentionally unspecified, not a negative clinical result.
- [All of Us v9 expanded sources](https://support.researchallofus.org/hc/en-us/articles/50653909888788-Our-Largest-Genomic-Dataset-Curated-Data-Repository-version-9):
  recent sleep summaries, clinical notes, srWGS/lrWGS, expression and
  proteomics do not become interchangeable numeric tables.
- [MIMIC-IV v3.1](https://physionet.org/content/mimiciv/3.1/),
  [hospital module](https://mimic.mit.edu/docs/iv/modules/hosp/),
  [ICU module](https://mimic.mit.edu/docs/iv/modules/icu/):
  distinct patient `subject_id`, admission `hadm_id` and ICU `stay_id`
  identifiers, **patient-specific time shifts**, and specialised table
  grain/clinical event semantics. Do not group deidentified years across
  patients as though they were real calendar years.
- [MIMIC prescriptions](https://mimic.mit.edu/docs/iv/modules/hosp/prescriptions.html)
  are medication *orders*; [eMAR](https://mimic.mit.edu/docs/iv/modules/hosp/emar.html)
  records administration-related events, including **Not Given**.
  Do not infer administration/adherence from an order.
- [MIMIC labs](https://mimic.mit.edu/docs/iv/modules/hosp/labevents.html)
  can lack `hadm_id` for legitimate reasons; assess time linkage and
  dictionary version rather than dropping those observations.

The shared [cross-dataset clinical quality guide](cross-dataset-clinical-quality.md)
covers reviewed-code fingerprints, missing/unknown codes, medication
order/dispense/admin status, external-site future holdouts and small-site
disclosure preflights. No result is automatically approved for publication.

See also [All of Us aggregate disclosure restrictions](aou-disclosure.md):
the generic `export_governed_bundle` is **not** an All of Us egress
mechanism, and the in-memory preflight never certifies a table for release.

## New source-aware code

| Module | Functions | Scope |
|---|---|---|
| `healthcare_sources` | `SourceContext`, `assess_source_access`, `inspect_source_table`, `relationship_integrity`, `visit_window_integrity` | source classification, structural patient/admission/table relationships; no rights conferred |
| `healthcare_omop` | `omop_concept_integrity`, `omop_person_visit_integrity`, `omop_observation_period_integrity`, `omop_measurement_quality` | concept dictionary coverage, patient/visit linkage, period chronology, numeric/units quality |
| `healthcare_aou_domains` | `aou_survey_response_quality`, `aou_wearable_daily_quality`, `aou_omics_provenance_quality` | PPI skip, Fitbit/day quality and controlled-tier omics metadata (no variant calling) |
| `healthcare_aou_query` | `plan_aou_omop_domain_query` | **non-executing** parameterized Workbench-specific OMOP v9 query plan |
| `healthcare_mimic` | `mimic_anchor_age_quality`, `mimic_stay_relationship_quality`, `mimic_lab_event_quality`, `mimic_prescription_quality`, `mimic_icd_version_quality`, `mimic_emar_quality`, `mimic_lab_dictionary_integrity`, `mimic_icu_chart_quality`, `mimic_order_to_emar_linkage_quality` | anchored age top-coding, hospital/ICU, shifted times, lab dictionary, orders vs eMAR, ICD-9/10 |
| `healthcare_hospital` | `hospital_encounter_quality`, `hospital_lab_quality`, `hospital_medication_quality`, `count_preindex_events`, `hospital_intervisit_gap_quality` | configurable site EHR, lab units, ordered/admin events, strictly preindex counts and noncausal encounter gaps |
| `healthcare_cohorts` | `cohort_attrition_summary`, `build_index_event_cohort`, `followup_event_quality` | prespecified eligibility flow, earliest observed code-defined index (not disease onset), censor-aware followup completeness checks |
| `healthcare_quality` | `code_set_manifest`, `clinical_code_coverage`, `medication_state_summary`, `site_temporal_holdout_preflight`, `site_missingness_preflight` | cross-source provenance, medication states, site/temporal generalization, disclosure preflights |
| `healthcare_foundation` | structural profiling, required-column contracts, split leakage, binary/regression/KM descriptive baselines | research-only summary baselines with no clinical utility claims |

**No automatic source-to-OMOP coding or unit conversion.** The software
preserves codes and identifies mismatches. Domain experts must approve the
correct vocabulary versions, lab units, time-zero definitions and clinical
phenotype algorithms.

## Synthetic All of Us OMOP and surveys

~~~python
import pandas as pd
from thomaslab.healthcare_omop import (
    omop_concept_integrity, omop_person_visit_integrity,
)
from thomaslab.healthcare_aou_domains import aou_survey_response_quality

# INVENTED rows, not Researcher Workbench data.
person = pd.DataFrame({"person_id": [101, 102]})
visits = pd.DataFrame({"person_id": [101], "visit_occurrence_id": [1001]})
observations = pd.DataFrame({
    "observation_id": [1, 2], "person_id": [101, 102],
    "visit_occurrence_id": pd.Series([1001, None], dtype="Int64"),
    "observation_concept_id": [123, 123],
    "value_as_concept_id": [903096, 456],
})
concept = pd.DataFrame({"concept_id": [123, 456]})
print(omop_person_visit_integrity(person, visits, observations))
print(omop_concept_integrity(
    observations, concept, concept_column="observation_concept_id"))
print(aou_survey_response_quality(observations))
~~~

In a **properly authorized Workbench context**, the non-executing query
planner builds a restricted domain query with bound concept IDs and dates
instead of string-interpolated SQL values. Project IDs and dataset releases
must be verified against the selected Workbench reference resource.

~~~python
from datetime import date
from thomaslab.healthcare_sources import SourceContext
from thomaslab.healthcare_aou_query import plan_aou_omop_domain_query

# The following synthetic metadata does NOT authenticate Workbench access.
ctx = SourceContext(
    family="all_of_us", release="registered_v9",
    environment="all_of_us_workbench", classification="RESTRICTED",
    authorization_reference="EXAMPLE_ONLY",
    responsible_steward="EXAMPLE_ONLY",
)
plan = plan_aou_omop_domain_query(
    context=ctx, approved_project_id="wb-affable-acorn-7941",
    table="condition_occurrence", concept_ids=(201826,),
    start_date=date(2022, 1, 1), end_date=date(2023, 1, 1),
)
assert plan.executed is False
# DO NOT log SQL parameters containing patient IDs or export query results.
~~~

This does not automatically execute SQL or grant IAM authorization.

## Synthetic MIMIC-IV v3.1 medical events

~~~python
import pandas as pd
from thomaslab.healthcare_mimic import (
    mimic_anchor_age_quality, mimic_prescription_quality, mimic_emar_quality,
)

patients = pd.DataFrame({
    "subject_id": [1], "anchor_age": [91], "anchor_year": [2158]})
orders = pd.DataFrame({
    "subject_id": [1], "hadm_id": [2001], "drug": ["SYNTHETIC_DRUG"],
    "starttime": ["2158-01-01"], "stoptime": ["2158-01-03"]})
emar = pd.DataFrame({
    "subject_id": [1], "emar_id": ["1-1"], "emar_seq": [1],
    "charttime": ["2158-01-02"], "event_txt": ["Not Given"]})
print(mimic_anchor_age_quality(patients))
print(mimic_prescription_quality(orders))
print(mimic_emar_quality(emar))
~~~

Age 91 is top-coded, not exact age. The synthetic order is not an
administration and `Not Given` is not counted as given. Credentialed MIMIC
access, its DUA and its licensing/derivation terms remain independent.

## Hospital EHR without assuming its schema

~~~python
from thomaslab.healthcare_hospital import (
    hospital_encounter_quality, hospital_lab_quality,
    hospital_medication_quality, count_preindex_events,
)
# Pass the institution's reviewed column names, encounter grain,
# timezone/date definitions and code/unit mappings explicitly.
# count_preindex_events(..., allow_patient_level=True) produces RESTRICTED
# in-memory patient-level data and must NEVER be exported via notebooks/logs.
~~~

The clinical site is responsible for separate decisions about planned vs
unplanned readmissions, data discontinuity, transfer logic, medication exposure
episodes, coding version, leakage, de-identification and outcome adjudication.

## One-command synthetic integration — all three source families

~~~bash
# No downloads, credentials, protected records, dataset files, or network I/O:
python scripts/synthetic_three_source_smoke.py --synthetic-only
~~~

The command returns a single JSON result with seven boolean software checks
and explicit `clinical_or_regulatory_validation: NOT_ASSESSED`.
From an approved Slurm allocation run it with the
`slurm/portable_cpu.sbatch` template, and retain the exact source SHA.
A synthetic result is not validation against real All of Us, MIMIC-IV
or site-specific hospital EHR data.

## Tests, completeness and release boundaries

~~~bash
python -m pytest -q tests/test_healthcare_sources.py \
  tests/test_healthcare_omop.py tests/test_healthcare_aou_domains.py \
  tests/test_healthcare_aou_query.py tests/test_healthcare_mimic.py \
  tests/test_healthcare_hospital.py tests/test_healthcare_cohorts.py \\
  tests/test_adaptive_source.py
~~~

When using any source, prespecify source-specific code sets and observation
windows. The new `healthcare_cohorts` module can build an **in-memory**
first-*observed* index event from a frozen code set
(`allow_patient_level=True` is required), count a sequential eligibility
waterfall, and check whether event followup reaches a prespecified horizon.
These helpers **do not prove first-ever incident disease, complete external
outcome ascertainment or exchangeability**. In All of Us Workbench, retain
all patient-level outputs in that workspace. In MIMIC, relative times are
consistent within a shifted patient, not across patients.

This is a **test plan**, not an assertion of completed execution.
For the exact-SHA full QA use `slurm/portable_acceptance.sbatch` on
authorized CPU compute. Further external validation must use authorized
unseen datasets and independent gold mappings; routine code tests cannot
certify a patient-data model or published causal estimate.

**Provenance limitations:** All 3 source families are `CANDIDATE` /
`NOT_ASSESSED` in `configs/method_readiness.yaml` until formally reviewed.
Never move All of Us Controlled/Registered records into generic UGA HPC,
personal cloud accounts or GitHub. Small counts and any patient-level
intermediate require the source's disclosure-review process.


## Source-specific record linkage and optional foreign keys

- **All of Us:** The Programme does not permit participant-level linkage to
  external data without explicit documented permission. The default
  `source_aware_relationship_integrity` function **always blocks different
  source families, CDR releases, classifications, environments and stewardship
  attestations**. It cannot issue linkage exceptions or independently
  verify Workbench credentials. Use same-CDR joins inside the approved
  Workbench only. Never combine an All of Us person ID with MIMIC or a
  separate hospital MRN by their superficial number/string similarity.
- **MIMIC-IV:** `hosp.labevents.hadm_id` can be missing for a legitimately
  recorded result. Use
  `relationship_integrity(..., allow_null_child_keys=True)` **only after
  reviewing the optional-FK semantics**; it separately reports
  `null_child_links`, does not guess admissions or silently drop rows,
  and returns `STRUCTURAL_REVIEW_REQUIRED` when null links occur.
  Other FKs still use fail-closed non-null defaults.
- **Generic hospital EHR:** join on a steward-reviewed, stable per-site
  patient/encounter mapping; use the same approved source/release context for
  both tables. Cross-site MRN linkage is not inferred or approved.

## Registered and Controlled CDR reference-resource safety

`plan_aou_omop_domain_query` is non-executing and accepts only official
v9 tier/project pairs from the
[All of Us Data Dictionaries](https://support.researchallofus.org/hc/en-us/articles/360033200232-Data-Dictionaries):
`registered_v9` -> `wb-affable-acorn-7941.R2025Q4R6`, and
`controlled_v9` -> `wb-silky-artichoke-2408.C2025Q4R6`.
Wrong-tier or unrecognized project IDs are refused. Confirm the currently
available release inside the actual Workbench before applying any plan.
Only the user's Workbench IAM entitlements can authenticate execution.

This source-aware linking preflight is a **structural contract**, not
proof of cross-dataset transportability, phenotype equivalence or clinical
causal validity.

## MIMIC-IV v3.1 additional documented table coverage

The v3.1 candidate schema contracts now recognize selected additional
`hosp.poe`, `hosp.emar_detail`, `hosp.services`, `icu.procedureevents`,
`icu.datetimeevents` and `icu.ingredientevents` structures.

- `poe_id` identifies a provider order. An `emar_detail` record can have
  multiple constituent dose rows for one eMAR event; never deduplicate merely
  by `emar_id` or assume a single dose per medication.
- A recorded ICU procedure indicates a documented event; a missing procedure
  record cannot establish clinical absence. ICU start/end times can still
  require a separate temporal-order review.
- `mimic_order_to_emar_linkage_quality` counts incompatible/missing
  `pharmacy_id` references and patient mismatches without joining raw rows
  into a broad patient-level table. It does not estimate actual exposure,
  dispense quantity, dose, adherence, or medication effectiveness.
- The `hosp` and `icu` modules are distinct source systems, even when
  records belong to the same deidentified `subject_id` / `hadm_id` chain.
  Cross-patient calendar comparisons remain invalid due to shifted dates.

References: [MIMIC IV hospital module](https://mimic.mit.edu/docs/iv/modules/hosp/),
[ICU module](https://mimic.mit.edu/docs/iv/modules/icu/),
[eMAR details](https://mimic.mit.edu/docs/iv/modules/hosp/emar_detail.html),
[POE](https://mimic.mit.edu/docs/iv/modules/hosp/poe.html),
[procedureevents](https://mimic.mit.edu/docs/iv/modules/icu/procedureevents.html).

**Readiness remains candidate structural validation only.** Real MIMIC data,
independent source-adjudication, clinical reference mappings and a
verified exact-source-SHA full QA report are still required.


See [Clinical ML leakage and follow-up](clinical-leakage-and-followup.md)
for point-in-time lab availability, patient/time group purging, train-only
preprocessing, claims enrollment completeness and outcome-censoring guards.
These checks do not establish clinical validity or permission to use restricted
All of Us, MIMIC-IV or hospital records.

# All of Us disclosure policy and guarded export boundaries

**Software disposition: CANDIDATE — not independently executed or cleared for real
All of Us participant data.** This document is shared between the private
Core and public handbook. It is not a programme permission or legal decision.

Official programme requirements:
- [Research Hub: Data and Statistics Dissemination Policy](https://www.researchallofus.org/faq/data-and-statistics-dissemination-policy/)
- [Research Hub: Data Access Tiers](https://www.researchallofus.org/data-tools/data-access/)
- [Workbench guidance: policy compliance and suppression](https://support.researchallofus.org/hc/en-us/articles/360043016291-How-to-comply-with-the-All-of-Us-Data-and-Statistics-Dissemination-Policy)

**Never publish/distribute participant-level records.** A participant count
of **1 through 20** must not be disclosed directly, and a small count must
not be deducible from other reported numbers, percentages, totals, visualizations,
text or complementary cells. A count of zero may be permitted, but its presence
does not establish report-level safety. Human review applies to *all*
tables, figures, models, summaries and narrative before dissemination.
Small-cell exceptions require express All of Us programme permission.

## What is implemented

- `thomaslab.adaptive.safe_bundle.export_governed_bundle` now requires
  `source_system` for every non-synthetic dataset and applies the declared
  source identity to its central `validate_environment` policy.
  For All of Us, **the generic bundle exporter always refuses to write**,
  even for an aggregate or a caller claiming a different source when the
  adapter provenance identifies All of Us. This prevents accidental copying
  to generic institutional HPC or external storage. It does not create a
  substitute programme-approved release channel.
- `thomaslab.adaptive.aou_disclosure.aou_aggregate_disclosure_preflight`
  examines **an already authorized in-memory summary**. It detects
  obviously prohibited values 1–20, noninteger/invalid participant counts
  and possible small differences in row totals. It never writes files,
  returns source values, or claims release approval. Its best possible
  outcome is `DISCLOSURE_REVIEW_REQUIRED`, not `PASS_TO_EXPORT`.
- `thomaslab.healthcare_quality.site_missingness_preflight(...,
  source_system="all_of_us")` blocks generic site aggregate disclosure:
  the usual threshold 11 is **not** an All of Us threshold.

## A fully invented demonstration

~~~python
import pandas as pd
from thomaslab.adaptive.aou_disclosure import (
    aou_aggregate_disclosure_preflight,
)

# Fabricated non-participant counts; no Workbench connection or data transfer.
study = pd.DataFrame({"total": [50], "shown_group": [37]})
review = aou_aggregate_disclosure_preflight(
    study,
    participant_count_columns=("shown_group",),
    row_total_column="total",
)
assert review["status"] == "BLOCK"  # 50 - 37 = 13
assert review["all_of_us_dissemination_approved"] is False
~~~

**Important:** even if all explicitly inspected values are 21 or greater,
other reported percentages, omitted categories, multiple figures or associated
data could reveal a prohibited small count. This check cannot certify
complementary suppression, true denominator uniqueness, data licensing,
participant identifiability, or the full publication policy.

## Practical release workflow

1. Analyse Registered/Controlled participant-level records **only inside**
   the Researcher Workbench under actual approved access.
2. Produce a proposed aggregate and inspect it in-memory; never output
   raw participant values, notes, identifiers or sensitive row-level records
   to common filesystem or public notebooks.
3. Apply the programme's Workbench statistical disclosure policy over
   all outputs jointly; use appropriately documented coarsening/suppression.
4. Obtain a named responsible reviewer, follow current Workbench programme
   procedures, and where needed seek a documented exception directly from
   the programme. No local Python flag certifies this approval.
5. Only use a **separate, programme-authorized release route**; the Core
   generic bundle writer intentionally does not implement it.

## Regression gates

~~~bash
python -m pytest -q tests/test_aou_disclosure.py \
  tests/test_adaptive_safe_bundle.py \
  tests/test_adaptive_governance.py \
  tests/test_healthcare_quality.py
~~~

Actual SHA acceptance still requires full test/quality/supply-chain evidence;
synthetic tests are insufficient for unrestricted research deployment.

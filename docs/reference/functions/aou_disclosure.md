# `thomaslab.adaptive.aou_disclosure` — disclosure preflight API

**Status:** software candidate. This source-aware preflight cannot approve any
All of Us participant-level export or aggregate publication.

## `aou_aggregate_disclosure_preflight`

**Signature**

~~~python
def aou_aggregate_disclosure_preflight(
    table: pd.DataFrame,
    *,
    participant_count_columns: Sequence[str],
    row_total_column: str | None = None,
    max_rows: int = 100_000,
) -> dict[str, Any]:
~~~

**Purpose:** check proposed, already authorized in-memory participant-count
summaries for directly prohibited values 1–20, invalid counts, and possible
small residuals calculated from a declared row total. Zero and counts of 21+
can pass this **structural preflight**, but never become approved outputs.

**Inputs:** `table` is an approved in-Workbench aggregate, not row-level data.
`participant_count_columns` identifies exact distinct-participant count
columns, never encounter or medication counts. If `row_total_column` is
supplied, it must express a total for the corresponding, independently reviewed
disjoint categories; this function does not certify disjointness.

**Outputs:** metadata flags only, including `status` (`BLOCK` or
`DISCLOSURE_REVIEW_REQUIRED`), `prohibited_small_count_detected`,
`potential_derived_small_count_detected` and
`all_of_us_dissemination_approved=False`. No source rows or cell counts
are returned.

**Failure conditions:** invalid DataFrame, ambiguous/duplicate count columns,
excessive row count, or unparseable inputs raise errors. The function does not
perform an external transfer.

For a complete fabricated example and official policy, see
[All of Us disclosure controls](../../guides/aou-disclosure.md).

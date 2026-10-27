# S23 — Synthetic quarantine and source-to-target lineage reconciliation

**Partial P3-06 candidate, never a real hospital quarantine service.** Private module: `thomaslab.adaptive.quarantine_reconcile.reconcile_synthetic_lineage`.

The function compares bounded **invented** source-key and target-source-key lists against a structured quarantine ledger. It reports source/target counts, duplicate source IDs, unexpected target records, mapped rows for quarantined sources, unmapped unquarantined records, and excess target fan-out for an expected one-to-one mapping.

Quarantine records are strictly limited to `source_key` plus one controlled reason code: `SOURCE_CORRUPT`, `MAPPING_UNCERTAIN`, `INVALID_CONCEPT`, `MISSING_KEYS`, `TIME_CONFLICT`, `REVIEW_REQUIRED` or `SOURCE_DUPLICATE`. Free-text notes, patient names, dates and arbitrary error descriptions are explicitly refused.

`ONE_TO_MANY` is permitted only with an opaque review reference; the helper **does not prove** that the asserted review was signed by a clinician or that the fan-out was clinically valid. Missing or duplicate source keys are flagged. No source IDs, target IDs, quarantined row values or linkage crosswalks are included in returned reports.

### Invented example

~~~python
from thomaslab.adaptive.quarantine_reconcile import reconcile_synthetic_lineage

result = reconcile_synthetic_lineage(
    source_keys=["sourceA", "sourceB", "sourceC"],
    target_source_keys=["sourceA", "sourceB"],
    quarantine=[{"source_key": "sourceC", "reason": "MAPPING_UNCERTAIN"}],
    site_scope="invented_site",
    source_schema_sha256="a" * 64,
)
assert result["unmapped_unquarantined_sources"] == 0
assert result["quarantined_rows"] == 1
assert result["raw_source_or_target_keys_returned"] is False
assert result["dataset_release_authorized"] is False
~~~

Even aggregate counts can be identifying for very small or rare groups. Returned `small_cell_disclosure_review_required=True` and `authorized_for_export=False` are mandatory. The `report_sha256` is a checksum of aggregate *diagnostics*, not a cryptographically authenticated row-level source-to-target provenance proof.

### Evidence and limitations

**23/23 S23 focused synthetic tests passed** on Python 3.13.5, including missing/duplicate/foreign target rows, unknown quarantine items, invalid reasons, invalid identity structure and fan-out review. Combined S21+S22 51 tests yield **74/74** passing locally. Test and source Git blobs match exact executed files; Python 3.9–3.13 AST grammar and compilation passed.

**P3-06 remains OPEN**: there is no encrypted durable patient-data quarantine, institutional authorizer, source/target clinical identity key reconciliation, approved exception-resolution workflow, signed audit trail or verified independent release. Real EHR rows, deidentified records and source keys must not be passed into this synthetic helper.

Related: [S21 OMOP core builder](omop_core_builder.md), [S22 sidecars](extension_tables.md), [S12 dataset manifests](release_manifest.md) and [platform roadmap](../../guides/ehr-platform-build-plan.md).

~~~bash
python -m pytest -q tests/test_adaptive_quarantine_reconcile.py
~~~

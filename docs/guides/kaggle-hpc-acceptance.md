# Kaggle and HPC: independent dataset acceptance

!!! warning "Do not equate a downloaded Kaggle dataset with clinical or publication validation"
    Kaggle is a hosting/distribution platform. Copies can have uncertain origin, restrictive licenses, inaccurate labels, obsolete clinical meanings or real identifiers. Only explicitly licensed, permitted sources may be staged; only independently reviewed source schema and gold mappings may be benchmarked. No Kaggle data is presumed appropriate for patient-level decisions.

## What this implementation tests

The private core repository supplies five separate stages:

1. **Acquire:** independently query Kaggle's metadata and license; download only on explicit request; store original archive and SHA-256 receipt. No implicit ZIP extraction.
2. **Inspect:** check every original file digest, archive traversal, compressed expansion risk and supported file type. A cached archive does not imply trustworthy research data.
3. **Review:** select one file for quarantine, inspect its schema without printing record values, and have a named domain researcher approve a gold mapping tied to its exact SHA-256.
4. **Execute:** run the approved mapper benchmark under a bounded CPU Slurm allocation, with immutable redacted aggregate output. A failed, skipped or blocked case returns a nonzero exit code.
5. **Release:** independently check source syntax (Python 3.9), all-module imports, targeted and full pytest, 84% coverage, static lint/types, package/wheel, 59 notebook interfaces and synthetic design gates.

An import PASS only shows a module loads. The AST callable count is an inventory; it does **not** mean every function was executed or numerically validated. The 19 legacy notebooks are not all human-interaction tested. Publication-level method review is independent of software QA.

## Prepare the dedicated HPC workspace

Use an institution-approved storage path and job allocation. The example keeps both data and generated reports **outside** the Git repository.

~~~bash
export THOMASLAB_HPC_ROOT="/path/to/approved-research/thomaslab_hpc"
mkdir -p "$THOMASLAB_HPC_ROOT/core"
cd "$THOMASLAB_HPC_ROOT/core"
git clone git@github.com:appsplorer/thomaslab-core.git
cd thomaslab-core
git fetch origin
git switch audit/kaggle-hpc-final-20261021
git pull --ff-only
bash scripts/setup_thomaslab_hpc.sh

module avail python
python3.9 --version
command -v kaggle
kaggle --version
~~~

Use the existing Kaggle login/CLI environment; never copy `kaggle.json`, bearer tokens or institutional patient data into GitHub, published docs, notebooks or SLURM logs. A currently installed Kaggle CLI may use a newer interpreter: the staging code invokes that CLI as a separate executable, while the research virtual environment can remain Python 3.9.

## Inspect and stage the 16 candidate handles

The catalog `benchmarks/kaggle/candidates.json` is **discovery-only**: no source or license is preapproved. Current candidate handles cover diabetes, breast cancer, liver disease, stroke, heart failure (two distinct distributions), health insurance, appointment attendance, cardiovascular risk, temporal credit payments, relational movie ratings, COVID surveillance, drug-review NLP, diabetes readmissions, CDC BRFSS and CMS hospital ratings.

~~~bash
KAGGLE_ROOT="$THOMASLAB_HPC_ROOT/datasets/kaggle"
python3.9 scripts/kaggle_hpc.py catalog --root "$KAGGLE_ROOT" --limit 16

# Review the live Kaggle license/metadata before retrieving anything.
kaggle datasets files andrewmvd/heart-failure-clinical-data
kaggle datasets metadata andrewmvd/heart-failure-clinical-data \
  -p "$THOMASLAB_HPC_ROOT/datasets/kaggle/metadata"

# Stage one named candidate; no data is downloaded without --execute.
python3.9 scripts/kaggle_hpc.py stage --root "$KAGGLE_ROOT" \
  --id heart_failure_clinical --max-mib 512 --execute

# To attempt the full initial 16-source catalog, with explicit budget:
python3.9 scripts/kaggle_hpc.py stage --root "$KAGGLE_ROOT" \
  --limit 16 --max-mib 512 --execute
~~~

**Resumable Kaggle staging:** Once an approved source has been downloaded, repeating `stage` verifies the stored receipt, source identity, file inventory, archive safety and SHA-256 before reusing it. `ALREADY_STAGED_VERIFIED` means the exact cached source bytes are intact; **no new Kaggle download is performed**. Mutated, missing or unexpected extra files produce `BLOCK_EXISTING_INTEGRITY_FAILURE` and are not automatically overwritten. This is an archive integrity check, not scientific review or a fresh verification of the Kaggle provider's current license terms.

For an incremental pilot, request a few candidates at a time:

~~~bash
python3.9 scripts/kaggle_hpc.py inventory --root "$KAGGLE_ROOT" \
  --id heart_failure_clinical

python3.9 scripts/kaggle_hpc.py stage --root "$KAGGLE_ROOT" \
  --id heart_failure_clinical --id medical_insurance \
  --id breast_cancer_wisconsin --max-mib 512 --execute
~~~

The batch continues through individual blocked candidates, but still returns a nonzero process status if any requested source is unavailable, unlicensed or unsafe. Full scientific or independent-source acceptance requires researcher-approved gold mappings and separate validation.

**CC BY 4.0 name normalization:** Kaggle metadata can return `Attribution 4.0 International (CC BY 4.0)` for the same license the project calls `CC-BY-4.0`. The private downloader now recognizes that **exact verified display name only**, preserves the original and canonical names in the checksum receipt, and continues to block unapproved, noncommercial, ShareAlike or NoDerivatives licenses. A CC BY license is already offered to the public; no purchase or author acceptance step is normally needed. Researchers must preserve required attribution. The [Heart Failure Prediction Kaggle dataset](https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data) requests credit to Davide Chicco and Giuseppe Jurman (2020). Read the [CC BY 4.0 terms](https://creativecommons.org/licenses/by/4.0/). Copyright permission is separate from institutional, ethics and privacy compliance.

**Expected blocking cases are not bugs.** Kaggle licenses such as unknown, "other", copyright-authors and CC BY-NC-SA are not automatically allowed by the acquisition policy. A candidate whose preferred file is not found must be corrected after running `kaggle datasets files <owner/slug>`. Large BRFSS files may exceed 512 MiB even individually. The size limit is verified *after* the Kaggle CLI returns; use project quota and site transfer limits before downloading a potentially large file. Never launch bulk downloads on Slurm compute nodes if the institution requires a designated transfer node.

A source distributed through Kaggle does not automatically count as an independent dataset. Check original provenance and overlap/duplicate cohort membership, and preserve required attribution.

## Kaggle 1.7.x metadata object validation

An actual HPC run on Kaggle API 1.7.4.5 returned a JSON string rather than the expected dataset metadata object. The private ingestion implementation now handles a nested JSON-encoded object when present, but **blocks all unstructured strings**, missing source identity, invalid license metadata, and malformed JSON. This prevents unsupported responses from being interpreted as license permission. Each candidate produces an independent status instead of stopping the entire 16-source staging attempt.

For a `BLOCK_METADATA_SHAPE` response, run the following on an institution-approved Kaggle CLI login/transfer node. This prints **type and key names only**, never the raw payload, data rows or access token:

~~~bash
DIAG_DIR="$THOMASLAB_HPC_ROOT/datasets/kaggle/metadata/heart-failure-debug"
mkdir -p "$DIAG_DIR"
chmod 700 "$DIAG_DIR"
kaggle datasets metadata andrewmvd/heart-failure-clinical-data -p "$DIAG_DIR"
python3.9 - "$DIAG_DIR/dataset-metadata.json" <<'PY'
import json, sys
from pathlib import Path
data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
print("outer_type:", type(data).__name__)
print("outer_keys:", sorted(data) if isinstance(data, dict) else "not-object")
if isinstance(data, str):
    try:
        nested = json.loads(data)
        print("nested_type:", type(nested).__name__)
        print("nested_keys:", sorted(nested) if isinstance(nested, dict) else "not-object")
    except (ValueError, TypeError):
        print("nested_type: not-valid-json-object")
PY
~~~

For Kaggle API 1.7.4.5, the server may provide an inner object with `ownerUser` and `datasetSlug` but no `id`. The private ingestion code now verifies the **exact owner and dataset slug together** against the requested Kaggle handle; if an `id` is also present, both forms must agree. Missing or mismatched identity, unapproved license, and malformed metadata remain **BLOCK**. This is a source-integrity check, not scientific dataset validation.

## Observed HPC pilot: source identity and open database licenses

On 21 October 2026, Python 3.9 HPC execution yielded **55 passing targeted tests**, a verified cached download and quarantined CSV extraction for the CC BY 4.0 heart-failure clinical dataset. This establishes file integrity and tool behavior, not clinical validity.

Three other Kaggle candidate handles were blocked:

- Medical insurance (`mirichoi0218/insurance`): Kaggle metadata reported `DbCL-1.0`.
- Heart failure prediction (`fedesoriano/heart-failure-prediction`): metadata reported `ODbL-1.0`.
- Wisconsin breast cancer (`uciml/breast-cancer-wisconsin-data`): identity fields did not match the catalogued Kaggle reference. The actual observed owner and slug remain unverified until a separate metadata inspection.

These are expected, **fail-closed** statuses, not evidence that the datasets or their licenses are illegitimate. The private core provides a metadata-only diagnostic that neither downloads records nor displays free-text metadata:

~~~bash
python3.9 scripts/kaggle_hpc.py metadata --root "$KAGGLE_ROOT" \
  --id breast_cancer_wisconsin

python3.9 scripts/kaggle_hpc.py metadata --root "$KAGGLE_ROOT" \
  --id medical_insurance --id heart_failure_fusion
~~~

The output is limited to public Kaggle identity fields, observed license labels, and exact-match decisions. A mismatched account/slug cannot be silently rewritten. Verify original provenance before revising the catalog.

The [Open Data Commons DbCL 1.0](https://opendatacommons.org/licenses/dbcl/1-0/) pertains to **database contents** and does not alone establish every applicable database right. The [Open Data Commons ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/) permits database reuse with **attribution** and public derivative-database share-alike obligations. Both values remain outside the automatic Kaggle acquisition allowlist until an independent, named source-specific permissions and scientific-provenance review. The downloader reports official terms URLs and review scope without bypassing this restriction.

## Actual 16-candidate metadata triage (HPC observation, October 2026)

The live Kaggle API 1.7.4.5 metadata survey of 16 candidate datasets produced four distinct outcomes. This reflects **source acquisition readiness only**, not independent data validation.

| Outcome | Count | Dataset IDs |
|---|---:|---|
| Source identity and base-license allowed | 3 | `heart_failure_clinical`, `movie_ratings_small`, `diabetes_readmissions` |
| Identity matched, license review required | 7 | `stroke_prediction`, `heart_failure_fusion`, `medical_insurance`, `medical_appointments`, `cardiovascular_70k`, `covid_19_epidemiology`, `drug_review_text` |
| Owner identity unresolved | 5 | `breast_cancer_wisconsin`, `indian_liver`, `credit_default_temporal`, `brfss_surveys`, `cms_hospital_quality` |
| Kaggle metadata CLI failure | 1 | `pima_diabetes` |

A provider response that gives the expected `datasetSlug` without a supported owner reference is not proof that the owner matches. The private `metadata` command now reports only the **types of whitelisted identity fields**, plus a sanitized CLI exit code when available, to distinguish null/object/string owners and source-endpoint failures. It never outputs raw metadata descriptions, private nested object values, Kaggle credentials or dataset rows.

~~~bash
# No dataset download; inspect unresolved source owner field shapes
python3.9 scripts/kaggle_hpc.py metadata --root "$KAGGLE_ROOT" \
  --id breast_cancer_wisconsin --id indian_liver \
  --id credit_default_temporal --id brfss_surveys \
  --id cms_hospital_quality

# No dataset download; inspect Pima metadata command outcome
python3.9 scripts/kaggle_hpc.py metadata --root "$KAGGLE_ROOT" \
  --id pima_diabetes

# Pilot additional base-allowlisted sources only after original
# source and selected-file provenance verification
kaggle datasets files rounakbanik/the-movies-dataset
kaggle datasets files brandao/diabetes
python3.9 scripts/kaggle_hpc.py stage --root "$KAGGLE_ROOT" \
  --id movie_ratings_small --id diabetes_readmissions --execute
~~~

These last two catalog entries are **candidate classifications only**. In particular, the scientific suitability and original cohort of `brandao/diabetes` must be checked before calling it a diabetes-readmissions dataset. Do not override unknown, noncommercial or legally complex licenses merely to complete a matrix of 16 rows.

## Kaggle organization display names and CSV-file confirmation

The latest Herts HPC metadata-only diagnostics show five expected Kaggle references whose provider `ownerUser` is a **string** but not a username-style slug. A publicly named Kaggle organization can be displayed as `UCI Machine Learning` despite having canonical URL slug `uciml`. This is a possible explanation, **not a verified metadata owner mapping**. The private CLI now displays a bounded, safely filtered `owner_display_label` for research diagnosis, always with `display_label_confirms_owner_slug: false`. No source acquisition authorization is inferred from a display name alone.

The HPC Kaggle file-list commands confirmed:
- `rounakbanik/the-movies-dataset` contains `ratings_small.csv` (2,438,266 bytes). Its much larger `ratings.csv` is not the selected benchmark file.
- `brandao/diabetes` contains `diabetic_data.csv` (19,159,383 bytes) and `description.pdf`. The CSV filename matches the candidate catalog, **but the upstream hospital cohort, clinical semantics and independent source provenance are not yet reviewed**.

After independently verifying access rights and institutional transfer-node policy, these two allowlisted single-file candidates may be staged in the private restricted HPC data area:

~~~bash
python3.9 scripts/kaggle_hpc.py stage --root "$KAGGLE_ROOT" \
  --id movie_ratings_small --id diabetes_readmissions \
  --max-mib 64 --execute

python3.9 scripts/kaggle_hpc.py inventory --root "$KAGGLE_ROOT" \
  --id movie_ratings_small --id diabetes_readmissions
~~~

For owner-label and Pima CLI-error diagnosis **without downloading source data**:

~~~bash
python3.9 scripts/kaggle_hpc.py metadata --root "$KAGGLE_ROOT" \
  --id breast_cancer_wisconsin --id indian_liver \
  --id credit_default_temporal --id brfss_surveys \
  --id cms_hospital_quality --id pima_diabetes
~~~

The data remain `NOT_ASSESSED` scientifically until named expert mappings and provenance reviews, including any privacy and rights checks, are completed.

## Check source integrity and quarantine one member

~~~bash
python3.9 scripts/kaggle_hpc.py inventory --root "$KAGGLE_ROOT" \
  --id heart_failure_clinical

python3.9 scripts/kaggle_hpc.py extract --root "$KAGGLE_ROOT" \
  --id heart_failure_clinical \
  --member heart_failure_clinical_records_dataset.csv --execute
~~~

Extraction is deliberately separate from acquisition and preserves the source ZIP and SHA-256. The extracted file remains **QUARANTINED_UNREVIEWED**.

For a Kaggle dataset with a different actual filename, inspect Kaggle's current file listing and update the reviewed candidate selection before retrying. No direct identifiers or row samples should appear in downloadable benchmark reports.

## Researcher-controlled gold mappings and approval

To count an independently reviewed case, the lab supplies **two files per candidate** in:

`$THOMASLAB_HPC_ROOT/benchmarks/gold_mappings/`

- `<id>.mapping.json`: JSON object of actual source-column names to canonical roles, independently verified against original data dictionary and units.
- `<id>.approval.json`: named reviewer, source SHA-256 (from `review-receipt.json`), **gold mapping SHA-256** (from `sha256sum <id>.mapping.json`), source license, reviewed domain, `status: "APPROVED"`, and `independent_source_review: "COMPLETE"`.

A safe initial approval template is **PENDING**, not approved:

~~~json
{
  "status": "PENDING",
  "reviewer": "",
  "dataset_sha256": "",
  "gold_mapping_sha256": "",
  "license": "UNVERIFIED",
  "independent_source_review": "NOT_ASSESSED",
  "domain": ""
}
~~~

Never promote the template automatically. Use a real expert review and the current dataset SHA. Do not infer canonical clinical meaning from lexical similarity alone.

## Execute the full software gate

Use an authorized CPU partition (the example Slurm account and CPU partition require verification against current HPC policies).

~~~bash
export THOMASLAB_EXPECTED_SHA="$(git rev-parse HEAD)"
export THOMASLAB_INSTALL=1
export THOMASLAB_FULL=0
sbatch --account=eng --partition=core32 --cpus-per-task=8 \
  --mem=32G --time=06:00:00 slurm/python39_validation.sbatch
~~~

The hardened script now includes an independent import audit for every source module and extra Kaggle provenance tests. Its existing 40 guided callbacks, 19 legacy registrations, 10 synthetic families, 100,000-row streaming benchmark, full pytest and 84% coverage checks remain part of the quality gate. Full release mode (`THOMASLAB_FULL=1`) also requires the compatible PyTorch/notebook/docs toolchain.

## Run the Kaggle-reviewed matrix in Slurm

After review/approval, run:

~~~bash
export THOMASLAB_EXPECTED_SHA="$(git rev-parse HEAD)"
sbatch --account=eng --partition=core32 --cpus-per-task=8 \
  --mem=32G --time=06:00:00 slurm/kaggle_reviewed_matrix.sbatch
~~~

A complete 16-candidate run fails on any missing, unapproved, unlicensed or mutated source. For **exploratory diagnostics only**, set `THOMASLAB_ALLOW_PARTIAL_BENCHMARK=1`: all excluded sources stay explicitly `NOT_RUN` or `BLOCK`, and partial results cannot establish 16-dataset acceptance.

The manifest uses **exact source SHA-256**, approved source and gold directories, at least 0.80 mapping-fidelity threshold, and fail-closed CLI exit codes. The eager mapping benchmark defaults to **64 MiB maximum source size** (`--max-source-mib`, upper bound 256 MiB). Larger BRFSS/EHR sources must use chunked full validation and approved large-scale methods rather than unbounded pandas materialization.

A benchmark PASS measures documented structural agreement, **not** correct pharmacotherapy, PGx guideline interpretation, clinical causal identification, drug-safety effects or external validity.

## What the 16 candidate sources do not cover

Kaggle copies do not establish true FHIR resource coverage, EHR-plus-claims-plus-genotype joins, validated adverse-event phenotypes, prescription exposure semantics, de-identification, specialist causal inference assumptions, or PGx assay and guideline version accuracy. Add specific licensed benchmark data, reviewed gold labels and method-specific synthetic contracts for those components. Multiple Kaggle representations of the same underlying UCI data must not count as independent source evidence.

**Outstanding external release gates:** 15–20 genuinely independent and approved unseen dataset studies, five independent nontechnical researcher task trials, HPC storage/account policy review, privacy/legal/IRB or DUA authorization where needed, manuscript-level numerical baselines, and expert scientific interpretation. Mark unexecuted items `NOT_RUN`, not PASS.

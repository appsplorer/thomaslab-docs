# Kaggle and HPC: independent dataset acceptance


!!! info "Current Python 3.9 guide and evidence status"
    **Use [the current isolated Python 3.9 Slurm procedure](hpc-python39.md)** for new acceptance runs. Earlier sections below preserve historical investigation commands (including legacy Slurm entry points and pre-repair diagnostics) as archival evidence; do **not** copy obsolete `slurm/python39_validation.sbatch`, `THOMASLAB_INSTALL`, or shared-environment examples to initiate a new run. The private Core **`main` now declares Python 3.9+** following non-squash integration of the HPC development history; the integrated Herts runner specifically requires Python **3.9**. The historical job `2498939` passed full pytest, both quality gates and **106/106** module imports, but failed the strict callable gate (**940/955** bodies observed). **The subsequent full integrated job `2499042` completed technical PASS** on exact source commit `469c120a81bdf5957911550dea4075fbf577ab61`: **21 executed phases PASS, 0 FAIL, 106/106 module imports, 955/955 declared named functions observed, 0 unobserved**. This is code execution evidence, **not** exhaustive branch correctness, independent dataset gold mapping or clinical validity. The original commits are preserved in `main` history. Dataset approvals and expert scientific validation remain **NOT_ASSESSED**.


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

## Three Kaggle HPC sources downloaded and structurally quarantined

At the October 2026 Herts HPC checkpoint, the private Python 3.9 Kaggle suite passed. The real source-download and SHA-256 inventory outcomes are:

| Candidate | Original Kaggle file selected | Downloaded bytes | Integrity |
|---|---|---:|---|
| Heart-failure clinical | `heart_failure_clinical_records_dataset.csv` | 12,239 | Passed (quarantined earlier) |
| Movie ratings small | `ratings_small.csv` | 675,002 | Passed |
| Diabetes readmissions candidate | `diabetic_data.csv` | 3,314,619 | Passed |

The downloaded byte counts may represent **compressed ZIP payloads**, not the CSV file sizes. Real Kaggle license and owner verification exists for these three handles, but clinical validity, readmission outcomes, independent cohort identity and expert mappings remain **NOT_ASSESSED**.

To begin schema review, the private core now offers `profile` for checksum-pinned quarantined CSV/TSV data. The workflow rechecks staged and quarantined SHA-256 receipts, streams input with a bounded row size, reports row and column counts and row-width consistency, and never prints patient-level row values. Suspicious column headers are positionally redacted. It does **not** self-approve schema mappings.

~~~bash
# If not already quarantined, extract the original selected CSVs
python3.9 scripts/kaggle_hpc.py extract --root "$KAGGLE_ROOT" \
  --id movie_ratings_small --member ratings_small.csv --execute
python3.9 scripts/kaggle_hpc.py extract --root "$KAGGLE_ROOT" \
  --id diabetes_readmissions --member diabetic_data.csv --execute

# Profile only the reviewed-area files; this does not authorize scientific claims
python3.9 scripts/kaggle_hpc.py profile --root "$KAGGLE_ROOT" \
  --id heart_failure_clinical --max-mib 64 --execute
python3.9 scripts/kaggle_hpc.py profile --root "$KAGGLE_ROOT" \
  --id movie_ratings_small --max-mib 64 --execute
python3.9 scripts/kaggle_hpc.py profile --root "$KAGGLE_ROOT" \
  --id diabetes_readmissions --max-mib 64 --execute
~~~

The diagnostic continues to block five unverified Kaggle publisher identities and the inaccessible Pima handle; a public display name is not a verified account slug. License and scientific review remain independent gates. The `brandao/diabetes` dataset's hospital/readmission provenance has not yet been reviewed and must not be called an accepted external EHR cohort.

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


## Combined CPU acceptance and optional GPU smoke

Real Herts HPC testing on 21 October 2026 confirmed that the Kaggle source checksum gates were working and the heart-failure clinical dataset profiled at **299 rows × 13 columns**. The movie ratings and diabetes CSV profiles instead raised `UnicodeDecodeError`. Their transferred file sizes were much smaller than the listed CSV sizes, consistent with ZIP-compressed Kaggle downloads saved under `.csv` names (byte signatures are still awaiting HPC confirmation). The private source parser now identifies ZIP content regardless of suffix; a guarded repair path preserves original pre-fix quarantines and creates correctly decompressed, SHA-256-pinned replacements **without scientific autoapproval**.

The new private `scripts/hpc_integrated_acceptance.sh` and `slurm/thomaslab_integrated_cpu.sbatch` run a single **technical CPU validation job** consisting of Python 3.9/shell checks, target/full pytest, dependency preflight, module imports, synthetic/scale benchmarks, the quick and optional full quality gates, and all three source integrity and schema profiles. It writes separate per-phase logs and a `summary.txt` under the HPC `benchmarks/integrated_acceptance` folder, outside Git. It performs **no Kaggle downloads**. Legacy ZIP-as-CSV quarantine repairs require an explicit `THOMASLAB_REPAIR_MISLABELED=1`; the original archived evidence is preserved under `reviewed_recovery`.

After pulling the audited feature branch, running targeted tests and checking local account/partition limits, one example authorized CPU submission is:

~~~bash
cd /path/to/approved-research/thomaslab_hpc/core/thomaslab-core
git switch audit/kaggle-hpc-final-20261021
git pull --ff-only
python3.9 -m pytest -q tests/test_kaggle_hpc.py tests/test_kaggle_review_manifest.py
bash -n scripts/hpc_integrated_acceptance.sh slurm/thomaslab_integrated_cpu.sbatch
sinfo -o "%P %a %l %D"

export THOMASLAB_HPC_ROOT="/path/to/approved-research/thomaslab_hpc"
export THOMASLAB_EXPECTED_SHA="$(git rev-parse HEAD)"
export THOMASLAB_PYTHON39=python3.9
export THOMASLAB_FULL=1
export THOMASLAB_REPAIR_MISLABELED=1
sbatch --account=eng --partition=core256 --cpus-per-task=16 \
  --mem=48G --time=08:00:00 --export=ALL \
  slurm/thomaslab_integrated_cpu.sbatch
~~~

The `eng` account and `core256` partition are examples requiring live site verification, not guarantees of user allocation. **Do not use login-node resources for the heavy job.** The full gate may legitimately fail when scientific dependencies, wheel-build requirements or the notebook runtime have not yet been installed. Dependencies must be installed through a separately authorized workflow, not fetched on compute nodes.

GPU work is separate and optional. The private `scripts/hpc_gpu_smoke.py` checks only a reproducible synthetic PyTorch CUDA matrix multiplication and gradient, not clinical models or all GPU software. If authorized on the normal `gpu` batch partition:

~~~bash
sbatch --account=eng --partition=gpu --gres=gpu:1 \
  --cpus-per-task=4 --mem=16G --time=01:00:00 \
  slurm/thomaslab_gpu_smoke.sbatch
~~~

The reported `gpu-interactive` partition is **interactive-only**, with **one GPU per user**, **one job per user**, and **12 hours maximum**, not five concurrently allocatable user GPUs. Use `srun --partition=gpu-interactive --gres=gpu:1 --pty bash` only if authorized; inside the allocated shell, run `python3.9 scripts/hpc_gpu_smoke.py --output /absolute/approved/new-file.json`. Never submit an `sbatch` job to the interactive-only partition.

Even if every available CPU and CUDA technical phase passes, *publication-level validity*, human-approved gold mappings, the other blocked Kaggle licenses and identities, and 15–20 independently sourced unseen datasets remain separately unverified. The report must not be described as complete clinical or all-function scientific acceptance.


## Observed first CPU and GPU acceptance jobs (21 October 2026)

A real authorized UH Slurm run produced **different outcomes** for GPU and CPU, which must not be combined into a single PASS.

| Gate | Slurm accounting | Verified outcome |
|---|---|---|
| Standard GPU smoke (`2493696`) | `COMPLETED 0:0` | **PASS**: one NVIDIA A100 80GB PCIe, PyTorch 2.8.0+cu128, CUDA matrix forward/gradient finite, maximum absolute CPU–GPU difference 1.71661376953125e-05 |
| Integrated CPU acceptance (`2493645`) | `FAILED 1:0` | **FAIL**: `shell_syntax` PASS; `python39_static` FAIL, exit 1 |
| Full CPU pytest, module import checks, synthetic performance, three reviewed CSV profiles | Not reached | **NOT_RUN**, not failures or passes |

The exact CPU source checkout was `1994be20b90393db9d6eecc9029501a55579d0f1`. The private CPU report recorded `cpu_technical_status=FAIL` and `scientific_validation=NOT_ASSESSED`. The user-supplied console excerpt did not include the static check's underlying file/line issues; its private `python39-static.json` and log are needed before determining the cause.

The integrated runner was updated so a failed static screen remains a **FAIL** but does not suppress all *independent* follow-up gates if Python 3.9 compilation and targeted tests still work. A failed compile or essential targeted regression continues to stop the run before dataset access. The GPU smoke already passed and need not be repeated without a changed CUDA environment. Neither result establishes clinical accuracy, full model coverage, or independent-source gold mapping approval.


## Identified Python 3.9 static compatibility finding

The 21 October 2026 UH HPC report inspected **126 Python source files** and isolated its first integrated CPU failure to one use of `zip(..., strict=True)` in the private causal matching module (line 438 at the earlier source commit). This keyword was introduced in Python 3.10; the HPC uses Python 3.9.

The private core feature branch now checks the lengths of the treated-order, selected-match and distance arrays **before using ordinary `zip`**, preserving the original strict pairing invariant. Normal NumPy matching and kernel-length mismatch regression tests have been added. The correction is **not yet confirmed on HPC**; the next acceptance step is the Python 3.9 static check plus targeted tests before repeating the integrated CPU Slurm validation. The separate A100 GPU synthetic smoke previously passed and is unaffected by this static compatibility finding.

~~~bash
python3.9 scripts/python39_compat.py
python3.9 -m pytest -q \
  tests/test_python39_compat.py tests/test_causal.py \
  tests/test_kaggle_hpc.py tests/test_kaggle_review_manifest.py
~~~

As before, technical compatibility does not establish scientific, clinical or independent-data acceptance.


## Integrated CPU job 2494199: benchmark subprocess import failure

The 21 October 2026 UH HPC CPU acceptance job at private-core commit `e389ecd55e96d2f99b5e552ca23ee98afd200283` ended after 12 seconds with `FAILED 1:0`. The validated phase record was `shell_syntax PASS`, `python39_static PASS`, `compile PASS`, and `targeted FAIL`. Two targeted `tests/test_adaptive_benchmark.py` subprocess tests failed because `scripts/run_lab_adaptation_benchmark.py` raised `ModuleNotFoundError: No module named 'thomaslab'` before any benchmark data analysis.

The project has a `src/thomaslab` source layout. Pytest's configuration makes that package importable within pytest, but this setting is not automatically inherited by a new Python process. This was an HPC execution setup defect, **not** a failed scientific outcome.

The private core branch now:
- Supplies the current checkout's `src` package path to the two standalone benchmark CLI subprocess tests.
- Exports that `src` path for nested Python processes in the integrated CPU runner.
- Adds a mandatory `package_origin` gate confirming the resolved `thomaslab` package belongs to the exact Git checkout under test, preventing accidental use of a different installed release.

Before submitting another Slurm allocation, verify the private branch on Python 3.9:

~~~bash
git switch audit/kaggle-hpc-final-20261021
git pull --ff-only
python3.9 -m pytest -q \
  tests/test_adaptive_benchmark.py \
  tests/test_kaggle_hpc.py \
  tests/test_kaggle_review_manifest.py
~~~

The corrected source is **not yet HPC-verified**. Missing mandatory scientific dependencies, full pytest, module imports, old ZIP quarantine repairs and three schema profiles remain independent gates. No protected dataset rows, private node paths, user credentials or approved gold mappings are included in the public documentation.


## Isolated Python 3.9 dependency recovery after passing subprocess tests

On UH HPC, all executed benchmark, Kaggle, Python 3.9 compatibility and causal tests passed at private source commit `5a44e89d7f2d259144edf065553d0c541a0c2593`. One lifelines-dependent survival test remained **SKIPPED**. An independent `pip check` in the user's **shared** `research_env` flagged five unrelated requirement conflicts: `botocore/urllib3`, `fastai/torch`, `safe-cvs-tai/pyarrow`, `tabpfn-common-utils/nvidia-ml-py` and `thinc/numpy`. These are environment consistency failures, not conclusive defects in the clinical/statistical algorithms.

**Do not attempt to resolve these by downgrading or upgrading the shared research environment.** The private core already has `constraints/python39.txt` for an appropriately bounded stack, including `numpy<2`, `pyarrow<19`, and `lifelines>=0.27,<0.30`.

The private project now includes `scripts/hpc_prepare_python39_env.sh` and `scripts/hpc_environment_gate.py`. On an institution-approved environment-preparation node with permitted package access and storage, the preparation script creates a new `thomaslab-core-cpu` Python 3.9 virtual environment under the approved research directory, installs source and bounded developer/documentation/notebook dependencies, optionally the PyTorch models needed for full mode, and runs `pip check`. The script refuses to install dependencies from inside a Slurm compute job.

~~~bash
# From the private thomaslab-core checkout after pulling latest feature branch.
export THOMASLAB_HPC_ROOT=/path/to/approved-research/thomaslab_hpc
export THOMASLAB_PREP_FULL=1
bash scripts/hpc_prepare_python39_env.sh

export THOMASLAB_VENV="$THOMASLAB_HPC_ROOT/environments/python39/thomaslab-core-cpu"
export THOMASLAB_PYTHON39="$THOMASLAB_VENV/bin/python"
"$THOMASLAB_PYTHON39" scripts/hpc_environment_gate.py \
  --expected-venv "$THOMASLAB_VENV" --full
"$THOMASLAB_PYTHON39" -m pytest -q \
  tests/test_hpc_environment_gate.py tests/test_adaptive_benchmark.py \
  tests/test_causal.py tests/test_kaggle_hpc.py \
  tests/test_kaggle_review_manifest.py tests/test_python39_compat.py
~~~

The integrated CPU runner now requires this exact isolated interpreter and an early passing environment gate. Required missing packages, inherited system site packages and inconsistent dependency resolutions must be treated as failures, not silently skipped. The venv preparation may need substantial storage for PyTorch; verify institutional node/storage/pip-index policy first and report any missing compatible wheels instead of relaxing project constraints. The previous A100 GPU arithmetic smoke is already PASS and need not be repeated just to isolate the CPU environment.

Scientific correctness, independent clinical data, source licensing, expert-reviewed mappings, and production authorization remain separate acceptance gates.


## Module imports versus individual function execution

The private integrated acceptance pipeline imports every discovered source Python module in a clean subprocess and inventories public functions/methods. Its quick quality gate runs the pytest suite with at least **84% aggregate line coverage**, requires observed execution of at least one body line in each audited **top-level public** function/method, and smoke-tests the 59 notebook workflows (40 guided callbacks and 19 legacy widget interfaces). **Import success is not function correctness.** Neither line coverage nor a single executed function-body line establishes all code paths, mathematical correctness, clinical safety or publication readiness.

The user-supplied latest isolated environment log shows Python 3.9.25, `lifelines 0.29.0`, zero dependency conflicts and passing targeted regression tests. It shows that Slurm job **2495601 was submitted**, not that full module/coverage tests finished. Its outcome must be read from the actual job report.

For the *next* pinned run, the private core branch adds `scripts/hpc_callable_evidence.py`, a source-wide function evidence ledger. The script inventories named Python functions and class methods, including nested-package and private declarations, and records `BODY_LINE_OBSERVED`, `BODY_NOT_OBSERVED`, `NO_COVERAGE_RECORD` or `NO_EXECUTABLE_BODY` from **fresh** pytest coverage. It writes a per-symbol JSON file outside the source repository alongside the integrated CPU reports. It excludes anonymous lambdas and dynamically generated functions and deliberately does not execute arbitrary user functions or assert scientific validity.

**This new ledger was committed after job 2495601 was submitted and therefore is not part of that existing job.** Do not pull a moving branch into an active job's checkout. Evaluate its final report first; if another run is necessary, pin the new source SHA and collect the ledger then. Even an all-observed report must not be represented as 100% branch or clinical validity.


## Actual integrated CPU result: 2495601 — 18 PASS, four FAIL

The isolated CPU acceptance run for source commit `f6ce6421eafb6f894db62c6a2b6e2e7556c681b4` finished on 21 October 2026, Slurm `FAILED 1:0`, after 7 minutes and 47 seconds. Phase evidence included **18 PASS**, **four FAIL**, and the independently unapproved gold-mapping matrix still `NOT_RUN`.

The passing phases include pinned Python 3.9 source integrity and isolated dependencies, package-origin verification, targeted pytest, all ten synthetic adaptation families, the 100,000-row synthetic scale check, all three Kaggle SHA-256 inventories, successful original-receipt-preserving repair of the movie and diabetes ZIP-as-CSV downloads, and successful structural profile of those two CSVs plus the heart-failure CSV. These data remain **UNREVIEWED** for scientific mapping, phenotype semantics and independent dataset status.

The four failures were full pytest (exit 2; detailed traceback not yet provided), recursive module imports (**101/106** imported), and quick/full quality gates. Both quality logs showed the exact same two Ruff problems: unused `os` import in the private environment gate and import ordering in the scientific input contracts test. Both were fixed in the private core feature branch.

The module import names that failed were `gformula`, `longitudinal_dr`, `causal_robustness`, `adaptive.notebook_groups.groups_32_39`, and `adaptive.notebook_groups.specialist_40_45`. Inspection of the core source showed immediately evaluated `StrategyRule = int | Mapping[...] | Callable[...]` aliases in the first two files; **ordinary type-union expressions are not supported as runtime values on Python 3.9 even with postponed annotations**. Those aliases are now `typing.Union`-based and a regression test imports all five named modules. The private Python 3.9 compatibility screen was extended to detect runtime type-alias unions. The exact `full_pytest.log` collection errors were not included in the shared log, so root-cause attribution is still being verified.

Before any repeat Slurm job, test the new branch inside the isolated venv with the Python 3.9 static screen, `ruff check`, selected five-module import tests, and full test *collection only*. The new per-function test-coverage ledger was also added **after** job 2495601; the existing job does not report that inventory. Neither successful module import nor one observed function-body line demonstrates branch-complete, numerical or clinical correctness. The core release remains blocked pending full technical and scientific gates.


## Final lightweight Python 3.9 log: four confirmed test/lint defects fixed on private branch

A follow-up real UH HPC local run at private commit `9d904cb0f5deb1756517db10d9b48cb6541d1e58` verified `python39_compat.py` **PASS** (128 inspected Python files, no findings) and **successful full pytest collection**. It reported four lightweight regressions:

| Failure | Concrete correction |
|---|---|
| Ruff UP035 in `scripts/hpc_callable_evidence.py` | Import `Iterator` from `collections.abc` |
| `test_python39_rejects_runtime_type_union_alias_even_with_future_annotations` | Three-part fixture now uses real source newlines, not literal backslash-n tokens |
| `test_python39_accepts_legacy_typing_union_runtime_alias` | Same fixture correction |
| `test_python39_does_not_misclassify_normal_bitwise_or_values` | Same fixture correction |

These fixes are committed in private Core PR #32 but have **not yet been rerun at the latest commit on HPC**. The Python 3.9 scientific-contracts CI assertion was also updated to match the package's actual `requires-python >=3.9` metadata.

**Every-module / every-function policy:** importing a Python module is not testing its functions. The private `hpc_callable_evidence.py --require-all-observed` flag now makes the next integrated CPU acceptance **FAIL** if any named declared Python function or class method (public, private or nested) lacks a freshly measured pytest-executed body line. An accompanying negative regression test confirms incomplete coverage blocks this strict gate. The detailed evidence JSON identifies each unobserved function and source module for targeted test authoring. This still cannot prove full branch coverage, reference numerical accuracy, clinical correctness, safety across unseen datasets, or user-task usability. Lambda-generated/dynamic callables are outside this declaration ledger and must be covered separately where clinically relevant.

**No automatic merge** has taken place. Before Core PR #32 can be considered for technical merging, the *same candidate SHA* must show: zero Python 3.9 screen findings; passing Ruff, mypy, full pytest and coverage quality gate; complete 106-source-module import validation; a complete strict named-callable execution ledger; and passing packaging, notebook and documentation checks. Scientific approval remains separately blocked by independent licensing, gold mappings, real clinical provenance, IRB/DUA and domain-review requirements.


## Actual 21 October 2026 CPU acceptance: 106/106 modules import, full release still blocked

The Herts HPC integrated CPU job **2498833** at private core commit `228ee2696fd60a581dc5c83a5be8ac34bbe0ec98` ended **FAILED 1:0** after **12 minutes 38 seconds**. Its report recorded **17 PASS**, **three FAIL** and **two NOT_RUN** phases.

- The recursively discovered Python module import gate achieved **106/106 PASS**, up from 101/106. This is not evidence that each function or each scientific branch executed.
- PASS: Python 3.9 compatibility, isolated dependency audit, targeted regression tests, source package provenance, ten synthetic adaptation families, 100K-row synthetic scale test, three Kaggle SHA-256 checks and all three original-quarantine schema profiles.
- FAIL: `full_pytest`, `quick_quality`, and `full_quality`; their individual logs and root causes were **not** included in this summary.
- NOT_RUN: strict per-function execution ledger (no fresh coverage file because the quick quality gate exited early) and independent expert-approved gold-mapping matrix.

The private core acceptance runner was improved *after that run* so `full_pytest` independently produces coverage JSON within the unique per-job private report directory and the strict per-function ledger reads it **before** the subsequent lint/type-quality sequence. A new regression test guards this evidence ordering. It will still fail acceptance if tests or declared function execution remain incomplete; scientific correctness is not inferred from code coverage. This change has **not yet been verified on HPC**.

**Merge sequencing matters:** The private Core PR stack is adaptive platform **#25 → scientific integrity #27 → Python 3.9 HPC #30 → final Kaggle/HPC #32**. Each is still draft and unmerged; PR #32 does not target `main` directly. All current and combined final target checks need verified success before a controlled integration to main can be recommended.

Existing `full_pytest.log`, `quick_quality.log` and `full_quality.log` from job 2498833 are the next evidence to retrieve before another CPU submission. Even full technical pass would not confer institutional patient-data, IRB/DUA, external gold-mapping or clinical deployment authorization.


## Job 2498833: exact full-suite and mypy failures identified and fixed in private draft

The full logs, beyond the earlier 17-PASS/3-FAIL/2-NOT_RUN phase summary, confirm **four failing pytest cases** in the original 21 October 2026 HPC commit:

- Two Python 3.10-only `zip(strict=True)` invocations remained in **test code**, not application source: three-annotator Fleiss kappa and active-comparator new-user trial. The private branch now uses the tested length-enforcing Python 3.9 `strict_zip` helper in both tests, preserving record alignment.
- Two GitBook documentation tests failed because three new researcher guides had no `docs/SUMMARY.md` sidebar entries. The private source documentation now lists the code-to-documentation evidence, HPC Python 3.9, and Kaggle HPC acceptance pages exactly once.
- Both quick and full quality gates independently passed **Ruff**, then stopped at **mypy**: missing `types-PyYAML` typing stubs in the isolated environment plus nullable-number comparisons in the notebooks 40–55 dynamic control preflight. The branch now declares PyYAML stubs as a development dependency and a fail-closed isolated-environment prerequisite, and explicitly type-narrows notebook controls. Negative tests cover missing, non-numeric, bool and nonfinite control inputs.

The Python 3.9 compatibility scan now covers test files as well as source and scripts; a GitHub CI workflow has been adjusted to run the previously failing contract tests. The new GitHub checks showed failures without retrievable logs, so **CI still needs diagnosis** and the private PR remains **DRAFT/UNMERGED**. These committed changes have **not yet passed Herts HPC**. User action: install the single typing-stubs package into the existing isolated environment on an approved preparation node (not a compute node), then verify static compatibility, Ruff, real mypy and the four previously failed pytest cases before another pinned integrated CPU job.

This fixes demonstrated integration bugs without licensing unreviewed Kaggle/clinical datasets or proving scientific validity. Even a complete named-function body-execution ledger does not test every branch, interpretation, or numerical reference property.

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

Use a Herts-approved storage path and job allocation. The example keeps both data and generated reports **outside** the Git repository.

~~~bash
export THOMASLAB_HPC_ROOT="/beegfs/general/$USER/research_workplace/Projects/thomaslab_hpc"
mkdir -p "$THOMASLAB_HPC_ROOT/core"
cd "$THOMASLAB_HPC_ROOT/core"
git clone git@github.com:appsplorer/thomaslab-core.git
cd thomaslab-core
git fetch origin
git switch main
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

**Resumable staging after the first successful HPC download:** A `DOWNLOADED_CHECKSUM_RECORDED` result is preserved in the private archive directory. Repeating `stage` for that candidate verifies the existing receipt, exact source identity, approved license, safe file types and current SHA-256. A successful cache check reports `ALREADY_STAGED_VERIFIED`, which counts as a successful staging operation **without contacting Kaggle or redownloading**. Changed files, unknown extra files or malformed receipts produce `BLOCK_EXISTING_INTEGRITY_FAILURE` and cannot be overwritten automatically. Use `inventory --id heart_failure_clinical` before `extract`; extraction remains `QUARANTINED_UNREVIEWED` and never creates a gold mapping or scientific approval.

For a gradual pilot, use repeated candidate `--id` flags; for example:

~~~bash
python3.9 scripts/kaggle_hpc.py stage --root "$KAGGLE_ROOT" \
  --id heart_failure_clinical --id medical_insurance \
  --id breast_cancer_wisconsin --max-mib 512 --execute
~~~

Even with successful caching, the complete batch returns a nonzero code if any selected candidate has an unverified license, absent Kaggle handle, unexpected metadata or unsafe payload. **Cached source integrity does not independently refresh the provider's license/version metadata**; check current source terms before later redistribution.

**CC BY 4.0 name normalization:** Kaggle's dataset metadata may describe the open license as `Attribution 4.0 International (CC BY 4.0)`, while the benchmark requires canonical `CC-BY-4.0`. The downloader recognizes **only that explicitly verified label** as an alias, preserves both the original and canonical license names in its receipt, and continues to block noncommercial, ShareAlike, NoDerivatives, unknown or ambiguous license labels. Users do not need to request a new CC BY license; they must review and follow the dataset's attribution terms. For example, [Heart Failure Prediction](https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data) explicitly requests credit to Davide Chicco and Giuseppe Jurman (BMC Medical Informatics and Decision Making, 2020); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) sets the reuse conditions. A copyright license is not an IRB/DUA or patient-privacy approval.

**Expected blocking cases are not bugs.** Kaggle licenses such as unknown, "other", copyright-authors and CC BY-NC-SA are not automatically allowed by the acquisition policy. A candidate whose preferred file is not found must be corrected after running `kaggle datasets files <owner/slug>`. Large BRFSS files may exceed 512 MiB even individually. The size limit is verified *after* the Kaggle CLI returns; use project quota and site transfer limits before downloading a potentially large file. Never launch bulk downloads on Slurm compute nodes if the institution requires a designated transfer node.

A source distributed through Kaggle does not automatically count as an independent dataset. Check original provenance and overlap/duplicate cohort membership, and preserve required attribution.

## Kaggle CLI 1.7.x metadata compatibility

A successful CLI exit code is not proof that `dataset-metadata.json` contains a valid object. Some installations or dataset endpoints may return a JSON **string** or other non-object value. The downloader now reads object-shaped metadata, accepts one additional encoding layer **only when it resolves to an object**, and reports `BLOCK_METADATA_SHAPE` otherwise. For Kaggle 1.7.4.5 server metadata, an absent `id` is expected when **both** `ownerUser` and `datasetSlug` are present. The downloader reconstructs their owner/dataset reference for **comparison only** and must match the requested Kaggle handle exactly. If an `id` is also present, both formats must agree. No missing owner, dataset slug or license is fabricated.

If you observe `BLOCK_METADATA_SHAPE`, run this diagnostic in the HPC login or approved transfer node without printing the metadata body or any credentials:

~~~bash
DIAG_DIR="$THOMASLAB_HPC_ROOT/datasets/kaggle/metadata/heart-failure-debug"
mkdir -p "$DIAG_DIR"
chmod 700 "$DIAG_DIR"
kaggle datasets metadata andrewmvd/heart-failure-clinical-data -p "$DIAG_DIR"
python3.9 - "$DIAG_DIR/dataset-metadata.json" <<'PY'
import json, sys
from pathlib import Path
p = Path(sys.argv[1])
obj = json.loads(p.read_text(encoding="utf-8"))
print("outer_type:", type(obj).__name__)
print("outer_keys:", sorted(obj) if isinstance(obj, dict) else "not-object")
if isinstance(obj, str):
    try:
        nested = json.loads(obj)
        print("nested_type:", type(nested).__name__)
        print("nested_keys:", sorted(nested) if isinstance(nested, dict) else "not-object")
    except (ValueError, TypeError):
        print("nested_type: not-valid-json-object")
PY
~~~

Share only the printed **types/keys**, not the raw metadata, Kaggle token, dataset rows or response text. If the data is genuinely not an object, leave the dataset blocked until the CLI/provider response is understood. The bulk staging command now returns one status per candidate even when another candidate is blocked; its process exit remains nonzero until all requested candidates pass.

## Real HPC incremental verification and license triage (21 October 2026)

At exact Python 3.9 HPC commit `6e8f88470a6288ee509d8357b48800f001780c5d`, 55 targeted tests passed. The user verified the first Kaggle source:

- `heart_failure_clinical`: `INTEGRITY_PASS`; `ALREADY_STAGED_VERIFIED` without redownloading; reviewed-area extract `QUARANTINED_UNREVIEWED` with selected-file SHA-256. These are **software/integrity results**, not clinical method approval.
- `medical_insurance`: metadata declared `DbCL-1.0`; acquisition blocked pending source-specific review.
- `heart_failure_fusion`: metadata declared `ODbL-1.0`; acquisition blocked pending source-specific review.
- `breast_cancer_wisconsin`: `BLOCK_SOURCE_ID_MISMATCH`; do not assume a Kaggle alias or owner rename without investigating what the API actually returns.

The private ingestion CLI now provides a **metadata-only** diagnostic:

~~~bash
export KAGGLE_ROOT="$THOMASLAB_HPC_ROOT/datasets/kaggle"
python3.9 scripts/kaggle_hpc.py metadata --root "$KAGGLE_ROOT" \
  --id breast_cancer_wisconsin

# Optional: inspect the expected handles and observed license flags
python3.9 scripts/kaggle_hpc.py metadata --root "$KAGGLE_ROOT" \
  --id medical_insurance --id heart_failure_fusion
~~~

This CLI command **does not download dataset bytes**. It prints a bounded set of public dataset-identity fields (`expected_source`, `observed_owner`, `observed_dataset_slug`, `observed_full_id`), a license name, and identity/license checks. It never prints a free-text Kaggle response, access token or data rows. A mismatch remains blocked. Correct the candidate registry **only** after confirming a canonical provider handle and original source provenance; never force an alias.

### Database contents license versus database license

The [Database Contents License v1.0](https://opendatacommons.org/licenses/dbcl/1-0/) grants rights over contents and references the separate database/ODbL rights. `DbCL-1.0` alone in Kaggle metadata does not establish all applicable dataset/database licensing.

The [Open Database License 1.0](https://opendatacommons.org/licenses/odbl/1-0/) generally permits database reuse subject to **attribution** and obligations associated with publicly used derivative databases. These should be reviewed before redistribution or publication, even when an internal benchmark is contemplated.

Neither license is globally auto-approved by Thomas Lab's downloader. Its `BLOCK_LICENSE_REVIEW_REQUIRED` status includes an official terms link and review scope for these two exact values. The appropriate next action is **named dataset-specific license/provenance review**, including original upstream source and publication/distribution plans. Do not change license identifiers or relabel copies to evade the gate. If these sources cannot be cleared, select other genuinely licensed public datasets and record them as substitutions rather than falsely counting these as accepted.

## Complete 16-candidate metadata triage (HPC observation, 21 October 2026)

The live Kaggle 1.7.4.5 `metadata --limit 16` inspection at core commit `9ff0bbb06e6fb62727be9f6d43a042af49a23892` returned **3 source+base-license matches, 7 identity matches with blocked licenses, 5 unresolved owner identities, and 1 Kaggle CLI metadata failure**. Targeted regression tests passed, but this inventory is not a 16-source acceptance result.

| Metadata classification | Catalog IDs | Action |
|---|---|---|
| Both checks PASS | `heart_failure_clinical`, `movie_ratings_small`, `diabetes_readmissions` | Eligible to attempt source download within quota; inspect actual filenames and cohort provenance first |
| Identity match, license BLOCK | `stroke_prediction`, `heart_failure_fusion`, `medical_insurance`, `medical_appointments`, `cardiovascular_70k`, `covid_19_epidemiology`, `drug_review_text` | Source-specific permissions review; **no automatic bypass** |
| Identity unresolved | `breast_cancer_wisconsin`, `indian_liver`, `credit_default_temporal`, `brfss_surveys`, `cms_hospital_quality` | Inspect provider owner identity field shape; a matching dataset slug alone does not establish the owner |
| Metadata command failure | `pima_diabetes` | Confirm Kaggle CLI exit code / source handle accessibility; remain blocked |

Kaggle's documented dataset metadata supports full `id=owner/dataset` references, while live Kaggle 1.7.4.5 server metadata may use `ownerUser` and `datasetSlug`. A missing or unsupported `ownerUser` can indicate a null, unexpected shape, or other provider behavior; **do not infer an organization-owned dataset from the name alone**.

The updated metadata-only diagnostic now displays `identity_field_types` for a fixed allowlist of public provider metadata keys (such as `ownerUser`, `ownerOrganization` and `id`) and an integer `cli_exit_code` when one is safely available. It does **not** output unknown nested owner values, arbitrary descriptions, HTTP error bodies, tokens, or dataset bytes.

Run after updating the audited core branch:

~~~bash
KAGGLE_ROOT="$THOMASLAB_HPC_ROOT/datasets/kaggle"

# Identify the exact metadata shape of unresolved owners, no data downloads
python3.9 scripts/kaggle_hpc.py metadata --root "$KAGGLE_ROOT" \
  --id breast_cancer_wisconsin --id indian_liver \
  --id credit_default_temporal --id brfss_surveys \
  --id cms_hospital_quality

# Distinguish missing handle/API command failure by sanitized exit code
python3.9 scripts/kaggle_hpc.py metadata --root "$KAGGLE_ROOT" \
  --id pima_diabetes

# After separate provenance and file listing review, pilot the two
# remaining base-allowlisted sources (do not infer clinical validity)
kaggle datasets files rounakbanik/the-movies-dataset
kaggle datasets files brandao/diabetes
python3.9 scripts/kaggle_hpc.py stage --root "$KAGGLE_ROOT" \
  --id movie_ratings_small --id diabetes_readmissions \
  --max-mib 512 --execute
~~~

The `diabetes_readmissions` label is only a candidate hypothesis: do not claim the `brandao/diabetes` repository is the intended 130-hospital readmission corpus until its provenance, field names and selected filename are independently verified. If provider ownership cannot be verified, choose independently documented replacement Kaggle handles. Metadata failure or restrictive license is not evidence of software-module failure.

## Kaggle organization display names and real file listing (October 2026)

A follow-up Herts Python 3.9 run of the previous diagnostics successfully completed targeted tests. The five unresolved `uciml`, `cdc` and `cms` entries all had `ownerUser` of type **string**, but the string failed the owner-slug regex. This suggests provider **display-name versus URL-slug** semantics (for example, Kaggle publicly displays `UCI Machine Learning` for organization `uciml`); **it does not establish the exact metadata values**, so no author/organization aliases or license overrides have been applied.

The private `metadata` diagnostic now includes `owner_display_label` when the string contains only narrowly allowed public name characters. The field `display_label_confirms_owner_slug: false` documents that the label is **not authentication**. Free-text provider metadata, emails, URLs, long/suspicious strings and values mentioning secrets or tokens remain withheld. Source staging still demands an actual full owner/dataset identity match; researcher verification of the Kaggle canonical handle/profile is required before the code can recognize any display-name alias.

Observed dataset-file listing:
- `rounakbanik/the-movies-dataset`: `ratings_small.csv` **2,438,266 bytes** (present). The separately offered `ratings.csv` is **709,550,327 bytes**, and is *not* the selected benchmarking file.
- `brandao/diabetes`: `diabetic_data.csv` **19,159,383 bytes** (present); a second `description.pdf` also exists. The tabular CSV may be staged; the publisher's original upstream provenance, readmission outcome definition and patient privacy still require examination before calling it independent hospital EHR.

The two selected files can be fetched as 2 single-file, checksum-receipted staging operations once quota and institutional transfer-node permission are confirmed:

~~~bash
python3.9 scripts/kaggle_hpc.py stage --root "$KAGGLE_ROOT" \
  --id movie_ratings_small --id diabetes_readmissions \
  --max-mib 64 --execute

# Inspect cached receipt integrity; missing candidates remain NOT_DOWNLOADED
python3.9 scripts/kaggle_hpc.py inventory --root "$KAGGLE_ROOT" \
  --id movie_ratings_small --id diabetes_readmissions
~~~

The metadata-only owner-label investigation and Pima CLI error diagnosis can be re-run safely without data downloads:

~~~bash
python3.9 scripts/kaggle_hpc.py metadata --root "$KAGGLE_ROOT" \
  --id breast_cancer_wisconsin --id indian_liver \
  --id credit_default_temporal --id brfss_surveys \
  --id cms_hospital_quality --id pima_diabetes
~~~

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

## Real HPC three-source checkpoint and quarantined CSV profiling (21 October 2026)

On Herts Python 3.9 at core commit `bc101fea525d57c23fe1c28e381450ecd9391d45`, the targeted Kaggle/regression suite passed; two new public Kaggle sources were staged with SHA-256 receipts and source integrity verified:

| Catalog ID | Kaggle selected file | Downloaded bytes | Staging status |
|---|---|---:|---|
| `movie_ratings_small` | `ratings_small.csv` | 675,002 | `DOWNLOADED_CHECKSUM_RECORDED`; `INTEGRITY_PASS` |
| `diabetes_readmissions` | `diabetic_data.csv` | 3,314,619 | `DOWNLOADED_CHECKSUM_RECORDED`; `INTEGRITY_PASS` |
| `heart_failure_clinical` | `heart_failure_clinical_records_dataset.csv` | 12,239 | Earlier verified download, `INTEGRITY_PASS`, `QUARANTINED_UNREVIEWED` |

The transfer sizes may be **compressed ZIP bytes**; do not call them the CSV sizes, assume the data are clean, or equate the downloader's receipts with scientific validity. Both new files still need extraction to quarantine. The previously unresolved publisher names remain blocked (public owner string does not equal confirmed Kaggle URL slug); Pima metadata CLI exited with code 1.

The private CLI now provides `profile` for **explicitly quarantined CSV/TSV** files. It first verifies the pinned source archive receipt and current SHA-256, quarantined selection and checksum. It then streams CSV records, counting rows and columns and detecting inconsistent row widths, without echoing any row values. Column names that fail a constrained safe-identifier policy are replaced by positional `REDACTED_COLUMN_N`. Any structural PASS remains `SCHEMA_PROFILED_UNREVIEWED`, with independent source, mappings, and clinical semantics **NOT_ASSESSED**.

Run after pulling the feature branch and passing its tests:

~~~bash
# Extract only the previously downloaded, checksum-verified selected files
python3.9 scripts/kaggle_hpc.py extract --root "$KAGGLE_ROOT" \
  --id movie_ratings_small --member ratings_small.csv --execute
python3.9 scripts/kaggle_hpc.py extract --root "$KAGGLE_ROOT" \
  --id diabetes_readmissions --member diabetic_data.csv --execute

# Read-only structural inspection; capped here at 64 MiB per source
python3.9 scripts/kaggle_hpc.py profile --root "$KAGGLE_ROOT" \
  --id heart_failure_clinical --max-mib 64 --execute
python3.9 scripts/kaggle_hpc.py profile --root "$KAGGLE_ROOT" \
  --id movie_ratings_small --max-mib 64 --execute
python3.9 scripts/kaggle_hpc.py profile --root "$KAGGLE_ROOT" \
  --id diabetes_readmissions --max-mib 64 --execute
~~~

The source bytes remain outside Git and public MkDocs. A structural profile is not a gold mapping and does not confirm readmission outcome meanings, patient linkage, survival-censoring semantics or external cohort independence. Expert mapping sign-off and audit-approved storage are still mandatory.

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

Use an authorized CPU partition (the `eng` account and `core32` examples require verification against current HPC policies).

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


## Integrated CPU validation and optional GPU smoke (21 October 2026)

The latest Herts HPC run completed Python 3.9 regression tests and extracted all three Kaggle sources, but produced an important newly observed defect: the heart-failure CSV profiled successfully at **299 rows × 13 columns**, while `ratings_small.csv` and `diabetic_data.csv` returned `BLOCK_SCHEMA_PROFILE_ERROR / UnicodeDecodeError`. Their downloaded payload lengths (675,002 and 3,314,619 bytes) are far below Kaggle's listed CSV lengths, consistent with compressed ZIP envelopes saved by the Kaggle CLI under a `.csv` filename. The exact byte signature has **not yet been independently observed on HPC**; the repair refuses to operate unless ZIP magic, pinned receipt identity, matching source SHA-256, and a unique safe archive member are verified.

The corrected downloader examines ZIP **content**, not only `.zip` suffixes. New archives are safely decompressed into quarantine while the original ZIP byte-for-byte receipt remains intact. For archives already copied into quarantine incorrectly, `kaggle_hpc.py repair --execute` requires an exact originally selected member, preserves the previous quarantine under `reviewed_recovery/<id>/<original_sha256>/`, and reconstructs a new `QUARANTINED_UNREVIEWED` CSV from the verified stage. It never approves the data or bypasses licenses. The original recovery folder is never deleted automatically.

**Run all currently automatable CPU software and dataset-integrity checks in one pinned Slurm allocation.** The new `scripts/hpc_integrated_acceptance.sh` via `slurm/thomaslab_integrated_cpu.sbatch` performs: shell and Python 3.9 preflight, targeted pytest, full pytest, dependency checks, all-module import inventory, ten-family synthetic adaptation, 100,000-row streaming scalability, quick/full software quality gates (including coverage/notebooks/docs where installed), all three Kaggle source integrity checks, optional explicit legacy ZIP repair, and read-only schema profiles. All output is stored in `$THOMASLAB_HPC_ROOT/benchmarks/integrated_acceptance/<run-id>/`, outside Git. No Kaggle network downloads, clinical data rows or credentials are written to reports.

First, on the user-authorized **login/transfer node**, pull latest head and run the lightweight regression test:

~~~bash
cd "$THOMASLAB_HPC_ROOT/core/thomaslab-core"
git switch main
git pull --ff-only
python3.9 -m pytest -q tests/test_kaggle_hpc.py tests/test_kaggle_review_manifest.py
bash -n scripts/hpc_integrated_acceptance.sh slurm/thomaslab_integrated_cpu.sbatch
sinfo -o "%P %a %l %D"
~~~

Then request an **authorized CPU** job, adjusting account/partition/time to locally confirmed limits. Opt in to recovery only when intentional; old quarantines will be preserved, not silently overwritten:

~~~bash
export THOMASLAB_HPC_ROOT="/beegfs/general/$USER/research_workplace/Projects/thomaslab_hpc"
export THOMASLAB_EXPECTED_SHA="$(git rev-parse HEAD)"
export THOMASLAB_PYTHON39=python3.9
export THOMASLAB_FULL=1
export THOMASLAB_REPAIR_MISLABELED=1

sbatch --account=eng --partition=core256 --cpus-per-task=16 \
  --mem=48G --time=08:00:00 --export=ALL \
  slurm/thomaslab_integrated_cpu.sbatch
~~~

If `core256` or `eng` is unavailable for this allocation, verify `sinfo` and account association, then substitute your approved CPU partition/account; do not assume the example can always run. The batch job's stdout announces the exact report folder; the stable `summary.txt` gives `cpu_technical_status` and separately states that scientific validation remains `NOT_ASSESSED`. Missing optional dependencies can produce legitimate failure statuses: the compute job does **not** install packages or access package registries. Install missing approved dependencies in a separate institution-authorized environment preparation step, then rerun at a pinned Git SHA.

**GPU is optional and a separate gate.** The source CSV and standard CPU tests do not require an accelerator. A minimal nonclinical CUDA arithmetic/gradient smoke test is implemented in `scripts/hpc_gpu_smoke.py`; it does not claim to execute every GPU-capable Thomas Lab module or validate clinical models. For the standard `gpu` batch partition, subject to verified authorization:

~~~bash
sbatch --account=eng --partition=gpu --gres=gpu:1 --cpus-per-task=4 \
  --mem=16G --time=01:00:00 --export=ALL \
  slurm/thomaslab_gpu_smoke.sbatch
~~~

The university's `gpu-interactive` partition was described as **interactive-only**, up to **one GPU per user**, **one job per user**, and **12 hours maximum** on a four-GPU node. It is not an authorized five-GPU allocation, and `sbatch` should **not** be used there. If `srun` access is authorized, acquire one interactive GPU:

~~~bash
srun --account=eng --partition=gpu-interactive --gres=gpu:1 \
  --cpus-per-task=4 --mem=16G --time=01:00:00 --pty bash
# Inside the allocated shell, after setting HPC_ROOT, and with torch installed:
mkdir -p "$THOMASLAB_HPC_ROOT/benchmarks/gpu_smoke"
python3.9 scripts/hpc_gpu_smoke.py \
  --output "$THOMASLAB_HPC_ROOT/benchmarks/gpu_smoke/manual-$(date -u +%Y%m%dT%H%M%SZ)-${SLURM_JOB_ID}.json"
~~~

A successful CPU gate means **technical execution only**, not that all independent external datasets have passed, all algorithms are correct, or results are publication-ready. The full 16-case matrix remains `NOT_RUN/BLOCK` until independently approved original sources and named signed gold mappings exist; no synthetic test, GPU smoke or batch-job completion supersedes this boundary.


## First integrated CPU/GPU Slurm execution — outcome audit (21 October 2026)

**Exact audited checkout:** `1994be20b90393db9d6eecc9029501a55579d0f1`. The user provided post-run Slurm accounting and the actual per-phase report summary.

- **GPU job 2493696:** Slurm `COMPLETED 0:0` in standard `gpu` partition, one allocated **NVIDIA A100 80GB PCIe**, CUDA available under **PyTorch 2.8.0+cu128**. Synthetic forward-matrix and backward-gradient tests both passed, max absolute CPU–GPU difference **1.71661376953125e-05**, all gradients finite. This is a **GPU numerical smoke PASS**, **not** full Thomas Lab GPU-module coverage or clinical validation.
- **CPU job 2493645:** Slurm `FAILED 1:0` in `core256`. The `shell_syntax` phase passed and `python39_static` failed with exit 1. **No later CPU phases ran**: full pytest, module imports, scale and synthetic benchmarks, repair, and three CSV profiles are **NOT_RUN**, not FAIL. The uploaded console output does **not** contain the static check's underlying individual file/line findings; these must be read from that existing run's private `python39-static.json` file. The summary correctly reported `cpu_technical_status=FAIL`, and `scientific_validation=NOT_ASSESSED`.

**Runner correction:** Independent phases now continue after a `python39_static` failure, while the overall CPU status retains **FAIL**. Genuine compilation failures and failed targeted Kaggle tests still abort before reading the three reviewed datasets. Do not suppress or relabel Python compatibility findings; use the next report to diagnose and correct them, and rerun the same pinned gate after code fixes. There is **no need to repeat the unchanged GPU smoke**.

The first failed CPU report stores `python39-static.json`, `python39_static.log`, `phases.tsv`, and `summary.txt` in its owner-only `benchmarks/integrated_acceptance/2493645-20261021T180430Z-bT76q5` folder. Read **file, line and issue metadata only**; do not publish configuration paths, secrets or row values. A later successful CPU run cannot approve unreviewed clinical mappings, dataset ownership or research validity.


## Python 3.9 causal matching gate correction (21 October 2026)

The first integrated CPU job's `python39-static.json` was recovered on UH HPC and found **exactly one** source-compatibility failure out of **126 files checked**:

```text
src/thomaslab/causal.py line 438 zip_strict_requires_python310
```

This identified an actual use of `zip(..., strict=True)` inside the causal module's greedy propensity-score matching function `fast_gpu_propensity_matching`. Python 3.9 cannot execute this Python 3.10+ builtin keyword. The code has now been corrected to **verify `len(treated_order) == len(selected) == len(distances)` before regular `zip`**, retaining the fail-closed invariant for truncated or extra matching-kernel outputs. Targeted synthetic tests cover normal NumPy matching and three invalid output-length combinations. No data, clinical criteria or matching thresholds were intentionally changed.

**The fix is committed but not yet validated on UH HPC.** On the current private branch, first run `python3.9 scripts/python39_compat.py` and `python3.9 -m pytest -q tests/test_python39_compat.py tests/test_causal.py tests/test_kaggle_hpc.py tests/test_kaggle_review_manifest.py`. Only if these pass should the integrated CPU batch be resubmitted with the new exact Git SHA. Keep the already passing A100 GPU numerical smoke result; this source fix does not establish full GPU analytical coverage.


## Integrated CPU job 2494199: subprocess source-layout import regression (21 October 2026)

This real UH HPC CPU job at pinned commit `e389ecd55e96d2f99b5e552ca23ee98afd200283` ended `FAILED 1:0` after **12 seconds**. Report phases: `shell_syntax PASS`, `python39_static PASS`, `compile PASS`, `targeted FAIL 1`. The targeted gate had **two failures** in `tests/test_adaptive_benchmark.py`: `test_manifest_cli_records_pending_benchmark_as_not_run` (CLI report missing) and `test_manifest_cli_can_explicitly_allow_incomplete_diagnostic` (CLI unexpectedly exit 1).

Both shared the observed subprocess traceback `ModuleNotFoundError: No module named 'thomaslab'` from `scripts/run_lab_adaptation_benchmark.py` before its benchmark implementation ran. The repo uses a `src/thomaslab` layout: pytest's `pythonpath = ["src"]` setting adds a path inside pytest, but is **not inherited** by an independent Python interpreter started through `subprocess.run`.

**Fix:** Both synthetic subprocess regression tests now inject the exact current repo `src` path into the subprocess `PYTHONPATH`, preserving the rest of their environment. Independently, the integrated CPU runner exports `PYTHONPATH=$ROOT/src` before launching nested CLI scripts and adds a mandatory `package_origin` phase that confirms the subprocess-visible `thomaslab.__init__` is under the pinned working checkout. The import failure never authorized a benchmark or clinical dataset; no gold mapping or scientific results have been assumed.

**Still pending:** New source/test changes must be pulled and run on the actual HPC Python 3.9. First run `python3.9 -m pytest -q tests/test_adaptive_benchmark.py tests/test_kaggle_hpc.py tests/test_kaggle_review_manifest.py` (expect PASS), then run the same unified CPU batch pinned to its new exact Git SHA. If a required dependency such as `lifelines` remains absent, full environment preflight/QA can separately fail; install only approved versions in the designated environment **outside compute nodes**, not by suppressing tests. The earlier A100 GPU synthetic numerical smoke remains PASS; no need to re-run it to correct this import path.


## Isolated Python 3.9 environment after real HPC dependency audit (21 October 2026)

**Supersedes earlier CPU-batch examples using `THOMASLAB_PYTHON39=python3.9` from the login shell.** Real Python 3.9 HPC evidence on the checkout `5a44e89d7f2d259144edf065553d0c541a0c2593` shows all selected causal, compatibility, Kaggle and benchmark tests **passed**, but one lifelines-dependent Cox test was **SKIPPED** because `lifelines` was unavailable. The *shared* `research_env` was not internally dependency consistent: `pip check` reported conflicting version requirements from `botocore/urllib3`, `fastai/torch`, `safe-cvs-tai/pyarrow`, `tabpfn-common-utils/nvidia-ml-py`, and `thinc/numpy`. These are environmental results, not proven scientific-method failures.

The private repository already provides bounded `constraints/python39.txt` including `numpy<2`, `pyarrow<19`, `lifelines>=0.27,<0.30`, a compatible scientific stack, plus `spacy/scispacy` bounds. **Never upgrade/downgrade the shared research environment to force these unrelated packages to coexist.**

Instead, on an **institution-approved environment-preparation node with permitted package-index access and adequate quota**, use `scripts/hpc_prepare_python39_env.sh`. It creates `$THOMASLAB_HPC_ROOT/environments/python39/thomaslab-core-cpu` without inheriting global site-packages or the invoking `PYTHONPATH`. It installs the constrained editable core and dev, docs, notebook and (when opted into full mode) PyTorch model extras. It refuses to download/install inside a Slurm compute allocation. A full environment can consume significant storage and package-index traffic; check policy and quota first.

~~~bash
cd "$THOMASLAB_HPC_ROOT/core/thomaslab-core"
git switch main
git pull --ff-only
export THOMASLAB_HPC_ROOT="${THOMASLAB_HPC_ROOT:?Set approved HPC workspace}"
export THOMASLAB_PREP_FULL=1
# The default base is /usr/bin/python3.9; set THOMASLAB_BASE_PYTHON39
# explicitly if the approved Python 3.9 interpreter lives elsewhere.
bash scripts/hpc_prepare_python39_env.sh
~~~

**Prepare only once** unless dependency versions are intentionally being rebuilt; an interrupted install can leave the private venv incomplete, which the gate will reject. The installer calls `pip check`, and a separate `scripts/hpc_environment_gate.py` ensures true venv isolation, exact interpreter path, required packages, and clean dependency resolution, reporting only metadata. It does not modify clinical data or grant mapping approval.

Then use the exact isolated interpreter for lightweight tests and for all CPU acceptance phases:

~~~bash
export THOMASLAB_VENV="$THOMASLAB_HPC_ROOT/environments/python39/thomaslab-core-cpu"
export THOMASLAB_PYTHON39="$THOMASLAB_VENV/bin/python"
export THOMASLAB_EXPECTED_SHA="$(git rev-parse HEAD)"
export THOMASLAB_FULL=1
export THOMASLAB_REPAIR_MISLABELED=1
"$THOMASLAB_PYTHON39" scripts/hpc_environment_gate.py \
  --expected-venv "$THOMASLAB_VENV" --full
"$THOMASLAB_PYTHON39" -m pytest -q \
  tests/test_hpc_environment_gate.py tests/test_adaptive_benchmark.py \
  tests/test_python39_compat.py tests/test_causal.py \
  tests/test_kaggle_hpc.py tests/test_kaggle_review_manifest.py
sbatch --account=eng --partition=core256 --cpus-per-task=16 \
  --mem=48G --time=08:00:00 --export=ALL \
  slurm/thomaslab_integrated_cpu.sbatch
~~~

The integrated runner now **requires** `THOMASLAB_VENV` and `THOMASLAB_PYTHON39=$THOMASLAB_VENV/bin/python`. Its early `environment_gate` phase rejects missing lifelines and unresolved dependencies before expensive module/scientific processing. This gate is independent of Python syntax, package-origin and numerical tests; no single phase is allowed to substitute for another. If the new package build fails because of institutional network policy or missing compatible wheels, report the installation traceback without modifying the global/shared environment. The previously successful A100 numerical smoke does not need to rerun for this CPU environment change.


## Every-module versus every-function testing: explicit coverage limits

At the environment-preparation checkpoint, the user's isolated Python 3.9 venv was successfully built, including `lifelines 0.29.0`, `numpy 1.26.4`, `pyarrow 18.1.0`, `torch 2.8.0`, and relevant validation packages. `scripts/hpc_environment_gate.py --full` returned `PASS` with `pip_check_exit_code=0`; the six targeted test files executed without a reported failure or skip. Slurm job **2495601 was submitted**, but the log did **not** provide its outcome, phase report or module/coverage conclusions. Never classify a submission as a completed PASS.

**What the integrated acceptance already does:**
- `scripts/hpc_module_audit.py` discovers **all** source-package `.py` modules recursively and imports each in an isolated Python subprocess, counting public functions and methods structurally. Successful import is **not** execution of each callable.
- `scripts/local_quality_gate.py --quick` runs all pytest tests under coverage instrumentation with **84% minimum aggregate source line coverage**, checks top-level public-callable body observation with `scripts/coverage_audit.py`, and runs the 59-notebook guided/synthetic interface smoke suite. Function coverage only proves some body code ran, not every branch, failure case or scientific hypothesis.
- The existing `coverage_audit.py` scans only top-level source modules for *public* functions/methods, so a PASS should not be interpreted as coverage of all nested-package, private or dynamically generated functions.

**New explicit evidence ledger (next commit/run only):** `scripts/hpc_callable_evidence.py` scans `src/thomaslab/**/*.py` recursively, including both top-level and nested-package declared Python functions and class methods (public/private/nested), joins each to fresh pytest coverage records, and writes an immutable `per-function-coverage.json` report under that CPU job's approved `benchmarks/integrated_acceptance/<run-id>` directory. Each named symbol has an actual `BODY_LINE_OBSERVED`, `BODY_NOT_OBSERVED`, `NO_COVERAGE_RECORD` or `NO_EXECUTABLE_BODY` status, plus observed/declared body-line counts. This does not invoke unknown functions; it expressly excludes lambda/runtime-generated callables and makes **no claim of branch, numerical, clinical or mathematical correctness**. The report is generated only if `coverage.json` was freshly produced in the same invocation; no stale coverage from an earlier checkout is accepted.

The new ledger is **not part of the already-submitted job 2495601**. Do not pull changes into a checkout while its pinned Slurm job is running. Retrieve 2495601's `summary.txt`, `phases.tsv`, `module-import.json`, and `quick_quality.log`/coverage after it finishes. If full technical outcomes require another rerun, pin the subsequent source SHA and collect the new per-function ledger then. A line of code being reached under synthetic tests is *not* a substitute for independently verified correctness, quantitative benchmark agreement, PHI/DUA authorization, review of dataset meaning or trained scientific experts.


## Integrated CPU job 2495601: real 18/22 technical phases passed, four failed (21 October 2026)

Real UH Slurm `2495601` at commit `f6ce6421eafb6f894db62c6a2b6e2e7556c681b4` completed `FAILED 1:0` after 7m47s. Its `phases.tsv` records **18 PASS**, **4 FAIL**, plus the separately expected `reviewed_gold_matrix NOT_RUN_REQUIRES_NAMED_APPROVAL`.

- PASS: shell, isolated Python3.9 dependency preflight, static/compile, correct source-package origin, targeted suite, pip check, full environment preflight, ten synthetic data families, 100k-row synthetic scalability, all three real Kaggle source checksum inventories, *both* content-aware ZIP quarantine repairs, and *all three* CSV structural profiles. The last three remain `SCHEMA_PROFILED_UNREVIEWED`, not scientifically mapped or IRB-approved.
- FAIL: full pytest (exit 2; full collection/traceback details were **not** supplied), recursive module import (101/106 Python source modules successfully imported), quick quality, full quality. Both quality reports identified Ruff `F401` unused `os` in `scripts/hpc_environment_gate.py` and `I001` import formatting in `tests/test_scientific_input_contracts.py`. These exact issues are now corrected on the draft core branch, and the new callable ledger's own test imports were also reordered for Ruff. Further quality issues may be discovered once Ruff passes.
- Five failed imported module names: `thomaslab.gformula`, `thomaslab.longitudinal_dr`, `thomaslab.causal_robustness`, `thomaslab.adaptive.notebook_groups.groups_32_39`, and `thomaslab.adaptive.notebook_groups.specialist_40_45`. Source inspection found ordinary runtime type assignments `StrategyRule = int | Mapping[int,int] | Callable[...]` in **gformula** and **longitudinal_dr**. Unlike deferred type annotations, these PEP 604 expressions evaluate immediately and are **not supported by Python 3.9**. The last three modules import these two modules. The source has been changed to Python3.9-compatible `typing.Union` aliases; explicit import regression tests cover all five and the static compatibility auditor now checks runtime type union assignments.
- The exact private `full_pytest.log` traceback and module exceptions have **not** yet been obtained, so causal attribution of the four job-phase failures must remain evidence-qualified until reproduction. The module audit now records only bounded Python exception-class names on import failures, never raw stack traces or patient data. Neither `module_import` PASS nor function-line observation establishes full functional or scientific correctness.

**Next:** Before any new `sbatch`, pull draft core HEAD only after `2495601` has finished; rerun `scripts/python39_compat.py`, `python -m ruff check src/thomaslab tests scripts`, focused import/ledger tests, and `python -m pytest --collect-only -q tests` using the isolated `thomaslab-core-cpu/bin/python`. Collect existing `full_pytest.log` terminal section (filtered for ERROR/SyntaxError/TypeError/ImportError). Do not modify the shared `research_env` or download source data. One follow-up CPU run can then test the remaining quality gate stages and produce the new callable execution ledger; old job 2495601 did not include that ledger.

Accept/release gate remains STOP: real Kaggle schema pass is not clinical mapping approval, and 16 independent gold-mapped external datasets / expert researcher trials are still unverified.


## Latest checkpoint: Python 3.9 targeted regressions and strict per-function merge gate

A real UH HPC login-node run at private commit `9d904cb0f5deb1756517db10d9b48cb6541d1e58` confirmed **128 Python source files static compatible** and complete pytest collection, but identified **four lightweight source quality/test failures**: Ruff `UP035` (`Iterator` imported from `typing` rather than `collections.abc`), plus three compatibility-screen regression fixtures which accidentally contained literal `\\n` tokens instead of actual newlines. Their syntax findings were fixture artifacts, not evidence that the earlier causal module repair failed.

All four defects are now corrected on the draft private branch. Furthermore, `.github/workflows/scientific-contracts.yml` had an obsolete package `requires-python == '>=3.10'` assertion despite the actual package requiring `>=3.9`; the assertion was aligned with the source package metadata. These changes still require fresh HPC/CI test execution at their exact new SHA.

**The user's requested all-functions merge requirement is now an explicit fail-closed technical gate.** `hpc_callable_evidence.py --require-all-observed` produces the already-designed per-module/per-function JSON ledger of fresh pytest execution and returns a nonzero status when any named declared source callable has no observed function-body execution. The integrated Slurm acceptance now invokes this strict flag. A unit test verifies a report with missing function execution **blocks** the complete-function gate. This still does not mean every parameter combination/branch, statistical property, numerical reference result or clinical assumption is verified; those are independent validation requirements. In particular, **do not merge** just because an inventory JSON was emitted, because all modules imported, or because average coverage exceeded 84%. The full source-function ledger must show explicit execution evidence for every declared named function to meet the stricter technical standard.

**Safe next checkpoint, no new Slurm allocation yet:** pull the draft Core head and run on the approved isolated `thomaslab-core-cpu/bin/python`: `scripts/python39_compat.py`, `ruff check src/thomaslab tests scripts`, `pytest -q tests/test_python39_compat.py tests/test_hpc_callable_evidence.py tests/test_hpc_module_audit.py`, and `pytest --collect-only -q tests`. If those succeed, submit the unified CPU validation pinned to the new commit to generate and evaluate the full fresh coverage ledger. The previous NVIDIA A100 synthetic arithmetic smoke and three public Kaggle structural profiles passed in earlier runs and need not be repeated separately; they do **not** authorize clinical dataset mapping or publication claims.


## Latest actual CPU checkpoint: job 2498833 (21 October 2026)

The completed UH Herts Slurm CPU job **2498833** ran at exact source SHA `228ee2696fd60a581dc5c83a5be8ac34bbe0ec98`. It finished `FAILED 1:0` after **00:12:38**. Actual phase counts: **17 PASS, 3 FAIL, 2 NOT_RUN**.

- **All 106 of 106 Python modules imported** successfully for the first time; this is import coverage, **not execution of each function**.
- PASS: isolated environment and `pip check`, Python 3.9 screen/compilation, package-origin guard, targeted tests, environment preflight, 10-family synthetic dataset benchmark, 100K-row scale benchmark, integrity and structural profile for `heart_failure_clinical`, `movie_ratings_small`, and `diabetes_readmissions`.
- FAIL: `full_pytest` (exit 1), `quick_quality` (exit 1), `full_quality` (exit 1). **Their individual failure traceback lines were not supplied**, and root causes are not inferred from this summary.
- NOT_RUN: `callable_evidence` because the quality runner produced **no fresh coverage file**, and `reviewed_gold_matrix` because no named independent gold mapping approval was supplied. Those statuses must not be reported as passed.

**Post-run diagnostic improvement on later draft source commit:** The independent `full_pytest` phase now runs with `--cov=thomaslab` and writes `coverage.json` into the *unique approved per-job report directory*. The strict `hpc_callable_evidence.py --require-all-observed` then consumes that file **before the Ruff/mypy quality phases**. The ledger therefore remains available for inspection even if subsequent lint stops quick/full quality; the overall run is still FAIL when tests fail or the strict callable coverage gate fails. A synthetic test locks in this phase ordering and fail-closed behavior. New code has **not been executed on UH HPC yet**.

**Critical integration note:** Core PR #32 currently targets the unmerged Python3.9 compatibility branch (PR #30). PR #30 targets the scientific-integrity branch (PR #27). PR #27 targets the adaptive notebook platform branch (PR #25). PR #25 targets `main`. This four-layer draft PR stack requires an integrated, exact-SHA QA and deliberate merge/rebase sequence. Merging only PR #32 cannot by itself publish all this code to `main`.

For next troubleshooting, inspect the **existing** job directory's `full_pytest.log`, `quick_quality.log`, and `full_quality.log` first (last 100–160 lines and collected failure headlines); do **not** submit a fresh CPU job just to rediscover the same failure. After correcting confirmed defects, pull the latest draft head and rerun strict Python3.9 static, targeted pytest and Ruff; only then schedule another pinned unified CPU job. The three public Kaggle datasets remain `SCHEMA_PROFILED_UNREVIEWED` and cannot substitute for independently reviewed, licensed gold-mapped clinical cohort validation.


## 21 Oct late-HPC audit: job 2498833 full QA root causes and corrections

The previously reported job 2498833 `full_pytest.log`, `quick_quality.log` and `full_quality.log` were recovered. This replaces any earlier generic explanation of that run with concrete evidence:

- **Full pytest**: four failures. `tests/test_annotation_v11.py::test_fleiss_kappa_three_annotators` and `tests/test_target_trial_v15.py::test_active_comparator_new_user_design` used Python 3.10's `zip(..., strict=True)` **inside the TESTS** on Python 3.9 (error `TypeError: zip() takes no keyword arguments`). They now use `thomaslab._compat.strict_zip`, which has explicit unequal-iterable tests and retains fail-closed source-record alignment semantics.
- The other two test failures were `tests/test_gitbook_docs.py::test_gitbook_documentation_coverage_audit_passes` and `::test_gitbook_sidebar_covers_all_researcher_guides_once`, because `docs/SUMMARY.md` omitted `guides/code-documentation-evidence.md`, `guides/hpc-python39.md`, and `guides/kaggle-hpc-acceptance.md`. All three existing guides are now linked exactly once. **No test has been weakened.**
- **Ruff passed** in the real quick/full quality logs. The **mypy** stage instead failed with 16 imports of `yaml` lacking `types-PyYAML` stubs and two operator findings in `src/thomaslab/adaptive/notebook_groups/groups_40_55.py`. The notebook preflight now explicitly narrows optional/malformed values, retaining synthetic-only, bounded controls; new negative tests reject `None`, booleans, strings, and nonfinite values. `types-PyYAML>=6.0.12,<7` is now part of the package's `dev` extra and a required distribution for the isolated HPC environment gate. Installing this approved stub package into the isolated venv must happen **outside** the compute-node allocation; do not disable mypy errors.
- The static Python 3.9 compatibility scan now scans `src/thomaslab`, `scripts`, AND `tests` to detect obsolete builtins in future test changes.
- The Python 3.9 GitHub workflow now includes this draft branch as a push/PR validation target and runs annotation, target-trial and GitBook regression tests on its interpreter matrix. The GitHub checks have reported failures, but job logs were not retrievable through the connected GitHub interface; **do not claim CI PASS**.

All source patches are committed to the **draft, unmerged** private Core feature branch. The latest code and type-stub installation are **not yet verified in UH HPC**. Before Slurm, pull exact SHA, install `types-PyYAML` in the already isolated Python3.9 environment on an institution-approved preparation/login node and re-run Python3.9 scan, Ruff, mypy, focused pytest and GitBook docs audits. Only then submit a new pinned CPU acceptance, which now produces its per-function JSON ledger separately from lint. Existing 106/106 module import PASS, A100 smoke PASS, three Kaggle checksum/schema profiles PASS are valid at their original audited SHAs but do not independently approve this new commit. Scientific gold mappings, real patient datasets and institutional approvals remain separate gates.


## Actual completed CPU job 2498939: 940/955 functions exercised, one technical blocker

Real 21 October 2026 UH Herts `core256` integrated CPU Slurm job **2498939**, source SHA `1ff0a055c43db0c5023b03a953cb92b08fb847ad`, finished `FAILED 1:0` after **00:17:38**. The actual report gives **20 PASS, one FAIL, one NOT_RUN**. In particular **full_pytest PASS, quick_quality PASS, full_quality PASS, module_import PASS (106/106), isolated Python3.9, targeted tests, synthetic ten-family, 100K-row scaling, and all three reviewed-inventory Kaggle integrity/schema profiles PASS**. The sole failed technical phase was `callable_evidence`, because the strict per-function report found **940 function/method bodies observed of 955 inventoried**; 15 were not observed. This is an explicit fail-closed blocker, not a pytest or Ruff failure.

The original 15 were:
- `adaptive.analysis_templates.GuidedExecution.disposition`;
- `adaptive.full_validation.FullValidationReport.to_dict`;
- `adaptive.mapping_workbench.MappingWorkbench.__init__.run` and `MappingWorkbench._safe_submit_button`;
- `adaptive.notebook_catalog._conditional_preflight`, `_conditional_run`, `_existing_run`;
- `adaptive.public_benchmark._open_url`;
- `adaptive.validation.ValidationFinding.__repr__`, `ValidationReport.__repr__`;
- `data.convert_schema_to_omop.has`;
- `models._DeepHitDiscrete.cumulative_incidence`, `_DeepHitDiscrete.__init__` (the **alternate no-PyTorch fallback** class declaration);
- `pgx._marker_haplotype`;
- `transportability._continuous_pipeline`.

**Post-job patch, unverified on Herts HPC:** Added focused tests to existing test modules to call each of these declared functions in its legitimate synthetic or fail-closed context. In particular widget interaction executes a real named mapping review and safely blocks unauthorized approval; the positive widget path leaves the revision `REVIEW_PENDING`. Public HTTP opener is tested through an in-process fake opener with no network access, asserting the no-redirect handler and timeout. The VCF haplotype helper rejects malformed/bool haplotypes. Continuous target-outcome standardization is tested against a known additive synthetic effect and verifies target outcomes are not used. DeepHit cumulative incidence is checked against probability-mass cumsum and normalization, and the optional-dependency fallback initializer is exercised through an isolated source-module import with PyTorch deliberately made unavailable. The other tests assert independently redacted research finding/report representations and conservative legacy/conditional notebook handler semantics. No patient data are included. **The 15-function gap cannot be declared closed until a new instrumented Herts run generates a report showing 955/955 or an explicitly justified refined inventory.**

No source integrity, license, named independent clinical mapping, or scientific-validation gate was weakened. The `reviewed_gold_matrix` remains `NOT_RUN_REQUIRES_NAMED_APPROVAL`: 16 eligible external sources and publication-level clinical validation were not established by this synthetic execution coverage. Even fully observed bodies are NOT evidence of all branches or numerical and scientific soundness.

**Fast next step:** Pull the new feature branch after job 2498939 is finished, use the existing isolated Python3.9 environment and run Ruff, static Python3.9 screen and the focused tests in `test_adaptive_templates`, `test_adaptive_full_validation`, `test_adaptive_mapping_workbench`, `test_adaptive_validation`, `test_notebook_catalog`, `test_adaptive_public_benchmark`, `test_models`, `test_expansion_data`, `test_pgx`, `test_transportability_v24`. Only if these pass, run a new exact-SHA integrated CPU Slurm job. Inspect the *new* `per-function-coverage.json`; do not reuse job 2498939 coverage or claim private Core PR #32 can merge based on prior-SHA technical passes.


## Final integrated CPU acceptance and main-branch integration (22 October 2026)

**Superseding status:** The earlier job `2498939` 940/955-function failure and "next run pending" notes above are *historical checkpoints*, not the latest technical status. The most recent supplied complete Herts job is **2499042** with exact tested development SHA `469c120a81bdf5957911550dea4075fbf577ab61`, Python **3.9.25** and Slurm `COMPLETED 0:0` in **00:16:51**.

The job's `summary.txt` states `cpu_technical_status=PASS`, `scientific_validation=NOT_ASSESSED`, `license_and_identity_overrides=NONE`, `independent_gold_mappings=NOT_ASSESSED`, and `all_sixteen_sources_approved=NO`.

`phases.tsv`: **21 PASS / 0 FAIL / 1 NOT_RUN**. Successful phases: shell syntax, isolated Python 3.9 environment, Python 3.9 static screen, compilation, source-package identity, targeted tests, pip dependency consistency, environment preflight, full pytest, strict callable evidence, complete module import audit, ten-family synthetic adaptation, synthetic scale, quick quality, full quality, and three source-integrity + schema profile pairs (including previously repaired movie-ratings and diabetes archives). The non-executed phase is `reviewed_gold_matrix NOT_RUN_REQUIRES_NAMED_APPROVAL`.

`module-import.json`: **106/106 source modules imported**. The strict `per-function-coverage.json` inventory reports **955/955 declared Python functions and methods with at least one observed executed body line**, of which 671 public and 284 private; **0 unobserved**, across 106 source modules. This represents source-aware execution coverage; it is **not** full branch/path coverage, correctness for all input values, formal proof, reproducibility on every runtime, or clinical/scientific method approval.

**Git integration:** The exact tested source tree (`97f390dbf28e2bca4b08394406a5c148f983f153`) was merged into `main` with a **two-parent, non-squash** merge commit `eca64d3832e967d93ac69a2c83b976ab4624abf8`, retaining all 413 distinct commits from the adaptive, scientific integrity, Python 3.9 and Kaggle/HPC branch chain in accessible commit history. Historical `main` GitBook export was preserved as a separate merge parent and in `backup/main-before-hpc-integration-20261022`, while the working tree uses the HPC-validated source and current private guides. A subsequent **documentation-only** update to the root README and this evidence guide does not alter the tested `src/` package. The canonical public documentation source is [appsplorer/thomaslab-docs](https://github.com/appsplorer/thomaslab-docs), already synchronized with these results.

**Integration waiver and remaining gates:** At the repository owner's explicit instruction, hosted GitHub Actions failures were **not a merge prerequisite**; their Python 3.9/3.10/3.11 conclusions were FAIL at the exact tested source SHA, and their root cause was unavailable in the connected logs. This waiver must remain disclosed and is not represented as a CI PASS. The 16 independently approved external source mappings, five unaffiliated researcher trials, patient-data authorization, expert clinical review and publication-level scientific validation are **not established**. No individual clinical research study or institutional deployment should be approved on the basis of code execution alone.

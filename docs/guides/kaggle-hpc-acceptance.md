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

Use a institution-approved storage path and job allocation. The example keeps both data and generated reports **outside** the Git repository.

~~~bash
export THOMASLAB_HPC_ROOT="/path/to/approved-research/thomaslab_hpc"
mkdir -p "$THOMASLAB_HPC_ROOT/core"
cd "$THOMASLAB_HPC_ROOT/core"
git clone git@github.com:appsplorer/thomaslab-core.git
cd thomaslab-core
git fetch origin
git switch audit/kaggle-hpc-matrix-20261021
git pull --ff-only
bash scripts/setup_thomaslab_hpc.sh

module avail python
python3.9 --version
command -v kaggle
kaggle --version
~~~

Use the existing Kaggle login/CLI environment; never copy \`kaggle.json\`, bearer tokens or institutional patient data into GitHub, published docs, notebooks or SLURM logs. A currently installed Kaggle CLI may use a newer interpreter: the staging code invokes that CLI as a separate executable, while the research virtual environment can remain Python 3.9.

## Inspect and stage the 16 candidate handles

The catalog \`benchmarks/kaggle/candidates.json\` is **discovery-only**: no source or license is preapproved. Current candidate handles cover diabetes, breast cancer, liver disease, stroke, heart failure (two distinct distributions), health insurance, appointment attendance, cardiovascular risk, temporal credit payments, relational movie ratings, COVID surveillance, drug-review NLP, diabetes readmissions, CDC BRFSS and CMS hospital ratings.

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

**Expected blocking cases are not bugs.** Kaggle licenses such as unknown, "other", copyright-authors and CC BY-NC-SA are not automatically allowed by the acquisition policy. A candidate whose preferred file is not found must be corrected after running \`kaggle datasets files <owner/slug>\`. Large BRFSS files may exceed 512 MiB even individually. The size limit is verified *after* the Kaggle CLI returns; use project quota and site transfer limits before downloading a potentially large file. Never launch bulk downloads on Slurm compute nodes if the institution requires a designated transfer node.

A source distributed through Kaggle does not automatically count as an independent dataset. Check original provenance and overlap/duplicate cohort membership, and preserve required attribution.

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

\`$THOMASLAB_HPC_ROOT/benchmarks/gold_mappings/\`

- \`<id>.mapping.json\`: JSON object of actual source-column names to canonical roles, independently verified against original data dictionary and units.
- \`<id>.approval.json\`: named reviewer, source SHA-256 (from \`review-receipt.json\`), source license, reviewed domain, \`status: "APPROVED"\`, and \`independent_source_review: "COMPLETE"\`.

A safe initial approval template is **PENDING**, not approved:

~~~json
{
  "status": "PENDING",
  "reviewer": "",
  "dataset_sha256": "",
  "license": "UNVERIFIED",
  "independent_source_review": "NOT_ASSESSED",
  "domain": ""
}
~~~

Never promote the template automatically. Use a real expert review and the current dataset SHA. Do not infer canonical clinical meaning from lexical similarity alone.

## Execute the full software gate

Use an authorized CPU partition (the \`eng\` account and \`core32\` examples require verification against current HPC policies).

~~~bash
export THOMASLAB_EXPECTED_SHA="$(git rev-parse HEAD)"
export THOMASLAB_INSTALL=1
export THOMASLAB_FULL=0
sbatch --account=eng --partition=core32 --cpus-per-task=8 \
  --mem=32G --time=06:00:00 slurm/python39_validation.sbatch
~~~

The hardened script now includes an independent import audit for every source module and extra Kaggle provenance tests. Its existing 40 guided callbacks, 19 legacy registrations, 10 synthetic families, 100,000-row streaming benchmark, full pytest and 84% coverage checks remain part of the quality gate. Full release mode (\`THOMASLAB_FULL=1\`) also requires the compatible PyTorch/notebook/docs toolchain.

## Run the Kaggle-reviewed matrix in Slurm

After review/approval, run:

~~~bash
export THOMASLAB_EXPECTED_SHA="$(git rev-parse HEAD)"
sbatch --account=eng --partition=core32 --cpus-per-task=8 \
  --mem=32G --time=06:00:00 slurm/kaggle_reviewed_matrix.sbatch
~~~

A complete 16-candidate run fails on any missing, unapproved, unlicensed or mutated source. For **exploratory diagnostics only**, set \`THOMASLAB_ALLOW_PARTIAL_BENCHMARK=1\`: all excluded sources stay explicitly \`NOT_RUN\` or \`BLOCK\`, and partial results cannot establish 16-dataset acceptance.

The manifest uses **exact source SHA-256**, approved source and gold directories, at least 0.80 mapping-fidelity threshold, and fail-closed CLI exit codes. A benchmark PASS measures documented structural agreement, **not** correct pharmacotherapy, PGx guideline interpretation, clinical causal identification, drug-safety effects or external validity.

## What the 16 candidate sources do not cover

Kaggle copies do not establish true FHIR resource coverage, EHR-plus-claims-plus-genotype joins, validated adverse-event phenotypes, prescription exposure semantics, de-identification, specialist causal inference assumptions, or PGx assay and guideline version accuracy. Add specific licensed benchmark data, reviewed gold labels and method-specific synthetic contracts for those components. Multiple Kaggle representations of the same underlying UCI data must not count as independent source evidence.

**Outstanding external release gates:** 15–20 genuinely independent and approved unseen dataset studies, five independent nontechnical researcher task trials, HPC storage/account policy review, privacy/legal/IRB or DUA authorization where needed, manuscript-level numerical baselines, and expert scientific interpretation. Mark unexecuted items \`NOT_RUN\`, not PASS.

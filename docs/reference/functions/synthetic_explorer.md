# S34 — Guided synthetic Jupyter dataset explorer (P5-01)

**Status: local synthetic engineering candidate only. P5-01 remains OPEN.** Private implementation: `thomaslab.adaptive.synthetic_explorer`. No production hospital records, All of Us participant data, MIMIC clinical extracts, source identifiers, source column labels, clinical samples or raw values may be supplied for public rendering.

- `build_synthetic_explorer(manifest, reports, min_rows=11)` accepts the real S12 release manifest validation contract and exactly three matching **completed S01** metadata profiles: `person`, `encounter`, `clinical_event`. It checks schema digests, source-system/release consistency, single dtypes, explicit nonapproval flags and bounded inputs.
- Suppresses all table cards if **any** table has fewer than the minimum count. For otherwise reviewable invented tables, returns only fixed domain names, field counts, a count of *unreviewed* heuristic role hints and a SHA-256 metadata fingerprint; **no source columns or row samples**.
- `render_synthetic_explorer_markdown(view)` produces fixed-label Markdown after hash/status/schema verification. `display_synthetic_explorer(view)` is optional Jupyter/IPython display; there is no Streamlit or network connection.

**Known limits:** metadata can itself be disclosive, and caller-declared `SYNTHETIC` does not independently establish absence of PHI. The SHA-256 view fingerprint detects accidental change, not forgery by a privileged actor. No role-specific IAM/approval or actual clinical mapping workbench has been demonstrated. A production workbench requires institution-authenticated permissions, expert review and independent disclosure checks.

**Evidence:** S34–S36 locally tested together on Python 3.13.5, **70/70 isolated tests passed**; Python 3.9–3.13 grammar parse passed. Local tests used an explicitly compatible S12 surrogate, not the entire private Core dependency environment. Full Core package tests/quality/CI, real site usability and HPC **NOT RUN / NOT PASSED**.

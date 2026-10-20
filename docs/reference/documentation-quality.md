# Documentation quality contract

The private GitBook portal is intended to support independent use by students, researchers, postdocs, and collaborators without requiring the package maintainer to explain every public function manually.

## Coverage target

The documentation contract is source-driven:

- every public module must appear in GitBook navigation;
- every public function and public method must have a callable marker;
- every callable signature must match current source;
- every callable must have parameter guidance and an input contract;
- every callable must describe its return type and output-handling expectations;
- every callable must expose raises/fail-closed behavior and scientific guardrails;
- every callable must include a synthetic implementation template with a concrete call;
- every callable must link to related functions, a workflow guide/notebook range, repository verification, and source code.

The current stable public surface contains 69 public modules and 570 public callables.

## Why examples are synthetic

The function reference never embeds PHI or institution-restricted data. Synthetic examples are deliberately small and are starting points for implementation. Complex clinical, causal, genomic, NLP, temporal, or multisite inputs still require the study-specific review described by the corresponding guide.

The self-service cookbook provides fuller end-to-end examples for the major research domains.

## Hard documentation gates

Run:

~~~powershell
python scripts/generate_gitbook_docs.py --check
python scripts/docs_coverage_audit.py
~~~

The audit fails when a public callable is missing, a signature is stale, an implementation section is absent, parameter guidance is missing, required portal files are absent, a module is missing from GitBook navigation, or a checked internal portal link is broken.

The full repository gate also runs these checks:

~~~powershell
python scripts/local_quality_gate.py
~~~

## Editing policy

Human-edit these files:

- domain guides;
- new-dataset wizard;
- curated examples;
- self-service cookbook;
- governance and research-use pages.

Do not manually maintain generated callable content as the long-term source of truth. When the Python public API changes, regenerate the reference:

~~~powershell
python scripts/generate_gitbook_docs.py
python scripts/generate_gitbook_docs.py --check
python scripts/docs_coverage_audit.py
~~~

Then review the resulting Markdown diff before merge.

## Scientific boundary

Documentation completeness is not scientific validation. A function can be perfectly documented and still be inappropriate for a particular dataset, population, estimand, code system, assay, or endpoint definition. The package therefore keeps ambiguity and unsupported assumptions visible rather than converting documentation convenience into silent scientific guesses.

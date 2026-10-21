# API stability and versioning

Version 1.0.0 establishes the first stable thomaslab-core public-module baseline.

The machine-readable baseline is stored in `api_compatibility.yaml`. Modules listed there correspond to `thomaslab.__all__` and are checked in CI. This gives maintainers an explicit review point whenever the public package surface changes.

## Versioning policy

The 1.x line follows a compatibility-oriented release policy:

- patch releases are for backward-compatible fixes, documentation, and validation improvements;
- minor releases may add backward-compatible capabilities;
- public removals require a recorded deprecation and migration path;
- breaking public API changes require a new major version unless a security or scientific-validity defect makes compatibility unsafe.

The stability promise applies to documented public interfaces. Private helpers, implementation details, notebook outputs, numerical convergence behavior, and third-party dependency internals are not frozen.

## Scientific stability is different from API stability

A stable function signature does not guarantee that a research design is identified, unbiased, transportable, clinically valid, or appropriate for a new dataset. Study assumptions and validation remain the responsibility of the research protocol.

## Deprecations

Every planned public removal must be listed in `deprecations.yaml` with:

- the deprecated symbol;
- the release in which it was deprecated;
- the earliest removal version;
- a replacement or migration path; and
- the reason for the change.

CI validates the deprecation registry and the v1 compatibility manifest together.

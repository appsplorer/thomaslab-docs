# Publishing the public Thomas Lab handbook

The Thomas Lab research handbook is published **only** from the separate, public `appsplorer/thomaslab-docs` repository. The Python library and notebooks remain in private `appsplorer/thomaslab-core`; **public documentation does not expose or install that private repository.**

## Architecture

```text
Private thomaslab-core (software + notebooks)
     | reviewed and sanitized Markdown only
     v
Public thomaslab-docs (static documentation source)
     | automated preflight + mkdocs build --strict
     v
GitHub Pages (HTML + CSS + JavaScript + search index)
     |
     v
https://appsplorer.github.io/thomaslab-docs/
```

A static API index and 69 module-reference documents are copied from the documented public interface. No automated private-to-public sync is configured; updates require editorial review.

## Enable Pages (repository administrator)

1. Open [thomaslab-docs → Settings → Pages](https://github.com/appsplorer/thomaslab-docs/settings/pages).
2. Under **Build and deployment**, set **Source** to **GitHub Actions**.
3. Open the [Actions tab](https://github.com/appsplorer/thomaslab-docs/actions) and inspect **Publish Thomas Lab Research Handbook**.
4. Merge an approved documentation pull request. A push to `main` builds and deploys the public HTML artifact.
5. Verify the Pages link, menus, responsive layout, search, accessibility, internal links and code samples.

**Do not change the private research repository's visibility to publish documentation.**

## Local documentation preview

```bash
git clone https://github.com/appsplorer/thomaslab-docs.git
cd thomaslab-docs
python -m pip install -r requirements-docs.txt
python scripts/check_public_docs.py
mkdocs build --strict
mkdocs serve
```

The rendered site is built solely from `docs/`, `mkdocs.yml` and public documentation requirements; there are no private Python package imports or `mkdocstrings` dependency.

## Quality gates

The GitHub workflow requires a public-documentation content preflight, strict MkDocs build, and checks for essential rendered pages. On a pull request it **builds but does not deploy**; after a reviewed merge into `main`, it publishes with the standard GitHub Pages artifact/deployment actions.

These automated checks only identify common problems. The publication owner must still review each added example for restricted clinical data, institution-specific paths, confidential research methods, credentials and misleading research claims.

## Information governance

- Use **fabricated records** in publicly accessible tutorials.
- Never commit PHI, patient-level EHR, credentials, research access tokens or restricted datasets.
- Publications of function signatures do not imply permission to use source code or institutional data.
- Reproducible software demonstrations do not establish methodological validity, clinical effectiveness, or IRB/DUA authorization.

**Related:** [Public site maintenance](public-site-maintenance.md) · [Research-use boundary](../reference/research-use.md) · [Lab readiness criteria](../guides/lab-validation-release-criteria.md).

# Publishing public documentation with GitHub Pages

The public Thomas Lab site is built with **MkDocs Material**. Documentation is built from approved Markdown in the private `thomaslab-core` repository, but only the rendered static site is published.

```text
Private repository / reviewed branch
  docs/ + mkdocs.yml + tutorials
     ↓ source + secret-pattern checks
  mkdocs build --strict
     ↓ static HTML, CSS, JS and search index only
  GitHub Pages artifact
     ↓ approved GitHub Actions deployment
  Public documentation website
```

## Repository administrator: first-time setup

1. In `appsplorer/thomaslab-core`, open **Settings → Pages**.
2. Select **GitHub Actions** under *Build and deployment*.
3. If Pages is unavailable for the private repository, check the repository owner's eligible GitHub Pro/Team/Enterprise subscription. On a free plan, use a **separate public documentation-only repository**; never make patient-research code public to enable free Pages.
4. Review the documents and branch contents for sensitive material.
5. Open **Actions → Public documentation (MkDocs Material)**. Run the workflow on the intended reviewed branch if necessary; approved pushes to configured branches can also publish.
6. Verify the deployed URL and website search, mobile navigation, code snippets, research-use warnings, and reference pages.

The proposed project-site URL is `https://appsplorer.github.io/thomaslab-core/` **only after** successful deployment. The mere presence of this workflow does not prove that Pages is enabled or live.

## Editorial and local preview workflow

From the private checkout:

```bash
python -m pip install -e ".[docs]"
python scripts/check_public_docs.py
python scripts/generate_gitbook_docs.py --check
python scripts/docs_coverage_audit.py
mkdocs build --strict
mkdocs serve
```

Review the local address printed by `mkdocs serve`. Tutorial code must use synthetic records, describe its expected result, and explain its scientific limitations.

## Confidentiality and content rules

- **Never publish** PHI, clinical notes, row-level institutional extracts, credentials, API tokens or unpublished restricted results.
- Public API pages show signatures and documentation, **not private Python implementation source**.
- Public access to documentation does not grant access to the private GitHub source repository.
- Static-site publishing does not constitute HIPAA compliance, an IRB approval, validation of a clinical study, or approval for medical decision support.
- Legacy GitBook may remain available while visitors migrate, but documentation on the website must not claim an unpublished feature has been institutionally approved.

## Troubleshooting

If a workflow fails, read its **Check public documentation boundaries**, **Build strictly**, and **Deploy** steps. A missing page usually indicates an incorrect navigation path or an unmerged guide. If GitHub returns a Pages permission or plan error, correct the Pages setting/plan rather than adding broad secrets or relaxing repository privacy.
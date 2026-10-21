# Public documentation maintenance

The public site is hosted at https://appsplorer.github.io/thomaslab-docs/ and builds **only from this public repository**, with no checkout of the private research code.

## Editing workflow

1. Open a documentation pull request in `appsplorer/thomaslab-docs`.
2. Add or update Markdown beneath `docs/`; update `mkdocs.yml` navigation for new pages.
3. Include synthetic examples, expected outputs, assumptions and limits.
4. Check source text for credentials, patient-level data, private institutional paths, and unsupported clinical promises.
5. Confirm the PR's **build** job passes with `mkdocs build --strict`.
6. Merge reviewed docs into `main`. GitHub Actions builds and deploys the static site.

The standalone documentation requirements and GitHub Actions checks must work on **Python 3.9 and Python 3.11**. The release-site build interpreter does not determine the private package's Python minimum. See [Python compatibility](../getting-started/python-compatibility.md). Never clone, publish or import the private repository in the public-docs CI.

## Local preview

```bash
python -m pip install -r requirements-docs.txt
python scripts/check_public_docs.py
mkdocs build --strict
mkdocs serve
```

## Notes for collaborators

- This public repository is **documentation only**; API documentation is a static snapshot and may lag the private software branch.
- Source-code installation requires authorized access to the private `thomaslab-core` repository.
- Never include real patient records, PHI, secrets, or restricted research exports in public examples.
- A successful software test is not a methodological, clinical, IRB, or publication approval.
- Changes in the private software repository do **not** auto-publish; synchronize only reviewed Markdown changes here.

## GitHub Pages activation

In the *public* `thomaslab-docs` repository choose **Settings → Pages → Build and deployment → GitHub Actions**. The build must succeed before the URL is treated as live.

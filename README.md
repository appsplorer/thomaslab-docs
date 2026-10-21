# Thomas Lab Research Handbook

Public, static research documentation for the private `thomaslab-core` scientific software and 59 Jupyter research notebooks.

**Documentation:** https://appsplorer.github.io/thomaslab-docs/ (available after GitHub Pages deployment).

This repository contains only publication-reviewed Markdown, generated API reference text, MkDocs configuration, and static website assets. It does **not** contain the Python research package, restricted datasets, patient records, or credentials.

**Core compatibility:** The private **`thomaslab-core/main` now declares Python 3.9 or newer**. The tested code from the HPC development branches was integrated through a non-squash merge preserving the individual commits. The last verified Herts HPC Python 3.9 job passed all 21 executed technical gates; clinical/scientific approval remains separate. See the [Python compatibility and environment matrix](https://appsplorer.github.io/thomaslab-docs/getting-started/python-compatibility/). The public MkDocs site builds independently of the private package. Python support does not imply approval for restricted datasets or all scientific workflows.

### Site development

```bash
python -m pip install -r requirements-docs.txt
python scripts/check_public_docs.py
mkdocs build --strict
mkdocs serve
```

**Safety:** The material is for research and education, not patient care or autonomous clinical decisions. Clinical-data use requires institutional approval, independent scientific review, and an approved research environment.

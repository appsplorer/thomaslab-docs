"""Fail-closed structural checks before public documentation publishing.

Static checks are not a substitute for authorized manual disclosure review.
"""
from __future__ import annotations
import re
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
BANNED = [
    re.compile(r"/beegfs/general/", re.I),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"),
    re.compile(r"(?i)(?:aws_secret_access_key|private[_-]?token)\s*[:=]\s*['\"][A-Za-z0-9/+]{24,}"),
]
REQUIRED = (
    "index.md", "getting-started/first-session.md",
    "tutorials/dataset-onboarding.md", "tutorials/scientific-review.md",
    "guides/notebook-workbench-quickstart.md",
    "getting-started/python-compatibility.md",
    "guides/hpc-python39.md",
    "guides/governed-notebook-use.md",
    "reference/functions/README.md",
)
def main() -> int:
    problems: list[str] = []
    config = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
    if config.get("site_url") != "https://appsplorer.github.io/thomaslab-docs/":
        problems.append("incorrect public site_url")
    if "mkdocstrings" in str(config.get("plugins", "")):
        problems.append("private package code cannot be needed by a public build")
    for path in REQUIRED:
        if not (DOCS / path).is_file():
            problems.append("missing core guide: " + path)
    for path in sorted(DOCS.rglob("*")):
        if path.is_file() and path.suffix in (".md", ".json", ".html", ".yml", ".yaml"):
            data = path.read_text(encoding="utf-8")
            if any(p.search(data) for p in BANNED):
                problems.append("sensitive content pattern: " + str(path.relative_to(ROOT)))
    for path in ("tutorials/dataset-onboarding.md", "tutorials/scientific-review.md", "getting-started/first-session.md"):
        data = (DOCS / path).read_text(encoding="utf-8") if (DOCS / path).exists() else ""
        if "python" not in data or "Expected" not in data:
            problems.append("missing code and expected output: " + path)
    # Prevent a stale minimum-version claim from reappearing on user-facing pages.
    minimum_claims = (
        re.compile(r"requires Python\s*\*\*3\.10 or newer", re.I),
        re.compile(r"Use Python 3\.10 or later", re.I),
        re.compile(r"with Python 3\.10\+", re.I),
    )
    for relative in (
        "getting-started/installation.md",
        "getting-started/first-session.md",
        "getting-started/local-validation.md",
        "guides/notebook-workbench-quickstart.md",
        "guides/pycharm-lab-workbench.md",
    ):
        path = DOCS / relative
        if not path.is_file():
            problems.append("missing compatibility guide: " + relative)
            continue
        body = path.read_text(encoding="utf-8")
        if any(pattern.search(body) for pattern in minimum_claims):
            problems.append("obsolete Python 3.10 minimum: " + relative)
    matrix = DOCS / "getting-started/python-compatibility.md"
    if matrix.is_file():
        content = matrix.read_text(encoding="utf-8")
        if "Python 3.9" not in content or "NOT_ASSESSED" not in content:
            problems.append("compatibility matrix missing Python 3.9 or evidence limits")
    for p in problems:
        print("ERROR:", p)
    if not problems:
        print("PASS: public documentation structure and obvious-secret checks")
    return int(bool(problems))

if __name__ == "__main__":
    raise SystemExit(main())

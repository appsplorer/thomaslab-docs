# Installation

## Supported Python

`thomaslab-core` requires Python **3.10 or newer**.

## Editable research installation

### Windows / PyCharm

```powershell
git clone https://github.com/appsplorer/thomaslab-core.git
cd thomaslab-core
py -3.11 -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev,docs,notebooks]"
```

Set the PyCharm project interpreter to `.venv\\Scripts\\python.exe`.

### Linux / macOS

```bash
git clone https://github.com/appsplorer/thomaslab-core.git
cd thomaslab-core
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev,docs,notebooks]"
```

## Documentation environment

```bash
python -m pip install -e ".[docs]"
mkdocs serve
```

Open the local address printed by MkDocs. The Material theme provides instant search, responsive navigation, and automatic light/dark mode.

## Verify the installation

```bash
python -c "import thomaslab; print(thomaslab.__version__)"
python scripts/environment_preflight.py
python scripts/local_quality_gate.py --quick
```

Before release or manuscript handoff, run the complete local gate:

```bash
python scripts/local_quality_gate.py
```

See [Local validation and PyCharm](local-validation.md) for the full validation sequence and Windows Application Control guidance.

!!! note
    `lifelines` is required for Cox proportional-hazards and Kaplan-Meier utilities. `shap` is required for model explanation. The package declares both as runtime dependencies.

## Optional research extras

Deep-learning functions:

```bash
python -m pip install -e ".[models]"
```

Local BGE/Transformer embedding functions:

```bash
python -m pip install -e ".[llm]"
```

Optional CUDA/CuPy matching backend:

```bash
python -m pip install -e ".[gpu]"
```

The high-performance CPU stack (DuckDB, Polars, PyArrow, and Numba) is part of the standard runtime dependencies.

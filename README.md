# Package Sorter

A simple package categorization system that sorts packages into STANDARD, SPECIAL, or REJECTED categories based on dimensions and mass.

## Function

`sort(w, h, l, m)` categorizes packages based on:
- **Width, Height, Length** (cm)
- **Mass** (kg)

### Categories

- **STANDARD**: Neither bulky nor heavy
- **SPECIAL**: Bulky OR heavy (but not both)
- **REJECTED**: Both bulky AND heavy

### Rules

**Bulky**: Volume ≥ 1,000,000 cm³ OR any dimension ≥ 150 cm  
**Heavy**: Mass ≥ 20 kg

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for Python package management.

### Install uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip
pip install uv
```

## Usage

```python
from main import sort

result = sort(100, 50, 30, 15)  # Returns "STANDARD"
```

## Running Tests

```bash
uv add --dev pytest
uv run pytest test_main.py
```